"""Generated from gga_c_op_g96.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t2 = r0 + r1
  t3 = 0.1e1 / t2
  t4 = (r0 - r1) * t3
  t5 = abs(t4)
  t10 = jnp.logical_and(r0 <= p.dens_threshold, r1 <= p.dens_threshold)
  t11 = jnp.logical_or(0.1e1 - t5 <= p.zeta_threshold, t10)
  t14 = p.zeta_threshold - 0.1e1
  t17 = -t14
  t18 = jnp.where(0.1e1 - t4 <= p.zeta_threshold, t17, t4)
  t19 = jnp.where(0.1e1 + t4 <= p.zeta_threshold, t14, t18)
  t20 = t19 ** 2
  t29 = jnp.where(0.2e1 * r1 * t3 <= p.zeta_threshold, t17, t4)
  t30 = jnp.where(0.2e1 * r0 * t3 <= p.zeta_threshold, t14, t29)
  t31 = 0.1e1 + t30
  t35 = 3 ** (0.1e1 / 0.3e1)
  t36 = t35 ** 2
  t38 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t40 = t36 / t38
  t41 = 4 ** (0.1e1 / 0.3e1)
  t42 = t40 * t41
  t43 = 2 ** (0.1e1 / 0.3e1)
  t44 = t31 <= p.zeta_threshold
  t45 = 0.1e1 - t30
  t46 = t45 <= p.zeta_threshold
  t47 = jnp.where(t46, t17, t30)
  t48 = jnp.where(t44, t14, t47)
  t51 = ((0.1e1 + t48) * t2) ** (0.1e1 / 0.3e1)
  t54 = jnp.sqrt(s0)
  t55 = r0 ** (0.1e1 / 0.3e1)
  t58 = t54 / t55 / r0
  t59 = jnp.sqrt(t58)
  t69 = jnp.where(t31 * t2 / 0.2e1 <= p.dens_threshold, 0, t42 * t43 / t51 / (0.1e1 + 0.2e1 / 0.1233e4 * t40 * t41 * t59 * t58) / 0.9e1)
  t74 = jnp.where(t44, t17, -t30)
  t75 = jnp.where(t46, t14, t74)
  t78 = ((0.1e1 + t75) * t2) ** (0.1e1 / 0.3e1)
  t81 = jnp.sqrt(s2)
  t82 = r1 ** (0.1e1 / 0.3e1)
  t85 = t81 / t82 / r1
  t86 = jnp.sqrt(t85)
  t96 = jnp.where(t45 * t2 / 0.2e1 <= p.dens_threshold, 0, t42 * t43 / t78 / (0.1e1 + 0.2e1 / 0.1233e4 * t40 * t41 * t86 * t85) / 0.9e1)
  t97 = t69 + t96
  t99 = jnp.where(t97 == 0.e0, 2.220446049250313e-16, t97)
  t103 = t99 ** 2
  t104 = t103 ** 2
  res = jnp.where(t11, 0, -0.25e0 * (0.1e1 - t20) * t2 * (0.359628532e1 / t99 + 0.5764e0) / (0.312207199195441936e2 / t104 + 0.149037398922132448e2 / t103 / t99 + 0.1778517305052e1 / t103))
  return res

def unpol(r0, s0, params, p):
  t1 = 0.1e1 <= p.zeta_threshold
  t3 = r0 / 0.2e1 <= p.dens_threshold
  t4 = jnp.logical_and(t3, t3)
  t5 = jnp.logical_or(t1, t4)
  t6 = p.zeta_threshold - 0.1e1
  t7 = -t6
  t8 = jnp.where(t1, t7, 0)
  t9 = jnp.where(t1, t6, t8)
  t10 = t9 ** 2
  t13 = 0.1e1 + t9
  t17 = 3 ** (0.1e1 / 0.3e1)
  t18 = t17 ** 2
  t20 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t22 = t18 / t20
  t23 = 4 ** (0.1e1 / 0.3e1)
  t24 = t22 * t23
  t25 = 2 ** (0.1e1 / 0.3e1)
  t26 = t13 <= p.zeta_threshold
  t27 = 0.1e1 - t9
  t28 = t27 <= p.zeta_threshold
  t29 = jnp.where(t28, t7, t9)
  t30 = jnp.where(t26, t6, t29)
  t33 = ((0.1e1 + t30) * r0) ** (0.1e1 / 0.3e1)
  t36 = jnp.sqrt(s0)
  t38 = r0 ** (0.1e1 / 0.3e1)
  t41 = t36 * t25 / t38 / r0
  t42 = jnp.sqrt(t41)
  t48 = 0.1e1 / (0.1e1 + 0.2e1 / 0.1233e4 * t22 * t23 * t42 * t41)
  t52 = jnp.where(t13 * r0 / 0.2e1 <= p.dens_threshold, 0, t24 * t25 / t33 * t48 / 0.9e1)
  t57 = jnp.where(t26, t7, -t9)
  t58 = jnp.where(t28, t6, t57)
  t61 = ((0.1e1 + t58) * r0) ** (0.1e1 / 0.3e1)
  t67 = jnp.where(t27 * r0 / 0.2e1 <= p.dens_threshold, 0, t24 * t25 / t61 * t48 / 0.9e1)
  t68 = t52 + t67
  t70 = jnp.where(t68 == 0.e0, 2.220446049250313e-16, t68)
  t74 = t70 ** 2
  t75 = t74 ** 2
  res = jnp.where(t5, 0, -0.25e0 * (0.1e1 - t10) * r0 * (0.359628532e1 / t70 + 0.5764e0) / (0.312207199195441936e2 / t75 + 0.149037398922132448e2 / t74 / t70 + 0.1778517305052e1 / t74))
  return res