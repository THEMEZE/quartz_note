---
title: L.P. 05 - M2 - Lois de conservation en dynamique
tags:
  - Agrégation
  - Physique
  - Oral
---
---

- **Niveau**  : Licence 
- **Prérequis** : Mécanique du point et du solide, [[Physique/Mécanique du Solide/M1 Rappels et compléments#$ bullet$ Référentiel barycentrique | Référentiel barycentrique ]], Cinématique des fluides, Notions sur la viscosité, Équation d’ Euler

---

[^1]: Physique Tout-en-un MP · MP* (ancien programme), Dunod. 
[^2]: Physique Spé. MP*, MP et PT*, PT, Gié, Sarmant, Olivier, More, Tec & Doc, 2000. 
[^3]: Mécanique 1, Jean-Pierre Faroux, Jacques Renault, Dunod, 1996. 
[^4]: Comparaison entre le mouvement de Kepler et le mouvement elliptique harmonique, Jean Sivardière, BUP n°751. 
[^5]: Mécanique, Landau & Lifchitz. 
[^6]: Mécanique : fondements et applications (7e édition), J-Ph Pérez, Dunod (2014). 
[^7]: Tout-en-un MPSI/PCSI (ancien programme, 3e édition), Dunod.
[^8]: Physique pour l'agrégation Jules Fillette - Julien Froustey - Hugo Roussille
[^9]: Physique Spé. PC*, PC Cours et exercices d'application Stéphane OLIVIER, Hubert GIÉ, Jean-Pierre SARMANT
[^10]: Formulaire MATHS, PHYSIQUE, CHIMIE, SII (2e édition), MPSI-MP , Bertrand Hauchecorne
[^11]: Formulaire MATHS, PHYSIQUE, CHIMIE, SII (3e édition), PCSI-MPSI/PTSI-PSI , Bertrand Beaufils
[^12]: Physique Tout-en-un PC · PC* , Dunod. 
[^13]: Hydrodtnamique Physique(3em-édition). Étienne GUYON, Jean-Pierre HULIN, and Lucand PETIT. 


>- 👉 <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Oraux/2025%20Guillaume%20Themeze/LP/L.P.02-M1-Gravitation_split.pdf#page=10&zoom=125" target="_blank" rel="noopener noreferrer">Manuscrit page 10</a>
>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/index.html?pdf=Aggregation%20Physique-Chimie/Oraux/" target="_blank" rel="noopener noreferrer">Lectures notes</a>

>-  <a href="https://drive.google.com/drive/folders/1i2FSRuEZTBRqYO-y2Ji_k-yNDNXvW4se?usp=drive_link/" target="_blank" rel="noopener noreferrer">Aggrégatifs</a>
>- <a href="https://drive.google.com/drive/folders/1EC5KW0wH97j7zVyYvGNlaMYUPvEYJwLB?usp=drive_link" target="_blank" rel="noopener noreferrer">Archives</a>

>-  <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Oraux/2018%20Benjamin%20Marchetti/lecon_physique_marchetti.pdf#page=21&zoom=125" target="_blank" rel="noopener noreferrer">Manuscrit BM</a> <-  <a href="https://marchettibenjamin.wordpress.com/agregation/plans-de-lecons/" target="_blank" >site perso</a>
>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Oraux/2019%20Jules%20Fillette/LeconsPhysique.pdf#page=23&zoom=125" target="_blank" rel="noopener noreferrer">Manuscrit JF</a>
>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Oraux/2019%20Hugo%20Roussille/plans_lecon_physique.pdf#page=24&zoom=125" target="_blank" rel="noopener noreferrer"> Manuscrit HR</a>
>- <a href="https://github.com/AnassNajlaoui/Lecons-Anass-Najlaoui-Agregation-Physique-2026/tree/main" target="_blank" rel="noopener noreferrer"> Manuscrit AN</a>

---


---

 #### 🎯 Fil directeur**

> **Symétries → lois de conservation → réduction drastique des équations du mouvement**

Les lois de conservation ne sont pas des « accidents » : elles proviennent de propriétés fondamentales de l’espace et du temps (théorème de Noether).

---
#### Plan (annoncé à l’oral)

I – Conservation de la quantité de mouvement (translation spatiale)  
II – Conservation du moment cinétique (rotation)  
III – Conservation de l’énergie (translation temporelle)  
IV – Lois de conservation en mécanique des fluides  
V. Ouverture : Noether et portée générale

---
#### Introduction 

- En mécanique, plusieurs théorèmes fondamentaux établissent un lien direct entre les variations temporelles de certaines grandeurs physiques et des « sources » qui les produisent. Par exemple, le **Principe Fondamental de la Dynamique** $(\mathsf{PFD})$ (**théorème de la résultante cinétique** $(\mathsf{TRC})$) relie la variation de la quantité de mouvement aux forces appliquées, tandis que le **Théorème du Moment Cinétique** $(\mathsf{TMC})$ relie la variation du moment cinétique aux moments des forces.

- Ces formulations ont une conséquence immédiate et profonde : en l’absence de telles « sources » — c’est-à-dire lorsque les forces ou les moments de forces s’annulent — les grandeurs associées sont **conservées**. On obtient ainsi des lois de conservation, qui jouent un rôle central en physique.

- Ces lois sont d’une importance capitale, car elles permettent souvent de simplifier considérablement l’analyse de systèmes complexes. En particulier, elles offrent des outils puissants pour résoudre des problèmes difficiles, comme celui du **système à deux corps**, que nous étudierons tout au long de cette leçon afin d’illustrer concrètement leur efficacité et leur portée.

---

# I – Conservation de la quantité de mouvement

## 1) Théorème fondamental (Loi de conservation)

- Système matériel $\mathscr S$ dans un référentiel galiléen $\mathscr R$. La **Théorème de la résultante cinétique** dans le cas d’un système isolé (ou 👉  pseudo-isolé : résultante des forces nulle $\overrightarrow{R}_{\mathscr S/ \mathscr R}^{\text{ext}} = 0$) :

$$  
\frac{d\overrightarrow P_{\mathscr S/ \mathscr R}}{dt} = \overrightarrow{R}_{\mathscr S/ \mathscr R}^{\text{ext}} = 0  
$$

avec  $\overrightarrow P_{\mathscr S/ \mathscr R} = \sum_i m_i \overrightarrow v_i$ , ou $\overrightarrow P_{\mathscr S/ \mathscr R} = \iiint_{ M \in \mathscr S }  \overrightarrow{sv} (M) \underbrace{\mu (M) d\tau }_{d m }$. Alors $\overrightarrow P_{\mathscr S/ \mathscr R} = \overrightarrow{\text{cste}}$ : il s’agit d’une **intégrale première du mouvement**. [^1]

- **Interprétation profonde** : 👉 **Homogénéité de l’espace** : Si les lois de la physique ne dépendent pas de la position ⇒ conservation de la quantité de mouvement. (i.e. Version "physicien" :  il n’y a pas de force selon $\vec{e}_x$ ; Si $U(y,z)$ ne dépend pas de $x$ ⇒ $P_x$ conservée ).

## 2) Exemples
- Application à l’ours sur la banquise. ([^1] p 256)
 - discuter les cas limites $m \ll M$ et $m \gg M$ ([^1] p 926)
 - Obtenir la relation $D/d = m/(M +m)$ ([^1] p 256).
 - message important : on ne connaît pas du tout $v(t)$, l’ours peut faire des allers-retours, accélérer puis ralentir, ramper, tant qu’à la fin il a parcouru la distance $d$ sur le bloc de glace la conservation de $\vec{p}$ fait le reste :  le chemin parcouru par l’ours ne joue aucun rôle, seuls les états initial et final sont importants!
 
>[!tip]- message (oral)
>
>Ours sur la banquise :
>
>- Pas besoin de connaître le détail du mouvement
  >  
>- Seule la conservation de $\vec P$ fixe le résultat final
 >   
>
>👉 Message jury : **puissance globale des lois de conservation**

>[!tip]- Remaque.  En réalité, la quantité de mouvement est une grandeur *conservative* et pas *constante* : elle n’est « ni créée ni détruite ». Voir [^2] p 305 pour plus de détails.
>Remarquons à ce titre que la force qui apparaît comme "source" de $\vec{P}$ ne correspond qu’à la quantité de mouvement de quelque chose d’autre qui est transférée, i.e. force = terme d’échange avec l’extérieur. En bref, $\overrightarrow{P}_{\text{Univers}} = \overrightarrow{\text{cste}}$

## 3) Application au problème à deux corps

1.  Notation, **théorème de la résultante cinétique** $(\mathsf{TRC})$ pour le centre de gravité G. ([^1] p 137 [^8] p 58 )
- Passage dans le référentiel barycentrique, galiléen ici car $\vec{v}_{\mathscr R}(G) =\overrightarrow{\text{cste}}$. 
2. Mobile fictif et masse réduite.

### 1) Mise en équation 

On considère l'exemple le plus général de deux corps ponctuels ($M_1$ , de masse $m_1$ et $M_2$ de masse $m_2$) en interaction mutuelle. L'ensemble est isolée et on étudie son mouvement dans un référentiel galiléen $\mathscr R$.

>[!note]- Notation.
>
>**Référentiel**
>- un référentiel $\mathscr R \doteq ( O ; \vec{e}_x ,  \vec{e}_y , \vec{e}_z )$ ; repère cartésien, et on notera la base $\mathscr B = (\vec{e}_x ,  \vec{e}_y , \vec{e}_z )$; 
>- un référentiel $\mathscr R_G \doteq ( G ; \vec{e}_{x} ,  \vec{e}_{y} , \vec{e}_{z} )$ ;  On verra que $\mathscr R_G$ est en translation par rapport à $\mathscr R$.
>
>**Position**
>- Dans le référentiel $\mathscr R$ on note le vecteur-position du point $M_1$ par $\vec{r}_1  \doteq \overrightarrow{OM_1}$ et le vecteur-positiondu point $M_1$ par $\vec{r}_2  \doteq \overrightarrow{OM_2}$. 
>- On note $G$ ne centre de gravité des deux corp $M_1$ et $M_2$. Dans le référentiel $\mathscr R$ on note le vecteur-position  du point  $G$ par $\vec{r}_G  \doteq \overrightarrow{OG}$.

L'application du **Principe Fondamental de la Dynamique** $(\mathsf{PFD})$ à chaque corps donne :
$$
\begin{array}{rcl}
\displaystyle m_1 \left . \frac{d^2 \vec{r}_1}{{dt}^2} \right )_{\mathscr R} & = & \overrightarrow{F}_{2 \to 1 } \\
\displaystyle m_2 \left . \frac{d^2 \vec{r}_2}{{dt}^2} \right )_{\mathscr R} & = & \overrightarrow{F}_{1 \to 2 }
\end{array}
$$
et le principe des actions réciproques implique $\overrightarrow{F}_{2 \to 1 } = - \overrightarrow{F}_{2 \to 1 }$. En sommant ces deux équations, on observe que le barycentre $G$ du système, défini par $(m_1 + m_2) \vec r_G = m_1 \vec r_1 + m_2 \vec r_2$, a un mouvement rectiligne uniforme :
$$
\left . \displaystyle \frac{d^2 \vec r_G }{{dt}^2}\right )_{\mathscr R} = \vec 0.
$$
Le référentiel $\mathscr R_G$, en translation par rapport à $\mathscr R$ et dans lequel $G$ est au repos (autrement dit il s'agit du *référentiel barycentrique* $\mathscr R^\ast$ du système), est donc galiléen.

>[!tip]- Remarque. Ce résultat peut s'obtenir directement en appliquant le **théorème de la résultante cinétique** $(\mathsf{TRC})$ au système global, qui est isolé.

Donc la vitesse un centre de gravité dans les référentiel $\mathscr R$ est constante :
$$
\vec{v}_{\mathscr R}(G) =\overrightarrow{\text{cste}},
$$
donc on peut passer  dans le référentiel barycentrique ($\mathscr R^\ast$ = $\mathscr R_G$). 


Le mouvement global des deux corps étant déterminé, il reste a s'intéresser au mouvement relatif.
### 2) Étude du mouvement relatif 

Étudions la coordonnée relative $\vec{r} = \vec{r}_2 - \vec{r}_1$. En faisant la différence pondérée des équations du $(\mathsf{PFD})$, on obtient :
$$
\left . \frac{d^2 \vec{r}}{{dt}^2} \right )_{\mathscr R} = \left (  \frac{1}{m_1} + \frac{1}{m_2}  \right ) \overrightarrow{F}_{1 \to 2 }.
$$
On en déduit la **masse réduite** $\mu$ telle que : 
$$
\frac{1}{\mu} =  \frac{1}{m_1} + \frac{1}{m_2} \quad \Longleftrightarrow \quad \mu =  \frac{m_1 m_2 }{ m_1 + m_2 }.
$$
Ainsi le mouvement relatif des deux corps est régi par l'équation différentielle
$$
\mu \left . \frac{d^2 \vec{r}}{{dt}^2} \right )_{\mathscr R}  = \overrightarrow{F}_{1 \to 2 },
$$
qui est identique à ce que l'on obtiendrait par application du $(\mathsf{PFD})$ dans le référentiel $\mathscr R_G$, galiléen, pour un unique corps de masse $\mu$ situé en un point $M$ vérifiant $\overrightarrow{GM} = \overrightarrow{M_1M_2} $, et soumis à une force $\overrightarrow{F}_{1 \to 2 }$. Or, par symétrie, la force $\overrightarrow{F}_{1 \to 2 }$ est nécessairement portée par la droite $(\mathsf{M_1M_1})$ qui contient le barycentre $G$ : c'est donc, dans $\mathscr R_G$, une force *centrale* de centre $G$.

