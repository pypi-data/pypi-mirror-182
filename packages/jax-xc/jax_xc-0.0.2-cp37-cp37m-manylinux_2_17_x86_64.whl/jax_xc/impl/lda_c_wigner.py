"""Generated from lda_c_wigner.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, params, p):
  t2 = (r0 - r1) ** 2
  t3 = r0 + r1
  t4 = t3 ** 2
  t9 = 3 ** (0.1e1 / 0.3e1)
  t11 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t13 = 4 ** (0.1e1 / 0.3e1)
  t14 = t13 ** 2
  t15 = t3 ** (0.1e1 / 0.3e1)
  res = (0.1e1 - t2 / t4) * params.a / (params.b + t9 * t11 * t14 / t15 / 0.4e1)
  return res

def unpol(r0, params, p):
  t1 = 3 ** (0.1e1 / 0.3e1)
  t3 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t5 = 4 ** (0.1e1 / 0.3e1)
  t6 = t5 ** 2
  t7 = r0 ** (0.1e1 / 0.3e1)
  res = params.a / (params.b + t1 * t3 * t6 / t7 / 0.4e1)
  return res