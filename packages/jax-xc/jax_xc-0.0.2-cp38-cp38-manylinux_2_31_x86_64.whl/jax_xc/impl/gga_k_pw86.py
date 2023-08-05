"""Generated from gga_k_pw86.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t2 = 3 ** (0.1e1 / 0.3e1)
  t3 = t2 ** 2
  t4 = jnp.pi ** (0.1e1 / 0.3e1)
  t6 = t3 * t4 * jnp.pi
  t7 = r0 + r1
  t8 = 0.1e1 / t7
  t11 = 0.2e1 * r0 * t8 <= p.zeta_threshold
  t12 = p.zeta_threshold - 0.1e1
  t15 = 0.2e1 * r1 * t8 <= p.zeta_threshold
  t16 = -t12
  t18 = (r0 - r1) * t8
  t19 = jnp.where(t15, t16, t18)
  t20 = jnp.where(t11, t12, t19)
  t21 = 0.1e1 + t20
  t23 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t24 = t23 ** 2
  t25 = t24 * p.zeta_threshold
  t26 = t21 ** (0.1e1 / 0.3e1)
  t27 = t26 ** 2
  t29 = jnp.where(t21 <= p.zeta_threshold, t25, t27 * t21)
  t30 = t7 ** (0.1e1 / 0.3e1)
  t31 = t30 ** 2
  t33 = 6 ** (0.1e1 / 0.3e1)
  t34 = jnp.pi ** 2
  t35 = t34 ** (0.1e1 / 0.3e1)
  t36 = t35 ** 2
  t38 = t33 / t36
  t39 = r0 ** 2
  t40 = r0 ** (0.1e1 / 0.3e1)
  t41 = t40 ** 2
  t47 = t33 ** 2
  t50 = t47 / t35 / t34
  t51 = s0 ** 2
  t52 = t39 ** 2
  t59 = t34 ** 2
  t60 = 0.1e1 / t59
  t63 = t52 ** 2
  t68 = (0.1e1 + 0.91999999999999999998e-1 * t38 * s0 / t41 / t39 + 0.1609375e-1 * t50 * t51 / t40 / t52 / r0 + 0.86805555555555555555e-4 * t60 * t51 * s0 / t63) ** (0.1e1 / 0.15e2)
  t72 = jnp.where(r0 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t6 * t29 * t31 * t68)
  t74 = jnp.where(t11, t16, -t18)
  t75 = jnp.where(t15, t12, t74)
  t76 = 0.1e1 + t75
  t78 = t76 ** (0.1e1 / 0.3e1)
  t79 = t78 ** 2
  t81 = jnp.where(t76 <= p.zeta_threshold, t25, t79 * t76)
  t83 = r1 ** 2
  t84 = r1 ** (0.1e1 / 0.3e1)
  t85 = t84 ** 2
  t91 = s2 ** 2
  t92 = t83 ** 2
  t101 = t92 ** 2
  t106 = (0.1e1 + 0.91999999999999999998e-1 * t38 * s2 / t85 / t83 + 0.1609375e-1 * t50 * t91 / t84 / t92 / r1 + 0.86805555555555555555e-4 * t60 * t91 * s2 / t101) ** (0.1e1 / 0.15e2)
  t110 = jnp.where(r1 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t6 * t81 * t31 * t106)
  res = t72 + t110
  return res

def unpol(r0, s0, params, p):
  t3 = 3 ** (0.1e1 / 0.3e1)
  t4 = t3 ** 2
  t5 = jnp.pi ** (0.1e1 / 0.3e1)
  t8 = 0.1e1 <= p.zeta_threshold
  t9 = p.zeta_threshold - 0.1e1
  t11 = jnp.where(t8, -t9, 0)
  t12 = jnp.where(t8, t9, t11)
  t13 = 0.1e1 + t12
  t15 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t16 = t15 ** 2
  t18 = t13 ** (0.1e1 / 0.3e1)
  t19 = t18 ** 2
  t21 = jnp.where(t13 <= p.zeta_threshold, t16 * p.zeta_threshold, t19 * t13)
  t22 = r0 ** (0.1e1 / 0.3e1)
  t23 = t22 ** 2
  t25 = 6 ** (0.1e1 / 0.3e1)
  t26 = jnp.pi ** 2
  t27 = t26 ** (0.1e1 / 0.3e1)
  t28 = t27 ** 2
  t31 = 2 ** (0.1e1 / 0.3e1)
  t32 = t31 ** 2
  t34 = r0 ** 2
  t40 = t25 ** 2
  t44 = s0 ** 2
  t46 = t34 ** 2
  t53 = t26 ** 2
  t57 = t46 ** 2
  t62 = (0.1e1 + 0.91999999999999999998e-1 * t25 / t28 * s0 * t32 / t23 / t34 + 0.321875e-1 * t40 / t27 / t26 * t44 * t31 / t22 / t46 / r0 + 0.34722222222222222222e-3 / t53 * t44 * s0 / t57) ** (0.1e1 / 0.15e2)
  t66 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t4 * t5 * jnp.pi * t21 * t23 * t62)
  res = 0.2e1 * t66
  return res