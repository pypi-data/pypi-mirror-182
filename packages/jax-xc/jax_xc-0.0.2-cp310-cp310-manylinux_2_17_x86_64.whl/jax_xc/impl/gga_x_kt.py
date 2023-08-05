"""Generated from gga_x_kt.mpl."""

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
  t29 = t2 ** 2
  t32 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t34 = 4 ** (0.1e1 / 0.3e1)
  t36 = params.gamma * t29 / t32 * t34
  t37 = 2 ** (0.1e1 / 0.3e1)
  t38 = t37 ** 2
  t39 = t20 * t6
  t40 = t39 ** (0.1e1 / 0.3e1)
  t42 = t38 * t40 * t39
  t43 = r0 ** 2
  t44 = r0 ** (0.1e1 / 0.3e1)
  t45 = t44 ** 2
  t60 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1e1 - t36 * t42 * s0 / t45 / t43 / (t42 / 0.4e1 + params.delta) / 0.18e2))
  t62 = jnp.where(t10, t15, -t17)
  t63 = jnp.where(t14, t11, t62)
  t64 = 0.1e1 + t63
  t66 = t64 ** (0.1e1 / 0.3e1)
  t68 = jnp.where(t64 <= p.zeta_threshold, t23, t66 * t64)
  t70 = t64 * t6
  t71 = t70 ** (0.1e1 / 0.3e1)
  t73 = t38 * t71 * t70
  t74 = r1 ** 2
  t75 = r1 ** (0.1e1 / 0.3e1)
  t76 = t75 ** 2
  t91 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t68 * t27 * (0.1e1 - t36 * t73 * s2 / t76 / t74 / (t73 / 0.4e1 + params.delta) / 0.18e2))
  res = t60 + t91
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
  t21 = t3 ** 2
  t24 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t26 = 4 ** (0.1e1 / 0.3e1)
  t29 = 2 ** (0.1e1 / 0.3e1)
  t30 = t12 * r0
  t31 = t30 ** (0.1e1 / 0.3e1)
  t32 = t31 * t30
  t34 = r0 ** 2
  t35 = t19 ** 2
  t39 = t29 ** 2
  t52 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1e1 - params.gamma * t21 / t24 * t26 * t29 * t32 * s0 / t35 / t34 / (t39 * t32 / 0.4e1 + params.delta) / 0.9e1))
  res = 0.2e1 * t52
  return res