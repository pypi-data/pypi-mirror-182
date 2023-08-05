"""Generated from gga_x_b86.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t2 = 3 ** (0.1e1 / 0.3e1)
  t3 = jnp.pi ** (0.1e1 / 0.3e1)
  t5 = t2 / t3
  t6 = r0 + r1
  t7 = 0.1e1 / t6
  t10 = 0.2e1 * r0 * t7 <= p.zeta_threshold
  t11 = p.zeta_threshold - 0.1e1
  t14 = 0.2e1 * r1 * t7 <= p.zeta_threshold
  t15 = -t11
  t17 = (r0 - r1) * t7
  t18 = jnp.where(t14, t15, t17)
  t19 = jnp.where(t10, t11, t18)
  t20 = 0.1e1 + t19
  t22 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t23 = t22 * p.zeta_threshold
  t24 = t20 ** (0.1e1 / 0.3e1)
  t26 = jnp.where(t20 <= p.zeta_threshold, t23, t24 * t20)
  t27 = t6 ** (0.1e1 / 0.3e1)
  t30 = r0 ** 2
  t31 = r0 ** (0.1e1 / 0.3e1)
  t32 = t31 ** 2
  t34 = 0.1e1 / t32 / t30
  t38 = (params.gamma * s0 * t34 + 0.1e1) ** params.omega
  t46 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1e1 + params.beta * s0 * t34 / t38))
  t48 = jnp.where(t10, t15, -t17)
  t49 = jnp.where(t14, t11, t48)
  t50 = 0.1e1 + t49
  t52 = t50 ** (0.1e1 / 0.3e1)
  t54 = jnp.where(t50 <= p.zeta_threshold, t23, t52 * t50)
  t57 = r1 ** 2
  t58 = r1 ** (0.1e1 / 0.3e1)
  t59 = t58 ** 2
  t61 = 0.1e1 / t59 / t57
  t65 = (params.gamma * s2 * t61 + 0.1e1) ** params.omega
  t73 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t54 * t27 * (0.1e1 + params.beta * s2 * t61 / t65))
  res = t46 + t73
  return res

def unpol(r0, s0, params, p):
  t3 = 3 ** (0.1e1 / 0.3e1)
  t4 = jnp.pi ** (0.1e1 / 0.3e1)
  t7 = 0.1e1 <= p.zeta_threshold
  t8 = p.zeta_threshold - 0.1e1
  t10 = jnp.where(t7, -t8, 0)
  t11 = jnp.where(t7, t8, t10)
  t12 = 0.1e1 + t11
  t14 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t16 = t12 ** (0.1e1 / 0.3e1)
  t18 = jnp.where(t12 <= p.zeta_threshold, t14 * p.zeta_threshold, t16 * t12)
  t19 = r0 ** (0.1e1 / 0.3e1)
  t22 = 2 ** (0.1e1 / 0.3e1)
  t23 = t22 ** 2
  t24 = r0 ** 2
  t25 = t19 ** 2
  t28 = t23 / t25 / t24
  t32 = (params.gamma * s0 * t28 + 0.1e1) ** params.omega
  t40 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1e1 + params.beta * s0 * t28 / t32))
  res = 0.2e1 * t40
  return res