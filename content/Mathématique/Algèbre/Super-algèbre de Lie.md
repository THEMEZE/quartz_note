---
title: Super-algèbre de Lie
tags:
  - Science
---
## Définition

Une **[Superal-gèbre de Lie](https://fr.wikipedia.org/wiki/Superalg%C3%A8bre_de_Lie)** (cd aussi **[ncatlab.org/]([https://fr.wikipedia.org/wiki/Superalg%C3%A8bre_de_Lie](https://ncatlab.org/nlab/show/super+Lie+algebra) 
$$
(\; \mathcal A \;,\; + \;,\; \cdot \; ,\; [\,\bullet \, , \, \bullet \, \} \, )
$$
avec :
- $+$ : addition
- $\cdot$ : multiplication par un scalaire
- $[\bullet  , \bullet  \} $  : super-crochet

(👉 Mais en pratique, **les deux premiers sont toujours implicites**) est un **[super-algèbre](https://fr.wikipedia.org/wiki/Superalg%C3%A8bre "Superalgèbre")** non-assosiative sur un  [anneau](https://fr.wikipedia.org/wiki/Anneau_\(math%C3%A9matiques\) "Anneau (mathématiques)") $\mathbb K $ ( $\mathbb R $ ou $\mathbb C$ en générale ), 

* muni d'un une décomposition en [somme directe](https://fr.wikipedia.org/wiki/Somme_directe "Somme directe") (cf [[Algèbre graduée]]/[Algèbre Graduée](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_gradu%C3%A9e)):
$$
{\displaystyle \mathcal A= \mathcal A_{0}\oplus \mathcal A_{1}},
$$
>[!info]- homogène
> Les éléments de $\mathcal A_i$ sont dit homohène ( pas de $x = x_0 + x_i$ , $x_i \in \mathcal A_i$) .

>[!tip]- bosons / fermions
>Les éléments de **$\mathcal A_0$** correspondent aux **bosons**.
>Les éléments de **$\mathcal A_1$** correspondent aux **fermions**.

* et une multiplication [bilinéaire](https://fr.wikipedia.org/wiki/Application_bilin%C3%A9aire "Application bilinéaire") ${\displaystyle \mathcal A \times \mathcal A \to \mathcal A}$ telle que
$$
{\displaystyle \mathcal A_{i} \mathcal A_{j}\subseteq \mathcal A_{i+j \mod 2}}
$$
où les indices se lisent [modulo](https://fr.wikipedia.org/wiki/Arithm%C3%A9tique_modulaire "Arithmétique modulaire") 2, c'est-à-dire qu'ils sont considérés comme des éléments de **$\mathbb Z_2$**.

> [!info]- super-anneau,  $\mathbb Z_2$-gradué
>Un **super-anneau**, ou [anneau](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_gradu%C3%A9e "Algèbre graduée") **$\mathbb Z_2$-gradué** , est une [super-algèbre](https://fr.wikipedia.org/wiki/Superalg%C3%A8bre "Superalgèbre") sur l'[anneau](https://fr.wikipedia.org/wiki/Anneau_\(math%C3%A9matiques\) "Anneau (mathématiques)")  des [entiers](https://fr.wikipedia.org/wiki/Entier_relatif "Entier relatif") **$\mathbb Z$** .

>[!tip]-  parité / degrès de Grassmann - $\quad   \vert   \bullet \vert \, \colon \, \mathcal A_i \ni x \mapsto i \in \mathbb Z_2$ 
>On définit l'opération ${\displaystyle \vert \bullet \vert :{\mathcal {A}}_{0}\cup {\mathcal {A}}_{1}\to \{0,1\}}]$ tel que ${\displaystyle |x|\mapsto {\begin{cases}0\quad {\text{si}}\quad x\in {\mathcal {A}}_{0}\\1\quad {\text{si}}\quad x\in {\mathcal {A}}_{1}\end{cases}}}$ pour noter le degré d'un élément homogène.
>$$ 
>\forall x \in \mathcal A_i \, \colon \,  \vert x \vert = i \, , \,  i \in \mathbb Z_2
>$$

> [!warning]-  $\vert x \cdot y \vert = \vert x \vert + \vert  y \vert \mod 2 $
> Si ${\displaystyle x}$ et ${\displaystyle y}$ sont tous les deux homogènes, alors leur produit ${\displaystyle x \cdot y}$ aussi est homogène et ${\displaystyle |x \cdot y|=|x|+|y|}$.


* Le produit interne [bilinéaire](https://fr.wikipedia.org/wiki/Application_bilin%C3%A9aire "Application bilinéaire") d'une **[super-algèbre de Lie](https://fr.wikipedia.org/wiki/Superalg%C3%A8bre_de_Lie))**  est noté ${\displaystyle [\bullet , \bullet \} :{\mathcal {A}}\times {\mathcal {A}}\to {\mathcal {A}}} $ et nommé **super-[crochet de Lie](https://fr.wikipedia.org/wiki/Crochet_de_Lie "Crochet de Lie")** ou **super-[commutateur](https://fr.wikipedia.org/wiki/Commutateur_\(op%C3%A9rateur\) "Commutateur (opérateur)")**. Il doit respecter les deux conditions suivantes :

	- **Super anti-symétrie**:  
    $$
    {\displaystyle \forall (x,y)\in {\mathcal {A}}_{i}\times {\mathcal {A}}_{j}\; \vert \; i , j \in \mathbb Z_2 \, \colon \quad [x,y\} =-(-1)^{|x||y|}[y,x\}}
    $$
	 - **Super-[relation de Jacobi](https://fr.wikipedia.org/wiki/Relation_de_Jacobi "Relation de Jacobi")**  
	$$
	{\displaystyle \forall (x,y,z) \in {\mathcal {A}}_{i} \times  {\mathcal {A}}_{j} \times  {\mathcal {A}}_{k} \; \vert \;  i, j , k \in \mathbb Z_2  \, \colon  \quad (-1)^{|x||z|}[x,[y,z\} \} +(-1)^{|y||x|}[y,[z,x\} \} +(-1)^{|z||y|}[z,[x,y\} \} =0}
	$$
	👉 Une expression 
	$$
    {\displaystyle \forall (x,y)\in {\mathcal {A}}_{i}\times {\mathcal {A}}_{j}\; \vert \; i , j \in \mathbb Z_2 \, \colon \quad [x,y\} = x \cdot y - (-1)^{\vert x \vert \, \vert y \vert }}y \cdot x .
    $$
>[!info]- Propriétés de - $[\bullet  , \bullet  \}$
>- ${\displaystyle \forall x\in {\mathcal {A}}_{0}\, \colon \quad [x,x \} =0}$
>- ${\displaystyle \forall x\in {\mathcal {A}}_{1}\, \colon \quad [[x,x\} ,x\} =0}$
>- ${\displaystyle \forall (x,y)\in {\mathcal {A}}_{i}\times {\mathcal {A}}_{j}\; \vert \; i , j \in \mathbb Z_2 \, \colon \quad |[x,y\} |=|x|+|y|\mod 2}$

>[!example]- Exemple : 𝖔𝖘𝖕(1|2)
> Soient ${\displaystyle J_{0}\in {\mathcal {A}}_{0}}$, ${\displaystyle J_{+}\in {\mathcal {A}}_{1}}$ et ${\displaystyle J_{-}\in {\mathcal {A}}_{1}}$ tels que :
> - ${\displaystyle [J_{0},J_{+}\}=J_{+}}$
> - ${\displaystyle [J_{0},J_{-}\}=-J_{-}}$
> - ${\displaystyle [J_{+},J_{-}\} =2J_{0}}$
> 
>Alors l'ensemble ${\displaystyle \{a\cdot J_{0}+b\cdot J_{+}+c\cdot J_{-}\; | \; a,b,c\in \mathbb {C} \}}$ , muni du super-[crochet de Lie](https://fr.wikipedia.org/wiki/Crochet_de_Lie "Crochet de Lie") défini par sa bilinéarité et par les produits de ${\displaystyle J_{0}}$, ${\displaystyle J_{+}}$ et ${\displaystyle J_{-}}$, forme la superalgèbre de Lie ${\displaystyle {\mathfrak {osp}}(1|2)}$.

