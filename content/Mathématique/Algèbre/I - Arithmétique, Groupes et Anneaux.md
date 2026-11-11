---
title: I - Arithmétique, Groupes et Anneaux
---
Jusqu'au début du vingtième siècle, l'algèbre désignait essentiellement l(étude de la résolution d'équation algèbrique ( en témoigne la dénomination de *théorème fondamental de l'algèbre*). Avec la résolution des équation algèbriques apparut, de manière plus ou poins confus, la notion de nombre complexe : on utilise le symbole $\sqrt{-1}$. Parallèlement, la théorie de congruence se développa.

Ainsi, de nouveaux objets mathématiques entrèrent en scène. Bientôt, les mathématiciens y virent des analogies étroites d'il cherchèrent à expliquer : l'algèbre devint progressivement l'étude abstraite des structures algèbriques, jusqu'à ce que connaît l'étudiant d'aujourd'hui.

# 1. Arithmétique sur les entiers

Nous supposons acquises les notions de base sur l'ensemble des entiers naturels $\mathbb{N}$ et des entiers relatifs $\mathbb{Z}$, ainsi que les calculs dans l'anneau quotient $\mathbb{Z}/n \mathbb{Z}$. Une études plus approfondie de ce dernier fait l'objet de la section 3 de ce chapitre.

## 1.1. Divisibilité - pgcd, ppcm

>[!note]- <span style="font-variant: small-caps;"> Définition 1 : $a\mid b$ </span> 
>Soient $a$ et $b$ deux entiers relatifs. On dit que $a$ *divise* $b$ ( ou que $b$ est un $mutiple$ de $a$), et on note $a\mid b$, s'il existe un entrier $n$ tel que $b=an$. Si $a$ ne divise pas $b$ on note $a\nmid b$.

