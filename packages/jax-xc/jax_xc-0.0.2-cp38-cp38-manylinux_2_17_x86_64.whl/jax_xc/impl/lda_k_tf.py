"""Generated from lda_k_tf.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, params, p):
  t2 = r0 + r1
  t4 = (r0 - r1) / t2
  t5 = 0.1e1 + t4
  t7 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t8 = t7 ** 2
  t9 = t8 * p.zeta_threshold
  t10 = t5 ** (0.1e1 / 0.3e1)
  t11 = t10 ** 2
  t13 = jnp.where(t5 <= p.zeta_threshold, t9, t11 * t5)
  t14 = 0.1e1 - t4
  t16 = t14 ** (0.1e1 / 0.3e1)
  t17 = t16 ** 2
  t19 = jnp.where(t14 <= p.zeta_threshold, t9, t17 * t14)
  t23 = 3 ** (0.1e1 / 0.3e1)
  t26 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t27 = t26 ** 2
  t29 = 4 ** (0.1e1 / 0.3e1)
  t30 = t29 ** 2
  t32 = t2 ** (0.1e1 / 0.3e1)
  t33 = t32 ** 2
  res = params.ax * (t13 / 0.2e1 + t19 / 0.2e1) * t23 / t27 * t30 * t33 / 0.3e1
  return res

def unpol(r0, params, p):
  t2 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t3 = t2 ** 2
  t5 = jnp.where(0.1e1 <= p.zeta_threshold, t3 * p.zeta_threshold, 1)
  t7 = 3 ** (0.1e1 / 0.3e1)
  t10 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t11 = t10 ** 2
  t13 = 4 ** (0.1e1 / 0.3e1)
  t14 = t13 ** 2
  t16 = r0 ** (0.1e1 / 0.3e1)
  t17 = t16 ** 2
  res = params.ax * t5 * t7 / t11 * t14 * t17 / 0.3e1
  return res