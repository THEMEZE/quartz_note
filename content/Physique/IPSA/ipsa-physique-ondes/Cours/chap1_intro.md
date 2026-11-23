---
title: "Chapitre 1 — Ondes mécaniques : introduction"
tags:
  - cours
---

[[physique/IPSA/ipsa-physique-ondes/index|⬅ Physique des ondes]]

*Cours*

<a href="/pdfs/cours_chap1.pdf" target="_blank" rel="noopener">📄 PDF</a>

## 1. Qu'est-ce qu'une onde ?

Une onde est la propagation d'une perturbation dans un milieu, sans
transport de matière : chaque point du milieu oscille autour de sa
position d'équilibre, et c'est cette oscillation qui se propage,
décalée dans le temps, aux points voisins.

> [!info] 💡 Remarque
> Ne pas confondre la vitesse de propagation de l'onde $c$ (vitesse à
> laquelle l'information voyage) avec la vitesse d'un point du milieu
> $v_y = \partial y/\partial t$ (mouvement local, transverse pour une
> onde sur une corde).


## 2. Équation de d'Alembert

Pour une corde tendue de masse linéique $\mu$ et de tension $F$, le
déplacement transversal $y(x,t)$ obéit à :
$$\frac{\partial^2 y}{\partial x^2} = \frac{1}{c^2}\frac{\partial^2 y}{\partial t^2},
\qquad c = \sqrt{F/\mu}.$$

<p style="text-align:center"><a href="/figures/td1_ex1_corde_t0.svg" target="_blank" rel="noopener"><img src="/figures/td1_ex1_corde_t0.svg" alt="Exemple d'onde progressive sinusoïdale sur une corde." loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>

> [!question]- 🔭 Aller plus loin — Master
> Cette équation se généralise en 3D à l'équation de d'Alembert
> $\Delta \psi = \dfrac{1}{c^2}\partial_t^2\psi$, point de départ de
> l'électromagnétisme (équation de propagation du champ dans le vide)
> et de l'acoustique 3D.


## 3. Onde plane progressive sinusoïdale

Solution particulière très utilisée : $y(x,t) = a\cos(kx - \omega t + \phi)$,
avec la relation de dispersion $\omega = kc$ (milieu non dispersif).

<p style="text-align:center"><a href="/animations/anim_corde_onde/animation.gif" target="_blank" rel="noopener"><img src="/animations/anim_corde_onde/animation.gif" alt="animation" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>

[🎞️ Voir en .mp4](/animations/anim_corde_onde/animation.mp4)

**S'entraîner sur ce cours (QCM)**

