"""Generated from gga_x_vmt.mpl."""

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
  t30 = params.mu * t29
  t31 = jnp.pi ** 2
  t32 = t31 ** (0.1e1 / 0.3e1)
  t33 = t32 ** 2
  t34 = 0.1e1 / t33
  t35 = t30 * t34
  t36 = r0 ** 2
  t37 = r0 ** (0.1e1 / 0.3e1)
  t38 = t37 ** 2
  t40 = 0.1e1 / t38 / t36
  t42 = params.alpha * t29
  t44 = t34 * s0 * t40
  t47 = jnp.exp(-t42 * t44 / 0.24e2)
  t60 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1e1 + t35 * s0 * t40 * t47 / (0.1e1 + t30 * t44 / 0.24e2) / 0.24e2))
  t62 = jnp.where(t10, t15, -t17)
  t63 = jnp.where(t14, t11, t62)
  t64 = 0.1e1 + t63
  t66 = t64 ** (0.1e1 / 0.3e1)
  t68 = jnp.where(t64 <= p.zeta_threshold, t23, t66 * t64)
  t70 = r1 ** 2
  t71 = r1 ** (0.1e1 / 0.3e1)
  t72 = t71 ** 2
  t74 = 0.1e1 / t72 / t70
  t77 = t34 * s2 * t74
  t80 = jnp.exp(-t42 * t77 / 0.24e2)
  t93 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t68 * t27 * (0.1e1 + t35 * s2 * t74 * t80 / (0.1e1 + t30 * t77 / 0.24e2) / 0.24e2))
  res = t60 + t93
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
  t22 = params.mu * t21
  t23 = jnp.pi ** 2
  t24 = t23 ** (0.1e1 / 0.3e1)
  t25 = t24 ** 2
  t26 = 0.1e1 / t25
  t29 = 2 ** (0.1e1 / 0.3e1)
  t30 = t29 ** 2
  t31 = r0 ** 2
  t32 = t19 ** 2
  t34 = 0.1e1 / t32 / t31
  t39 = s0 * t30 * t34
  t42 = jnp.exp(-params.alpha * t21 * t26 * t39 / 0.24e2)
  t56 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1e1 + t22 * t26 * s0 * t30 * t34 * t42 / (0.1e1 + t22 * t26 * t39 / 0.24e2) / 0.24e2))
  res = 0.2e1 * t56
  return res