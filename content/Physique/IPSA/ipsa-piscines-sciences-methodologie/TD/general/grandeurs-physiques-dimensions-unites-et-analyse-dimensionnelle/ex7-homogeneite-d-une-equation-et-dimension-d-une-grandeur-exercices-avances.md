---
title: "Exercice 7 — (*) Homogénéité d'une équation et dimension d'une grandeur : exercices avancés"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/index|⬅ Retour]] · <a href="/pdfs/td1_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 7. (*) Homogénéité d'une équation et dimension d'une grandeur : exercices avancés *(facultatif)*

Cet exercice reprend les deux grands usages de l'analyse dimensionnelle : **tester l'homogénéité** d'une équation (détecter une erreur) et **déterminer la dimension** d'une grandeur (ou d'une constante) à partir d'une loi. Les situations sont plus variées que dans les exercices précédents : électricité, thermodynamique, ondes, mécanique quantique, mécanique des fluides.

**q1.** **Tester l'homogénéité d'équations**\\

$x$ est une position, $v$ une vitesse, $a$ une accélération, $t$ un temps, $P$ une pression, $\rho$ une masse volumique, $g$ l'accélération de la pesanteur, $h$ une hauteur, $M_S$ la masse du Soleil, $p$ une quantité de mouvement, $F$ une force, $S$ une surface. Dire pour chaque équation si elle est homogène, et si elle est fausse la corriger :


(a) $x = x_0 + v_0 t + a t^2$

(b) $P + \tfrac{1}{2}\rho v^2 + \rho g h = \text{cste}$

(c) $P + \rho v + \rho g h = \text{cste}$

(d) $v = \sqrt{\dfrac{G M_S}{r}}$

(e) $E^2 = p^2 c^2 + m^2 c^4$

(f) $F = \tfrac{1}{2}\rho S v$ (force de traînée)

> [!tip]- 💡 Coup de pouce
> **Que compare-t-on ?
> **
>
> Il suffit de calculer la dimension de chaque terme. Ne pas s'arrêter à la première équation homogène : demandez-vous aussi si elle est **correcte**.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 1
> **
>
> (a) $[a t^2] = L\,T^{-2}\,T^2 = L$, $[v_0 t] = L$, $[x_0] = L$ : l'équation est **homogène**. Elle est pourtant **fausse** car le facteur $\tfrac{1}{2}$ est absent : $x = x_0 + v_0 t + \tfrac{1}{2} a t^2$. L'homogénéité est nécessaire mais non suffisante.
>
> (b) $[P] = M L^{-1} T^{-2}$, $[\rho v^2] = M L^{-3} L^2 T^{-2} = M L^{-1} T^{-2}$, $[\rho g h] = M L^{-3} L T^{-2} L = M L^{-1} T^{-2}$ : **homogène** (relation de Bernoulli).
>
> (c) $[\rho v] = M L^{-3} L T^{-1} = M L^{-2} T^{-1} \neq [P]$ : **non homogène** donc fausse. Correction : remplacer $\rho v$ par $\tfrac{1}{2}\rho v^2$.
>
> (d) $\left[\dfrac{G M_S}{r}\right] = \dfrac{M^{-1} L^3 T^{-2} \cdot M}{L} = L^2 T^{-2}$, donc le second membre est $L\,T^{-1}$ : **homogène** (vitesse orbitale circulaire).
>
> (e) $[E^2] = M^2 L^4 T^{-4}$. $[p c] = M L T^{-1} \cdot L T^{-1} = M L^2 T^{-2}$ donc $[p^2 c^2] = M^2 L^4 T^{-4}$. $[m c^2] = M L^2 T^{-2}$ donc $[m^2 c^4] = M^2 L^4 T^{-4}$ : **homogène** (relation énergie-impulsion relativiste).
>
> (f) $[\rho S v] = M L^{-3} L^2 L T^{-1} = M T^{-1} \neq [F] = M L T^{-2}$ : **non homogène**. Correction : $F = \tfrac{1}{2}\rho S v^2$ car $[\rho S v^2] = M L^{-3} L^2 L^2 T^{-2} = M L T^{-2}$.


**q2.** **Déterminer la dimension d'une grandeur électrique ou magnétique**\\

À partir des lois suivantes, donner l'équation aux dimensions de la grandeur demandée :


(a) la viscosité dynamique $\eta$, avec la loi de Stokes $F = 6\pi \eta R v$ ;

(b) la tension électrique $U$, avec la puissance $P = U I$ ;

(c) la résistance $R = \dfrac{U}{I}$ ;

(d) la capacité $C$, avec $Q = C U$ où $Q$ est une charge ;

(e) le champ magnétique $B$, avec la force de Lorentz $F = q v B$ ;

(f) l'inductance $L$, avec l'énergie magnétique $E = \tfrac{1}{2} L I^2$.

(g) Vérifier ensuite que la loi $U = L \dfrac{\mathrm{d}I}{\mathrm{d}t}$ est homogène avec les résultats précédents.

> [!tip]- 💡 Coup de pouce
> **Ordre de calcul
> **
>
> Commencer par $[U]$ (question b) : il sert pour c), d) et g). Une dérivée $\dfrac{\mathrm{d}I}{\mathrm{d}t}$ a pour dimension $[I]/T$.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 2
> **
>
> (a) $[\eta] = \dfrac{[F]}{[R][v]} = \dfrac{M L T^{-2}}{L \cdot L T^{-1}} = M\,L^{-1}\,T^{-1}$ (unité : $\text{Pa.s}$).
>
> (b) $[U] = \dfrac{[P]}{[I]} = M\,L^2\,T^{-3}\,I^{-1}$ (unité : $\text{V}$).
>
> (c) $[R] = \dfrac{[U]}{[I]} = M\,L^2\,T^{-3}\,I^{-2}$ (unité : $\Omega$).
>
> (d) $[C] = \dfrac{[Q]}{[U]} = \dfrac{I\,T}{M L^2 T^{-3} I^{-1}} = M^{-1}\,L^{-2}\,T^{4}\,I^{2}$ (unité : $\text{F}$).
>
> (e) $[B] = \dfrac{[F]}{[q][v]} = \dfrac{M L T^{-2}}{I T \cdot L T^{-1}} = M\,T^{-2}\,I^{-1}$ (unité : $\text{T}$).
>
> (f) $[L] = \dfrac{[E]}{[I]^2} = \dfrac{M L^2 T^{-2}}{I^2} = M\,L^2\,T^{-2}\,I^{-2}$ (unité : $\text{H}$).
>
> (g) $\left[L \dfrac{\mathrm{d}I}{\mathrm{d}t}\right] = M L^2 T^{-2} I^{-2} \cdot I\,T^{-1} = M\,L^2\,T^{-3}\,I^{-1} = [U]$ : l'équation est **homogène**.


