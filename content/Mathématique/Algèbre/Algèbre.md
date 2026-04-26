---
title: Algèbre
tags:
  - Science
---
# 1. Arithmétique, Groupes et Anneaux 

## 2. Groupes

### 1. Généralité 

>[!note]- Definition (Groupe $(G , \ast)$ )
>
>On appelle *groupe* un ensemble $G$ muni d'une loi interne $\ast$ telle que
>* (i) La loi $*$ est *associative* (*i.e.* $\forall x , y , z \in G \, \colon \, ( x \ast y ) \ast z = x \ast (y \ast z)$ )
>* (ii) Il exite un *élément neutre* $e$ (*i.e.* $ \exist e \, , \, \forall x  \in G \, \colon \, x \ast e  =e  \ast x = x $ )
>* (iii) Tout élémént a un *symétrique*  (*i.e.* $\forall x \in G \, \colon \, \exist y \in G \, , \,   x \ast y  = y \ast x = e $ )
>Si la loi $\ast$ est commutative, on parle de groupe *commutatif* (ou *abélien*).

>[!note]- Remarque ($e$ et $x^-1$ sont uniques)
>
>* L'élémént neutre $e$ de $(G,\ast)$ est unique.
>* Pour tout $x \in G$, $x$ a un unique symétrique, souvent noté $x^{-1}$ .

>[!note]- Definition (Sous-groupe $(H,\ast)$ de $(G,\ast)$ )
>
>Soit $(G, \ast)$ un groupe; on dit que la restriction de la loi $\ast$ à $H\subset G$ est un *sous-groupe* $(H , \ast)$de $(G , \ast)$  (*i.e.* $(H , \ast) \subset ( G , \ast )$) si la restriction de la loi $\ast$ à $H$ lui confère une structure de groupe. (*i.e.*
>$$
>\left \{ (G,\ast)\ \text{groupe} \right \} \, \&\,  \left \{ H \subset G \right \} \, \&\, \left \{ (H,\ast)\ \text{groupe} \right \}   \Longrightarrow (H,\ast)\ \text{sous-groupe de}\ (G,\ast)
>$$
>)

>[!info]- Proposition 
>
>Soit $(G,\ast)$ un *groupe* et $H \subset G$. L'ensemble $H$ forme un *sous-groupe* $(H , \ast)$ de $(G,\ast)$ *si et seulement si* $H \neq \emptyset$ et pour tout couple $(x, y) \in H^{-1}$ on a $x \ast y^{-1} \in H$.

>[!done]-  Critère standard (le bon à retenir)
>
>On utilise en pratique :
>$$
>H \neq \varnothing \quad \text{et} \quad \forall x,y \in H,\; x \ast y^{-1} \in H
>$$
>
>👉 Cela suffit pour garantir que :
>
>*    $e \in H$ 
>*    $x^{-1} \in H$ 
>*    $x \ast y \in H$ 
>
>Donc  $H$  est automatiquement un groupe pour la loi induite.

>[!info]- Proposition ($\bigcap \text{sous-groupe}$)
>Une *intersection* de *sous-groupes* d'un groupe $G$ est un *sous-groupe* de $G$.

>[!note]- Definition (*Centre de $(G,\ast)$ , $\mathcal Z((G,\ast))$*)
>Soit $(G, \ast)$ un groupe. On appelle *centre* de $(G,\ast)$, noté $\mathcal Z((G,\ast))$, l'ensemble des éléments de $G$ commutant avec les éléments de $G$.
>$$
>\mathcal Z((G,\ast)) \doteq \{ x \in G \, \vert \, \forall y \in G \, \colon \,  x \ast y = y \ast x\}
>$$
>L'ensemble  $\mathcal Z((G,\ast))$ est un sous-groupe de $(G,\ast)$.

