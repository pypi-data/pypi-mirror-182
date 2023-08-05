"""Generated from gga_x_ft97.mpl."""

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
  t35 = 2 ** (0.1e1 / 0.3e1)
  t38 = t20 ** 2
  t39 = t6 ** 2
  t40 = t38 * t39
  t42 = (t20 * t6) ** (0.1e1 / 0.3e1)
  t43 = t42 ** 2
  t44 = s0 * t34
  t55 = params.beta0 + params.beta1 * s0 * t34 * t35 * t40 * t43 / (params.beta2 + t44 * t35 * t40 * t43 / 0.8e1) / 0.8e1
  t58 = t2 ** 2
  t60 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t62 = t58 / t60
  t63 = 4 ** (0.1e1 / 0.3e1)
  t64 = t55 ** 2
  t65 = jnp.arcsinh(t44)
  t66 = t65 ** 2
  t71 = jnp.sqrt(0.9e1 * t44 * t64 * t66 + 0.1e1)
  t81 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1e1 + 0.2e1 / 0.9e1 * t55 * s0 * t34 * t62 * t63 / t71))
  t83 = jnp.where(t10, t15, -t17)
  t84 = jnp.where(t14, t11, t83)
  t85 = 0.1e1 + t84
  t87 = t85 ** (0.1e1 / 0.3e1)
  t89 = jnp.where(t85 <= p.zeta_threshold, t23, t87 * t85)
  t92 = r1 ** 2
  t93 = r1 ** (0.1e1 / 0.3e1)
  t94 = t93 ** 2
  t96 = 0.1e1 / t94 / t92
  t99 = t85 ** 2
  t100 = t99 * t39
  t102 = (t85 * t6) ** (0.1e1 / 0.3e1)
  t103 = t102 ** 2
  t104 = s2 * t96
  t115 = params.beta0 + params.beta1 * s2 * t96 * t35 * t100 * t103 / (params.beta2 + t104 * t35 * t100 * t103 / 0.8e1) / 0.8e1
  t118 = t115 ** 2
  t119 = jnp.arcsinh(t104)
  t120 = t119 ** 2
  t125 = jnp.sqrt(0.9e1 * t104 * t118 * t120 + 0.1e1)
  t135 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t89 * t27 * (0.1e1 + 0.2e1 / 0.9e1 * t115 * s2 * t96 * t62 * t63 / t125))
  res = t81 + t135
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
  t22 = t19 ** 2
  t23 = 0.1e1 / t22
  t25 = t12 ** 2
  t27 = (t12 * r0) ** (0.1e1 / 0.3e1)
  t28 = t27 ** 2
  t29 = t25 * t28
  t38 = params.beta0 + params.beta1 * s0 * t23 * t29 / (params.beta2 + s0 * t23 * t29 / 0.4e1) / 0.4e1
  t40 = 2 ** (0.1e1 / 0.3e1)
  t41 = t40 ** 2
  t42 = r0 ** 2
  t44 = 0.1e1 / t22 / t42
  t47 = t3 ** 2
  t49 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t52 = 4 ** (0.1e1 / 0.3e1)
  t53 = s0 * t41
  t54 = t38 ** 2
  t57 = jnp.arcsinh(t53 * t44)
  t58 = t57 ** 2
  t63 = jnp.sqrt(0.9e1 * t53 * t44 * t54 * t58 + 0.1e1)
  t73 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1e1 + 0.2e1 / 0.9e1 * t38 * s0 * t41 * t44 * t47 / t49 * t52 / t63))
  res = 0.2e1 * t73
  return res