>[!success]- $\overrightarrow{F}_{1 \to 2 } \in \bigcap P_s^i $ avec $P_s^i$ un plan de symétrie du système.
>
>En toute rigueur, la force est un "vrais" vecteur donc elle appartient à tout plan de symétrie du système. En l'occurence pour des corps ponctuels tous les plans contenant la droite $(\mathsf{M_1M_1})$ sont dans le plan de symétrie. La force $\overrightarrow{F}_{1 \to 2 }$ est donc contenus dans l'intersection de tous ces plans, à savoir la droite $(\mathsf{M_1M_1})$.

On peut donc entièrement ramener l'étude du mouvement relatif des corps à celle d'un unique point matériel, appelé "**particule réduite**" ( ou "**mobile fictif**"), plongé dans un champ de force centrale. 

> [!warning]-
> L'argument crucial est la colinéarité de $\overrightarrow{F}_{1 \to 2}$ avec $\overrightarrow{M_1 M_2}$. Une fois cela vérifié, on voit que les forces centrales régissent le mouvement d'une très grande variété de situation ! Remarquons à cette occasion que $\overrightarrow{F}_{1 \to 2}$ n'est centrale que dans le référentiel $\mathscr R_G$, mais pas dans le premier référentiel galiléen initial $\mathscr R$ dans lequel $G$ n'est pas un point fixe !

