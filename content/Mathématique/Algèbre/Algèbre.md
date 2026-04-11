---
title: Algèbre
tags:
  - Science
---
# Arithmétique, Groupes et Anneaux 

## Groupes

### Généralité 

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

## Anneaux

### Définitions

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
### [[Idéal|Idéaux]]

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

# Corps, polynômes et fractions rationnelles

## Corps, polynômes et arithmétiques dans $\mathbb K[X]$

### Corps

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