"""Generated from gga_k_lgap_ge.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t2 = 3 ** (0.1e1 / 0.3e1)
  t3 = t2 ** 2
  t4 = jnp.pi ** (0.1e1 / 0.3e1)
  t6 = t3 * t4 * jnp.pi
  t7 = r0 + r1
  t8 = 0.1e1 / t7
  t11 = 0.2e1 * r0 * t8 <= p.zeta_threshold
  t12 = p.zeta_threshold - 0.1e1
  t15 = 0.2e1 * r1 * t8 <= p.zeta_threshold
  t16 = -t12
  t18 = (r0 - r1) * t8
  t19 = jnp.where(t15, t16, t18)
  t20 = jnp.where(t11, t12, t19)
  t21 = 0.1e1 + t20
  t23 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t24 = t23 ** 2
  t25 = t24 * p.zeta_threshold
  t26 = t21 ** (0.1e1 / 0.3e1)
  t27 = t26 ** 2
  t29 = jnp.where(t21 <= p.zeta_threshold, t25, t27 * t21)
  t30 = t7 ** (0.1e1 / 0.3e1)
  t31 = t30 ** 2
  t34 = 6 ** (0.1e1 / 0.3e1)
  t35 = t34 ** 2
  t36 = params.mu[0] * t35
  t37 = jnp.pi ** 2
  t38 = t37 ** (0.1e1 / 0.3e1)
  t39 = 0.1e1 / t38
  t40 = jnp.sqrt(s0)
  t42 = r0 ** (0.1e1 / 0.3e1)
  t49 = params.mu[1] * t34
  t50 = t38 ** 2
  t51 = 0.1e1 / t50
  t53 = r0 ** 2
  t54 = t42 ** 2
  t62 = params.mu[2] / t37
  t64 = t53 ** 2
  t73 = jnp.where(r0 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t6 * t29 * t31 * (0.1e1 + t36 * t39 * t40 / t42 / r0 / 0.12e2 + t49 * t51 * s0 / t54 / t53 / 0.24e2 + t62 * t40 * s0 / t64 / 0.48e2))
  t75 = jnp.where(t11, t16, -t18)
  t76 = jnp.where(t15, t12, t75)
  t77 = 0.1e1 + t76
  t79 = t77 ** (0.1e1 / 0.3e1)
  t80 = t79 ** 2
  t82 = jnp.where(t77 <= p.zeta_threshold, t25, t80 * t77)
  t84 = jnp.sqrt(s2)
  t86 = r1 ** (0.1e1 / 0.3e1)
  t93 = r1 ** 2
  t94 = t86 ** 2
  t101 = t93 ** 2
  t110 = jnp.where(r1 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t6 * t82 * t31 * (0.1e1 + t36 * t39 * t84 / t86 / r1 / 0.12e2 + t49 * t51 * s2 / t94 / t93 / 0.24e2 + t62 * t84 * s2 / t101 / 0.48e2))
  res = t73 + t110
  return res

def unpol(r0, s0, params, p):
  t3 = 3 ** (0.1e1 / 0.3e1)
  t4 = t3 ** 2
  t5 = jnp.pi ** (0.1e1 / 0.3e1)
  t8 = 0.1e1 <= p.zeta_threshold
  t9 = p.zeta_threshold - 0.1e1
  t11 = jnp.where(t8, -t9, 0)
  t12 = jnp.where(t8, t9, t11)
  t13 = 0.1e1 + t12
  t15 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t16 = t15 ** 2
  t18 = t13 ** (0.1e1 / 0.3e1)
  t19 = t18 ** 2
  t21 = jnp.where(t13 <= p.zeta_threshold, t16 * p.zeta_threshold, t19 * t13)
  t22 = r0 ** (0.1e1 / 0.3e1)
  t23 = t22 ** 2
  t26 = 6 ** (0.1e1 / 0.3e1)
  t27 = t26 ** 2
  t29 = jnp.pi ** 2
  t30 = t29 ** (0.1e1 / 0.3e1)
  t33 = jnp.sqrt(s0)
  t34 = 2 ** (0.1e1 / 0.3e1)
  t43 = t30 ** 2
  t46 = t34 ** 2
  t48 = r0 ** 2
  t58 = t48 ** 2
  t67 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t4 * t5 * jnp.pi * t21 * t23 * (0.1e1 + params.mu[0] * t27 / t30 * t33 * t34 / t22 / r0 / 0.12e2 + params.mu[1] * t26 / t43 * s0 * t46 / t23 / t48 / 0.24e2 + params.mu[2] / t29 * t33 * s0 / t58 / 0.24e2))
  res = 0.2e1 * t67
  return res