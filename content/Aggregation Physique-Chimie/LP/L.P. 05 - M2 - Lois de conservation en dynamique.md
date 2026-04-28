---
title: L.P. 05 - M2 - Lois de conservation en dynamique
tags:
  - Agrégation
  - Physique
  - Oral
---
---

- **Niveau**  : Licence 
- **Prérequis** : Mécanique du point et du solide, référentiel barycentrique

---

[^1]: Physique Tout-en-un MP · MP* (ancien programme), Dunod. 
[^2]: Physique Spé. MP*, MP et PT*, PT, Gié, Sarmant, Olivier, More, Tec & Doc, 2000. 
[^3]: Mécanique 1, Jean-Pierre Faroux, Jacques Renault, Dunod, 1996. 
[^4]: Comparaison entre le mouvement de Kepler et le mouvement elliptique harmonique, Jean Sivardière, BUP n°751. 
[^5]: Mécanique, Landau & Lifchitz. 
[^6]: Mécanique : fondements et applications (7e édition), J-Ph Pérez, Dunod (2014). 
[^7]: Tout-en-un MPSI/PCSI (ancien programme, 3e édition), Dunod.
[^8]: Physique pour l'agrégation Jules Fillette - Julien Froustey - Hugo Roussille

---

 #### 🎯 Fil directeur**

> **Symétries → lois de conservation → réduction drastique des équations du mouvement**

Les lois de conservation ne sont pas des « accidents » : elles proviennent de propriétés fondamentales de l’espace et du temps (théorème de Noether).

---
#### Plan (annoncé à l’oral)

I. Quantité de mouvement (translation spatiale)  
II. Moment cinétique (rotation)  
III. Énergie (translation temporelle)  
IV. Application structurante : problème à deux corps  
V. Ouverture : Noether et portée générale

---
#### Introduction 

- En mécanique, plusieurs théorèmes fondamentaux établissent un lien direct entre les variations temporelles de certaines grandeurs physiques et des « sources » qui les produisent. Par exemple, le **Principe Fondamental de la Dynamique** $(\mathsf{PFD})$ (**théorème de la résultante cinétique** $(\mathsf{TRC})$) relie la variation de la quantité de mouvement aux forces appliquées, tandis que le **Théorème du Moment Cinétique** $(\mathsf{TMC})$ relie la variation du moment cinétique aux moments des forces.

- Ces formulations ont une conséquence immédiate et profonde : en l’absence de telles « sources » — c’est-à-dire lorsque les forces ou les moments de forces s’annulent — les grandeurs associées sont **conservées**. On obtient ainsi des lois de conservation, qui jouent un rôle central en physique.

- Ces lois sont d’une importance capitale, car elles permettent souvent de simplifier considérablement l’analyse de systèmes complexes. En particulier, elles offrent des outils puissants pour résoudre des problèmes difficiles, comme celui du **système à deux corps**, que nous étudierons tout au long de cette leçon afin d’illustrer concrètement leur efficacité et leur portée.

---

# I – Conservation de la quantité de mouvement

## 1) Théorème fondamental (Loi de conservation)

- Système matériel $\mathscr S$ dans un référentiel galiléen $\mathscr R$. La **Théorème de la résultante cinétique** dans le cas d’un système isolé (ou 👉  pseudo-isolé : résultante des forces nulle $\overrightarrow{R}_{ext} = 0$) :

$$  
\frac{d\overrightarrow P}{dt} = \overrightarrow R_{ext} = 0  
$$

avec  $\overrightarrow P = \sum_i m_i \overrightarrow v_i$ , ou $\overrightarrow P = \iiint_{ M \in \mathscr S }  \overrightarrow{sv} (M) \underbrace{\mu (M) d\tau }_{d m }$. Alors $\overrightarrow P = \overrightarrow{\text{cste}}$ : il s’agit d’une **intégrale première du mouvement**. [^1]

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

-  Système matériel $\mathscr S$ dans un référentiel galiléen $\mathscr R$. **Théorème du moment cinétique** $(\mathsf{TMC})$ en un point fixe :
$$  
\left. \frac{d\vec L_{\mathscr R}(O)}{dt} \right )_{\mathscr R } = \vec{\mathscr M}_{\text ext}(O)  
$$