>[!tip]- Style Bourbaki / catégorie ($(G,\ast,e,(\cdot)^{-1})$)
>
>Oon peux reformuler en version “algèbre abstraite propre” (style Bourbaki / catégorie), ou montrer comment ça s’interprète en termes de monoïdes et foncteurs.
>
>Passons à une formulation propre, de niveau **algèbre structurale / catégorique**.
>
>>[!abstract]- 1. Cadre bourbachique (structures)
>>
>>On travaille dans la catégorie des ensembles munis d’une loi :
>>
>>$$
>>(G,\ast,e,(\cdot)^{-1})
>>$$
>>
>>est un **objet de la théorie des groupes**.
>>
>>Soit  $H \subset G$ . On considère l’**inclusion ensembliste** :
>>
>>$$
>>i : H \hookrightarrow G
>>$$
>>
>>>[!note]- Définition (sous-groupe, version structurelle)
>>>
>>> $H$  est un **sous-groupe** de  $G$  si :
>>>
>>>*    $H$  est muni de la **structure induite** par  $G$ , i.e. :
>>>    $$
>>>    \ast_H := \ast|_{H \times H}
>>>    $$
>>>*   et l’inclusion
>>>    $$
>>>    i : (H,\ast_H) \to (G,\ast)
>>>    $$
>>>    est un **morphisme de groupes**.
>>
>>
>>>[!success]- Traduction explicite
>>>
>>>Cela équivaut à dire que  $H$  est **stable par les opérations structurelles** :
>>>
>>>$$
>>>\begin{cases} \forall x,y \in H,\quad x \ast y \in H \\ \forall x \in H,\quad x^{-1} \in H \\ e \in H \end{cases}
>>>$$
>>>
>>>Autrement dit :
>>>
>>>$$
>>>H \ \text{est un sous-objet de } G \text{ dans la catégorie des groupes.}
>>>$$
>>
>
>>[!note]- 2. Reformulation catégorique
>>
>>Dans la catégorie **Grp** :
>>
>>*   les **objets** : groupes
>>*   les **morphismes** : homomorphismes de groupes
>>
>>
>>>[!tip]- Sous-groupe = sous-objet
>>>
>>>Un sous-groupe de  $G$  est un **sous-objet** :
>>>
>>>$$
>>>(H, i) \quad \text{avec} \quad i : H \rightarrow G
>>>$$
>>>
>>>où :
>>>
>>>*    $i$  est un **monomorphisme** dans **Grp**
>>>*   i.e. un morphisme injectif (dans Grp, mono ⇔ injectif)
>>
>>
>>>[!todo]- Condition intrinsèque
>>>
>>>
>>>On peut caractériser  $H$  sans mention explicite de structure :
>>>
>>>$$
>>>H \subset G \text{ est un sous-groupe } \iff \text{le diagramme suivant se factorise}
>>>$$
>>>
>>>pour les lois :
>>>
>>>$$
>>>\ast : G \times G \to G
>>>$$
>>>
>>>il existe :
>>>
>>>$$
>>>\ast_H : H \times H \to H
>>>$$
>>>
>>>tel que :
>>>
>>>$$
>>>i(x \ast_H y) = i(x) \ast i(y)
>>>$$
>>
>
>>[!note]- 3. Version ultra-condensée (style Bourbaki pur)
>>
>>
>>$$
>>H \subset G \ \text{est un sous-groupe} \iff H \ \text{est stable par les opérations définissant la structure de groupe.}
>>$$
>>
>>ou encore :
>>
>>$$
>>H \ \text{est une sous-structure de } G
>>$$
>>
>
>
>>[!note]- 4. Lecture de ton implication initiale
>>
>>
>>Tu écrivais :
>>
>>$$
>>(G,\ast)\ \text{groupe},\quad H \subset G,\quad (H,\ast)\ \text{groupe}
>>$$
>>
>>👉 En langage catégorique :
>>
>>*   tu supposes déjà que  $H$  est un **objet de Grp**
>>*   et que l’inclusion est compatible à la loi
>>
>>Donc :
>>
>>$$
>>i : H \to G \ \text{est automatiquement un morphisme}
>>$$
>>
>>⇒  $H$  est déjà un **sous-objet**
>>
>>👉 Ton implication devient :
>>
>>$$
>>\text{“objet + inclusion compatible”} \Rightarrow \text{sous-objet}
>>$$
>>
>>qui est **tautologique** dans ce cadre.
>>
>
>
>>[!note]- 5. Insight conceptuel (important)
>>
>>
>>La bonne notion n’est pas “être un groupe à part”, mais :
>>
>> être **fermé sous les opérations de la structure ambiante**
>>
>>C’est exactement la notion générale de :
>>
>>*   **sous-algèbre**
>>*   **sous-objet**
>>*   **structure induite**
>>
>
>
>>[!note]- 6. Généralisation immédiate
>>
>>
>>Même schéma pour toute théorie algébrique :
>>
>>*   anneaux → sous-anneaux
>>*   espaces vectoriels → sous-espaces
>>*   algèbres → sous-algèbres
>>
>>👉 Toujours :
>>
>>$$
>>\text{stabilité sous les opérations} \;\Longleftrightarrow\; \text{sous-objet}
>>$$
>>
>

>[!warning]- Notation Abusive. On dit souvent que $G$ est un groupe au lien de préciser  $(G , \ast )$, sous entendant que "l'ensemble $G$ muni d'un lois interne notée "$\ast$" est un groupe"  
> 

## 3. Anneaux

### 1. Définitions

>[!note]- Definition (Anneaux $(A , + ,  \cdot )$ )
>Soit $A$ un ensemble muni de deux lois internes notées "$+$" et "$\cdot$". On dit que $(A,+,\cdot)$ est un *anneau* si :
>* (i) $(A,+)$ est un *groupe abélien*,
>* (ii) la loi "$\cdot$" est *associative*,
>* (iii) la loi "$\cdot$" est *distributive* par rapport à la loi "$+$".
>
>Si la loi "$\cdot$" admet un élément neutre, on parle d'anneau *unitaire*; si la loi "$\cdot$" est commutative on parle d'anneau *commutatif*: un élément de $A$ est dit *inversible* s'il l'est pour la loi "$\cdot$".

>[!note]- Notation. "$0$" : élément neutre de "$+$" et "$e$" ou "$1$" : élément neutre de "$\cdot$".
>
>- Le neutre de la loi "$+$" est souvent noté "$0$",
>- celui de la loi "$\cdot$" est noté "$1$" (ou "$e$").

>[!note]- Definition (Diviveur de $A$ )
>Soit l'anneau $(A,+,\cdot)$. Un élément $a$ de $A$ est dit *diviseur* de $0$ à droite (resp. à gauche) si $a\neq 0$ et s'il existe $b\neq 0$ tel que $a\cdot b = 0$ (resp. $b \cdot a = 0$).

>[!note]- Definition (Anneau intègre )
>Un anneau $(A,+,\cdot)$ est dit *intègre* s'il est sans diviseur de zéro, autrement dit si $(a\neq 0, b\neq 0 \Rightarrow a\cdot b \neq 0)$.

>[!note]- Definition (Élément nilpotent d'un anneau )
>Soit l'anneau $(A,+,\circ)$. Un élément $a \in A$ est dit *nilpotent* s'il existe un entier naturel non nul $n$ tel que $a^n \equiv \underbrace{ a \circ \cdots \circ a }_{n \text{ termes}} = 0$. *L'indice ( ou l'ordre) de nilpotence* de $a$ est le plus petit entier naturel non nul $n$ tel que $a^n = 0$.

>[!note]- Definition (Sous-anneau $(B, + , \ast)$ de $(A, + , \ast)$ )
>Soient $(A, + , \ast)$ un anneau et une sous-ensemble $B subset A$ de $A$. Si $(B, + , \ast)$ est un anneau alors  $(B, + , \ast)$ est un *sous-anneau* de $(A, + , \ast)$.

>[!example]-
>- $(\mathbb Z , + ,  \cdot)$ est est un *anneau unitaire intègre*
>- $(\mathbb Z/8\mathbb Z , + , \cdot)$ est un *anneau non intègre* ($\dot{2}\cdot\dot{4}=\dot{0}$), dans lequel $\dot 2$ est *nilpotent d'indice $3$*.
>- L'ensemble des matrices carrées $\mathcal M_n(\mathbb R)$, muni des opérations classiques d'addition et de multiplication des matrices, est un *anneau unitaire non intègre*.

