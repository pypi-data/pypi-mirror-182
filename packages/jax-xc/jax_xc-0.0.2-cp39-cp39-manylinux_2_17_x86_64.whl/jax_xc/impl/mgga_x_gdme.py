"""Generated from mgga_x_gdme.mpl."""

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
  t31 = 2 ** (0.1e1 / 0.3e1)
  t34 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t35 = 0.1e1 / t34
  t36 = 4 ** (0.1e1 / 0.3e1)
  t38 = jnp.pi ** 2
  t39 = t38 ** (0.1e1 / 0.3e1)
  t40 = t39 ** 2
  t44 = 0.2e1 / 0.9e1 * (params.AA + 0.3e1 / 0.5e1 * params.BB) * t31 * t35 * t36 / t40
  t46 = params.BB * t2 * t35
  t47 = t31 ** 2
  t48 = t36 * t47
  t50 = 0.1e1 / t39 / t38
  t51 = params.a ** 2
  t52 = t51 - params.a + 0.1e1 / 0.2e1
  t54 = r0 ** (0.1e1 / 0.3e1)
  t55 = t54 ** 2
  t57 = 0.1e1 / t55 / r0
  t70 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (t44 + t46 * t48 * t50 * (t52 * l0 * t57 - 0.2e1 * tau0 * t57) / 0.27e2))
  t72 = jnp.where(t10, t15, -t17)
  t73 = jnp.where(t14, t11, t72)
  t74 = 0.1e1 + t73
  t76 = t74 ** (0.1e1 / 0.3e1)
  t78 = jnp.where(t74 <= p.zeta_threshold, t23, t76 * t74)
  t81 = r1 ** (0.1e1 / 0.3e1)
  t82 = t81 ** 2
  t84 = 0.1e1 / t82 / r1
  t97 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t78 * t27 * (t44 + t46 * t48 * t50 * (t52 * l1 * t84 - 0.2e1 * tau1 * t84) / 0.27e2))
  res = t70 + t97
  return res

def unpol(r0, s0, l0, tau0, params, p):
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
  t23 = 2 ** (0.1e1 / 0.3e1)
  t26 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t27 = 0.1e1 / t26
  t28 = 4 ** (0.1e1 / 0.3e1)
  t30 = jnp.pi ** 2
  t31 = t30 ** (0.1e1 / 0.3e1)
  t32 = t31 ** 2
  t39 = t23 ** 2
  t43 = params.a ** 2
  t46 = t19 ** 2
  t48 = 0.1e1 / t46 / r0
  t63 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.2e1 / 0.9e1 * (params.AA + 0.3e1 / 0.5e1 * params.BB) * t23 * t27 * t28 / t32 + params.BB * t3 * t27 * t28 * t39 / t31 / t30 * ((t43 - params.a + 0.1e1 / 0.2e1) * l0 * t39 * t48 - 0.2e1 * tau0 * t39 * t48) / 0.27e2))
  res = 0.2e1 * t63
  return res