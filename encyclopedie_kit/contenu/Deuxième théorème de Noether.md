## 1. Énoncé

Soit une action $S[\phi]$ invariante sous des transformations $\delta\phi_A=(D\varepsilon)_A$ dépendant de **fonctions arbitraires** $\varepsilon(x)$ et de leurs dérivées (symétrie **locale** ou de jauge), $D$ un opérateur différentiel.

>[!tip]+ **Deuxième théorème de Noether.** Les expressions d'Euler–Lagrange $E^A=\delta S/\delta\phi_A$ vérifient des **identités** $D^\dagger E=0$ (identités de Noether), **sans utiliser les équations du mouvement**.
>
>*Démonstration (idée).* $0=\delta S=\int E^A(D\varepsilon)_A\,d^dx=\int\varepsilon\,(D^\dagger E)\,d^dx+\text{terme de bord}$, où $D^\dagger$ est l'adjoint formel. Comme $\varepsilon$ est arbitraire à support compact, $D^\dagger E=0$. $\square$

Conséquence : les équations $E^A=0$ ne sont **pas indépendantes** : elles ne déterminent pas toutes les évolutions (indétermination = redondance de jauge).

## 2. Exemples

>[!example]+ Électromagnétisme
>$\delta A_\mu=\partial_\mu\varepsilon$, $E^\nu=\delta S/\delta A_\nu=\partial_\mu F^{\mu\nu}$ (sans source) : l'identité de Noether est
>$$
>\partial_\nu E^\nu=\partial_\nu\partial_\mu F^{\mu\nu}\equiv0 .
>$$
>Avec matière, $E^\nu=\partial_\mu F^{\mu\nu}-j^\nu$ et l'identité devient $\partial_\nu j^\nu=0$ sur la couche de masse : **conservation de la charge**.

>[!example]+ Gravitation
>$\delta g_{\mu\nu}=\nabla_\mu\xi_\nu+\nabla_\nu\xi_\mu$ (difféomorphismes) donne l'**identité de Bianchi contractée** $\nabla^\mu G_{\mu\nu}\equiv0$ et, avec matière, $\nabla^\mu T_{\mu\nu}=0$.

## 3. Lien avec le premier théorème

Pour une symétrie locale, le courant associé à la partie **globale** ($\varepsilon=$ const) est $J^\mu=\partial_\nu S^{[\nu\mu]}+(\text{termes}\propto E)$ : c'est un **courant trivial**, dont la charge est un terme de bord (loi de Gauss). C'est pourquoi, en jauge, les charges vivent à l'infini (charge électrique, masse ADM).

## 4. Fil de Noether

- Symétrie **globale** ⇒ **charge conservée** ([[Théorème de Noether]], [[Théorème de Noether pour les champs]]).
- Symétrie **locale** ⇒ **identités** (Bianchi) + équations non indépendantes ; voir [[Théories de jauge]], [[Courbure]].
