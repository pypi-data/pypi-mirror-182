"""Generated from gga_xc_th3.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t2 = r0 ** (0.1e1 / 0.6e1)
  t4 = r1 ** (0.1e1 / 0.6e1)
  t6 = t2 * r0 + t4 * r1
  t9 = r0 ** (0.1e1 / 0.3e1)
  t10 = t9 * r0
  t11 = r1 ** (0.1e1 / 0.3e1)
  t12 = t11 * r1
  t13 = t10 + t12
  t16 = jnp.sqrt(r0)
  t18 = jnp.sqrt(r1)
  t20 = t16 * r0 + t18 * r1
  t23 = t9 ** 2
  t25 = t11 ** 2
  t27 = t23 * r0 + t25 * r1
  t30 = r0 ** (0.1e1 / 0.12e2)
  t31 = t30 ** 2
  t32 = t31 ** 2
  t35 = r1 ** (0.1e1 / 0.12e2)
  t36 = t35 ** 2
  t37 = t36 ** 2
  t42 = jnp.sqrt(s0)
  t45 = r0 - r1
  t46 = r0 + r1
  t47 = 0.1e1 / t46
  t48 = t45 * t47
  t49 = 0.1e1 + t48
  t51 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t52 = t51 * p.zeta_threshold
  t53 = t49 ** (0.1e1 / 0.3e1)
  t55 = jnp.where(t49 <= p.zeta_threshold, t52, t53 * t49)
  t56 = 2 ** (0.1e1 / 0.3e1)
  t57 = t56 ** 2
  t60 = jnp.sqrt(s2)
  t63 = 0.1e1 - t48
  t65 = t63 ** (0.1e1 / 0.3e1)
  t67 = jnp.where(t63 <= p.zeta_threshold, t52, t65 * t63)
  t71 = t42 / t10 * t55 * t57 / 0.4e1 + t60 / t12 * t67 * t57 / 0.4e1
  t83 = t2 ** 2
  t84 = t83 ** 2
  t87 = t4 ** 2
  t88 = t87 ** 2
  t91 = t84 * t2 * r0 + t88 * t4 * r1
  t97 = r0 ** 2
  t101 = t55 ** 2
  t103 = s0 / t23 / t97 * t101 * t56
  t104 = r1 ** 2
  t108 = t67 ** 2
  t110 = s2 / t25 / t104 * t108 * t56
  t112 = t103 / 0.8e1 + t110 / 0.8e1
  t120 = t97 + t104
  t130 = t46 ** 2
  t131 = t46 ** (0.1e1 / 0.3e1)
  t132 = t131 ** 2
  t136 = t103 / 0.4e1 + t110 / 0.4e1 - (s0 + 0.2e1 * s1 + s2) / t132 / t130
  t146 = t45 ** 2
  t148 = t146 / t130
  t160 = r0 ** 0.10833333333333333333e1
  t161 = r1 ** 0.10833333333333333333e1
  t164 = params.omega[0] * t6 + params.omega[1] * t13 + params.omega[2] * t20 + params.omega[3] * t27 + params.omega[4] * (t32 * t30 * r0 + t37 * t35 * r1) * t71 / 0.2e1 + params.omega[5] * t20 * t71 / 0.2e1 + params.omega[6] * t27 * t71 / 0.2e1 + params.omega[7] * t91 * t71 / 0.2e1 + params.omega[8] * t27 * t112 / 0.2e1 + params.omega[9] * t91 * t112 / 0.2e1 + params.omega[10] * t120 * t112 / 0.2e1 + params.omega[11] * t27 * t136 + params.omega[12] * t91 * t136 + params.omega[13] * t120 * t136 + params.omega[14] * t6 * t148 + params.omega[15] * t13 * t148 + params.omega[16] * t20 * t148 + params.omega[17] * t27 * t148 + params.omega[18] * (t160 + t161)
  res = t164 * t47
  return res

def unpol(r0, s0, params, p):
  t2 = 2 ** (0.1e1 / 0.6e1)
  t3 = t2 ** 2
  t4 = t3 ** 2
  t7 = r0 ** (0.1e1 / 0.6e1)
  t12 = 2 ** (0.1e1 / 0.3e1)
  t13 = t12 ** 2
  t15 = r0 ** (0.1e1 / 0.3e1)
  t20 = jnp.sqrt(0.2e1)
  t22 = jnp.sqrt(r0)
  t28 = t15 ** 2
  t29 = t28 * r0
  t33 = 2 ** (0.1e1 / 0.12e2)
  t34 = t33 ** 2
  t36 = t34 ** 2
  t39 = r0 ** (0.1e1 / 0.12e2)
  t40 = jnp.sqrt(s0)
  t43 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t45 = jnp.where(0.1e1 <= p.zeta_threshold, t43 * p.zeta_threshold, 1)
  t69 = 0.1e1 / r0
  t71 = t45 ** 2
  t77 = t7 ** 2
  t78 = t77 ** 2
  t79 = t78 * t7
  t93 = r0 ** 2
  t96 = s0 / t28 / t93
  t98 = t96 * t71 - t96
  t113 = r0 ** 0.10833333333333333333e1
  t116 = params.omega[0] * t4 * t2 * t7 * r0 / 0.2e1 + params.omega[1] * t13 * t15 * r0 / 0.2e1 + params.omega[2] * t20 * t22 * r0 / 0.2e1 + params.omega[3] * t12 * t29 / 0.2e1 + params.omega[4] * t36 * t34 * t33 * t39 * t40 * t45 / 0.4e1 + params.omega[5] * t20 * t7 * t40 * t45 / 0.4e1 + params.omega[6] * t12 * t15 * t40 * t45 / 0.4e1 + params.omega[7] * t2 * t22 * t40 * t45 / 0.4e1 + params.omega[8] * t12 * t69 * s0 * t71 / 0.8e1 + params.omega[9] * t2 / t79 * s0 * t71 / 0.8e1 + params.omega[10] / t28 * s0 * t71 / 0.8e1 + params.omega[11] * t12 * t29 * t98 / 0.2e1 + params.omega[12] * t2 * t79 * r0 * t98 / 0.2e1 + params.omega[13] * t93 * t98 / 0.2e1 + 0.94387431268169349665e0 * params.omega[18] * t113
  res = t116 * t69
  return res