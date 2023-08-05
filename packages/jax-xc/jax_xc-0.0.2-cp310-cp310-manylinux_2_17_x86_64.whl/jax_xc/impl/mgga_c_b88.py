"""Generated from mgga_c_b88.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, l0, l1, tau0, tau1, params, p):
  t1 = r0 - r1
  t2 = t1 ** 2
  t3 = r0 + r1
  t4 = t3 ** 2
  t9 = r0 <= p.dens_threshold
  t10 = 3 ** (0.1e1 / 0.3e1)
  t11 = t10 ** 2
  t12 = 0.1e1 / jnp.pi
  t13 = t12 ** (0.1e1 / 0.3e1)
  t16 = 4 ** (0.1e1 / 0.3e1)
  t17 = t11 / t13 * t16
  t18 = 2 ** (0.1e1 / 0.3e1)
  t19 = 0.1e1 / t3
  t22 = 0.2e1 * r0 * t19 <= p.zeta_threshold
  t23 = p.zeta_threshold - 0.1e1
  t26 = 0.2e1 * r1 * t19 <= p.zeta_threshold
  t27 = -t23
  t28 = t1 * t19
  t29 = jnp.where(t26, t27, t28)
  t30 = jnp.where(t22, t23, t29)
  t32 = (0.1e1 + t30) * t3
  t33 = t32 ** (0.1e1 / 0.3e1)
  t36 = r0 ** 2
  t37 = r0 ** (0.1e1 / 0.3e1)
  t38 = t37 ** 2
  t41 = s0 / t38 / t36
  t44 = (0.1e1 + 0.7e-2 * t41) ** (0.1e1 / 0.5e1)
  t45 = t44 ** 2
  t46 = t45 ** 2
  t51 = 0.1e1 + 0.83333333333333333333e-3 * t17 * t41 / t46
  t54 = t17 * t18 / t33 / t51
  t56 = jnp.where(t9, 0, t54 / 0.9e1)
  t57 = 0.63e0 * t56
  t58 = r1 <= p.dens_threshold
  t59 = jnp.where(t22, t27, -t28)
  t60 = jnp.where(t26, t23, t59)
  t62 = (0.1e1 + t60) * t3
  t63 = t62 ** (0.1e1 / 0.3e1)
  t66 = r1 ** 2
  t67 = r1 ** (0.1e1 / 0.3e1)
  t68 = t67 ** 2
  t71 = s2 / t68 / t66
  t74 = (0.1e1 + 0.7e-2 * t71) ** (0.1e1 / 0.5e1)
  t75 = t74 ** 2
  t76 = t75 ** 2
  t81 = 0.1e1 + 0.83333333333333333333e-3 * t17 * t71 / t76
  t84 = t17 * t18 / t63 / t81
  t86 = jnp.where(t58, 0, t84 / 0.9e1)
  t87 = 0.63e0 * t86
  t90 = jnp.log(0.1e1 + t57 + t87)
  t96 = 0.1e1 + t28 <= p.zeta_threshold
  t98 = 0.1e1 - t28 <= p.zeta_threshold
  t99 = jnp.where(t98, t27, t28)
  t100 = jnp.where(t96, t23, t99)
  t101 = 0.1e1 + t100
  t102 = t101 ** 2
  t103 = t101 ** (0.1e1 / 0.3e1)
  t104 = t103 ** 2
  t106 = t18 ** 2
  t108 = t3 ** (0.1e1 / 0.3e1)
  t109 = t108 ** 2
  t110 = t109 * t3
  t122 = 0.1e1 / t13 / t12 * t16
  t125 = t51 ** 2
  t126 = t125 ** 2
  t131 = jnp.log(0.1e1 + 0.10666666666666666667e0 * t54)
  t134 = t16 ** 2
  t135 = t134 * t106
  t145 = jnp.where(t9, 0, -0.18641351111111111112e-3 * t104 * t102 * t106 * t110 * (0.2e1 * tau0 / t38 / r0 - t41 / 0.4e1) * t11 * t122 / t33 / t32 / t126 * (0.1e1 - 0.390625e0 * t131 * t10 * t13 * t135 * t33 * t51))
  t146 = jnp.where(t96, t27, -t28)
  t147 = jnp.where(t98, t23, t146)
  t148 = 0.1e1 + t147
  t149 = t148 ** 2
  t150 = t148 ** (0.1e1 / 0.3e1)
  t151 = t150 ** 2
  t165 = t81 ** 2
  t166 = t165 ** 2
  t171 = jnp.log(0.1e1 + 0.10666666666666666667e0 * t84)
  t183 = jnp.where(t58, 0, -0.18641351111111111112e-3 * t151 * t149 * t106 * t110 * (0.2e1 * tau1 / t68 / r1 - t71 / 0.4e1) * t11 * t122 / t63 / t62 / t166 * (0.1e1 - 0.390625e0 * t171 * t10 * t13 * t135 * t63 * t81))
  res = -0.2e0 * (0.1e1 - t2 / t4) * t3 * (t57 + t87) * (t57 + t87 - t90) + t145 + t183
  return res

def unpol(r0, s0, l0, tau0, params, p):
  t2 = r0 / 0.2e1 <= p.dens_threshold
  t3 = 3 ** (0.1e1 / 0.3e1)
  t4 = t3 ** 2
  t5 = 0.1e1 / jnp.pi
  t6 = t5 ** (0.1e1 / 0.3e1)
  t9 = 4 ** (0.1e1 / 0.3e1)
  t10 = t4 / t6 * t9
  t11 = 2 ** (0.1e1 / 0.3e1)
  t12 = 0.1e1 <= p.zeta_threshold
  t13 = p.zeta_threshold - 0.1e1
  t15 = jnp.where(t12, -t13, 0)
  t16 = jnp.where(t12, t13, t15)
  t17 = 0.1e1 + t16
  t18 = t17 * r0
  t19 = t18 ** (0.1e1 / 0.3e1)
  t22 = t11 ** 2
  t23 = s0 * t22
  t24 = r0 ** 2
  t25 = r0 ** (0.1e1 / 0.3e1)
  t26 = t25 ** 2
  t28 = 0.1e1 / t26 / t24
  t29 = t23 * t28
  t32 = (0.1e1 + 0.7e-2 * t29) ** (0.1e1 / 0.5e1)
  t33 = t32 ** 2
  t34 = t33 ** 2
  t40 = 0.1e1 + 0.83333333333333333333e-3 * t10 * t23 * t28 / t34
  t43 = t10 * t11 / t19 / t40
  t45 = jnp.where(t2, 0, t43 / 0.9e1)
  t47 = 0.126e1 * t45
  t49 = jnp.log(0.1e1 + t47)
  t53 = t17 ** 2
  t54 = t17 ** (0.1e1 / 0.3e1)
  t55 = t54 ** 2
  t58 = t26 * r0
  t73 = t40 ** 2
  t74 = t73 ** 2
  t79 = jnp.log(0.1e1 + 0.10666666666666666667e0 * t43)
  t82 = t9 ** 2
  t93 = jnp.where(t2, 0, -0.18641351111111111112e-3 * t55 * t53 * t22 * t58 * (0.2e1 * tau0 * t22 / t58 - t29 / 0.4e1) * t4 / t6 / t5 * t9 / t19 / t18 / t74 * (0.1e1 - 0.390625e0 * t79 * t3 * t6 * t82 * t22 * t19 * t40))
  res = -0.252e0 * r0 * t45 * (t47 - t49) + 0.2e1 * t93
  return res