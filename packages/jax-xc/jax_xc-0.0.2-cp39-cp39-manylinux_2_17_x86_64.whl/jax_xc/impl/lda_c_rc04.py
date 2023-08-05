"""Generated from lda_c_rc04.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, params, p):
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
  res = t19 * t18 * (-0.655868e0 * t33 + 0.897889e0) * t37 / t23 * t25 * t27 / 0.3e1
  return res

def unpol(r0, params, p):
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
  res = t5 * t4 * (-0.655868e0 * t19 + 0.897889e0) * t23 / t9 * t11 * t13 / 0.3e1
  return res