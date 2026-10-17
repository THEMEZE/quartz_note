---
title: "Exercice 4 — Lois et Constantes Fondamentales en physiques"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/index|⬅ Retour]] · <a href="/pdfs/td1_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 4. Lois et Constantes Fondamentales en physiques

L’objectif de l’exercice est d’utiliser l’analyse dimensionnelle afin de déterminer la dimension de constante intervenant dans les lois physiques.

**q1.** **Constante de la gravitation universelle $\mathcal{G}$.**\\

La force d’attraction qui s’exerce entre deux points matériels, de masse $m$ et $m'$ , séparés par une distance $r$, est donnée, en module, par la loi d’interaction gravitationnelle de Newton :
$$
F = \mathcal{G} \frac{m m'}{r^2}.
$$



(a) Donner les dimensions des différentes grandeurs physiques de la formule.

(b) Écrire l’équation aux dimensions et en déduire la dimension de la constante universelle de la gravitation $\mathcal{G}$. Donner son unité dans le S.I. (Système International).

(c) Peut-on calculer sa valeur numérique ? \\
  *Remarque*  : la constante $\mathcal{G}$ a été mesurée directement la première fois par Henry Cavendish en 1798 au moyen de sa balance de torsion et il trouva une valeur de $6,6 10^{-11}$ S.I. (à des erreurs expérimentales près)

> [!tip]- 💡 Coup de pouce
> En isolant la constante dans l'équation de la loi physique, on détermine sa dimension globale : $[\mathcal{G}] = [F] * [r]^2 / ([m] * [m'])$.


> [!question]- 🔭 Aller plus loin — Licence : valeur de $\mathcal{G}$

