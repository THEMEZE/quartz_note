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


# Rappels de cinématique de solide

- un référentiel $\mathscr R \doteq ( O ; \vec{e}_x ,  \vec{e}_y , \vec{e}_z )$ ; repère cartésien, et on notera la base $\mathscr B = (\vec{e}_x ,  \vec{e}_y , \vec{e}_z )$; 
- un référentiel $\mathscr R' \doteq ( O' ; \vec{e}_{x'} ,  \vec{e}_{y'} , \vec{e}_{z'} )$ ; repère cartésien , mobile par rapport à $\mathscr R$.  Et on notera la base mobile $\mathscr B' = (\vec{e}_{x'} ,  \vec{e}_{y'} , \vec{e}_{z'} )$ par rapport à la base $\mathscr B$.

## Champ des vitesse d'un solide
### Vecteur Position 
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


### Vecteur Vitesse

>[!tip]- Caractère absolue du temps
>
>*En mécanique classique*, le temps est une quantité absolue, indépendante du référentiel :
>$$
>t' = t 
>$$

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


>[!question]- ${\displaystyle \frac{d \vec{e}_{i'} }{dt}(t) = ? }$
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
>>> \forall f , g \in \mathcal L ( E) \colon \forall x , y \in E \colon x \cdot ( f \circ g )^\ast ( y) = ( f \circ g )(x) \cdot y = g(x) \cdot f^\ast(y) = x \cdot (g^\ast \circ f^\ast )(y)
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
>Donc si on dérive par rapport à $t$
>$$
>\forall t \in \mathbb R \colon \forall f_t \in \mathcal{SO}(\mathbb R^3) \colon  \exist g_t \in \mathfrak{so}(\mathbb R^3), \dot{f}_t = \dot{g}_t \cdot \exp(g_t) = \dot{g}_t \cdot f_t ,
>$$
>avec 
>$$
>\dot{g}_t \colon \; \mathbb R^3 \rightarrow \mathbb R^3 \quad \overrightarrow{x} \mapsto \dot{\overrightarrow{v}}(t) \wedge  \overrightarrow{x}.
>$$
>En utilisant que $f_t \circ f_t^\ast = \text{id}_{\mathbb R^3}$, il vient que 
>$$
>\Omega_t \doteq \dot{f}_t\circ f_t^\ast = \dot{g}_t \circ  f_t^\ast \cdot f_t \circ  f_t^\ast  = \dot{g}_t \circ  f_t^\ast 
>$$
>
>et qu'il existe une $B_1(t)$ tel que 
>$$
>[u_t]_{B_1(t)} = 
>\left ( 
>\begin{array}{cc}
>\theta(t) J & 0_{2,1}\\
> 0_{1,2} & 0
>\end{array}
>\right )
>$$
>il exite une vecteur $\overrightarrow{\Omega}$ tel que $\Omega \overrightarrow{x} = \overrightarrow{\Omega} \wedge \overrightarrow{x}$ 
>$$
>\overrightarrow{\Omega}(t) = 
>\left ( 
>\begin{array}{c}
>\Omega_x \\ \Omega_y \\\Omega_z 
>\end{array}
>\right )
>\quad \Longleftrightarrow \quad 
>{\Omega}(t) =
>\left ( 
>\begin{array}{ccc}
>0 & -\Omega_x & \Omega_y \\ \Omega_z & 0 & - \Omega_z \\- \Omega_y & \Omega_x & 0 
>\end{array}
>\right )
>$$
>(cf  [[Mathématique/Algèbre/Algèbre#Exercice 5. (Exponentielle d'une matrice antisymétrique)|Exercice 5.3.5.5. (Exponentielle d'une matrice antisymétrique)]] ).
>avec  
>$$
>R(t)\in SO(3) \doteq \{  A \in \mathcal M_3(\mathbb R) \, \vert \, {~}^t A A = A \! {~}^t A = I_3 \}, 
>$$
>$$
>R(t_1+ t_2) = R(t_1)R(t_2)
>$$ 
>et 
>$$
>\vec{e}_i'(0) = R(\tau_0) \vec{e}_i(0)
>$$
>Donc 
>$$
>\frac{d \vec{e}_i'}{dt}(t) = \dot{R}(t) \vec{e}_i'(0) = \dot{R}(t)\! {~}^tR(t) \, \vec{e}_i'(t)
>$$
>
>>[!tip]- $\dot{R}(t)\! {~}^tR(t) \in \mathfrak{so}(3) = \{ A \in \mathcal M_3(\mathbb{R}) \;\mid\; {~}^tA = -A \} $.
>>
>>$R(t) \in SO(3)$ donc 
>>$$
>>R(t)\! {~}^t R(t) = I_3 
>>$$
>>donc en dérivant selon le temps il viens que :
>>$$
>>\dot{R}(t)\! {~}^t R(t) = - R(t)\! {~}^t\dot{R}(t) 
>>$$
>>er en transposant le membre de droite et en comparent le résultas avec le membre de droite,  il vient que 
>>$$
>>{~}^t(\dot{R}(t)\! {~}^t R(t)) = R(t)\! {~}^t\dot{R}(t) = -  \dot{R}(t)\! {~}^t R(t)
>>$$
>>Donc 
>>$$
>>\dot{R}(t)\! {~}^t R(t) \in \mathfrak{so}(3) = \{ A \in \mathcal M_3(\mathbb{R}) \;\mid\; {~}^tA = -A \}.
>>$$
>>
>Donc si on note 
>$$
>\Omega(t) \doteq \dot{R}(t)\! {~}^tR(t) 
>$$
>il exite une vecteur $\overrightarrow{\Omega}$ tel que $\Omega \overrightarrow{x} = \overrightarrow{\Omega} \wedge \overrightarrow{x}$ 
>$$
>\overrightarrow{\Omega}(t) = 
>\left ( 
>\begin{array}{c}
>\Omega_x \\ \Omega_y \\\Omega_z 
>\end{array}
>\right )
>\quad \Longleftrightarrow \quad 
>{\Omega}(t) =
>\left ( 
>\begin{array}{ccc}
>0 & -\Omega_x & \Omega_y \\ \Omega_z & 0 & - \Omega_z \\- \Omega_y & \Omega_x & 0 
>\end{array}
>\right )
>$$
>(cf  [[Mathématique/Algèbre/Algèbre#Exercice 5. (Exponentielle d'une matrice antisymétrique)|Exercice 5.3.5.5. (Exponentielle d'une matrice antisymétrique)]] ).
>
