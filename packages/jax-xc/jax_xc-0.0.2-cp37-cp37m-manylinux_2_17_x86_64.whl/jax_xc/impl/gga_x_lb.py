"""Generated from gga_x_lb.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t1 = 3 ** (0.1e1 / 0.3e1)
  t4 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t5 = 4 ** (0.1e1 / 0.3e1)
  t6 = t5 ** 2
  t10 = jnp.sqrt(s0)
  t11 = r0 ** (0.1e1 / 0.3e1)
  t13 = 0.1e1 / t11 / r0
  t14 = t10 * t13
  t17 = r0 ** 2
  t18 = t11 ** 2
  t23 = params.gamma * t10 * t13
  t24 = jnp.arcsinh(t23)
  t33 = jnp.log(0.2e1 * t23)
  t37 = jnp.where(t14 < 0.3e3, params.beta * s0 / t18 / t17 / (0.3e1 * params.beta * t10 * t13 * t24 + 0.1e1), t14 / t33 / 0.3e1)
  res = (-params.alpha * t1 * t4 * t6 / 0.2e1 - t37) * t11
  return res

def unpol(r0, s0, params, p):
  t1 = 3 ** (0.1e1 / 0.3e1)
  t4 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t5 = 4 ** (0.1e1 / 0.3e1)
  t6 = t5 ** 2
  t10 = jnp.sqrt(s0)
  t11 = 2 ** (0.1e1 / 0.3e1)
  t12 = t10 * t11
  t13 = r0 ** (0.1e1 / 0.3e1)
  t15 = 0.1e1 / t13 / r0
  t19 = t11 ** 2
  t20 = r0 ** 2
  t21 = t13 ** 2
  t26 = t11 * t15
  t28 = params.gamma * t10 * t26
  t29 = jnp.arcsinh(t28)
  t38 = jnp.log(0.2e1 * t28)
  t43 = jnp.where(t12 * t15 < 0.3e3, params.beta * s0 * t19 / t21 / t20 / (0.3e1 * params.beta * t10 * t26 * t29 + 0.1e1), t12 * t15 / t38 / 0.3e1)
  res = (-params.alpha * t1 * t4 * t6 / 0.2e1 - t43) * t19 * t13 / 0.2e1
  return res