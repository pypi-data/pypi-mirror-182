"""Generated from mgga_x_gx.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable

from ._helper import Heaviside

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
  t29 = 2 ** (0.1e1 / 0.3e1)
  t30 = t2 ** 2
  t32 = 4 ** (0.1e1 / 0.3e1)
  t34 = 0.8e1 / 0.27e2 * t29 * t30 * t32
  t35 = r0 ** (0.1e1 / 0.3e1)
  t36 = t35 ** 2
  t40 = r0 ** 2
  t45 = tau0 / t36 / r0 - s0 / t36 / t40 / 0.8e1
  t46 = 6 ** (0.1e1 / 0.3e1)
  t48 = jnp.pi ** 2
  t49 = t48 ** (0.1e1 / 0.3e1)
  t50 = t49 ** 2
  t51 = 0.1e1 / t50
  t52 = t45 * t46 * t51
  t54 = t46 * t51
  t58 = params.c0 + params.c1 - 0.1e1
  t65 = 0.1e1 - t34
  t70 = 0.5e1 / 0.9e1 * t52
  t71 = 0.1e1 - t70
  t72 = Heaviside(t71)
  t74 = 0.1e1 - params.alphainf
  t81 = Heaviside(-t71)
  t87 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * ((t34 + 0.5e1 / 0.9e1 * t52 * (params.c0 + 0.5e1 / 0.9e1 * params.c1 * t45 * t54) / (0.1e1 + 0.5e1 / 0.9e1 * t58 * t45 * t54) * t65) * t72 + (0.1e1 + t74 * t71 / (0.1e1 + t70)) * t81))
  t89 = jnp.where(t10, t15, -t17)
  t90 = jnp.where(t14, t11, t89)
  t91 = 0.1e1 + t90
  t93 = t91 ** (0.1e1 / 0.3e1)
  t95 = jnp.where(t91 <= p.zeta_threshold, t23, t93 * t91)
  t97 = r1 ** (0.1e1 / 0.3e1)
  t98 = t97 ** 2
  t102 = r1 ** 2
  t107 = tau1 / t98 / r1 - s2 / t98 / t102 / 0.8e1
  t109 = t107 * t46 * t51
  t124 = 0.5e1 / 0.9e1 * t109
  t125 = 0.1e1 - t124
  t126 = Heaviside(t125)
  t134 = Heaviside(-t125)
  t140 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t95 * t27 * ((t34 + 0.5e1 / 0.9e1 * t109 * (params.c0 + 0.5e1 / 0.9e1 * params.c1 * t107 * t54) / (0.1e1 + 0.5e1 / 0.9e1 * t58 * t107 * t54) * t65) * t126 + (0.1e1 + t74 * t125 / (0.1e1 + t124)) * t134))
  res = t87 + t140
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
  t21 = 2 ** (0.1e1 / 0.3e1)
  t22 = t3 ** 2
  t24 = 4 ** (0.1e1 / 0.3e1)
  t26 = 0.8e1 / 0.27e2 * t21 * t22 * t24
  t27 = t21 ** 2
  t29 = t19 ** 2
  t34 = r0 ** 2
  t39 = tau0 * t27 / t29 / r0 - s0 * t27 / t29 / t34 / 0.8e1
  t40 = 6 ** (0.1e1 / 0.3e1)
  t42 = jnp.pi ** 2
  t43 = t42 ** (0.1e1 / 0.3e1)
  t44 = t43 ** 2
  t45 = 0.1e1 / t44
  t46 = t39 * t40 * t45
  t48 = t40 * t45
  t64 = 0.5e1 / 0.9e1 * t46
  t65 = 0.1e1 - t64
  t66 = Heaviside(t65)
  t75 = Heaviside(-t65)
  t81 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * ((t26 + 0.5e1 / 0.9e1 * t46 * (params.c0 + 0.5e1 / 0.9e1 * params.c1 * t39 * t48) / (0.1e1 + 0.5e1 / 0.9e1 * (params.c0 + params.c1 - 0.1e1) * t39 * t48) * (0.1e1 - t26)) * t66 + (0.1e1 + (0.1e1 - params.alphainf) * t65 / (0.1e1 + t64)) * t75))
  res = 0.2e1 * t81
  return res