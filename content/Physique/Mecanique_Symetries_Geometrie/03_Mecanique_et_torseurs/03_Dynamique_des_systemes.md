---
title: Dynamique des systèmes matériels fermés
tags:
  - Physique
  - Mathematiques
lang: fr
partie: IV
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Dynamique des systèmes matériels fermés

## IV.1 Axiomes (rappels)

1. Les forces d'interaction sont invariantes par changement de référentiel.
2. Il existe des référentiels galiléens ; ils sont en translation rectiligne uniforme les uns par rapport aux autres.
3. Dans un galiléen, pour un point matériel : $\dfrac{d\vec p}{dt}=\vec F$, $\vec p\doteq m\vec v$ ($m\vec a=\vec F$ si $m$ constante). *Historique* : la forme $\sum\vec F=m\vec a$ est d'Euler (1750) ; Newton écrit $\dot{\vec p}$.
4. **Principe des actions réciproques** (forme forte) : $\vec F_{1\to2}=-\vec F_{2\to1}$, portées par la droite $(M_1M_2)$ ; pour deux systèmes disjoints, le torseur $\mathscr A_{1\to2}=-\mathscr A_{2\to1}$.

> [!warning] Forme faible/forte
> Avec la seule forme faible (forces opposées mais non alignées), $\vec P$ est conservée **mais pas $L$** (IX.3).

## IV.2 Masse, centre d'inertie, mesure

$m_{\mathscr S}=\int dm$, $\overrightarrow{OG}\doteq\frac1m\int\overrightarrow{OM}\,dm$, $\vec P\doteq\int\vec v\,dm=m\,v_G$.

## IV.3 Les quatre torseurs

Pour un système $\mathscr S$ dans $\mathscr R$ (réduits en $A$) :

| Torseur | Résultante | Moment en $A$ | Type |
|---|---|---|---|
| **cinématique** $\mathscr V$ | $\Omega_{\mathscr S/\mathscr R}$ | $v(A)$ | vitesse (solide) |
| **cinétique** $\mathscr C$ | $\vec P=\int\vec v\,dm$ | $L(A)\doteq\int\overrightarrow{AM}\wedge\vec v\,dm$ | moment |
| **dynamique** $\mathscr D$ | $\vec S=\int\vec a\,dm$ (quantité d'accélération) | $D(A)\doteq\int\overrightarrow{AM}\wedge\vec a\,dm$ | moment |
| **actions** $\mathscr A$ | $\vec F=\int d\vec F$ | $\mathfrak M(A)\doteq\int\overrightarrow{AM}\wedge d\vec F$ | moment |

Les trois derniers satisfont **BABAR** :
$$
L(B)=L(A)+\overrightarrow{BA}\wedge\vec P,\quad D(B)=D(A)+\overrightarrow{BA}\wedge\vec S,\quad\mathfrak M(B)=\mathfrak M(A)+\overrightarrow{BA}\wedge\vec F .
$$
Le torseur cinématique est de type vitesse et n'a de sens (loi de Varignon cinématique) que pour un **solide**.

## IV.4 Relations entre les torseurs : la chaîne

$$
\mathscr V\ \xrightarrow{\ \ \mathbb I\ \ }\ \mathscr C\ \xrightarrow{\ \ d/dt\ \ }\ \mathscr D\ \overset{\text{PFD}}=\ \mathscr A .
$$
- $\mathscr V\to\mathscr C$ : opérateur d'inertie (partie V), linéaire pour un solide ; $\vec P=m\,v_G$ (translation) et $L(G)=-\mathbb I_G(\Omega)$ (rotation).
- $\mathscr C\to\mathscr D$ : $\;D(A)=\dfrac{dL(A)}{dt}\Big)_{\mathscr R}+v(A)\wedge\vec P$ pour $A$ mobile, et $\vec S=\dot{\vec P}$ (cf. III.2).
  *Preuve* : $\dot L(A)=\int(\vec v-v_A)\wedge\vec v\,dm+\int\overrightarrow{AM}\wedge\vec a\,dm=-v_A\wedge\vec P+D(A)$ car $\int\vec v\wedge\vec v=0$. $\square$
  Si $A$ est fixe dans $\mathscr R$, ou si $A=G$ (car $v_G\wedge\vec P=m\,v_G\wedge v_G=0$) : $D(A)=\dot L(A)$.
- $\mathscr D=\mathscr A$ : PFD généralisé ; $\mathscr D=\mathscr A^{\text{ext}}$ pour un système fermé dans un galiléen.

