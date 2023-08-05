# -*- coding: utf-8 -*-

"""
The ``base`` module for whole BrainPy ecosystem.

- This module provides the most fundamental class ``BrainPyObject``,
  and its associated helper class ``Collector`` and ``ArrayCollector``.
- For each instance of "BrainPyObject" class, users can retrieve all
  the variables (or trainable variables), integrators, and nodes.
- This module also provides a ``FunAsObject`` class to wrap user-defined
  functions. In each function, maybe several nodes are used, and
  users can initialize a ``FunAsObject`` by providing the nodes used
  in the function. Unfortunately, ``FunAsObject`` class does not have
  the ability to gather nodes automatically.
- This module provides ``io`` helper functions to help users save/load
  model states, or share user's customized model with others.
- This module provides ``naming`` tools to guarantee the unique nameing
  for each BrainPyObject object.

Details please see the following.
"""

from brainpy.base.base import *
from brainpy.base.collector import *
from brainpy.base.function import *
from brainpy.base.io import *
from brainpy.base.naming import *

