---
title: "Exercice 1 — Célérité d'une onde acoustique dans un fluide parfait"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · <a href="/pdfs/td2_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_PhV212_enonce)</a> · <a href="/pdfs/td2_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_enonce)</a> · <a href="/pdfs/td2_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_aides)</a> · <a href="/pdfs/td2_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_exs_maison_aide)</a>

### Exercice 1. Célérité d'une onde acoustique dans un fluide parfait

Le fluide considéré est de l'air, modélisé comme un fluide parfait, de
rapport des capacités calorifiques $\gamma = C_P/C_V = 1.4$. Masse molaire
$M = 29$ g/mol, température $T = 293$ K, $R = 8.32$ J·mol$^{-1}$·K$^{-1}$.
On rappelle le coefficient de compressibilité $\chi = -\dfrac{1}{V}\dfrac{\partial V}{\partial P}$.

**q1.** On suppose que lors du passage de l'onde acoustique, le fluide subit
une transformation isotherme. En le modélisant comme un gaz parfait,
montrer que $c_T = \sqrt{RT/M}$.

> [!tip]- 💡 Coup de pouce
> Pour un gaz parfait en transformation isotherme, $PV=$ cte à $T$ fixé,
> donc $\chi_T = 1/P$. La célérité du son vérifie en général $c=\sqrt{1/(\rho\chi)}$
> (rappelée dans les prérequis).


**q2.** Calculer $c_T$ numériquement. Est-ce en accord avec la mesure expérimentale ($\approx 340~m/s$) ? Conclure.

> [!tip]- 💡 Coup de pouce
> Attention aux unités SI : $M$ en kg/mol.


**q3.** À quel type de transformation correspond alors la propagation de l'onde sonore ? Définir cette transformation.

> [!tip]- 💡 Coup de pouce
> L'écart avec l'isotherme suggère une transformation trop rapide pour un échange de chaleur : pensez à l'adiabatique réversible (isentropique).


**q4.** Montrer que pour ce type de transformation, $c_S=\sqrt{\gamma RT/M}$. Calculer numériquement et commenter.

> [!tip]- 💡 Coup de pouce
> Pour une transformation isentropique d'un gaz parfait, $PV^\gamma=$ cte, donc $\chi_S=1/(\gamma P)$ (cf. point cours de thermodynamique).


**q5.** Comparer la vitesse du son au niveau de la mer et au sommet de l'Everest (densité de l'air environ 3 fois plus faible, composition chimique identique).

> [!tip]- 💡 Coup de pouce
> $c_S=\sqrt{\gamma P/\rho}$ ; à composition chimique et température fixées, comment $P/\rho$ varie-t-il avec l'altitude ?


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex7-resonateur-de-helmholtz-la-bouteille-qui-chante|Exercice 7 — Résonateur de Helmholtz : la bouteille qui chante]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex4-reflexion-et-transmission-d-une-onde-acoustique-a-une-interface-entre-deux-fluides|Exercice 4 — Réflexion et transmission d'une onde acoustique à une interface entre deux fluides]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]]

