"""Generated from mgga_x_mcml.mpl."""

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
  t20 = t19 + 0.1e1
  t22 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t23 = t22 * p.zeta_threshold
  t24 = t20 ** (0.1e1 / 0.3e1)
  t26 = jnp.where(t20 <= p.zeta_threshold, t23, t24 * t20)
  t27 = t6 ** (0.1e1 / 0.3e1)
  t29 = 6 ** (0.1e1 / 0.3e1)
  t30 = jnp.pi ** 2
  t31 = t30 ** (0.1e1 / 0.3e1)
  t32 = t31 ** 2
  t33 = 0.1e1 / t32
  t34 = t29 * t33
  t35 = r0 ** 2
  t36 = r0 ** (0.1e1 / 0.3e1)
  t37 = t36 ** 2
  t40 = s0 / t37 / t35
  t46 = t34 * t40 / (0.65124e1 + t34 * t40 / 0.24e2)
  t48 = t46 / 0.12e2 - 0.1e1
  t49 = t48 ** 2
  t50 = t49 ** 2
  t60 = 0.5e1 / 0.9e1 * (tau0 / t37 / r0 - t40 / 0.8e1) * t29 * t33
  t62 = 0.1e5 < t60
  t63 = jnp.where(t62, t60, 0.1e5)
  t64 = t63 ** 2
  t70 = t64 ** 2
  t74 = jnp.where(t62, 0.1e5, t60)
  t75 = t74 ** 2
  t76 = 0.1e1 - t75
  t77 = t76 ** 2
  t79 = t75 * t74
  t86 = jnp.where(0.1e5 <= t60, -0.1e1 / 0.4e1 + 0.3e1 / 0.4e1 / t64 + 0.1e1 / t64 / t63 / 0.16e2 - 0.3e1 / 0.4e1 / t70, t77 * t76 / (0.1e1 + t79 * (0.1e1 + 0.4e1 * t79)))
  t87 = t86 ** 2
  t88 = t87 ** 2
  t89 = t88 * t87
  t94 = t88 * t86
  t96 = t87 * t86
  t98 = t88 * t96
  t100 = t50 * t48
  t102 = t49 * t48
  t104 = t50 * t102
  t106 = t50 * t49
  t109 = -0.1e1 / 0.2e1 + 0.3e1 / 0.2e1 * t49
  t113 = 0.63e2 / 0.8e1 * t94 - 0.35e2 / 0.4e1 * t96 + 0.15e2 / 0.8e1 * t86
  t119 = -0.5e1 / 0.16e2 + 0.231e3 / 0.16e2 * t89 - 0.315e3 / 0.16e2 * t88 + 0.105e3 / 0.16e2 * t87
  t126 = 0.429e3 / 0.16e2 * t98 - 0.693e3 / 0.16e2 * t94 + 0.315e3 / 0.16e2 * t96 - 0.35e2 / 0.16e2 * t86
  t129 = -0.1047053293912749375e-2 * t50 - 0.37102687351218925312e0 * t49 - 0.28551704175417885e-1 * t89 + 0.294397262786656575e-1 * t88 - 0.58828844909941371e-2 * t87 + 0.20748619661467272631e0 * t86 + 0.8753451580964013919e-1 * t94 - 0.32121495135261672812e-1 * t96 - 0.67464548655177289688e-1 * t98 - 0.15887583418757175563e-1 * t100 + 0.7416880187036191562e-2 * t102 + 0.15682422300093093188e-1 * t104 + 0.22419222998949863625e-1 * t106 - 0.1189668304951413e-2 * t109 * t113 - 0.1288306127279617e-2 * t109 * t119 - 0.1175614476758423e-2 * t109 * t126
  t132 = 0.5e1 / 0.2e1 * t102 - t46 / 0.8e1 + 0.3e1 / 0.2e1
  t139 = 0.3e1 / 0.8e1 + 0.35e2 / 0.8e1 * t88 - 0.15e2 / 0.4e1 * t87
  t146 = 0.5e1 / 0.2e1 * t96 - 0.3e1 / 0.2e1 * t86
  t150 = -0.1e1 / 0.2e1 + 0.3e1 / 0.2e1 * t87
  t173 = -0.1030571429426108e-1 * t132 * t86 + 0.1179363564823021e0 * t48 * t86 - 0.2494950550547465e-2 * t132 * t139 + 0.1672905908063297e-3 * t132 * t113 + 0.3712786171321043e-2 * t132 * t146 - 0.7090296813211244e-3 * t132 * t150 + 0.179463855686441e-2 * t48 * t150 + 0.2125332357775206e-2 * t48 * t146 + 0.2915285520983635e-2 * t48 * t139 + 0.2007295399058147e-2 * t48 * t113 + 0.1491587478361034e-2 * t48 * t119 + 0.1940164714223896e-2 * t48 * t126 - 0.1437960658302686e-1 * t109 * t86 - 0.1153807045825489e-2 * t109 * t150 - 0.9641371299507833e-3 * t109 * t146 - 0.1863882881010248e-2 * t109 * t139
  t178 = 0.63e2 / 0.8e1 * t100 - 0.35e2 / 0.4e1 * t102 + 0.5e1 / 0.32e2 * t46 - 0.15e2 / 0.8e1
  t185 = 0.3e1 / 0.8e1 + 0.35e2 / 0.8e1 * t50 - 0.15e2 / 0.4e1 * t49
  t207 = -0.5e1 / 0.16e2 + 0.231e3 / 0.16e2 * t106 - 0.315e3 / 0.16e2 * t50 + 0.105e3 / 0.16e2 * t49
  t218 = 0.6670848599065867e-2 * t178 * t150 - 0.257733338272708e-3 * t178 * t86 + 0.2776060240069905e-3 * t185 * t119 + 0.3212943141118693e-5 * t185 * t126 - 0.2721968500889238e-3 * t185 * t113 + 0.4187827907710905e-3 * t185 * t139 + 0.1282471852770764e-2 * t185 * t146 + 0.1683215086686233e-1 * t185 * t86 + 0.137028863545747e-3 * t185 * t150 + 0.4312411759243052e-3 * t132 * t126 - 0.6058496834176058e-3 * t132 * t119 + 0.4230264400260503e-3 * t207 * t139 - 0.6510071882485726e-2 * t207 * t146 + 0.2334616776649133e-2 * t207 * t86 - 0.5498112922165805e-2 * t207 * t150 - 0.2202759704065197e-3 * t178 * t126
  t231 = 0.429e3 / 0.16e2 * t104 - 0.693e3 / 0.16e2 * t100 + 0.315e3 / 0.16e2 * t102 - 0.35e2 / 0.192e3 * t46 + 0.35e2 / 0.16e2
  t253 = 0.13502664484515602222e1 - 0.1622621390953226e-2 * t178 * t119 - 0.5869916483960576e-3 * t178 * t113 + 0.2262886186270548e-3 * t178 * t146 - 0.1009981263546227e-2 * t178 * t139 + 0.1522474179598972e-2 * t231 * t113 + 0.1243327883803539e-1 * t231 * t146 + 0.1421391023843761e-2 * t231 * t150 + 0.3837976998664341e-3 * t231 * t86 + 0.4260858412001439e-3 * t207 * t119 + 0.3807158595350892e-3 * t207 * t126 + 0.1136485825094485e-2 * t207 * t113 - 0.3695503801501715e-3 * t231 * t126 - 0.3682519432462936e-3 * t231 * t119 + 0.245752591853626e-2 * t231 * t139 - 0.13465921726261020182e-1 * t46
  t259 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (t129 + t173 + t218 + t253))
  t261 = jnp.where(t10, t15, -t17)
  t262 = jnp.where(t14, t11, t261)
  t263 = t262 + 0.1e1
  t265 = t263 ** (0.1e1 / 0.3e1)
  t267 = jnp.where(t263 <= p.zeta_threshold, t23, t265 * t263)
  t269 = r1 ** 2
  t270 = r1 ** (0.1e1 / 0.3e1)
  t271 = t270 ** 2
  t274 = s2 / t271 / t269
  t280 = t34 * t274 / (0.65124e1 + t34 * t274 / 0.24e2)
  t282 = t280 / 0.12e2 - 0.1e1
  t283 = t282 ** 2
  t284 = t283 ** 2
  t287 = t284 * t283
  t296 = 0.5e1 / 0.9e1 * (tau1 / t271 / r1 - t274 / 0.8e1) * t29 * t33
  t298 = 0.1e5 < t296
  t299 = jnp.where(t298, t296, 0.1e5)
  t300 = t299 ** 2
  t306 = t300 ** 2
  t310 = jnp.where(t298, 0.1e5, t296)
  t311 = t310 ** 2
  t312 = 0.1e1 - t311
  t313 = t312 ** 2
  t315 = t311 * t310
  t322 = jnp.where(0.1e5 <= t296, -0.1e1 / 0.4e1 + 0.3e1 / 0.4e1 / t300 + 0.1e1 / t300 / t299 / 0.16e2 - 0.3e1 / 0.4e1 / t306, t313 * t312 / (0.1e1 + t315 * (0.1e1 + 0.4e1 * t315)))
  t323 = t322 ** 2
  t325 = t323 ** 2
  t326 = t325 * t323
  t330 = t325 * t322
  t332 = t323 * t322
  t334 = t325 * t332
  t336 = t284 * t282
  t338 = t283 * t282
  t340 = t284 * t338
  t343 = -0.1e1 / 0.2e1 + 0.3e1 / 0.2e1 * t283
  t345 = -0.1e1 / 0.2e1 + 0.3e1 / 0.2e1 * t323
  t352 = 0.429e3 / 0.16e2 * t334 - 0.693e3 / 0.16e2 * t330 + 0.315e3 / 0.16e2 * t332 - 0.35e2 / 0.16e2 * t322
  t358 = -0.5e1 / 0.16e2 + 0.231e3 / 0.16e2 * t326 - 0.315e3 / 0.16e2 * t325 + 0.105e3 / 0.16e2 * t323
  t361 = -0.1047053293912749375e-2 * t284 - 0.37102687351218925312e0 * t283 + 0.22419222998949863625e-1 * t287 - 0.58828844909941371e-2 * t323 - 0.28551704175417885e-1 * t326 + 0.294397262786656575e-1 * t325 + 0.20748619661467272631e0 * t322 + 0.8753451580964013919e-1 * t330 - 0.32121495135261672812e-1 * t332 - 0.67464548655177289688e-1 * t334 - 0.15887583418757175563e-1 * t336 + 0.7416880187036191562e-2 * t338 + 0.15682422300093093188e-1 * t340 - 0.1153807045825489e-2 * t343 * t345 + 0.1940164714223896e-2 * t282 * t352 + 0.1491587478361034e-2 * t282 * t358
  t364 = 0.3e1 / 0.8e1 + 0.35e2 / 0.8e1 * t325 - 0.15e2 / 0.4e1 * t323
  t370 = 0.63e2 / 0.8e1 * t330 - 0.35e2 / 0.4e1 * t332 + 0.15e2 / 0.8e1 * t322
  t375 = 0.5e1 / 0.2e1 * t332 - 0.3e1 / 0.2e1 * t322
  t384 = 0.5e1 / 0.2e1 * t338 - t280 / 0.8e1 + 0.3e1 / 0.2e1
  t407 = 0.2915285520983635e-2 * t282 * t364 + 0.2007295399058147e-2 * t282 * t370 + 0.2125332357775206e-2 * t282 * t375 + 0.179463855686441e-2 * t282 * t345 + 0.1179363564823021e0 * t282 * t322 + 0.4312411759243052e-3 * t384 * t352 - 0.6058496834176058e-3 * t384 * t358 + 0.1672905908063297e-3 * t384 * t370 + 0.3712786171321043e-2 * t384 * t375 - 0.2494950550547465e-2 * t384 * t364 - 0.7090296813211244e-3 * t384 * t345 - 0.1030571429426108e-1 * t384 * t322 - 0.1288306127279617e-2 * t343 * t358 - 0.1175614476758423e-2 * t343 * t352 - 0.1189668304951413e-2 * t343 * t370 - 0.1863882881010248e-2 * t343 * t364
  t416 = 0.63e2 / 0.8e1 * t336 - 0.35e2 / 0.4e1 * t338 + 0.5e1 / 0.32e2 * t280 - 0.15e2 / 0.8e1
  t425 = 0.3e1 / 0.8e1 + 0.35e2 / 0.8e1 * t284 - 0.15e2 / 0.4e1 * t283
  t443 = -0.5e1 / 0.16e2 + 0.231e3 / 0.16e2 * t287 - 0.315e3 / 0.16e2 * t284 + 0.105e3 / 0.16e2 * t283
  t452 = -0.9641371299507833e-3 * t343 * t375 - 0.1437960658302686e-1 * t343 * t322 - 0.1009981263546227e-2 * t416 * t364 + 0.6670848599065867e-2 * t416 * t345 - 0.257733338272708e-3 * t416 * t322 + 0.2776060240069905e-3 * t425 * t358 + 0.3212943141118693e-5 * t425 * t352 - 0.2721968500889238e-3 * t425 * t370 + 0.4187827907710905e-3 * t425 * t364 + 0.1282471852770764e-2 * t425 * t375 + 0.1683215086686233e-1 * t425 * t322 + 0.137028863545747e-3 * t425 * t345 + 0.1136485825094485e-2 * t443 * t370 + 0.4230264400260503e-3 * t443 * t364 - 0.6510071882485726e-2 * t443 * t375 + 0.2334616776649133e-2 * t443 * t322
  t467 = 0.429e3 / 0.16e2 * t340 - 0.693e3 / 0.16e2 * t336 + 0.315e3 / 0.16e2 * t338 - 0.35e2 / 0.192e3 * t280 + 0.35e2 / 0.16e2
  t487 = 0.13502664484515602222e1 - 0.5498112922165805e-2 * t443 * t345 - 0.2202759704065197e-3 * t416 * t352 - 0.1622621390953226e-2 * t416 * t358 - 0.5869916483960576e-3 * t416 * t370 + 0.2262886186270548e-3 * t416 * t375 + 0.245752591853626e-2 * t467 * t364 + 0.1522474179598972e-2 * t467 * t370 + 0.1243327883803539e-1 * t467 * t375 + 0.1421391023843761e-2 * t467 * t345 + 0.3837976998664341e-3 * t467 * t322 + 0.4260858412001439e-3 * t443 * t358 + 0.3807158595350892e-3 * t443 * t352 - 0.3695503801501715e-3 * t467 * t352 - 0.3682519432462936e-3 * t467 * t358 - 0.13465921726261020182e-1 * t280
  t493 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t267 * t27 * (t361 + t407 + t452 + t487))
  res = t259 + t493
  return res

