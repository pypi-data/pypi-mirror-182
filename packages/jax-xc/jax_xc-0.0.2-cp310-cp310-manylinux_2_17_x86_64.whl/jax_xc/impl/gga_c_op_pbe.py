"""Generated from gga_c_op_pbe.mpl."""

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
  t41 = 4 ** (0.1e1 / 0.3e1)
  t42 = t36 / t38 * t41
  t43 = 2 ** (0.1e1 / 0.3e1)
  t44 = t31 <= p.zeta_threshold
  t45 = 0.1e1 - t30
  t46 = t45 <= p.zeta_threshold
  t47 = jnp.where(t46, t17, t30)
  t48 = jnp.where(t44, t14, t47)
  t51 = ((0.1e1 + t48) * t2) ** (0.1e1 / 0.3e1)
  t54 = 6 ** (0.1e1 / 0.3e1)
  t55 = jnp.pi ** 2
  t56 = t55 ** (0.1e1 / 0.3e1)
  t57 = t56 ** 2
  t59 = t54 / t57
  t60 = r0 ** 2
  t61 = r0 ** (0.1e1 / 0.3e1)
  t62 = t61 ** 2
  t76 = jnp.where(t31 * t2 / 0.2e1 <= p.dens_threshold, 0, t42 * t43 / t51 / (0.1804e1 - 0.646416e0 / (0.804e0 + 0.91464571985215458336e-2 * t59 * s0 / t62 / t60)) / 0.9e1)
  t81 = jnp.where(t44, t17, -t30)
  t82 = jnp.where(t46, t14, t81)
  t85 = ((0.1e1 + t82) * t2) ** (0.1e1 / 0.3e1)
  t88 = r1 ** 2
  t89 = r1 ** (0.1e1 / 0.3e1)
  t90 = t89 ** 2
  t104 = jnp.where(t45 * t2 / 0.2e1 <= p.dens_threshold, 0, t42 * t43 / t85 / (0.1804e1 - 0.646416e0 / (0.804e0 + 0.91464571985215458336e-2 * t59 * s2 / t90 / t88)) / 0.9e1)
  t105 = t76 + t104
  t107 = jnp.where(t105 == 0.e0, 2.220446049250313e-16, t105)
  t111 = t107 ** 2
  t112 = t111 ** 2
  res = jnp.where(t11, 0, -0.25e0 * (0.1e1 - t20) * t2 * (0.361925846e1 / t107 + 0.5764e0) / (0.320261508740743441e2 / t112 + 0.151911844324290596e2 / t111 / t107 + 0.1801312286343e1 / t111))
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
  t23 = 4 ** (0.1e1 / 0.3e1)
  t24 = t18 / t20 * t23
  t25 = 2 ** (0.1e1 / 0.3e1)
  t26 = t13 <= p.zeta_threshold
  t27 = 0.1e1 - t9
  t28 = t27 <= p.zeta_threshold
  t29 = jnp.where(t28, t7, t9)
  t30 = jnp.where(t26, t6, t29)
  t33 = ((0.1e1 + t30) * r0) ** (0.1e1 / 0.3e1)
  t36 = 6 ** (0.1e1 / 0.3e1)
  t37 = jnp.pi ** 2
  t38 = t37 ** (0.1e1 / 0.3e1)
  t39 = t38 ** 2
  t42 = t25 ** 2
  t44 = r0 ** 2
  t45 = r0 ** (0.1e1 / 0.3e1)
  t46 = t45 ** 2
  t56 = 0.1e1 / (0.1804e1 - 0.646416e0 / (0.804e0 + 0.91464571985215458336e-2 * t36 / t39 * s0 * t42 / t46 / t44))
  t60 = jnp.where(t13 * r0 / 0.2e1 <= p.dens_threshold, 0, t24 * t25 / t33 * t56 / 0.9e1)
  t65 = jnp.where(t26, t7, -t9)
  t66 = jnp.where(t28, t6, t65)
  t69 = ((0.1e1 + t66) * r0) ** (0.1e1 / 0.3e1)
  t75 = jnp.where(t27 * r0 / 0.2e1 <= p.dens_threshold, 0, t24 * t25 / t69 * t56 / 0.9e1)
  t76 = t60 + t75
  t78 = jnp.where(t76 == 0.e0, 2.220446049250313e-16, t76)
  t82 = t78 ** 2
  t83 = t82 ** 2
  res = jnp.where(t5, 0, -0.25e0 * (0.1e1 - t10) * r0 * (0.361925846e1 / t78 + 0.5764e0) / (0.320261508740743441e2 / t83 + 0.151911844324290596e2 / t82 / t78 + 0.1801312286343e1 / t82))
  return res