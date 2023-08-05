"""Generated from gga_c_scan_e0.mpl."""

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
  t89 = t36 / t38 * t60 * (-0.310907e-1 * (0.1e1 + 0.5137e-1 * t11) * t71 + t33 - 0.19751673498613801407e-1 * t85)
  t91 = 0.19751673498613801407e-1 * t60 * t85
  t92 = jnp.log(0.2e1)
  t93 = 0.1e1 - t92
  t94 = jnp.pi ** 2
  t97 = t45 ** 2
  t98 = t47 ** 2
  t99 = jnp.where(t44, t97, t98)
  t100 = t52 ** 2
  t101 = jnp.where(t51, t97, t100)
  t103 = t99 / 0.2e1 + t101 / 0.2e1
  t104 = t103 ** 2
  t105 = t104 * t103
  t112 = 0.1e1 / t93
  t119 = jnp.exp(-(-t33 + t89 + t91) * t112 * t94 / t105)
  t120 = t119 - 0.1e1
  t139 = (0.1e1 + 0.27801896084645508333e-2 * (0.1e1 + 0.25e-1 * t11) / (0.1e1 + 0.4445e-1 * t11) * t112 * t94 / t120 * (s0 + 0.2e1 * s1 + s2) / t8 / t37 * t56 / t104 * t19 / t3 * t5) ** (0.1e1 / 0.4e1)
  t145 = jnp.log(0.1e1 + 0.1e1 * (0.1e1 - 0.1e1 / t139) * t120)
  res = -t33 + t89 + t91 + t93 / t94 * t105 * t145
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
  t32 = 0.621814e-1 * (0.1e1 + 0.53425e-1 * t10) * t30
  t33 = 0.1e1 <= p.zeta_threshold
  t34 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t36 = jnp.where(t33, t34 * p.zeta_threshold, 1)
  t39 = 2 ** (0.1e1 / 0.3e1)
  t54 = jnp.log(0.1e1 + 0.29608749977793437516e2 / (0.51785e1 * t13 + 0.905775e0 * t10 + 0.1100325e0 * t16 + 0.1241775e0 * t24))
  t57 = 0.19751673498613801407e-1 * (0.2e1 * t36 - 0.2e1) / (0.2e1 * t39 - 0.2e1) * (0.1e1 + 0.278125e-1 * t10) * t54
  t58 = jnp.log(0.2e1)
  t59 = 0.1e1 - t58
  t60 = jnp.pi ** 2
  t63 = t34 ** 2
  t64 = jnp.where(t33, t63, 1)
  t65 = t64 ** 2
  t66 = t65 * t64
  t73 = 0.1e1 / t59
  t80 = jnp.exp(-(-t32 + t57) * t73 * t60 / t66)
  t81 = t80 - 0.1e1
  t86 = r0 ** 2
  t99 = (0.1e1 + 0.27801896084645508333e-2 * (0.1e1 + 0.25e-1 * t10) / (0.1e1 + 0.4445e-1 * t10) * t73 * t60 / t81 * s0 / t7 / t86 * t39 / t65 * t18 / t3 * t5) ** (0.1e1 / 0.4e1)
  t105 = jnp.log(0.1e1 + 0.1e1 * (0.1e1 - 0.1e1 / t99) * t81)
  res = -t32 + t57 + t59 / t60 * t66 * t105
  return res