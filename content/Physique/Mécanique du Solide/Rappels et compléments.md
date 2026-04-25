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


>[!question]- ${\displaystyle \frac{d \vec{e}_i' }{dt}(t) = ? }$
>
>$$
>\vec{e}_i'(t-t_0) = R(t-t_0) \vec{e}_i'(t_0) 
>$$
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
>(cf  [[Mathématique/Algèbre/Algèbre#Exercice 5. (Exponentielle d'une matrace antisymétrique)|Exercice 5. (Exponentielle d'une matrace antisymétrique)]] ).
>
