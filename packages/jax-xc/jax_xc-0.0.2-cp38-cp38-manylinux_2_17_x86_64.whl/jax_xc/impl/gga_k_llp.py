"""Generated from gga_k_llp.mpl."""

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
  t35 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t37 = params.beta * t3 / t35
  t38 = 4 ** (0.1e1 / 0.3e1)
  t40 = r0 ** 2
  t41 = r0 ** (0.1e1 / 0.3e1)
  t42 = t41 ** 2
  t45 = params.gamma * params.beta
  t46 = jnp.sqrt(s0)
  t49 = t46 / t41 / r0
  t50 = jnp.arcsinh(t49)
  t63 = jnp.where(r0 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t6 * t29 * t31 * (0.1e1 + 0.2e1 / 0.9e1 * t37 * t38 * s0 / t42 / t40 / (0.1e1 + t45 * t49 * t50)))
  t65 = jnp.where(t11, t16, -t18)
  t66 = jnp.where(t15, t12, t65)
  t67 = 0.1e1 + t66
  t69 = t67 ** (0.1e1 / 0.3e1)
  t70 = t69 ** 2
  t72 = jnp.where(t67 <= p.zeta_threshold, t25, t70 * t67)
  t75 = r1 ** 2
  t76 = r1 ** (0.1e1 / 0.3e1)
  t77 = t76 ** 2
  t80 = jnp.sqrt(s2)
  t83 = t80 / t76 / r1
  t84 = jnp.arcsinh(t83)
  t97 = jnp.where(r1 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t6 * t72 * t31 * (0.1e1 + 0.2e1 / 0.9e1 * t37 * t38 * s2 / t77 / t75 / (0.1e1 + t45 * t83 * t84)))
  res = t63 + t97
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
  t27 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t29 = 4 ** (0.1e1 / 0.3e1)
  t32 = 2 ** (0.1e1 / 0.3e1)
  t33 = t32 ** 2
  t35 = r0 ** 2
  t39 = jnp.sqrt(s0)
  t42 = 0.1e1 / t22 / r0
  t46 = jnp.arcsinh(t39 * t32 * t42)
  t59 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t4 * t5 * jnp.pi * t21 * t23 * (0.1e1 + 0.2e1 / 0.9e1 * params.beta * t4 / t27 * t29 * s0 * t33 / t23 / t35 / (0.1e1 + params.gamma * params.beta * t39 * t32 * t42 * t46)))
  res = 0.2e1 * t59
  return res