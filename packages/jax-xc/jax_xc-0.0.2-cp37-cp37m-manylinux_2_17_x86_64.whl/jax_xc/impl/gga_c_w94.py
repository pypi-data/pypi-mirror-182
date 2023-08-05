"""Generated from gga_c_w94.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t2 = r0 + r1
  t4 = (r0 - r1) / t2
  t6 = jnp.where(0.e0 < t4, t4, -t4)
  t8 = jnp.where(0.1e-9 < t6, t6, 0.1e-9)
  t9 = t8 ** (0.1e1 / 0.3e1)
  t10 = t9 ** 2
  t13 = jnp.sqrt(-t10 * t8 + 0.1e1)
  t15 = s0 + 0.2e1 * s1 + s2
  t16 = jnp.sqrt(t15)
  t18 = t2 ** 2
  t19 = t18 ** 2
  t22 = t2 ** (0.1e1 / 0.3e1)
  t26 = (t16 / t22 / t2) ** (0.1e1 / 0.16e2)
  t27 = t26 ** 2
  t35 = 3 ** (0.1e1 / 0.3e1)
  t37 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t39 = 4 ** (0.1e1 / 0.3e1)
  t40 = t39 ** 2
  res = -t13 / (0.118e2 + 0.15067e0 * t27 * t26 * t16 * t15 / t19 + 0.1102e-1 * t15 / t18 / t2 + t35 * t37 * t40 / t22 / 0.4e1)
  return res

def unpol(r0, s0, params, p):
  t2 = jnp.where(0 < 0, 0, 0)
  t4 = jnp.where(0.1e-9 < t2, t2, 0.1e-9)
  t5 = t4 ** (0.1e1 / 0.3e1)
  t6 = t5 ** 2
  t9 = jnp.sqrt(-t6 * t4 + 0.1e1)
  t10 = jnp.sqrt(s0)
  t12 = r0 ** 2
  t13 = t12 ** 2
  t16 = r0 ** (0.1e1 / 0.3e1)
  t20 = (t10 / t16 / r0) ** (0.1e1 / 0.16e2)
  t21 = t20 ** 2
  t29 = 3 ** (0.1e1 / 0.3e1)
  t31 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t33 = 4 ** (0.1e1 / 0.3e1)
  t34 = t33 ** 2
  res = -t9 / (0.118e2 + 0.15067e0 * t21 * t20 * t10 * s0 / t13 + 0.1102e-1 * s0 / t12 / r0 + t29 * t31 * t34 / t16 / 0.4e1)
  return res