"""Generated from gga_x_ak13.mpl."""

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
  t29 = 6 ** (0.1e1 / 0.3e1)
  t30 = t29 ** 2
  t32 = jnp.pi ** 2
  t33 = t32 ** (0.1e1 / 0.3e1)
  t34 = 0.1e1 / t33
  t35 = params.B1 * t30 * t34
  t36 = jnp.sqrt(s0)
  t37 = r0 ** (0.1e1 / 0.3e1)
  t40 = t36 / t37 / r0
  t41 = t30 * t34
  t45 = jnp.log(0.1e1 + t41 * t40 / 0.12e2)
  t50 = params.B2 * t30 * t34
  t52 = jnp.log(0.1e1 + t45)
  t60 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1e1 + t35 * t40 * t45 / 0.12e2 + t50 * t40 * t52 / 0.12e2))
  t62 = jnp.where(t10, t15, -t17)
  t63 = jnp.where(t14, t11, t62)
  t64 = 0.1e1 + t63
  t66 = t64 ** (0.1e1 / 0.3e1)
  t68 = jnp.where(t64 <= p.zeta_threshold, t23, t66 * t64)
  t70 = jnp.sqrt(s2)
  t71 = r1 ** (0.1e1 / 0.3e1)
  t74 = t70 / t71 / r1
  t78 = jnp.log(0.1e1 + t41 * t74 / 0.12e2)
  t83 = jnp.log(0.1e1 + t78)
  t91 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t68 * t27 * (0.1e1 + t35 * t74 * t78 / 0.12e2 + t50 * t74 * t83 / 0.12e2))
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
  t21 = 6 ** (0.1e1 / 0.3e1)
  t22 = t21 ** 2
  t24 = jnp.pi ** 2
  t25 = t24 ** (0.1e1 / 0.3e1)
  t26 = 0.1e1 / t25
  t28 = jnp.sqrt(s0)
  t29 = 2 ** (0.1e1 / 0.3e1)
  t30 = t28 * t29
  t32 = 0.1e1 / t19 / r0
  t38 = jnp.log(0.1e1 + t22 * t26 * t30 * t32 / 0.12e2)
  t46 = jnp.log(0.1e1 + t38)
  t55 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1e1 + params.B1 * t22 * t26 * t30 * t32 * t38 / 0.12e2 + params.B2 * t22 * t26 * t30 * t32 * t46 / 0.12e2))
  res = 0.2e1 * t55
  return res