**q3.** **Arguments de fonctions et constantes**\\

Un argument d'exponentielle, de logarithme ou de fonction trigonométrique est nécessairement sans dimension.


(a) Une onde progressive s'écrit $y(x,t) = A \sin(\omega t - k x)$. Donner les dimensions de $\omega$ et $k$, puis celle de la vitesse de phase $v_\varphi = \omega / k$.

(b) La pression atmosphérique varie avec l'altitude $z$ selon $P(z) = P_0 \exp\!\left(-\dfrac{M_{mol}\, g\, z}{R\, T}\right)$ où $M_{mol}$ est la masse molaire, $R$ la constante des gaz parfaits ($[R] = M L^2 T^{-2} N^{-1} \Theta^{-1}$) et $T$ la température. Vérifier que l'argument est sans dimension.

(c) Loi d'Arrhenius : $k = A \exp\!\left(-\dfrac{E_a}{R T}\right)$. Déterminer la dimension et l'unité SI de $E_a$. Que peut-on dire de la dimension de $A$ ?

(d) Un étudiant écrit $u(t) = u_0 \ln(t)$ où $t$ est un temps. Cette écriture est-elle homogène ? Comment la corriger ?

> [!tip]- 💡 Coup de pouce
> **Masse molaire
> **
>
> $[M_{mol}] = M\,N^{-1}$ (masse par quantité de matière). Pour c), écrire que $\dfrac{E_a}{R T}$ est adimensionnel.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 3
> **
>
> (a) $\omega t$ est sans dimension donc $[\omega] = T^{-1}$. De même $k x$ est sans dimension donc $[k] = L^{-1}$. Alors $[v_\varphi] = \dfrac{T^{-1}}{L^{-1}} = L\,T^{-1}$ : c'est bien une vitesse.
>
> (b) $\left[\dfrac{M_{mol}\, g\, z}{R\, T}\right] = \dfrac{M N^{-1} \cdot L T^{-2} \cdot L}{M L^2 T^{-2} N^{-1} \Theta^{-1} \cdot \Theta} = 1$ : l'argument est bien **sans dimension**.
>
> (c) $[E_a] = [R][T] = M L^2 T^{-2} N^{-1} \Theta^{-1} \cdot \Theta = M\,L^2\,T^{-2}\,N^{-1}$. Unité SI : $\text{kg.m}^2\text{.s}^{-2}\text{.mol}^{-1} = \text{J.mol}^{-1}$. Comme l'exponentielle est sans dimension, $[A] = [k]$ : $A$ a la même dimension que la constante de vitesse $k$.
>
> (d) Le logarithme d'une grandeur dimensionnée n'a pas de sens : **non homogène**. Il faut écrire $u(t) = u_0 \ln\!\left(\dfrac{t}{\tau}\right)$ où $\tau$ est un temps de référence (par exemple $1 ~\text{s}$).


