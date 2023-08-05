"""Generated from lda_xc_zlp.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, params, p):
  t2 = (r0 + r1) ** (0.1e1 / 0.3e1)
  t6 = jnp.log(0.1e1 + 0.10555627099250339363e3 / t2)
  res = -0.93222e0 * (0.1e1 - 0.947362e-2 * t6 * t2) * t2
  return res

def unpol(r0, params, p):
  t1 = r0 ** (0.1e1 / 0.3e1)
  t5 = jnp.log(0.1e1 + 0.10555627099250339363e3 / t1)
  res = -0.93222e0 * (0.1e1 - 0.947362e-2 * t5 * t1) * t1
  return res