avec : $\vec L_{\mathscr R}(O) = \sum_i \overrightarrow{OM_i} \wedge m_i \vec v_i$ , ou forme intégrale $\vec L_{\mathscr R}(O) = \iiint_{M \in \mathscr S} dm(M)\,  \overrightarrow{OM} \wedge \vec{v}_{\mathscr R}(M)$. Et $\vec{\mathscr M}_{\text{ext}}(O) = \sum_i \vec{\mathscr M}^{[\vec F^i_{\text{ext}}]}(O)$ et $\vec{\mathscr M}^{[\vec F]}(O) = \overrightarrow{OM} \wedge \vec{F}$ avec la force $\vec{F}$ s'exerçant au point $M$.


---

## 2) Cas de conservation

- Système isolé
    
- Force centrale
    

$$  
\vec F \parallel \vec r \Rightarrow \vec M = 0  
$$

👉 Donc :

$$  
\vec L = \text{cste}  
$$

---

## 3) Interprétation

👉 **Isotropie de l’espace**

Si le système ne dépend pas de l’angle ⇒ moment cinétique conservé

---

## 4) Conséquences majeures

- Mouvement plan
    
- Loi des aires :
    

$$  
r^2 \dot\theta = \text{cste}  
$$

👉 Kepler 2 directement

---

## 5) Exemple physique

Patineur / disque :

$$  
L = I \omega = \text{cste}  
$$

👉 variation de $\omega$ sans force externe

---

# III – Conservation de l’énergie

## 1) Théorème de l’énergie cinétique

$$  
\Delta E_c = W_{ext} + W_{int}  
$$

👉 Attention : forces internes apparaissent

---

## 2) Systèmes conservatifs

Si forces dérivent d’un potentiel :

$$  
E_m = E_c + E_p = \text{cste}  
$$

---

## 3) Origine fondamentale

👉 **Invariance par translation temporelle**

Le temps est homogène ⇒ énergie conservée

---

## 4) Subtilités importantes (oral++)

- Énergie mécanique pas toujours conservée
    
- Dissipation ⇒ énergie interne
    
- Vision correcte : **énergie totale conservée**
    

---

## 5) Puissance en 1D

$$  
\frac{1}{2} m \dot x^2 + V(x) = E  
$$

👉 résolution complète sans équation différentielle

---

# IV – Application : problème à deux corps

## 1) Réduction du problème

Deux corps $m_1, m_2$ ⇒ masse réduite :

$$  
\mu = \frac{m_1 m_2}{m_1 + m_2}  
$$

Centre de masse découplé

---

## 2) Quantité de mouvement

$$  
\vec P = \text{cste} \Rightarrow \vec V_G = \text{cste}  
$$

👉 Travail dans le référentiel barycentrique

---

## 3) Moment cinétique

Force centrale ⇒

$$  
\vec L = \text{cste}  
$$

👉 mouvement plan + loi des aires

---

## 4) Énergie

$$  
E = \frac{1}{2} \mu \dot r^2 + \frac{L^2}{2\mu r^2} + U(r)  
$$

👉 potentiel effectif :

$$  
V_{eff}(r) = \frac{L^2}{2\mu r^2} + U(r)  
$$

---

## 5) Lecture qualitative

- Points de retournement
    
- États liés vs diffusion
    
- Orbites circulaires (minimum)
    

👉 **Sans résoudre les équations !**

---

## 6) Cas newtonien (bonus top niveau)

$$  
U(r) = - \frac{GM\mu}{r}  
$$

👉 invariant supplémentaire : Runge–Lenz

⇒ trajectoires coniques

---

# V – Synthèse : puissance des lois de conservation

|Symétrie|Quantité conservée|
|---|---|
|Translation espace|Quantité de mouvement|
|Rotation|Moment cinétique|
|Translation temps|Énergie|

👉 Structure universelle de la physique

---

# VI – Ouverture : théorème de Noether

## Énoncé (version simple)

Toute symétrie continue d’un système ⇒ quantité conservée

---

## Lecture physique

- espace homogène ⇒ $\vec P$
    
- espace isotrope ⇒ $\vec L$
    
- temps homogène ⇒ $E$
    

---

## Message final (très important à l’oral)

> Les lois de conservation ne sont pas seulement des outils de calcul :  
> elles révèlent la structure profonde des lois physiques.

---

# Conclusion

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