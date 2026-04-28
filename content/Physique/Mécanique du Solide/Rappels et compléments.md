---
title: Rappels et compléments
tags:
  - Agrégation
  - Physique
---

>[!question]-  $=$, $:=$ , $\overset{\mathrm{def}}{=}$ , $\triangleq$ où $\doteq$  ?
>
>>[!note]-   $=$  : égalité (fait mathématique)
>>
>>
>>C’est une **assertion** : deux objets sont égaux, soit par calcul, soit parce que c’est un théorème.
>>
>>>[!example]- **Exemples**
>>>
>>>*   Calcul :
>>>    
>>>$$
>>>2+2 = 4
>>>$$
>>>*   Résultat :
>>>    
>>>$$
>>>\sin^2 x + \cos^2 x = 1
>>>$$
>>>*   Équation à résoudre :
>>>    
>>>$$
>>>x^2 = 1
>>>$$
>>>
>>>👉 Ici, tu affirmes une vérité (à prouver ou déjà prouvée).
>>
>
>
>>[!note]-   $\equiv$  : identité ou congruence
>>
>>
>>Deux usages distincts selon le contexte.
>>
>>
>>>[!note]- (a) Identité (valable pour tout  $x$ )
>>>
>>>
>>>Tu insistes sur le fait que c’est **vrai universellement**, pas juste pour une solution.
>>>
>>>$$
>>>(x+1)^2 \equiv x^2 + 2x + 1
>>>$$
>>>
>>>👉 Différence subtile avec  $=$  :
>>>
>>>*    $=$  peut être une équation à résoudre
>>>*    $\equiv$  dit : _c’est vrai pour tout  $x$ _
>>>
>>
>>
>>>[!note]- (b) Congruence (arithmétique modulaire)
>>>
>>>
>>>$$
>>>a \equiv b \pmod n
>>>$$
>>>
>>>>[!example]- Exemple :
>>>>
>>>>$$
>>>>17 \equiv 5 \pmod{12}
>>>>$$
>>>>
>>>>👉 Là ce n’est **pas une égalité**, mais une relation d’équivalence.
>>>
>>
>
>>[!note]-   $:=$ ,  $\overset{\mathrm{def}}{=}$ ,  $\triangleq$ ,  $\doteq$ 
>>
>>
>>→ définition / affectation
>>
>>Tu **introduis** un objet.
>>
>>
>>
>>>[!note]- (a) Définition stricte
>>>
>>>
>>>$$
>>>f(x) := x^2 + 1
>>>$$
>>>
>>>👉 Tu fixes la signification de  $f$ .
>>>
>>
>>
>>>[!note]- (b) Définition avec mise en avant
>>>
>>>
>>>$$
>>>E \overset{\mathrm{def}}{=} mc^2
>>>$$
>>>
>>>👉 Même chose, mais visuellement explicite dans un texte.
>>
>>
>>>[!note]- (c) Variante notationnelle
>>>
>>>
>>>$$
>>>A \triangleq B
>>>$$
>>>
>>>👉 Souvent utilisée en physique / ingénierie.
>>>
>>
>>
>>>[!note]- (d)  $\doteq$ 
>>>
>>>
>>>Plus ambigu :
>>>
>>>*   parfois **définition**
>>>*   parfois **égalité valable dans un contexte particulier** (genre "à un facteur près" ou "dans ce cadre")
>>>
>>>>[!example]- Exemple typique en physique :
>>>>
>>>>$$
>>>>f(x) \doteq x^2 \quad (\text{approximation ou modèle})
>>>>$$
>>>
>>
>
>
>
>>[!abstract]- Résumé opérationnel (ce qui compte vraiment)
>>
>>
>>| Symbole | Sens | Usage typique |
>>| --- | --- | --- |
>>|  $=$  | égalité | résultat, équation |
>>|  $\equiv$  | identité / congruence | vrai ∀x ou modulaire |
>>|  $:=$  | définition | programmation, maths modernes |
>>|  $\overset{\mathrm{def}}{=}$  | définition explicite | textes formels |
>>|  $\triangleq$  | définition | physique, signal processing |
>>|  $\doteq$  | dépend du contexte | approximation / définition molle |
>
>
>
>>[!example]- Exemple comparatif clair
>>
>>
>>$$
>>f(x) := x^2
>>$$
>>
>>$$
>>f(x) \equiv x^2 \quad (\text{identité vraie ∀x})
>>$$
>> 
>>$$
>>f(2) = 4
>>$$
>> 
>>$$
>>17 \equiv 5 \pmod{12}
>>$$
>> 
>>$$
>>g(x) \doteq x^2 \quad (\text{approximation ou modèle})
>>$$
>
>
>>[!tip]- Point important (niveau avancé)
>>
>>
>>Dans un raisonnement propre :
>>
>>*   **définition** →  $:=$ 
>>*   **résultat démontré** →  $=$ 
>>*   **identité structurelle** →  $\equiv$ 
>>
>>Si tu mélanges tout avec  $=$ , tu perds de l’information logique.
>


# 1. Rappels de cinématique de solide

- un référentiel $\mathscr R \doteq ( O ; \vec{e}_x ,  \vec{e}_y , \vec{e}_z )$ ; repère cartésien, et on notera la base $\mathscr B = (\vec{e}_x ,  \vec{e}_y , \vec{e}_z )$; 
- un référentiel $\mathscr R' \doteq ( O' ; \vec{e}_{x'} ,  \vec{e}_{y'} , \vec{e}_{z'} )$ ; repère cartésien , mobile par rapport à $\mathscr R$.  Et on notera la base mobile $\mathscr B' = (\vec{e}_{x'} ,  \vec{e}_{y'} , \vec{e}_{z'} )$ par rapport à la base $\mathscr B$.

## 1. Champ des vitesse d'un solide
### 1. Vecteur Position 
On peut définir la position $M$ dans les deux référentiels :

- Dans $\mathscr R$ : $\overrightarrow{OM} \equiv x \vec{e}_x + y \vec{e}_y + z \vec{e}_z $ : ( $M$ à partir de l'origine $O$ et dans la base $(\vec{e}_{x} ,  \vec{e}_{y} , \vec{e}_{z})$ ) 
- Dans $\mathscr R'$ : $ \overrightarrow{O'M}  \equiv x' \vec{e}_{x'} + y' \vec{e}_{y'} + z' \vec{e}_{z'} $ :  ( $M$ à partir de l'origine $O'$  et dans la base $(\vec{e}_{x'} ,  \vec{e}_{y'} , \vec{e}_{z'})$ )

Et 
$$
\overrightarrow{OM} = \overrightarrow{OO'} + \overrightarrow{O'M} \, .
$$

>[!tip]- La fonction $\overrightarrow{o}_{\mathscr R}(M)$
>On peut définir une fonction position 
>$$ 
>\overrightarrow{o}_{\mathscr R}(M) \doteq \left .\overrightarrow{OM}  \right)_{\mathscr R} \doteq x \vec{e}_x + y \vec{e}_y + z \vec{e}_z \, , 
>$$
>paramétrer par le référentiel $\mathscr R$ et avec le point $M$ comme argument  ( $M$ à partir de l'origine $O$ et dans la base $(\vec{e}_{x} ,  \vec{e}_{y} , \vec{e}_{z})$ ) 
>
>- Dans $\mathscr R$ : $\overrightarrow{o}_{\mathscr R}(M) \doteq \left .\overrightarrow{OM}  \right)_{\mathscr R} \doteq x \vec{e}_x + y \vec{e}_y + z \vec{e}_z $ : ( $M$ à partir de l'origine $O$ et dans la base $(\vec{e}_{x} ,  \vec{e}_{y} , \vec{e}_{z})$ ) 
>- Dans $\mathscr R'$ : $\overrightarrow{o}_{\mathscr R'}(M) \doteq \left. \overrightarrow{O'M} \right)_{\mathscr R'} \doteq x' \vec{e}_{x'} + y' \vec{e}_{y'} + z' \vec{e}_{z'} $ :  ( $M$ à partir de l'origine $O'$  et dans la base $(\vec{e}_{x'} ,  \vec{e}_{y'} , \vec{e}_{z'})$ )
>
>$$
>\overrightarrow{o}_{\mathscr R}(M) = \overrightarrow{OM} = \overrightarrow{OO'} + \overrightarrow{O'M} = \overrightarrow{o}_{\mathscr R}(O') + \overrightarrow{o}_{\mathscr R'}(M)
>$$

>[!note]- Notation $\left . \overrightarrow{A} \right )_{\mathscr R}$
>
> Le vecteur $\overrightarrow{A}$ dans le reférentiel $\mathscr R$.


### 2. Vecteur Vitesse ,  Accélération 

>[!tip]- Caractère absolue du temps
>
>*En mécanique classique*, le temps est une quantité absolue, indépendante du référentiel :
>$$
>t' = t 
>$$

Dans le référentiel $\mathscr R$ la base $(\vec{e}_{x},\vec{e}_{y},\vec{e}_{y} )$ est constante. Donc les vecteur vitesse et accélération du point $M$ dans le référentiel $\mathscr R$ s'écrivent 
$$
\overrightarrow{v}_{\mathscr R} (M) = \displaystyle \left.\frac{ d \overrightarrow{OM} }{dt} \right)_{\mathscr R} = \frac{ d x}{d t } \vec{e}_{x} + \frac{ d y}{d t } \vec{e}_{y} + \frac{ d z}{d t } \vec{e}_{z} , \quad \& \quad  \overrightarrow{a}_{\mathscr R} (M) = \displaystyle \left.\frac{ d^2 \overrightarrow{OM} }{{dt}^2} \right)_{\mathscr R} = \frac{ d^2 x}{{dt}^2} \vec{e}_{x} + \frac{ d^2 y}{{dt}^2} \vec{e}_{y} + \frac{ d^2 z}{{dt}^2 } \vec{e}_{z}.
$$

