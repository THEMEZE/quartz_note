---
title: "Exercice 9 — (*) Entraînement : chiffres significatifs, incertitudes et propagation"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/index|⬅ Retour]] · <a href="/pdfs/td1_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 9. (*) Entraînement : chiffres significatifs, incertitudes et propagation *(facultatif)*

Cet exercice d'entraînement est composé de questions directes (application immédiate des règles) puis de questions plus difficiles (calculs à plusieurs grandeurs mesurées, propagation des incertitudes, changements d'unités).

**q1.** **Compter les chiffres significatifs (question directe)**\\

Donner le nombre de chiffres significatifs de chaque valeur, puis l'écrire en notation scientifique :


(a) $0,0250 ~\text{m}$

(b) $3,0 \times 10^{2} ~\text{s}$

(c) $1,20 \times 10^{-3} ~\text{kg}$

(d) $0,00700 ~\text{mm}$

(e) $4,05 \times 10^{5} ~\text{Pa}$

> [!tip]- 💡 Coup de pouce
> **Astuce
> **
>
> Écrire d'abord la valeur sous la forme $a \times 10^n$ avec $1 \leq a < 10$, puis compter les chiffres de $a$.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 1
> **
>
> (a) $0,0250 ~\text{m} = 2,50 \times 10^{-2} ~\text{m}$ : **3 chiffres significatifs**.
>
> (b) $3,0 \times 10^{2} ~\text{s}$ : **2 chiffres significatifs**.
>
> (c) $1,20 \times 10^{-3} ~\text{kg}$ : **3 chiffres significatifs**.
>
> (d) $0,00700 ~\text{mm} = 7,00 \times 10^{-3} ~\text{mm}$ : **3 chiffres significatifs**.
>
> (e) $4,05 \times 10^{5} ~\text{Pa}$ : **3 chiffres significatifs**.


**q2.** **Écrire correctement un résultat (question directe)**\\

Pour chaque mesure, arrondir l'incertitude absolue à $1$ chiffre significatif par excès puis écrire le résultat sous la forme $(x_m \pm \Delta x) \text{ unité}$ :


(a) $x = 12,3456 ~\text{m}$ avec $\Delta x = 0,0234 ~\text{m}$

(b) $T = 2,5 ~\text{s}$ avec une incertitude relative de $4 \%$

(c) $U = 5,00 ~\text{V}$ avec une incertitude relative de $1,5 \%$

(d) $v = 3,0 \times 10^{8} ~\text{m.s}^{-1}$ avec $\Delta v = 1 \times 10^{6} ~\text{m.s}^{-1}$

> [!tip]- 💡 Coup de pouce
> **Ordre des opérations
> **
>
> Calculer $\Delta x$ (si besoin), l'arrondir **par excès** à un chiffre significatif, puis arrondir la valeur mesurée à la même décimale que l'incertitude.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 2
> **
>
> (a) $\Delta x = 0,0234 \to 0,03 ~\text{m}$ (par excès). La valeur est arrondie à $2$ décimales :
>   $$x = (12,35 \pm 0,03) ~\text{m}$$
>
> (b) $\Delta T = 0,04 \times 2,5 = 0,10 ~\text{s}$, soit $0,1 ~\text{s}$. Une seule décimale :
>   $$T = (2,5 \pm 0,1) ~\text{s}$$
>
> (c) $\Delta U = 0,015 \times 5,00 = 0,075 ~\text{V}$, arrondi par excès à $0,08 ~\text{V}$. Deux décimales :
>   $$U = (5,00 \pm 0,08) ~\text{V}$$
>
> (d) $\Delta v = 1 \times 10^{6} = 0,01 \times 10^{8} ~\text{m.s}^{-1}$. Il faut donc écrire la valeur avec deux décimales dans la même puissance de $10$ :
>   $$v = (3,00 \pm 0,01) \times 10^{8} ~\text{m.s}^{-1}$$


**q3.** **Opérations et chiffres significatifs (question directe)**\\

Effectuer les opérations suivantes en donnant le résultat avec le bon nombre de chiffres significatifs :


(a) $12,5 + 3,72$

(b) $4,20 \times 3,1$

(c) $\dfrac{8,0}{3,00}$

(d) $1,5 \times 10^{3} + 2,50 \times 10^{2}$

