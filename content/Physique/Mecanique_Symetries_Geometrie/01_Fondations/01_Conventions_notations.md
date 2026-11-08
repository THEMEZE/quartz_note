---
title: Conventions et notations
tags:
  - Physique
  - Mathematiques
lang: fr
partie: 0
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Conventions et notations

## 0.1 Symboles logiques

| Symbole | Sens | Usage |
|---|---|---|
| $a \doteq b$ | **définition** de $a$ par $b$ | remplace $:=$ partout dans ce document |
| $a = b$ | égalité **démontrée** / équation | résultat, calcul |
| $a \equiv b$ | identité valable $\forall$ valeur des variables, ou congruence $a\equiv b \pmod n$ | structurel |
| $f \colon X \to Y,\; x \mapsto f(x)$ | **définition d'une application** | convention imposée ici |
| $\simeq,\ \approx$ | approximation | numérique / développement |
| $\propto$ | proportionnel | |

Exemple : $\;q \colon \mathbb R \to \mathscr E,\; t \mapsto q(t)$ ; $\;g \colon E\times E \to \mathbb R,\; (u,v)\mapsto g(u,v) \doteq g_{ij}u^iv^j$.

## 0.2 Objets de base

- $\mathscr E$ : espace affine euclidien de dimension $n$, d'espace directeur $E$, produit scalaire $g=\langle\cdot,\cdot\rangle$ ; points $A,B,M,\dots$ ; $\overrightarrow{AB}\in E$.
- Base orthonormée $(e_i)$ ; indices latins $i,j,\dots\in\{1,\dots,n\}$ ; sommation d'Einstein ; $\delta_{ij}$ Kronecker, $\varepsilon_{i_1\dots i_n}$ Levi-Civita.
- $\mathscr R$ référentiel (repère $(O,(e_i))$ + horloge) ; $\mathscr S$ système matériel ; $G$ centre d'inertie ; $\mathscr R^\ast$ référentiel barycentrique.
- $\vec{\ }$ pour les vecteurs ; les bivecteurs/tenseurs antisymétriques sont notés sans flèche ($M$, $L$, $\Omega$).
- Dérivée temporelle dans $\mathscr R$ : $\dfrac{d\,\cdot}{dt}\Big)_{\mathscr R}$.
- Définitions de $\mathscr T$ : $\mathscr V$ (cinématique), $\mathscr C$ (cinétique), $\mathscr D$ (dynamique), $\mathscr A$ (actions).

## 0.3 Convention de transport « BABAR »

Pour un torseur de **type moment** $\{R;\,M(A)\}$ :
$$
M(B) = M(A) + \overrightarrow{BA}\wedge R \qquad(\textbf{B}\text{ égale }\textbf{A}\text{ plus }\textbf{BA}\text{ vectoriel }\textbf{R}).
$$
Pour un torseur de **type vitesse** $\{\Omega;\,v(A)\}$ : $\;v(B)=v(A)+\Omega\cdot\overrightarrow{AB}$ (en 3D : $=v(A)+\overrightarrow{BA}\wedge\vec\Omega$).

## 0.4 Niveaux

Les sections marquées **[3D]** n'ont de sens qu'en dimension 3 (produit vectoriel, rotationnel, vecteur rotation) ; **[nD]** valent en toute dimension $n\geq 2$ ; **[Mink]** en espace-temps ; ★ = niveau avancé.
