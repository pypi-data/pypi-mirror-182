"""Generated from hyb_mgga_x_js18.mpl."""

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
  t33 = s0 / r0 / tau0 / 0.8e1
  t35 = jnp.where(t33 < 0.1e1, t33, 0.1e1)
  t36 = t35 ** 2
  t37 = t36 * t35
  t41 = (0.1e1 + t37) ** 2
  t43 = (t36 + 0.3e1 * t37) / t41
  t44 = 9 ** (0.1e1 / 0.3e1)
  t45 = t44 ** 2
  t47 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t48 = t47 ** 2
  t50 = t45 * t48 * p.cam_omega
  t52 = t2 / t27
  t53 = 6 ** (0.1e1 / 0.3e1)
  t54 = jnp.pi ** 2
  t55 = t54 ** (0.1e1 / 0.3e1)
  t56 = t55 ** 2
  t57 = 0.1e1 / t56
  t58 = t53 * t57
  t59 = r0 ** 2
  t60 = r0 ** (0.1e1 / 0.3e1)
  t61 = t60 ** 2
  t63 = 0.1e1 / t61 / t59
  t64 = s0 * t63
  t65 = t58 * t64
  t67 = t53 ** 2
  t70 = t67 / t55 / t54
  t71 = s0 ** 2
  t72 = t59 ** 2
  t79 = 0.1e1 + 0.15045488888888888889e0 * t65 + 0.26899490462262948e-2 * t70 * t71 / t60 / t72 / r0
  t80 = t79 ** (0.1e1 / 0.1e2)
  t83 = 0.1e1 + t17 <= p.zeta_threshold
  t85 = 0.1e1 - t17 <= p.zeta_threshold
  t86 = jnp.where(t85, t15, t17)
  t87 = jnp.where(t83, t11, t86)
  t88 = 0.1e1 + t87
  t90 = t88 ** (0.1e1 / 0.3e1)
  t91 = jnp.where(t88 <= p.zeta_threshold, t22, t90)
  t92 = 0.1e1 / t91
  t96 = t50 * t52 / t80 * t92 / 0.18e2
  t98 = jnp.where(t96 < 0.1e-9, 0.1e-9, t96)
  t100 = 0.135e1 < t98
  t101 = jnp.where(t100, t98, 0.135e1)
  t102 = t101 ** 2
  t105 = t102 ** 2
  t108 = t105 * t102
  t111 = t105 ** 2
  t123 = t111 ** 2
  t127 = jnp.where(t100, 0.135e1, t98)
  t128 = jnp.sqrt(jnp.pi)
  t131 = jax.lax.erf(0.1e1 / t127 / 0.2e1)
  t133 = t127 ** 2
  t136 = jnp.exp(-0.1e1 / t133 / 0.4e1)
  t147 = jnp.where(0.135e1 <= t98, 0.1e1 / t102 / 0.36e2 - 0.1e1 / t105 / 0.96e3 + 0.1e1 / t108 / 0.2688e5 - 0.1e1 / t111 / 0.82944e6 + 0.1e1 / t111 / t102 / 0.2838528e8 - 0.1e1 / t111 / t105 / 0.107347968e10 + 0.1e1 / t111 / t108 / 0.445906944e11 - 0.1e1 / t123 / 0.20214448128e13, 0.1e1 - 0.8e1 / 0.3e1 * t127 * (t128 * t131 + 0.2e1 * t127 * (t136 - 0.3e1 / 0.2e1 - 0.2e1 * t133 * (t136 - 0.1e1))))
  t148 = t79 ** (0.1e1 / 0.5e1)
  t149 = 0.1e1 / t148
  t152 = 0.27e0 < t98
  t153 = jnp.where(t152, t98, 0.27e0)
  t154 = t153 ** 2
  t155 = t154 ** 2
  t156 = t155 ** 2
  t157 = t156 * t155
  t158 = t156 ** 2
  t159 = t158 ** 2
  t163 = t155 * t154
  t164 = t156 * t163
  t174 = t156 * t154
  t189 = 0.1e1 / t159 / t157 / 0.33929038000650146833571361325056e38 - 0.1e1 / t159 / t164 / 0.3511556992918352140755776405766144e40 + 0.3e1 / 0.224e4 / t155 - 0.1e1 / t163 / 0.1152e5 + 0.3e1 / 0.78848e6 / t156 - 0.1e1 / t174 / 0.745472e7 + 0.1e1 / t157 / 0.24772608e9 - 0.1e1 / t164 / 0.93585408e10 + 0.1e1 / t158 / 0.3944742912e12 - 0.1e1 / t158 / t154 / 0.183119118336e14 + 0.1e1 / t158 / t155 / 0.9270284255232e15
  t222 = -0.1e1 / t158 / t163 / 0.50785035485184e17 + 0.1e1 / t158 / t156 / 0.2991700272218112e19 - 0.1e1 / t158 / t174 / 0.188514051721003008e21 + 0.1e1 / t158 / t157 / 0.12648942844388573184e23 - 0.1e1 / t158 / t164 / 0.900231674141645733888e24 + 0.1e1 / t159 / 0.67726520292999771979776e26 - 0.1e1 / t159 / t154 / 0.536974553751641049268224e28 + 0.1e1 / t159 / t155 / 0.44747310348880790522167296e30 - 0.1e1 / t159 / t163 / 0.3909716563474290836848508928e32 + 0.1e1 / t159 / t156 / 0.357385233699457383710280646656e34 - 0.1e1 / t159 / t174 / 0.34109511607036583784813762183168e36
  t224 = jnp.where(t152, 0.27e0, t98)
  t225 = t224 ** 2
  t227 = t225 ** 2
  t228 = 0.64e2 * t227
  t232 = jnp.exp(-0.1e1 / t225 / 0.4e1)
  t238 = jax.lax.erf(0.1e1 / t224 / 0.2e1)
  t245 = jnp.where(0.27e0 <= t98, t189 + t222, 0.1e1 + 0.24e2 * t225 * ((0.2e2 * t225 - t228) * t232 - 0.3e1 - 0.36e2 * t225 + t228 + 0.1e2 * t224 * t128 * t238))
  t248 = tau0 / t61 / r0
  t249 = 0.14554132e0 * t248
  t250 = t67 * t56
  t251 = 0.43662396e-1 * t250
  t255 = t148 ** 2
  t256 = 0.1e1 / t255
  t261 = 0.32e0 < t98
  t262 = jnp.where(t261, t98, 0.32e0)
  t263 = t262 ** 2
  t264 = t263 ** 2
  t267 = t264 * t263
  t270 = t264 ** 2
  t273 = t270 * t263
  t276 = t270 * t264
  t279 = t270 * t267
  t282 = t270 ** 2
  t306 = t282 ** 2
  t318 = 0.3e1 / 0.784e4 / t264 - 0.1e1 / t267 / 0.56448e5 + 0.5e1 / 0.8515584e7 / t270 - 0.1e1 / t273 / 0.6150144e8 + 0.1e1 / t276 / 0.253034496e10 - 0.1e1 / t279 / 0.1158119424e12 + 0.1e1 / t282 / 0.581192122368e13 - 0.1e1 / t282 / t263 / 0.316612955602944e15 + 0.1e1 / t282 / t264 / 0.185827061661696e17 - 0.1e1 / t282 / t267 / 0.1168055816159232e19 + 0.1e1 / t282 / t270 / 0.7824446865801216e20 - 0.1e1 / t282 / t273 / 0.55625110547104530432e22 + 0.1e1 / t282 / t276 / 0.41817405043548622946304e24 - 0.1e1 / t282 / t279 / 0.33139778504339333578752e26 + 0.1e1 / t306 / 0.2760851680179343645999104e28 - 0.1e1 / t306 / t263 / 0.24119107039344543796297728e30 + 0.1e1 / t306 / t264 / 0.22046293272414372635684634624e32 - 0.1e1 / t306 / t267 / 0.21042094544618633283918675050496e34
  t319 = jnp.where(t261, 0.32e0, t98)
  t321 = t319 ** 2
  t322 = t321 * t319
  t324 = t321 ** 2
  t329 = t324 ** 2
  t335 = jnp.exp(-0.1e1 / t321 / 0.4e1)
  t349 = jax.lax.erf(0.1e1 / t319 / 0.2e1)
  t356 = jnp.where(0.32e0 <= t98, t318, 0.1e1 + 0.8e1 / 0.7e1 * t319 * ((-0.576e3 * t324 * t319 - 0.12288e6 * t329 * t319 + 0.384e4 * t324 * t322 - 0.8e1 * t319 + 0.256e3 * t322) * t335 + 0.24e2 * t322 * (0.512e4 * t324 * t321 + 0.224e3 * t321 - 0.144e4 * t324 - 0.35e2) + 0.2e1 * t128 * (-0.2e1 + 0.6e2 * t321) * t349))
  t364 = 0.1e1 - t43
  t367 = t50 * t52 * t92 / 0.18e2
  t369 = 0.135e1 < t367
  t370 = jnp.where(t369, t367, 0.135e1)
  t371 = t370 ** 2
  t374 = t371 ** 2
  t377 = t374 * t371
  t380 = t374 ** 2
  t392 = t380 ** 2
  t396 = jnp.where(t369, 0.135e1, t367)
  t399 = jax.lax.erf(0.1e1 / t396 / 0.2e1)
  t401 = t396 ** 2
  t404 = jnp.exp(-0.1e1 / t401 / 0.4e1)
  t415 = jnp.where(0.135e1 <= t367, 0.1e1 / t371 / 0.36e2 - 0.1e1 / t374 / 0.96e3 + 0.1e1 / t377 / 0.2688e5 - 0.1e1 / t380 / 0.82944e6 + 0.1e1 / t380 / t371 / 0.2838528e8 - 0.1e1 / t380 / t374 / 0.107347968e10 + 0.1e1 / t380 / t377 / 0.445906944e11 - 0.1e1 / t392 / 0.20214448128e13, 0.1e1 - 0.8e1 / 0.3e1 * t396 * (t128 * t399 + 0.2e1 * t396 * (t404 - 0.3e1 / 0.2e1 - 0.2e1 * t401 * (t404 - 0.1e1))))
  t430 = (t248 - t64 / 0.8e1) * t53 * t57 / 0.4e1 - 0.9e1 / 0.2e2 + t65 / 0.36e2
  t431 = t430 ** 2
  t438 = (0.1e1 + 0.5e1 / 0.12e2 * (0.1e2 / 0.81e2 + 0.25e2 / 0.8748e4 * t65) * t53 * t57 * s0 * t63 + 0.292e3 / 0.405e3 * t431 - 0.146e3 / 0.135e3 * t430 * t35 * (0.1e1 - t35)) ** (0.1e1 / 0.1e2)
  t443 = 0.256337604e0 * t250
  t459 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (-p.cam_beta * (t43 * (t147 * t149 + 0.35e2 / 0.81e2 * t245 * (-t249 + t251 + 0.42296278333333333333e-1 * t64) * t58 * t256 + 0.26329605555555555556e-1 * t356 * t53 * t57 * t64 * t256) + t364 * t415 * t438) + t43 * (t149 + 0.7e1 / 0.9e1 * (0.1e1 + 0.63943327777777777778e-1 * t65 - 0.5e1 / 0.9e1 * (t249 + t443 + 0.11867481666666666667e-1 * t64) * t53 * t57) * t256) + t364 * t438))
  t461 = jnp.where(t10, t15, -t17)
  t462 = jnp.where(t14, t11, t461)
  t463 = 0.1e1 + t462
  t465 = t463 ** (0.1e1 / 0.3e1)
  t467 = jnp.where(t463 <= p.zeta_threshold, t23, t465 * t463)
  t473 = s2 / r1 / tau1 / 0.8e1
  t475 = jnp.where(t473 < 0.1e1, t473, 0.1e1)
  t476 = t475 ** 2
  t477 = t476 * t475
  t481 = (0.1e1 + t477) ** 2
  t483 = (t476 + 0.3e1 * t477) / t481
  t484 = r1 ** 2
  t485 = r1 ** (0.1e1 / 0.3e1)
  t486 = t485 ** 2
  t488 = 0.1e1 / t486 / t484
  t489 = s2 * t488
  t490 = t58 * t489
  t492 = s2 ** 2
  t493 = t484 ** 2
  t500 = 0.1e1 + 0.15045488888888888889e0 * t490 + 0.26899490462262948e-2 * t70 * t492 / t485 / t493 / r1
  t501 = t500 ** (0.1e1 / 0.1e2)
  t503 = jnp.where(t83, t15, -t17)
  t504 = jnp.where(t85, t11, t503)
  t505 = 0.1e1 + t504
  t507 = t505 ** (0.1e1 / 0.3e1)
  t508 = jnp.where(t505 <= p.zeta_threshold, t22, t507)
  t509 = 0.1e1 / t508
  t513 = t50 * t52 / t501 * t509 / 0.18e2
  t515 = jnp.where(t513 < 0.1e-9, 0.1e-9, t513)
  t517 = 0.135e1 < t515
  t518 = jnp.where(t517, t515, 0.135e1)
  t519 = t518 ** 2
  t522 = t519 ** 2
  t525 = t522 * t519
  t528 = t522 ** 2
  t540 = t528 ** 2
  t544 = jnp.where(t517, 0.135e1, t515)
  t547 = jax.lax.erf(0.1e1 / t544 / 0.2e1)
  t549 = t544 ** 2
  t552 = jnp.exp(-0.1e1 / t549 / 0.4e1)
  t563 = jnp.where(0.135e1 <= t515, 0.1e1 / t519 / 0.36e2 - 0.1e1 / t522 / 0.96e3 + 0.1e1 / t525 / 0.2688e5 - 0.1e1 / t528 / 0.82944e6 + 0.1e1 / t528 / t519 / 0.2838528e8 - 0.1e1 / t528 / t522 / 0.107347968e10 + 0.1e1 / t528 / t525 / 0.445906944e11 - 0.1e1 / t540 / 0.20214448128e13, 0.1e1 - 0.8e1 / 0.3e1 * t544 * (t128 * t547 + 0.2e1 * t544 * (t552 - 0.3e1 / 0.2e1 - 0.2e1 * t549 * (t552 - 0.1e1))))
  t564 = t500 ** (0.1e1 / 0.5e1)
  t565 = 0.1e1 / t564
  t568 = 0.27e0 < t515
  t569 = jnp.where(t568, t515, 0.27e0)
  t570 = t569 ** 2
  t571 = t570 ** 2
  t572 = t571 ** 2
  t573 = t572 * t571
  t574 = t572 ** 2
  t575 = t574 ** 2
  t579 = t571 * t570
  t580 = t572 * t579
  t590 = t572 * t570
  t605 = 0.1e1 / t575 / t573 / 0.33929038000650146833571361325056e38 - 0.1e1 / t575 / t580 / 0.3511556992918352140755776405766144e40 + 0.3e1 / 0.224e4 / t571 - 0.1e1 / t579 / 0.1152e5 + 0.3e1 / 0.78848e6 / t572 - 0.1e1 / t590 / 0.745472e7 + 0.1e1 / t573 / 0.24772608e9 - 0.1e1 / t580 / 0.93585408e10 + 0.1e1 / t574 / 0.3944742912e12 - 0.1e1 / t574 / t570 / 0.183119118336e14 + 0.1e1 / t574 / t571 / 0.9270284255232e15
  t638 = -0.1e1 / t574 / t579 / 0.50785035485184e17 + 0.1e1 / t574 / t572 / 0.2991700272218112e19 - 0.1e1 / t574 / t590 / 0.188514051721003008e21 + 0.1e1 / t574 / t573 / 0.12648942844388573184e23 - 0.1e1 / t574 / t580 / 0.900231674141645733888e24 + 0.1e1 / t575 / 0.67726520292999771979776e26 - 0.1e1 / t575 / t570 / 0.536974553751641049268224e28 + 0.1e1 / t575 / t571 / 0.44747310348880790522167296e30 - 0.1e1 / t575 / t579 / 0.3909716563474290836848508928e32 + 0.1e1 / t575 / t572 / 0.357385233699457383710280646656e34 - 0.1e1 / t575 / t590 / 0.34109511607036583784813762183168e36
  t640 = jnp.where(t568, 0.27e0, t515)
  t641 = t640 ** 2
  t643 = t641 ** 2
  t644 = 0.64e2 * t643
  t648 = jnp.exp(-0.1e1 / t641 / 0.4e1)
  t654 = jax.lax.erf(0.1e1 / t640 / 0.2e1)
  t661 = jnp.where(0.27e0 <= t515, t605 + t638, 0.1e1 + 0.24e2 * t641 * ((0.2e2 * t641 - t644) * t648 - 0.3e1 - 0.36e2 * t641 + t644 + 0.1e2 * t640 * t128 * t654))
  t664 = tau1 / t486 / r1
  t665 = 0.14554132e0 * t664
  t669 = t564 ** 2
  t670 = 0.1e1 / t669
  t675 = 0.32e0 < t515
  t676 = jnp.where(t675, t515, 0.32e0)
  t677 = t676 ** 2
  t678 = t677 ** 2
  t681 = t678 * t677
  t684 = t678 ** 2
  t687 = t684 * t677
  t690 = t684 * t678
  t693 = t684 * t681
  t696 = t684 ** 2
  t720 = t696 ** 2
  t732 = 0.3e1 / 0.784e4 / t678 - 0.1e1 / t681 / 0.56448e5 + 0.5e1 / 0.8515584e7 / t684 - 0.1e1 / t687 / 0.6150144e8 + 0.1e1 / t690 / 0.253034496e10 - 0.1e1 / t693 / 0.1158119424e12 + 0.1e1 / t696 / 0.581192122368e13 - 0.1e1 / t696 / t677 / 0.316612955602944e15 + 0.1e1 / t696 / t678 / 0.185827061661696e17 - 0.1e1 / t696 / t681 / 0.1168055816159232e19 + 0.1e1 / t696 / t684 / 0.7824446865801216e20 - 0.1e1 / t696 / t687 / 0.55625110547104530432e22 + 0.1e1 / t696 / t690 / 0.41817405043548622946304e24 - 0.1e1 / t696 / t693 / 0.33139778504339333578752e26 + 0.1e1 / t720 / 0.2760851680179343645999104e28 - 0.1e1 / t720 / t677 / 0.24119107039344543796297728e30 + 0.1e1 / t720 / t678 / 0.22046293272414372635684634624e32 - 0.1e1 / t720 / t681 / 0.21042094544618633283918675050496e34
  t733 = jnp.where(t675, 0.32e0, t515)
  t735 = t733 ** 2
  t736 = t735 * t733
  t738 = t735 ** 2
  t743 = t738 ** 2
  t749 = jnp.exp(-0.1e1 / t735 / 0.4e1)
  t763 = jax.lax.erf(0.1e1 / t733 / 0.2e1)
  t770 = jnp.where(0.32e0 <= t515, t732, 0.1e1 + 0.8e1 / 0.7e1 * t733 * ((-0.576e3 * t738 * t733 - 0.12288e6 * t743 * t733 + 0.384e4 * t738 * t736 - 0.8e1 * t733 + 0.256e3 * t736) * t749 + 0.24e2 * t736 * (0.512e4 * t738 * t735 + 0.224e3 * t735 - 0.144e4 * t738 - 0.35e2) + 0.2e1 * t128 * (-0.2e1 + 0.6e2 * t735) * t763))
  t778 = 0.1e1 - t483
  t781 = t50 * t52 * t509 / 0.18e2
  t783 = 0.135e1 < t781
  t784 = jnp.where(t783, t781, 0.135e1)
  t785 = t784 ** 2
  t788 = t785 ** 2
  t791 = t788 * t785
  t794 = t788 ** 2
  t806 = t794 ** 2
  t810 = jnp.where(t783, 0.135e1, t781)
  t813 = jax.lax.erf(0.1e1 / t810 / 0.2e1)
  t815 = t810 ** 2
  t818 = jnp.exp(-0.1e1 / t815 / 0.4e1)
  t829 = jnp.where(0.135e1 <= t781, 0.1e1 / t785 / 0.36e2 - 0.1e1 / t788 / 0.96e3 + 0.1e1 / t791 / 0.2688e5 - 0.1e1 / t794 / 0.82944e6 + 0.1e1 / t794 / t785 / 0.2838528e8 - 0.1e1 / t794 / t788 / 0.107347968e10 + 0.1e1 / t794 / t791 / 0.445906944e11 - 0.1e1 / t806 / 0.20214448128e13, 0.1e1 - 0.8e1 / 0.3e1 * t810 * (t128 * t813 + 0.2e1 * t810 * (t818 - 0.3e1 / 0.2e1 - 0.2e1 * t815 * (t818 - 0.1e1))))
  t844 = (t664 - t489 / 0.8e1) * t53 * t57 / 0.4e1 - 0.9e1 / 0.2e2 + t490 / 0.36e2
  t845 = t844 ** 2
  t852 = (0.1e1 + 0.5e1 / 0.12e2 * (0.1e2 / 0.81e2 + 0.25e2 / 0.8748e4 * t490) * t53 * t57 * s2 * t488 + 0.292e3 / 0.405e3 * t845 - 0.146e3 / 0.135e3 * t844 * t475 * (0.1e1 - t475)) ** (0.1e1 / 0.1e2)
  t872 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t467 * t27 * (-p.cam_beta * (t483 * (t563 * t565 + 0.35e2 / 0.81e2 * t661 * (-t665 + t251 + 0.42296278333333333333e-1 * t489) * t58 * t670 + 0.26329605555555555556e-1 * t770 * t53 * t57 * t489 * t670) + t778 * t829 * t852) + t483 * (t565 + 0.7e1 / 0.9e1 * (0.1e1 + 0.63943327777777777778e-1 * t490 - 0.5e1 / 0.9e1 * (t665 + t443 + 0.11867481666666666667e-1 * t489) * t53 * t57) * t670) + t778 * t852))
  res = t459 + t872
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
  t25 = s0 / r0 / tau0 / 0.8e1
  t27 = jnp.where(t25 < 0.1e1, t25, 0.1e1)
  t28 = t27 ** 2
  t29 = t28 * t27
  t33 = (0.1e1 + t29) ** 2
  t35 = (t28 + 0.3e1 * t29) / t33
  t36 = 9 ** (0.1e1 / 0.3e1)
  t37 = t36 ** 2
  t39 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t40 = t39 ** 2
  t42 = t37 * t40 * p.cam_omega
  t44 = t3 / t19
  t45 = 6 ** (0.1e1 / 0.3e1)
  t46 = jnp.pi ** 2
  t47 = t46 ** (0.1e1 / 0.3e1)
  t48 = t47 ** 2
  t49 = 0.1e1 / t48
  t50 = t45 * t49
  t51 = 2 ** (0.1e1 / 0.3e1)
  t52 = t51 ** 2
  t53 = s0 * t52
  t54 = r0 ** 2
  t55 = t19 ** 2
  t57 = 0.1e1 / t55 / t54
  t58 = t53 * t57
  t59 = t50 * t58
  t61 = t45 ** 2
  t65 = s0 ** 2
  t67 = t54 ** 2
  t74 = 0.1e1 + 0.15045488888888888889e0 * t59 + 0.53798980924525896e-2 * t61 / t47 / t46 * t65 * t51 / t19 / t67 / r0
  t75 = t74 ** (0.1e1 / 0.1e2)
  t77 = jnp.where(t13, t14, t16)
  t78 = 0.1e1 / t77
  t82 = t42 * t44 / t75 * t78 / 0.18e2
  t84 = jnp.where(t82 < 0.1e-9, 0.1e-9, t82)
  t86 = 0.135e1 < t84
  t87 = jnp.where(t86, t84, 0.135e1)
  t88 = t87 ** 2
  t91 = t88 ** 2
  t94 = t91 * t88
  t97 = t91 ** 2
  t109 = t97 ** 2
  t113 = jnp.where(t86, 0.135e1, t84)
  t114 = jnp.sqrt(jnp.pi)
  t117 = jax.lax.erf(0.1e1 / t113 / 0.2e1)
  t119 = t113 ** 2
  t122 = jnp.exp(-0.1e1 / t119 / 0.4e1)
  t133 = jnp.where(0.135e1 <= t84, 0.1e1 / t88 / 0.36e2 - 0.1e1 / t91 / 0.96e3 + 0.1e1 / t94 / 0.2688e5 - 0.1e1 / t97 / 0.82944e6 + 0.1e1 / t97 / t88 / 0.2838528e8 - 0.1e1 / t97 / t91 / 0.107347968e10 + 0.1e1 / t97 / t94 / 0.445906944e11 - 0.1e1 / t109 / 0.20214448128e13, 0.1e1 - 0.8e1 / 0.3e1 * t113 * (t114 * t117 + 0.2e1 * t113 * (t122 - 0.3e1 / 0.2e1 - 0.2e1 * t119 * (t122 - 0.1e1))))
  t134 = t74 ** (0.1e1 / 0.5e1)
  t135 = 0.1e1 / t134
  t138 = 0.27e0 < t84
  t139 = jnp.where(t138, t84, 0.27e0)
  t140 = t139 ** 2
  t141 = t140 ** 2
  t142 = t141 ** 2
  t143 = t142 * t141
  t144 = t142 ** 2
  t145 = t144 ** 2
  t149 = t141 * t140
  t150 = t142 * t149
  t160 = t142 * t140
  t175 = 0.1e1 / t145 / t143 / 0.33929038000650146833571361325056e38 - 0.1e1 / t145 / t150 / 0.3511556992918352140755776405766144e40 + 0.3e1 / 0.224e4 / t141 - 0.1e1 / t149 / 0.1152e5 + 0.3e1 / 0.78848e6 / t142 - 0.1e1 / t160 / 0.745472e7 + 0.1e1 / t143 / 0.24772608e9 - 0.1e1 / t150 / 0.93585408e10 + 0.1e1 / t144 / 0.3944742912e12 - 0.1e1 / t144 / t140 / 0.183119118336e14 + 0.1e1 / t144 / t141 / 0.9270284255232e15
  t208 = -0.1e1 / t144 / t149 / 0.50785035485184e17 + 0.1e1 / t144 / t142 / 0.2991700272218112e19 - 0.1e1 / t144 / t160 / 0.188514051721003008e21 + 0.1e1 / t144 / t143 / 0.12648942844388573184e23 - 0.1e1 / t144 / t150 / 0.900231674141645733888e24 + 0.1e1 / t145 / 0.67726520292999771979776e26 - 0.1e1 / t145 / t140 / 0.536974553751641049268224e28 + 0.1e1 / t145 / t141 / 0.44747310348880790522167296e30 - 0.1e1 / t145 / t149 / 0.3909716563474290836848508928e32 + 0.1e1 / t145 / t142 / 0.357385233699457383710280646656e34 - 0.1e1 / t145 / t160 / 0.34109511607036583784813762183168e36
  t210 = jnp.where(t138, 0.27e0, t84)
  t211 = t210 ** 2
  t213 = t211 ** 2
  t214 = 0.64e2 * t213
  t218 = jnp.exp(-0.1e1 / t211 / 0.4e1)
  t224 = jax.lax.erf(0.1e1 / t210 / 0.2e1)
  t231 = jnp.where(0.27e0 <= t84, t175 + t208, 0.1e1 + 0.24e2 * t211 * ((0.2e2 * t211 - t214) * t218 - 0.3e1 - 0.36e2 * t211 + t214 + 0.1e2 * t210 * t114 * t224))
  t235 = tau0 * t52 / t55 / r0
  t236 = 0.14554132e0 * t235
  t237 = t61 * t48
  t242 = t134 ** 2
  t243 = 0.1e1 / t242
  t248 = 0.32e0 < t84
  t249 = jnp.where(t248, t84, 0.32e0)
  t250 = t249 ** 2
  t251 = t250 ** 2
  t254 = t251 * t250
  t257 = t251 ** 2
  t260 = t257 * t250
  t263 = t257 * t251
  t266 = t257 * t254
  t269 = t257 ** 2
  t293 = t269 ** 2
  t305 = 0.3e1 / 0.784e4 / t251 - 0.1e1 / t254 / 0.56448e5 + 0.5e1 / 0.8515584e7 / t257 - 0.1e1 / t260 / 0.6150144e8 + 0.1e1 / t263 / 0.253034496e10 - 0.1e1 / t266 / 0.1158119424e12 + 0.1e1 / t269 / 0.581192122368e13 - 0.1e1 / t269 / t250 / 0.316612955602944e15 + 0.1e1 / t269 / t251 / 0.185827061661696e17 - 0.1e1 / t269 / t254 / 0.1168055816159232e19 + 0.1e1 / t269 / t257 / 0.7824446865801216e20 - 0.1e1 / t269 / t260 / 0.55625110547104530432e22 + 0.1e1 / t269 / t263 / 0.41817405043548622946304e24 - 0.1e1 / t269 / t266 / 0.33139778504339333578752e26 + 0.1e1 / t293 / 0.2760851680179343645999104e28 - 0.1e1 / t293 / t250 / 0.24119107039344543796297728e30 + 0.1e1 / t293 / t251 / 0.22046293272414372635684634624e32 - 0.1e1 / t293 / t254 / 0.21042094544618633283918675050496e34
  t306 = jnp.where(t248, 0.32e0, t84)
  t308 = t306 ** 2
  t309 = t308 * t306
  t311 = t308 ** 2
  t316 = t311 ** 2
  t322 = jnp.exp(-0.1e1 / t308 / 0.4e1)
  t336 = jax.lax.erf(0.1e1 / t306 / 0.2e1)
  t343 = jnp.where(0.32e0 <= t84, t305, 0.1e1 + 0.8e1 / 0.7e1 * t306 * ((-0.576e3 * t311 * t306 - 0.12288e6 * t316 * t306 + 0.384e4 * t311 * t309 - 0.8e1 * t306 + 0.256e3 * t309) * t322 + 0.24e2 * t309 * (0.512e4 * t311 * t308 + 0.224e3 * t308 - 0.144e4 * t311 - 0.35e2) + 0.2e1 * t114 * (-0.2e1 + 0.6e2 * t308) * t336))
  t352 = 0.1e1 - t35
  t355 = t42 * t44 * t78 / 0.18e2
  t357 = 0.135e1 < t355
  t358 = jnp.where(t357, t355, 0.135e1)
  t359 = t358 ** 2
  t362 = t359 ** 2
  t365 = t362 * t359
  t368 = t362 ** 2
  t380 = t368 ** 2
  t384 = jnp.where(t357, 0.135e1, t355)
  t387 = jax.lax.erf(0.1e1 / t384 / 0.2e1)
  t389 = t384 ** 2
  t392 = jnp.exp(-0.1e1 / t389 / 0.4e1)
  t403 = jnp.where(0.135e1 <= t355, 0.1e1 / t359 / 0.36e2 - 0.1e1 / t362 / 0.96e3 + 0.1e1 / t365 / 0.2688e5 - 0.1e1 / t368 / 0.82944e6 + 0.1e1 / t368 / t359 / 0.2838528e8 - 0.1e1 / t368 / t362 / 0.107347968e10 + 0.1e1 / t368 / t365 / 0.445906944e11 - 0.1e1 / t380 / 0.20214448128e13, 0.1e1 - 0.8e1 / 0.3e1 * t384 * (t114 * t387 + 0.2e1 * t384 * (t392 - 0.3e1 / 0.2e1 - 0.2e1 * t389 * (t392 - 0.1e1))))
  t417 = (t235 - t58 / 0.8e1) * t45 * t49 / 0.4e1 - 0.9e1 / 0.2e2 + t59 / 0.36e2
  t418 = t417 ** 2
  t425 = (0.1e1 + 0.5e1 / 0.12e2 * (0.1e2 / 0.81e2 + 0.25e2 / 0.8748e4 * t59) * t45 * t49 * t58 + 0.292e3 / 0.405e3 * t418 - 0.146e3 / 0.135e3 * t417 * t27 * (0.1e1 - t27)) ** (0.1e1 / 0.1e2)
  t446 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (-p.cam_beta * (t35 * (t133 * t135 + 0.35e2 / 0.81e2 * t231 * (-t236 + 0.43662396e-1 * t237 + 0.42296278333333333333e-1 * t58) * t50 * t243 + 0.26329605555555555556e-1 * t343 * t45 * t49 * t53 * t57 * t243) + t352 * t403 * t425) + t35 * (t135 + 0.7e1 / 0.9e1 * (0.1e1 + 0.63943327777777777778e-1 * t59 - 0.5e1 / 0.9e1 * (t236 + 0.256337604e0 * t237 + 0.11867481666666666667e-1 * t58) * t45 * t49) * t243) + t352 * t425))
  res = 0.2e1 * t446
  return res