> [!tip]- 💡 Coup de pouce
> **Quelle règle ?
> **
>
> Somme : compter les **décimales**. Produit ou quotient : compter les **chiffres significatifs**.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 3
> **
>
> (a) Somme : $12,5 + 3,72 = 16,22$. Le terme le moins précis a $1$ décimale : **$16,2$**.
>
> (b) Produit : $4,20 \times 3,1 = 13,02$. Le facteur le moins précis a $2$ chiffres significatifs : **$13$**.
>
> (c) Quotient : $8,0 / 3,00 = 2,666\ldots$ Le facteur le moins précis ($8,0$) a $2$ chiffres significatifs : **$2,7$**.
>
> (d) Mettons les deux termes à la même puissance de $10$ : $1,5 \times 10^{3} + 0,250 \times 10^{3} = 1,750 \times 10^{3}$. Le terme le moins précis ($1,5 \times 10^3$) a $1$ décimale : **$1,8 \times 10^{3}$**.


**q4.** **Masse volumique d'un cylindre (question difficile)**\\

Un cylindre métallique plein est caractérisé par les mesures suivantes :
$$
m = (152,3 \pm 0,1) ~\text{g}, \qquad D = (2,50 \pm 0,02) ~\text{cm}, \qquad h = (10,00 \pm 0,05) ~\text{cm}.
$$


(a) Donner l'expression de la masse volumique $\rho$ en fonction de $m$, $D$ et $h$.

(b) Calculer $\rho$ avec la calculatrice, sans arrondir.

(c) Calculer les incertitudes relatives de $m$, $D$ et $h$. Quelle mesure est la moins précise en valeur relative ?

(d) En déduire l'incertitude relative sur $\rho$ puis l'incertitude absolue $\Delta \rho$ (arrondie à $1$ chiffre significatif par excès).

(e) Écrire $\rho$ en $\text{g.cm}^{-3}$ puis en $\text{kg.m}^{-3}$, avec son incertitude.

> [!tip]- 💡 Coup de pouce
> **Attention à l'exposant
> **
>
> $\rho = \dfrac{4m}{\pi D^2 h}$. Comme $D$ est au carré, son incertitude relative intervient avec un facteur $2$. Les constantes $4$ et $\pi$ n'ont pas d'incertitude.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 4
> **
>
> (a) $V = \pi \dfrac{D^2}{4} h$ donc $\displaystyle \rho = \frac{m}{V} = \frac{4m}{\pi D^2 h}$.
>
> (b) $\rho = \dfrac{4 \times 152,3}{\pi \times 2,50^2 \times 10,00} = \dfrac{609,2}{196,35} \approx 3,1027 ~\text{g.cm}^{-3}$.
>
> (c) $$\frac{\Delta m}{m} = \frac{0,1}{152,3} \approx 0,0007, \qquad \frac{\Delta D}{D} = \frac{0,02}{2,50} = 0,008, \qquad \frac{\Delta h}{h} = \frac{0,05}{10,00} = 0,005.$$
>   La mesure de $D$ est la moins précise en valeur relative ($0,8 \%$).
>
> (d) $$\frac{\Delta \rho}{\rho} = \frac{\Delta m}{m} + 2\frac{\Delta D}{D} + \frac{\Delta h}{h} \approx 0,00066 + 0,016 + 0,005 \approx 0,0217.$$
>   $\Delta \rho = 0,0217 \times 3,1027 \approx 0,067 ~\text{g.cm}^{-3}$, arrondi par excès à $0,07 ~\text{g.cm}^{-3}$.
>
> (e) $$\rho = (3,10 \pm 0,07) ~\text{g.cm}^{-3} = (3,10 \pm 0,07) \times 10^{3} ~\text{kg.m}^{-3}.$$
>   (Conversion : $1 ~\text{g.cm}^{-3} = 10^{3} ~\text{kg.m}^{-3}$.)


**q5.** **Mesure de $g$ avec un pendule simple (question difficile)**\\

Pour un pendule simple de longueur $L$ et de petites oscillations, la période est $T = 2\pi \sqrt{\dfrac{L}{g}}$. On mesure
$$
L = (0,850 \pm 0,005) ~\text{m}, \qquad T = (1,85 \pm 0,02) ~\text{s}.
$$


