"""Generated from gga_c_revtca.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t1 = r0 - r1
  t2 = r0 + r1
  t3 = 0.1e1 / t2
  t4 = t1 * t3
  t5 = 0.1e1 + t4
  t7 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t8 = t7 ** 2
  t9 = t5 ** (0.1e1 / 0.3e1)
  t10 = t9 ** 2
  t11 = jnp.where(t5 <= p.zeta_threshold, t8, t10)
  t12 = 0.1e1 - t4
  t14 = t12 ** (0.1e1 / 0.3e1)
  t15 = t14 ** 2
  t16 = jnp.where(t12 <= p.zeta_threshold, t8, t15)
  t18 = t11 / 0.2e1 + t16 / 0.2e1
  t19 = t18 ** 2
  t21 = 3 ** (0.1e1 / 0.3e1)
  t22 = 0.1e1 / jnp.pi
  t23 = t22 ** (0.1e1 / 0.3e1)
  t25 = 4 ** (0.1e1 / 0.3e1)
  t26 = t25 ** 2
  t27 = t2 ** (0.1e1 / 0.3e1)
  t33 = jnp.arctan(0.488827e1 + 0.79425925e0 * t21 * t23 * t26 / t27)
  t37 = t21 ** 2
  t38 = 0.1e1 / t23
  t42 = 6 ** (0.1e1 / 0.3e1)
  t43 = t42 ** 2
  t44 = jnp.pi ** 2
  t45 = t44 ** (0.1e1 / 0.3e1)
  t47 = t43 / t45
  t48 = 2 ** (0.1e1 / 0.3e1)
  t50 = s0 + 0.2e1 * s1 + s2
  t51 = jnp.sqrt(t50)
  t52 = t48 * t51
  t57 = (t47 * t52 / t27 / t2) ** 0.23e1
  t61 = t1 ** 2
  t62 = t61 ** 2
  t63 = t2 ** 2
  t64 = t63 ** 2
  t65 = 0.1e1 / t64
  t67 = jnp.pi ** (0.1e1 / 0.3e1)
  t69 = 9 ** (0.1e1 / 0.3e1)
  t76 = t67 * jnp.pi * t69 * t47 * t52 * t3 * t37 * t38 / 0.36e2
  t77 = 2.220446049250313e-16 ** (0.1e1 / 0.4e1)
  t79 = t67 ** 2
  t81 = t69 ** 2
  t83 = t45 ** 2
  t87 = t48 ** 2
  t91 = t23 ** 2
  t97 = t44 ** 2
  t105 = t50 ** 2
  t116 = jnp.where(t77 < t76, t76, t77)
  t117 = jnp.sin(t116)
  t120 = jnp.where(t76 <= t77, 0.1e1 - t79 * t44 * t81 * t42 / t83 * t87 * t50 / t63 * t21 / t91 / 0.432e3 + t67 * t97 * jnp.pi * t69 * t43 / t45 / t44 * t48 * t105 * t65 * t37 / t23 / t22 / 0.3456e5, t117 / t116)
  t121 = t120 ** 2
  res = t19 * t18 * (-0.655868e0 * t33 + 0.897889e0) * t37 * t38 * t25 * t27 / (0.1e1 + 0.47121507034422759993e-2 * t57) * (0.1e1 - t62 * t65 * (0.1e1 - t121)) / 0.3e1
  return res

def unpol(r0, s0, params, p):
  t2 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t3 = t2 ** 2
  t4 = jnp.where(0.1e1 <= p.zeta_threshold, t3, 1)
  t5 = t4 ** 2
  t7 = 3 ** (0.1e1 / 0.3e1)
  t9 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t11 = 4 ** (0.1e1 / 0.3e1)
  t12 = t11 ** 2
  t13 = r0 ** (0.1e1 / 0.3e1)
  t19 = jnp.arctan(0.488827e1 + 0.79425925e0 * t7 * t9 * t12 / t13)
  t23 = t7 ** 2
  t27 = 6 ** (0.1e1 / 0.3e1)
  t28 = t27 ** 2
  t29 = jnp.pi ** 2
  t30 = t29 ** (0.1e1 / 0.3e1)
  t33 = 2 ** (0.1e1 / 0.3e1)
  t34 = jnp.sqrt(s0)
  t40 = (t28 / t30 * t33 * t34 / t13 / r0) ** 0.23e1
  res = t5 * t4 * (-0.655868e0 * t19 + 0.897889e0) * t23 / t9 * t11 * t13 / (0.1e1 + 0.47121507034422759993e-2 * t40) / 0.3e1
  return res