>[!warning]- Notation Abusive. On dit souvent que $A$ est un anneau au lien de préciser  $(A , + ,  \cdot )$, sous entendant  que "l'ensemble $A$ muni de deux lois internes notées "$+$" et "$\cdot$ est un anneau"  
> 
>Exemple on va dire :
>- $\mathbb Z$ est est un *anneau unitaire intègre*
>- $\mathbb Z/8\mathbb Z$  est un *anneau non intègre*  ($\dot{2}\cdot\dot{4}=\dot{0}$), dans lequel $\dot 2$ est *nilpotent d'indice $3$*.
### 2. [[Idéal|Idéaux]]

>[!note]- Definitions (Idéal "gauche"/ "droite" / "bilatère")
>Soit $I \subset A$. On dit que $(I,+,\cdot)$ est *idéal gauche* (resp. *droit*) de l'anneau $(A,+,\cdot)$ si 
>- (i) $(I,+)$ est un *sous-groupe additif* de $(A,+)$.
>- (ii) $\forall (x , a) \in I \times A \, \colon \, a \cdot x \in I \; (\text{resp. } x \cdot a \in I)$
>
>On dit que $(I,+,\cdot)$ est un *idéal* ou *idéa "bilatère"* s'il est *idéa "gauche"*  et *idéa "droite"*.

>[!note]- Remarques
>- Un *idéal* est un *sous-anneau*.
>- La notion d'*idéal* est en quelque sorte l'*analogue* pour les *anneaux* de la notion de *sous-groupe distingué*. En revanche, la notion de *sous-anneau* est beaucoup *moins utilisée* que la notion de *sous-groupe*.
>- Si l'*anneau* $(A,+,\cdot)$ est *commutatif* et si $x \in A$, l'ensemble $x \cdot A \equiv\{ x \cdot a , a \in A \}$ constitue un *idéal* $(x \in A , + , \cdot)$ de $(A,+,\cdot)$.
>- Si $(A,+,\cdot)$ est un *anneau unitaire* et si $1\in I$ où $(I , + , \cdot)$ est un idéal de $(A , + , \cdot)$, la propriété *(ii)* d'un idéal entraîne que $I = A$. Si un $(I , + , \cdot)$ de $(A , + , \cdot)$ possède un élément inversible $x$ de $A$, alors $1 = x^{-1} \cdot x \in I$ d'après *(ii)* et donc $I=A$.
>- Lorsque $(A, + , \cdot)$ est un anneau, $I\subset A$ vérifie *(i)* et vérifie seulement $a \cdot x  \in I$ ( resp.  $x \cdot a \in I$) pour tout $(x,a) \in I \times A$, on dit qie $I$ est un idéal à *gauche* (resp. à *droite*) de $(A,+,\cdot)$. Si $(I,+,\cdot)$ est à la fois *ideal à gauche* et *idéal à droite* de $(A,+,\cdot)$, $(I,+,\cdot)$ est donc un *idéal* de $(A,+,\cdot)$ (on précise parfois en disant que $(I,+,\cdot)$ est un *idéal bilatère*).

>[!note]- Proposition 
>Un *intersection  d'idéaux* de $(A,+,\ast)$ est un *idéal* de $(A,+,\ast)$. Une *somme finie d'idéaux* de $(A,+,\ast)$ est un *idéal*  de $(A,+,\ast)$.

>[!note]- Definitions (Idéal / Anneau principal)
>Soit $(A,+,\ast)$ un anneau *commutatif*. Un idéal $(I,+,\ast)$ de $(A,+,\ast)$ est dit *principal* s'il existe $x \in A$ tel que $I = x \cdot A$. On note alors $I = (x)$.
>L'anneau $(A,+,\ast)$ est dit *principal* s'il est *commutatif*, *unitaire*, *intègre* et si tous les idéaux de $(A,+,\ast)$ sont *principaux*.

>[!example]-
>Les anneaux $(\mathbb Z , + , \ast)$ et $(\mathbb R[X] , + , \cdot)$ sont *principaux*.

>[!warning]- Notation Abusive. On dit souvent que $I$ est un idéal de l'anneau $A$ au lien de préciser  $(I , + ,  \cdot )$ est un idéal de  $(A , + ,  \cdot )$, sous entendant  que "l'ensemble $I$  muni de deux lois internes notées "$+$" et "$\cdot$ est un idéal de l'anneau $(A , + ,  \cdot )$".  
> 

# 2. Corps, polynômes et fractions rationnelles

## 1. Corps, polynômes et arithmétiques dans $\mathbb K[X]$

### 1. Corps

>[!note]- Definition (Corps $(\mathbb K , + ,  \cdot )$ )
>Soit $\mathbb K$ un ensemble muni de deux lois internes notées "$+$" et "$\cdot$". On dit que $(\mathbb K,+,\cdot)$ est un *corps* si :
>* (i) $(\mathbb K,+)$ est un *groupe abélien*,
>* (ii) $(\mathbb K^\ast,\cdot)$ est un *groupe*,
>* (iii) la loi "$\cdot$" est *distributive* par rapport à la loi "$+$".
>

>[!note]- Remarques
>- Si la lois "$\cdot$" est *commutative*, on parle de *corps commutatif*.
>- Il revient au même de dire qu'un corps est un anneau dans leuel tout élément non-nul est inversible
>- Les corps les plus couramment rencontrés sont $\mathbb Q$, $\mathbb R$, $\mathbb C$ et $\mathbb Z/p\mathbb Z$ ($p$ premier)  muni de deux lois internes notées "$+$" et "$\cdot$".

>[!note]- Definition (Sous-corps $(\mathbb K , + ,  \cdot )$ de $(\mathbb L , + ,  \cdot )$ )
>Soit $(\mathbb L , + ,  \cdot )$ un corps et $\mathbb K \subset \mathbb L$. On dit que $(\mathbb K , + ,  \cdot )$ est un *sous-corps* de $(\mathbb L , + ,  \cdot )$ si la restriction à $\mathbb K$ des lois $+$ et $\cdot$ lui confère un structure de corps (on dit aussi que $(\mathbb L , + ,  \cdot )$) est un *sur-corps* ou une *extension* de $(\mathbb K , + ,  \cdot )$).

