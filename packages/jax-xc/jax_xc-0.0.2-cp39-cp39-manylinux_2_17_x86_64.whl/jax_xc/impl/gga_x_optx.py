"""Generated from gga_x_optx.mpl."""

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
  t29 = params.gamma ** 2
  t30 = params.b * t29
  t31 = s0 ** 2
  t32 = r0 ** 2
  t33 = t32 ** 2
  t35 = r0 ** (0.1e1 / 0.3e1)
  t40 = t35 ** 2
  t45 = (0.1e1 + params.gamma * s0 / t40 / t32) ** 2
  t53 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (params.a + t30 * t31 / t35 / t33 / r0 / t45))
  t55 = jnp.where(t10, t15, -t17)
  t56 = jnp.where(t14, t11, t55)
  t57 = 0.1e1 + t56
  t59 = t57 ** (0.1e1 / 0.3e1)
  t61 = jnp.where(t57 <= p.zeta_threshold, t23, t59 * t57)
  t63 = s2 ** 2
  t64 = r1 ** 2
  t65 = t64 ** 2
  t67 = r1 ** (0.1e1 / 0.3e1)
  t72 = t67 ** 2
  t77 = (0.1e1 + params.gamma * s2 / t72 / t64) ** 2
  t85 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t61 * t27 * (params.a + t30 * t63 / t67 / t65 / r1 / t77))
  res = t53 + t85
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
  t21 = params.gamma ** 2
  t23 = s0 ** 2
  t25 = 2 ** (0.1e1 / 0.3e1)
  t26 = r0 ** 2
  t27 = t26 ** 2
  t33 = t25 ** 2
  t34 = t19 ** 2
  t40 = (0.1e1 + params.gamma * s0 * t33 / t34 / t26) ** 2
  t49 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (params.a + 0.2e1 * params.b * t21 * t23 * t25 / t19 / t27 / r0 / t40))
  res = 0.2e1 * t49
  return res