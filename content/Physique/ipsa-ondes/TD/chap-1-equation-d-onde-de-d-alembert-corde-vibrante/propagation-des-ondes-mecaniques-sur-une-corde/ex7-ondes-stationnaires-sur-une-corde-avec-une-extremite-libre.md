---
title: "Exercice 7 — Ondes stationnaires sur une corde avec une extrémité libre"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td1_PhV212_corrige.pdf) · [📄 Énoncé](/pdfs/td1_PhV212_enonce.pdf) · [📄 Aides (td1_PhV212_aides)](/pdfs/td1_PhV212_aides.pdf) · [📄 Aides (td1_PhV212_exs_maison_aide)](/pdfs/td1_PhV212_exs_maison_aide.pdf) · [📄 PDF (td1_ex1_coup_de_pouce)](/pdfs/td1_ex1_coup_de_pouce.pdf) · [📄 PDF (td1_ex1_solution_detaillee)](/pdfs/td1_ex1_solution_detaillee.pdf) · [📄 Fiche enseignant (td1_PhV212_fiche)](/pdfs/td1_PhV212_fiche.pdf) · [📄 Fiche enseignant (td1_ex1_fiche)](/pdfs/td1_ex1_fiche.pdf) · [📄 Fiche enseignant (td1_exs_maison_fiche)](/pdfs/td1_exs_maison_fiche.pdf)

### Exercice 7. Ondes stationnaires sur une corde avec une extrémité libre *(facultatif)*

On considère une corde de longueur $L$, fixée à l'extrémité $A(x=0)$ et totalement libre de se déplacer transversalement à l'extrémité $B(x=L)$. À l'extrémité libre, la force transversale est nulle, ce qui impose un nœud de tension transversale :
$$T_y(L,t) = F \sin( \alpha( L , t )) \approx F\left.\frac{\partial y}{\partial x}\right|_{x=L} = 0$$

[![](/figures/td1_ex6_phv212_corde_stationaire_libre.svg)](/figures/td1_ex6_phv212_corde_stationaire_libre.svg)

**q1.** Déterminer la forme des modes propres $y_N(x,t)$ de cette corde et exprimer les fréquences propres $f_N$ en fonction de $N$, $c$ et $L$.

> [!tip]- 💡 Coup de pouce
> **Conditions aux limites fixée/libre**
>
> Appliquez $y(0,t) = 0$ (extrémité fixe) et $\left.\dfrac{\partial y}{\partial x}\right|_{x=L} = 0$ (extrémité libre).


> [!success]- ✅ Correction
> **Résultat**
>
> $y_N(x,t) = A_N \sin\left((2N-1)\dfrac{\pi x}{2L}\right)\cos(\omega_N t + \phi_N)$.
> $f_N = (2N-1) f_1$ avec $f_1 = \dfrac{c}{4L}$ ($N \in \mathbb{N}^*$).


> [!example]- 📝 Solution détaillée
> **Démonstration complète**
>
> En partant de la forme séparée $y(x,t) = A\cos(kx+\varphi)\cos(\omega t+\phi)$ :
> 1. En $x=0$ (extrémité fixe) : $y(0,t) = 0 \implies \varphi = \dfrac{\pi}{2} [\pi]$, donc $f(x) \propto \sin(kx)$.
> 2. En $x=L$ (extrémité libre) : $\left.\dfrac{\partial y}{\partial x}\right|_{x=L} = 0 \implies k \cos(kL) = 0$.
>
> Ceci impose $k_N L = (2N-1)\dfrac{\pi}{2}$ avec $N \in \mathbb{N}^*$ (entiers impairs).
> Les longueurs d'onde possibles sont $\lambda_N = \dfrac{4L}{2N-1}$.
>
> Les fréquences propres s'écrivent :
> $$f_N = \frac{c}{\lambda_N} = (2N-1)\frac{c}{4L} = (2N-1)f_1 \quad \text{avec } f_1 = \frac{c}{4L}$$
> Seuls les harmoniques **impairs** de la fréquence fondamentale $f_1$ sont présents.


**q2.** Préciser la position du premier ventre et du premier nœud pour le mode fondamental ($N=1$).

> [!tip]- 💡 Coup de pouce
> **Analyse du mode N=1**
>
> Pour $N=1$, $y_1(x,t) \propto \sin\left(\dfrac{\pi x}{2L}\right)$.


> [!question]- 🔭 Aller plus loin — Licence : Analogie avec les tuyaux sonores
> Une corde fixée/libre est l'analogue mécanique exact d'un tuyau sonore fermé à une extrémité et ouvert à l'autre (tube de Kundt demi-ouvert, instrument à vent comme la clarinette), qui ne produit également que des harmoniques impairs ($f_N = (2N-1)f_1$).


> [!success]- ✅ Correction
> **Résultat**
>
> Nœud en $x=0$ (extrémité fixe).
> Ventre en $x=L$ (extrémité libre, la corde y oscille avec l'amplitude maximale).


> [!example]- 📝 Solution détaillée
> **Interprétation physique**
>
> Pour le fondamental $N=1$, la corde contient un quart de longueur d'onde ($L = \lambda_1/4$) :
>
>
> - **Nœud :** en $x=0$ (déplacement imposé nul).
> - **Ventre :**  en $x=L$ (déplacement transversal maximal, pente spatiale nulle).


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex16-masse-en-bout-de-corde-condition-aux-limites-dynamique-et-equation-transcendante|Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante]] · [[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]]

