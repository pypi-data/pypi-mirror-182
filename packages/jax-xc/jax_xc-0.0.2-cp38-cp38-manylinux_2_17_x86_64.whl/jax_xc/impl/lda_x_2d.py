"""Generated from lda_x_2d.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, params, p):
  t1 = jnp.sqrt(0.2e1)
  t2 = jnp.sqrt(jnp.pi)
  t6 = r0 + r1
  t8 = (r0 - r1) / t6
  t9 = 0.1e1 + t8
  t11 = jnp.sqrt(p.zeta_threshold)
  t12 = t11 * p.zeta_threshold
  t13 = jnp.sqrt(t9)
  t15 = jnp.where(t9 <= p.zeta_threshold, t12, t13 * t9)
  t16 = 0.1e1 - t8
  t18 = jnp.sqrt(t16)
  t20 = jnp.where(t16 <= p.zeta_threshold, t12, t18 * t16)
  t23 = jnp.sqrt(t6)
  res = -0.4e1 / 0.3e1 * t1 / t2 * (t15 / 0.2e1 + t20 / 0.2e1) * t23
  return res

def unpol(r0, params, p):
  t1 = jnp.sqrt(0.2e1)
  t2 = jnp.sqrt(jnp.pi)
  t6 = jnp.sqrt(p.zeta_threshold)
  t8 = jnp.where(0.1e1 <= p.zeta_threshold, t6 * p.zeta_threshold, 1)
  t9 = jnp.sqrt(r0)
  res = -0.4e1 / 0.3e1 * t1 / t2 * t8 * t9
  return res