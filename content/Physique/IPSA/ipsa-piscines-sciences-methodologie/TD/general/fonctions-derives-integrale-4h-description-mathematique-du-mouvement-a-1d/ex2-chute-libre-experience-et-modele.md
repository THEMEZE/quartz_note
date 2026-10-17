---
title: "Exercice 2 — Chute libre : expérience et modèle"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/index|⬅ Retour]] · <a href="/pdfs/td3_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td3_PhV110.pdf" target="_blank" rel="noopener">📄 PDF</a> · <a href="/pdfs/td3_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 2. Chute libre : expérience et modèle

Étude expérimentale puis théorique du mouvement de chute libre d'une bille de billard lâchée sans vitesse initiale. Le référentiel terrestre est supposé galiléen.

**q1.** **Étude expérimentale**

Une bille est photographiée toutes les $\tau = 1/30\text{ s}$.



(a) Compléter le tableau de relevés des positions $x(t)$ et vitesses moyennes $v_x(t)$.

(b) Représenter $x(t)$ : comment évolue $x$ au cours du temps ?

(c) Représenter $x(t^2)$ et en déduire une expression mathématique de $x(t)$.

(d) Représenter $v_x(t)$ et donner son expression mathématique.

(e) Déterminer par le calcul $v_x(t)$ à partir de l'expression de $x(t)$.

(f) Déterminer l'accélération $a_x(t)$ graphiquement puis par le calcul. Qualifier le mouvement.

> [!example]- 📝 Solution détaillée
> **Résolution expérimentale**
>
> (a) Positions : $x(0)=0\text{ m}$, $x(\tau) \approx 0,005\text{ m}$, $x(2\tau) \approx 0,022\text{ m}$, $x(3\tau) \approx 0,049\text{ m}$, $x(4\tau) \approx 0,087\text{ m}$.
>
> (b) $x(t)$ présente une forme paraboloïdale : la position augmente de plus en plus vite.
>
> (c) $x(t^2)$ est une droite passant par l'origine de pente $k \approx 4,9\text{ m}\cdot\text{s}^{-2} \implies x(t) = k t^2$.
>
> (d) $v_x(t)$ est une droite linéaire : $v_x(t) = a t$ avec $a \approx 9,8\text{ m}\cdot\text{s}^{-2}$.
>
> (e) Par calcul : $v_x(t) = \frac{\mathrm{d}x}{\mathrm{d}t} = 2k t = 9,8 t\text{ m}\cdot\text{s}^{-1}$.
>
> (f) $a_x = \frac{\mathrm{d}v_x}{\mathrm{d}t} \approx 9,8\text{ m}\cdot\text{s}^{-2} = \text{Cte}$. Le mouvement est **rectiligne uniformément accéléré (MRUA)**.


**q2.** **Modélisation théorique**

Une masse $m$ est en chute libre sans vitesse initiale dans le champ $\vec{g}$.



(a) Définir un repère adapté.

(b) Bilan des forces.

(c) Appliquer le PFD et déduire l'accélération.

(d) Intégrer pour obtenir $v_x(t)$ et $x(t)$.

(e) Estimer l'intensité de la pesanteur $g$ depuis l'étude expérimentale.

> [!example]- 📝 Solution détaillée
> **Résolution théorique**
>
> (a) Repère axe vertical $(Ox)$ dirigé vers le bas, origine $O$ au point de lâcher.
>
> (b) Seul le poids $\vec{P} = m\vec{g}$ s'exerce (frottements négligés).
>
> (c) PFD : $m\vec{a} = m\vec{g} \implies \vec{a} = \vec{g} \implies a_x = g$.
>
> (d) $v_x(t) = g t + v_{x,0} = g t$ ; $x(t) = \frac{1}{2}g t^2 + x_0 = \frac{1}{2}g t^2$.
>
> (e) Par identification avec $x(t) = k t^2$ où $k \approx 4,9\text{ m}\cdot\text{s}^{-2}$, on a $g = 2k \approx 9,8\text{ m}\cdot\text{s}^{-2}$.


**q3.** **Applications**



(a) Une pierre tombe dans un puits et touche l'eau après $1,5\text{ s}$. Déterminer la profondeur du puits et la vitesse d'impact ($g = 9,81\text{ m}\cdot\text{s}^{-2}$).

(b) Calculer la durée de chute lors d'une tombe d'une chaise haute de $0,5\text{ m}$.

> [!example]- 📝 Solution détaillée
> **Calculs d'applications**
>
> (a) Profondeur $h = \frac{1}{2}g t^2 = 0,5 \times 9,81 \times 1,5^2 \approx 11,04\text{ m}$. Vitesse $v = g t = 9,81 \times 1,5 \approx 14,72\text{ m}\cdot\text{s}^{-1}$.
>
> (b) $h = \frac{1}{2}g t^2 \implies t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{2 \times 0,5}{9,81}} \approx 0,32\text{ s}$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/ex1-position-deplacement-vitesse-et-acceleration|Exercice 1 — Position, déplacement, vitesse et accélération]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/ex3-equations-de-mouvement|Exercice 3 — Équations de mouvement]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/ex4-mouvement-rectiligne-uniformement-accelere-mrua|Exercice 4 — Mouvement rectiligne uniformément accéléré (MRUA)]]