> [!info]- <span style="font-variant: small-caps;"> Proposition 1 (Division Euclidienne) </span>
> Soient $a\in \mathbb{Z}, b\in \mathbb{N}^\ast$. *Il existe un unique couple $(q,r) \in \mathbb{Z}\times \mathbb{N}^\ast$ tel que
> $$ a = bq + r, \quad \textit{avec} \quad 0 \leq r \leq b - 1 \quad (r\in \llbracket 0, b \llbracket = [\![ 0, b [\![). $$
> $q$ s'appelle le quotient, $r$ le reste, de la division euclidienne de $a$ par $b$.*
>
>>[!tip]- <span style="font-variant: small-caps;">Proofs </span>
>>>[!succes]- <span style="font-variant: small-caps;"> Démonstration de l'existence (dans $\mathbb{N}$) </span>
>>>Soient $a \in \mathbb{N}$ et $b \in \mathbb{N}^\ast$ ($b>0$). On considère l'ensemble des multiples de $b$ inférieurs ou égaux à $a$, ou on utilise le principe du plus petit élément.
>>>1. Considérons l'ensemble $E = \{a - kb \mid k \in \mathbb{N}, a - k b \geq 0\}$
>>>2. Cet ensemble $E$ est une partie de $\mathbb{N}$.
>>>3. De plus, $E$ est non vide car pour $k=0,a - 0\times b = a \geq 0$ (ou si on prend $k$ assez grand, $a-kb<0$, donc $E$ est borné supérieurement et posséde un plus grand $k$).
>>>4. D'après le principe du bon ordre dans $\mathbb{N}$, l'ensemble $E$ possède un plus petit élément que l'on note $r$.
>>>5. Par définition, il existe un entier $q \in \mathbb{N}$ tel que $r=a-qb \geq 0$, ce qui donne : $$ a = b q +r$$
>>>6. Il reste a prouver que $r < b$. Par l'absurde, supposons que $r\geq b$. Alors on aurait $r - b \geq 0$, c'est-à-dire $(a - qb)-b = a -(q+1)b \geq 0$. Cela signifirait que $a-(q+1)b$ appartiendrais à $E$ et serait strictement plus petit que $r$, ($r-b<r$), ce qui contredit le fait que $r$ est le *plus petit élément de $E$*.
>>>7. On en déduit donc obligatoirement que $0 \leq r <b$
>>>8. Pour $\mathbb{Z}$, on étend le résultat à $a \in \mathbb{Z}$ en appliquant le cas dans $\mathbb{N}$ à $\vert a \vert$ et $\vert b \vert$, puis en ajustant les signes de $q$ et $r$.
>>>$\square$
>>
>>
>>>[!succes]- <span style="font-variant: small-caps;"> Démonstration de l'unicité (dans $\mathbb{Z}$) </span>
>>>Supposons qu'il existe deux couples $(q,r)$ et $(q',r')$ vérifiant la relation:
>>>$$a=bq + r, \quad \textit{avec} \quad 0 \leq r \leq b - 1 $$
>>>$$a=bq' + r', \quad \textit{avec} \quad 0 \leq r' \leq b - 1 $$
>>>9. On a donc : $$ bq +r = bq'+r' \Rightarrow b(q-q')=r'-r$$
>>>10. En passant aux valeurs absolues :$$ \vert b \vert \cdot \vert q - q' \vert = \vert r' - r \vert $$
>>>11. Encadrons $r' -r$ :
>>>	1. Comme $0 \leq r < b$ et $0\leq r' < b$, on a $- b < -r$ et $0 \leq r' < b$.
>>>	2. En combinant les inégalités, on obtient : $$ - b < r' - r < b \Rightarrow \vert r' - r \vert < b$$
>>>12. On réinjecte cela dans l'égalité des valeurs absolues : $$ b \cdot \vert q - q' \vert < b $$
>>>13. Comme $b\neq 0$ (donc $b > 0$), on peut diviser par $b$ : $$\vert q - q' \vert < 1 $$
>>>14. Or, $q$ et $q'$ sont des nombres entiers, donc $\vert q- q'\vert$ est un entier positif strictement inférieur à $1$. La seule possibilité est que : $$ q = q' $$
>>>15. En remplaçant $q = q'$ dans l'équation initiale $b(q-q')=r'-r$, on obtient: $$b(0) = r'-r \Rightarrow r = r'$$
>>>Le couple $(q,r)$ est donc **unique**.
>>>$\square$
>>
>>$\square$
>>
>>

>[!infos]- <span style="font-variant: small-caps;"> Rappel de la définition d'un anneau euclidien </span>
>Soit $A$ un anneau cummutuatif intègre. On dit que $A$ est un **anneau euclidien** s'il existe une application $v \colon A \backslash \{0\} \rightarrow \mathbb{N}$ (appellée stathme euclidien) vérifiant la propriété suivante :
>Pour tous $a, b\in A$ avec $b\neq 0$, il existe un couple $(q,r)\in A \times A$ tel que:
>
>>[!note]-
>>L'**existence** fait partie intégrante de l'axiome fondateur de la strcture. Elle ne se démontre pas de manière générale pour l'anneau abstrat, elle est présupposée dés lors que l'on manipule ub tel anneau.)
>
>>[!tip]-  <span style="font-variant: small-caps;"> Démonstration fondamentale : Tout anneau euclidien est principal </span>
>>
>>Puisque l'unicité du reste n'est pas garentie dans le cas générale, le théorème le plus important et le plus formellement démontré en algèbre pour ces structures est que la **division euclidienne sont principaux** (c'est-à-dire engendrès par un seul élément).
>>
>>>**Objectif :**
>>>Soit $I$ un idéal de $A$. Nous voulons démontrer qu'il existe une élément $b \in A$ tel que $I =b A$ (l'idéal engendré par $b$).
>>>
>>>**Étapes de la démonstration :**
>>>16. **Cas trivial :** Si $I=\{0\}$, alors $I$ est l'idéal nul engendré par $0$ ($I=0A$). La propriété est vérifiée.
>>>17. **Choix du candidat générateur :** Supposons maintenant que $I\neq \{0\}$.
>>>	1. Considérons l'ensemble des valeurs des stathmes des éléments non nuls de $I:v(I\backslash \{0\})= \{ v(x) \mid x \in I, x \neq 0 \}$.
>>>	2. Cet enssemble est une partie non vide de $\mathbb{N}$. Par le principe du bon ordre (toute partie non vide de $\mathbb{N}$ possède un plus petit élément), cet ensemble admet unminimum.
>>>	3. Soit $b\in I \backslash \{0\}$ un élément qui attent ce minimum. Autrement dit, pour tout $x \in I \backslash \{0\}$, on a $v(b) \leq v(x)$.
>>>18. **Utilisation de la division euclidienne (Double inclusion):**
>>>	1. **Inclusion facile $\boldsymbol{(bA\subset I)}$ :** Comme $b\in I$ et que $I$ est un idéal, par définition, tout multiple de $b$ par un élément de $A$ reste dans $I$. Donc $bA \subset I$.
>>>	2. **Inclusion réciproque $\boldsymbol{( I \subset bA)}$ :** Soit $a$ un élément quelconque de $I$. Appliquons de division euclidienne de $a$ par $b$: Il existe $q,r\in A$ tels que : $$ a = bq + r \quad \textit{avec} \quad r = 0 \quad \textit{où} \quad v(r) < v(b)$$
>>>19. **Analyse du reste par minimalité :**
>>>	1. Exprimons le reste : $r = a - bq$.
>>>	2. Comme $a \in I$ et $b\in I$, et que $I$ est un idéal (stable par combinaison linéaire) on en déduit que $\boldsymbol{r \in I}$.
>>>	3. Si $r \neq 0$, alors par définition du stathme euclidien, on doit aoir $v(r) < v(b)$.
>>>	4. Or, $b$ a été choisi précisément pour avoir le stathme **le plus petit possible** parmi tous les élément non nuls de $I$. Une inégalité $v(r)<v(b)$ avec $r\in I \backslash \{0\}$ est donc une **contradiction**.
>>>20. **Conclusion :**
>>>	1. La seule issue possible est que $\boldsymbol{r = 0}$.
>>>	2. Par conséquent, $a =bq$, ce qui prouve que $a\in bA$.
>>>	3. On a donc bien $I \subset bA$.
>>>
>>>Par double inclusion, $\boldsymbol{I = bA}$. L'idéal $I$ est principal, ce qui prouve que **tout anneau euclidien est un anneau principal**.
### 1.1.1. *Classes de congruence modulo $\boldsymbol{n}$*.

>[!note]- <span style="font-variant: small-caps;"> Définition 2 : congrus modulo $\boldsymbol{n}$ </span> 
>Soient $n$ un entier naturel non nul ($\mathbb{N}^\ast$). On note $n \mathbb{Z} = \{n k \mid k \in \mathbb{Z} \}$. Si $x$ et $y$ sont deux entiers, on note $x \equiv y \quad (\text{mod}\,  n )$ si $x-y \in n\mathbb{Z}$, et on dit alors que $x$ et $y$ sont *congrus modulo $n$*.

>[!note]- <span style="font-variant: small-caps;"> Définition 3 : $\boldsymbol{\mathbb{Z}/n\mathbb{Z}= \{\overline{0},\overline{1}, \cdots, \overline{n-1} \}}$ </span> 
>Soient $n$ un entier naturel non nul ($\mathbb{N}^\ast$). L'anneau quotient de $\mathbb{Z}$ par $n \mathbb{Z}$ est noté $\mathbb{Z}/n\mathbb{Z}$. On note généralement $\overline{x}$ ( ou $\dot{x}$) la classe d'un entier $x$ dans $\mathbb{Z}/n\mathbb{Z}$. Ainsi, $\mathbb{Z}/n\mathbb{Z} = \{\overline{0},\overline{1}, \cdots, \overline{n-1} \}$.

### 1.1.2. *Plus Grand Commun Diviseur (PGCD)*.

>[!note]- <span style="font-variant: small-caps;"> Définition 4 : Plus Grand Commun Diviseur (PGCD) :   </span> le plus grand nombre entier qui divise à la fois deux ou plusieurs nombres sans laisser de reste
>- Soient $a_1, \cdots , a_n$ des entiers. Il existe une unique entier naturel $d$ tel que $a_1 \mathbb{Z}+ \cdots + a_n \mathbb{Z} = d \mathbb{Z}$. Ainsi défini, $d$ s'appelle le *pgcd* de $a_1, \cdots , a_n$ et on note $d = \text{pgcd}(a_1, \cdots , a_n)$. L'entier $d$ est ainsi le plus grand entier naturel divisant tous les $a_i$ ( $1 \leq i \leq n$).
>- Lorsque $\text{pgcd}(a_1, \cdots , a_n)=1$, on dit que les entiers $a_1, \cdots , a_n$ sont premiers entre eux *dans leur ensemble*. Lorsque $\text{pgcd}(a_i, a_j)=1$ dès que $i\neq j$, les entiers $a_i$ sont dits premiers entre eux *deux à deux*.

>[!note]- <span style="font-variant: small-caps;"> Remarque 1 :    </span>
>- Des en
>- Lorsque $\text{pgcd}(a_1, \cdots , a_n)=1$, on dit que les entiers $a_1, \cdots , a_n$ sont premiers entre eux *dans leur ensemble*. Lorsque $\text{pgcd}(a_i, a_j)=1$ dès que $i\neq j$, les entiers $a_i$ sont dits premiers entre eux *deux à deux*.




<span style="font-variant: small-caps;">Texte en Petites Capitales</span>