def unpol(r0, s0, l0, tau0, params, p):
  t3 = 3 ** (0.1e1 / 0.3e1)
  t4 = jnp.pi ** (0.1e1 / 0.3e1)
  t7 = 0.1e1 <= p.zeta_threshold
  t8 = p.zeta_threshold - 0.1e1
  t10 = jnp.where(t7, -t8, 0)
  t11 = jnp.where(t7, t8, t10)
  t12 = t11 + 0.1e1
  t14 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t16 = t12 ** (0.1e1 / 0.3e1)
  t18 = jnp.where(t12 <= p.zeta_threshold, t14 * p.zeta_threshold, t16 * t12)
  t19 = r0 ** (0.1e1 / 0.3e1)
  t21 = 6 ** (0.1e1 / 0.3e1)
  t22 = jnp.pi ** 2
  t23 = t22 ** (0.1e1 / 0.3e1)
  t24 = t23 ** 2
  t25 = 0.1e1 / t24
  t26 = t21 * t25
  t28 = 2 ** (0.1e1 / 0.3e1)
  t29 = t28 ** 2
  t30 = r0 ** 2
  t31 = t19 ** 2
  t33 = 0.1e1 / t31 / t30
  t36 = s0 * t29 * t33
  t42 = t26 * s0 * t29 * t33 / (0.65124e1 + t26 * t36 / 0.24e2)
  t44 = t42 / 0.12e2 - 0.1e1
  t45 = t44 ** 2
  t46 = t45 ** 2
  t49 = t46 * t45
  t59 = 0.5e1 / 0.9e1 * (tau0 * t29 / t31 / r0 - t36 / 0.8e1) * t21 * t25
  t61 = 0.1e5 < t59
  t62 = jnp.where(t61, t59, 0.1e5)
  t63 = t62 ** 2
  t69 = t63 ** 2
  t73 = jnp.where(t61, 0.1e5, t59)
  t74 = t73 ** 2
  t75 = 0.1e1 - t74
  t76 = t75 ** 2
  t78 = t74 * t73
  t85 = jnp.where(0.1e5 <= t59, 0.3e1 / 0.4e1 / t63 + 0.1e1 / t63 / t62 / 0.16e2 - 0.3e1 / 0.4e1 / t69 - 0.1e1 / 0.4e1, t76 * t75 / (0.1e1 + t78 * (0.1e1 + 0.4e1 * t78)))
  t86 = t85 ** 2
  t87 = t86 * t85
  t88 = t86 ** 2
  t89 = t88 * t87
  t91 = t88 * t85
  t97 = t88 * t86
  t99 = t45 * t44
  t101 = t46 * t44
  t103 = t46 * t99
  t106 = -0.1e1 / 0.2e1 + 0.3e1 / 0.2e1 * t86
  t111 = 0.5e1 / 0.2e1 * t87 - 0.3e1 / 0.2e1 * t85
  t116 = 0.3e1 / 0.8e1 + 0.35e2 / 0.8e1 * t88 - 0.15e2 / 0.4e1 * t86
  t119 = -0.1047053293912749375e-2 * t46 - 0.37102687351218925312e0 * t45 + 0.22419222998949863625e-1 * t49 - 0.67464548655177289688e-1 * t89 + 0.8753451580964013919e-1 * t91 - 0.32121495135261672812e-1 * t87 + 0.20748619661467272631e0 * t85 + 0.294397262786656575e-1 * t88 - 0.58828844909941371e-2 * t86 - 0.28551704175417885e-1 * t97 + 0.7416880187036191562e-2 * t99 - 0.15887583418757175563e-1 * t101 + 0.15682422300093093188e-1 * t103 + 0.179463855686441e-2 * t44 * t106 + 0.2125332357775206e-2 * t44 * t111 + 0.2915285520983635e-2 * t44 * t116
  t123 = 0.63e2 / 0.8e1 * t91 - 0.35e2 / 0.4e1 * t87 + 0.15e2 / 0.8e1 * t85
  t129 = -0.5e1 / 0.16e2 + 0.231e3 / 0.16e2 * t97 - 0.315e3 / 0.16e2 * t88 + 0.105e3 / 0.16e2 * t86
  t136 = 0.429e3 / 0.16e2 * t89 - 0.693e3 / 0.16e2 * t91 + 0.315e3 / 0.16e2 * t87 - 0.35e2 / 0.16e2 * t85
  t140 = -0.1e1 / 0.2e1 + 0.3e1 / 0.2e1 * t45
  t157 = 0.5e1 / 0.2e1 * t99 - t42 / 0.8e1 + 0.3e1 / 0.2e1
  t171 = 0.63e2 / 0.8e1 * t101 - 0.35e2 / 0.4e1 * t99 + 0.5e1 / 0.32e2 * t42 - 0.15e2 / 0.8e1
  t174 = 0.2007295399058147e-2 * t44 * t123 + 0.1491587478361034e-2 * t44 * t129 + 0.1940164714223896e-2 * t44 * t136 - 0.1437960658302686e-1 * t140 * t85 - 0.1153807045825489e-2 * t140 * t106 - 0.9641371299507833e-3 * t140 * t111 - 0.1863882881010248e-2 * t140 * t116 - 0.1189668304951413e-2 * t140 * t123 - 0.1288306127279617e-2 * t140 * t129 - 0.1175614476758423e-2 * t140 * t136 - 0.1030571429426108e-1 * t157 * t85 - 0.7090296813211244e-3 * t157 * t106 + 0.3712786171321043e-2 * t157 * t111 - 0.2494950550547465e-2 * t157 * t116 + 0.1179363564823021e0 * t44 * t85 - 0.257733338272708e-3 * t171 * t85
  t178 = 0.3e1 / 0.8e1 + 0.35e2 / 0.8e1 * t46 - 0.15e2 / 0.4e1 * t45
  t202 = -0.5e1 / 0.16e2 + 0.231e3 / 0.16e2 * t49 - 0.315e3 / 0.16e2 * t46 + 0.105e3 / 0.16e2 * t45
  t215 = 0.3212943141118693e-5 * t178 * t136 + 0.2776060240069905e-3 * t178 * t129 - 0.2721968500889238e-3 * t178 * t123 + 0.1282471852770764e-2 * t178 * t111 + 0.4187827907710905e-3 * t178 * t116 + 0.137028863545747e-3 * t178 * t106 + 0.1683215086686233e-1 * t178 * t85 - 0.6058496834176058e-3 * t157 * t129 + 0.4312411759243052e-3 * t157 * t136 + 0.1672905908063297e-3 * t157 * t123 - 0.5498112922165805e-2 * t202 * t106 + 0.2334616776649133e-2 * t202 * t85 - 0.2202759704065197e-3 * t171 * t136 - 0.5869916483960576e-3 * t171 * t123 - 0.1622621390953226e-2 * t171 * t129 - 0.1009981263546227e-2 * t171 * t116
  t224 = 0.429e3 / 0.16e2 * t103 - 0.693e3 / 0.16e2 * t101 + 0.315e3 / 0.16e2 * t99 - 0.35e2 / 0.192e3 * t42 + 0.35e2 / 0.16e2
  t250 = 0.13502664484515602222e1 + 0.2262886186270548e-3 * t171 * t111 + 0.6670848599065867e-2 * t171 * t106 + 0.1243327883803539e-1 * t224 * t111 + 0.1421391023843761e-2 * t224 * t106 + 0.3837976998664341e-3 * t224 * t85 + 0.3807158595350892e-3 * t202 * t136 + 0.4260858412001439e-3 * t202 * t129 + 0.1136485825094485e-2 * t202 * t123 - 0.6510071882485726e-2 * t202 * t111 + 0.4230264400260503e-3 * t202 * t116 - 0.3682519432462936e-3 * t224 * t129 - 0.3695503801501715e-3 * t224 * t136 + 0.1522474179598972e-2 * t224 * t123 + 0.245752591853626e-2 * t224 * t116 - 0.13465921726261020182e-1 * t42
  t256 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (t119 + t174 + t215 + t250))
  res = 0.2e1 * t256
  return res