> (a) [c)] L'analyse dimensionnelle ne donne pas la valeur numérique de $G$. Pour la déterminer, on utilise un protocole expérimental reposant sur la balance de torsion de Cavendish :
>
>
>
> - **Dispositif :** On accroche deux masses identiques $m$ aux deux extrémités d'une tige horizontale rigide de longueur $L$.
> - **Suspension :** La tige est suspendue en son centre par un fil vertical très fin dont on connaît la constante de torsion $C$. Le poids de la tige est négligeable devant celui des masses $m$.
> - **Interactions :** On approche deux grosses masses identiques $m'$ ($m' \gg m$) à une distance $r$ de chaque masse $m$, disposées de façon symétrique par rapport au centre du fil.
> - **Mise en mouvement :** La force d'attraction gravitationnelle exercée par chaque masse $m'$ sur la masse $m$ voisine s'écrit :
>       $$F = G \frac{m m'}{r^2}$$
> - **Équilibre des couples :** Ces forces créent un couple gravitationnel $\mathcal{M}_{\text{grav}} = F \cdot L$ qui fait tourner la tige d'un angle $\theta$. Le fil se tord jusqu'à ce que le couple de rappel de torsion $\mathcal{M}_{\text{torsion}} = C \cdot \theta$ équilibre le couple gravitationnel :
>       $$G \frac{m m'}{r^2} L = C \theta \implies G = \frac{C \theta r^2}{m m' L}$$
> - **Mesure de l'angle :** L'angle de déviation $\theta$ est mesuré très précisément au moyen d'un rayon lumineux réfléchi par un miroir solidaire du fil vertical.
> - **Réduction des erreurs :** On répète l'expérience en plaçant les masses $m'$ de l'autre côté de la tige pour observer une déviation en sens opposé (angle $2\theta$), permettant de s'affranchir des erreurs d'alignement initial.
>
>
>
> En 1798 Henry Cavendish mesure $6,6\times10^{-11}~\mathrm{kg}^{-1}\,\mathrm{m}^3\,\mathrm{s}^{-2}$. Et aujourd'hui la mesure la plus précise est $(6,67430 \pm 0,00015)\times10^{-11}~\mathrm{kg}^{-1}\,\mathrm{m}^3\,\mathrm{s}^{-2}$.


> [!question]- 🔭 Aller plus loin — Master : Équilibre des couples

> - **Équilibre des couples :**
>     La tige est suspendue en son centre $O$ par le fil de torsion ($O$ est donc le baricentre de la tige, On applique donc le Théorème du moment cinétique barycentrique (TMC*) sur la tige).
>     On note $L$ la longueur totale de la tige. Les deux petites masses
>     $m$ sont donc situées aux extrémités $A$ et $B$, avec
>     \[
>       OA=OB=\frac{L}{2}.
>     \]
>
>     La force gravitationnelle exercée par chacune des grosses masses $m'$
>     sur la petite masse $m$ située à proximité vaut
>     \[
>       F=G\frac{m m'}{r^2}.
>     \]
>
>     Calculons le moment de ces forces par rapport au point $O$.
>     Pour la force appliquée en $A$ :
>     \[
>       \vec{\mathcal M}_O(\vec F_A)
>       =
>       \overrightarrow{OA}\times\vec F_A.
>     \]
>
>     Dans la configuration considérée, la force est perpendiculaire à la
>     tige, de sorte que
>     \[
>       \left\|\vec{\mathcal M}_O(\vec F_A)\right\|
>       =
>       OA\,F
>       =
>       \frac{L}{2}F.
>     \]
>
>     La force appliquée à l'autre extrémité $B$ produit un moment de même
>     sens :
>     \[
>       \left\|\vec{\mathcal M}_O(\vec F_B)\right\|
>       =
>       \frac{L}{2}F.
>     \]
>
>     Le moment gravitationnel total par rapport à $O$ est donc
>     \[
>       \mathcal M_{\mathrm{grav}}
>       =
>       \frac{L}{2}F+\frac{L}{2}F
>       =
>       FL
>       =
>       G\frac{m m'}{r^2}L.
>     \]
>
>     Le fil de torsion exerce en $O$ un couple de rappel
>     \[
>       \mathcal M_{\mathrm{torsion}}=-C\theta.
>     \]
>
>     À l'équilibre, la somme des moments par rapport à $O$ est nulle :
>     \[
>       \sum \mathcal M_O=0.
>     \]
>
>     Ainsi,
>     \[
>       G\frac{m m'}{r^2}L-C\theta=0,
>     \]
>     d'où
>     \[
>       \boxed{
>       G=\frac{C\theta r^2}{m m'L}
>       }.
>     \]
>
> <p style="text-align:center"><a href="/figures/cavendish_exp.svg" target="_blank" rel="noopener"><img src="/figures/cavendish_exp.svg" alt="" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>


> [!question]- 🔭 Aller plus loin — Licence : Remarques $\&$ Précautions expérimentales

> 1. **Isolation aérodynamique et thermique :** 
>       Les forces gravitationnelles en jeu sont extrêmement faibles (de l'ordre de $10^{-9}\text{ N}$). Le moindre courant d'air, flux de convection thermique ou différence de température modifie le résultat. Le dispositif doit être placé sous une cloche transparente étanche.
> 2. **Mesure optique de l'angle (Amplification) :** 
>       L'angle de déviation $\theta$ est très petit. Il est mesuré sans contact mécanique au moyen d'un miroir fixe solidaire du fil vertical : un faisceau lumineux (ou laser) envoyé sur le miroir est dévié d'un angle $2\theta$ sur une règle graduée éloignée.
> 3. **Gestion des oscillations (Régime dynamique) :** 
>       Le système se comporte comme un oscillateur harmonique très peu amorti de période propre $T_0 = 2\pi \sqrt{\frac{J}{C}}$ (où $J = 2m(L/2)^2 = \frac{1}{2}mL^2$ est le moment d'inertie). Au lieu d'attendre l'extinction des oscillations qui prend plusieurs heures, on détermine l'angle d'équilibre $\theta$ en calculant la moyenne des positions extrêmes d'oscillation.
> 4. **Corrections géométriques (Attraction croisée) :** 
>       Chaque grosse masse $m'$ attire fortement la petite masse $m$ voisine, mais exerce aussi une attraction résiduelle plus faible sur la masse $m$ située à l'autre extrémité de la tige. Une correction géométrique sur la distance doit être appliquée pour les calculs de haute précision.
> 5. **Effets parasites électrostatiques et magnétiques :** 
>       Les masses et le châssis doivent être reliés à la terre ou constitués de matériaux amagnétiques (plomb, laiton) pour éviter que des forces électrostatiques ou magnétiques ne masquent l'interaction gravitationnelle.


> [!question]- 🔭 Aller plus loin — Master : De la force gravitationnelle à la courbure de l'espace-temps

> Dans le modèle de Newton, la gravitation est décrite comme une force
> attractive exercée entre deux masses :
> \[
>   F = \mathcal{G}\frac{m m'}{r^2}.
> \]
>
> Cette description est extrêmement efficace dans le domaine classique.
> Cependant, en relativité générale, la gravitation n'est plus décrite
> comme une force au sens newtonien : elle est interprétée comme une
> propriété géométrique de l'espace-temps.
>
>
>
> (a) [a)] **De la force à la géométrie.**
>
>   En relativité générale, ce n'est pas uniquement la masse qui intervient
>   comme source de la gravitation. Le tenseur énergie-impulsion
>   $T_{\mu\nu}$, qui contient notamment la densité d'énergie, la quantité
>   de mouvement, la pression et les contraintes, est relié à la courbure
>   de l'espace-temps par les équations d'Einstein :
>   \[
>     G_{\mu\nu}
>     =
>     \frac{8\pi G}{c^4}T_{\mu\nu}.
>   \]
>
>   Autrement dit, la matière et l'énergie influencent la géométrie de
>   l'espace-temps, et cette géométrie détermine à son tour le mouvement
>   des corps.
>
>   \begin{center}
>     *« La matière dit à l'espace-temps comment se courber,
>     et l'espace-temps dit à la matière comment se déplacer. »*
>   \end{center}
>
>   *Référence : Einstein Online, Max Planck Institute for
>   Gravitational Physics, « The curvature of spacetime ».*


> [!question]- 🔭 Aller plus loin — Master : Pourquoi les corps tombent-ils ?

> (a) [b)] **Pourquoi les corps tombent-ils ?**
>
>   Un corps en chute libre ne subit pas nécessairement une force
>   gravitationnelle au sens newtonien. En relativité générale, il suit
>   une géodésique de l'espace-temps, c'est-à-dire une trajectoire
>   déterminée par la géométrie locale de celui-ci.
>
>   Cette interprétation est liée au principe d'équivalence :
>   localement, un observateur en chute libre ne peut pas distinguer son
>   mouvement d'un mouvement inertiel dans une région sans gravitation.
>
>   *Référence : Einstein Online, Max Planck Institute for
>   Gravitational Physics, « The equivalence principle ».*
>
> (b) [c)] **Et le poids ?**
>
>   Cette distinction permet de comprendre pourquoi un astronaute en
>   orbite ressent l'apesanteur alors qu'il se trouve toujours dans le
>   champ gravitationnel terrestre.
>
>   L'astronaute est en chute libre et suit approximativement une
>   géodésique. À l'inverse, un objet posé sur une table est empêché de
>   suivre librement sa géodésique par la force de contact exercée par
>   la table.
>
>   Le « poids » que nous ressentons lorsque nous sommes debout est donc
>   associé à la force de contact qui nous empêche de tomber librement,
>   et non à une force gravitationnelle ressentie directement comme une
>   poussée.
>
>   *Référence : Einstein Online, Max Planck Institute for
>   Gravitational Physics, « Falling freely ».*


> [!question]- 🔭 Aller plus loin — Master : Masse inertielle et masse gravitationnelle.

> (a) [d)] **Masse inertielle et masse gravitationnelle.**
>
>   Dans la mécanique classique, on distingue la masse inertielle, qui
>   intervient dans la relation
>   \[
>     \vec{F}=m_{\mathrm{i}}\vec{a},
>   \]
>   et la masse gravitationnelle, qui intervient dans l'interaction
>   gravitationnelle.
>
>   L'égalité entre ces deux masses constitue le contenu expérimental
>   du principe d'équivalence faible. En relativité générale, cette
>   propriété devient un principe fondamental de la théorie : localement,
>   tous les corps en chute libre suivent la même géométrie gravitationnelle,
>   indépendamment de leur composition.
>
>   Il faut cependant éviter de dire que « seule la masse courbe
>   l'espace-temps ». Dans les équations d'Einstein, c'est le tenseur
>   énergie-impulsion $T_{\mu\nu}$ qui joue le rôle de source.
>
>   *Référence : Einstein Online, Max Planck Institute for
>   Gravitational Physics, « The equivalence principle ».*
>
> (b) [e)] **Retour à la loi de Newton.**
>
>   Dans la limite des champs gravitationnels faibles et des vitesses
>   petites devant $c$, les équations de la relativité générale
>   conduisent à la loi de Newton :
>   \[
>     F = G\frac{m m'}{r^2}.
>   \]
>
>   La force gravitationnelle newtonienne doit donc être comprise comme
>   une approximation de la description relativiste dans son domaine
>   de validité.
>
>   *Référence : Einstein Online, Max Planck Institute for
>   Gravitational Physics, « Newtonian limit of general relativity ».*


> [!question]- 🔭 Aller plus loin — Master : Gravitation et interactions quantiques.

> (a) [f)] **Gravitation et interactions quantiques.**
>
>   Une différence fondamentale apparaît lorsqu'on compare la gravitation
>   à l'électromagnétisme.
>
>   L'électromagnétisme est décrit par une théorie quantique des champs.
>   Son boson médiateur est le photon, qui possède un spin
>   \[
>     s=1.
>   \]
>
>   L'interaction électromagnétique peut être attractive ou répulsive :
>   deux charges électriques de même signe se repoussent, tandis que deux
>   charges de signes opposés s'attirent.
>
>   Une éventuelle description quantique perturbative de la gravitation
>   fait apparaître une particule hypothétique appelée *graviton*,
>   qui serait un boson de spin
>   \[
>     s=2.
>   \]
>
>   Le graviton n'a cependant jamais été observé expérimentalement.
>   Il est donc important de distinguer son statut théorique de celui
>   du photon, qui est une particule expérimentalement établie.
>
>   *Référence : CERN, « The Standard Model ».*
>
> (b) [g)] **Les interactions fondamentales.**
>
>   Il est donc incorrect de dire que « toutes les forces sont
>   électromagnétiques ». La physique actuelle distingue quatre
>   interactions fondamentales :
>   \[
>     \boxed{
>     \text{gravitationnelle},
>     \quad
>     \text{électromagnétique},
>     \quad
>     \text{faible},
>     \quad
>     \text{forte}.
>     }
>   \]
>
>   Les interactions électromagnétique, faible et forte sont décrites
>   dans le cadre du Modèle standard de la physique des particules.
>   La gravitation est décrite par la relativité générale et n'est pas
>   intégrée au Modèle standard.
>
>   La recherche d'une théorie quantique de la gravitation permettant
>   de réunir ces deux descriptions constitue encore un problème ouvert
>   de la physique fondamentale.
>
>   *Référence : CERN, « The Standard Model ».*


> [!example]- 📝 Solution détaillée
> **Dimmension de $[\mathcal{G}]$
> **
>
> (a) %\vspace{-0.5cm}
>
>
> - [<span style="color:#8C0000">$\bullet$</span>] <span style="color:#8C0000">la force : $[F] = M * L * T^{-2}$</span>
> - [<span style="color:#57659E">$\bullet$</span>] <span style="color:#57659E">les masses : $[m] = [m'] = M$</span>
> - [<span style="color:#4A3628">$\bullet$</span>] <span style="color:#4A3628">la distance : $[r] = L$</span>
> - [<span style="color:#2E7D5B">$\bullet$</span>] <span style="color:#2E7D5B">la constante universelle de la gravitation :
>       $[\mathcal{G}] = ??? $</span>
>
>
>
>
>     $$
>     $ \displaystyle \color{#8C0000} F$ = $ \displaystyle \color{#2E7D5B} \mathcal{G}$  \frac{$ \displaystyle \color{#57659E} m m'$}{$ \displaystyle \color{#4A3628} r^2$ }.
>     $$
>     \begin{tikzpicture}[overlay,remember picture]
>       \draw[  opacity = 1 ]
>         (Force) edge[line width=0.2ex ,color = colorOne ,arrows = -{Computer Modern Rightarrow[sharp ,length=0.1cm]},  , out = 110 , in = 0  ]node[pos=1, left]<span style="color:#8C0000">\fontsize{6pt}{10pt}\selectfont \bfseries  $[F] = M * L * T^{-2}$  </span>($(Force) + (-1.05cm,0.45cm)$)
>       ;
>
>       \draw[  opacity = 1 ]
>       (Gravi) edge[line width=0.2ex ,color = colorSix ,arrows = -{Computer Modern Rightarrow[sharp ,length=0.1cm]},  , out = -70 , in = 180  ]node[pos=1, draw = none , right=0.00cm , rectangle  , shift = {(0.00cm , -0.0cm)} ]<span style="color:#2E7D5B">\fontsize{6pt}{4}\selectfont \bfseries $\displaystyle [\mathcal{G}] = ??? $ </span>($(Gravi) + (2.0cm,-0.95cm)$)
>       ;
>
>       \draw[  opacity = 1 ]
>       (Massesmm) edge[line width=0.2ex ,color = colorFour ,arrows = -{Computer Modern Rightarrow[sharp ,length=0.1cm]},  , out = 70 , in = 180  ]node[pos=1, draw = none , right=0.00cm , rectangle  , shift = {(0.00cm , -0.0cm)} ]<span style="color:#57659E">\fontsize{6pt}{4}\selectfont \bfseries $\displaystyle [m] = [m'] = M $ </span>($(Massesmm) + (1.0cm,0.65cm)$)
>       ;
>
>       \draw[  opacity = 1 ]
>       (Distance) edge[line width=0.2ex ,color = colorFive ,arrows = -{Computer Modern Rightarrow[sharp ,length=0.1cm]},  , out = -10 , in = 180  ]node[pos=1, draw = none , right=0.00cm , rectangle  , shift = {(0.00cm , -0.0cm)} ]<span style="color:#4A3628">\fontsize{6pt}{4}\selectfont \bfseries $\displaystyle [r] = L $ </span>($(Distance) + (1.0cm,-0.05cm)$)
>       ;
>
>
>     \end{tikzpicture}
>
> (b) En isolant la formule il vient que $ {\displaystyle {\color{#2E7D5B} \mathcal{G}} = {\color{#8C0000} F}  \frac{\color{#4A3628}r^2}{ \color{#57659E} mm'}}$ donc 
>
>
> - ${\displaystyle {\color{#2E7D5B}[\mathcal{G}]}  = {\color{#8C0000} \overbrace{M * L * T^{-2}}^{[F]}} \frac{{\color{#4A3628} \overbrace{L^2}^{[r^2]}}}{{\color{#57659E}\underbrace{M^2}_{[mm']}}}  } = {\color{#2E7D5B} M^{-1} * L^3 * T^{-2}} $ .
> - son unité est donnée en ${\color{#2E7D5B} kg^{-1} \cdot m^3 \cdot s^{-2}} $
>
> (c) [c)] L'analyse dimensionnelle ne donne pas la valeur numérique de $G$.


**q2.** **(${}^*$) Constante diélectrique $\bm{\varepsilon_0}$** (ou permittivité du vide)\\

Coulomb énonce la loi d’interaction électrostatique en 1785 : la force qui s’exerce entre deux charges électriques $q$ et $q'$ , séparées par une distance $r$, est donnée par
$$
F = \frac{1}{4 \pi \varepsilon_0 } \frac{q q'}{r^2}.
$$



(a) Donner les dimensions des différentes grandeurs physiques de la formule.

(b) Écrire l’équation aux dimensions et en déduire la dimension de la constante diélectrique. Donner son unité dans le S.I.

> [!tip]- 💡 Coup de pouce
> En isolant la constante dans l'équation de la loi physique, on détermine sa dimension globale : $[\varepsilon_0] = 1 / [F] * [q] * [q']/ [r]^2 $.
>
> L'intensité électrique I est une dimension de base. La charge q s'exprime comme q = I * t, d'où [q] = I * T.


> [!question]- 🔭 Aller plus loin — Licence
> $\varepsilon_0 = \frac{ 10^7}{ 4 \pi c^2 }\, F\cdot m\cdot s^{-2} = 8,854~187\times 10^{-12} ~{\color{#2E7D5B} \overbrace{kg^{-1}\cdot m^{-3}\cdot s^4\cdot A^2}^{F/m}}$


> [!example]- 📝 Solution détaillée
> **Dimmension de $[\varepsilon_0]$
> **
>
> (a) %\vspace{-0.5cm}
>
>
> - [<span style="color:#8C0000">$\bullet$</span>] <span style="color:#8C0000">la force : $[F] = M * L * T^{-2}$</span>
> - [<span style="color:#57659E">$\bullet$</span>] <span style="color:#57659E">les charges : $[q] = [q'] = I * T $</span>
> - [<span style="color:#4A3628">$\bullet$</span>] <span style="color:#4A3628">la distance : $[r] = L$</span>
> - [<span style="color:#2E7D5B">$\bullet$</span>] <span style="color:#2E7D5B">la constante diélectrique : $[\varepsilon_0] = ???$ </span>
>
>
>
>
>     $$
>     $ \displaystyle \color{#8C0000} F$ = \frac{1}{4\pi $ \displaystyle \color{#2E7D5B} \varepsilon_0$}  \frac{$ \displaystyle \color{#57659E} q q'$}{$ \displaystyle \color{#4A3628} r^2$ }.
>     $$
>     \begin{tikzpicture}[overlay,remember picture]
>       \draw[  opacity = 1 ]
>         (Force) edge[line width=0.2ex ,color = colorOne ,arrows = -{Computer Modern Rightarrow[sharp ,length=0.1cm]},  , out = 110 , in = 0  ]node[pos=1, left]<span style="color:#8C0000">\fontsize{6pt}{10pt}\selectfont \bfseries  $[F] = M * L * T^{-2}$  </span>($(Force) + (-1.05cm,0.45cm)$)
>       ;
>
>       \draw[  opacity = 1 ]
>       (Gravi) edge[line width=0.2ex ,color = colorSix ,arrows = -{Computer Modern Rightarrow[sharp ,length=0.1cm]},  , out = -70 , in = 180  ]node[pos=1, draw = none , right=0.00cm , rectangle  , shift = {(0.00cm , -0.0cm)} ]<span style="color:#2E7D5B">\fontsize{6pt}{4}\selectfont \bfseries $\displaystyle [\varepsilon_0] = ??? $ </span>($(Gravi) + (2.0cm,-0.95cm)$)
>       ;
>
>       \draw[  opacity = 1 ]
>       (Massesmm) edge[line width=0.2ex ,color = colorFour ,arrows = -{Computer Modern Rightarrow[sharp ,length=0.1cm]},  , out = 70 , in = 180  ]node[pos=1, draw = none , right=0.00cm , rectangle  , shift = {(0.00cm , -0.0cm)} ]<span style="color:#57659E">\fontsize{6pt}{4}\selectfont \bfseries $\displaystyle [q] = [q'] = I*T $ </span>($(Massesmm) + (1.0cm,0.65cm)$)
>       ;
>
>       \draw[  opacity = 1 ]
>       (Distance) edge[line width=0.2ex ,color = colorFive ,arrows = -{Computer Modern Rightarrow[sharp ,length=0.1cm]},  , out = -10 , in = 180  ]node[pos=1, draw = none , right=0.00cm , rectangle  , shift = {(0.00cm , -0.0cm)} ]<span style="color:#4A3628">\fontsize{6pt}{4}\selectfont \bfseries $\displaystyle [r] = L $ </span>($(Distance) + (1.0cm,-0.05cm)$)
>       ;
>
>
>     \end{tikzpicture}
>
> (b) En isolant la formule il vient que $ {\displaystyle {\color{#2E7D5B} \varepsilon_0} =  \frac{1}{4 \pi} \frac{{ \color{#57659E} mm'} }{{\color{#8C0000} F} {\color{#4A3628}r^2} } }$ donc 
>
>
> - ${\displaystyle {\color{#2E7D5B}[\varepsilon_0]}  = {\color{#8C0000} \overbrace{M^{-1} * L^{-1} * T^{2}}^{[F^{-1}]}} \frac{ {\color{#57659E} \overbrace{I^2*T^2}^{[qq']} } }{ {\color{#4A3628} \underbrace{L^2}_{[r^2]} } } = {\color{#2E7D5B} M^{-1} * L^{-3} * T^4 * I^2}} $ .
> - son unité est donnée en ${\color{#2E7D5B} kg^{-1}\cdot m^{-3}\cdot s^4\cdot A^2} $


**q3.** **(${}^*$) Constante des gaz parfait $\bm{R}$** \\

La loi des gaz parfait relie le volume $V$, la pression $P$ et la température $T$ de $n$ moles de gaz :
$$
PV = n RT.
$$



(a) Donner les dimensions des différentes grandeurs physiques de la formule.

(b) Écrire l’équation aux dimensions et en déduire la dimension de la constante des gaz parfait $R$. Donner son unité dans le S.I.

> [!tip]- 💡 Coup de pouce
> Le produit de la pression par le volume $P * V$ représente une dimension d'énergie :$M * L^2 * T^{-2}$.


> [!question]- 🔭 Aller plus loin — Licence
> $R = N_A \cdot k_B = 8,314 ~ {\color{#2E7D5B} \text{J} \cdot \text{mol}^{-1} \cdot \text{K}^{-1} }$ avec $N_A = 6,022 \times 10^{23} ~ \text{mol}^{-1}$ (nombre d'Avogadro) et $k_B = 1,380 \times 10^{-23} ~ \text{J} \cdot \text{K}^{-1}$ (constante de Boltzmann)


> [!example]- 📝 Solution détaillée
> **Dimmension de $[\mathcal{G}]$
> **
>
> (a) %\vspace{-0.5cm}
>
>
> - la pression : $[P] = [F]/[S] = M * L^{-1} * T^{-2}$
> - la force : $[F] = M * L * T^{-2}$
> - le volume : $[V] = L^3$
> - la quantitée de matière : $[n] = N $
> - la température: $[T] = K$.
> - la constante des gaz parfait : $[R] = ??? $.
>
> (b) En isolant la formule il vien que $R = PV/(nT)$ donc 
>
>
> - ${\displaystyle [R] =  \frac{ \overbrace{M * L^{-1} * T^{-2}}^{[P]} * \overbrace{L^3}^{[V]} }{ \underbrace{mol}_{[N]} * \underbrace{\Theta}_{[T]} } = M * L^2 * T^{-2} * \Theta^{-1} * N^{-1} } $ .
> - son utité est donnée en $J \cdot K^{-1} \cdot mol^{-1}$ (ou $kg \cdot m^2 \cdot s^{-2} \cdot K^{-1} \cdot mol^{-1}$ ).
>
>
>
>
>
> (a) %\vspace{-0.5cm}
>
>
> - [<span style="color:#8C0000">$\bullet$</span>] <span style="color:#8C0000">la pression : $[P] = [F]/[S] = M * L^{-1} * T^{-2}$</span>
> - [<span style="color:#57659E">$\bullet$</span>] <span style="color:#57659E">le volume : $[V] = L^3$</span>
> - [<span style="color:#4A3628">$\bullet$</span>] <span style="color:#4A3628">la quantitée de matière : $[n] = N$</span>
> - [<span style="color:#1565C0">$\bullet$</span>] <span style="color:#1565C0">la température : $[T] = K$</span>
> - [<span style="color:#2E7D5B">$\bullet$</span>] <span style="color:#2E7D5B">la constante des gaz parfait : $[R] = ??? $ </span>
>
>
>
>
>     $$
>     $ \displaystyle \color{#8C0000} P$ $ \displaystyle \color{#57659E} V$  =  $ \displaystyle \color{#4A3628} n$ $ \displaystyle \color{#2E7D5B} R$ $ \displaystyle \color{#1565C0} T$
>     $$
>     \begin{tikzpicture}[overlay,remember picture]
>       \draw[  opacity = 1 ]
>         (Force) edge[line width=0.2ex ,color = colorOne ,arrows = -{Computer Modern Rightarrow[sharp ,length=0.1cm]},  , out = 110 , in = 0  ]node[pos=1, left]<span style="color:#8C0000">\fontsize{6pt}{10pt}\selectfont \bfseries  $[P] = M * L^{-1} * T^{-2}$  </span>($(Force) + (-1.05cm,0.45cm)$)
>       ;
>
>       \draw[  opacity = 1 ]
>       (Gravi) edge[line width=0.2ex ,color = colorSix ,arrows = -{Computer Modern Rightarrow[sharp ,length=0.1cm]},  , out = -70 , in = 180  ]node[pos=1, draw = none , right=0.00cm , rectangle  , shift = {(0.00cm , -0.0cm)} ]<span style="color:#2E7D5B">\fontsize{6pt}{4}\selectfont \bfseries $\displaystyle [R] = ??? $ </span>($(Gravi) + (2.0cm,-0.65cm)$)
>       ;
>
>       \draw[  opacity = 1 ]
>       (Massesmm) edge[line width=0.2ex ,color = colorFour ,arrows = -{Computer Modern Rightarrow[sharp ,length=0.1cm]},  , out = 70 , in = 180  ]node[pos=1, draw = none , right=0.00cm , rectangle  , shift = {(0.00cm , -0.0cm)} ]<span style="color:#57659E">\fontsize{6pt}{4}\selectfont \bfseries $\displaystyle [V] = L^3 $ </span>($(Massesmm) + (1.0cm,0.65cm)$)
>       ;
>
>       \draw[  opacity = 1 ]
>       (Temp) edge[line width=0.2ex ,color = colorThree ,arrows = -{Computer Modern Rightarrow[sharp ,length=0.1cm]},  , out = 10 , in = 180  ]node[pos=1, draw = none , right=0.00cm , rectangle  , shift = {(0.00cm , -0.0cm)} ]<span style="color:#1565C0">\fontsize{6pt}{4}\selectfont \bfseries $\displaystyle [T] = K$ </span>($(Temp) + (1.0cm,0.05cm)$)
>       ;
>
>       \draw[  opacity = 1 ]
>       (Distance) edge[line width=0.2ex ,color = colorFive ,arrows = -{Computer Modern Rightarrow[sharp ,length=0.1cm]},  , out = -90 , in = 180  ]node[pos=1, draw = none , right=0.00cm , rectangle  , shift = {(0.00cm , -0.0cm)} ]<span style="color:#4A3628">\fontsize{6pt}{4}\selectfont \bfseries $\displaystyle [n] = N $ </span>($(Distance) + (1.0cm,-0.95cm)$)
>       ;
>
>
>     \end{tikzpicture}
>
> (b) En isolant la formule il vient que $ {\displaystyle {\color{#2E7D5B} \varepsilon_0} =  \frac{1}{4 \pi} \frac{{ \color{#57659E} mm'} }{{\color{#8C0000} F} {\color{#4A3628}r^2} } }$ donc 
>
>
> - ${\displaystyle {\color{#2E7D5B}[\varepsilon_0]}  = {\color{#8C0000} \overbrace{M^{-1} * L^{-1} * T^{2}}^{[F^{-1}]}} \frac{ {\color{#57659E} \overbrace{I^2*T^2}^{[qq']} } }{ {\color{#4A3628} \underbrace{L^2}_{[r^2]} } } = {\color{#2E7D5B} M^{-1} * L^{-3} * T^4 * I^2}} $ .
> - son unité est donnée en ${\color{#2E7D5B} kg^{-1}\cdot m^{-3}\cdot s^4\cdot A^2} $
>
> (c) En isolant la formule il vien que ${\displaystyle {\color{#2E7D5B} R}  = \frac{{\color{#8C0000} P} {\color{#57659E} V } }{ {\color{#4A3628} n} {\color{#1565C0} T }}}$ donc 
>
>
> - ${\displaystyle {\color{#2E7D5B} [R]}  =  \frac{ {\color{#8C0000} \overbrace{M * L^{-1} * T^{-2}}^{[P]}}  * {\color{#57659E} \overbrace{L^3}^{[V]}}  }{ {\color{#4A3628} \underbrace{N}_{[n]} } * {\color{#1565C0} \underbrace{\Theta}_{[T]}} } = {\color{#2E7D5B} M * L^2 * T^{-2} * \Theta^{-1} * N^{-1} } } $ .
> - son utité est donnée en ${\color{#2E7D5B}J \cdot K^{-1} \cdot mol^{-1}} $ (ou ${\color{#2E7D5B} kg \cdot m^2 \cdot s^{-2} \cdot K^{-1} \cdot mol^{-1}} $ ).


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex1-grandeurs-physiques-fondamentales-dimensions-et-unites-de-base|Exercice 1 — Grandeurs physiques fondamentales : dimensions et unités de base]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex2-grandeurs-derivees-equation-au-dimensions-dimension-et-unites-derivees-composees|Exercice 2 — Grandeurs Dérivées : Équation au dimensions , dimension et unités dérivées (composées)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex3-homogeneite-et-analyse-dimensinnelle|Exercice 3 — Homogénéité et Analyse Dimensinnelle]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex5-l-analyse-dimensionnelle-comme-outil-de-prediction|Exercice 5 — L'analyse dimensionnelle comme outil de prédiction]]

