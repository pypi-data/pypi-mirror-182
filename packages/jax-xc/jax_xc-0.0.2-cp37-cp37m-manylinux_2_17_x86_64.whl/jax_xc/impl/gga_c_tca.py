"""Generated from gga_c_tca.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t2 = r0 + r1
  t4 = (r0 - r1) / t2
  t5 = 0.1e1 + t4
  t7 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t8 = t7 ** 2
  t9 = t5 ** (0.1e1 / 0.3e1)
  t10 = t9 ** 2
  t11 = jnp.where(t5 <= p.zeta_threshold, t8, t10)
  t12 = 0.1e1 - t4
  t14 = t12 ** (0.1e1 / 0.3e1)
  t15 = t14 ** 2
  t16 = jnp.where(t12 <= p.zeta_threshold, t8, t15)
  t18 = t11 / 0.2e1 + t16 / 0.2e1
  t19 = t18 ** 2
  t21 = 3 ** (0.1e1 / 0.3e1)
  t23 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t25 = 4 ** (0.1e1 / 0.3e1)
  t26 = t25 ** 2
  t27 = t2 ** (0.1e1 / 0.3e1)
  t33 = jnp.arctan(0.488827e1 + 0.79425925e0 * t21 * t23 * t26 / t27)
  t37 = t21 ** 2
  t41 = 6 ** (0.1e1 / 0.3e1)
  t42 = t41 ** 2
  t43 = jnp.pi ** 2
  t44 = t43 ** (0.1e1 / 0.3e1)
  t47 = 2 ** (0.1e1 / 0.3e1)
  t50 = jnp.sqrt(s0 + 0.2e1 * s1 + s2)
  t56 = (t42 / t44 * t47 * t50 / t27 / t2) ** 0.23e1
  res = t19 * t18 * (-0.655868e0 * t33 + 0.897889e0) * t37 / t23 * t25 * t27 / (0.1e1 + 0.47121507034422759993e-2 * t56) / 0.3e1
  return res

def unpol(r0, s0, params, p):
  t2 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t3 = t2 ** 2
  t4 = jnp.where(0.1e1 <= p.zeta_threshold, t3, 1)
  t5 = t4 ** 2
  t7 = 3 ** (0.1e1 / 0.3e1)
  t9 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t11 = 4 ** (0.1e1 / 0.3e1)
  t12 = t11 ** 2
  t13 = r0 ** (0.1e1 / 0.3e1)
  t19 = jnp.arctan(0.488827e1 + 0.79425925e0 * t7 * t9 * t12 / t13)
  t23 = t7 ** 2
  t27 = 6 ** (0.1e1 / 0.3e1)
  t28 = t27 ** 2
  t29 = jnp.pi ** 2
  t30 = t29 ** (0.1e1 / 0.3e1)
  t33 = 2 ** (0.1e1 / 0.3e1)
  t34 = jnp.sqrt(s0)
  t40 = (t28 / t30 * t33 * t34 / t13 / r0) ** 0.23e1
  res = t5 * t4 * (-0.655868e0 * t19 + 0.897889e0) * t23 / t9 * t11 * t13 / (0.1e1 + 0.47121507034422759993e-2 * t40) / 0.3e1
  return res