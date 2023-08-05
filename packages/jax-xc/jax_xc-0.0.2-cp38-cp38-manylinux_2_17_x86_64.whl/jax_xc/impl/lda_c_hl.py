"""Generated from lda_c_hl.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, params, p):
  t2 = 0.1e1 / jnp.pi
  t3 = r0 + r1
  t4 = 0.1e1 / t3
  t5 = t2 * t4
  t6 = params.hl_r[0]
  t7 = t6 ** 2
  t13 = 3 ** (0.1e1 / 0.3e1)
  t14 = t13 ** 2
  t15 = t2 ** (0.1e1 / 0.3e1)
  t17 = t14 / t15
  t18 = 4 ** (0.1e1 / 0.3e1)
  t19 = t3 ** (0.1e1 / 0.3e1)
  t20 = t18 * t19
  t25 = jnp.log(0.1e1 + t17 * t20 * t6 / 0.3e1)
  t27 = t15 ** 2
  t28 = t14 * t27
  t29 = t19 ** 2
  t31 = t18 / t29
  t36 = t13 * t15
  t37 = t18 ** 2
  t39 = t37 / t19
  t45 = params.hl_c[0] * ((0.1e1 + 0.3e1 / 0.4e1 * t5 / t7 / t6) * t25 - t28 * t31 / t7 / 0.4e1 + t36 * t39 / t6 / 0.8e1 - 0.1e1 / 0.3e1)
  t47 = (r0 - r1) * t4
  t48 = 0.1e1 + t47
  t50 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t51 = t50 * p.zeta_threshold
  t52 = t48 ** (0.1e1 / 0.3e1)
  t54 = jnp.where(t48 <= p.zeta_threshold, t51, t52 * t48)
  t55 = 0.1e1 - t47
  t57 = t55 ** (0.1e1 / 0.3e1)
  t59 = jnp.where(t55 <= p.zeta_threshold, t51, t57 * t55)
  t61 = 2 ** (0.1e1 / 0.3e1)
  t67 = params.hl_r[1]
  t68 = t67 ** 2
  t78 = jnp.log(0.1e1 + t17 * t20 * t67 / 0.3e1)
  res = -t45 + (t54 + t59 - 0.2e1) / (0.2e1 * t61 - 0.2e1) * (-params.hl_c[1] * ((0.1e1 + 0.3e1 / 0.4e1 * t5 / t68 / t67) * t78 - t28 * t31 / t68 / 0.4e1 + t36 * t39 / t67 / 0.8e1 - 0.1e1 / 0.3e1) + t45)
  return res

def unpol(r0, params, p):
  t2 = 0.1e1 / jnp.pi
  t4 = t2 / r0
  t5 = params.hl_r[0]
  t6 = t5 ** 2
  t12 = 3 ** (0.1e1 / 0.3e1)
  t13 = t12 ** 2
  t14 = t2 ** (0.1e1 / 0.3e1)
  t16 = t13 / t14
  t17 = 4 ** (0.1e1 / 0.3e1)
  t18 = r0 ** (0.1e1 / 0.3e1)
  t19 = t17 * t18
  t24 = jnp.log(0.1e1 + t16 * t19 * t5 / 0.3e1)
  t26 = t14 ** 2
  t27 = t13 * t26
  t28 = t18 ** 2
  t30 = t17 / t28
  t35 = t12 * t14
  t36 = t17 ** 2
  t38 = t36 / t18
  t44 = params.hl_c[0] * ((0.1e1 + 0.3e1 / 0.4e1 * t4 / t6 / t5) * t24 - t27 * t30 / t6 / 0.4e1 + t35 * t38 / t5 / 0.8e1 - 0.1e1 / 0.3e1)
  t46 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t48 = jnp.where(0.1e1 <= p.zeta_threshold, t46 * p.zeta_threshold, 1)
  t51 = 2 ** (0.1e1 / 0.3e1)
  t57 = params.hl_r[1]
  t58 = t57 ** 2
  t68 = jnp.log(0.1e1 + t16 * t19 * t57 / 0.3e1)
  res = -t44 + (0.2e1 * t48 - 0.2e1) / (0.2e1 * t51 - 0.2e1) * (-params.hl_c[1] * ((0.1e1 + 0.3e1 / 0.4e1 * t4 / t58 / t57) * t68 - t27 * t30 / t58 / 0.4e1 + t35 * t38 / t57 / 0.8e1 - 0.1e1 / 0.3e1) + t44)
  return res