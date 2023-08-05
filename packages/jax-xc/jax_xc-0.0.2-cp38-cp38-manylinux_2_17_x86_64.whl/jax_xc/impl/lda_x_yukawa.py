"""Generated from lda_x_yukawa.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, params, p):
  t1 = 3 ** (0.1e1 / 0.3e1)
  t3 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t5 = 4 ** (0.1e1 / 0.3e1)
  t6 = t5 ** 2
  t7 = t1 * t3 * t6
  t8 = 2 ** (0.1e1 / 0.3e1)
  t9 = t8 ** 2
  t11 = r0 + r1
  t13 = (r0 - r1) / t11
  t14 = 0.1e1 + t13
  t15 = t14 <= p.zeta_threshold
  t16 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t17 = t16 * p.zeta_threshold
  t18 = t14 ** (0.1e1 / 0.3e1)
  t20 = jnp.where(t15, t17, t18 * t14)
  t22 = t11 ** (0.1e1 / 0.3e1)
  t23 = 9 ** (0.1e1 / 0.3e1)
  t24 = t23 ** 2
  t25 = t3 ** 2
  t27 = t24 * t25 * p.cam_omega
  t29 = t1 / t22
  t30 = jnp.where(t15, t16, t18)
  t34 = t27 * t29 / t30 / 0.18e2
  t36 = 0.192e1 < t34
  t37 = jnp.where(t36, t34, 0.192e1)
  t38 = t37 ** 2
  t41 = t38 ** 2
  t44 = t41 * t38
  t47 = t41 ** 2
  t50 = t47 * t38
  t53 = t47 * t41
  t56 = t47 * t44
  t59 = t47 ** 2
  t83 = t59 ** 2
  t92 = 0.1e1 / t38 / 0.9e1 - 0.1e1 / t41 / 0.3e2 + 0.1e1 / t44 / 0.7e2 - 0.1e1 / t47 / 0.135e3 + 0.1e1 / t50 / 0.231e3 - 0.1e1 / t53 / 0.364e3 + 0.1e1 / t56 / 0.54e3 - 0.1e1 / t59 / 0.765e3 + 0.1e1 / t59 / t38 / 0.1045e4 - 0.1e1 / t59 / t41 / 0.1386e4 + 0.1e1 / t59 / t44 / 0.1794e4 - 0.1e1 / t59 / t47 / 0.2275e4 + 0.1e1 / t59 / t50 / 0.2835e4 - 0.1e1 / t59 / t53 / 0.348e4 + 0.1e1 / t59 / t56 / 0.4216e4 - 0.1e1 / t83 / 0.5049e4 + 0.1e1 / t83 / t38 / 0.5985e4 - 0.1e1 / t83 / t41 / 0.703e4
  t93 = jnp.where(t36, 0.192e1, t34)
  t94 = jnp.arctan2(0.1e1, t93)
  t95 = t93 ** 2
  t99 = jnp.log(0.1e1 + 0.1e1 / t95)
  t108 = jnp.where(0.192e1 <= t34, t92, 0.1e1 - 0.8e1 / 0.3e1 * t93 * (t94 + t93 * (0.1e1 - (t95 + 0.3e1) * t99) / 0.4e1))
  t112 = 0.1e1 - t13
  t113 = t112 <= p.zeta_threshold
  t114 = t112 ** (0.1e1 / 0.3e1)
  t116 = jnp.where(t113, t17, t114 * t112)
  t118 = jnp.where(t113, t16, t114)
  t122 = t27 * t29 / t118 / 0.18e2
  t124 = 0.192e1 < t122
  t125 = jnp.where(t124, t122, 0.192e1)
  t126 = t125 ** 2
  t129 = t126 ** 2
  t132 = t129 * t126
  t135 = t129 ** 2
  t138 = t135 * t126
  t141 = t135 * t129
  t144 = t135 * t132
  t147 = t135 ** 2
  t171 = t147 ** 2
  t180 = 0.1e1 / t126 / 0.9e1 - 0.1e1 / t129 / 0.3e2 + 0.1e1 / t132 / 0.7e2 - 0.1e1 / t135 / 0.135e3 + 0.1e1 / t138 / 0.231e3 - 0.1e1 / t141 / 0.364e3 + 0.1e1 / t144 / 0.54e3 - 0.1e1 / t147 / 0.765e3 + 0.1e1 / t147 / t126 / 0.1045e4 - 0.1e1 / t147 / t129 / 0.1386e4 + 0.1e1 / t147 / t132 / 0.1794e4 - 0.1e1 / t147 / t135 / 0.2275e4 + 0.1e1 / t147 / t138 / 0.2835e4 - 0.1e1 / t147 / t141 / 0.348e4 + 0.1e1 / t147 / t144 / 0.4216e4 - 0.1e1 / t171 / 0.5049e4 + 0.1e1 / t171 / t126 / 0.5985e4 - 0.1e1 / t171 / t129 / 0.703e4
  t181 = jnp.where(t124, 0.192e1, t122)
  t182 = jnp.arctan2(0.1e1, t181)
  t183 = t181 ** 2
  t187 = jnp.log(0.1e1 + 0.1e1 / t183)
  t196 = jnp.where(0.192e1 <= t122, t180, 0.1e1 - 0.8e1 / 0.3e1 * t181 * (t182 + t181 * (0.1e1 - (t183 + 0.3e1) * t187) / 0.4e1))
  res = -0.3e1 / 0.32e2 * t7 * t9 * t20 * t22 * t108 - 0.3e1 / 0.32e2 * t7 * t9 * t116 * t22 * t196
  return res

def unpol(r0, params, p):
  t1 = 3 ** (0.1e1 / 0.3e1)
  t3 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t5 = 4 ** (0.1e1 / 0.3e1)
  t6 = t5 ** 2
  t8 = 2 ** (0.1e1 / 0.3e1)
  t9 = t8 ** 2
  t10 = 0.1e1 <= p.zeta_threshold
  t11 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t13 = jnp.where(t10, t11 * p.zeta_threshold, 1)
  t15 = r0 ** (0.1e1 / 0.3e1)
  t16 = 9 ** (0.1e1 / 0.3e1)
  t17 = t16 ** 2
  t18 = t3 ** 2
  t23 = jnp.where(t10, t11, 1)
  t27 = t17 * t18 * p.cam_omega * t1 / t15 / t23 / 0.18e2
  t29 = 0.192e1 < t27
  t30 = jnp.where(t29, t27, 0.192e1)
  t31 = t30 ** 2
  t34 = t31 ** 2
  t37 = t34 * t31
  t40 = t34 ** 2
  t43 = t40 * t31
  t46 = t40 * t34
  t49 = t40 * t37
  t52 = t40 ** 2
  t76 = t52 ** 2
  t85 = 0.1e1 / t31 / 0.9e1 - 0.1e1 / t34 / 0.3e2 + 0.1e1 / t37 / 0.7e2 - 0.1e1 / t40 / 0.135e3 + 0.1e1 / t43 / 0.231e3 - 0.1e1 / t46 / 0.364e3 + 0.1e1 / t49 / 0.54e3 - 0.1e1 / t52 / 0.765e3 + 0.1e1 / t52 / t31 / 0.1045e4 - 0.1e1 / t52 / t34 / 0.1386e4 + 0.1e1 / t52 / t37 / 0.1794e4 - 0.1e1 / t52 / t40 / 0.2275e4 + 0.1e1 / t52 / t43 / 0.2835e4 - 0.1e1 / t52 / t46 / 0.348e4 + 0.1e1 / t52 / t49 / 0.4216e4 - 0.1e1 / t76 / 0.5049e4 + 0.1e1 / t76 / t31 / 0.5985e4 - 0.1e1 / t76 / t34 / 0.703e4
  t86 = jnp.where(t29, 0.192e1, t27)
  t87 = jnp.arctan2(0.1e1, t86)
  t88 = t86 ** 2
  t92 = jnp.log(0.1e1 + 0.1e1 / t88)
  t101 = jnp.where(0.192e1 <= t27, t85, 0.1e1 - 0.8e1 / 0.3e1 * t86 * (t87 + t86 * (0.1e1 - (t88 + 0.3e1) * t92) / 0.4e1))
  res = -0.3e1 / 0.16e2 * t1 * t3 * t6 * t9 * t13 * t15 * t101
  return res