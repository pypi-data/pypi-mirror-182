"""Generated from gga_x_bayesian.mpl."""

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
  t30 = jnp.pi ** 2
  t31 = t30 ** (0.1e1 / 0.3e1)
  t32 = t31 ** 2
  t34 = t29 / t32
  t36 = r0 ** 2
  t37 = r0 ** (0.1e1 / 0.3e1)
  t38 = t37 ** 2
  t40 = 0.1e1 / t38 / t36
  t41 = t29 ** 2
  t43 = t41 / t31
  t44 = jnp.sqrt(s0)
  t51 = (0.1e1 + t43 * t44 / t37 / r0 / 0.12e2) ** 2
  t52 = 0.1e1 / t51
  t66 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.10008e1 + t34 * s0 * t40 * t52 * (0.1926e0 + 0.79008333333333333333e-1 * t34 * s0 * t40 * t52) / 0.24e2))
  t68 = jnp.where(t10, t15, -t17)
  t69 = jnp.where(t14, t11, t68)
  t70 = 0.1e1 + t69
  t72 = t70 ** (0.1e1 / 0.3e1)
  t74 = jnp.where(t70 <= p.zeta_threshold, t23, t72 * t70)
  t77 = r1 ** 2
  t78 = r1 ** (0.1e1 / 0.3e1)
  t79 = t78 ** 2
  t81 = 0.1e1 / t79 / t77
  t82 = jnp.sqrt(s2)
  t89 = (0.1e1 + t43 * t82 / t78 / r1 / 0.12e2) ** 2
  t90 = 0.1e1 / t89
  t104 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t74 * t27 * (0.10008e1 + t34 * s2 * t81 * t90 * (0.1926e0 + 0.79008333333333333333e-1 * t34 * s2 * t81 * t90) / 0.24e2))
  res = t66 + t104
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
  t22 = jnp.pi ** 2
  t23 = t22 ** (0.1e1 / 0.3e1)
  t24 = t23 ** 2
  t27 = t21 / t24 * s0
  t28 = 2 ** (0.1e1 / 0.3e1)
  t29 = t28 ** 2
  t30 = r0 ** 2
  t31 = t19 ** 2
  t34 = t29 / t31 / t30
  t35 = t21 ** 2
  t38 = jnp.sqrt(s0)
  t46 = (0.1e1 + t35 / t23 * t38 * t28 / t19 / r0 / 0.12e2) ** 2
  t47 = 0.1e1 / t46
  t60 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.10008e1 + t27 * t34 * t47 * (0.1926e0 + 0.79008333333333333333e-1 * t27 * t34 * t47) / 0.24e2))
  res = 0.2e1 * t60
  return res