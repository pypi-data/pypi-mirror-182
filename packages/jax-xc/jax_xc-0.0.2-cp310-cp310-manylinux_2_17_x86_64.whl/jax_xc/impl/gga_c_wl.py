"""Generated from gga_c_wl.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t2 = (r0 - r1) ** 2
  t3 = r0 + r1
  t4 = t3 ** 2
  t8 = jnp.sqrt(0.1e1 - t2 / t4)
  t11 = jnp.sqrt(s0 + 0.2e1 * s1 + s2)
  t12 = t3 ** (0.1e1 / 0.3e1)
  t19 = jnp.sqrt(s0)
  t20 = r0 ** (0.1e1 / 0.3e1)
  t25 = jnp.sqrt(s2)
  t26 = r1 ** (0.1e1 / 0.3e1)
  t31 = 3 ** (0.1e1 / 0.3e1)
  t33 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t35 = 4 ** (0.1e1 / 0.3e1)
  t36 = t35 ** 2
  res = t8 * (-0.7486e0 + 0.6001e-1 * t11 / t12 / t3) / (0.360073e1 + 0.9e0 * t19 / t20 / r0 + 0.9e0 * t25 / t26 / r1 + t31 * t33 * t36 / t12 / 0.4e1)
  return res

def unpol(r0, s0, params, p):
  t1 = jnp.sqrt(s0)
  t2 = r0 ** (0.1e1 / 0.3e1)
  t4 = 0.1e1 / t2 / r0
  t8 = 2 ** (0.1e1 / 0.3e1)
  t12 = 3 ** (0.1e1 / 0.3e1)
  t14 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t16 = 4 ** (0.1e1 / 0.3e1)
  t17 = t16 ** 2
  res = (-0.7486e0 + 0.6001e-1 * t1 * t4) / (0.360073e1 + 0.18e1 * t1 * t8 * t4 + t12 * t14 * t17 / t2 / 0.4e1)
  return res