


import tkinter as T

from typing import Any, Callable, Dict, DefaultDict, List
from collections import defaultdict

from .errors import BindingError


BIND_PREFIX = '_bound_'



class BindingDescriptor:
    """ Descriptor handling the "Model -> Presentation" way of the two-way binding, at runtime.

        The BindingDescriptor.bind(...) classmethod is hacking at runtime the class body of a
        given instance, preserving any preexisting state/behavior (at class or instance level)
        and put in place a way to update the given widget each time the object property is updated.

        - The binding auto update is working on a specific widget instance for a specific instance
          property.
        - If the widget is destroyed, the binding is "unreferenced", but the descriptor stays in
          place on the class body, for the sake of simplicity.
    """

    DESCRIPTOR_SPECIFIC_METHODS_SET = set('__get__ __set__ __delete__'.split())

    inner_descriptor:   Any = None  # None | a descriptor originally on the class at binding time
    patched_property:   str = None  # Property of the class bound with the descriptor
    protected_property: str = None  # Protected property name, added by the descriptor to each
                                    # instance/class, to keep track of the bound property value.

    _bindings:     DefaultDict[Any, Dict[T.Widget,Callable[[Any],None]] ]
        # dict of dicts tracking which instance (or class) is bound to what widget

    _bindings_sec: DefaultDict[T.Widget, List[Any] ]
        # tracks all objects bound to a widget, for proper unsubscription on widget destruction.


    def __init__(self, prop=None):
        self._bindings     = defaultdict(dict)
        self._bindings_sec = defaultdict(list)
        if prop:
            self.__set_name__(None, prop)


    def __set_name__(self, _, prop):
        """ (automatically called during regular "in body" declaration only) """
        self.patched_property = prop
        self.protected_property = BIND_PREFIX + prop


    def __get__(self, obj, kls):
        """ Relay the "reading" operation to the inner descriptor, or extract the protected
            data from the object or the class.
        """
        if self.inner_descriptor:
            out = self.inner_descriptor.__get__(obj,kls)
            return out

        if obj:
            # If the instance was created before the binding, the property access will go through
            # the descriptor, but the protected value doesn't exist yet and must be created from
            # the instance level value, or a possible class level default value:
            instance_data = vars(obj)
            if self.protected_property not in instance_data:

                if self.patched_property in instance_data:   # instance level previous value
                    value = instance_data[ self.patched_property ]

                elif not hasattr(obj.__class__, self.protected_property):
                    raise AttributeError(
                        'Undefined or uninitialized property '+repr(self.patched_property)
                    )
                else:                                           # class level default value exists
                    value = getattr(obj.__class__, self.protected_property)

                setattr(obj, self.protected_property, value)
                return value

        out = getattr(obj or kls, self.protected_property)
        return out


    def __set__(self, obj, value):
        """ Relay the "setting" operation to the inner descriptor, or set the value of the
            protected property on the target (may be an instance or a class).

            REMINDER:
                If the attribute is set at the class level directly, the Descriptor WILL BE LOST!
        """
        if self.inner_descriptor:
            self.inner_descriptor.__set__(obj, value)
        else:
            setattr(obj, self.protected_property, value)

        if obj in self._bindings:
            for cbk in self._bindings[obj].values():
                cbk(value)




    # WEAKREFS!?
    def subscribe(self, obj, widget, two_ways_cbk):
        """ Register the two way bindig for the given association ("model -> GUI way") """
        self._bindings[obj][widget] = two_ways_cbk
        self._bindings_sec[widget].append(obj)


    def unsubscribe(self, obj:Any, widget:T.Widget):
        """ Remove the update callback for the given association from the descriptor register """
        del self._bindings[obj][widget]


    def unsubscribe_on_destroy(self, widget:T.Widget):
        """ specific unsubscription for widgets destruction """
        objs = self._bindings_sec[widget]
        for obj in objs:
            self.unsubscribe(obj, widget)
        objs.clear()
        del self._bindings_sec[widget]





    @classmethod
    def bind(cls,                       # pylint: disable=too-many-locals
             instance:Any,
             prop:str,
             two_ways_cbk:Callable[[Any],None],
             widget:T.Widget
    ) -> 'BindingDescriptor':
        """ Set up the two-way binding logic for the given object/class and widget, meaning:

            - patch the class property with a BindingDescriptor if not already done
            - secure current state of this property to not lose any data
            - set up the callback so that the widget is updated after a property update
            - return the BindingDescriptor so that the widget.destroy method can be
                hacked to trigger unsubscription (this isn't done in the current function
                to avoid to create a lingering scope/callback here with widget and obj).

            NOTE: Support class level binding as well!
        """
        is_cls_level_binding = isinstance(instance, type)

        # pylint: disable-next=unidiomatic-typecheck
        if is_cls_level_binding and type(instance) is type:
            raise BindingError(
                f"Attempt to bind {instance.__name__}.{prop}:\n"
                "Binding a class level property isn't allowed if the class is directly derived "
                "from the builtin type function. An intermediate metaclass has to be defined."
            )

        kls = instance.__class__

        # State of what's currently on the class body and on the instance itself
        instance_attributes   = vars(instance)
        instance_level_value  = instance_attributes.get(prop,None)
        kls_attributes        = vars(kls)
        kls_level_value       = kls_attributes.get(prop,None)

        has_kls_descriptor_properties = set(dir(kls_attributes.get(prop,[])))  \
                                      & cls.DESCRIPTOR_SPECIFIC_METHODS_SET

        is_kls_attribute      = prop in kls_attributes
        is_descriptor         = is_kls_attribute and bool(has_kls_descriptor_properties)
        is_binder_descriptor  = is_descriptor and isinstance(kls_level_value, BindingDescriptor)
        is_kls_level_property = is_kls_attribute and not is_descriptor
        is_instance_level_property = prop in instance_attributes


        # Binder descriptor to use:
        binder = kls_level_value if is_binder_descriptor else cls(prop)


        if not is_binder_descriptor:                           # Class not bound yet
            if is_descriptor:
                binder.inner_descriptor = kls_level_value      # Archive current value/descriptor

            else:
                kls_or_instance_defined  = set(kls_attributes) | set(instance_attributes)
                defined_protected_name   = binder.protected_property in kls_or_instance_defined
                annotated_protected_name = binder.protected_property in getattr(kls,'__annotations__',())

                if defined_protected_name or annotated_protected_name:
                    raise BindingError(
                        f"{binder.protected_property} must be available on the class/instance "
                        "without collisions to put a two-way binding in place."
                    )

                # Prepare class level protected property (backup of the current value)
                if is_kls_level_property:
                    setattr(kls, binder.protected_property, kls_level_value)

                # WARNING: an instance could have overridden the class level definition!
                # So prepare instance level protected property as well, if needed
                if is_instance_level_property:
                    setattr(instance, binder.protected_property, instance_level_value)

            setattr(kls, prop, binder)           # Put the new descriptor in place on the class


        elif is_instance_level_property and binder.protected_property not in instance_attributes:
            # When a BindingDescriptor is already in place on the property but a new instance is
            # given to be patched, it must be ensured that the new object already has it's instance
            # level protected value ready. If not, extract it from the instance __dict__ and put
            # it in place. This situation may occur if the given instance has been created before
            # the first binding, while the binding was done with another instance.
            setattr(instance, binder.protected_property, instance_level_value)


        binder.subscribe(instance, widget, two_ways_cbk)     # Reference the model -> GUI binding
        return binder
