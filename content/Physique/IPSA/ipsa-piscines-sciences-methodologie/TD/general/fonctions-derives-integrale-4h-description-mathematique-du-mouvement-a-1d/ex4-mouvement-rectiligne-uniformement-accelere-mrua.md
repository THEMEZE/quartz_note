---
title: "Exercice 4 — Mouvement rectiligne uniformément accéléré (MRUA)"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/index|⬅ Retour]] · <a href="/pdfs/td3_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td3_PhV110.pdf" target="_blank" rel="noopener">📄 PDF</a> · <a href="/pdfs/td3_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 4. Mouvement rectiligne uniformément accéléré (MRUA)

Exercices pratiques sur l'utilisation des équations cinématiques du MRUA dans des contextes réels (avion, camion, voiture).

**q1.** Un avion commence sa course au repos ($v_A = 0$) en $A$. Il décolle $30\text{ s}$ plus tard en $B$ avec une accélération constante $a$. La distance $AB = 900\text{ m}$.



(a) Calculer l'accélération $a$.

(b) Calculer la vitesse de décollage $v_B$.

> [!example]- 📝 Solution détaillée
> **Résolution avion**
>
> (a) $x(t) = \frac{1}{2}a t^2 \implies 900 = \frac{1}{2} a (30)^2 = 450 a \implies a = \frac{900}{450} = 2\text{ m}\cdot\text{s}^{-2}$.
>
> (b) $v_B = a t = 2 \times 30 = 60\text{ m}\cdot\text{s}^{-1}$ (soit $216\text{ km}\cdot\text{h}^{-1}$).


**q2.** Un camion parcourt $164\text{ m}$ en $8\text{ s}$ lors d'une décélération constante de $0,5\text{ m}\cdot\text{s}^{-2}$.



(a) Calculer sa vitesse initiale.

(b) Calculer sa vitesse finale.

(c) Calculer la distance parcourue pendant le premier intervalle de $0,6\text{ s}$.

> [!example]- 📝 Solution détaillée
> **Résolution camion**
>
> (a) $a = -0,5\text{ m}\cdot\text{s}^{-2}$. $x(t) = \frac{1}{2}a t^2 + v_0 t \implies 164 = \frac{1}{2}(-0,5)(8)^2 + v_0(8) \implies 164 = -16 + 8 v_0 \implies v_0 = 22,5\text{ m}\cdot\text{s}^{-1}$.
>
> (b) $v_{\text{finale}} = a t + v_0 = -0,5(8) + 22,5 = 18,5\text{ m}\cdot\text{s}^{-1}$.
>
> (c) $x(0,6) = \frac{1}{2}(-0,5)(0,6)^2 + 22,5(0,6) = -0,09 + 13,5 = 13,41\text{ m}$.


**q3.** Une voiture a une vitesse $v_A = 50\text{ km}\cdot\text{h}^{-1}$ au point $A$ et subit une accélération de $a = 3\text{ m}\cdot\text{s}^{-2}$.



(a) Calculer le temps mis pour atteindre le point $B$ situé à $50\text{ m}$ de $A$.

(b) Calculer la vitesse au point $B$.

> [!example]- 📝 Solution détaillée
> **Résolution voiture**
>
> (a) $v_A = \frac{50}{3,6} \approx 13,89\text{ m}\cdot\text{s}^{-1}$. Equation de position : $1,5 t^2 + 13,89 t - 50 = 0$.
>         $\Delta = (13,89)^2 - 4(1,5)(-50) \approx 192,9 + 300 = 492,9 \implies \sqrt{\Delta} \approx 22,20$.
>         $t = \frac{-13,89 + 22,20}{3} \approx 2,77\text{ s}$.
>
> (b) $v_B = a t + v_A = 3(2,77) + 13,89 = 22,20\text{ m}\cdot\text{s}^{-1}$ (soit $\approx 79,9\text{ km}\cdot\text{h}^{-1}$).


**q4.** Tracer et commenter les caractéristiques des courbes $x(t)$, $v_x(t)$ et $a_x(t)$ pour les trois mouvements.

> [!example]- 📝 Solution détaillée
> **Allure des courbes MRUA**
>
> - **$a_x(t)$** : Droite horizontale d'ordonnée égale à l'accélération constante.
> - **$v_x(t)$** : Droite affine de pente $a_x$ et d'ordonnée à l'origine $v_0$.
> - {\bf$x(t)$} : Parabole orientée vers le haut ($a_x > 0$) ou vers le bas ($a_x < 0$), avec une tangente en $t=0$ de pente égale à $v_0$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/ex1-position-deplacement-vitesse-et-acceleration|Exercice 1 — Position, déplacement, vitesse et accélération]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/ex2-chute-libre-experience-et-modele|Exercice 2 — Chute libre : expérience et modèle]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/ex3-equations-de-mouvement|Exercice 3 — Équations de mouvement]]

