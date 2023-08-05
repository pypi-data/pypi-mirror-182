"""Generated from mgga_c_cc.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, l0, l1, tau0, tau1, params, p):
  t3 = r0 + r1
  t4 = t3 ** 2
  t5 = t4 ** 2
  t6 = t3 ** (0.1e1 / 0.3e1)
  t7 = t6 ** 2
  t11 = r0 ** (0.1e1 / 0.3e1)
  t12 = t11 ** 2
  t16 = r0 - r1
  t18 = t16 / t3
  t19 = 0.1e1 + t18
  t20 = t19 / 0.2e1
  t21 = t20 ** (0.1e1 / 0.3e1)
  t22 = t21 ** 2
  t25 = r1 ** (0.1e1 / 0.3e1)
  t26 = t25 ** 2
  t30 = 0.1e1 - t18
  t31 = t30 / 0.2e1
  t32 = t31 ** (0.1e1 / 0.3e1)
  t33 = t32 ** 2
  t38 = t16 ** 2
  t43 = 3 ** (0.1e1 / 0.3e1)
  t45 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t47 = 4 ** (0.1e1 / 0.3e1)
  t48 = t47 ** 2
  t51 = t43 * t45 * t48 / t6
  t54 = jnp.sqrt(t51)
  t57 = t51 ** 0.15e1
  t59 = t43 ** 2
  t60 = t45 ** 2
  t64 = t59 * t60 * t47 / t7
  t70 = jnp.log(0.1e1 + 0.16081979498692535067e2 / (0.379785e1 * t54 + 0.8969e0 * t51 + 0.204775e0 * t57 + 0.123235e0 * t64))
  t72 = 0.621814e-1 * (0.1e1 + 0.53425e-1 * t51) * t70
  t73 = t38 ** 2
  t77 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t78 = t77 * p.zeta_threshold
  t79 = t19 ** (0.1e1 / 0.3e1)
  t81 = jnp.where(t19 <= p.zeta_threshold, t78, t79 * t19)
  t83 = t30 ** (0.1e1 / 0.3e1)
  t85 = jnp.where(t30 <= p.zeta_threshold, t78, t83 * t30)
  t87 = 2 ** (0.1e1 / 0.3e1)
  t91 = (t81 + t85 - 0.2e1) / (0.2e1 * t87 - 0.2e1)
  t102 = jnp.log(0.1e1 + 0.32163958997385070134e2 / (0.705945e1 * t54 + 0.1549425e1 * t51 + 0.420775e0 * t57 + 0.1562925e0 * t64))
  t115 = jnp.log(0.1e1 + 0.29608749977793437516e2 / (0.51785e1 * t54 + 0.905775e0 * t51 + 0.1100325e0 * t57 + 0.1241775e0 * t64))
  t116 = (0.1e1 + 0.278125e-1 * t51) * t115
  res = (0.1e1 - (s0 + 0.2e1 * s1 + s2) / t7 / t5 / (tau0 / t12 / r0 * t22 * t20 + tau1 / t26 / r1 * t33 * t31) * t38 / 0.8e1) * (-t72 + t73 / t5 * t91 * (-0.310907e-1 * (0.1e1 + 0.5137e-1 * t51) * t102 + t72 - 0.19751673498613801407e-1 * t116) + 0.19751673498613801407e-1 * t91 * t116)
  return res

def unpol(r0, s0, l0, tau0, params, p):
  t1 = 3 ** (0.1e1 / 0.3e1)
  t3 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t5 = 4 ** (0.1e1 / 0.3e1)
  t6 = t5 ** 2
  t7 = r0 ** (0.1e1 / 0.3e1)
  t10 = t1 * t3 * t6 / t7
  t13 = jnp.sqrt(t10)
  t16 = t10 ** 0.15e1
  t18 = t1 ** 2
  t19 = t3 ** 2
  t21 = t7 ** 2
  t24 = t18 * t19 * t5 / t21
  t30 = jnp.log(0.1e1 + 0.16081979498692535067e2 / (0.379785e1 * t13 + 0.8969e0 * t10 + 0.204775e0 * t16 + 0.123235e0 * t24))
  t34 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t36 = jnp.where(0.1e1 <= p.zeta_threshold, t34 * p.zeta_threshold, 1)
  t39 = 2 ** (0.1e1 / 0.3e1)
  t54 = jnp.log(0.1e1 + 0.29608749977793437516e2 / (0.51785e1 * t13 + 0.905775e0 * t10 + 0.1100325e0 * t16 + 0.1241775e0 * t24))
  res = -0.621814e-1 * (0.1e1 + 0.53425e-1 * t10) * t30 + 0.19751673498613801407e-1 * (0.2e1 * t36 - 0.2e1) / (0.2e1 * t39 - 0.2e1) * (0.1e1 + 0.278125e-1 * t10) * t54
  return res