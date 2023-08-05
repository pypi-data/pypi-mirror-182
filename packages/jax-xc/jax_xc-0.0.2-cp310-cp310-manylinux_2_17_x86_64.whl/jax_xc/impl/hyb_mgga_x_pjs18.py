"""Generated from hyb_mgga_x_pjs18.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, l0, l1, tau0, tau1, params, p):
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
  t27 = t6 ** (0.1e1 / 0.3e1)
  t29 = 9 ** (0.1e1 / 0.3e1)
  t30 = t29 ** 2
  t32 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t33 = t32 ** 2
  t35 = t30 * t33 * p.cam_omega
  t37 = t2 / t27
  t38 = 6 ** (0.1e1 / 0.3e1)
  t39 = jnp.pi ** 2
  t40 = t39 ** (0.1e1 / 0.3e1)
  t41 = t40 ** 2
  t42 = 0.1e1 / t41
  t43 = t38 * t42
  t44 = r0 ** 2
  t45 = r0 ** (0.1e1 / 0.3e1)
  t46 = t45 ** 2
  t49 = s0 / t46 / t44
  t52 = t38 ** 2
  t55 = t52 / t40 / t39
  t56 = s0 ** 2
  t57 = t44 ** 2
  t64 = 0.1e1 + 0.15045488888888888889e0 * t43 * t49 + 0.26899490462262948e-2 * t55 * t56 / t45 / t57 / r0
  t65 = t64 ** (0.1e1 / 0.1e2)
  t68 = 0.1e1 + t17 <= p.zeta_threshold
  t70 = 0.1e1 - t17 <= p.zeta_threshold
  t71 = jnp.where(t70, t15, t17)
  t72 = jnp.where(t68, t11, t71)
  t73 = 0.1e1 + t72
  t75 = t73 ** (0.1e1 / 0.3e1)
  t76 = jnp.where(t73 <= p.zeta_threshold, t22, t75)
  t81 = t35 * t37 / t65 / t76 / 0.18e2
  t83 = jnp.where(t81 < 0.1e-9, 0.1e-9, t81)
  t85 = 0.135e1 < t83
  t86 = jnp.where(t85, t83, 0.135e1)
  t87 = t86 ** 2
  t90 = t87 ** 2
  t93 = t90 * t87
  t96 = t90 ** 2
  t108 = t96 ** 2
  t112 = jnp.where(t85, 0.135e1, t83)
  t113 = jnp.sqrt(jnp.pi)
  t116 = jax.lax.erf(0.1e1 / t112 / 0.2e1)
  t118 = t112 ** 2
  t121 = jnp.exp(-0.1e1 / t118 / 0.4e1)
  t132 = jnp.where(0.135e1 <= t83, 0.1e1 / t87 / 0.36e2 - 0.1e1 / t90 / 0.96e3 + 0.1e1 / t93 / 0.2688e5 - 0.1e1 / t96 / 0.82944e6 + 0.1e1 / t96 / t87 / 0.2838528e8 - 0.1e1 / t96 / t90 / 0.107347968e10 + 0.1e1 / t96 / t93 / 0.445906944e11 - 0.1e1 / t108 / 0.20214448128e13, 0.1e1 - 0.8e1 / 0.3e1 * t112 * (t113 * t116 + 0.2e1 * t112 * (t121 - 0.3e1 / 0.2e1 - 0.2e1 * t118 * (t121 - 0.1e1))))
  t133 = t64 ** (0.1e1 / 0.5e1)
  t137 = 0.27e0 < t83
  t138 = jnp.where(t137, t83, 0.27e0)
  t139 = t138 ** 2
  t140 = t139 ** 2
  t141 = t140 ** 2
  t142 = t141 * t140
  t143 = t141 ** 2
  t144 = t143 ** 2
  t148 = t140 * t139
  t149 = t141 * t148
  t159 = t141 * t139
  t174 = 0.1e1 / t144 / t142 / 0.33929038000650146833571361325056e38 - 0.1e1 / t144 / t149 / 0.3511556992918352140755776405766144e40 + 0.3e1 / 0.224e4 / t140 - 0.1e1 / t148 / 0.1152e5 + 0.3e1 / 0.78848e6 / t141 - 0.1e1 / t159 / 0.745472e7 + 0.1e1 / t142 / 0.24772608e9 - 0.1e1 / t149 / 0.93585408e10 + 0.1e1 / t143 / 0.3944742912e12 - 0.1e1 / t143 / t139 / 0.183119118336e14 + 0.1e1 / t143 / t140 / 0.9270284255232e15
  t207 = -0.1e1 / t143 / t148 / 0.50785035485184e17 + 0.1e1 / t143 / t141 / 0.2991700272218112e19 - 0.1e1 / t143 / t159 / 0.188514051721003008e21 + 0.1e1 / t143 / t142 / 0.12648942844388573184e23 - 0.1e1 / t143 / t149 / 0.900231674141645733888e24 + 0.1e1 / t144 / 0.67726520292999771979776e26 - 0.1e1 / t144 / t139 / 0.536974553751641049268224e28 + 0.1e1 / t144 / t140 / 0.44747310348880790522167296e30 - 0.1e1 / t144 / t148 / 0.3909716563474290836848508928e32 + 0.1e1 / t144 / t141 / 0.357385233699457383710280646656e34 - 0.1e1 / t144 / t159 / 0.34109511607036583784813762183168e36
  t209 = jnp.where(t137, 0.27e0, t83)
  t210 = t209 ** 2
  t212 = t210 ** 2
  t213 = 0.64e2 * t212
  t217 = jnp.exp(-0.1e1 / t210 / 0.4e1)
  t223 = jax.lax.erf(0.1e1 / t209 / 0.2e1)
  t230 = jnp.where(0.27e0 <= t83, t174 + t207, 0.1e1 + 0.24e2 * t210 * ((0.2e2 * t210 - t213) * t217 - 0.3e1 - 0.36e2 * t210 + t213 + 0.1e2 * t209 * t113 * t223))
  t236 = 0.43662396e-1 * t52 * t41
  t240 = t133 ** 2
  t241 = 0.1e1 / t240
  t246 = 0.32e0 < t83
  t247 = jnp.where(t246, t83, 0.32e0)
  t248 = t247 ** 2
  t249 = t248 ** 2
  t252 = t249 * t248
  t255 = t249 ** 2
  t258 = t255 * t248
  t261 = t255 * t249
  t264 = t255 * t252
  t267 = t255 ** 2
  t291 = t267 ** 2
  t303 = 0.3e1 / 0.784e4 / t249 - 0.1e1 / t252 / 0.56448e5 + 0.5e1 / 0.8515584e7 / t255 - 0.1e1 / t258 / 0.6150144e8 + 0.1e1 / t261 / 0.253034496e10 - 0.1e1 / t264 / 0.1158119424e12 + 0.1e1 / t267 / 0.581192122368e13 - 0.1e1 / t267 / t248 / 0.316612955602944e15 + 0.1e1 / t267 / t249 / 0.185827061661696e17 - 0.1e1 / t267 / t252 / 0.1168055816159232e19 + 0.1e1 / t267 / t255 / 0.7824446865801216e20 - 0.1e1 / t267 / t258 / 0.55625110547104530432e22 + 0.1e1 / t267 / t261 / 0.41817405043548622946304e24 - 0.1e1 / t267 / t264 / 0.33139778504339333578752e26 + 0.1e1 / t291 / 0.2760851680179343645999104e28 - 0.1e1 / t291 / t248 / 0.24119107039344543796297728e30 + 0.1e1 / t291 / t249 / 0.22046293272414372635684634624e32 - 0.1e1 / t291 / t252 / 0.21042094544618633283918675050496e34
  t304 = jnp.where(t246, 0.32e0, t83)
  t306 = t304 ** 2
  t307 = t306 * t304
  t309 = t306 ** 2
  t314 = t309 ** 2
  t320 = jnp.exp(-0.1e1 / t306 / 0.4e1)
  t334 = jax.lax.erf(0.1e1 / t304 / 0.2e1)
  t341 = jnp.where(0.32e0 <= t83, t303, 0.1e1 + 0.8e1 / 0.7e1 * t304 * ((-0.576e3 * t309 * t304 - 0.12288e6 * t314 * t304 + 0.384e4 * t309 * t307 - 0.8e1 * t304 + 0.256e3 * t307) * t320 + 0.24e2 * t307 * (0.512e4 * t309 * t306 + 0.224e3 * t306 - 0.144e4 * t309 - 0.35e2) + 0.2e1 * t113 * (-0.2e1 + 0.6e2 * t306) * t334))
  t351 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (t132 / t133 + 0.35e2 / 0.81e2 * t230 * (-0.14554132e0 * tau0 / t46 / r0 + t236 + 0.42296278333333333333e-1 * t49) * t43 * t241 + 0.26329605555555555556e-1 * t341 * t38 * t42 * t49 * t241))
  t353 = jnp.where(t10, t15, -t17)
  t354 = jnp.where(t14, t11, t353)
  t355 = 0.1e1 + t354
  t357 = t355 ** (0.1e1 / 0.3e1)
  t359 = jnp.where(t355 <= p.zeta_threshold, t23, t357 * t355)
  t361 = r1 ** 2
  t362 = r1 ** (0.1e1 / 0.3e1)
  t363 = t362 ** 2
  t366 = s2 / t363 / t361
  t369 = s2 ** 2
  t370 = t361 ** 2
  t377 = 0.1e1 + 0.15045488888888888889e0 * t43 * t366 + 0.26899490462262948e-2 * t55 * t369 / t362 / t370 / r1
  t378 = t377 ** (0.1e1 / 0.1e2)
  t380 = jnp.where(t68, t15, -t17)
  t381 = jnp.where(t70, t11, t380)
  t382 = 0.1e1 + t381
  t384 = t382 ** (0.1e1 / 0.3e1)
  t385 = jnp.where(t382 <= p.zeta_threshold, t22, t384)
  t390 = t35 * t37 / t378 / t385 / 0.18e2
  t392 = jnp.where(t390 < 0.1e-9, 0.1e-9, t390)
  t394 = 0.135e1 < t392
  t395 = jnp.where(t394, t392, 0.135e1)
  t396 = t395 ** 2
  t399 = t396 ** 2
  t402 = t399 * t396
  t405 = t399 ** 2
  t417 = t405 ** 2
  t421 = jnp.where(t394, 0.135e1, t392)
  t424 = jax.lax.erf(0.1e1 / t421 / 0.2e1)
  t426 = t421 ** 2
  t429 = jnp.exp(-0.1e1 / t426 / 0.4e1)
  t440 = jnp.where(0.135e1 <= t392, 0.1e1 / t396 / 0.36e2 - 0.1e1 / t399 / 0.96e3 + 0.1e1 / t402 / 0.2688e5 - 0.1e1 / t405 / 0.82944e6 + 0.1e1 / t405 / t396 / 0.2838528e8 - 0.1e1 / t405 / t399 / 0.107347968e10 + 0.1e1 / t405 / t402 / 0.445906944e11 - 0.1e1 / t417 / 0.20214448128e13, 0.1e1 - 0.8e1 / 0.3e1 * t421 * (t113 * t424 + 0.2e1 * t421 * (t429 - 0.3e1 / 0.2e1 - 0.2e1 * t426 * (t429 - 0.1e1))))
  t441 = t377 ** (0.1e1 / 0.5e1)
  t445 = 0.27e0 < t392
  t446 = jnp.where(t445, t392, 0.27e0)
  t447 = t446 ** 2
  t448 = t447 ** 2
  t449 = t448 ** 2
  t450 = t449 * t448
  t451 = t449 ** 2
  t452 = t451 ** 2
  t456 = t448 * t447
  t457 = t449 * t456
  t467 = t449 * t447
  t482 = 0.1e1 / t452 / t450 / 0.33929038000650146833571361325056e38 - 0.1e1 / t452 / t457 / 0.3511556992918352140755776405766144e40 + 0.3e1 / 0.224e4 / t448 - 0.1e1 / t456 / 0.1152e5 + 0.3e1 / 0.78848e6 / t449 - 0.1e1 / t467 / 0.745472e7 + 0.1e1 / t450 / 0.24772608e9 - 0.1e1 / t457 / 0.93585408e10 + 0.1e1 / t451 / 0.3944742912e12 - 0.1e1 / t451 / t447 / 0.183119118336e14 + 0.1e1 / t451 / t448 / 0.9270284255232e15
  t515 = -0.1e1 / t451 / t456 / 0.50785035485184e17 + 0.1e1 / t451 / t449 / 0.2991700272218112e19 - 0.1e1 / t451 / t467 / 0.188514051721003008e21 + 0.1e1 / t451 / t450 / 0.12648942844388573184e23 - 0.1e1 / t451 / t457 / 0.900231674141645733888e24 + 0.1e1 / t452 / 0.67726520292999771979776e26 - 0.1e1 / t452 / t447 / 0.536974553751641049268224e28 + 0.1e1 / t452 / t448 / 0.44747310348880790522167296e30 - 0.1e1 / t452 / t456 / 0.3909716563474290836848508928e32 + 0.1e1 / t452 / t449 / 0.357385233699457383710280646656e34 - 0.1e1 / t452 / t467 / 0.34109511607036583784813762183168e36
  t517 = jnp.where(t445, 0.27e0, t392)
  t518 = t517 ** 2
  t520 = t518 ** 2
  t521 = 0.64e2 * t520
  t525 = jnp.exp(-0.1e1 / t518 / 0.4e1)
  t531 = jax.lax.erf(0.1e1 / t517 / 0.2e1)
  t538 = jnp.where(0.27e0 <= t392, t482 + t515, 0.1e1 + 0.24e2 * t518 * ((0.2e2 * t518 - t521) * t525 - 0.3e1 - 0.36e2 * t518 + t521 + 0.1e2 * t517 * t113 * t531))
  t546 = t441 ** 2
  t547 = 0.1e1 / t546
  t552 = 0.32e0 < t392
  t553 = jnp.where(t552, t392, 0.32e0)
  t554 = t553 ** 2
  t555 = t554 ** 2
  t558 = t555 * t554
  t561 = t555 ** 2
  t564 = t561 * t554
  t567 = t561 * t555
  t570 = t561 * t558
  t573 = t561 ** 2
  t597 = t573 ** 2
  t609 = 0.3e1 / 0.784e4 / t555 - 0.1e1 / t558 / 0.56448e5 + 0.5e1 / 0.8515584e7 / t561 - 0.1e1 / t564 / 0.6150144e8 + 0.1e1 / t567 / 0.253034496e10 - 0.1e1 / t570 / 0.1158119424e12 + 0.1e1 / t573 / 0.581192122368e13 - 0.1e1 / t573 / t554 / 0.316612955602944e15 + 0.1e1 / t573 / t555 / 0.185827061661696e17 - 0.1e1 / t573 / t558 / 0.1168055816159232e19 + 0.1e1 / t573 / t561 / 0.7824446865801216e20 - 0.1e1 / t573 / t564 / 0.55625110547104530432e22 + 0.1e1 / t573 / t567 / 0.41817405043548622946304e24 - 0.1e1 / t573 / t570 / 0.33139778504339333578752e26 + 0.1e1 / t597 / 0.2760851680179343645999104e28 - 0.1e1 / t597 / t554 / 0.24119107039344543796297728e30 + 0.1e1 / t597 / t555 / 0.22046293272414372635684634624e32 - 0.1e1 / t597 / t558 / 0.21042094544618633283918675050496e34
  t610 = jnp.where(t552, 0.32e0, t392)
  t612 = t610 ** 2
  t613 = t612 * t610
  t615 = t612 ** 2
  t620 = t615 ** 2
  t626 = jnp.exp(-0.1e1 / t612 / 0.4e1)
  t640 = jax.lax.erf(0.1e1 / t610 / 0.2e1)
  t647 = jnp.where(0.32e0 <= t392, t609, 0.1e1 + 0.8e1 / 0.7e1 * t610 * ((-0.576e3 * t615 * t610 - 0.12288e6 * t620 * t610 + 0.384e4 * t615 * t613 - 0.8e1 * t610 + 0.256e3 * t613) * t626 + 0.24e2 * t613 * (0.512e4 * t615 * t612 + 0.224e3 * t612 - 0.144e4 * t615 - 0.35e2) + 0.2e1 * t113 * (-0.2e1 + 0.6e2 * t612) * t640))
  t657 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t359 * t27 * (t440 / t441 + 0.35e2 / 0.81e2 * t538 * (-0.14554132e0 * tau1 / t363 / r1 + t236 + 0.42296278333333333333e-1 * t366) * t43 * t547 + 0.26329605555555555556e-1 * t647 * t38 * t42 * t366 * t547))
  res = t351 + t657
  return res

def unpol(r0, s0, l0, tau0, params, p):
  t3 = 3 ** (0.1e1 / 0.3e1)
  t4 = jnp.pi ** (0.1e1 / 0.3e1)
  t7 = 0.1e1 <= p.zeta_threshold
  t8 = p.zeta_threshold - 0.1e1
  t10 = jnp.where(t7, -t8, 0)
  t11 = jnp.where(t7, t8, t10)
  t12 = 0.1e1 + t11
  t13 = t12 <= p.zeta_threshold
  t14 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t16 = t12 ** (0.1e1 / 0.3e1)
  t18 = jnp.where(t13, t14 * p.zeta_threshold, t16 * t12)
  t19 = r0 ** (0.1e1 / 0.3e1)
  t21 = 9 ** (0.1e1 / 0.3e1)
  t22 = t21 ** 2
  t24 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t25 = t24 ** 2
  t30 = 6 ** (0.1e1 / 0.3e1)
  t31 = jnp.pi ** 2
  t32 = t31 ** (0.1e1 / 0.3e1)
  t33 = t32 ** 2
  t34 = 0.1e1 / t33
  t35 = t30 * t34
  t36 = 2 ** (0.1e1 / 0.3e1)
  t37 = t36 ** 2
  t38 = s0 * t37
  t39 = r0 ** 2
  t40 = t19 ** 2
  t42 = 0.1e1 / t40 / t39
  t43 = t38 * t42
  t46 = t30 ** 2
  t50 = s0 ** 2
  t52 = t39 ** 2
  t59 = 0.1e1 + 0.15045488888888888889e0 * t35 * t43 + 0.53798980924525896e-2 * t46 / t32 / t31 * t50 * t36 / t19 / t52 / r0
  t60 = t59 ** (0.1e1 / 0.1e2)
  t62 = jnp.where(t13, t14, t16)
  t67 = t22 * t25 * p.cam_omega * t3 / t19 / t60 / t62 / 0.18e2
  t69 = jnp.where(t67 < 0.1e-9, 0.1e-9, t67)
  t71 = 0.135e1 < t69
  t72 = jnp.where(t71, t69, 0.135e1)
  t73 = t72 ** 2
  t76 = t73 ** 2
  t79 = t76 * t73
  t82 = t76 ** 2
  t94 = t82 ** 2
  t98 = jnp.where(t71, 0.135e1, t69)
  t99 = jnp.sqrt(jnp.pi)
  t102 = jax.lax.erf(0.1e1 / t98 / 0.2e1)
  t104 = t98 ** 2
  t107 = jnp.exp(-0.1e1 / t104 / 0.4e1)
  t118 = jnp.where(0.135e1 <= t69, 0.1e1 / t73 / 0.36e2 - 0.1e1 / t76 / 0.96e3 + 0.1e1 / t79 / 0.2688e5 - 0.1e1 / t82 / 0.82944e6 + 0.1e1 / t82 / t73 / 0.2838528e8 - 0.1e1 / t82 / t76 / 0.107347968e10 + 0.1e1 / t82 / t79 / 0.445906944e11 - 0.1e1 / t94 / 0.20214448128e13, 0.1e1 - 0.8e1 / 0.3e1 * t98 * (t99 * t102 + 0.2e1 * t98 * (t107 - 0.3e1 / 0.2e1 - 0.2e1 * t104 * (t107 - 0.1e1))))
  t119 = t59 ** (0.1e1 / 0.5e1)
  t123 = 0.27e0 < t69
  t124 = jnp.where(t123, t69, 0.27e0)
  t125 = t124 ** 2
  t126 = t125 ** 2
  t127 = t126 ** 2
  t128 = t127 * t126
  t129 = t127 ** 2
  t130 = t129 ** 2
  t134 = t126 * t125
  t135 = t127 * t134
  t145 = t127 * t125
  t160 = 0.1e1 / t130 / t128 / 0.33929038000650146833571361325056e38 - 0.1e1 / t130 / t135 / 0.3511556992918352140755776405766144e40 + 0.3e1 / 0.224e4 / t126 - 0.1e1 / t134 / 0.1152e5 + 0.3e1 / 0.78848e6 / t127 - 0.1e1 / t145 / 0.745472e7 + 0.1e1 / t128 / 0.24772608e9 - 0.1e1 / t135 / 0.93585408e10 + 0.1e1 / t129 / 0.3944742912e12 - 0.1e1 / t129 / t125 / 0.183119118336e14 + 0.1e1 / t129 / t126 / 0.9270284255232e15
  t193 = -0.1e1 / t129 / t134 / 0.50785035485184e17 + 0.1e1 / t129 / t127 / 0.2991700272218112e19 - 0.1e1 / t129 / t145 / 0.188514051721003008e21 + 0.1e1 / t129 / t128 / 0.12648942844388573184e23 - 0.1e1 / t129 / t135 / 0.900231674141645733888e24 + 0.1e1 / t130 / 0.67726520292999771979776e26 - 0.1e1 / t130 / t125 / 0.536974553751641049268224e28 + 0.1e1 / t130 / t126 / 0.44747310348880790522167296e30 - 0.1e1 / t130 / t134 / 0.3909716563474290836848508928e32 + 0.1e1 / t130 / t127 / 0.357385233699457383710280646656e34 - 0.1e1 / t130 / t145 / 0.34109511607036583784813762183168e36
  t195 = jnp.where(t123, 0.27e0, t69)
  t196 = t195 ** 2
  t198 = t196 ** 2
  t199 = 0.64e2 * t198
  t203 = jnp.exp(-0.1e1 / t196 / 0.4e1)
  t209 = jax.lax.erf(0.1e1 / t195 / 0.2e1)
  t216 = jnp.where(0.27e0 <= t69, t160 + t193, 0.1e1 + 0.24e2 * t196 * ((0.2e2 * t196 - t199) * t203 - 0.3e1 - 0.36e2 * t196 + t199 + 0.1e2 * t195 * t99 * t209))
  t227 = t119 ** 2
  t228 = 0.1e1 / t227
  t233 = 0.32e0 < t69
  t234 = jnp.where(t233, t69, 0.32e0)
  t235 = t234 ** 2
  t236 = t235 ** 2
  t239 = t236 * t235
  t242 = t236 ** 2
  t245 = t242 * t235
  t248 = t242 * t236
  t251 = t242 * t239
  t254 = t242 ** 2
  t278 = t254 ** 2
  t290 = 0.3e1 / 0.784e4 / t236 - 0.1e1 / t239 / 0.56448e5 + 0.5e1 / 0.8515584e7 / t242 - 0.1e1 / t245 / 0.6150144e8 + 0.1e1 / t248 / 0.253034496e10 - 0.1e1 / t251 / 0.1158119424e12 + 0.1e1 / t254 / 0.581192122368e13 - 0.1e1 / t254 / t235 / 0.316612955602944e15 + 0.1e1 / t254 / t236 / 0.185827061661696e17 - 0.1e1 / t254 / t239 / 0.1168055816159232e19 + 0.1e1 / t254 / t242 / 0.7824446865801216e20 - 0.1e1 / t254 / t245 / 0.55625110547104530432e22 + 0.1e1 / t254 / t248 / 0.41817405043548622946304e24 - 0.1e1 / t254 / t251 / 0.33139778504339333578752e26 + 0.1e1 / t278 / 0.2760851680179343645999104e28 - 0.1e1 / t278 / t235 / 0.24119107039344543796297728e30 + 0.1e1 / t278 / t236 / 0.22046293272414372635684634624e32 - 0.1e1 / t278 / t239 / 0.21042094544618633283918675050496e34
  t291 = jnp.where(t233, 0.32e0, t69)
  t293 = t291 ** 2
  t294 = t293 * t291
  t296 = t293 ** 2
  t301 = t296 ** 2
  t307 = jnp.exp(-0.1e1 / t293 / 0.4e1)
  t321 = jax.lax.erf(0.1e1 / t291 / 0.2e1)
  t328 = jnp.where(0.32e0 <= t69, t290, 0.1e1 + 0.8e1 / 0.7e1 * t291 * ((-0.576e3 * t296 * t291 - 0.12288e6 * t301 * t291 + 0.384e4 * t296 * t294 - 0.8e1 * t291 + 0.256e3 * t294) * t307 + 0.24e2 * t294 * (0.512e4 * t296 * t293 + 0.224e3 * t293 - 0.144e4 * t296 - 0.35e2) + 0.2e1 * t99 * (-0.2e1 + 0.6e2 * t293) * t321))
  t339 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (t118 / t119 + 0.35e2 / 0.81e2 * t216 * (-0.14554132e0 * tau0 * t37 / t40 / r0 + 0.43662396e-1 * t46 * t33 + 0.42296278333333333333e-1 * t43) * t35 * t228 + 0.26329605555555555556e-1 * t328 * t30 * t34 * t38 * t42 * t228))
  res = 0.2e1 * t339
  return res