**q4.** **Équation de Van der Waals (question difficile)**\\

L'équation d'état d'un gaz réel de $n$ moles, de volume $V$, de pression $P$ et de température $T$ s'écrit
$$
\left(P + \frac{a\, n^2}{V^2}\right)\left(V - n\, b\right) = n\, R\, T.
$$


(a) Quelle relation doivent vérifier les dimensions de $P$ et de $\dfrac{a n^2}{V^2}$ ? En déduire $[a]$.

(b) Quelle relation doivent vérifier $[V]$ et $[n b]$ ? En déduire $[b]$.

(c) Déterminer $[R]$ et l'unité SI de $R$ à partir de la loi des gaz parfaits.

(d) Donner les unités SI de $a$ et de $b$ en unités de base, puis en $\text{Pa.m}^6\text{.mol}^{-2}$ pour $a$ et $\text{m}^3\text{.mol}^{-1}$ pour $b$.

(e) Pour le dioxyde de carbone, $a = 0,364 ~\text{Pa.m}^6\text{.mol}^{-2}$ et $b = 4,27 \times 10^{-5} ~\text{m}^3\text{.mol}^{-1}$. Calculer la pression corrective $\dfrac{a n^2}{V^2}$ pour $n = 1,00 ~\text{mol}$ dans $V = 1,00 ~\text{L}$, et la comparer à $P_{atm} = 1,01 \times 10^{5} ~\text{Pa}$.

