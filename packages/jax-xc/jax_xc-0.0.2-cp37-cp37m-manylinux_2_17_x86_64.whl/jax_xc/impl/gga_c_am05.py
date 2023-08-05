"""Generated from gga_c_am05.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t1 = 3 ** (0.1e1 / 0.3e1)
  t3 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t5 = 4 ** (0.1e1 / 0.3e1)
  t6 = t5 ** 2
  t7 = r0 + r1
  t8 = t7 ** (0.1e1 / 0.3e1)
  t11 = t1 * t3 * t6 / t8
  t14 = jnp.sqrt(t11)
  t17 = t11 ** 0.15e1
  t19 = t1 ** 2
  t20 = t3 ** 2
  t22 = t8 ** 2
  t25 = t19 * t20 * t5 / t22
  t31 = jnp.log(0.1e1 + 0.16081979498692535067e2 / (0.379785e1 * t14 + 0.8969e0 * t11 + 0.204775e0 * t17 + 0.123235e0 * t25))
  t33 = 0.621814e-1 * (0.1e1 + 0.53425e-1 * t11) * t31
  t34 = r0 - r1
  t35 = t34 ** 2
  t36 = t35 ** 2
  t37 = t7 ** 2
  t38 = t37 ** 2
  t42 = t34 / t7
  t43 = 0.1e1 + t42
  t44 = t43 <= p.zeta_threshold
  t45 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t46 = t45 * p.zeta_threshold
  t47 = t43 ** (0.1e1 / 0.3e1)
  t49 = jnp.where(t44, t46, t47 * t43)
  t50 = 0.1e1 - t42
  t51 = t50 <= p.zeta_threshold
  t52 = t50 ** (0.1e1 / 0.3e1)
  t54 = jnp.where(t51, t46, t52 * t50)
  t56 = 2 ** (0.1e1 / 0.3e1)
  t60 = (t49 + t54 - 0.2e1) / (0.2e1 * t56 - 0.2e1)
  t71 = jnp.log(0.1e1 + 0.32163958997385070134e2 / (0.705945e1 * t14 + 0.1549425e1 * t11 + 0.420775e0 * t17 + 0.1562925e0 * t25))
  t84 = jnp.log(0.1e1 + 0.29608749977793437516e2 / (0.51785e1 * t14 + 0.905775e0 * t11 + 0.1100325e0 * t17 + 0.1241775e0 * t25))
  t85 = (0.1e1 + 0.278125e-1 * t11) * t84
  t93 = jnp.where(t44, p.zeta_threshold, t43)
  t94 = 6 ** (0.1e1 / 0.3e1)
  t95 = params.alpha * t94
  t96 = jnp.pi ** 2
  t97 = t96 ** (0.1e1 / 0.3e1)
  t98 = t97 ** 2
  t99 = 0.1e1 / t98
  t101 = r0 ** 2
  t102 = r0 ** (0.1e1 / 0.3e1)
  t103 = t102 ** 2
  t110 = 0.1e1 / (0.1e1 + t95 * t99 * s0 / t103 / t101 / 0.24e2)
  t115 = jnp.where(t51, p.zeta_threshold, t50)
  t117 = r1 ** 2
  t118 = r1 ** (0.1e1 / 0.3e1)
  t119 = t118 ** 2
  t126 = 0.1e1 / (0.1e1 + t95 * t99 * s2 / t119 / t117 / 0.24e2)
  res = (-t33 + t36 / t38 * t60 * (-0.310907e-1 * (0.1e1 + 0.5137e-1 * t11) * t71 + t33 - 0.19751673498613801407e-1 * t85) + 0.19751673498613801407e-1 * t60 * t85) * (t93 * (t110 + params.gamma * (0.1e1 - t110)) / 0.2e1 + t115 * (t126 + params.gamma * (0.1e1 - t126)) / 0.2e1)
  return res

def unpol(r0, s0, params, p):
  t1 = 3 ** (0.1e1 / 0.3e1)
  t3 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t5 = 4 ** (0.1e1 / 0.3e1)
  t6 = t5 ** 2
  t7 = r0 ** (0.1e1 / 0.3e1)
  t10 = t1 * t3 * t6 / t7
  t13 = jnp.sqrt(t10)
  t16 = t10 ** 0.15e1
  t18 = t1 ** 2
  t19 = t3 ** 2
  t21 = t7 ** 2
  t24 = t18 * t19 * t5 / t21
  t30 = jnp.log(0.1e1 + 0.16081979498692535067e2 / (0.379785e1 * t13 + 0.8969e0 * t10 + 0.204775e0 * t16 + 0.123235e0 * t24))
  t33 = 0.1e1 <= p.zeta_threshold
  t34 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t36 = jnp.where(t33, t34 * p.zeta_threshold, 1)
  t39 = 2 ** (0.1e1 / 0.3e1)
  t54 = jnp.log(0.1e1 + 0.29608749977793437516e2 / (0.51785e1 * t13 + 0.905775e0 * t10 + 0.1100325e0 * t16 + 0.1241775e0 * t24))
  t59 = jnp.where(t33, p.zeta_threshold, 1)
  t61 = 6 ** (0.1e1 / 0.3e1)
  t63 = jnp.pi ** 2
  t64 = t63 ** (0.1e1 / 0.3e1)
  t65 = t64 ** 2
  t68 = t39 ** 2
  t70 = r0 ** 2
  t77 = 0.1e1 / (0.1e1 + params.alpha * t61 / t65 * s0 * t68 / t21 / t70 / 0.24e2)
  res = (-0.621814e-1 * (0.1e1 + 0.53425e-1 * t10) * t30 + 0.19751673498613801407e-1 * (0.2e1 * t36 - 0.2e1) / (0.2e1 * t39 - 0.2e1) * (0.1e1 + 0.278125e-1 * t10) * t54) * t59 * (t77 + params.gamma * (0.1e1 - t77))
  return res