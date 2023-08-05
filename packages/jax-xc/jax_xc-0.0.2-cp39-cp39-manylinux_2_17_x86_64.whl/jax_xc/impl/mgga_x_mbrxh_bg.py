"""Generated from mgga_x_mbrxh_bg.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, l0, l1, tau0, tau1, params, p):
  t2 = r0 + r1
  t3 = 0.1e1 / t2
  t6 = 0.2e1 * r0 * t3 <= p.zeta_threshold
  t7 = p.zeta_threshold - 0.1e1
  t10 = 0.2e1 * r1 * t3 <= p.zeta_threshold
  t11 = -t7
  t13 = (r0 - r1) * t3
  t14 = jnp.where(t10, t11, t13)
  t15 = jnp.where(t6, t7, t14)
  t16 = 0.1e1 + t15
  t18 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t19 = t18 * p.zeta_threshold
  t20 = t16 ** (0.1e1 / 0.3e1)
  t22 = jnp.where(t16 <= p.zeta_threshold, t19, t20 * t16)
  t23 = t2 ** (0.1e1 / 0.3e1)
  t26 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t27 = 0.1e1 / t26
  t29 = 4 ** (0.1e1 / 0.3e1)
  t30 = r0 ** (0.1e1 / 0.3e1)
  t31 = t30 ** 2
  t36 = 6 ** (0.1e1 / 0.3e1)
  t37 = t36 ** 2
  t38 = jnp.pi ** 2
  t39 = t38 ** (0.1e1 / 0.3e1)
  t40 = t39 ** 2
  t42 = 0.3e1 / 0.1e2 * t37 * t40
  t43 = r0 ** 2
  t48 = s0 ** 2
  t49 = t43 ** 2
  t55 = 0.46864e0 * tau0 / t31 / r0 - t42 + 0.89e-1 * s0 / t31 / t43 + 0.53e-2 * t48 / t30 / t49 / r0
  t56 = abs(t55)
  t59 = jnp.where(0.e0 < t55, 0.5e-12, -0.5e-12)
  t60 = jnp.where(t56 < 0.5e-12, t59, t55)
  t61 = br89_x(t60)
  t63 = jnp.exp(t61 / 0.3e1)
  t65 = jnp.exp(-t61)
  t75 = jnp.where(r0 <= p.dens_threshold, 0, -t22 * t23 * t27 * t29 * t63 * (0.1e1 - t65 * (0.1e1 + t61 / 0.2e1)) / t61 / 0.4e1)
  t77 = jnp.where(t6, t11, -t13)
  t78 = jnp.where(t10, t7, t77)
  t79 = 0.1e1 + t78
  t81 = t79 ** (0.1e1 / 0.3e1)
  t83 = jnp.where(t79 <= p.zeta_threshold, t19, t81 * t79)
  t86 = r1 ** (0.1e1 / 0.3e1)
  t87 = t86 ** 2
  t92 = r1 ** 2
  t97 = s2 ** 2
  t98 = t92 ** 2
  t104 = 0.46864e0 * tau1 / t87 / r1 - t42 + 0.89e-1 * s2 / t87 / t92 + 0.53e-2 * t97 / t86 / t98 / r1
  t105 = abs(t104)
  t108 = jnp.where(0.e0 < t104, 0.5e-12, -0.5e-12)
  t109 = jnp.where(t105 < 0.5e-12, t108, t104)
  t110 = br89_x(t109)
  t112 = jnp.exp(t110 / 0.3e1)
  t114 = jnp.exp(-t110)
  t124 = jnp.where(r1 <= p.dens_threshold, 0, -t83 * t23 * t27 * t29 * t112 * (0.1e1 - t114 * (0.1e1 + t110 / 0.2e1)) / t110 / 0.4e1)
  res = t75 + t124
  return res

def unpol(r0, s0, l0, tau0, params, p):
  t3 = 0.1e1 <= p.zeta_threshold
  t4 = p.zeta_threshold - 0.1e1
  t6 = jnp.where(t3, -t4, 0)
  t7 = jnp.where(t3, t4, t6)
  t8 = 0.1e1 + t7
  t10 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t12 = t8 ** (0.1e1 / 0.3e1)
  t14 = jnp.where(t8 <= p.zeta_threshold, t10 * p.zeta_threshold, t12 * t8)
  t15 = r0 ** (0.1e1 / 0.3e1)
  t18 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t21 = 4 ** (0.1e1 / 0.3e1)
  t22 = 2 ** (0.1e1 / 0.3e1)
  t23 = t22 ** 2
  t25 = t15 ** 2
  t30 = 6 ** (0.1e1 / 0.3e1)
  t31 = t30 ** 2
  t32 = jnp.pi ** 2
  t33 = t32 ** (0.1e1 / 0.3e1)
  t34 = t33 ** 2
  t38 = r0 ** 2
  t43 = s0 ** 2
  t45 = t38 ** 2
  t51 = 0.46864e0 * tau0 * t23 / t25 / r0 - 0.3e1 / 0.1e2 * t31 * t34 + 0.89e-1 * s0 * t23 / t25 / t38 + 0.106e-1 * t43 * t22 / t15 / t45 / r0
  t52 = abs(t51)
  t55 = jnp.where(0.e0 < t51, 0.5e-12, -0.5e-12)
  t56 = jnp.where(t52 < 0.5e-12, t55, t51)
  t57 = br89_x(t56)
  t59 = jnp.exp(t57 / 0.3e1)
  t61 = jnp.exp(-t57)
  t71 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -t14 * t15 / t18 * t21 * t59 * (0.1e1 - t61 * (0.1e1 + t57 / 0.2e1)) / t57 / 0.4e1)
  res = 0.2e1 * t71
  return res