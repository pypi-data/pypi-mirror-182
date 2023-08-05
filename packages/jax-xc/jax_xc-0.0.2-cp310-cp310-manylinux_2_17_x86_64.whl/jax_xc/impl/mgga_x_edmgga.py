"""Generated from mgga_x_edmgga.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, l0, l1, tau0, tau1, params, p):
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
  t29 = 4 ** (0.1e1 / 0.3e1)
  t30 = t2 ** 2
  t32 = jnp.pi ** 2
  t33 = t32 ** (0.1e1 / 0.3e1)
  t35 = t29 * t30 * t33 / 0.9e1
  t36 = 0.1e1 - t35
  t37 = r0 ** (0.1e1 / 0.3e1)
  t38 = t37 ** 2
  t40 = 0.1e1 / t38 / r0
  t42 = r0 ** 2
  t50 = 6 ** (0.1e1 / 0.3e1)
  t52 = t33 ** 2
  t53 = 0.1e1 / t52
  t54 = (tau0 * t40 - s0 / t38 / t42 / 0.8e1 - l0 * t40 / 0.4e1) * t50 * t53
  t55 = 0.5e1 / 0.9e1 * t54
  t57 = 0.39111111111111111111e0 * t54
  t61 = jnp.where(0.e0 < 0.70414204545454545455e0 - t57, -0.14204545454545454545e-3, 0.704e0 - t57)
  t64 = t61 ** 2
  t70 = (0.1e1 - t55) ** 2
  t73 = jnp.sqrt(0.1e1 + 0.495616e0 * t70)
  t75 = jnp.where(-t55 < -0.14205545454545454545e5, -0.1e1 / t61 / 0.2e1 + 0.1e1 / t64 / t61 / 0.8e1, 0.704e0 - t57 + t73)
  t78 = t36 / jnp.pi
  t79 = jnp.sqrt(0.3e2)
  t80 = jnp.sqrt(t75)
  t82 = t36 ** 2
  t86 = 0.1e1 / t82 / t36 * t32 * jnp.pi
  t91 = t79 * (0.59400000000000000006e1 * t82 / t32 - 0.206514e-1)
  t96 = jnp.arcsinh(0.12611295594149683617e-1 * t86 * t91 * (t75 - 0.1e1))
  t107 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (t35 + t36 * t75 / (0.1e1 + 0.44497190922573977694e0 * t78 * t79 * t80 * t96)))
  t109 = jnp.where(t10, t15, -t17)
  t110 = jnp.where(t14, t11, t109)
  t111 = 0.1e1 + t110
  t113 = t111 ** (0.1e1 / 0.3e1)
  t115 = jnp.where(t111 <= p.zeta_threshold, t23, t113 * t111)
  t117 = r1 ** (0.1e1 / 0.3e1)
  t118 = t117 ** 2
  t120 = 0.1e1 / t118 / r1
  t122 = r1 ** 2
  t131 = (tau1 * t120 - s2 / t118 / t122 / 0.8e1 - l1 * t120 / 0.4e1) * t50 * t53
  t132 = 0.5e1 / 0.9e1 * t131
  t134 = 0.39111111111111111111e0 * t131
  t138 = jnp.where(0.e0 < 0.70414204545454545455e0 - t134, -0.14204545454545454545e-3, 0.704e0 - t134)
  t141 = t138 ** 2
  t147 = (0.1e1 - t132) ** 2
  t150 = jnp.sqrt(0.1e1 + 0.495616e0 * t147)
  t152 = jnp.where(-t132 < -0.14205545454545454545e5, -0.1e1 / t138 / 0.2e1 + 0.1e1 / t141 / t138 / 0.8e1, 0.704e0 - t134 + t150)
  t154 = jnp.sqrt(t152)
  t160 = jnp.arcsinh(0.12611295594149683617e-1 * t86 * t91 * (t152 - 0.1e1))
  t171 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t115 * t27 * (t35 + t36 * t152 / (0.1e1 + 0.44497190922573977694e0 * t78 * t79 * t154 * t160)))
  res = t107 + t171
  return res

def unpol(r0, s0, l0, tau0, params, p):
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
  t21 = 4 ** (0.1e1 / 0.3e1)
  t22 = t3 ** 2
  t24 = jnp.pi ** 2
  t25 = t24 ** (0.1e1 / 0.3e1)
  t27 = t21 * t22 * t25 / 0.9e1
  t28 = 0.1e1 - t27
  t29 = 2 ** (0.1e1 / 0.3e1)
  t30 = t29 ** 2
  t32 = t19 ** 2
  t34 = 0.1e1 / t32 / r0
  t37 = r0 ** 2
  t46 = 6 ** (0.1e1 / 0.3e1)
  t48 = t25 ** 2
  t50 = (tau0 * t30 * t34 - s0 * t30 / t32 / t37 / 0.8e1 - l0 * t30 * t34 / 0.4e1) * t46 / t48
  t51 = 0.5e1 / 0.9e1 * t50
  t53 = 0.39111111111111111111e0 * t50
  t57 = jnp.where(0.e0 < 0.70414204545454545455e0 - t53, -0.14204545454545454545e-3, 0.704e0 - t53)
  t60 = t57 ** 2
  t66 = (0.1e1 - t51) ** 2
  t69 = jnp.sqrt(0.1e1 + 0.495616e0 * t66)
  t71 = jnp.where(-t51 < -0.14205545454545454545e5, -0.1e1 / t57 / 0.2e1 + 0.1e1 / t60 / t57 / 0.8e1, 0.704e0 - t53 + t69)
  t75 = jnp.sqrt(0.3e2)
  t76 = jnp.sqrt(t71)
  t78 = t28 ** 2
  t92 = jnp.arcsinh(0.12611295594149683617e-1 / t78 / t28 * t24 * jnp.pi * t75 * (0.59400000000000000006e1 * t78 / t24 - 0.206514e-1) * (t71 - 0.1e1))
  t103 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (t27 + t28 * t71 / (0.1e1 + 0.44497190922573977694e0 * t28 / jnp.pi * t75 * t76 * t92)))
  res = 0.2e1 * t103
  return res