>[!tip]- La "vrais" $3^{ème}$ Loi de Kepler
>
>$$
>\begin{array}{rcl}
>\displaystyle \mu \left . \frac{d^2 \vec r}{{dt}^2} \right )_{\mathscr R}  & = & \displaystyle -  \mathscr G \frac{M_{\odot}m}{r^2} \vec{u}_r, \\
>& = & - \mu \mathscr G \frac{M_{\odot} + m}{r^2}
>\end{array}
>$$
>Ainsi, pour la particule réduite, tout revient à réaliser l'étude newtonienne habituelle mais en remplaçant la masse du centre attracteur par $M_{\odot} + m$. Notamment, la véritable $3^{ème}$ loi de Kepler s'écrit donc 
>$$
>\frac{T^2}{a^3} = \frac{4 \pi^2}{\mathscr G ( M_{\odot} + m )} \underset{\frac{m}{M_\odot} \ll 1 }{=} \frac{4 \pi^2}{\mathscr G M_{\odot}}\left  ( 1  - \frac{m}{M_\odot} + o \left (  \frac{m}{M_\odot} \right ) \right ).
>$$
>

>[!tip]-
>Toute l'étude précédente s'applique alors :
>- le moment cinétique en $G$ , $\vec{L}_{\mathscr R}(G)$ est conservé;
>- si la force d'interaction dérive d'un potentielle, l'énergie mécanique est conservée;
>- on peut définir une énergie potentielle effective, discuter qualitativement des trajectoires possibles, etc.

>[!quote] Transition. On a parlé de résultantes de forces, on peut aussi s’intéresser aux moments. Les mouvements de rotation donnent un rôle majeur à une autre grandeur mécanique : le moment cinétique.

```{=latex}
\begin{tikzpicture}
\draw[->] (0,0) -- (2,0) node[right] {$x$};
\draw[->] (0,0) -- (0,2) node[above] {$y$};
```

---

# II – Conservation du moment cinétique

## 1) Théorème du moment cinétique