> [!tip]- 💡 Coup de pouce
> **Somme de termes
> **
>
> Dans $P + \dfrac{a n^2}{V^2}$ et dans $V - n b$, les deux termes doivent avoir la même dimension pour que la somme ait un sens.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 4
> **
>
> (a) $\left[\dfrac{a n^2}{V^2}\right] = [P]$ donc $[a] = \dfrac{[P][V]^2}{[n]^2} = \dfrac{M L^{-1} T^{-2} \cdot L^6}{N^2} = M\,L^5\,T^{-2}\,N^{-2}$.
>
> (b) $[n b] = [V]$ donc $[b] = \dfrac{L^3}{N} = L^3\,N^{-1}$.
>
> (c) $R = \dfrac{P V}{n T}$ donc $[R] = \dfrac{M L^{-1} T^{-2} \cdot L^3}{N \cdot \Theta} = M\,L^2\,T^{-2}\,N^{-1}\,\Theta^{-1}$. Unité : $\text{kg.m}^2\text{.s}^{-2}\text{.mol}^{-1}\text{.K}^{-1} = \text{J.mol}^{-1}\text{.K}^{-1}$.
>
> (d) $a$ : $\text{kg.m}^5\text{.s}^{-2}\text{.mol}^{-2}$, soit $\text{Pa.m}^6\text{.mol}^{-2}$ car $1 ~\text{Pa} = 1 ~\text{kg.m}^{-1}\text{.s}^{-2}$. $b$ : $\text{m}^3\text{.mol}^{-1}$.
>
> (e) $V = 1,00 ~\text{L} = 1,00 \times 10^{-3} ~\text{m}^3$. Alors
>   $$\frac{a n^2}{V^2} = \frac{0,364 \times 1,00^2}{(1,00 \times 10^{-3})^2} = 3,64 \times 10^{5} ~\text{Pa}.$$
>   C'est environ $3,6$ fois la pression atmosphérique : la correction n'est pas négligeable à cette densité.


**q5.** **Équation de Schrödinger (question difficile)**\\

En mécanique quantique, une particule de masse $m$ se déplaçant selon $x$ dans un potentiel $V(x)$ est décrite par une fonction d'onde $\psi(x,t)$ vérifiant
$$
i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2} + V\, \psi.
$$
On donne $[\hbar] = M L^2 T^{-1}$ et $i$ est adimensionnel.


(a) Donner la dimension de chacun des deux premiers termes en fonction de $[\psi]$. Vérifier qu'ils sont homogènes entre eux.

(b) En déduire la dimension de $V$. Quelle grandeur physique reconnaît-on ?

(c) La probabilité de trouver la particule entre $x$ et $x + \mathrm{d}x$ est $|\psi|^2 \, \mathrm{d}x$ et la probabilité totale vaut $1$ : $\displaystyle \int |\psi|^2 \, \mathrm{d}x = 1$. En déduire $[\psi]$.

(d) Que devient $[\psi]$ pour une particule en trois dimensions avec $\displaystyle \int |\psi|^2 \, \mathrm{d}^3 r = 1$ ?

> [!tip]- 💡 Coup de pouce
> **Probabilité
> **
>
> Une probabilité est un nombre pur : $\left[\displaystyle \int |\psi|^2 \, \mathrm{d}x\right] = [\psi]^2 \cdot L = 1$.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 5
> **
>
> (a) $\left[i\hbar \dfrac{\partial \psi}{\partial t}\right] = \dfrac{M L^2 T^{-1}}{T}[\psi] = M\,L^2\,T^{-2}\,[\psi]$.\\
>   $\left[\dfrac{\hbar^2}{2m}\dfrac{\partial^2 \psi}{\partial x^2}\right] = \dfrac{M^2 L^4 T^{-2}}{M \cdot L^2}[\psi] = M\,L^2\,T^{-2}\,[\psi]$.\\
>   Les deux termes ont la même dimension : **homogène**.
>
> (b) $[V\psi] = [V][\psi]$ doit valoir $M L^2 T^{-2}[\psi]$ donc $[V] = M\,L^2\,T^{-2}$ : c'est une **énergie** (énergie potentielle).
>
> (c) $[\psi]^2 \cdot L = 1$ donc $[\psi] = L^{-1/2}$ (unité : $\text{m}^{-1/2}$).
>
> (d) $[\psi]^2 \cdot L^3 = 1$ donc $[\psi] = L^{-3/2}$ (unité : $\text{m}^{-3/2}$).


**q6.** **Loi de Poiseuille : trouver l'erreur (question difficile)**\\

