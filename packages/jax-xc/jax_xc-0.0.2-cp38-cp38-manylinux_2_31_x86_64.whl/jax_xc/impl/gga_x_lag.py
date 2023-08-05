"""Generated from gga_x_lag.mpl."""

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
  t28 = t6 ** (0.1e1 / 0.3e1)
  t29 = 6 ** (0.1e1 / 0.3e1)
  t30 = t29 ** 2
  t31 = jnp.pi ** 2
  t32 = t31 ** (0.1e1 / 0.3e1)
  t34 = t30 / t32
  t35 = jnp.sqrt(s0)
  t36 = r0 ** (0.1e1 / 0.3e1)
  t41 = (t34 * t35 / t36 / r0) ** 0.2626712e1
  t45 = (0.1e1 + 0.13471619689594796103e-3 * t41) ** (-0.657946e0)
  t49 = jnp.where(r0 <= p.dens_threshold, 0, -0.22554757207579166202e-4 * t5 * t26 * t28 * t41 * t45)
  t51 = jnp.where(t10, t15, -t17)
  t52 = jnp.where(t14, t11, t51)
  t53 = 0.1e1 + t52
  t55 = t53 ** (0.1e1 / 0.3e1)
  t57 = jnp.where(t53 <= p.zeta_threshold, t23, t55 * t53)
  t59 = jnp.sqrt(s2)
  t60 = r1 ** (0.1e1 / 0.3e1)
  t65 = (t34 * t59 / t60 / r1) ** 0.2626712e1
  t69 = (0.1e1 + 0.13471619689594796103e-3 * t65) ** (-0.657946e0)
  t73 = jnp.where(r1 <= p.dens_threshold, 0, -0.22554757207579166202e-4 * t5 * t57 * t28 * t65 * t69)
  res = t49 + t73
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
  t20 = r0 ** (0.1e1 / 0.3e1)
  t21 = 6 ** (0.1e1 / 0.3e1)
  t22 = t21 ** 2
  t23 = jnp.pi ** 2
  t24 = t23 ** (0.1e1 / 0.3e1)
  t27 = jnp.sqrt(s0)
  t28 = 2 ** (0.1e1 / 0.3e1)
  t34 = (t22 / t24 * t27 * t28 / t20 / r0) ** 0.2626712e1
  t38 = (0.1e1 + 0.13471619689594796103e-3 * t34) ** (-0.657946e0)
  t42 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.22554757207579166202e-4 * t3 / t4 * t18 * t20 * t34 * t38)
  res = 0.2e1 * t42
  return res