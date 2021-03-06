"""
Modifiers provide convenient mechanisms for modifying and combining
:class:`~revscoring.features.Feature` and constant values into new
:class:`~revscoring.features.Feature`.

.. autofunction:: revscoring.features.modifiers.log

----

.. autofunction:: revscoring.features.modifiers.min
.. autofunction:: revscoring.features.modifiers.max

----

.. autofunction:: revscoring.features.modifiers.add
.. autofunction:: revscoring.features.modifiers.sub
.. autofunction:: revscoring.features.modifiers.mul
.. autofunction:: revscoring.features.modifiers.div

----

.. autofunction:: revscoring.features.modifiers.eq
.. autofunction:: revscoring.features.modifiers.ne
.. autofunction:: revscoring.features.modifiers.gt
.. autofunction:: revscoring.features.modifiers.lt
.. autofunction:: revscoring.features.modifiers.ge
.. autofunction:: revscoring.features.modifiers.le

"""
from .feature import add, div, eq, ge, gt, le, log, lt, max, min, mul, ne, sub
