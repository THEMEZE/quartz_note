---
title: "Exercice 10 — (*) Théorème $\\Pi$ et similitude : dimensionner une maquette"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/index|⬅ Retour]] · <a href="/pdfs/td1_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 10. (*) Théorème $\Pi$ et similitude : dimensionner une maquette *(facultatif)*

Comment prévoir la force qui s'exerce sur une voiture ou un navire avant de le construire ? On teste une **maquette** à échelle réduite, mais il faut choisir les conditions d'essai pour que les résultats soient transposables au **prototype** réel. Le théorème $\Pi$ (Vaschy-Buckingham) fournit les groupes adimensionnels qui doivent rester identiques entre la maquette et le prototype. Les questions $1$ à $4$ posent la méthode (pendule, voiture, navire) ; les questions $5$ à $10$ l'appliquent à l'aéronautique : **avion**, **drone**, **fusée**, **montgolfière**, **parachute** et comparaison des régimes de vol.

**q1.** **Échauffement : le pendule simple**\\

On suppose que la période $T$ d'un pendule simple dépend de sa masse $m$, de sa longueur $L$ et de l'intensité de la pesanteur $g$.


(a) Combien y a-t-il de variables $n$ ? Combien de dimensions fondamentales $k$ ? Combien de groupes $\Pi$ ?

(b) Déterminer le groupe $\Pi = T^a \, m^b \, L^c \, g^d$ sans dimension.

(c) En déduire la forme de $T$. La masse intervient-elle ?

> [!tip]- 💡 Coup de pouce
> **Système sur les exposants
> **
>
> Écrire $[\Pi] = M^b \, L^{c+d} \, T^{a-2d} = 1$ et annuler chaque exposant.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 1
> **
>
> (a) Variables : $T$, $m$, $L$, $g$ donc $n = 4$. Dimensions : $M$, $L$, $T$ donc $k = 3$. Il y a $n-k = 1$ groupe $\Pi$.
>
> (b) $[T] = T$, $[m] = M$, $[L] = L$, $[g] = L\,T^{-2}$ donc
>   $$[\Pi] = T^{a} \, M^{b} \, L^{c} \, (L\,T^{-2})^{d} = M^{b} \, L^{c+d} \, T^{a-2d}.$$
>   Il faut $b = 0$, $c + d = 0$ et $a - 2d = 0$. En posant $d = 1$ : $a = 2$, $c = -1$. Donc
>   $$\Pi = \frac{g\,T^2}{L}.$$
>
> (c) Un seul groupe adimensionnel est nécessairement une constante : $\dfrac{g\,T^2}{L} = C$, soit $T = \sqrt{C}\,\sqrt{\dfrac{L}{g}}$. La masse $m$ n'intervient pas (son exposant $b$ est nul). L'analyse dimensionnelle ne donne pas la constante ($C = 4\pi^2$ par un calcul complet).


**q2.** **Force sur un objet dans un fluide**\\

La force de traînée $F$ sur un objet de taille caractéristique $D$ placé dans un écoulement de vitesse $v$ dépend de la masse volumique $\rho$ et de la viscosité dynamique $\mu$ du fluide. On rappelle $[\mu] = M \, L^{-1} \, T^{-1}$.


(a) Lister les variables. Donner $n$, $k$ et le nombre de groupes $\Pi$.

(b) Choisir $\rho$, $v$, $D$ comme variables de base et construire les deux groupes $\Pi_1$ (contenant $F$) et $\Pi_2$ (contenant $\mu$).

(c) Montrer que $F = \rho \, v^2 D^2 \, \varphi(\mathrm{Re})$ où $\mathrm{Re} = \dfrac{\rho \, v \, D}{\mu}$ est le nombre de Reynolds.

