"""Generated from gga_xc_th2.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t1 = r0 ** (0.1e1 / 0.12e2)
  t4 = r1 ** (0.1e1 / 0.12e2)
  t7 = r0 ** (0.1e1 / 0.6e1)
  t8 = t7 * r0
  t10 = r1 ** (0.1e1 / 0.6e1)
  t11 = t10 * r1
  t13 = r0 ** (0.1e1 / 0.3e1)
  t14 = t13 * r0
  t16 = r1 ** (0.1e1 / 0.3e1)
  t17 = t16 * r1
  t19 = jnp.sqrt(r0)
  t20 = t19 * r0
  t22 = jnp.sqrt(r1)
  t23 = t22 * r1
  t25 = t13 ** 2
  t26 = t25 * r0
  t28 = t16 ** 2
  t29 = t28 * r1
  t31 = t1 ** 2
  t32 = t31 ** 2
  t35 = t4 ** 2
  t36 = t35 ** 2
  t40 = jnp.sqrt(s0)
  t43 = r0 - r1
  t44 = r0 + r1
  t45 = 0.1e1 / t44
  t46 = t43 * t45
  t47 = 0.1e1 + t46
  t49 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t50 = t49 * p.zeta_threshold
  t51 = t47 ** (0.1e1 / 0.3e1)
  t53 = jnp.where(t47 <= p.zeta_threshold, t50, t51 * t47)
  t54 = 2 ** (0.1e1 / 0.3e1)
  t55 = t54 ** 2
  t58 = jnp.sqrt(s2)
  t61 = 0.1e1 - t46
  t63 = t61 ** (0.1e1 / 0.3e1)
  t65 = jnp.where(t61 <= p.zeta_threshold, t50, t63 * t61)
  t69 = t40 / t14 * t53 * t55 / 0.4e1 + t58 / t17 * t65 * t55 / 0.4e1
  t72 = t20 + t23
  t75 = 0.678831e0 * t1 * r0 + 0.678831e0 * t4 * r1 - 0.175821e1 * t8 - 0.175821e1 * t11 + 0.127676e1 * t14 + 0.127676e1 * t17 - 0.160789e1 * t20 - 0.160789e1 * t23 + 0.36561e0 * t26 + 0.36561e0 * t29 - 0.906635e-1 * (t32 * t1 * r0 + t36 * t4 * r1) * t69 + 0.734865e-1 * t72 * t69
  t76 = t26 + t29
  t79 = t7 ** 2
  t80 = t79 ** 2
  t83 = t10 ** 2
  t84 = t83 ** 2
  t87 = t80 * t7 * r0 + t84 * t10 * r1
  t90 = r0 ** 2
  t94 = t53 ** 2
  t96 = s0 / t25 / t90 * t94 * t54
  t97 = r1 ** 2
  t101 = t65 ** 2
  t103 = s2 / t28 / t97 * t101 * t54
  t105 = t96 / 0.8e1 + t103 / 0.8e1
  t110 = t90 + t97
  t117 = t44 ** 2
  t118 = t44 ** (0.1e1 / 0.3e1)
  t119 = t118 ** 2
  t123 = t96 / 0.4e1 + t103 / 0.4e1 - (s0 + 0.2e1 * s1 + s2) / t119 / t117
  t131 = t43 ** 2
  t133 = 0.1e1 / t117
  t143 = r0 ** 0.16666666666666666667e1
  t144 = r1 ** 0.16666666666666666667e1
  t149 = 0.735705e-1 * t76 * t69 - 0.3584585e-1 * t87 * t69 - 0.2035835e-1 * t76 * t105 + 0.1073125e-1 * t87 * t105 - 0.384078e-3 * t110 * t105 + 0.310377e-1 * t76 * t123 - 0.720326e-1 * t87 * t123 + 0.446562e-1 * t110 * t123 - 0.266802e0 * (t8 + t11) * t131 * t133 + 0.150822e1 * (t14 + t17) * t131 * t133 - 0.194515e1 * t72 * t131 * t133 + 0.679078e0 * (t143 + t144) * t131 * t133
  res = (t75 + t149) * t45
  return res

def unpol(r0, s0, params, p):
  t1 = 2 ** (0.1e1 / 0.12e2)
  t2 = t1 ** 2
  t3 = t2 * t1
  t4 = t2 ** 2
  t5 = t4 ** 2
  t7 = r0 ** (0.1e1 / 0.12e2)
  t11 = 2 ** (0.1e1 / 0.6e1)
  t12 = t11 ** 2
  t13 = t12 ** 2
  t15 = r0 ** (0.1e1 / 0.6e1)
  t19 = 2 ** (0.1e1 / 0.3e1)
  t20 = t19 ** 2
  t21 = r0 ** (0.1e1 / 0.3e1)
  t25 = jnp.sqrt(0.2e1)
  t26 = jnp.sqrt(r0)
  t30 = t21 ** 2
  t32 = t19 * t30 * r0
  t36 = jnp.sqrt(s0)
  t38 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t40 = jnp.where(0.1e1 <= p.zeta_threshold, t38 * p.zeta_threshold, 1)
  t41 = t36 * t40
  t53 = 0.1e1 / r0
  t55 = t40 ** 2
  t56 = s0 * t55
  t59 = t15 ** 2
  t60 = t59 ** 2
  t61 = t60 * t15
  t70 = r0 ** 2
  t73 = s0 / t30 / t70
  t75 = t73 * t55 - t73
  t84 = 0.3394155e0 * t5 * t3 * t7 * r0 - 0.879105e0 * t13 * t11 * t15 * r0 + 0.63838e0 * t20 * t21 * r0 - 0.803945e0 * t25 * t26 * r0 + 0.182805e0 * t32 - 0.4533175e-1 * t4 * t3 * t7 * t41 + 0.3674325e-1 * t25 * t15 * t41 + 0.3678525e-1 * t19 * t21 * t41 - 0.17922925e-1 * t11 * t26 * t41 - 0.50895875e-2 * t19 * t53 * t56 + 0.26828125e-2 * t11 / t61 * t56 - 0.960195e-4 / t30 * s0 * t55 + 0.1551885e-1 * t32 * t75 - 0.360163e-1 * t11 * t61 * r0 * t75 + 0.223281e-1 * t70 * t75
  res = t84 * t53
  return res