Le débit volumique $Q$ d'un fluide de viscosité dynamique $\eta$ dans un tuyau cylindrique de rayon $R$ et de longueur $\ell$, soumis à une différence de pression $\Delta P$, est cherché par trois étudiants :
$$
\text{(A)}~ Q = \frac{\pi R^3 \Delta P}{8 \eta \ell}, \qquad \text{(B)}~ Q = \frac{\pi R^4 \Delta P}{8 \eta \ell}, \qquad \text{(C)}~ Q = \frac{\pi R^4 \Delta P}{8 \eta}.
$$


(a) Donner la dimension du débit volumique $Q$.

(b) Tester l'homogénéité des trois formules. Laquelle est possible ?

(c) On suppose $Q = k \, \dfrac{R^p \, \Delta P}{\eta \, \ell}$ avec $k$ constante sans dimension. Déterminer l'exposant $p$ par homogénéité.

(d) L'homogénéité permet-elle de trouver la valeur $k = \dfrac{\pi}{8}$ ? Justifier.

(e) On mesure $Q = 1,0 \times 10^{-6} ~\text{m}^3\text{.s}^{-1}$ pour de l'eau ($\eta = 1,0 \times 10^{-3} ~\text{Pa.s}$) dans un tube de rayon $R = 1,0 ~\text{mm}$ et de longueur $\ell = 1,0 ~\text{m}$. Utiliser (B) pour calculer $\Delta P$ avec le bon nombre de chiffres significatifs.

> [!tip]- 💡 Coup de pouce
> **Dimensions utiles
> **
>
> $[\Delta P] = M L^{-1} T^{-2}$, $[\eta] = M L^{-1} T^{-1}$. Calculer d'abord $\left[\dfrac{\Delta P}{\eta \, \ell}\right]$ : cette combinaison est commune aux trois formules.
>
> **Pour l'application numérique
> **
>
> Isoler $\Delta P = \dfrac{8 \eta \ell Q}{\pi R^4}$ et convertir $R$ en mètres.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 6
> **
>
> (a) $[Q] = \dfrac{\text{volume}}{\text{temps}} = L^3\,T^{-1}$.
>
> (b) $\left[\dfrac{\Delta P}{\eta \ell}\right] = \dfrac{M L^{-1} T^{-2}}{M L^{-1} T^{-1} \cdot L} = L^{-1}\,T^{-1}$.
>
>
> - (A) : $[R^3] \cdot L^{-1} T^{-1} = L^2 T^{-1} \neq L^3 T^{-1}$ : non homogène.
> - (B) : $[R^4] \cdot L^{-1} T^{-1} = L^3 T^{-1} = [Q]$ : **homogène**.
> - (C) : $[R^4] \cdot \dfrac{M L^{-1} T^{-2}}{M L^{-1} T^{-1}} = L^4 T^{-1} \neq L^3 T^{-1}$ : non homogène.
>
>
>   Seule (B) est possible.
>
> (c) $L^{p} \cdot L^{-1} T^{-1} = L^3 T^{-1}$ donc $p - 1 = 3$ soit $p = 4$.
>
> (d) Non : les facteurs numériques (comme $\pi$ et $8$) sont sans dimension et ne sont donc pas contraints par l'homogénéité. Il faut un calcul complet (résolution de l'équation de Navier-Stokes) ou une mesure.
>
> (e) $\Delta P = \dfrac{8 \eta \ell Q}{\pi R^4} = \dfrac{8 \times 1,0 \times 10^{-3} \times 1,0 \times 1,0 \times 10^{-6}}{\pi \times (1,0 \times 10^{-3})^4} = \dfrac{8,0 \times 10^{-9}}{3,14 \times 10^{-12}} \approx 2,5 \times 10^{3} ~\text{Pa}$ (soit $2$ chiffres significatifs).


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex8-conversions-d-unites-et-unites-des-constantes-fondamentales|Exercice 8 — (*) Conversions d'unités et unités des constantes fondamentales]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex10-theoreme-pi-et-similitude-dimensionner-une-maquette|Exercice 10 — (*) Théorème $\Pi$ et similitude : dimensionner une maquette]]