Et dans le référentiel $\mathscr R'$ la base $(\vec{e}_{x'},\vec{e}_{y'},\vec{e}_{y'} )$ est constante. Donc les vecteur vitesse et accélération du point $M$ dans le référentiel $\mathscr R'$ s'écrivent 
$$
\overrightarrow{v}_{\mathscr R'} (M) = \displaystyle \left.\frac{ d \overrightarrow{O'M} }{dt} \right)_{\mathscr R'} = \frac{ d x'}{d t } \vec{e}_{x'} + \frac{ d y'}{d t } \vec{e}_{y'} + \frac{ d z'}{d t } \vec{e}_{z'}, \quad \& \quad \overrightarrow{a}_{\mathscr R'} (M) = \displaystyle \left.\frac{ d^2 \overrightarrow{O'M} }{{dt}^2} \right)_{\mathscr R'} = \frac{ d^2 x'}{{dt}^2} \vec{e}_{x'} + \frac{ d^2 y'}{{dt}^2} \vec{e}_{y'} + \frac{ d^2 z'}{{dt}^2} \vec{e}_{z'}.
$$

### 3. Mouvement relatif de deux référentiels 

#### 1. Deux types de mouvement 

De manière générale, le mouvement de $\mathscr R'$ par rapport à $\mathscr R$ se décompose en :
- une translation instantanée, que l'on peut décrire par le mouvement de n'importe quel point fixe de $\mathscr R'$ (par exemple $O'$)
$$
\overrightarrow{v}_{\mathscr R} (O'), \quad \overrightarrow{a}_{\mathscr R} (O'), \quad \cdots 
$$
- une rotation instantanée, correspondant au changement d'orientation des vecteurs $\vec{e}_{x'}$ , $\vec{e}_{y'}$ et $\vec{e}_{z'}$ dans le référentiel $\mathscr R$ . On définit ainsi le **vecteur rotation** $\overrightarrow{\Omega}_{\mathscr R'/\mathscr R}$ ("rotation de $\mathscr R'$ par rapport à $\mathscr R$" )
$$
{\displaystyle \left.\frac{d \vec{e}_{i'} }{dt}\right)_{\mathscr R} = \overrightarrow{\Omega}_{\mathscr R'/ \mathscr R} \wedge \vec{e}_{i'}} , \quad i \in \{ x , y  , z \}.
$$


>[!question]- ${\displaystyle \left.\frac{d \vec{e}_{i'} }{dt}\right)_{\mathscr R} = \overrightarrow{\Omega}_{\mathscr R'/ \mathscr R} \wedge \vec{e}_{i'}}$
>
>Le référentiel $\mathscr R'$ est mobile par rapport  au référentiel $\mathscr R$. Donc si on fixe le centre $O$ et la base orthonormale $B = (\vec{e}_x,\vec{e}_y,\vec{e}_z)$ au référentiel $\mathscr R$; on fixe $O'(t)$ et la base orthonormale  $B'(t) \equiv (\vec{e}_{x'}(t),\vec{e}_{y'}(t),\vec{e}_{z'}(t))$ au référentiel  $\mathscr R'$; dépendent du temps $t$ dans le  référentiel $\mathscr R$.
>
>On ce met dans le référentiel $\mathscr R$, le centre $O'(t)$ est en translation (c'est un point ;))  et on étudit comment  la base orthonormale $B'(t) \equiv (\vec{e}_{x'}(t),\vec{e}_{y'}(t),\vec{e}_{z'}(t))$ se comportent.
>
>> [!tip]- $\forall t \in \mathbb R  \colon \exist f_t \in \mathcal{SO}(\mathbb R^3), \forall i \in \{x , y , z\} \colon \vec{e}_{i'}(t) = f_t(\vec{e}_{i'}(0))$.
>> 
>> *Hypothèses*.
>> - L'espace liés au référentiel $\mathscr R'$ ne se déforme pas par rapport à l'espace liés au référentiel $\mathscr R$, donc la base orthonormale $B'(t)$ subis une isométrie. (cf la proposition [[Mathématique/Algèbre/Algèbre#Propriétés matricielles des isométries et des endomorphismes unitaires.|Proposition 5.2.3.6.]]). L'ensemble des isométries d'une espace euclidien (ici $\mathbb R^3$) est un groupe (muni de la loi $\circ$ de composition), appelé *groupe orthogonal* de $\mathbb R^3$ et noté $\mathcal O(\mathbb R^3)$ (cf la [[Mathématique/Algèbre/Algèbre#3. Isométries et endomorphismes unitaires|Proposition 5.2.3.5.]]).  Donc 
>> $$
>> \forall t \in \mathbb R  \colon \exist f_t \in \mathcal O(\mathbb R^3), \forall i \in \{x , y , z\} \colon \vec{e}_{i'}(t) = f_t(\vec{e}_{i'}(0)).
>> $$
>> - De plus l'hypothèse que l'absence de déformation de l'espace liés au référentiel $\mathscr R'$ par rapport à l'espace liés au référentiel $\mathscr R$ permet aussi  de supposerque $(\vec{e}_{x'}(t),\vec{e}_{y'}(t),\vec{e}_{z'}(t))$ reste directe (resp. indirecte) au court du temps. Soit $\forall t \in \mathbb R \colon \vec{e}_{x'}(t)\wedge \vec{e}_{y'}(t) = \vec{e}_{z'}(t)$ (resp. $\vec{e}_{x'}(t)\wedge \vec{e}_{y'}(t) = -\vec{e}_{z'}(t)$). L'ensemble $\{f \in \mathcal O(\mathbb R^3) \vert \det f = 1 \}$ est un sous-groupe distingué de $\mathcal O(\mathbb R^3)$ appelé *groupe spécial orthonormal* de $\mathbb R^3$ et noté $\mathcal O^+(\mathbb R^3)$ (on le note encore $\mathcal{S O}(\mathbb R^3)$) (cf la [[Mathématique/Algèbre/Algèbre#Propriétés matricielles des isométries et des endomorphismes unitaires.|Définition 5.2.3.4.]]). 
>> $$
>>\forall t \in \mathbb R  \colon \exist f_t \in \mathcal{SO}(\mathbb R^3), \forall i \in \{x , y , z\} \colon \vec{e}_{i'}(t) = f_t(\vec{e}_{i'}(0)).
>>$$ 
>
>>[!tip]- $\forall t \in \mathbb R  \colon \exist f_t \in \mathcal{SO}(\mathbb R^3), \forall i \in \{x , y , z\} \colon \vec{e}_{i'}(0) = f_t^\ast(\vec{e}_{i'}(t))$.
>>
>>En réunissant la  [[Mathématique/Algèbre/Algèbre#3. Isométries et endomorphismes unitaires|Proposition 5.2.3.3]]  ($\forall (x , y) \in (\mathbb R^3)^2 \colon f(x) \cdot f(y) = x \cdot y$) sur la  [[Mathématique/Algèbre/Algèbre#4. Endomorphismes adjoints|Définition 5.2.3.5.]] d'ajoint $f_t^\ast$ d'un endomorphisme $f_t$ ($\forall (x , y) \in (\mathbb R^3)^2 \colon f(x) \cdot y = x \cdot f^\ast(y)$), il vient que pour $ (x , y ) \in (\mathbb R^3)^2 $ , il vient que $  x \cdot y  = f_t(x) \cdot f_t(y) =  x \cdot  (f_t^\ast \circ f_t)(y)$ , soit 
>>$$
>>\forall x , y \in \mathbb R^3 \colon x \cdot y  =  x \cdot  (f_t^\ast \circ f_t)(y).
>>$$
>> Par non-dégénérescence du produit scalaire :
>>$$
>>f_t^\ast \circ f_t = \text{id}_{\mathbb R^3} .
>>$$
>> Et la [[Mathématique/Algèbre/Algèbre#3. Isométries et endomorphismes unitaires|Proposition 5.2.3.4]] dit que une isométrie $f_t$ est injective et en dimension finie $f_t$ est bilective. Donc ici $f_t^{-1}$ existe et $\forall x , y \in \mathbb R^3 \colon x \cdot y = (f_t \circ f_t^{-1}) (x) \cdot y = f_t^{-1}(x) \cdot f_t^\ast(y) = (f_t \circ f_t^{-1}) (x) \cdot ( f_t \circ f_t^\ast) (y) = x \cdot ( f_t \circ f_t^\ast) (y)$ soit 
>>$$
>>\forall x , y \in \mathbb R^3 \colon x \cdot y  =  x \cdot  (f_t \circ f_t^\ast)(y).
>>$$
>> Par non-dégénérescence du produit scalaire :
>>$$
>>f_t \circ f_t^\ast = \text{id}_{\mathbb R^3} .
>>$$
>>Donc 
>>$$
>>\forall t \in \mathbb R  \colon \exist f_t \in \mathcal{SO}(\mathbb R^3), \forall i \in \{x , y , z\} \colon \vec{e}_{i'}(0) = f_t^\ast(\vec{e}_{i'}(t)).
>>$$ 
>>👉 donc l’espace engendré est de dimension 2 :
>>
>>
>
> Utilisons ces propriétés, en partant de 
>$$
>\forall t \in \mathbb R  \colon \exist f_t \in \mathcal{SO}(\mathbb R^3), \forall i \in \{x , y , z\} \colon \vec{e}_{i'}(t) = f_t(\vec{e}_{i'}(0)).
>$$
>Et en dérivant , il vient que 
>$$
>\forall t \in \mathbb R  \colon \exist f_t \in \mathcal{SO}(\mathbb R^3), \forall i \in \{x , y , z\} \colon \dot{\vec{e}}_{i'}(t) = \dot{f}_t(\vec{e}_{i'}(0)) = (\dot{f}_t \circ f_t^\ast)(\vec{e}_{i'}(t)).
>$$
>>[!tip]- $\dot{f}_t \circ f_t^\ast \in \mathfrak{so}(\mathbb R^3) = \{ f \in \mathcal L(\mathbb{R}^3) \;\mid\; f^\ast  = -f \} $.
>>
>>$\forall t \in \mathbb R \colon f_t \in \mathcal{SO}(\mathbb R^3)$ donc 
>>$$
>> \forall t \in \mathbb R \colon f_t \circ f_t^\ast  = \text{id}_{\mathbb R^3}. 
>>$$
>>Donc en dérivant selon le temps $t$ il viens que $ \dot{(f_t \circ f_t^\ast)} = 0$ , soit  :
>>$$
>>\dot{f}_t\circ f_t^\ast  = - f_t \circ  \dot{f}_t^\ast,  \tag{$\ast$}
>>$$
>>> [!tip]+
>>> $$
>>> \forall f , g \in \mathcal L ( E)  \colon ( f \circ g )^\ast = g^\ast \circ f^\ast \tag{$\ast \ast$}.
>>> $$
>>> 
>>> $$
>>> \forall f , g \in \mathcal L (E) \colon \forall x , y \in E \colon x \cdot ( f \circ g )^\ast ( y) = ( f \circ g )(x) \cdot y = g(x) \cdot f^\ast(y) = x \cdot (g^\ast \circ f^\ast )(y)
>>> $$
>>
>>Et en cherchant l'adjoint de  ($\ast$) et  ($\ast\ast $), il vient que 
>>$$
>>(\dot{f}_t\circ f_t^\ast)^\ast  = - (f_t \circ  \dot{f}_t^\ast)^\ast  = -  \dot{f}_t \circ  f_t^\ast
>>$$
>>Donc 
>>$$
>>\dot{f}_t\circ f_t^\ast \in \mathfrak{so}(\mathbb R^3) = \{ f \in \mathcal L(\mathbb{R}^3) \;\mid\; f^\ast  = -f \}.
>>$$
>
>On note 
>$$
>\forall t \in \mathbb R \colon \Omega_t \doteq \dot{f}_t\circ f_t^\ast \in \mathfrak{so}(\mathbb R^3),
>$$
>antysymétrique .
>
>L' [[Mathématique/Algèbre/Algèbre#Exercice 5. (Exponentielle d'une matrice antisymétrique)|Exercice 5.3.5.5. (Exponentielle d'une matrice antisymétrique)]] , nous dit entre autre  
>$$
>\forall t \in \mathbb R \colon \forall f_t \in \mathcal{SO}(\mathbb R^3) \colon  \exist g_t \in \mathfrak{so}(\mathbb R^3), f_t = \exp(g_t).
>$$
>Il existe une vecteur $\overrightarrow{v}(t)\in \mathbb R^3$ tel que 
>$$
>g_t \colon \; \mathbb R^3 \rightarrow \mathbb R^3 \quad \overrightarrow{x} \mapsto \overrightarrow{v}(t) \wedge  \overrightarrow{x}.
>$$
>
>>[!tip]- Écritures matricielles de $g_t$.
>>  
>> Si dans la base $B$ , $\overrightarrow{v}(t) = ( v_x(t) , v_y(t) , v_z(t))$ alors 
>>$$
>>[g_t]_{B} = 
>>\left ( 
>>\begin{array}{ccc}
>>0& -v_z(t) & v_y(t) \\
>>v_z(t) & 0 & -v_x(t ) \\
>>-v_y(t) & v_x(t) & 0 \\
>>\end{array} 
>>\right ).
>>$$
>>Partant du vecteur $\vec{u}(t) = \overrightarrow{v}(t)/ \Vert \overrightarrow{v}(t) \Vert = \frac{1}\theta(t) \overrightarrow{v}(t) $, on le complète avec deux vecteurs $\vec{u}_1(t)$ et $\vec{u}_2(t)$ de sorte que $B_1(t) \doteq (\vec{u}_1(t) , \vec{u}_2(t) , \vec{u}(t) )$ soit une base orthogonormale directe de $\mathbb R^3$. Comme $\overrightarrow{v} = \theta(t) \vec{u}(t)$ , on a 
>>$$
>>g_t(\vec{u}_1) = \theta(t) \vec{u}(t) \wedge \vec{u}_1(t) = \theta(t) \vec{u}_2(t) , \quad g_t(\vec{u}_2(t)) = \theta(t) \vec{u}(t) \wedge \vec{u}_2(t) = - \theta(t) \vec{u}_1(t) , \quad g_t(\vec{u}(t)) = \theta(t) \vec{u}(t) \wedge \vec{u}(t) = 0,
>>$$
>>autrement dit la matrice de $g_t$ dans la base $B_1(t)$ à la forme par blocs 
>>$$
>>[g_t]_{B_1(t)} = 
>>\left (
>>\begin{array}{cc}
>>\theta(t)  J & 0_{2,1} \\
>>0_{1,2} & 0  \\
>>\end{array}
>>\right )
>>$$
>>où $J = {\scriptstyle  \left ( \begin{smallmatrix} 0 & -1 \\ +1 & 0  \end{smallmatrix} \right )}$.
>
>
>De plus $\Omega_t \doteq \dot{f}_t\circ f_t^\ast \in \mathfrak{so}(\mathbb R^3)$ antisymétrique donc il existe une vecteur $\overrightarrow{\omega}(t)\in \mathbb R^3$ tel que 
>$$
>\Omega_t \colon \; \mathbb R^3 \rightarrow \mathbb R^3 \quad \overrightarrow{x} \mapsto \overrightarrow{\omega}(t) \wedge  \overrightarrow{x}.
>$$
>>[!tip]- Écritures matricielles de $\Omega_t$.
>>  
>> Si dans la base $B$ , $\overrightarrow{\omega}(t) = ( \omega_x(t) , \omega_y(t) , \omega_z(t))$ alors 
>>$$
>>[\Omega_t]_{B} = 
>>\left ( 
>>\begin{array}{ccc}
>>0& -\omega_z(t) & \omega_y(t) \\
>>\omega_z(t) & 0 & -\omega_x(t ) \\
>>-\omega_y(t) & \omega_x(t) & 0 \\
>>\end{array} 
>>\right ).
>>$$    
>>Partant du vecteur $\vec{u}(t) = \overrightarrow{\omega}(t)/ \Vert \overrightarrow{\omega}(t) \Vert = \frac{1}\theta(t) \overrightarrow{\omega}(t) $, on le complète avec deux vecteurs $\vec{u}_1(t)$ et $\vec{u}_2(t)$ de sorte que $B_1(t) \doteq (\vec{u}_1(t) , \vec{u}_2(t) , \vec{u}(t) )$ soit une base orthogonormale directe de $\mathbb R^3$. Comme $\overrightarrow{\omega} = \theta(t) \vec{u}(t)$ , on a 
>>$$
>>\Omega_t(\vec{u}_1) = \theta(t) \vec{u}(t) \wedge \vec{u}_1(t) = \theta(t) \vec{u}_2(t) , \quad \Omega_t(\vec{u}_2(t)) = \theta(t) \vec{u}(t) \wedge \vec{u}_2(t) = - \theta(t) \vec{u}_1(t) , \quad \Omega_t(\vec{u}(t)) = \theta(t) \vec{u}(t) \wedge \vec{u}(t) = 0,
>>$$
>>autrement dit la matrice de $g_t$ dans la base $B_1(t)$ à la forme par blocs 
>>$$
>>[\Omega_t]_{B_1(t)} = 
>>\left (
>>\begin{array}{cc}
>>\theta(t)  J & 0_{2,1} \\
>>0_{1,2} & 0  \\
>>\end{array}
>>\right )
>>$$
>>où $J = {\scriptstyle  \left ( \begin{smallmatrix} 0 & -1 \\ +1 & 0  \end{smallmatrix} \right )}$.
>
>Le lien entre $\overrightarrow{\omega}(t)$ et $\overrightarrow{v}(t)$ est la formule de   [Rodrigues](https://rotations.berkeley.edu/other-representations-of-a-rotation/).
>
>>[!tip]- Formule de Rodrigeus $\overrightarrow{\omega}(t) = \overrightarrow{\dot{v}}(t) + \frac{1 - \cos(\Vert\overrightarrow{v}(t) \Vert)}{\Vert \overrightarrow{v}(t) \Vert^2} \overrightarrow{v}(t) \wedge \overrightarrow{\dot{v}}(t) + \frac{\Vert \overrightarrow{v}(t) \Vert - \sin(\Vert\overrightarrow{v}(t) \Vert)}{\Vert \overrightarrow{v}(t) \Vert^3} \overrightarrow{v}(t) \wedge ( \overrightarrow{v}(t) \wedge \overrightarrow{\dot{v}}(t) ).$
>>
>>>[!tip]-  $\frac{d ( f_t\circ g_t )}{dt}(x) = (\dot f_t \circ g_t)(x) + (D\{f_t\}_{g_t(x)}) \cdot (\dot g_t)(x)) $
>>
>>
>>Donc si on dérive par rapport à $t$ 
>>
>>>[!danger]- Je ne sais pas si $\dot{g}_t$ et  $g_t$  commutent !!
>>>
>>>La parité de $d/dt$ et de $\dot{g}_t$ sont paire. Ce sont des bosons. Donc d'après [[Algèbres graduées, formes différentielles et structure de superalgèbre de Lie#Autre définition de $d(e a)$|Autre définition de exp(a)]]      
>>>$$
>>>\frac{d e^{g_t}}{dt} =  e^{g_t} \circ  \phi\left (- \text{ad}_{g_t}\right)(dot{g}_t) =  \phi\left ( \text{ad}_{g_t}\right)(\dot{g}_t)\circ e^{g_t} . 
>>>$$
>>> avec 
>>> $$
>>> \phi(z) \equiv \frac{e^{z} - 1 }{z} = \sum_{n = 0}^{\infty} \frac{z^n}{(n+1)!}  \quad \text{et} \quad \text{ad}_{f}(g) = [f , g ] = f \circ g - g \circ f.
>>> $$
>>
>>
>> 
>>$$
>>\forall t \in \mathbb R \colon \forall f_t \in \mathcal{SO}(\mathbb R^3) \colon  \exist g_t \in \mathfrak{so}(\mathbb R^3), \dot{f}_t = \phi\left ( \text{ad}_{g_t}\right)(\dot{g}_t)\circ \exp(g_t) = \phi\left ( \text{ad}_{g_t}\right)(\dot{g}_t)\circ \cdot f_t ,
>>$$
>>avec 
>>$$
>>\phi(z) \equiv \frac{e^{z} - 1 }{z} = \sum_{n = 0}^{\infty} \frac{z^n}{(n+1)!}    
>>\quad ,  \;  
>>\text{ad}_{f}(g) = [f , g ] = f \circ g - g \circ f
>>\quad \text{et} \quad 
>>\dot{g}_t \colon \; \mathbb R^3 \rightarrow \mathbb R^3 \quad \overrightarrow{x} \mapsto \dot{\overrightarrow{v}}(t) \wedge  \overrightarrow{x}.
>>$$
>>En utilisant que $f_t \circ f_t^\ast = \text{id}_{\mathbb R^3}$, il vient que 
>>$$
>>\Omega_t \doteq \dot{f}_t\circ f_t^\ast = \phi\left ( \text{ad}_{g_t}\right)(\dot{g}_t) \circ f_t \circ  f_t^\ast  = \phi\left ( \text{ad}_{g_t}\right)(\dot{g}_t)     
>>$$
>>
>>>[!tip]- $\psi(\mathrm{ad}_{\hat{v}})(\hat{u}) = \widehat{ \sum_{n = 0}^\infty a_i \, \underbrace{ v \wedge (v \wedge (\cdots \wedge (v}_{\text{n termes}} \wedge u) \cdots ) ) }$ avec $\psi(z) = \sum_{n = 0}^\infty a_i z^n $.
>>>
>>>Si on note $\hat{v}$ tel que $\hat{v}(x) = v \wedge x$
>>>Alors 
>>>$$
>>>\hat{v} + \hat{u}  = \widehat{v + u} \quad \& \quad [ \hat{v} , \hat{u}] = \widehat{v \wedge u }
>>>$$
>>>avec $[ \hat{v} , \hat{u}] = \hat{v} \circ  \hat{u} -  \hat{u} \circ  \hat{v}$.  
>> Donc on note $\mathrm{ad}_{\hat{v}}$ tel que  $\mathrm{ad}_{\hat{v}}(\hat{u}) = [ \hat{v} , \hat{u}]$ . Donc 
>>> $$
>>> \mathrm{ad}_{\hat{v}}^n \equiv \underset{i = 0}{\overset{n}{\bigcirc}}\mathrm{ad}_{\hat{v}}  \equiv [ \hat{v} , \mathrm{ad}_{\hat{v}}^{n-1} ] \equiv [\underbrace{ \hat{v} , [ \hat{v} , [ \cdots [\hat{v}}_{\text{n termes }} , \bullet ] \cdots ] ] ] \equiv \widehat{\underbrace{ v \wedge (v \wedge (\cdots \wedge (v}_{\text{n termes}} \wedge \bullet) \cdots ) ) } \equiv \widehat{ v \wedge v^n }  \equiv \widehat{\underset{i = 0 }{\overset{n}{\bigwedge}} v } \equiv \widehat{v^n}
>>> $$
>>> et pour tous fonction $\psi$ analytique ($\psi(z) = \sum_{n = 0}^\infty a_i z^n $) on a  
>>>$$
>>>\psi(\mathrm{ad}_{\hat{v}})(\hat{u}) = \widehat{ \sum_{n = 0}^\infty a_i \, \underbrace{ v \wedge (v \wedge (\cdots \wedge (v}_{\text{n termes}} \wedge u) \cdots ) ) } .
>>>$$  
>>
>>Donc 
>>$$
>>\Omega_t \doteq \dot{f}_t\circ f_t^\ast =  \phi\left ( \text{ad}_{g_t}\right)(\dot{g}_t) =  \widehat{ \sum_{n = 0}^\infty \frac{1}{(n+1)!} \, \underbrace{ \overrightarrow{v}(t) \wedge ( \overrightarrow{v}(t) \wedge (\cdots \wedge (\overrightarrow{v}(t)}_{\text{n termes}} \wedge  \overrightarrow{\dot v}(t) ) \cdots ) ) },   
>>$$
>>avec $ g_t (\overrightarrow{x}) = \widehat{\overrightarrow{v}}(t) = \overrightarrow{v}(t) \wedge \overrightarrow{x} \quad \& \quad \dot{g}_t (\overrightarrow{x}) = \widehat{\overrightarrow{\dot{v}}}(t) = \overrightarrow{\dot{v}}(t) \wedge \overrightarrow{x} $ .
>>Ainsi 
>>$$
>>\Omega_t = \widehat{\overrightarrow{\omega}}(t) \quad \text{avec} \quad \overrightarrow{\omega}(t) = \sum_{n = 0}^\infty \frac{1}{(n+1)!} \, \underbrace{ \overrightarrow{v}(t) \wedge ( \overrightarrow{v}(t) \wedge (\cdots \wedge (\overrightarrow{v}(t)}_{\text{n termes}} \wedge  \overrightarrow{\dot v}(t) ) \cdots ) )    ).  
>>$$
>>
>>>[!tip]- Structure algébrique cruciale 
>>>
>>>Dans $\mathbb{R}^3$ :
>>>$$
>>>v\wedge(v\wedge x) = v(v\cdot x) - \|v\|^2 x
>>>$$
>>>👉 donc l’espace engendré est de dimension 2 :
>>>$$
>>>\{\,\dot v,\; v\wedge \dot v,\; v\wedge(v\wedge \dot v)\,\}
>>>$$
>>>Tous les termes se réexpriment dans cette base.
>>
>>On a 
>>$$
>>\begin{array}{rclcl}
>>\mathrm{ad}_{\hat{v}}(\hat{u}) & = & \widehat{  \overrightarrow{v} \wedge \overrightarrow{u} } , \\
>>\mathrm{ad}_{\hat{v}}^2(\hat{u}) & = & \widehat{  \overrightarrow{v} \wedge ( \overrightarrow{v} \wedge \overrightarrow{u} ) } & = & \widehat{( \overrightarrow{v} \cdot \overrightarrow{u} ) \overrightarrow{v} - \Vert \overrightarrow{v} \Vert^2 \overrightarrow{u}} , \\
>>\mathrm{ad}_{\hat{v}}^3(\hat{u}) & = & \widehat{( \overrightarrow{v} \cdot \overrightarrow{u} ) \underbrace{\overrightarrow{v} \wedge \overrightarrow{v}}_{0} - \Vert \overrightarrow{v} \Vert^2  \overrightarrow{v} \wedge \overrightarrow{u}} & = & -  \Vert \overrightarrow{v} \Vert^2 \mathrm{ad}_{\hat{v}}(\hat{u}) \\
>>\end{array}
>>$$
>>Donc 
>>$$
>>\mathrm{ad}_{\hat{v}}^{2k +1} = ( - \Vert \overrightarrow{v} \Vert^2  )^k \mathrm{ad}_{\hat{v}} \quad \& \quad \mathrm{ad}_{\hat{v}}^{2k +2} = ( - \Vert \overrightarrow{v} \Vert^2  )^k \mathrm{ad}_{\hat{v}}^2.
>>$$
>>Or 
>>$$
>>e^{\mathrm{ad}_{\hat{v}}} = \sum_{n=0}^\infty \frac{\mathrm{ad}_{\hat{v}}^n}{n!}
>>$$
>>On sépare :
>>
>>**termes impairs**
>>$$
>>\sum_{k=0}^\infty \frac{\mathrm{ad}_{\hat{v}}^{2k+1}}{(2k+1)!} = \mathrm{ad}_{\hat{v}} \underbrace{\sum_{k=0}^\infty \frac{(-\Vert \overrightarrow{v} \Vert^2)^k}{(2k+1)!}}_{\frac{\sin(\Vert \overrightarrow{v} \Vert)}{\Vert \overrightarrow{v} \Vert}}
>>$$
>>**termes pairs (≥2)**
>>$$
>>\sum_{k=0}^\infty \frac{\mathrm{ad}_{\hat{v}}^{2k+2}}{(2k+2)!} = \mathrm{ad}_{\hat{v}}^2 \underbrace{\sum_{k=0}^\infty \frac{(-\Vert \overrightarrow{v} \Vert^2)^k}{(2k+2)!}}_{\frac{1 - \cos(\Vert \overrightarrow{v} \Vert)}{\Vert \overrightarrow{v} \Vert^2}}
>>$$
>>Donc 
>>$$
>>e^{\mathrm{ad}_{\hat{v}}} = I + \mathrm{ad}_{\hat{v}} \sum_{k=0}^\infty \frac{(-\Vert \overrightarrow{v} \Vert^2)^k}{(2k+1)!} + \mathrm{ad}_{\hat{v}}^2 \sum_{k=0}^\infty \frac{(-\Vert \overrightarrow{v} \Vert^2)^k}{(2k+2)!} = \mathrm{id} + \frac{\sin(\Vert \overrightarrow{v} \Vert)}{\Vert \overrightarrow{v} \Vert}\mathrm{ad}_{\hat{v}} + \frac{1 - \cos(\Vert \overrightarrow{v} \Vert)}{\Vert \overrightarrow{v} \Vert^2}\mathrm{ad}_{\hat{v}}^2.
>>$$
>>Maintenant 
>>$$
>>\phi(\mathrm{ad}_{\hat{v}}) = \sum_{n = 0}^\infty \frac{\mathrm{ad}_{\hat{v}}^n}{(n+1)!} = \mathrm{id} + \sum_{n = 0}^\infty \frac{\mathrm{ad}_{\hat{v}}^{2n+1}}{(2n+2)!} + \sum_{n = 0}^\infty \frac{\mathrm{ad}_{\hat{v}}^{2n+2}}{(2n+3)!}  = \mathrm{id} + \sum_{n = 0}^\infty \frac{(-\Vert \overrightarrow{v} \Vert^2)^k}{(2n+2)!} \mathrm{ad}_{\hat{v}} + \sum_{n = 0}^\infty \frac{(-\Vert \overrightarrow{v} \Vert^2)^k}{(2n+3)!} \mathrm{ad}_{\hat{v}}^2, 
>>$$
>>et on a
>>$$
>>\sum_{n = 0}^\infty \frac{(-\Vert \overrightarrow{v} \Vert^2)^k}{(2n+2)!} = \frac{1}{\Vert \overrightarrow{v} \Vert^2} \sum_{n = 0}^\infty \frac{\displaystyle (-1)^k \Vert \overrightarrow{v} \Vert^{2k +2}}{(2n+2)!} = \frac{\displaystyle 1 - \sum_{n = 0}^\infty \frac{\displaystyle (-1)^k\Vert \overrightarrow{v} \Vert^{2k}}{(2n)!}}{\Vert \overrightarrow{v} \Vert^2} = \frac{1 - \cos(\Vert\overrightarrow{v} \Vert)}{\Vert \overrightarrow{v} \Vert^2}
>>$$
>>et 
>>$$
>>\sum_{n = 0}^\infty \frac{(-\Vert \overrightarrow{v} \Vert^2)^k}{(2n+3)!} = \frac{1}{\Vert \overrightarrow{v} \Vert^3} \sum_{n = 0}^\infty \frac{\displaystyle (-1)^k \Vert \overrightarrow{v} \Vert^{2k +3}}{(2n+3)!} = \frac{\displaystyle \Vert \overrightarrow{v} \Vert - \sum_{n = 0}^\infty \frac{\displaystyle (-1)^k\Vert \overrightarrow{v} \Vert^{2k+1}}{(2n+1)!}}{\Vert \overrightarrow{v} \Vert^2} = \frac{\Vert \overrightarrow{v} \Vert - \sin(\Vert\overrightarrow{v} \Vert)}{\Vert \overrightarrow{v} \Vert^3},
>>$$
>>Donc 
>>$$
>>\phi(\mathrm{ad}_{\hat{v}}) =  \mathrm{id} + \frac{1 - \cos(\Vert\overrightarrow{v} \Vert)}{\Vert \overrightarrow{v} \Vert^2} \mathrm{ad}_{\hat{v}} + \frac{\Vert \overrightarrow{v} \Vert - \sin(\Vert\overrightarrow{v} \Vert)}{\Vert \overrightarrow{v} \Vert^3} \mathrm{ad}_{\hat{v}}^2,
>>$$
>>et $ \Omega_t = \widehat{\omega}(t) = \phi(\mathrm{ad}_{\hat{v}(t)})(\hat{\dot{v}}(t)) $ Donc 
>>$$
>> \overrightarrow{\omega}(t) = \overrightarrow{\dot{v}}(t) + \frac{1 - \cos(\Vert\overrightarrow{v}(t) \Vert)}{\Vert \overrightarrow{v}(t) \Vert^2} (\overrightarrow{v}(t) \wedge \overrightarrow{\dot{v}}(t)) + \frac{\Vert \overrightarrow{v}(t) \Vert - \sin(\Vert\overrightarrow{v}(t) \Vert)}{\Vert \overrightarrow{v}(t) \Vert^3} (\overrightarrow{v}(t) \wedge ( \overrightarrow{v}(t) \wedge \overrightarrow{\dot{v}}(t) )).
>> $$
>
>>[!tip]- $\overrightarrow{\omega}(t) = \dot\theta(t)\vec{u} + \theta(t)\vec{\dot{u}} + (1 - \cos(\theta(t)))(\vec{u}(t) \wedge \vec{\dot{u}}(t)) + (\theta(t) - \sin(\theta(t)))(\vec{u}(t) \wedge ( \vec{u}(t) \wedge \vec{\dot{u}}(t) )$
>>
>>Si on note $\theta(t) = \Vert \overrightarrow{v}(t) \Vert$ tel que $\vec{u}(t) = \frac{\overrightarrow{v}(t)}{\Vert \overrightarrow{v}(t) \Vert}$. Donc 
>>$$
>>\begin{array}{rclcl}
>>\overrightarrow{\dot{v}}(t) & = & \dot{\theta}(t) \vec{u}(t)  + \theta(t)\dot{u}(t),\\
>>\overrightarrow{v}(t) \wedge \overrightarrow{\dot{v}}(t) & = & \dot{\theta}(t)\theta(t) (\underbrace{\vec{u}(t) \wedge \vec{u}(t)}_{0}) + \theta^2(t) (\vec{u}(t) \wedge \vec{\dot u}(t)) = \theta^2(t) (\vec{u}(t) \wedge \vec{\dot u}(t)) ,\\
>>\overrightarrow{v}(t) \wedge (\overrightarrow{v}(t) \wedge \overrightarrow{\dot{v}}(t)) & = & \theta^3(t) (\vec{u}(t) \wedge  (\vec{u}(t) \wedge \vec{\dot u}(t)))
>>\end{array}.
>>$$
>>Donc 
>>$$
>>\overrightarrow{\omega}(t) = \underbrace{\dot\theta(t)\vec{u}}_{\text{rotation autour de l'axe}} + \underbrace{\theta(t)\vec{\dot{u}}}_{\text{transport de l'axe}} + \underbrace{(1 - \cos(\theta(t)))(\vec{u}(t) \wedge \vec{\dot{u}}(t))}_{\text{correctrion géométrique}} + \underbrace{(\theta(t) - \sin(\theta(t)))(\vec{u}(t) \wedge ( \vec{u}(t) \wedge \vec{\dot{u}}(t) )}_{\text{terme non-linéaire}}.
>>$$
>>- terme $\dot\theta(t)\vec{u}(t)$ ,  $\vec{u}(t) $→ spin
>>- termes en $\theta(t)\vec{\dot u}(t)$ , $\vec{\dot u}(t)$˙ → **précession / nutation**
>>- termes trigonométriques → correction due à la géométrie de $\mathcal{SO}(3)$
>>
>>Et 
>>- $\overrightarrow{v}(t) = \theta(t)\vec{u}(t)$  vit dans un espace **linéaire**
>>- $\overrightarrow{\omega}(t)$ vit dans l’algèbre **tangent au groupe**
>>
>>👉 la différence = **courbure + non-commutativité**
>
>On note $ \overrightarrow{\Omega}_{\mathscr R'/\mathscr R} \equiv \overrightarrow{\omega}(t)$ la rotation de $\mathscr R'$ dans $\mathscr R$. Alors 
>$$
>\left. \frac{d \vec{e}_{i'}}{dt} \right )_{\mathscr R} = \overrightarrow{\Omega}_{\mathscr R'/\mathscr R} \wedge \vec{e}_{i'}.
>$$

#### 2. Dérivés temporelle d'un vecteur quelconque $\overrightarrow{A}$ dans le un référentiel $\mathscr R$

On écrit le vecteur 
$$
\overrightarrow{A} = a_{x'} \vec{e}_{x'} + a_{y'} \vec{e}_{t'} + a_{z'} \vec{e}_{z'}.
$$
Dans le référentiel $\mathscr R'$ la base $(\vec{e}_{x'},\vec{e}_{y'},\vec{e}_{y'} )$ est constante donc 
$$
\displaystyle \left.\frac{ d \overrightarrow{A} }{dt} \right)_{\mathscr R'} = \frac{ d a_{x'}}{d t } \vec{e}_{x'} + \frac{ d a_{y'}}{d t } \vec{e}_{y'} + \frac{ d a_{z'}}{d t } \vec{e}_{z'}.
$$
Donc 
$$
\begin{array}{rcl}
\displaystyle \left.\frac{ d \overrightarrow{A} }{dt} \right)_{\mathscr R} &= & \displaystyle \underbrace{\frac{ d a_{x'}}{d t } \vec{e}_{x'} + \frac{ d a_{y'}}{d t } \vec{e}_{y'} + \frac{ d a_{z'}}{d t } \vec{e}_{z'}}_{\displaystyle  \left.\frac{ d \overrightarrow{A} }{dt} \right)_{\mathscr R'}}  + \underbrace{a_{x'} \displaystyle \left.\frac{ d \vec{e}_{x'} }{dt} \right)_{\mathscr R} + a_{y'} \displaystyle \left.\frac{ d \vec{e}_{y')} }{dt} \right)_{\mathscr R} + a_{z'} \displaystyle \left.\frac{ d \vec{e}_{z')} }{dt} \right)_{\mathscr R}}_{\displaystyle \overrightarrow{\Omega}_{\mathscr R'/\mathscr R} \wedge \overrightarrow{A}} \\
& = & \displaystyle \left.\frac{ d \overrightarrow{A} }{dt} \right)_{\mathscr R'}  + \; \displaystyle \overrightarrow{\Omega}_{\mathscr R'/\mathscr R} \wedge \overrightarrow{A}.
\end{array}
$$
### 4. Cinématique

#### 1. Loi de composition des vitesses.


$$
\begin{array}{rcl}
\overrightarrow{v}_{\mathscr R}(M)  & \doteq &    \displaystyle  \left .\frac{d \overrightarrow{OM}}{dt} \right )_{\mathscr R} \\
& =  &  \displaystyle  \left .\frac{d \overrightarrow{OO'}}{dt} \right )_{\mathscr R} + \left .\frac{d \overrightarrow{O'M}}{dt} \right )_{\mathscr R} \\
 &=&   \displaystyle  \overrightarrow{v}_{\mathscr R}(O') + \left.\frac{ d \overrightarrow{O'M}}{dt}\right)_{\mathscr R}
\end{array}
$$

>[!tip]- Détails
>$$
>\begin{array}{rcl}
>\overrightarrow{v}_{\mathscr R}(M)  & \doteq &  \displaystyle  \left.\frac{ d \overrightarrow{o}_{\mathscr R}}{dt}\right)_{\mathscr R}(M) \\
>& = &  \displaystyle  \left .\frac{d \overrightarrow{OM}}{dt} \right )_{\mathscr R} \\
>& =  &  \displaystyle  \left .\frac{d \overrightarrow{OO'}}{dt} \right )_{\mathscr R} + \left .\frac{d \overrightarrow{O'M}}{dt} \right )_{\mathscr R} \\
>& = &  \displaystyle  \left.\frac{ d \overrightarrow{o}_{\mathscr R}}{dt}\right)_{\mathscr R}(O') + \left.\frac{ d \overrightarrow{o}_{\mathscr R'}}{dt}\right)_{\mathscr R}(M) \\
>&=&   \displaystyle  \overrightarrow{v}_{\mathscr R}(O') + \left.\frac{ d \overrightarrow{o}_{\mathscr R'}}{dt}\right)_{\mathscr R}(M)
>\end{array}
>$$


