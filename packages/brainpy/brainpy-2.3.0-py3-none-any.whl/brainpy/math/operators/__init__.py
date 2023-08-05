# -*- coding: utf-8 -*-

"""
Operators for brain dynamics modeling.
"""

from . import (
  op_register,
  pre_syn_post,
  surrogate,
  wrap_jax,
  event_matmul,
  sparse_matmul,
)

__all__ = (
    op_register.__all__
    + pre_syn_post.__all__
    + wrap_jax.__all__
    + surrogate.__all__
    + event_matmul.__all__
    + sparse_matmul.__all__
)

from .event_matmul import *
from .sparse_matmul import *
from .op_register import *
from .pre_syn_post import *
from .wrap_jax import *
from .surrogate import *
