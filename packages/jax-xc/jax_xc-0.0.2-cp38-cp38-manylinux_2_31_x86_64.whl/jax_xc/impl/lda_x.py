"""Generated from lda_x.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, params, p):
  t2 = 3 ** (0.1e1 / 0.3e1)
  t3 = jnp.pi ** (0.1e1 / 0.3e1)
  t5 = t2 / t3
  t6 = r0 + r1
  t7 = 0.1e1 / t6
  t8 = r0 * t7
  t11 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t12 = t11 * p.zeta_threshold
  t13 = 2 ** (0.1e1 / 0.3e1)
  t15 = t8 ** (0.1e1 / 0.3e1)
  t19 = jnp.where(0.2e1 * t8 <= p.zeta_threshold, t12, 0.2e1 * t13 * r0 * t7 * t15)
  t20 = t6 ** (0.1e1 / 0.3e1)
  t24 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t19 * t20)
  t27 = r1 * t7
  t31 = t27 ** (0.1e1 / 0.3e1)
  t35 = jnp.where(0.2e1 * t27 <= p.zeta_threshold, t12, 0.2e1 * t13 * r1 * t7 * t31)
  t39 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t35 * t20)
  res = params.alpha * t24 + params.alpha * t39
  return res

def unpol(r0, params, p):
  t3 = 3 ** (0.1e1 / 0.3e1)
  t4 = jnp.pi ** (0.1e1 / 0.3e1)
  t8 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t10 = jnp.where(0.1e1 <= p.zeta_threshold, t8 * p.zeta_threshold, 1)
  t11 = r0 ** (0.1e1 / 0.3e1)
  t15 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t10 * t11)
  res = 0.2e1 * params.alpha * t15
  return res