---
title: "Exercice 3 — Équations de mouvement"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/index|⬅ Retour]] · <a href="/pdfs/td3_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td3_PhV110.pdf" target="_blank" rel="noopener">📄 PDF</a> · <a href="/pdfs/td3_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 3. Équations de mouvement

Exercices d'application directe sur le passage entre position $x(t)$, vitesse $v_x(t)$ et accélération $a_x(t)$ par dérivation et intégration avec conditions initiales.

**q1.** Soit une particule de position $x(t) = 6t^2 - t^3$ (en m).



(a) Déterminer $v_x(t)$ et $a_x(t)$.

(b) Décrire le mouvement entre $t=0$ et $t=2\text{ s}$.

(c) Décrire le mouvement entre $t=2\text{ s}$ et $t=4\text{ s}$.

(d) Décrire le mouvement entre $t=4\text{ s}$ et $t=6\text{ s}$.

(e) Décrire le mouvement après $t=6\text{ s}$.

> [!example]- 📝 Solution détaillée
> **Résolution question 1**
>
> (a) $v_x(t) = 12t - 3t^2\text{ m}\cdot\text{s}^{-1}$ ; $a_x(t) = 12 - 6t\text{ m}\cdot\text{s}^{-2}$.
>
> (b) $0 < t < 2\text{ s}$ : $v_x > 0$ et $a_x > 0 \implies$ le mobile se déplace vers les $x$ croissants en **accélérant**.
>
> (c) $2 < t < 4\text{ s}$ : $v_x > 0$ et $a_x < 0 \implies$ le mobile avance toujours vers les $x$ croissants mais en **décélérant**.
>
> (d) $4 < t < 6\text{ s}$ : à $t=4\text{ s}$, $v_x=0$. Pour $4 < t < 6\text{ s}$, $v_x < 0$ et $a_x < 0 \implies$ le mobile a fait demi-tour et se déplace vers les $x$ négatifs en **accélérant**.
>
> (e) $t > 6\text{ s}$ : $x(t) < 0$, $v_x < 0$, $a_x < 0 \implies$ poursuite du mouvement vers les $x$ négatifs en **accélérant**.


**q2.** Soit la position $x(t) = t^3 - 6t^2 - 15t + 40$ (en m).



(a) Déterminer l'instant où la vitesse s'annule.

(b) Calculer la position à cet instant.

(c) Calculer l'accélération à cet instant.

> [!example]- 📝 Solution détaillée
> **Résolution question 2**
>
> (a) $v_x(t) = 3t^2 - 12t - 15$. On cherche $v_x(t)=0 \implies 3(t^2 - 4t - 5) = 0 \implies (t-5)(t+1) = 0$. Comme $t \ge 0$, l'instant cherché est $t = 5\text{ s}$.
>
> (b) $x(5) = 5^3 - 6(5)^2 - 15(5) + 40 = 125 - 150 - 75 + 40 = -60\text{ m}$.
>
> (c) $a_x(t) = 6t - 12 \implies a_x(5) = 6(5) - 12 = 18\text{ m}\cdot\text{s}^{-2}$.


**q3.** L'accélération d'une particule est $a(t) = 12t - 6$ ($\text{m}\cdot\text{s}^{-2}$). À $t=0$, $v_0 = 4\text{ m}\cdot\text{s}^{-1}$ et $x_0 = -3\text{ m}$.



(a) Déterminer l'expression de $v(t)$.

(b) Déterminer l'expression de $x(t)$.

(c) Déterminer l'instant où la vitesse s'annule.

> [!example]- 📝 Solution détaillée
> **Résolution question 3**
>
> (a) $v(t) = \int (12t - 6)\mathrm{d}t = 6t^2 - 6t + v_0 = 6t^2 - 6t + 4\text{ m}\cdot\text{s}^{-1}$.
>
> (b) $x(t) = \int (6t^2 - 6t + 4)\mathrm{d}t = 2t^3 - 3t^2 + 4t + x_0 = 2t^3 - 3t^2 + 4t - 3\text{ m}$.
>
> (c) $v(t) = 0 \implies 6t^2 - 6t + 4 = 0 \implies 3t^2 - 3t + 2 = 0$. Le discriminant $\Delta = 9 - 24 = -15 < 0$. **La vitesse ne s'annule jamais** sur $\mathbb{R}$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/ex1-position-deplacement-vitesse-et-acceleration|Exercice 1 — Position, déplacement, vitesse et accélération]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/ex2-chute-libre-experience-et-modele|Exercice 2 — Chute libre : expérience et modèle]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/ex4-mouvement-rectiligne-uniformement-accelere-mrua|Exercice 4 — Mouvement rectiligne uniformément accéléré (MRUA)]]

