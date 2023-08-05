"""Generated from gga_x_g96.mpl."""

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
  t29 = t2 ** 2
  t31 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t33 = t29 / t31
  t34 = 4 ** (0.1e1 / 0.3e1)
  t35 = jnp.sqrt(s0)
  t36 = r0 ** (0.1e1 / 0.3e1)
  t39 = t35 / t36 / r0
  t40 = jnp.sqrt(t39)
  t49 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1e1 + 0.2e1 / 0.1233e4 * t33 * t34 * t40 * t39))
  t51 = jnp.where(t10, t15, -t17)
  t52 = jnp.where(t14, t11, t51)
  t53 = 0.1e1 + t52
  t55 = t53 ** (0.1e1 / 0.3e1)
  t57 = jnp.where(t53 <= p.zeta_threshold, t23, t55 * t53)
  t59 = jnp.sqrt(s2)
  t60 = r1 ** (0.1e1 / 0.3e1)
  t63 = t59 / t60 / r1
  t64 = jnp.sqrt(t63)
  t73 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t57 * t27 * (0.1e1 + 0.2e1 / 0.1233e4 * t33 * t34 * t64 * t63))
  res = t49 + t73
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
  t21 = t3 ** 2
  t23 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t26 = 4 ** (0.1e1 / 0.3e1)
  t27 = jnp.sqrt(s0)
  t28 = 2 ** (0.1e1 / 0.3e1)
  t32 = t27 * t28 / t19 / r0
  t33 = jnp.sqrt(t32)
  t42 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1e1 + 0.2e1 / 0.1233e4 * t21 / t23 * t26 * t33 * t32))
  res = 0.2e1 * t42
  return res