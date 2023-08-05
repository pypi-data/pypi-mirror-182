"""Generated from gga_c_ccdf.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t1 = r0 + r1
  t2 = t1 ** (0.1e1 / 0.3e1)
  t8 = 2 ** (0.1e1 / 0.3e1)
  t9 = 6 ** (0.1e1 / 0.3e1)
  t10 = t9 ** 2
  t12 = jnp.pi ** 2
  t13 = t12 ** (0.1e1 / 0.3e1)
  t17 = jnp.sqrt(s0 + 0.2e1 * s1 + s2)
  t26 = jnp.exp(-params.c4 * (t8 * t10 / t13 * t17 / t2 / t1 / 0.12e2 - params.c5))
  res = params.c1 / (0.1e1 + params.c2 / t2) * (0.1e1 - params.c3 / (0.1e1 + t26))
  return res

def unpol(r0, s0, params, p):
  t1 = r0 ** (0.1e1 / 0.3e1)
  t7 = 2 ** (0.1e1 / 0.3e1)
  t8 = 6 ** (0.1e1 / 0.3e1)
  t9 = t8 ** 2
  t11 = jnp.pi ** 2
  t12 = t11 ** (0.1e1 / 0.3e1)
  t14 = jnp.sqrt(s0)
  t23 = jnp.exp(-params.c4 * (t7 * t9 / t12 * t14 / t1 / r0 / 0.12e2 - params.c5))
  res = params.c1 / (0.1e1 + params.c2 / t1) * (0.1e1 - params.c3 / (0.1e1 + t23))
  return res