## IV.5 Théorèmes généraux (systèmes fermés, $\mathscr R$ galiléen)

**Forces intérieures/extérieures.** $d\vec F_M=d\vec F^{\text{ext}}_M+\int_{M'}d\vec F_{M'\to M}$, avec $d\vec F_{M'\to M}=-d\vec F_{M\to M'}$ (3e loi) et colinéaire à $\overrightarrow{MM'}$ (forme forte).

> [!tip] **TRD** (résultante). $\ \dfrac{d\vec P}{dt}\Big)_{\mathscr R}=\vec F^{\text{ext}}$, i.e. $m\,a_G=\vec F^{\text{ext}}$.
> *Preuve.* Double intégrale des interactions $=\tfrac12\iint(d\vec F_{M'\to M}+d\vec F_{M\to M'})=0$.

> [!tip] **TMD** (moment dynamique). $\ D(A)=\mathfrak M^{\text{ext}}(A)\quad\forall A$.
> *Preuve.* Terme intérieur $\tfrac12\iint(\overrightarrow{AM}\wedge dF_{M'\to M}+\overrightarrow{AM'}\wedge dF_{M\to M'})=\tfrac12\iint\overrightarrow{M'M}\wedge dF_{M'\to M}=0$ par colinéarité.

> [!tip] **TMC** en $A$ fixe : $\dfrac{dL(A)}{dt}\Big)_{\mathscr R}=\mathfrak M^{\text{ext}}(A)$. **TMC\*** barycentrique : $\dfrac{dL^\ast}{dt}\Big)_{\mathscr R}=\mathfrak M^{\text{ext}}(G)$ (valable même si $G$ accélère, car $\overrightarrow{GM}\wedge(-a_G)$ s'intègre en zéro).

**Version torseur.** $\mathscr D_{\mathscr S/\mathscr R}(A)=\mathscr A^{\text{ext}}_{\mathscr S/\mathscr R}(A)$ : deux torseurs égaux en un point le sont partout (transport identique).

## IV.6 Théorèmes de König

$$
L(A)=L^\ast+\overrightarrow{AG}\wedge m\,v_G,\qquad T=\tfrac12m\,v_G^2+T^\ast,\qquad L^\ast\doteq\int\overrightarrow{GM}\wedge v^\ast\,dm,\ T^\ast\doteq\int\tfrac12 v^{\ast2}dm .
$$
Corollaire : l'énergie cinétique de $G$ ne peut pas être dissipée dans un système isolé (X, IX).

## IV.7 Énergie

- **TEC** (point) : $\Delta T=\sum W$, avec $W_{A\to B}(\vec F)=\int_A^B\vec F\cdot d\vec r$. Preuve : $m\vec v\cdot d\vec v=d(\tfrac12mv^2)$.
- Force conservative : $\vec F=-\nabla E_p$ ; **TEM** : $\Delta E_m=W_{\text{nc}}$, $E_m=T+E_p$.
- **Système** : $dT/dt=\mathcal P^{\text{ext}}+\mathcal P^{\text{int}}$ ; pour un solide, $\mathcal P^{\text{int}}=0$ et $\mathcal P^{\text{ext}}=\langle\mathscr A,\mathscr V\rangle$.
- **Viriel en dimension $n$** : pour $V$ homogène de degré $k$ (V(λx)=λ^kV(x)) et mouvement borné, $2\langle T\rangle=k\langle V\rangle$. Kepler ($k=-1$) : $\langle T\rangle=-\tfrac12\langle V\rangle=-E$.
- Trois conservations distinctes : énergie **totale** (toujours), $E_m$ (si $W_{\text{nc}}=0$), $E_c$ (seulement chocs élastiques).

## IV.8 Référentiels non galiléens

TRD/TMD dans $\mathscr R'$ : ajouter aux actions les torseurs d'inertie :
$$
\mathscr A^{\text{ie}}\!:\ \vec F_{ie}=-m\,a_e(G)\ \text{(si champ homogène)},\ \ \mathfrak M_{ie}(A)=\int\overrightarrow{AM}\wedge(-a_e)\,dm,\qquad \mathscr A^{\text{ic}}:\ \int-2\Omega v_r\,dm\ \text{etc.}
$$
Pour le barycentre : $\mathfrak M^{\text{ext}}(G)=\mathfrak M^{\text{ext}}(A)+\overrightarrow{AG}\wedge(-m\,a_G)$.