-  Système matériel $\mathscr S$ dans un référentiel galiléen $\mathscr R$. **Théorème du moment cinétique** $(\mathsf{TMC})$ en un point fixe $O$ ([^1] p 227 et [[M2 Dynamique des systèmes matériels fermés#$ bullet$ Théorème du moment cinétique en un point fixe $( mathsf{TMC})$|Théorème du moment cinétique en un point fixe (TMC)]] ):
$$  
\left. \frac{d\vec L_{\mathscr R}(O)}{dt} \right )_{\mathscr R } = \vec{\mathscr M}_{\text ext}(O)  
$$
avec : $\vec L_{\mathscr R}(O) = \sum_i \overrightarrow{OM_i} \wedge m_i \vec v_i$ , ou forme intégrale $\vec L_{\mathscr R}(O) = \iiint_{M \in \mathscr S} dm(M)\,  \overrightarrow{OM} \wedge \vec{v}_{\mathscr R}(M)$. Et $\vec{\mathscr M}_{\text{ext}}(O) = \iiint_{M \in \mathscr S} d\vec{\mathscr M}^{[\vec F^i_{\text{ext}}]}(O;M)$ et $d\vec{\mathscr M}^{[\vec F]}(O;M) = \overrightarrow{OM} \wedge d\vec{F}(M)-$ avec la force $d\vec{F}(M)$ s'exerçant au point $M$ (pour un système de points ([^3] p 127)). $(\mathsf{TMC})$ par rapport à un axe fixe ([^1] p 231).

>[!tip]- Remarque
>Pour un point quelconque on utilise le moment dynamique 
>$$
>\vec{D}(A) = \vec{\mathscr M}_{\text ext}(A)
>$$
>avec 
>$$
>\vec{D}(A) = \left . \frac{d \vec{L}(A)}{dt} \right )_{\mathscr R } + m \, \vec{v}(A) \wedge \vec{v}(G)
>$$
>-  il faut bien comprendre que ce terme vient du fait que **AAA n’est pas fixe**
>- ce n’est pas une formule “fondamentale”, mais une correction cinématique
>
>(cf [[Physique/Mécanique du Solide/M1 Rappels et compléments#$ bullet$ Moment dynamique|  Moment dynamique]]  , [^9] p 194 , [^8] p 120 )

- Conservation : système isolé ($d \vec F_{\text{ext}}(M) = \vec 0 \Rightarrow \vec{\mathscr M}_{\text ext}(O) = \vec 0$ ) ou bien force centrale ($\overrightarrow{OM} \wedge d\vec F_{\text{ext}}(M) = \vec 0 \Rightarrow \vec{\mathscr M}_{\text ext}(O) = \vec 0$) .
$$
\vec L_{\mathscr R}(O) = \overrightarrow{const}.
$$
- Origine profonde : isotropie de l’espace. Pour le faire sentir, si $U$ est indépendant de $\theta$ (en coordonnées cylindriques)
$$
\left ( 
\begin{array}{c}
F_r \\
F_\theta \\
F_z 
\end{array}
\right )_{\mathscr R}
=
\vec F_{\text{ext}}(M) = - \overrightarrow{grad} ( U ( r , z )) = - \left ( 
\begin{array}{c}
\partial_r U(r,z) \\
\frac{1}{r} \partial_\theta U(r,z) = 0\\
\partial_z U(r,z)
\end{array}
\right )_{\mathscr R},
$$
les forces sont forcément suivant  $\vec{e}_r$ ou $\vec{e}_z$ , donc
$$
\vec{\mathscr M}_{\text ext}(O) = \overrightarrow{OM} \wedge \vec F_{\text{ext}}(M) = 
\left ( 
\begin{array}{c}
r \\
0\\
z 
\end{array}
\right )_{\mathscr R}
\wedge 
\left ( 
\begin{array}{c}
\partial_r U(r,z) \\
0 \\
\partial_z U(r,z) 
\end{array}
\right )_{\mathscr R} =
\left ( 
\begin{array}{c}
0 \\
z \partial_r U(r,z) - r \partial_z U(r,z)\\
0 
\end{array}
\right )_{\mathscr R},
$$
Donc 
$$
\vec L_z(0) = \overrightarrow{const}_z \,  \quad \& \quad \vec L_r(0) = \overrightarrow{const}_r,
$$
$\vec L_z(0)$ et $\vec L_r(0)$ seront conservées. Mais Le fait que $\vec L_r(0)$ soit conservé ici est **accidentel lié à ta géométrie** (coordonnées cylindriques mal projetées dans base cartésienne)

👉 Physiquement, la seule vraie symétrie est : rotation autour de $z$
Donc :
$$
\vec L_z(0) \quad \text{est conservée}
$$

👉 **Isotropie de l’espace** : Si le système ne dépend pas de l’angle ⇒ moment cinétique conservé
## 2) Exemple

>[!tip]+ Ecran.
>Vidéo YouTube : https://www.youtube.com/watch?v=2Oc-Ucx_4Ug (2 :23).

- Voir modélisation en [[Physique/Mécanique du Solide/M1 Rappels et compléments#a. Composante utile du moment cinétique d'un solide en rotation autour d'un axe fixe.|a. Composante utile du moment cinétique d'un solide en rotation autour d'un axe fixe. ]] ou dans [^9] p 167
- Conservation de $L_{\Delta , \mathscr S / \mathscr R}(O) = \vec L_{ \mathscr S /  \mathscr R}(O ) \cdot \vec e_z = J_\Delta \Omega_{\mathscr S / \mathscr R}$ (vor [[Physique/Mécanique du Solide/M1 Rappels et compléments#a. Composante utile du moment cinétique d'un solide en rotation autour d'un axe fixe.|a. Composante utile du moment cinétique d'un solide en rotation autour d'un axe fixe. ]] ou dans [^9] p 167 )
-  Rapide calcul d’ordre de grandeur suivant ([^6] p 324) 

>[!tip]- **ODG (ordre de grandeur) : danseuse**
>
>>Hypothèse :
>>
>>- masse $m$
>>- bras étendus → $R \sim 1\,\text{m}$
>>- bras repliés → $r \sim 0.2\,\text{m}$
>
>Moment d’inertie (ODG) :
>$$
>J \sim m R^2
>$$
>Donc :
>$$
>J_1 \sim m R^2, \quad J_2 \sim m r^2
>$$
>Conservation :
>$$
>J_1 \omega_1 = J_2 \omega_2
>$$
>Donc :
>$$
>\frac{\omega_2}{\omega_1} = \frac{J_1}{J_2}= \frac{R^2}{r^2}
>$$
>Numériquement :
>$$
>\frac{\omega_2}{\omega_1} \sim \left(\frac{1}{0.2}\right)^2 = 25
>$$
>👉 **la vitesse peut être multipliée par ~25**  
>(en pratique moins → corps pas ponctuel)

- Deux systèmes emboîtés, vitesse de rotation finale $\omega_f = \frac{J_2}{J_1+L_2} \omega_i$ ([^2] p 309). Ne pas encore parler d’énergie.

>[!tip]- Deux systèmes emboîtés
>
>>Situation
>>
>>- système 1 : moment $J_1$​, vitesse initiale $\omega_i$
>>- système 2 : moment $J_2$​​, initialement au repos
>>- puis couplage (frottement interne) → vitesse finale commune $\omega_f$
>
> Conservation du moment cinétique
> Avant :
> $$
> L_{\text{init}} = J_1 \omega_i
> $$
> Après :
> $$
> L_{\text{final}} = (J_1 + J_2)\, \omega_f
> $$
> Donc :
> $$
> J_1 \omega_0 = (J_1 + J_2)\, \omega_f
> $$
> Donc
> $$
>\omega_f = \frac{I_1}{I_1 + I_2}\, \omega_0.
>$$

>[!quote] Transition. On revient sur le mobile fictif du problème à deux corps : il est soumis à une force centrale, ce qui va nous permettre d’appliquer des résultats obtenus dans cette section.
## 3) Problème à deux corps et force centrale

- Le moment cinétique $\vec L_{\mathscr S / \mathscr R}(G) = \vec{r} \wedge \vec v_{\mathscr S / \mathscr R}(G)$ du mobile fictif est une constante, donc $\vec r$  est orthogonal à un vecteur constant et le mouvement est plan ([^3] p 139) Le plan $( G , \vec r_O , \vec v_0)$ .
- En coordonnées polaires, on a $\vec L_{\mathscr S / \mathscr R}(G) = m r^2 \theta \vec e_z$ , donc $r^2 \theta$ est une constante ([^3] p 132).

>[!quote] Transition. Il reste une grandeur mécanique qui peut grandement simplifier la résolution de certains problèmes : l’énergie. Cependant elle fait aussi apparaître des subtilités...

---
# III – Conservation de l’énergie

## 1) Systèmes conservatifs
-  1) Théorème de l’énergie cinétique
$$  
\Delta \mathcal E_c = W_{ext} + W_{int}  
$$
👉 Attention : forces **internes** apparaissent ([^1] p 298)

- 2) Conservation de l’énergie mécanique pour un système conservatif

Si forces dérivent d’un potentiel :

$$  
\mathcal E_m = \mathcal E_c + \mathcal E_p = \text{cste}  
$$
([^1] p 308)

>[!tip]- Origine fondamentale
>
>👉 **Invariance par translation temporelle**
>
>Le temps est homogène ⇒ énergie conservée
>
>Cependant, on a montré que l’énergie mécanique n’était conservée que pour les systèmes conservatifs... Calcul avec l’énergie des deux systèmes emboîtés de [^2] p 309 : il semblerait que l’énergie mécanique ne soit pas conservée. En réalité, il faut considérer l’énergie totale, qui contient l’énergie interne. C’est de la thermo et on ne développera pas ça lors de la leçon.
>


-  Pour un système à un seul degré de liberté, écrire la conservation de l’énergie mécanique suffit à résoudre entièrement le problème : on peut par exemple résoudre intégralement le pendule simple.

>[!quote] Transition. Retour aux problèmes conservatifs : on peut résoudre le problème à deux corps car la force est conservative.

## 2. Trajectoires dans le problème à deux corps

- Sans le référentiel barycentrique $\mathscr R^\ast$ de centre de masse $G$, on admet que l’énergie s’écrit bien .
$$
\mathcal E_{m; \mathscr S / \mathscr R^\ast } = \frac{1}{2} \mu \left ( \frac{d \vec r}{dt} \right )_{\mathscr R^\ast}^2 + U(\Vert \vec r \Vert )
$$
(détail du calcul [^3] p 139 par sommation des énergies cinétiques individuelles) On a introduit un potentiel $U(r )$, on a ainsi supposé l’interaction conservative (et $U(r )$ uniquement car force centrale).
- Graphe d’énergie potentielle effective, trajectoire circulaire, trajectoires liées et états de diffusion ([^3] p 132).
- Remarquer qu’on n’a rien supposé sur la forme de $U(r )$ ! Les seules hypothèses réalisées sont que l’interaction est centrale et conservative.
- Pour un potentiel newtonien on peut même déterminer l’équation du mouvement grâce à une grandeur conservée supplémentaire (= symétrie dynamique, cf. [^4] et [^8] p 50 ) : le vecteur de Runge-Lenz :
$$
\vec{\mathscr A} = \vec v \wedge \vec{L}_G - k \, \vec e_r 
$$
avec $\vec v = \left . \frac{ d \vec r }{dt} \right )_{\mathscr R^\ast} = r \dot \theta \vec e_\theta$ ,$ \vec r = \overrightarrow{M_1  M_2}$ ,   $\vec{L}_{\mathscr S / \mathscr R^\ast}(G) = m \vec{r} \wedge \vec v  = m \underbrace{r^2 \dot \theta}_{C} \vec{e}_z $ , $\vec e_r = \vec r / \Vert \vec r \Vert $ et $k = \mathscr G m_1 m_2 = \mathscr G \mu ( m_1 + m_2)$ qui vient de $U(r) = - k/r$  et donc $\vec{F} = - k/r^2 \vec e_r$ et $m \left . \frac{ d \vec v }{dt} \right )_{\mathscr R^\ast} = \vec F$.
$$
\left . \frac{ d \vec{\mathscr A}}{dt} \right )_{\mathscr  R^\ast } = \left . \frac{ d \vec v }{dt} \right )_{\mathscr R^\ast}  \wedge \vec L_G - k \, \left . \frac{ d \vec e_r }{dt} \right )_{\mathscr R^\ast} = - \frac{k}{m r^2} \vec e_r \wedge mr^2 \dot \theta \vec e_z - k \dot \theta \vec e_\theta = \vec 0.
$$
$$
\vec{\mathscr A} \cdot \vec e_r = (\vec v \wedge \vec{L}_G)\cdot \vec e_r  - k  = ( \vec e_r \wedge \vec v  ) \cdot \vec{L}_G - k = \frac{m C^2}{r} - k.
$$
En choisissant l'axe ($Ox$) comme étant orienté par $\vec{\mathscr A}$ (possible car $\vec{\mathscr A}$  constant ) et en notant $\theta$ l'angle entre $\vec e_r$ et $\vec e_x$, on a $\vec{\mathscr A} \cdot \vec e_r = \mathscr A \cos \theta$ avec $\mathscr A = \Vert \vec{\mathscr A} \Vert$. Il vient que 
$$
\mathscr A \cos \theta = \frac{m C^2}r - k\quad \text{puis} \quad r = \frac{p}{1 + e \cos \theta},
$$
avec $ p = \frac{m C^2}k$ et $e = \frac{\mathscr A}k$.

>[!cite] Transition.  Jusqu’à présent, nous avons étudié les lois de conservation pour des systèmes discrets ou des solides indéformables.  
> Cependant, ces principes ne dépendent pas de la nature discrète du système : ils restent valables pour des milieux continus, à condition d’en adapter la formulation.  
> Nous allons maintenant illustrer cette généralisation dans le cadre de la mécanique des fluides, où les lois de conservation prennent une forme locale et permettent de décrire des écoulements.

# IV – Lois de conservation en mécanique des fluides
## 1- Passage au milieu continu
- densité $\rho(x,t)$
- champ de vitesse $\vec v(x,t)$
- dérivée matérielle :
$$
\frac{D}{Dt} = \frac{\partial}{\partial t} + (\vec v \cdot \nabla)
$$
👉 lien direct avec la partie I (quantité de mouvement)

## 2- Conservation de la masse (équation de continuité)
$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec v) = 0
$$
👉 analogue de conservation de $\vec P$
## 3- Conservation de l’énergie → théorème de Bernoulli

### $\bullet$ Équation d’ Euler

([^9] p 450 .)
Considérons une particule de *fluide*, système fermé occupant à l’instant $t$ un
volume élementaire $d\tau$ au voisinage d’un point $M$. Sa masse $dm= \rho d\tau$ est constante.
Soit $d\vec F$ la résultante des forces exercées par le reste du fluide. En supposant que
le référentiel d’étude est galiliéen, la forme locale du Principe Fondamentale d la
Dynamique s’écrit avec l’équation de Navier-Stokes
$$
\rho  \, \vec a = \rho \frac{D \vec v}{Dt}  =  \rho \left (  \frac{\partial \vec v}{\partial t} + (\vec v  \cdot \overrightarrow{grad}) \vec v  \right ) = - \overrightarrow{grad}(p) + \frac {d \vec F}{d \tau } + \overrightarrow{div}[\sigma']
$$
On néglige la viscosité donc $\xcancel{\overrightarrow{div}[\sigma']}$ Nous obtenons une équation locale, valable en tout point du fluide, appelée *équation d’ Euler* :
$$
\rho \left (  \frac{\partial \vec v}{\partial t} + (\vec v  \cdot \overrightarrow{grad}) \vec v  \right ) = - \overrightarrow{grad}(p) + \frac {d \vec F}{d \tau }
$$
- On peut facilement montrer que l’équation d’ Euler est en accord avec sur le fait que l’écoulement parfait sont réversible. En eﬀet la transformation $
\left \{ 
\begin{array}{rcl}
\vec v (x,y,z) & \rightarrow &- \vec v (x,y,z)\\
t & \rightarrow & -t 
\end{array}
\right .
$laisse cette équation invariante. La source d’irréversibilité c’est la dissipation d’énergie par la viscosité, source qui n’existe donc par pour ces fuides idéalisée.
- L’*équation d’ Euler* est non-linéaire à cause de la contribution de l’accélération convective $(\vec v \cdot \overrightarrow{grad} ) \vec v$; cette non-linéarité explique la grande richesse de la dynamique des fluides, mais constitue souvent un obstacle dans les calcule qui devient compliqué voir impossible. On est ainssi souvant amené, même pour chercher une solution numérique avec un ordinateur, à repérer a priori les termes dominants de l’équation d’ Euler et à négliger d’autres.(cf [^9] fin p 450 ) et (cf [^12] fin p 356 )
- 
$$
\frac{D \vec v}{Dt}  \doteq  {\color{blue}\underbrace{\frac{ \partial \vec v}{\partial t}}_{\begin{array}{c}\text{Accélération local}\\\text{(carractère non permanent)}\end{array}}} + {\color{red} \underbrace{(\vec v \cdot \vec \nabla) \vec v }_{\begin{array}{c}\text{Accélération convective}\\\text{(carractère non uniforme)}\end{array}}}
$$
On peut utilisé $\vec \nabla (\vec A \cdot \vec B) = (\vec A \cdot \vec \nabla  )(\vec B) + ( \vec B \cdot \vec \nabla  )(\vec A)−(\vec \nabla  \wedge \vec A) ∧ B− (\vec \nabla  \wedge \vec B) ∧ A$ avec $\vec A=  \vec B= \vec v$, et en utilisant $\vec \nabla ( \vec A^2 ) = 2 \vec A \cdot \vec \nabla \cdot \vec A$  l’accélération convectif devient $(\vec v \cdot \vec \nabla  ) \vec v= \vec \nabla  ( \vec v^2/2) + ( \vec \nabla \wedge \vec v )  \wedge  \vec v)$ soit :
$$
\frac{D \vec v}{Dt}  \doteq  {\color{blue}\underbrace{\frac{ \partial \vec v}{\partial t}}_{\begin{array}{c}\text{Accélération local}\\\text{(carractère non permanent)}\end{array}}} 
+ 
{\color{red} 

{\color{brown} 
\underbrace{ \vec{\nabla} \left ( \frac{ v^2}2\right)}_{
\begin{array}{c}\text{variation de}\\\Vert \vec v \Vert \end{array}
}
}

+

{\color{pink} 
\underbrace{ ( \vec{\nabla} \wedge \vec v )  \wedge \vec v }_{
\begin{array}{c}\text{variation de}\\\text{la direction de } \vec v  \end{array}
}
}

}
$$
et l’équation d’ Euler devient
$$
\rho \left (  \frac{\partial \vec v}{\partial t} +  \overrightarrow{grad} \left (  \frac{v^2}2 \right) +  \overrightarrow{rot}(\vec v) \wedge \vec v  \right ) = - \overrightarrow{grad}(p) + \frac {d \vec F}{d \tau }.
$$
Pour déterminer la dynamique (resp complètement l’état) du fluide, on doit connaître les champs eulériens de vitesse $\{\vec v \equiv (v_x,v_y,v_z)\}$, de pression $p$ ,et de masse volumique $\rho$ (resp et de température $T$ ), soit 5 champs scalaires ( resp soit 6 champs scalaires). L’équation d’Euler fournit 3 équations et l’équation locale de conservation de la masse $\partial_t\rho + div (\rho \vec{v}) = 0$ en donne une. 

On doit encore utiliser 2 équations supplémentaires : l’équation d’état du fluide et une relation traduisant la nature des transformations thermodynamiques subies par la particules de fluide.(cf propagation des ondes acoustiques)(cf [^9] fin page 450 ) et (cf [^12] fin page 356). 

Dans le cas d’écoulement incompressibles et homogènes on rajoute respectivement les conditions $div (\vec v) = 0$ et $\rho (M,t) = Cte$, à des condition aux limites prés on a à les 5 champs scalairs ; (cf [^9] fin page 450 )

- Si le fuide est au repos dans le référentiel d’étude $\mathscr R$, l’équation d’Euler se réduit à l’équation locale de la statique des fuides, vue en première année :
$$
- \overrightarrow{grad}(p) + \frac{d \vec F}{d \tau } = 0
$$
([^12]fin page 356 )

### $\bullet$ Théorème de Bernoulli

Un fluide parfait n’ayant par définition pas de viscosité, in ne peut pas dissiper d’énergie. On peut donc à partir de l’équation d’Euler trouver une équation de conservation de l’énergie, appellée équation de Bernoulli.

#### Énoncés
Il y en a plusieurs, mais qu’on en verra deux seulement. Voyons d’abord la version classique de cette équation.

##### Cas d’un écoulement HPPI (Homogène, Parfait, Permanent et In-compressible)

On suppose l’ensemble des conditions HPPI (Homogène, Parfait, Permanent et Incompressible) :

1. un fuide de masse volumique constante ($\rho = Cste$)
2. un écoulement stationnaire ($\partial / \partial_t = 0$)
3. les forces volumiques exterieurs dérient d’un potentiel  $\frac{d \vec F}{d \tau } = - \rho \, \overrightarrow{grad}(\Phi_{ext})$ ;( : $g=− \vec{grad} (\Phi_g))$.Dans le cas de la force de la gravité $\Phi_g = gz$ avec l’axe $z$ dirigé vers le haut.
L’équation d’ Euler devient :
$$
\rho \Bigg (  \xcancel{\frac{\partial \vec v}{\partial t}} +  \overbrace{\overrightarrow{grad} \left (  \frac{v^2}2 \right) +  \overrightarrow{rot}(\vec v) \wedge \vec v}^{\displaystyle  (\vec v  \cdot \overrightarrow{grad}) \vec v  }  \Bigg ) = - \overrightarrow{grad}\left (p + \rho \,\Phi_{\text{ext}} \right ).
$$
soit l’équation d’ Euler devient :
$$
\overrightarrow{grad}\Bigg ( \underbrace{\frac{p}\rho + \Phi_{\text{ext}} + \frac{v^2}2}_{\displaystyle C} \Bigg )
= 
\vec v \wedge \overrightarrow{rot}(\vec v)
$$
Nous allons montrer que $C= \frac{p}\rho+ \Phi_{\text{ext}} + \frac{v^2}2$, appelée parfois la "charge", reste constante sur une line de courant. Par définition du gradient :
$$
dC= \overrightarrow{grad}(C) \cdot \vec{dl} = (\vec v ∧ \overrightarrow{rot}(\vec v))· \vec{dl}
$$
Donc si dl est colinéaire à $\vec v$, ce qui est le cas le long d’une ligne de courant, on trouve que $dC = 0$ le long d’une line de courant ( " il n’y a pas de perte de charge le long d’une de courant"). Toutefois cette constante peut être diﬀérente pour chaque ligne de courant.

Sur une ligne de courant l’équation de Bernoulli s’écrit alors :
$$
\frac{p}\rho + \Phi_{\text{ext}} + \frac{v^2}2 = \text{Cst}
$$
Le même raisonnement permet de montrer que $C$ est aussi constante sur les ligne de *vorticité* ( la *vorticité* est $\vec \omega = \vec{rot}(\vec{v})$).

Si de plus l’écoulement est *potentiel* ($\vec{v} = \vec{grad} \Phi$) ie écoulement est *irrotationnel* ($\vec{rot}(\vec{v}) = \vec{0}$) dans un certain domaine de l’espace, alors la constante $C$ est la même sur toutes les lignes de courant traversant dans ce domaine.

-  $p$ : *pression statique* ( ou *locale* )
- $\Phi_{\text{ext}} = \rho gh$ : *pression hydrostatique*
- $\rho \frac{v^2}2$ : *pression dynamique*
- $p + \rho \,\Phi_{\text{ext}} +\rho \, \frac{v^2}2 $  : *pression totale* ou *presion de stagnation* ou encore *pression d’arrêt*. En eﬀet sur une ligne de courant, cette *pression totale* est aussi la pression que l’on mesure en un point où la vitesse est nulle.

Lien avec la conservation de l’énergie, mais on n’aura pas le temps de faire la petite démo dessus.(cf [^13] chap 5 page (201-202) et (198-199) )

Lien avec la conservation de l’énergie, mais on n’aura pas le temps de faire la petite démo dessus.{\color{green} (cf Hydrodynamique Physique 3em edition chap 5 page (201-202) et (198-199) )}


$$ 
e_c = \frac{ d E_c }{ d V } = \frac {\mu v^2}2
$$
L'Équation d'Euler

$$ 
\rho  (  \partial_t v^{i} + v^{j} \partial_j v^{i} ) = -\partial_i p + \partial_j \sigma'^{j{i}}+ \mu f^{i} 
$$

$$
\begin{array}{rcl}
\displaystyle \partial_j ( \alpha A^j ) & = & \displaystyle A^j \partial_j ( \alpha ) +  \alpha \partial_j ( A^j) \\

\displaystyle div ( \alpha \vec{A} ) & = & \displaystyle \vec{A} \cdot \overrightarrow{grad}(\alpha) + \alpha \, div(\vec{A}) \\

\displaystyle \partial_j\left [   v^{j} \left ( \frac{ \rho v^2}2 + p \right ) \right ] & =& \displaystyle \left ( \frac{ \rho v^2}2 + p \right ) \partial_j v^j + (-v^{j}  \partial_j )\left ( \frac{ \rho v^2}2 + p \right )\\

\displaystyle div \left [ \vec{v} \left ( \frac{ \mu v^2}2 + p\right ) \right ] & = & \displaystyle \left ( \frac{ \mu v^2}2 + p\right )  div(\vec{v}) +  ( \vec{v} \cdot \overrightarrow{grad} ) \left ( \frac{ \rho v^2}2 + p \right )                
\end{array}
$$
Pour un système im-compréssible $div (\vec v) = 0$. 
$$
div \left [ \vec{v} \left ( \frac{ \mu v^2}2 + p\right ) \right ]  =    ( \vec{v} \cdot \overrightarrow{grad} ) \left ( \frac{ \rho v^2}2 + p \right ) 
$$
Soit 
$$
\begin{array}{rcl}

\displaystyle \frac{\partial}{\partial t}\left ( \frac{ \rho v^2}2 \right ) & = &  \displaystyle\rho v_{i} \partial_t v^{i}\\

& = & \displaystyle - \rho  v_{i} v^{j} \partial_j v^{i} - v_{i} \partial_i p + v_{i} \partial_j \sigma'^{j{i}} + \rho v_{i}f^{i}\\

& = & \displaystyle- v^{j}  \partial_j \left ( \frac{ \rho v^2}2 + p \right ) + \partial_j (v_{i} \sigma'^{j{i}}) -   \sigma'^{j{i}}\partial_j v_{i}+ \rho v_{i}f^{i}\\

& = &  \displaystyle ( - \vec{v} \cdot \overrightarrow{grad}) \left ( \frac{ \rho v^2}2 + p \right ) + div ( [ \vec{\vec{\sigma'}}] \cdot \vec{v} ) - \sigma'^{j{i}}\partial_j v_{i}+ \rho \vec{v} \cdot \vec{f}  \\

& = & \displaystyle - div \left [ \vec{v} \left ( \frac{ \rho v^2}2 + p\right )  - ( [ \vec{\vec{\sigma'}}] \cdot \vec{v}  ) \right ] + \rho \vec{v} \cdot \vec{f} -  \sigma'^{j{i}}\partial_j v_{i}

\end{array}
$$
   Pour un fuide parfait en écoulement stationnaire, on peut négliger les pertes d'énergie par viscosité. 

$$ 
\xcancel{\frac{\partial}{\partial t}\left ( \frac{ \mu v^2}2 \right )  } =  -div \left [ \vec{v} \left ( \frac{ \rho v^2}2 + p\right )  - \xcancel{( [ \vec{\vec{\sigma'}}] \cdot \vec{v}  ) }\right ] + \rho \vec{v} \cdot \vec{f} - \xcancel{\sigma'^{j{i}}\partial_j v_{i}} \overset{ \vec{f} = -\overrightarrow{grad}(\Phi_{ext})}{=}  - div \left [ \vec{v} \left ( \frac{ \rho v^2}2 + p\right )  \right ] - \rho ( \vec{v} \cdot \overrightarrow{grad} ) (\Phi_{ext})
$$

 En utilisant la relation vectorielle générale : $div ( \alpha \vec{A} )  =  \vec{A} \cdot \overrightarrow{grad}(\alpha) + \alpha \, div \vec{A}$ et la relation d'incompressibilité $div(\vec{v}) = 0$ et la propriétés $\rho = Cte$ il vient que 

$$ 
(\vec{v} \cdot \overrightarrow{grad} ) \left ( \frac{ \rho v^2 } { 2} + p +  \rho \Phi_{ext} \right ) = 0 
$$

  
##### Généralisation aux écoulements parfaits, instationnaires, irrotationnels, incompressibles et homogènes

En l'absence de l'hypothèse "stationnaire" , le terme $\rho ( \partial \vec{v} / \partial t )$ subsuste dans l'* équation}*d'$\mathsf{Euler}$ qui s'écrit : 
$$ 
\frac{\partial \vec{v}}{\partial t } + \overrightarrow{grad}\left ( \frac{p}{\rho} + \Phi_{ext} + \frac{1}2 v^2 \right ) = \rho \vec{v} \wedge \vec{rot}(\vec{v}) 
$$
Si de plus l'*écoulement* est *potentiel* ($\vec{v} \cdot \vec{grad}(\Phi)$) ie  *écoulement* est *irrotationnel* ( $\vec{rot}(\vec{v}) = \vec{0}$), alors $\frac{\partial \vec{v}}{\partial t } = \frac{ \partial \vec{grad}(\Phi) } { \partial t} \overset{Schwart}{=} \vec{grad} \left(\frac{ \partial \Phi } {\partial t }\right)$. Il vient que :

$$
\vec{grad} \left ( \frac{ \partial \Phi }{\partial t } + \frac{p}{\rho} + \Phi_{ext} + \frac{1}2 v^2 \right )
$$
ou
 
Soit 

$$
C(t) =   \frac{ \partial \Phi }{\partial t } + \frac{p}{\rho} + \Phi_{ext} + \frac{1}2 v^2
$$

ou 

$$
C(t) =   \frac{ \partial \Phi }{\partial t } + \frac{p}{\rho} + gz + \frac{1}{2} v^2
$$

La charge $C(t)$ ne dépent pas de la position mais uniquement du temps. À chaque instant $C = Cste$ dans toute la zone irrotationnelle.(On peut faire disparaître cette constante avec la potentiel $\Phi' = \Phi = \int_0^t C(t)\,d t $. $\vec{grad}(\Phi') = \vec{grad}( \Phi) $ mais garde aux changement de référentiel) 

{\color{green}(cf. Cour de M.Rabaud "Modèle de l'écoulement parfait d'un fluide" page 552 ) et (cf [^12] page 455-456 )}

##### Quelques applications des théorèmes de Bernoulli

(cf [^9]p 456-460 )}

On considère un écoulement HPPI (Homogène, Parfait, Permanent et Incompressible) dans un référentiel d'étude galiléen.

- Le phénomène de Venturi

 $\bullet$ **Observations**

D'une façon générale, un resseerement des lignes de champ traduit une augmentation de la vitesse dans un écoulement incompressible et conduit donc d'après l'*équation* de $\mathsf{Bernoulli}$ à une diminition de la pression : c'est le phénomène de $\mathsf{Venturi}$. Par exemple dans une conduite horizotale de section $S_1$ possédant un étranglement de section $S_2 \ll S_1$, on observe une dépression au voisinage de l'étranglement. 

$\bullet$ **Modèle quantitatif**

Pour interprétrer quantitativement cette observation, prenons un modèle d'écoulement unidimensinnel dans les section $S_1$ et $S_2$, avec des vitesses respectives $v_1$ et $v_2$ et des oressions respectices $p_1$ et $p_2$.

La conservation du débit volumique pour l'écoulement supposé incompressible s'écrit : 
$$ 
D_{V_1} = D_{V_1} \quad \text{soit} \quad v_1 S_1 = v_2 S_2
$$

Avec $S_2 \ll S_1 $, el en résulte que $v_2 \gg v_1$ : contrairement à l'intuition, on observe une augmentation de la vitesse au niveau de l'étranglement. D'autre part, l'axe de symétrie de la conduite constitue une ligne de champ particulière. Appliquons le *théorème* de $\mathsf{Bernoulli}$ entre $A_1$ et $A_2$ le long de cette ligne de champ : 
$$ 
\frac { p_2 } \rho + g z_{A_2} + \frac{ v_2^2} 2 = \frac { p_1 } \rho + g z_{A_1} + \frac{ v_1^2} 2  
$$

   La conduite est supposé horizontale, donc $z_{A_2} = z_{A_1}$($z_{A_2} = z_{A_1}$ assez faible pour négliger $g(z_{A_2} = z_{A_1})$). En éliminant la vitesse $v_2$ avec la conservation du débit volumique , la différence despression est 
   $$ 
 p_2 - p_1 = \rho \frac{ v_1^2}2 \left ( 1 - \left ( \frac{ S_1}{ S_2} \right )^2 \right )
 $$

Avec $S_2 \ll S_1$ nous avons bien $p_2 < p_1$, c'est-à-dire une dépression au niveau de l'étranglement.

Pour un écoulement d'eau avec 
$$
\left \{ 
\begin{array}{rcl} 
\rho & = & 10^3 ~\text{kg.m}^{-3} \\ 
p_1 & = & 1 ~\text{bar} \\ 
S_1 & = & 1 ~\text{m} \\ 
S_2 & = & 0,01 ~\text{m} 
\end{array} 
\right .
$$

calculons la vitesse $v_1$ pour atteindre une pression de $p_2 = 2~500~\text{Pa}$ au niveau de l'étranglement : 

$$
v_1 = \sqrt{ \frac{ 2 ( p_2 - p_1 ) }{ \displaystyle \rho \left ( 1 - \left ( \frac{ S_1}{ S_2} \right )^2 \right )}} \overset{AN}{=} 0,14 ~ \text{m.s}^{-1}
$$

Cette vitesse est tout à fait accessible. Pour des vitesse supérieure, la formule pourrait donner une pression négative au niveau de l'étranglement, ce qui est absurde: en pratique l'eau but ; il apparaît des bulles de vapeur d'eau ; l'écoulemnt devient diphasique, donc compressible, et de relève plus de la description adoptée.

$\bullet$ **Limites du modèles de l'écoulement parfait**

Par symétrie pon devrait trouver par le *théorème* de  $\mathsf{Bernoulli}$ entre les points $A_1$ et $A_3$ : $p_3 = p_1$. ce resultat n'est pas conforrme à la réalité : il y a une légère baise de la pression. Le **théorème** de  $\mathsf{Bernoulli}$  n'est pas valable entre $A_1$ et $A_3$ : il y à des effet de viscosité dans l'étranglement.(* écoulement de $\mathsf{Poiseulle}$*)

  
$\bullet$ **Applications**

Le *débitmètre* de $\mathsf{Venturi}$ utilise le *phénomène* de $\mathsf{Venturi}$. La géomètrie est la même que pour la figure precédante : avec une baromètre on a $p_2 - p_1$ et connaissant la géomètrie du débimètre on a la vitesse $v_1$ et le débit volumique $D_V = v_1 S_1$.\\

La *trompe à eau* pour "faire le vide" {\color{green}(cf [^9] page 458 )}

  

- {Tube de Pitot}

$\bullet$ **Description et modèle**

Le tube de $\mathsf{Pitot}$ est utilisé en aérodynamique pour mesurer la vitesse d'un écoulement d'air uniforme et stationnaire. Il est constitué d'un tube métalique de section $s \approx 5 ~\text{mm}^2$ dont l' extrémité arrondit est percée d'un trou très fin de centre $A$ et de rayon $r \approx 0,5 ~\text{mm}$. Le tube est placé longitudinalement dans un écoulement d'air de section $S \gg s $; loins du tube, l'écoulement est unidimentionnel avec une vitesse $\vec{V}_\infty = V_\infty \vec{e}_x$ et une pression $p_\infty$ uniformes. Le tube comporte une prise de pression la lathérale $p_B$ et une prise de pression axiale $p_A$ entre lesquelles un baromètre differentiel mesure la différence de pression $p_A - p_B$.

$\bullet$ **Mise en équation**\\

L'équilibre du manomètre qui mesure $p_A - p_B$ assure que l'air situé à l'intérieur du tube de {\sc Pitot} est au repos et l'incomprressibilité assure que l'air extérieur ne pénètre pas dans le tube : $\vec{v}_{int} = \vec{0}$. La condition aux limite $v_{int}(A) \cdot \vec{n} = v_{ext}(A) \cdot \vec{n}$ au point $A$, avec $\vec{v}_{ext}(A)$ parallèle à $\vec{n}$ impose donc que $\vec{v}_{ext}(A) = \vec{0}$ : $A$ est n point d'arrêt.\\

Le *théorème* de $\mathsf{Bernoulli}$ appliqué sur une ligne de courant entre les points $A_\infty$ et $A$ s'écrit : 
$$ 
\frac{ p_{A_\infty}}{\rho} + g z_{A_\infty }+ \frac{ v_{A_\infty}^2}{ 2} = \frac{ p_{A}}{\rho} + g z_{A }+ \frac{ v_{A}^2}{ 2}
$$
En négligeant la dénivellation entre ces points et en remplaçant ce qui est connu ($ v_{A_\infty} = v_\infty$, $p_{A_\infty} = p_\infty$, $v_A = 0$ , $ g (z_{A_\infty }- z_{A}) \approx 0 $)   il vient : 
$$ 
p_A = p_\infty + \rho \frac{ v_\infty^2}2 
$$
On dit que la prise de pression axiale est une prise de {\em pression dynamique} car la pression $p_A$ qu'elle mesure dépend de la pression et de l'écoulement loin du tube de $\mathsf{Pitot}$.

Au point $B$, la vitesse $v_B$ est tangentielle au tube de $\mathsf{Pitot}$: dans le modèle de l'écoulement parfait, la condition au limites qui n eporte que sur les composantes normales n'impose donc rien ici. Pour déterminer $v_B$, supposons que l'écoulement est unidimentionnel dans la section $(S_B)$ de l'écoulement contenant $B$ ; la conservation du débit volumique entre $(S_B)$ à l'infini s'écrit :

$$ 
S_B v_B = S_\infty v_\infty \quad \text{soit} \quad v_B \frac{ S_\infty}{S_B} v_\infty \approx v_\infty \quad \text{car} \quad S_B = S_\infty - s \approx S_\infty 
$$
Le *théorème* de $\mathsf{Bernoulli}$ appliqué sur une ligne de courant entre les points $B_\infty$ et $B$ s'écrit : 

$$ 
\frac{ p_{B_\infty}}{\rho} + g z_{B_\infty }+ \frac{ v_{B_\infty}^2}{ 2} = \frac{ p_{B}}{\rho} + g z_{B }+ \frac{ v_{B}^2}{ 2}
$$
En négligeant la dénivellation entre ces points et en remplaçant ce qui est connu\footnote{$ v_{B_\infty} = v_\infty$, $p_{B_\infty} = p_\infty$, $v_B = v_\infty$ , $ g (z_{B_\infty }- z_{B}) \approx 0 $}   il vient : 
$$ 
p_B = p_\infty + \rho \frac{ v_\infty^2}2 - \rho \frac{ v_\infty^2}2 = p_\infty  
$$
On dit que la prise de pression laterale est une prise de pressuin *statique* car la pression $p_B$ qu'elle mesure dépend de la pression loin du tube de $\mathsf{Pitot}$ mais ne dépend pas de la vitesse loin du tube.

En rassemblant les expressions de $p_A$ et $p_B$, nous obtenons : 
$$ 
p_A - p_B = \rho \frac{ v_\infty^2} 2 
$$
Connaissant la masse volumique $\mu$ de l'air, la mesure de $p_A - p_B$ donne donc accès à la vitesse $v_\infty$. Numériquement dans l'air, avec une soufflerie où $v_\infty = 40 ~ \text{m.s}^{-1}$ on obtient $p_A - p_B \approx 10^3 ~\text{Pa} = 0,01 ~\text{bar}$ ce qui est aisé à mesurer.

  


# Conclusion

## 1– Synthèse : puissance des lois de conservation

|Symétrie|Quantité conservée|
|---|---|
|Translation espace|Quantité de mouvement|
|Rotation|Moment cinétique|
|Translation temps|Énergie|

👉 Structure universelle de la physique

## 2– Ouverture : théorème de Noether

On a essayé de faire sentir le lien profond entre grandeurs mécaniques conservées et propriétés d’invariance. De manière fondamentale en physique, les symétries (continues) sont associées à des quantités conservées, c’est le théorème de Noether.

## Énoncé (version simple)

Toute symétrie continue d’un système ⇒ quantité conservée

## Lecture physique

- espace homogène ⇒ $\vec P$
- espace isotrope ⇒ $\vec L$
- temps homogène ⇒ $E$

## Message final (très important à l’oral)

> Les lois de conservation ne sont pas seulement des outils de calcul :  
> elles révèlent la structure profonde des lois physiques.

## Conclusion

Les lois de conservation permettent :

- simplification drastique des problèmes
    
- compréhension qualitative sans résolution
    
- lien profond entre mathématiques et physique
    

👉 Exemple ultime : problème de Kepler entièrement contrôlé par ces invariants

---

# ⚠️ Questions classiques du jury

- Différence système isolé / pseudo-isolé
    
- Validité du référentiel barycentrique
    
- Pourquoi une force centrale conserve $\vec L$ ?
    
- Différence énergie mécanique / totale
    
- Peut-on avoir conservation de $\vec P$ sans homogénéité ?
    

---

# 💡 Bonus différenciant

- Mention explicite de Noether
    
- Lecture hamiltonienne (si question)
    
- Insister sur "sans résoudre les équations"
    
- Faire un lien avec relativité ou collisions


>[!tip]+ Remarque
>- Lecture instructive pour le "background" (niveau L3) de la leçon : [^5] § 3 - 9. 
>- Homogène ⇒ isotrope ? Pas clair. En effet si on a juste un potentiel $U$ qui ne dépend ni de $x$, ni de $y$, ni de $z$, beh c’est isotrope du coup. C’est faux dans le cas général, où il y a plusieurs grandeurs selon la direction où l’on regarde (par exemple la biréfringence). 
>- Trouver une démonstration/présentation la plus simple possible, orientée L3, du théorème de Noether.