Dans le référentiel $\mathscr R'$ la base $(\vec{e}_{x'},\vec{e}_{y'},\vec{e}_{y'} )$ est constante donc 
$$
\displaystyle \left.\frac{ d \overrightarrow{O'M} }{dt} \right)_{\mathscr R'} = \frac{ d x'}{d t } \vec{e}_{x'} + \frac{ d y'}{d t } \vec{e}_{y'} + \frac{ d z'}{d t } \vec{e}_{z'}.
$$
Donc 
$$
\begin{array}{rcl}
\displaystyle \left.\frac{ d \overrightarrow{O'M} }{dt} \right)_{\mathscr R} &= & \displaystyle \underbrace{\frac{ d x'}{d t } \vec{e}_{x'} + \frac{ d y'}{d t } \vec{e}_{y'} + \frac{ d z'}{d t } \vec{e}_{z'}}_{\displaystyle  \left.\frac{ d \overrightarrow{O'M} }{dt} \right)_{\mathscr R'} = \; \overrightarrow{v}_{\mathscr R'}(M) }  + \underbrace{x' \displaystyle \left.\frac{ d \vec{e}_{x'} }{dt} \right)_{\mathscr R} + y' \displaystyle \left.\frac{ d \vec{e}_{y')} }{dt} \right)_{\mathscr R} + z' \displaystyle \left.\frac{ d \vec{e}_{z')} }{dt} \right)_{\mathscr R}}_{\displaystyle \overrightarrow{\Omega}_{\mathscr R'/\mathscr R} \wedge \overrightarrow{O'M}} \\
& = & \displaystyle  \overrightarrow{v}_{\mathscr R'}(M) + \displaystyle \overrightarrow{\Omega}_{\mathscr R'/\mathscr R} \wedge \overrightarrow{O'M}.
\end{array}
$$

On peut donc écrire que 
$$
\overrightarrow{v}_{\mathscr R}(M) = \overrightarrow{v}_{\mathscr R'}(M) + \overrightarrow{v}_{\mathscr R'/\mathscr R}^e(M) 
$$
avec  la **vitesse d'entraînement** :
$$
\overrightarrow{v}_{\mathscr R'/\mathscr R}^e(M) = \overrightarrow{v}_{\mathscr R}(O') + \overrightarrow{\Omega}_{\mathscr R'/\mathscr R} \wedge \overrightarrow{O'M}
$$
et 
$$
\overrightarrow{v}_{\mathscr R}(A) = \left . \frac{ d \overrightarrow{OA}}{dt} \right )_{\mathscr R} \quad \& \quad \overrightarrow{v}_{\mathscr R'}(A) = \left . \frac{ d \overrightarrow{O'A}}{dt} \right )_{\mathscr R'}.
$$



##### 1. Vecteur-rotation 

Un solide $(\mathscr S)$ est un ensemble de points tel que pour tout couple de ponts $(M,N)$ de $(\mathscr S)$, la distance $MN$ est indépendante du temps (pour solide indéformable). Cette contrainte forte lie les mouvements des différents points $M$ du solide dans un référentiel ($\mathscr R$).

(On fixe le solide dans un référentiel ($\mathscr R'$) si on veut faire un lient avec ce vus plus haut).

Il existe un unique vecteur $\overrightarrow{\Omega}_{\mathscr S / \mathscr R}$ appelé **vecteur-rotation-instantanée** du solide dans le référentiel ($\mathscr R$), tel que pour deux point $B$ et $A$ du solide on a la formule de $\mathsf{Varignon}$ :
$$
\overrightarrow{v}_{\mathscr S/ \mathscr R} (B) = \overrightarrow{v}_{\mathscr S/ \mathscr R}(A) + \overrightarrow{\Omega}_{\mathscr S / \mathscr R} \wedge \overrightarrow{AB},
$$
ce qui ressemble à la **vitesse d'entraînement**. Juste pour le mémothéchnique mon va retenir **"BABAR"** avec la réécriture 
$$
\overrightarrow{v}_{\mathscr S/ \mathscr R} (B) = \overrightarrow{v}_{\mathscr S/ \mathscr R}(A) +  \overrightarrow{BA} \wedge  \overrightarrow{\Omega}_{\mathscr S / \mathscr R}
$$
Ainsi, la rigidité d'un solide impose tellement de contraîntes sur le champ des vitesses $\overrightarrow{v}_{\mathscr S/ \mathscr R} (B)$ que ce champ est entièrement déterminé par la donnée du vecteur-vitesse $\overrightarrow{v}_{\mathscr S/ \mathscr R} (A)$ d'un de ces points $A$ et par le vecteur-rotation $\overrightarrow{\Omega}_{\mathscr S / \mathscr R}$ ; ainsi un solide a au plus $6$ degrés de liberté cinématiques : $3 $composantes de $\overrightarrow{v}_{\mathscr S/ \mathscr R} (A)$ et $3$ composantes de  $\overrightarrow{\Omega}_{\mathscr S / \mathscr R}$. 

Comme le champ des vitesses, le vecteur-rotation détend du temps et du référentiel ($\mathscr R$).

#### 2. Loi de composition des accélérations.

$$
\begin{array}{rcl}
\displaystyle \overrightarrow{a}_{\mathscr R}(O') & = & \displaystyle \left . \frac{ d \overrightarrow{v}_{\mathscr R}(O')}{dt} \right )_{\mathscr R}, \\
\displaystyle \left . \frac{ d \overrightarrow{v}_{\mathscr R'}(M)}{dt} \right )_{\mathscr R} & = & \displaystyle \underbrace{\left . \frac{ d \overrightarrow{v}_{\mathscr R'}(M)}{dt} \right )_{\mathscr R'}}_{\displaystyle \overrightarrow{a}_{\mathscr R'}(M)} + \overrightarrow{\Omega}_{\mathscr R' / \mathscr R} \wedge \overrightarrow{v}_{\mathscr R'}(M),
\end{array}
$$
De plus 
$$
\begin{array}{rcl}
\displaystyle \left . \frac{ d \overrightarrow{\Omega}_{\mathscr R'/\mathscr R}}{dt} \right )_{\mathscr R} & = & \displaystyle \left . \frac{ d \overrightarrow{\Omega}_{\mathscr R'/\mathscr R}}{dt} \right )_{\mathscr R'} + \underbrace{\overrightarrow{\Omega}_{\mathscr R'/\mathscr R} \wedge \overrightarrow{\Omega}_{\mathscr R'/\mathscr R}}_{0} \equiv \dot{\overrightarrow{\Omega}}_{\mathscr R'/\mathscr R},\\
\displaystyle \left . \frac{ d \overrightarrow{O'M}}{dt} \right )_{\mathscr R} & = & \underbrace{\displaystyle \left . \frac{ d \overrightarrow{O'M}}{dt} \right )_{\mathscr R'}}_{\displaystyle \overrightarrow{v}_{\mathscr R'}(M)} + \overrightarrow{\Omega}_{\mathscr R'/\mathscr R} \wedge \overrightarrow{O'M}.
\end{array}
$$
Donc 
$$
\begin{array}{rcl}
\displaystyle \left . \frac{d (\overrightarrow{\Omega}_{\mathscr R'/\mathscr R} \wedge \overrightarrow{O'M}) }{dt}\right )_{\mathscr R} & = & \dot{\overrightarrow{\Omega}}_{\mathscr R'/\mathscr R} \wedge \overrightarrow{O'M} + \overrightarrow{\Omega}_{\mathscr R' / \mathscr R} \wedge \overrightarrow{v}_{\mathscr R'}(M) + \overrightarrow{\Omega}_{\mathscr R' / \mathscr R} \wedge \left (\overrightarrow{\Omega}_{\mathscr R' / \mathscr R} \wedge \overrightarrow{v}_{\mathscr R'}(M) \right ).
\end{array}
$$
Donc 
$$
\begin{array}{rcl}
 \overrightarrow{a}_{\mathscr R'}(M)  & = & \displaystyle    \frac{ d ( \overbrace{\overrightarrow{v}_{\mathscr R'}(M) + \overbrace{ \overrightarrow{v}_{\mathscr R}(O') + \overrightarrow{\Omega}_{\mathscr R'/\mathscr R} \wedge \overrightarrow{O'M}}^{\overrightarrow{v}_{\mathscr R'/\mathscr R}^e(M)} }^{\overrightarrow{v}_{\mathscr R}(M)}) }{dt} \Bigg )_{\mathscr R} \\
  & = &   \displaystyle \overrightarrow{a}_{\mathscr R'}(M) + \underbrace{\overrightarrow{a}_{\mathscr R}(O') + \dot{\overrightarrow{\Omega}}_{\mathscr R'/\mathscr R} \wedge \overrightarrow{O'M}  + \overrightarrow{\Omega}_{\mathscr R' / \mathscr R} \wedge \left (\overrightarrow{\Omega}_{\mathscr R' / \mathscr R} \wedge \overrightarrow{v}_{\mathscr R'}(M) \right )}_{\displaystyle \overrightarrow{a}_{\mathscr R'/\mathscr R}^e(M)} + \underbrace{2 \overrightarrow{\Omega}_{\mathscr R' / \mathscr R} \wedge \overrightarrow{v}_{\mathscr R'}(M)}_{\displaystyle \overrightarrow{a}_{\mathscr R'/\mathscr R}^c(M)}
\end{array}
$$
