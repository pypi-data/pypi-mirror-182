# -*- coding: utf-8 -*-


import warnings
from typing import Tuple

import brainpylib

from brainpy.math.numpy_ops import as_jax
from brainpy.types import ArrayType

__all__ = [
  'event_csr_matvec',
]


def event_csr_matvec(values: ArrayType,
                     indices: ArrayType,
                     indptr: ArrayType,
                     events: ArrayType,
                     shape: Tuple[int, int],
                     transpose: bool = False):
  """The pre-to-post event-driven synaptic summation with `CSR` synapse structure.

  Parameters
  ----------
  values: ArrayType, float
    An array of shape ``(nse,)`` or a float.
  indices: ArrayType
    An array of shape ``(nse,)``.
  indptr: ArrayType
    An array of shape ``(shape[0] + 1,)`` and dtype ``indices.dtype``.
  events: ArrayType
    An array of shape ``(shape[0] if transpose else shape[1],)``
    and dtype ``data.dtype``.
  shape: tuple of int
    A length-2 tuple representing the sparse matrix shape.
  transpose: bool
    A boolean specifying whether to transpose the sparse matrix
    before computing. Default is False.

  Returns
  -------
  out: ArrayType
    A tensor with the shape of ``shape[1]`` if `transpose=True`,
    or ``shape[0]`` if `transpose=False`.
  """
  warnings.warn('Please use ``brainpylib.event_ops.event_csr_matvec()`` instead.', UserWarning)
  events = as_jax(events)
  indices = as_jax(indices)
  indptr = as_jax(indptr)
  values = as_jax(values)
  return brainpylib.event_csr_matvec(values, indices, indptr, events,
                                     shape=shape, transpose=transpose)