>[!note]- Remarque
>Si $(\mathbb K , + ,  \cdot )$ est un *sous-corps commutatif* de $(\mathbb L , + ,  \cdot )$, $\mathbb L$ est un $\mathbb K$-espace vectoriel.


>[!warning]- Notation Abusive. On dit souvent que $\mathbb K$ est un corps au lien de préciser  $(\mathbb K , + ,  \cdot )$, sous entendant  que "l'ensemble $\mathbb K$ muni de deux lois internes notées "$+$" et "$\cdot$ est un corps"  
> 
>Exemple on va dire :
>- $\mathbb Q$, $\mathbb R$, $\mathbb C$ et $\mathbb Z/p\mathbb Z$ ($p$ premier) sont des corps.


## 5. Problèmes

### Problème 4 (Théorème Fondamental de l'algèbre).

# 4. Réduction d'endomorphismes

## 3. Topologie sur endomorphisme

### 4. Exercices

#### Exercice 2. (Déterminant d'exponentielle d'une matrice)

>[!question]- a) Soit $n \in \mathbb N^\ast$ et $A \in \mathcal M_n ( \mathbb C)$. Montrer que $ \det(\exp (A)) = \exp( \text{tr} (A))$.
>
>>[!success]+ Solution 
>>
>>Le corps $\mathbb C$ étant algébriquement clos, on peut trigonaliser la matrice $A$, donc 
>>$$
>>\exist P \in \mathcal G\ell_n (\mathbb C), \quad A = P^{-1} T P \; \text{avec} \; T = 
>>\left ( 
>>\begin{array}{cccc}
>>\lambda_1 & \times & \cdots & \times \\
>>0  & \lambda_2 & \ddots & \vdots \\
>>\vdots & \ddots & \ddots & \times \\
>>0 & \cdots & 0 & \lambda_n 
>>\end{array}
>>\right ).
>>$$
>>La matrice $T^k$ est une matrice triangulaire supérieur dont les coefficients diagonaux sont les $\lambda_i^k$, donc
>>$$
>>\exp(T) = \sum_{k = 0}^{+\infty} \frac{1}{k!} M^k = \sum_{k = 0}^{+ \infty } \frac{1}{k!} 
>>\left ( 
>>\begin{array}{cccc}
>>\lambda_1^k & \times & \cdots & \times \\
>>0  & \lambda_2^k & \ddots & \vdots \\
>>\vdots & \ddots & \ddots & \times \\
>>0 & \cdots & 0 & \lambda_n^k 
>>\end{array}
>>\right )
>>= 
>>\left ( 
>>\begin{array}{cccc}
>>e^{\lambda_1} & \times & \cdots & \times \\
>>0  & e^{\lambda_2} & \ddots & \vdots \\
>>\vdots & \ddots & \ddots & \times \\
>>0 & \cdots & 0 & e^{\lambda_n} 
>>\end{array}
>>\right ).
>>$$
>>Ceci entraîne 
>>$$
>>\det(\exp (T)) =  \prod_{i = 1}^n e^{\lambda_i} = \exp \left (  \sum_{i = 1}^n \lambda_i \right ) =  \exp( \text{tr} (T)
>>$$
>>Comme $A$ et $T$ sont semblables, il en est de même de $\exp(A)$ et $\exp(T)$, et on en déduit 
>>$$
>>\det(\exp (A)) = \det(\exp (T)) =  \exp( \text{tr} (T) =  \exp( \text{tr} (A).
>>$$

>[!question]- b) Soit $M \in \mathcal M_n (\mathbb R )$. Montrer que si $M$ est l'exponnentielle d'une matrice réelle, alors $\det(M) > 0 $. Montrer que la réciproque est fausse.
>
>>[!tip]- Indication 
>>
>>Montrer que la matrice $M = { \criptstyle \left ( \begin{array}{cc} -1 & +1 \\ 0 & -1  \end{array} \right ) }$ n'est pas un carré .
>
>>[!success]- Solution 
>>
>>Si $M =  \exp(A)$ avec $A \in \mathcal M_n ( \mathbb R )$, alors on a $\det(M) = \exp ( \text{tr}(A))$ d'après le résultat précédent, donc $\det(M) > 0$ car $\text{tr}(A)$ est un nombre réel. La réciproque est fausse, comme le montre le contre-exemple de la matrice $M = { \scriptstyle \left ( \begin{array}{cc} -1 & +1 \\ 0 & -1  \end{array} \right ) }$. Si $M$ était l'exponentielle d'une matrice réelle $A$. La matrice réelle $N = \exp( \tfrac{1}{2} A)$ vérifirait $N^2 = \exp(A) = M$. Or ceci est impossible car en écrivant $ N = { \scriptstyle \left ( \begin{array}{cc} a & b \\ c & d  \end{array} \right ) }$, on aurait 
>>$$
>>M = 
>>\left ( 
>>\begin{array}{cc}
>>-1 & +1 \\
>>0  & -1 \\ 
>>\end{array}
>>\right )
>>= N^2 =
>>\left ( 
>>\begin{array}{cc}
>> a^2 + bc  & ab + bd  \\
>> ac + dc   & cb + d^2  \\ 
>>\end{array}
>>\right ).
>>$$
>>Ceci entraîne $1 = b(a+d)$, donc $a + d$ est non nul. Les termes inférieurs gauches donnent $ 0 = c ( a + d )$, donc $c = 0 $. L'égalité de termes diagonaux donneraient alors $a^2 = -1$ et $d^2 = -1$, ce qui est impossible puisque $a$ et $d$ sont des nombre réels. Ainsi, la matrice $M$ a bien un déterminant positif (on a $\det(M) = 1 $ ) mais cette matrice réelle n'est pas l'exponentielle d'une matrice réelle.

>[!tip]- Remarque.
>On peut montrer qu'une matrice réelle est l'exponentielle d'une matrice réelle si et seulement si elle est le carré d'une matrice réelle inversible.
>- Toute matrice complexe inversible est l'exponentielle d'une matrice complexe ( voir l'[[Mathématique/Algèbre/Algèbre#Exercice 5. (Logarithme d'une matrice inversible)|Exercice 4.4.4.5. (Logarithme d'une matrice inversible)]] )

## 4. Sous-Espace caractéristiques - Réduction de Jordan

### 4.  Exercices

#### Exercice 5. (Logarithme d'une matrice inversible)


# 5. Espaces Euclidiens 

## 2. Espaces Préhilbertiens

### 1. Généralités 

### 2. Orthogonalité

### 3. Isométries et endomorphismes unitaires

#### Propriétés matricielles des isométries et des endomorphismes unitaires.

### 4. Endomorphismes adjoints


## 3. Compléments de cours 

Cette section propose quelque études complémentaires très classiques, et souvent utiles dans les exercices ou les problèmes.

### 1. Réduction des isométries et des endomorphisme unitaires

Nous allons voir que les isométries (resp. les endomorphismes unitaires), bien que n'étant pas des endomorphismes autoadjoints, peuvent se réduire de manière intéressante dans  une base orthonormale. Nous commençons par les isométries.

>[!info]- Proposition 1. Soit $E$ un espaace euclidien (rest. hermitien) et $u \in \mathcal L(E)$ une isométrie (resp. un endomorphisme unitaire). Si $F$ est un s.e.v de $E$ stable par $u$, alors $F^\perp$ est stable par $u$.
>
>>[!success]+ Démonstration.
>>
>>Il s'agit de montrer que pour tout $x \in F^\perp$ et pour tout $y \in F, \, u(x) \cdot y = 0$. Comme $u_{\vert F}$ est un isométrie,  $u_{\vert F}$ est bijective ( on est en dimension finie), donc il existe $y' \in F$ tel que $y \in u(y')$. On a maintenant
>>$$
>>u(x) \cdot y = u(x) \cdot u(y') = x \cdot y' = 0.
>>$$
>>Ceci étant vrai pour tout $x \in F^\perp$ et pour tout $y \in F$, $ F^\perp$ est bien stable par $u$.

#### Réduction des isométries

>[!info]+ Théorème 1.
>Soit $E$ un espace euclidien et $u \in \mathcal L(E)$ une isométrie. Alors il existe une base orthonormale $B$ de $E$ dans laquelle la matrice de $u$ à la forme par blocs
>$$
>[u]_B = 
>\left (
>\begin{array}{cccccc}
>R(\theta_1) & 0_2 & \cdots & \cdots & \cdots & 0_2 \\
>0_2& \ddots & \ddots  & 0 & 0 & \vdots \\
>\vdots & \ddots & R(\theta_r) & \ddots & 0  & \vdots \\
>\vdots & 0 & \ddots & \varepsilon_1 & \ddots & \vdots \\
>\vdots & 0 & 0  & \ddots & \ddots & 0 \\
>0 & \cdots & \cdots &  \cdots &  0 & \varepsilon_s
>\end{array}
>\right ),
>\tag{$\ast$}
>$$
>où pour tout $j, \varepsilon_j \in \{ - 1 , + 1 \}$ et pour tout $i$, 
>$$
>R(\theta_i) =
>\left ( 
>\begin{array}{cc}
>\cos \theta_i & - \sin \theta_i \\
>\sin \theta_i & \cos \theta_i 
>\end{array}
>\right)
>\in \mathcal M_n ( \mathbb R),  \quad 
>\text{avec}\quad 
>\theta_i \in \mathbb R, \; \theta_i \not\equiv 0 \quad  (\text{mod } \pi ). 
>$$
>>[!success]- Demonstration.
>>
>>On procède par récurrence sur $n = \dim E$. Pour $n = 1$, c'est évident. Suposons le résultat vrai jusqu'au rang $n-1$ et montrans le au rang $n$.  Nous traitons deux cas .
>>
>>> *Premier cas*. L'isométrie $u$ admet au moins une valeur propre réelle $\varepsilon$. Soit $x$ un vecteur propre normé associé. Comme $\Vert u(x) \Vert = \Vert \varepsilon x \Vert = \vert \varepsilon \vert \Vert x \Vert$ et  $\Vert u(x) \Vert = \vert \Vert x \Vert$, on a $\vert \varepsilon \vert = 1$. De plus $\varepsilon \in \mathbb R$, on en déduit $\varepsilon \in \{ - 1 , + 1 \}$. Maintenant, comme $F = \text{Vect}(x)$ est stable par $u$, $F^\perp$ est stable par $u$ d'après la [[Mathématique/Algèbre/Algèbre#1. Réduction des isométries et des endomorphisme unitaires|Proposition 5.3.1.1]] . En appliquant l'hypothèse en récurrence à $u_{\vert F^\perp}$, on trouve une base orthonormale $B_0$ de $F^\perp$ dans laquelle la matrice de $u_{\vert F^\perp}$ à la forme $(\ast)$. En ajoutant $x$ à la base $B_0$, on obtient une base orthonormale $B$ de $E$ dans laquelle la matrice de $u$ a la forme $(\ast)$.
>>
>>>*Second cas*.  L'isométrie $u$ n'a aucune valeur propre réelle. On considère l'endomorphisme $v = u + u^\ast$. Comme $v$ est symétrique, $v$ admet une valeur propre réelle$\lambda$ associée à un vecteur propre $x$. On a $(u + u^\ast)(x) = \lambda x$ donc $u ( u + u^\ast )(x) = u^2 (x) + x  = \lambda u(x)$, d'où 
>>>$$
>>>u^2(x) = \lambda u(x) - x. \tag{$\ast \ast$}
>>>$$
>>>Par ailleurs, la famille $(x , u(x))$ est libre puisque $u$ n'admet pas de valeur propre réelle. En posant $F = \text{Vect} ( x , u (x))$, on voit que $\dim F = 2$ et que $F$ est stable par $u$ (d'après $(\ast \ast)$). Soit $ N = {\scriptscriptstyle \left ( \begin{smallmatrix}  a & c \\ b & d \end{smallmatrix}  \right )}$ la matrice de $u_{\vert F}$ dans une base orthonormale $B_0$ de $F$. Comme $u_{\vert F}$ est une isométrie, $N^\ast N = I_n = N N^\ast$. Parmi les équations issues de ces égalités, on trouve
>>>$$
>>>a^2 + b^2 = a^2 + c^2 = 1 \quad \text{et} \quad ab + cd = 0. \tag{$\ast \ast \ast$}
>>>$$
>>>La première assertion de $(\ast \ast \ast)$ entraîne $c = \pm b$. On ne peut pas avoir $c = b$ car $N$ serait symétrique ce qui est impossible vu que $u$ n'abmet pas de valeur propre réelle. Donc $c = -b \neq 0$, et d'après la deuxième assertion de $(\ast \ast \ast)$ on en déduit $d = a$. Comme de plus $a^2 + b^2  =1 $ , il existe $\theta \in \mathbb R$ tel que $a = \cos \theta$ et $b = \sin \theta$ ( et $\theta \not\equiv 0 \; ( \text{mod } \pi)$ car $b \neq 0$). Finalement, la matrice $N$ est de la forme 
>>>$$
>>>R(\theta) = 
>>>\left ( 
>>>\begin{array}{cc}
>>>\cos \theta & - \sin \theta \\
>>>\sin \theta & \cos \theta 
>>>\end{array}
>>>\right ), \quad 
>>>\theta \in \mathbb R \backslash \pi \mathbb Z.
>>>$$
>>>Maintenant, d'après la [[Mathématique/Algèbre/Algèbre#1. Réduction des isométries et des endomorphisme unitaires|Proposition 5.3.1.1]]  le s.e.v $F^\perp$ est stable par $u$, et $u_{\vert F^\perp}$ est une isométrie donc il existe d'après l'hypothèse de récurrence une base orthonormale $B_1$ de $F^\perp$ qui diagonalise  $u_{\vert F^\perp}$. La base $B$ obtenue en concaténant $B_0$ et $B_1$ est orthonormale et dans cette base, la matrice de $u$ a la forme voulue, d'où le théorème.

>[!info]- Remarque 1.
>
>On retrouve ainsi la forme des isométries du plan et de l'espace :
>- Les isométrie directes du plan sont des **rotations** d'angle $\theta$ ( elles ont pour matrice $R(\theta) = {\scriptscriptstyle  \left(\begin{smallmatrix}  \cos\theta & -\sin\theta \\  \sin\theta & \cos\theta  \end{smallmatrix}\right)}$ ),  les isométries indirectecte des symétries par rapport à des droites ( matrice ${\scriptscriptstyle  \left(\begin{smallmatrix}  1 & 0 \\  0 & -1  \end{smallmatrix}\right)}$ ) . Notez d'ailleurs la relation $R(\theta)R(\theta') = R(\theta + \theta')$ qui entraîne la commutativité des rotation dans le plan.
>- Les isométrie directes de l'espace sont des **rotations** d'angle $\theta$ autour d'un axe  ( matrice ${\scriptscriptstyle  \left(\begin{smallmatrix}  \cos \theta  & - \sin \theta & 0  \\  \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1  \end{smallmatrix}\right)}$, le l'espace vecteur de la base étant l'axe de rotation ) . Lorsque $\theta = \pi$, on parle de *retournement*. Les isometries indirectes de l'espace ont pour matrice ${\scriptscriptstyle  \left(\begin{smallmatrix}  \cos \theta  & - \sin \theta & 0  \\  \sin \theta & \cos \theta & 0 \\ 0 & 0 & -1  \end{smallmatrix}\right)}$. Lorsque $\theta = 0$, on a affaire à une symétrie par rapport à un plan et on parle alors de *réflexion*.

>[!info]- Remarque 2.
>
>La version matricielle de ce théorème est la suivante. Soit $M \in \mathcal  M_n(\mathbb R)$ une matrice orthonormale. Alors il existe une matrice orthonormale $P$ telle que $P^{-1} M P = P^\ast M P$ ait la forme $(\ast)$.

#### Réduction des endomorphismes unitaires.

>[!info]+ Théorème 2.
>
>Soit $E$ un espace hermitien et $u \in \mathcal (E)$ un endomorphisme unitaire. Alors il existe une base orthonormale qui diagonalise $u$, et toutes les valeurs propres de $u$ ont leur module égal à $1$.
>
>>[!success]- Démonstration.
>>
>>La preuve est plus simple que la précédente. Il est d'abord claire que toute valeur propre $\lambda$ de $u$ vérifie $\vert \lambda \vert = 1$, car si $u(x) = \lambda x$ avec $x \neq 0$, on a $\Vert x \Vert = \Vert u(x) \Vert = \vert \lambda \vert \Vert x \Vert$. On procède ensuite par récurrence sur $n = \dim E$. Le cas $n = 1$ est immédiat, et le passage du rang $n-1$ au rang $n$ se fait comme suit.
>>
>>Le corps de base $\mathbb C$ étant algébriquement clos, $u$ admet au moins une valeur propre complexe $\lambda$. Soit $x$ un vecteur propre associé, $\Vert x \Vert = 1$. La droite $F = \text{Vect}(x)$ est stable par $u$, donc d'après la [[Mathématique/Algèbre/Algèbre#1. Réduction des isométries et des endomorphisme unitaires|Proposition 5.3.1.1]], l'hyperplan $F^\perp$ est également stable une base orthonormale $B_0$ de $F^\perp$ qui diagonalise $u_{\vert F^\perp}$. En ajoutant $x$ à $B_0$, on obtient une base orthonormale de $E$ qui diagonalise $u$ et le théorème est prouvé.

>[!info]+ Corolaire 1 (Version matricielle). Soit $U \in \mathcal M_n(\mathbb C)$ une matrice unitaire. Alors il existe matrice unitaire $P$ telle que 
>$$
>P^{-1} U P = P^\ast U P = 
>\left (
>\begin{array}{cccc}
>e^{i \theta_1} & 0 &  \cdots  & 0 \\
>0 & e^{i \theta_2}& \ddots  &  \vdots  \\
>\vdots & \ddots & \ddots & 0  \\
>0 & \cdots & 0 & e^{i \theta_n}
>\end{array}
>\right )
>$$
>où les $\theta_i$ sont des nombre réels.

### 2. Endomorphismes normaux
### 5. Exercices 

#### Exercice 5. (Exponentielle d'une matrice antisymétrique)

>[!question]- 1/ Soit $\theta \in \mathbb R$. Montrer l'égalité 
>$$
>\exp \left (  \begin{array}{cc} 0 & - \theta \\ \theta & 0  \end{array} \right ) = \left (  \begin{array}{cc} \cos \theta  & - \sin \theta \\ \sin \theta & \cos \theta   \end{array} \right ) 
>$$
>
>
>>[!success]- Solution
>>
>>Notons $ J = \left (  \begin{array}{cc} 0 & - 1 \\ 1 & 0  \end{array} \right ) $. Un calcul facile donne $J^2 = -I_2$, ce qui entraîne pour tout $n \in \mathbb N$ les égalités $J^{2n} = (-1)^{n} I_2$ et $J^{2n + 1 } = (-1)^{n} J$. On déduit
>>$$
>>\exp ( \theta J ) = \sum_{n = 0}^{+ \infty } \frac{\theta^n}{n!} J^n = \sum_{n = 0}^{+ \infty } \frac{(-1)^n \theta^{2n}}{(2n)!} I_1 + \sum_{n = 0}^{+ \infty } \frac{(-1)^n \theta^{2n+1}}{(2n+1)!} J = (\cos \theta) I_2 + (\sin \theta) J,
>>$$
>>ce qui est précisément le résultat demondé
>
>

>[!question]+ 2/
>>[!question]- a)  Soit $n \in \mathbb{N}^\ast$. Montrer que $P\in \mathcal M_n (\mathbb R)$ est une matrice orthogonale directe si et seulement s'il existe une matrice antisymétrique $A \in \mathcal M_n ( \mathbb R)$ telle que $ P = \exp ( A)$.
>>
>>>[!success]+ Solution
>>>
>>>La condition suffisante est immédiate : si $A \in \mathcal M_n(\mathbb R)$ est une matrice antisymétrique, alors la matrice $P=\exp(A)$ vérifie ${~}^t P P = \exp({~}^t A)\exp(A) = \exp(-A)\exp(A) = I_n$. Enfin, on a $\det (P) = \det(\exp(A)) = \exp(\text{tr } A) = 1$ ( voir l'[[Mathématique/Algèbre/Algèbre#Exercice 2. (Déterminant d'exponentielle d'une matrice)|Exercice 4.3.4.2. (Déterminant d'exponentielle d'une matrice)]] ) .
>>>
>>>Montrons maintenant la condition nécessaire. Soit $P \in \mathcal M_n(\mathbb R)$ une matrice orthogonale directe, soit $u \in \mathcal L ( \mathbb R^n)$ son isométrie associée. D'après le [[Mathématique/Algèbre/Algèbre#Réduction des isométries|Théorème 5.3.1.1]] , il existe une base orthonormale $B$ de $\mathbb R^n$ dans laquelle la matrice de $u$ a la forme 
>>>$$
>>>[u]_B = 
>>>\left (
>>>\begin{array}{cccccc}
>>>R(\theta_1) & 0_2 & \cdots & \cdots & \cdots & 0_2 \\
>>>0_2& \ddots & \ddots  & 0 & 0 & \vdots \\
>>>\vdots & \ddots & R(\theta_r) & \ddots & 0  & \vdots \\
>>>\vdots & 0 & \ddots & \varepsilon_1 & \ddots & \vdots \\
>>>\vdots & 0 & 0  & \ddots & \ddots & 0 \\
>>>0 & \cdots & \cdots &  \cdots &  0 & \varepsilon_s
>>>\end{array}
>>>\right )
>>>$$
>>>où pour tout $i$, $R(\theta_i)$ est la matrice de rotation $2 \times 2$ d'angle $\theta_i$, et où $\varepsilon_j \in \{- 1 , + 1 \}$ pour tout $j$. Par hypothèse, $u$ est une isométrie directe donc $\det u = 1$. Le calcul de déterminant par blocs donne 
>>>$$
>>>\det u = \det R(\theta_1) \cdots \det R(\theta_r) \,  \varepsilon_1 \cdots \varepsilon_s = \varepsilon_1 \cdots \varepsilon_s.
>>>$$
>>>Ainsi, le produit des $\varepsilon_i$ vaut $1$, donc il y en a un nombre pair $2p$ (avec $p \in \mathbb N$) qui valent $-1$, et les $q$ autres valent $+1$ (avec $2p + q = s$). Quitte à permuter les $s$ derniers vecteurs de la base $B$, on peut même supposer que kes $2p$ premiers $\varepsilon_j$ valent $-1$, et les $q$ derniers valent $+1$. Comme la matrices ${ \scriptstyle  \left ( \begin{smallmatrix} -1 & 0 \\ 0 & -1  \end{smallmatrix} \right )}$ est une matrice de rotation d'angle $\pi$, il revient au même de dire quela matrice de $u$ dans $B$ a la forme
>>>$$
>>>[u]_B = 
>>>\left (
>>>\begin{array}{cccc}
>>>R(\theta_1) & 0_2 & \cdots & 0_2 \\
>>>0_2 & \ddots & \ddots  &  \vdots \\
>>>\vdots & \ddots & R(\theta_m) & 0_{2,q}  \\
>>>0_{q,2} & \cdots & 0_{q,2} & I_q \\
>>>\end{array}
>>>\right )
>>>$$
>>>avec $\theta_i = \pi$ pour $r < i \leq m = r + p$. La résultat de la question 1/ nous permet maintenant de remarquer que 
>>>$$
>>>[u]_B = \exp (M) \quad  \text{où} \quad M = 
>>>\left (
>>>\begin{array}{cccc}
>>>\theta_1 J & 0_2 & \cdots & 0_2 \\
>>>0_2 & \ddots & \ddots  &  \vdots \\
>>>\vdots & \ddots & \theta_m J & 0_{2,q}  \\
>>>0_{q,2} & \cdots & 0_{q,2} & 0_q \\
>>>\end{array}
>>>\right ),
>>>$$
>>>avec $J = { \scriptstyle  \left ( \begin{array}{cc} 0 & -1 \\ +1 & 0  \end{array} \right )}$. La matrice par blocs $M$ est antisymétrique cas $J$ est antisymétrique.
>>>En notant $Q$ ma matrice de passage de la base canonique de $\mathbb R^n$ à la base $B$ (c'est une matrice orthogonale), on a donc montré que $P = {~}^t Q \exp(M) Q$. En posant $A = {~}^t Q M Q$ on a donc $P = \exp(A)$ et la matrice $A$ est antisymétrique car ${~}^t A = {~}^t Q {~}^tM Q = {~}^t Q(-M)Q = -A$, d'où le résultat 
>
>>[!question]- b) En déduire que le groupe spécial orthogonal $\mathcal{S O}_n$ est connexe par arcs.
>>>[!success]+ Solution
>>>
>>>Étant données deux matrices $P$ et $Q$ dans $\mathcal{S O}_n$, on peut écrire $P = \exp(A)$ et $Q = \exp{B}$ avec $A$ et $B$ antisymétriques d'après la question précédente. La question précédente nous assure également que le chemin continu $[0, 1] \rightarrow \mathcal{M}_n (\mathbb R ) \quad t \mapsto \exp( (1-t) A + t B )$ est à valeur dans $\mathcal{SO}_n$, donc le groupe spécial orthogonal est bien connexe par arcs.

>[!question]+ 3/ (Cas de $\mathbb R^3$) Soit $v = (a , b  , c)$ un vecteur non nul de l'espace euclidien $\mathbb R^3$.
>>[!question]- a) Montrer que l'exponentielle de la matrice antisymétrique
>>$$
>>\hat{v} = 
>>\left (
>>\begin{array}{ccc}
>>0 & -c & b  \\
>>c& 0 & -a \\
>>-b & a & 0  \\
>>\end{array}
>>\right )
>>$$
>>est la matrice de la rotation d'axe $e = v / \Vert v \Vert $ , d'angle $\theta = \Vert v \Vert $, où $\Vert \cdot \Vert$ désigne la norme euclidienne.
>>
>>>[!tip]- Indication  
>>>
>>>Remarquer que $\hat{v}$ est la matrice de l'endomorphisme $ X \mapsto v \wedge X$, où $\wedge$ désigne le produit vectoriel).
>>
>>>[!success]-  Solution
>>>
>>>Suivons l'indication et considérons l'endomorphisme $u \, \colon \; \mathbb R^3 \mapsto \mathbb R^3 \; X \mapsto v \wedge X$. On remarque aisement que la matrice de $u$ dans la base canonique de $\mathbb R^3 $ est la matrice $\hat{v}$. Partant du vecteur $ e = v / \Vert v \Vert = \frac{1}\theta v $, on le complète avec deux vecteurs $e_1$ et $e_2$ de sorte que $(e_1 , e_2 , e )$ soit une base orthogonormale directe de $\mathbb R^3 $. Comme $v = \theta e $ , on a 
>>>$$
>>>u(e_1) = \theta e \wedge e_1 = \theta e_2 , \quad u(e_2) = \theta e \wedge e_2 = - \theta e_1 , \quad u(e) = \theta e \wedge e = 0,
>>>$$
>>>autrement dit la matrice de $u$ dans la base $B$ à la forme par blocs 
>>>$$
>>>[u]_B = 
>>>\left (
>>>\begin{array}{cc}
>>>\theta J & 0_{2,1} \\
>>>0_{1,2} & 0  \\
>>>\end{array}
>>>\right ) \tag{$\ast$}
>>>$$
>>>où $J = { \scriptstyle  \left ( \begin{smallmatrix} 0 & -1 \\ +1 & 0  \end{smallmatrix} \right )}$. Nous avons vus que $\exp(\theta J)$ est une matrice $2 \times 2$ de rotation d'angle $\theta$, donc
>>>$$
>>>\exp([u]_B) = 
>>>\left (
>>>\begin{array}{ccc}
>>>\cos \theta  & - \sin \theta & 0  \\
>>>\sin \theta  & \cos \theta & 0   \\
>>>0 & 0 & 1 
>>>\end{array}
>>>\right ). \tag{$\ast \ast$}
>>>$$
>>>Comme $\exp([u]_B)$ est aussi la matrice de $\exp(u)$ dans la base $B$, ceci entraine que $\exp(u)$ est la rotation autour du vecteur $e$ d'angle $\theta$, d'où le résultat.
>
>>[!question]- b) Montrer la {\em formule de Rodrigues}
>>$$
>>\exp(\hat{v}) = I_3 + \frac{\sin \theta}\theta \hat{v} + \frac{1 - \cos \theta}{\theta^2} \hat{v}^2.
>>$$
>>
>>>[!success]- Solution
>>>
>>>En utilisant la forme par bloc $(\ast)$, de la matrice de $u$ dans la base $B$, on obtient
>>>$$
>>>I_3 + \frac{\sin \theta}\theta [u]_B + \frac{ 1 - \cos \theta }{\theta^2}([u]_B)^2 = I_3 + \sin \left ( \begin{array}{cc} J & 0_{2,1} \\ 0_{1,2}  & 0 \end{array} \right ) + ( 1 - \cos \theta ) \left ( \begin{array}{cc} - I_2 & 0_{2,1} \\ 0_{1,2}  & 0 \end{array} \right )
>>>$$
>>>ce qui s'écrit encore 
>>>$$
>>>I_3 + \frac{\sin \theta}\theta [u]_B + \frac{ 1 - \cos \theta }{\theta^2}([u]_B)^2 = 
>>>>>>\left (
>>>\begin{array}{ccc}
>>>\cos \theta  & - \sin \theta & 0  \\
>>>\sin \theta  & \cos \theta & 0   \\
>>>0 & 0 & 1 
>>>\end{array}
>>>\right ). 
>>>$$
>>>D'après la forme $(\ast \ast)$, ceci est précisément l'exponentielle de la matrice $u$ dans la base $B$. D'où le résultat par changement de base.