(a) Exprimer $g$ en fonction de $L$ et $T$.

(b) Calculer $g$ avec la calculatrice, sans arrondir.

(c) Calculer l'incertitude relative puis absolue sur $g$.

(d) Écrire le résultat $g = (g_m \pm \Delta g) \text{ unité}$.

(e) Le résultat est-il compatible avec la valeur tabulée $g = 9,81 ~\text{m.s}^{-2}$ ? Quelle mesure faut-il améliorer en priorité ?

> [!tip]- 💡 Coup de pouce
> **Isoler $g$
> **
>
> Élever au carré : $T^2 = 4\pi^2 \dfrac{L}{g}$. Comme $T$ est au carré, l'incertitude relative de $T$ compte deux fois.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 5
> **
>
> (a) $g = \dfrac{4\pi^2 L}{T^2}$.
>
> (b) $g = \dfrac{4\pi^2 \times 0,850}{1,85^2} = \dfrac{33,556}{3,4225} \approx 9,805 ~\text{m.s}^{-2}$.
>
> (c) $$\frac{\Delta g}{g} = \frac{\Delta L}{L} + 2\frac{\Delta T}{T} = \frac{0,005}{0,850} + 2 \times \frac{0,02}{1,85} \approx 0,0059 + 0,0216 \approx 0,0275.$$
>   $\Delta g = 0,0275 \times 9,805 \approx 0,27 ~\text{m.s}^{-2}$, arrondi par excès à $0,3 ~\text{m.s}^{-2}$.
>
> (d) $g = (9,8 \pm 0,3) ~\text{m.s}^{-2}$.
>
> (e) L'intervalle est $[9,5 ~;~ 10,1] ~\text{m.s}^{-2}$ : il contient $9,81 ~\text{m.s}^{-2}$, le résultat est **compatible** avec la valeur tabulée. La mesure de $T$ (incertitude relative $\approx 1,1 \%$, comptée deux fois) est la principale source d'incertitude : il vaut mieux mesurer la durée de plusieurs périodes.


**q6.** **Somme de longueurs avec unités mélangées (question difficile)**\\

Trois segments sont mis bout à bout : $\ell_1 = 2,34 \times 10^{-3} ~\text{m}$, $\ell_2 = 4,1 ~\text{mm}$ et $\ell_3 = 0,0068 ~\text{m}$.


(a) Convertir les trois longueurs en millimètres et indiquer le nombre de décimales de chacune.

(b) Calculer la longueur totale $\ell$ avec le bon nombre de chiffres significatifs.

(c) Exprimer $\ell$ en mètres en notation scientifique.

(d) Le segment $\ell_2$ est mesuré avec une incertitude de $0,1 ~\text{mm}$ et $\ell_1$, $\ell_3$ avec la même incertitude. Que vaut l'incertitude absolue sur $\ell$ ? Cela est-il cohérent avec le résultat de la question b) ?

> [!tip]- 💡 Coup de pouce
> **Unité commune
> **
>
> Pour une somme, il faut d'abord exprimer tous les termes dans la **même unité**, puis compter les décimales.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 6
> **
>
> (a) $\ell_1 = 2,34 ~\text{mm}$ ($2$ décimales), $\ell_2 = 4,1 ~\text{mm}$ ($1$ décimale), $\ell_3 = 6,8 ~\text{mm}$ ($1$ décimale).
>
> (b) $\ell = 2,34 + 4,1 + 6,8 = 13,24 ~\text{mm}$. Le résultat a au plus $1$ décimale : **$\ell = 13,2 ~\text{mm}$**.
>
> (c) $\ell = 1,32 \times 10^{-2} ~\text{m}$ ($3$ chiffres significatifs).
>
> (d) Pour une somme, les incertitudes absolues s'additionnent : $\Delta \ell = 3 \times 0,1 = 0,3 ~\text{mm}$. On écrit $\ell = (13,2 \pm 0,3) ~\text{mm}$. Le dernier chiffre significatif ($1$ décimale) est bien celui de l'incertitude : c'est cohérent avec la règle de la somme.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex6-grandeurs-numeriques-mesures-incertitudes-chiffres-significatifs|Exercice 6 — (*) Grandeurs numériques : mesures, incertitudes $\&$ chiffres significatifs]]

