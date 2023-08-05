"""Generated from mgga_xc_cc06.mpl."""

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
  t8 = r0 * t7
  t11 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t12 = t11 * p.zeta_threshold
  t13 = 2 ** (0.1e1 / 0.3e1)
  t15 = t8 ** (0.1e1 / 0.3e1)
  t19 = jnp.where(0.2e1 * t8 <= p.zeta_threshold, t12, 0.2e1 * t13 * r0 * t7 * t15)
  t20 = t6 ** (0.1e1 / 0.3e1)
  t24 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t19 * t20)
  t26 = r1 * t7
  t30 = t26 ** (0.1e1 / 0.3e1)
  t34 = jnp.where(0.2e1 * t26 <= p.zeta_threshold, t12, 0.2e1 * t13 * r1 * t7 * t30)
  t38 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t34 * t20)
  t40 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t42 = 4 ** (0.1e1 / 0.3e1)
  t43 = t42 ** 2
  t46 = t2 * t40 * t43 / t20
  t49 = jnp.sqrt(t46)
  t52 = t46 ** 0.15e1
  t54 = t2 ** 2
  t55 = t40 ** 2
  t57 = t20 ** 2
  t60 = t54 * t55 * t42 / t57
  t66 = jnp.log(0.1e1 + 0.16081824322151104822e2 / (0.379785e1 * t49 + 0.8969e0 * t46 + 0.204775e0 * t52 + 0.123235e0 * t60))
  t68 = 0.62182e-1 * (0.1e1 + 0.53425e-1 * t46) * t66
  t69 = r0 - r1
  t70 = t69 ** 2
  t71 = t70 ** 2
  t72 = t6 ** 2
  t73 = t72 ** 2
  t76 = t69 * t7
  t77 = 0.1e1 + t76
  t79 = t77 ** (0.1e1 / 0.3e1)
  t81 = jnp.where(t77 <= p.zeta_threshold, t12, t79 * t77)
  t82 = 0.1e1 - t76
  t84 = t82 ** (0.1e1 / 0.3e1)
  t86 = jnp.where(t82 <= p.zeta_threshold, t12, t84 * t82)
  t91 = (t81 + t86 - 0.2e1) / (0.2e1 * t13 - 0.2e1)
  t102 = jnp.log(0.1e1 + 0.32164683177870697974e2 / (0.705945e1 * t49 + 0.1549425e1 * t46 + 0.420775e0 * t52 + 0.1562925e0 * t60))
  t115 = jnp.log(0.1e1 + 0.29608574643216675549e2 / (0.51785e1 * t49 + 0.905775e0 * t46 + 0.1100325e0 * t52 + 0.1241775e0 * t60))
  t116 = (0.1e1 + 0.278125e-1 * t46) * t115
  t125 = r0 ** (0.1e1 / 0.3e1)
  t126 = t125 ** 2
  t130 = t77 / 0.2e1
  t131 = t130 ** (0.1e1 / 0.3e1)
  t132 = t131 ** 2
  t135 = r1 ** (0.1e1 / 0.3e1)
  t136 = t135 ** 2
  t140 = t82 / 0.2e1
  t141 = t140 ** (0.1e1 / 0.3e1)
  t142 = t141 ** 2
  t147 = t54 * t42 * t55 * (l0 / t126 / r0 * t132 * t130 + l1 / t136 / r1 * t142 * t140)
  res = (t24 + t38 - t68 + t71 / t73 * t91 * (-0.3109e-1 * (0.1e1 + 0.5137e-1 * t46) * t102 + t68 - 0.19751789702565206229e-1 * t116) + 0.19751789702565206229e-1 * t91 * t116) * (0.1e1 + (-0.7e-3 + 0.2e-2 * t147) / (0.1e1 + 0.65e-2 * t147))
  return res

def unpol(r0, s0, l0, tau0, params, p):
  t3 = 3 ** (0.1e1 / 0.3e1)
  t4 = jnp.pi ** (0.1e1 / 0.3e1)
  t8 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t10 = jnp.where(0.1e1 <= p.zeta_threshold, t8 * p.zeta_threshold, 1)
  t11 = r0 ** (0.1e1 / 0.3e1)
  t15 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t10 * t11)
  t18 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t20 = 4 ** (0.1e1 / 0.3e1)
  t21 = t20 ** 2
  t24 = t3 * t18 * t21 / t11
  t27 = jnp.sqrt(t24)
  t30 = t24 ** 0.15e1
  t32 = t3 ** 2
  t33 = t18 ** 2
  t35 = t11 ** 2
  t38 = t32 * t33 * t20 / t35
  t44 = jnp.log(0.1e1 + 0.16081824322151104822e2 / (0.379785e1 * t27 + 0.8969e0 * t24 + 0.204775e0 * t30 + 0.123235e0 * t38))
  t49 = 2 ** (0.1e1 / 0.3e1)
  t64 = jnp.log(0.1e1 + 0.29608574643216675549e2 / (0.51785e1 * t27 + 0.905775e0 * t24 + 0.1100325e0 * t30 + 0.1241775e0 * t38))
  t74 = t32 * t20 * t33 * l0 / t35 / r0
  res = (0.2e1 * t15 - 0.62182e-1 * (0.1e1 + 0.53425e-1 * t24) * t44 + 0.19751789702565206229e-1 * (0.2e1 * t10 - 0.2e1) / (0.2e1 * t49 - 0.2e1) * (0.1e1 + 0.278125e-1 * t24) * t64) * (0.1e1 + (-0.7e-3 + 0.2e-2 * t74) / (0.1e1 + 0.65e-2 * t74))
  return res