<a href="/qcm/physique-ondes-ipsa/?c=td1_qcm" target="_blank" rel="noopener">td1_qcm — 3 questions</a><br><a href="/qcm/physique-ondes-ipsa/?c=td1_qcm" target="_blank" rel="noopener"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNjQiIGhlaWdodD0iMTY0IiBjbGFzcz0ic2Vnbm8iPjxwYXRoIHRyYW5zZm9ybT0ic2NhbGUoNCkiIGNsYXNzPSJxcmxpbmUiIHN0cm9rZT0iIzE2MzIzZiIgZD0iTTIgMi41aDdtMSAwaDRtMiAwaDNtMSAwaDJtNCAwaDJtMSAwaDFtMiAwaDdtLTM3IDFoMW01IDBoMW05IDBoM20xIDBoMm0yIDBoMm0yIDBoMW0xIDBoMW01IDBoMW0tMzcgMWgxbTEgMGgzbTEgMGgxbTMgMGgxbTIgMGgzbTEgMGg1bTEgMGgxbTIgMGgxbTEgMGgxbTEgMGgxbTEgMGgzbTEgMGgxbS0zNyAxaDFtMSAwaDNtMSAwaDFtMSAwaDNtMiAwaDFtNCAwaDJtMyAwaDVtMiAwaDFtMSAwaDNtMSAwaDFtLTM3IDFoMW0xIDBoM20xIDBoMW0xIDBoMW00IDBoMW0xIDBoMW0yIDBoMW0yIDBoMW0xIDBoMW0yIDBoM20xIDBoMW0xIDBoM20xIDBoMW0tMzcgMWgxbTUgMGgxbTEgMGgxbTIgMGgxbTEgMGgxbTEgMGgybTEgMGgybTEgMGgybTIgMGgxbTIgMGgxbTEgMGgxbTUgMGgxbS0zNyAxaDdtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDdtLTI5IDFoNm0yIDBoM20zIDBoMm0yIDBoMW0xIDBoMW0tMjkgMWgxbTMgMGgxbTEgMGgzbTEgMGgzbTEgMGgxbTMgMGgybTIgMGgxbTEgMGgxbTQgMGg1bTIgMGgxbS0zNSAxaDFtNSAwaDFtMSAwaDVtMSAwaDJtMSAwaDNtMiAwaDFtMiAwaDJtMyAwaDRtLTM2IDFoNG0yIDBoMm0zIDBoNG0xIDBoM20xIDBoOG0xIDBoMW0xIDBoMW0yIDBoMW0tMzUgMWgxbTIgMGgybTQgMGgybTEgMGgybTMgMGgybTIgMGgxbTEgMGgybTUgMGgzbTEgMGgybS0zNiAxaDJtMiAwaDFtMSAwaDFtMSAwaDFtMiAwaDJtMiAwaDVtMSAwaDRtMiAwaDVtMiAwaDNtLTM3IDFoMW0xIDBoMW0xIDBoMm0xIDBoMW0zIDBoMW0xIDBoMW0xIDBoNG00IDBoMW0xIDBoMW0xIDBoMm0zIDBoMm0tMzQgMWgybTEgMGgybTEgMGgxbTEgMGgxbTEgMGgybTEgMGgzbTIgMGgxbTEgMGg0bTIgMGgxMG0tMzUgMWgybTIgMGgxbTMgMGgxbTEgMGgxbTIgMGgzbTIgMGgzbTIgMGgxbTYgMGgybTEgMGgxbS0zNSAxaDJtNCAwaDFtMiAwaDNtMyAwaDJtMyAwaDFtMyAwaDFtMiAwaDVtMSAwaDRtLTM1IDFoNG0xIDBoMW0xIDBoNG00IDBoM20xIDBoM20xIDBoM20xIDBoMW0xIDBoNW0tMzYgMWgybTMgMGg1bTMgMGgzbTIgMGgybTMgMGgzbTEgMGgxbTIgMGgzbS0zMiAxaDFtMSAwaDNtMSAwaDFtMiAwaDFtMSAwaDFtMSAwaDhtNCAwaDFtMyAwaDFtMyAwaDJtLTM2IDFoMm0xIDBoNG0xIDBoMm0xIDBoMW0yIDBoMW0yIDBoMW0yIDBoM200IDBoMW0xIDBoM20yIDBoMW0tMzIgMWgxbTEgMGgxbTEgMGgybTEgMGgxbTIgMGg0bTMgMGgybTEgMGgxbTEgMGgzbTEgMGgxbTEgMGgybS0zMyAxaDJtMSAwaDJtMSAwaDJtMyAwaDFtMSAwaDNtMSAwaDFtNSAwaDJtMSAwaDJtMSAwaDFtMSAwaDRtLTMzIDFoMW0xIDBoMm00IDBoNW0xIDBoNG0yIDBoM20zIDBoMm0xIDBoMm0xIDBoMW0tMzQgMWgybTMgMGgxbTEgMGgybTEgMGg0bTMgMGgybTIgMGgxbTEgMGgxbTEgMGgxbTIgMGgybTIgMGg0bS0zNyAxaDFtMiAwaDFtMSAwaDFtNCAwaDFtMyAwaDFtMSAwaDFtMiAwaDNtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMiAwaDNtLTMzIDFoNm0xIDBoNW0yIDBoMm0yIDBoMW0yIDBoMm0xIDBoMm0zIDBoMW0xIDBoMW0tMzIgMWgxbTEgMGgxbTIgMGgybTEgMGgxbTIgMGgybTIgMGgxbTMgMGgzbTIgMGgzbTIgMGgxbTIgMGgzbS0zNyAxaDNtMSAwaDFtMSAwaDFtMSAwaDFtMyAwaDZtMSAwaDFtMSAwaDFtMiAwaDFtMyAwaDVtMSAwaDFtMSAwaDFtLTI5IDFoMm0yIDBoMm0xIDBoNG00IDBoMW0xIDBoMW0xIDBoMm0zIDBoMW0yIDBoMW0tMzYgMWg3bTEgMGgxbTEgMGgxbTQgMGgxbTIgMGgxbTIgMGg0bTMgMGgxbTEgMGgxbTEgMGgxbS0zMyAxaDFtNSAwaDFtMiAwaDFtMyAwaDFtMSAwaDJtMiAwaDNtMSAwaDJtMSAwaDFtMSAwaDFtMyAwaDNtLTM1IDFoMW0xIDBoM20xIDBoMW0xIDBoMm0yIDBoMW0yIDBoMm0yIDBoMm0yIDBoMW0xIDBoMW0yIDBoN20xIDBoMW0tMzcgMWgxbTEgMGgzbTEgMGgxbTMgMGg0bTMgMGgzbTEgMGgzbTEgMGgxbTIgMGg0bTEgMGgxbTIgMGgxbS0zNyAxaDFtMSAwaDNtMSAwaDFtMiAwaDVtMSAwaDFtMSAwaDFtMSAwaDFtMyAwaDJtMSAwaDNtMSAwaDFtMiAwaDJtLTM1IDFoMW01IDBoMW0yIDBoMW0xIDBoN20xIDBoNG0xIDBoMW0yIDBoMW0xIDBoMW0yIDBoMW0xIDBoMm0tMzYgMWg3bTEgMGgxbTEgMGgybTEgMGgxbTIgMGgybTIgMGg1bTEgMGgybTEgMGgxbTEgMGgxbTIgMGgzIi8+PC9zdmc+Cg==" width="110" height="110" alt="QR code : td1_qcm — 3 questions" style="image-rendering:pixelated"></a>