> [!tip]- 💡 Coup de pouce
> **Groupes attendus
> **
>
> Chercher $\Pi_1 = F \, \rho^{a} v^{b} D^{c}$ et $\Pi_2 = \mu \, \rho^{a'} v^{b'} D^{c'}$. On peut vérifier le résultat final par les dimensions : $[\rho\,v^2 D^2]$ doit être une force.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 2
> **
>
> (a) Variables : $F$, $\rho$, $v$, $D$, $\mu$ donc $n = 5$, $k = 3$ et $n - k = 2$ groupes $\Pi$.
>
> (b) Dimensions : $[F] = M\,L\,T^{-2}$, $[\rho] = M\,L^{-3}$, $[v] = L\,T^{-1}$, $[D] = L$.
>
>
> - $\Pi_1 = F \, \rho^{a} v^{b} D^{c}$ : 
>     $M^{1+a} \, L^{1-3a+b+c} \, T^{-2-b} = 1$ donc $a = -1$, $b = -2$, $c = -2$. Ainsi
>     $$\Pi_1 = \frac{F}{\rho \, v^2 D^2}.$$
> - $\Pi_2 = \mu \, \rho^{a'} v^{b'} D^{c'}$ : 
>     $M^{1+a'} \, L^{-1-3a'+b'+c'} \, T^{-1-b'} = 1$ donc $a' = -1$, $b' = -1$, $c' = -1$. Ainsi
>     $$\Pi_2 = \frac{\mu}{\rho \, v \, D} = \frac{1}{\mathrm{Re}}.$$
>
> (c) Le théorème $\Pi$ donne $\Pi_1 = \varphi(\Pi_2)$, c'est-à-dire, en notant $\varphi$ la fonction de $\mathrm{Re}$ :
>   $$F = \rho \, v^2 D^2 \, \varphi(\mathrm{Re}).$$
>   Vérification : $[\rho \, v^2 D^2] = M L^{-3} \cdot L^2 T^{-2} \cdot L^2 = M\,L\,T^{-2}$, c'est bien une force.


**q3.** **Maquette de voiture en soufflerie**\\

Un constructeur veut prévoir la force de traînée sur une voiture (prototype) de longueur $L_p = 4,0 ~\text{m}$ roulant à $v_p = 30 ~\text{m.s}^{-1}$ dans l'air. Il teste une maquette de longueur $L_m = 1,0 ~\text{m}$ (échelle $1/4$). On utilise le résultat de la question 2 : les deux écoulements sont semblables si $\mathrm{Re}_m = \mathrm{Re}_p$.

Données : viscosité cinématique $\nu = \dfrac{\mu}{\rho}$ ; $\nu_{air} = 1,5 \times 10^{-5} ~\text{m}^2\text{.s}^{-1}$, $\nu_{eau} = 1,0 \times 10^{-6} ~\text{m}^2\text{.s}^{-1}$ ; $\rho_{air} = 1,2 ~\text{kg.m}^{-3}$, $\rho_{eau} = 1,0 \times 10^{3} ~\text{kg.m}^{-3}$ ; célérité du son dans l'air $c = 340 ~\text{m.s}^{-1}$.


(a) Exprimer $\mathrm{Re}$ avec $\nu$. Quelle vitesse $v_m$ faut-il imposer si la maquette est testée dans l'**air** ?

(b) Calculer le nombre de Mach $\mathrm{Ma} = v_m / c$. Cette vitesse convient-elle si l'on considère l'air incompressible pour $\mathrm{Ma} < 0,3$ ?

(c) On teste maintenant la maquette dans un **canal à eau**. Calculer la vitesse $v_m$ nécessaire.

(d) Exprimer le rapport $F_p / F_m$ en fonction de $\rho_p/\rho_m$, $v_p/v_m$ et $L_p/L_m$, puis le calculer pour l'essai dans l'eau.

(e) On mesure $F_m = 1,0 ~\text{kN}$ dans l'eau. Quelle est la traînée $F_p$ sur la voiture réelle ?

> [!tip]- 💡 Coup de pouce
> **Conservation de $\mathrm{Re}$ et de $\varphi$
> **
>
> Si $\mathrm{Re}_m = \mathrm{Re}_p$ alors $\varphi(\mathrm{Re}_m) = \varphi(\mathrm{Re}_p)$, donc le groupe $\Pi_1 = \dfrac{F}{\rho v^2 D^2}$ prend la même valeur pour la maquette et le prototype.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 3
> **
>
> (a) $\mathrm{Re} = \dfrac{\rho v L}{\mu} = \dfrac{v L}{\nu}$. Dans l'air, $\nu_m = \nu_p$ donc $v_m L_m = v_p L_p$ :
>   $$v_m = v_p \frac{L_p}{L_m} = 30 \times 4 = 1,2 \times 10^{2} ~\text{m.s}^{-1}.$$
>
> (b) $\mathrm{Ma} = \dfrac{120}{340} \approx 0,35 > 0,3$. L'air n'est plus incompressible : l'effet de compressibilité (nouveau nombre $\Pi$, le Mach) modifie l'écoulement et la maquette n'est pas fidèle au prototype. Cette solution n'est pas satisfaisante.
>
> (c) $\dfrac{v_m L_m}{\nu_{eau}} = \dfrac{v_p L_p}{\nu_{air}}$ donc
>   $$v_m = v_p \frac{L_p}{L_m}\frac{\nu_{eau}}{\nu_{air}} = 30 \times 4 \times \frac{1,0 \times 10^{-6}}{1,5 \times 10^{-5}} = 8,0 ~\text{m.s}^{-1}.$$
>   L'eau permet une vitesse d'essai réaliste.
>
> (d) L'égalité de $\Pi_1$ donne $\dfrac{F_p}{\rho_p v_p^2 L_p^2} = \dfrac{F_m}{\rho_m v_m^2 L_m^2}$, soit
>   $$\frac{F_p}{F_m} = \frac{\rho_p}{\rho_m} \left(\frac{v_p}{v_m}\right)^2 \left(\frac{L_p}{L_m}\right)^2 = \frac{1,2}{1,0 \times 10^{3}} \times \left(\frac{30}{8,0}\right)^2 \times 4^2 \approx 0,27.$$
>
> (e) $F_p = 0,27 \times 1,0 ~\text{kN} \approx 0,27 ~\text{kN} = 2,7 \times 10^{2} ~\text{N}$.


**q4.** **Maquette de navire : la similitude de Froude**\\

Pour un navire, la résistance à l'avancement due aux vagues dépend de la vitesse $v$, de la longueur $L$, de la masse volumique de l'eau $\rho$, de l'intensité de la pesanteur $g$ et de la force $F$. Un cargo (prototype) de longueur $L_p = 100 ~\text{m}$ navigue à $v_p = 10 ~\text{m.s}^{-1}$. Sa maquette est à l'échelle $1/25$ et testée dans de l'eau, avec le même $g$.


(a) Combien y a-t-il de groupes $\Pi$ ? Les construire avec $\rho$, $v$, $L$ comme variables de base. Montrer que l'on trouve $\Pi_1 = \dfrac{F}{\rho v^2 L^2}$ et $\Pi_2 = \dfrac{g L}{v^2}$.

(b) On appelle nombre de Froude $\mathrm{Fr} = \dfrac{v}{\sqrt{g L}}$. Quelle vitesse $v_m$ faut-il pour la maquette ?

(c) On mesure sur la maquette $F_m = 12 ~\text{N}$. Calculer $F_p$ avec le bon nombre de chiffres significatifs.

(d) Calculer le rapport $\dfrac{\mathrm{Re}_m}{\mathrm{Re}_p}$ en supposant le même fluide. Peut-on respecter à la fois $\mathrm{Fr}$ et $\mathrm{Re}$ ? Que conclure ?

> [!tip]- 💡 Coup de pouce
> **Groupe contenant $g$
> **
>
> $[g L] = L^2 T^{-2}$ et $[v^2] = L^2 T^{-2}$ : le rapport $\dfrac{g L}{v^2}$ est déjà sans dimension.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 4
> **
>
> (a) Variables : $F$, $\rho$, $v$, $L$, $g$ donc $n = 5$, $k = 3$ et $2$ groupes $\Pi$. Comme à la question 2, $\Pi_1 = \dfrac{F}{\rho v^2 L^2}$. Pour $g$ : $\Pi_2 = g\,\rho^{a} v^{b} L^{c}$ avec $[\Pi_2] = M^{a} \, L^{1-3a+b+c} \, T^{-2-b}$ donc $a = 0$, $b = -2$, $c = 1$ et $\Pi_2 = \dfrac{g L}{v^2}$.
>
> (b) Le groupe $\Pi_2 = 1/\mathrm{Fr}^2$ doit être conservé : $\dfrac{v_m}{\sqrt{L_m}} = \dfrac{v_p}{\sqrt{L_p}}$ donc
>   $$v_m = v_p \sqrt{\frac{L_m}{L_p}} = 10 \times \sqrt{\frac{1}{25}} = 2,0 ~\text{m.s}^{-1}.$$
>
> (c) Avec $\rho_m = \rho_p$ et $\Pi_1$ conservé :
>   $$\frac{F_p}{F_m} = \left(\frac{v_p}{v_m}\right)^2 \left(\frac{L_p}{L_m}\right)^2 = 5^2 \times 25^2 = 25 \times 625 = 15\,625 = 25^3.$$
>   $F_p = 15\,625 \times 12 = 187\,500 ~\text{N}$. Avec $2$ chiffres significatifs (limités par $12 ~\text{N}$) : **$F_p = 1,9 \times 10^{5} ~\text{N}$**.
>
> (d) $\dfrac{\mathrm{Re}_m}{\mathrm{Re}_p} = \dfrac{v_m L_m}{v_p L_p} = \dfrac{1}{5} \times \dfrac{1}{25} = \dfrac{1}{125}$. Le nombre de Reynolds de la maquette est $125$ fois plus petit : on ne peut pas respecter $\mathrm{Fr}$ et $\mathrm{Re}$ en même temps avec le même fluide. C'est une **similitude partielle** : pour un navire, on respecte le Froude (effet dominant des vagues) et on corrige les effets de viscosité par des méthodes empiriques.


**q5.** **Maquette d'avion : Mach et Reynolds (soufflerie pressurisée)**\\

La portance $F$ d'un avion de ligne dépend de sa longueur caractéristique $L$, de sa vitesse $v$, de la masse volumique $\rho$, de la viscosité dynamique $\mu$ et de la célérité du son $c$ de l'air.

Prototype en croisière : $L_p = 20 ~\text{m}$, $v_p = 240 ~\text{m.s}^{-1}$, $\rho_p = 0,40 ~\text{kg.m}^{-3}$, $\mu_p = 1,5 \times 10^{-5} ~\text{Pa.s}$, $c_p = 300 ~\text{m.s}^{-1}$. Maquette à l'échelle $1/20$ dans une soufflerie à l'air ambiant : $\rho_m = 1,2 ~\text{kg.m}^{-3}$, $\mu_m = 1,8 \times 10^{-5} ~\text{Pa.s}$, $c_m = 340 ~\text{m.s}^{-1}$, pression $P_0 = 1,0 \times 10^{5} ~\text{Pa}$.


(a) Donner $n$, $k$ et le nombre de groupes $\Pi$. Vérifier que $\Pi_1 = \dfrac{F}{\rho v^2 L^2}$, $\Pi_2 = \mathrm{Re} = \dfrac{\rho v L}{\mu}$ et $\Pi_3 = \mathrm{Ma} = \dfrac{v}{c}$ sont sans dimension.

(b) Calculer le nombre de Mach du prototype. Quelle vitesse $v_m$ impose la conservation de $\mathrm{Ma}$ pour la maquette ?

(c) Calculer $\mathrm{Re}_p$ et $\mathrm{Re}_m$. Le nombre de Reynolds est-il conservé ?

(d) À température constante, $\rho$ est proportionnelle à la pression et $\mu$ ne dépend pas de la pression. Quelle pression $P_m$ faut-il dans la soufflerie pour avoir aussi $\mathrm{Re}_m = \mathrm{Re}_p$ ?

(e) Dans ces conditions, calculer $F_p/F_m$. On mesure $F_m = 25 ~\text{kN}$ : en déduire $F_p$ et la masse soutenue par la portance en vol horizontal.

> [!tip]- 💡 Coup de pouce
> **Trois groupes
> **
>
> Ici $n = 6$ et $k = 3$ donc $3$ groupes $\Pi$. Pour la similitude complète, **deux** groupes d'entrée doivent être conservés : $\mathrm{Ma}$ et $\mathrm{Re}$. La seule variable à ajuster est alors la masse volumique de la soufflerie.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 5
> **
>
> (a) Variables : $F$, $L$, $v$, $\rho$, $\mu$, $c$ donc $n = 6$, $k = 3$ et $3$ groupes $\Pi$. On a $[\rho v^2 L^2] = M L T^{-2} = [F]$, $\left[\dfrac{\rho v L}{\mu}\right] = \dfrac{M L^{-3} \cdot L T^{-1} \cdot L}{M L^{-1} T^{-1}} = 1$ et $[v/c] = 1$.
>
> (b) $\mathrm{Ma}_p = \dfrac{240}{300} = 0,80$. On impose $\mathrm{Ma}_m = 0,80$ donc $v_m = 0,80 \times 340 = 2,7 \times 10^{2} ~\text{m.s}^{-1}$ (soit $272 ~\text{m.s}^{-1}$).
>
> (c) $\mathrm{Re}_p = \dfrac{0,40 \times 240 \times 20}{1,5 \times 10^{-5}} \approx 1,3 \times 10^{8}$ et $\mathrm{Re}_m = \dfrac{1,2 \times 272 \times 1,0}{1,8 \times 10^{-5}} \approx 1,8 \times 10^{7}$. Le rapport $\mathrm{Re}_p / \mathrm{Re}_m \approx 7,1$ : **$\mathrm{Re}$ n'est pas conservé**.
>
> (d) $\mathrm{Re} \propto \rho$ à $v$, $L$, $\mu$ fixés ($v_m$ est imposée par le Mach). Il faut donc multiplier $\rho_m$ par $7,06$ : $\rho_m = 1,2 \times 7,06 \approx 8,5 ~\text{kg.m}^{-3}$, soit
>   $$P_m = 7,06 \times 1,0 \times 10^{5} \approx 7,1 \times 10^{5} ~\text{Pa} = 7,1 ~\text{bar}.$$
>   C'est le principe des souffleries pressurisées (ou cryogéniques, qui abaissent $\mu/\rho$ et $c$).
>
> (e) En gardant les valeurs non arrondies ($\rho_m = 8,47 ~\text{kg.m}^{-3}$) :
>   $$\frac{F_p}{F_m} = \frac{\rho_p}{\rho_m}\left(\frac{v_p}{v_m}\right)^2\left(\frac{L_p}{L_m}\right)^2 = \frac{0,40}{8,47} \times \left(\frac{240}{272}\right)^2 \times 20^2 \approx 14,7.$$
>   $F_p \approx 14,7 \times 25 ~\text{kN} \approx 3,7 \times 10^{5} ~\text{N}$. En vol horizontal, $F_p = m g$ donc $m = \dfrac{3,7 \times 10^{5}}{9,81} \approx 3,7 \times 10^{4} ~\text{kg}$, soit environ $37$ tonnes.


**q6.** **Hélice de drone : coefficients de poussée et de puissance**\\

La poussée $T$ d'une hélice de diamètre $D$ tournant à la fréquence $N$ (en tours par seconde) dans l'air de masse volumique $\rho$ est étudiée. On néglige la viscosité (Reynolds élevé) et la compressibilité.


(a) Montrer par le théorème $\Pi$ que $T = C_T \, \rho \, N^2 D^4$ où $C_T$ est un coefficient sans dimension.

(b) De même, la puissance $P$ absorbée s'écrit $P = C_P \, \rho \, N^3 D^5$ : vérifier l'homogénéité.

(c) Un banc d'essai sur une petite hélice ($D_m = 0,25 ~\text{m}$, $N_m = 80 ~\text{tr.s}^{-1}$, $\rho = 1,2 ~\text{kg.m}^{-3}$) donne $T_m = 4,0 ~\text{N}$ et $P_m = 45 ~\text{W}$. Calculer $C_T$ et $C_P$.

(d) Une hélice géométriquement semblable de diamètre $D_p = 0,50 ~\text{m}$ tourne à $N_p = 40 ~\text{tr.s}^{-1}$. Calculer sa poussée $T_p$ et sa puissance $P_p$.

(e) Un drone quadricoptère de masse $m = 2,0 ~\text{kg}$ utilise quatre de ces hélices ($D = 0,50 ~\text{m}$). Quelle fréquence de rotation faut-il en vol stationnaire ? L'exprimer en $\text{tr.min}^{-1}$ et calculer la puissance totale nécessaire.

> [!tip]- 💡 Coup de pouce
> **Variables de l'hélice
> **
>
> Pour $T$, les variables sont $T$, $\rho$, $N$, $D$ donc $n = 4$, $k = 3$ et un seul groupe $\Pi$. Avec $[N] = T^{-1}$, chercher $\Pi = T \, \rho^{a} N^{b} D^{c}$. Pour la question e), en vol stationnaire la poussée totale compense le poids.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 6
> **
>
> (a) $[T] = M L T^{-2}$, $[\rho] = M L^{-3}$, $[N] = T^{-1}$, $[D] = L$. Pour $\Pi = T \rho^{a} N^{b} D^{c}$ : $M^{1+a} \, L^{1-3a+c} \, T^{-2-b} = 1$ donc $a = -1$, $b = -2$, $c = -4$. Alors $\Pi = \dfrac{T}{\rho N^2 D^4} = C_T$ (constante d'après le théorème $\Pi$).
>
> (b) $[\rho N^3 D^5] = M L^{-3} T^{-3} L^5 = M L^2 T^{-3} = [P]$ : homogène.
>
> (c) $C_T = \dfrac{4,0}{1,2 \times 80^2 \times 0,25^4} = \dfrac{4,0}{30} \approx 0,13$. $C_P = \dfrac{45}{1,2 \times 80^3 \times 0,25^5} = \dfrac{45}{600} \approx 0,075$.
>
> (d) À $C_T$ et $C_P$ constants : $\dfrac{T_p}{T_m} = \left(\dfrac{N_p}{N_m}\right)^2 \left(\dfrac{D_p}{D_m}\right)^4 = \dfrac{1}{4} \times 16 = 4$ donc $T_p = 16 ~\text{N}$. $\dfrac{P_p}{P_m} = \left(\dfrac{1}{2}\right)^3 \times 2^5 = 4$ donc $P_p = 180 ~\text{W}$.
>
> (e) Chaque hélice porte $\dfrac{m g}{4} = \dfrac{2,0 \times 9,81}{4} \approx 4,9 ~\text{N}$. Alors
>   $$N = \sqrt{\frac{T}{C_T \, \rho \, D^4}} = \sqrt{\frac{4,9}{0,133 \times 1,2 \times 0,50^4}} = \sqrt{490} \approx 22 ~\text{tr.s}^{-1} \approx 1,3 \times 10^{3} ~\text{tr.min}^{-1}.$$
>   Puissance par hélice : $C_P \, \rho N^3 D^5 = 0,075 \times 1,2 \times 22,1^3 \times 0,50^5 \approx 31 ~\text{W}$, soit $P_{tot} \approx 1,2 \times 10^{2} ~\text{W}$ pour les quatre.


**q7.** **Fusée : poussée et limites de la maquette réduite**\\



(a) La poussée $F$ d'un moteur-fusée dépend du débit massique d'éjection $q_m$ (en $\text{kg.s}^{-1}$) et de la vitesse d'éjection $v_e$. Écrire les équations aux dimensions de $F$, $q_m$, $v_e$. Combien de groupes $\Pi$ y a-t-il, sachant que le rang de la matrice des dimensions est $2$ ? Montrer que $F = C \, q_m v_e$.

(b) Un lanceur (prototype) a $q_{m,p} = 2,5 \times 10^{3} ~\text{kg.s}^{-1}$ et $v_e = 3,0 \times 10^{3} ~\text{m.s}^{-1}$. Calculer sa poussée $F_p$.

(c) On construit une maquette à l'échelle $1/10$, semblable géométriquement, avec le même propergol et la même pression de chambre. Le débit massique est proportionnel à la section de la tuyère. Calculer $q_{m,m}$ et $F_m$.

(d) La masse du prototype est $m_p = 5,0 \times 10^{5} ~\text{kg}$ ; la masse de la maquette est proportionnelle à $L^3$ (même masse volumique moyenne). Montrer que $\Pi = \dfrac{F}{m g}$ est sans dimension, puis comparer sa valeur pour le prototype et pour la maquette. Conclusion ?

> [!tip]- 💡 Coup de pouce
> **Rang de la matrice
> **
>
> Ici $[F]$, $[q_m]$ et $[v_e]$ ne font intervenir que $M$, $L$, $T$, mais les trois vecteurs d'exposants sont liés : le rang est $2$ et non $3$. Le nombre de groupes $\Pi$ est $n$ moins le **rang**, soit $3 - 2 = 1$.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 7
> **
>
> (a) $[F] = M L T^{-2}$, $[q_m] = M T^{-1}$, $[v_e] = L T^{-1}$. On a $[q_m v_e] = M L T^{-2} = [F]$. Avec $n = 3$ et un rang de $2$, il y a $n - 2 = 1$ groupe $\Pi = \dfrac{F}{q_m v_e}$, nécessairement constant : $F = C \, q_m v_e$ ($C = 1$ dans le vide si la pression d'éjection est égale à la pression extérieure).
>
> (b) $F_p = 2,5 \times 10^{3} \times 3,0 \times 10^{3} = 7,5 \times 10^{6} ~\text{N}$.
>
> (c) La section varie en $L^2$ : $q_{m,m} = \dfrac{2,5 \times 10^{3}}{10^2} = 25 ~\text{kg.s}^{-1}$ et $F_m = 25 \times 3,0 \times 10^{3} = 7,5 \times 10^{4} ~\text{N}$.
>
> (d) $[F/(m g)] = \dfrac{M L T^{-2}}{M \cdot L T^{-2}} = 1$. Prototype : $\dfrac{7,5 \times 10^{6}}{5,0 \times 10^{5} \times 9,81} \approx 1,5$. Maquette : $m_m = 5,0 \times 10^{2} ~\text{kg}$ donc $\dfrac{7,5 \times 10^{4}}{5,0 \times 10^{2} \times 9,81} \approx 15$. Le rapport poussée/poids de la maquette est $10$ fois plus grand ($F \propto L^2$, $m g \propto L^3$). La maquette n'est **pas semblable dynamiquement** : elle décolle beaucoup plus violemment. Elle sert à tester la tuyère ou l'aérodynamique, pas la trajectoire complète.


**q8.** **Maquette de montgolfière : similitude de flottabilité**\\

La vitesse ascensionnelle $v$ d'une montgolfière de diamètre $L$ dépend de $L$, de $g$, de la masse volumique de l'air extérieur $\rho$ et de l'écart de masse volumique $\Delta\rho = \rho - \rho_{int}$ entre l'air extérieur et l'air chaud intérieur.


(a) Donner $n$, $k$ et le nombre de groupes $\Pi$. Avec $\rho$, $g$, $L$ comme variables de base, construire $\Pi_1 = \dfrac{v}{\sqrt{g L}}$ et $\Pi_2 = \dfrac{\Delta\rho}{\rho}$.

(b) À pression constante, $\rho \propto 1/T$ (gaz parfait). Montrer que $\dfrac{\Delta\rho}{\rho} = 1 - \dfrac{T_{ext}}{T_{int}}$ et calculer sa valeur pour $T_{ext} = 288 ~\text{K}$ et $T_{int} = 373 ~\text{K}$.

(c) La montgolfière (prototype) a un diamètre $L_p = 20 ~\text{m}$ et monte à $v_p = 3,0 ~\text{m.s}^{-1}$. Une maquette au $1/10$ est gonflée avec la même température intérieure. Quelle est sa vitesse $v_m$ ? Le prototype monte de $900 ~\text{m}$ en $300 ~\text{s}$ : quelle est la durée de la montée de $90 ~\text{m}$ pour la maquette ?

(d) La force ascensionnelle est $F = \Delta\rho \, V g$. Calculer $F_p/F_m$. Le prototype soulève une charge utile de $1,2 \times 10^{3} ~\text{kg}$ : quelle charge la maquette peut-elle soulever ?

> [!tip]- 💡 Coup de pouce
> **Conservation de $\Pi_2$
> **
>
> Même température intérieure et extérieure donc même $\Delta\rho/\rho$ : il reste à conserver $\Pi_1$, c'est-à-dire le nombre de Froude. Le volume est proportionnel à $L^3$.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 8
> **
>
> (a) Variables : $v$, $L$, $g$, $\rho$, $\Delta\rho$ donc $n = 5$, $k = 3$ et $2$ groupes $\Pi$. Pour $v$ : $\Pi_1 = v \rho^{a} g^{b} L^{c}$ avec $M^{a} \, L^{1-3a+b+c} \, T^{-1-2b} = 1$ donc $a = 0$, $b = -\dfrac{1}{2}$, $c = -\dfrac{1}{2}$ : $\Pi_1 = \dfrac{v}{\sqrt{gL}}$. Pour $\Delta\rho$ : $\Pi_2 = \Delta\rho \, \rho^{-1}$ (même dimension que $\rho$).
>
> (b) $\rho_{int} = \rho \, \dfrac{T_{ext}}{T_{int}}$ donc $\dfrac{\Delta\rho}{\rho} = 1 - \dfrac{T_{ext}}{T_{int}} = 1 - \dfrac{288}{373} \approx 0,23$.
>
> (c) $\dfrac{v_m}{\sqrt{g L_m}} = \dfrac{v_p}{\sqrt{g L_p}}$ donc $v_m = v_p \sqrt{\dfrac{L_m}{L_p}} = \dfrac{3,0}{\sqrt{10}} \approx 0,95 ~\text{m.s}^{-1}$. Durée de la montée de $90 ~\text{m}$ : $t_m = \dfrac{90}{0,95} \approx 95 ~\text{s}$ (soit $t_p/\sqrt{10}$).
>
> (d) $\dfrac{F_p}{F_m} = \dfrac{V_p}{V_m} = \left(\dfrac{L_p}{L_m}\right)^3 = 10^3$. La maquette soulève $\dfrac{1,2 \times 10^{3}}{10^3} = 1,2 ~\text{kg}$. En pratique, la maquette se refroidit plus vite (rapport surface/volume plus grand) : la similitude thermique n'est pas respectée sur de longues durées.


**q9.** **Parachute : vitesse limite et maquette**\\

On suppose que la vitesse limite de chute $v$ d'un parachute de diamètre $D$ ne dépend que du poids total $W = m g$ et de la masse volumique de l'air $\rho$.


(a) Donner $n$, $k$ et le nombre de groupes $\Pi$. Montrer que $v = C\sqrt{\dfrac{W}{\rho D^2}}$ où $C$ est une constante sans dimension.

(b) Un parachutiste de masse totale $m_p = 80 ~\text{kg}$ sous une voilure de diamètre $D_p = 8,0 ~\text{m}$ atterrit à $v_p = 5,0 ~\text{m.s}^{-1}$ ($\rho = 1,2 ~\text{kg.m}^{-3}$). Calculer $C$.

(c) On teste une maquette de diamètre $D_m = 1,0 ~\text{m}$. Quelle masse $m_m$ faut-il suspendre pour obtenir la même vitesse de chute $5,0 ~\text{m.s}^{-1}$ ?

(d) Avec la même maquette chargée de $2,0 ~\text{kg}$, quelle est la vitesse de chute ?

> [!tip]- 💡 Coup de pouce
> **Variables
> **
>
> Les variables sont $v$, $W$, $\rho$, $D$ : $n = 4$, $k = 3$. Chercher $\Pi = v^{\alpha} W^{\beta} \rho^{\gamma} D^{\delta}$ en fixant $\beta = -1$.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 9
> **
>
> (a) $n = 4$, $k = 3$ donc un seul groupe $\Pi$. $[v^\alpha W^\beta \rho^\gamma D^\delta] = M^{\beta+\gamma} \, L^{\alpha+\beta-3\gamma+\delta} \, T^{-\alpha-2\beta}$. Alors $\gamma = -\beta$, $\alpha = -2\beta$ et $\delta = -2\beta$. Pour $\beta = -1$ : $\alpha = 2$, $\gamma = 1$, $\delta = 2$ donc $\Pi = \dfrac{\rho v^2 D^2}{W}$ est constant, d'où $v = C\sqrt{\dfrac{W}{\rho D^2}}$.
>
> (b) $W_p = 80 \times 9,81 \approx 785 ~\text{N}$ et $\dfrac{W_p}{\rho D_p^2} = \dfrac{785}{1,2 \times 64} \approx 10,2$, donc $C = \dfrac{5,0}{\sqrt{10,2}} \approx 1,6$.
>
> (c) Même $v$ donc même $\dfrac{W}{D^2}$ : $m_m = m_p \left(\dfrac{D_m}{D_p}\right)^2 = 80 \times \dfrac{1}{64} = 1,25 ~\text{kg}$.
>
> (d) $v = 5,0 \times \sqrt{\dfrac{2,0}{1,25}} \approx 6,3 ~\text{m.s}^{-1}$ : plus la charge est lourde, plus la chute est rapide, en $\sqrt{m}$.


**q10.** **Régimes de vol : du moustique à l'avion**\\

On calcule le nombre de Reynolds $\mathrm{Re} = \dfrac{v L}{\nu}$ avec $\nu_{air} = 1,5 \times 10^{-5} ~\text{m}^2\text{.s}^{-1}$ (air au niveau du sol) pour trois « engins volants » :


- un moustique : $L = 3,0 ~\text{mm}$, $v = 0,30 ~\text{m.s}^{-1}$ ;
- un drone : $L = 0,30 ~\text{m}$ (corde de pale), $v = 10 ~\text{m.s}^{-1}$ ;
- un avion de ligne à l'approche : $L = 4,0 ~\text{m}$ (corde moyenne de l'aile), $v = 70 ~\text{m.s}^{-1}$.




(a) Calculer $\mathrm{Re}$ pour chacun. Classer les régimes en supposant que la viscosité domine pour $\mathrm{Re} < 10^3$.

(b) Pour une maquette de l'avion à l'échelle $1/50$ dans l'air ambiant, quelle vitesse conserverait $\mathrm{Re}$ ? Calculer le nombre de Mach correspondant ($c = 340 ~\text{m.s}^{-1}$). Conclusion ?

> [!tip]- 💡 Coup de pouce
> **Ordres de grandeur
> **
>
> Écrire chaque $\mathrm{Re}$ en notation scientifique avec $2$ chiffres significatifs. Pour b), imposer $v_m L_m = v_p L_p$ dans le même fluide.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 10
> **
>
> (a) Moustique : $\mathrm{Re} = \dfrac{0,30 \times 3,0 \times 10^{-3}}{1,5 \times 10^{-5}} = 60$. Drone : $\mathrm{Re} = \dfrac{10 \times 0,30}{1,5 \times 10^{-5}} = 2,0 \times 10^{5}$. Avion : $\mathrm{Re} = \dfrac{70 \times 4,0}{1,5 \times 10^{-5}} \approx 1,9 \times 10^{7}$. Le moustique vole dans un régime où la viscosité domine ($\mathrm{Re} \ll 10^3$) ; le drone et l'avion sont dans un régime d'inertie, l'avion avec un écoulement fortement turbulent.
>
> (b) $v_m = v_p \dfrac{L_p}{L_m} = 70 \times 50 = 3\,500 ~\text{m.s}^{-1}$ soit $\mathrm{Ma} = \dfrac{3\,500}{340} \approx 10$ : vitesse hypersonique, physiquement absurde pour un essai. On ne peut pas respecter $\mathrm{Re}$ dans l'air ambiant avec une petite maquette : on augmente la masse volumique (soufflerie pressurisée) ou on refroidit le gaz (soufflerie cryogénique), comme à la question 5.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex7-homogeneite-d-une-equation-et-dimension-d-une-grandeur-exercices-avances|Exercice 7 — (*) Homogénéité d'une équation et dimension d'une grandeur : exercices avancés]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex8-conversions-d-unites-et-unites-des-constantes-fondamentales|Exercice 8 — (*) Conversions d'unités et unités des constantes fondamentales]]

