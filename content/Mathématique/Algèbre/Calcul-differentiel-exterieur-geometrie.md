---
title: Calcul différentiel extérieur et géométrie
tags:
  - Science
---
<div id="include-html"></div>  
  




[Frédéric Hélein M2 Calcul différentiel extérieur et géométrie](https://webusers.imj-prg.fr/~frederic.helein/caldiffext.pdf)
[[Forme-différentielle]]


# Les bases du calcul différentiel extérieur
## L’algèbre extérieure
<a id="algebre-ext"></a>

### Définition
Dans la suite $V$ désigne un espace vectoriel et on note $V^\ast$ son dual, c’est à dire l’espace vectoriel des formes linéaires sur $V$ .

  
> [!note]- Définition (Forme p-multilinéaire alternée)
>Soit $V$ un espace vectoriel sur $\mathbb R$ de dimension finie $m$. Une **forme p-multilinéaire alternée $\alpha$ sur $V$** ou, de façon abrégée, une **p-forme $\alpha$ sur V** est une application $\alpha \colon  \underbrace{V \times  \cdots  \times V}_{p ~ \text{fois}} \to \mathbb R$  (où $V \times  \cdots  \times V = V^p$ ) qui est
>- **multilinéaire**, *i.e.*.$\forall i \in \mathbb N\, \vert \, 1 \leq i \leq p \, \vert \, \forall v_1 , \cdots , v_i , \cdots , v_p , w_i \in V \, \vert \,  \forall \lambda , \mu \in \mathbb R \colon :$
>	$$
>	\alpha (v_1 , \cdots , \lambda v_i + \mu w_i , \cdots , v_p ) = \lambda  \alpha (v_1 , \cdots , v_i  , \cdots , v_p ) + \mu \alpha (v_1 , \cdots ,   w_i , \cdots , v_p ) 
>	$$
>- **alternée**, *i.e.* $\forall i , j \in \mathbb N \, \vert \,  1 \leq i , j \leq p \colon $
>$$
>\alpha( \cdots , v_i , \cdots , v_j , \cdots ) + \alpha( \cdots , v_j , \cdots , v_i , \cdots ) = 0
>$$
>L’ensemble des **p-formes sur $V$** forme un espace vectoriel, que l’on note $\Lambda^p V^\ast$.
>Nous conviendrons que $\Lambda^0 V^\ast = \mathbb R$, autrement dit une **0-forme sur $V$** est un nombre réel.


Nous remarquons que $\Lambda^1 V^\ast$ s’identifie à $V^\ast$ et que $\Lambda^p V^\ast = \{0\}$ si $p > m$.

> [!note]- Définition (Produit extérieur)  
> Pour $p, q \in \mathbb{N}$, on définit le produit extérieur  
> $$
> \begin{array}{rcl}
> \Lambda^p V^\ast \times \Lambda^q V^\ast & \longrightarrow & \Lambda^{p+q} V^\ast \\
> (\alpha , \beta ) & \longmapsto & \alpha \wedge \beta 
> \end{array}
> $$
> par 
> $$
> \alpha \wedge \beta ( v_1 , \cdots , v_{p+q} ) = \frac{1}{p!q!}\sum_{ \sigma \in \mathfrak{S}(p+q)}(-1)^{\vert \sigma \vert } \alpha (v_{\sigma(1)} , \cdots ,v_{\sigma(p)} )\beta (v_{\sigma(p+1)} , \cdots ,v_{\sigma(p+q)} ).
> $$

Cette opération est clairement bilinéaire. De plus, elle satisfait les propriétés suivantes

>[!info]- Proposition  (Le produit extérieur est associatif) :
>$$
>\forall ( \alpha , \beta , \gamma ) \in (\Lambda^p V^\ast) \times (\Lambda^q V^\ast) \times (\Lambda^r V^\ast) \, \colon \, (\alpha \wedge \beta ) \wedge \gamma = \alpha \wedge ( \beta \wedge \gamma ).
>$$
>On peut donc noter ce produit extérieur : $\alpha \wedge \beta \wedge \gamma $ .

Comme nous le verrons au fur et à mesure, l’associativité du produit extérieur est une propriété merveilleuse, qui a le pouvoir de transformer des calculs compliqués en des identités toutes simples ! Le produit extérieur n’est pas commutatif mais...

>[!info]- Proposition  (Le produit extérieur est commutatif gradué, c’est à dire) :
>$$
>\forall ( \alpha , \beta  ) \in (\Lambda^p V^\ast) \times (\Lambda^q V^\ast)  \, \colon \, \beta \wedge \alpha  = (-1)^{pq}\alpha \wedge  \beta .
>$$

>[!example]-
>
>(i)  Si $\alpha \in \Lambda^0 V^\ast = \mathbb R $ et si $\beta \in \Lambda^q V^\ast$, $\alpha \wedge \beta = \alpha \beta $,  expression dans laquelle le scalaire $\alpha$ multiple la q-forme $\beta$.
>
>(ii) Si $\alpha , \beta \in \Lambda^1 V^\ast \equiv V^\ast $ alors , 
>$$
>\forall v , w \in V \, \colon \, \alpha \wedge \beta ( v , w ) = \alpha(v) \beta(w) - \beta(v) \alpha (w) = \left \vert \begin{array}{cc} \alpha(v) & \alpha(w) \\ \beta(v) & \beta(w) \end{array} \right \vert.
>$$
>Supposons pour simplifier encore que $\text{dim}V = 2$ et soit $(\theta_1 , \theta_2 )$ une base de $V^/ast$. Notons $v_1 = \theta_1(v)$, $v_2 = \theta_2 (v)$, $w_1 = \theta_1 (w)$ et $w_2 = \theta_2 (w)$. Décomposons également $\alpha = a_1 \theta_1 + a_2 \theta_2$ et $\beta = b_1 \theta_1 + b_2 \theta_2$. Alors
>$$
>\begin{array}{rcl}
>\alpha \wedge \beta (v, w) & = & (a_1 v_1 + a_2 v_2 )(b_1 w_1 +b_2 w_2) - (a_1 w_1 + a_2 w_2 )(b_1 v_1 +b_2 v_2) \\
>& = & (a_1 b_2 - a_2 b_1 )(v_1 w_2 - v_2 w_1) \\
>\end{array}
>$$
>En particulier $\theta_1 \wedge \theta_2 (v , w ) = v_1 w_2 - v_2 w_1$. Nous voyons ainsi que
>$$
>\alpha \wedge \beta = \left \vert \begin{array}{cc} a_1 & a_2 \\ b_1 & b_2 \end{array} \right \vert \theta_1 \wedge \theta_2 \quad \text{et} \quad \alpha \wedge \beta = - \beta \wedge \alpha.
>$$
>
>(iii) Plus généralement, si $\alpha_1 , \cdots , \alpha_p \in V^\ast$ et si $v_1 , \cdots , v_p \in V$,
>$$
>\alpha_1 \wedge \cdots \wedge \alpha_p (v_1 , \cdots , v_p ) = \left \vert \begin{array}{ccc} \alpha_1(v_1) & \cdots & \alpha_1(v_p) \\ \vdots & & \vdots \\ \alpha_p(v_i) & \cdots & \alpha_p(v_p) \end{array}\right \vert.
>$$
>
>(iv) Si $\alpha \in V^\ast$ et $\beta \in \Lambda^2 V^\ast$, $\forall u , v , w \in V$ ,
>$$
>\alpha \wedge \beta ( u , v , w) = \alpha(u) \beta (v , w) + \alpha(v) \beta(w ,u ) + \alpha(w) \beta(u,v).
>$$

Le produit extérieur n’est pas une loi de composition interne. Pour y remédier il suffit de rassembler tous les $\Lambda^p V^\ast$.

## Formes différentielles et champs de vecteur sur un ouvert de $\mathbb R^m$
<a id="formes-diff"></a>
### Définitions

> [!note]- Définition ($\Omega^p (U)$ : Espace vectoriel des p-formes différentielles sur un ouvert de $\mathbb R^m$ et $\Omega^\bullet (U) \equiv \oplus_{p = 0}^m \Omega^p(U)$)
> Soit $U$ un ouvert de $\mathbb R^m$, $p \in \mathbb N$. Une p-forme différentielle $\alpha$ sur $U$ est une application régulière 
> $$
> \alpha \, \colon \,  U \longrightarrow \Lambda^p (\mathbb R^m)^\ast
> $$
> Pour tout $M \in U$, on note $\alpha_M \in  \Lambda^p (\mathbb R^m)^\ast$ la valeur de $\alpha$ en $M$. On note $\Omega^p(U)$ l’espace vectoriel des p-formes différentielles sur $U$ et on pose $\Omega^\bullet (U) \equiv \oplus_{p = 0}^m \Omega^p(U)$.

Il est naturel de définir en même temps l’espace des champs de vecteur.

>[!note]- Définition ($X(M)$ la valeur d’un champ de vecteur $X \in X (U)$ en un point $m \in U$)
>Soit $U$ un ouvert de $\mathbb R^m$. Un champ de vecteur sur $U$ est une application régulière 
>$$
>X \, \colon \,   U \longrightarrow \mathbb R^m.
>$$
>On note $X(M)$ la valeur d’un champ de vecteur $X \in X (U)$ en un point $M \in U$. On note $\mathcal X (U)$ l’espace vectoriel des champs de vecteurs sur $U$.


**Produits extérieurs et intérieurs** 
Les opérations de produit extérieur et de produit intérieur définies précédemment s’étendent de façon immédiate aux formes différentielles extérieures et aux champs de vecteur. 
—  Si $\alpha \in \Omega^p (U)$  et $\beta \in  \Omega^q (U)$, le produit extérieur de $\alpha$ par $\beta$ est la (p + q)-forme $\alpha \wedge \beta \in \Omega^{p+q} (U)$ définie par 
$$
\forall M \in U \, \colon \, (\alpha \wedge \beta)_M = \alpha_M \wedge \beta_M .
$$
— Si $\alpha \in \Omega^p(u)$ et $X\in \mathcal X(U)$, le produit intérieur de $X$ par $\alpha$ est la ($p − 1$)-forme $X \,  \lrcorner \, \alpha \in \Omega^{p-1} (U)$ définie par
$$
\forall M \in U\, \colon \,  (X \, \lrcorner \, \alpha )_M = X(M) \, \lrcorner  \, \alpha_M.
$$


### Deux exemples fondamentaux de formes différentielles extérieures

L’exemple le plus simple d’une forme différentielle sur un ouvert $U$ est une forme de degré $0 $: comme $\Lambda^0(\mathbb R^m)^\ast$ s’identifie à $\mathbb R$, une $0$-forme est simplement une fonction de $U$ dans $\mathbb R$. Un autre exemple simple consiste à partir d’une fonction $\varphi$ définie sur $U$, à valeurs dans $\mathbb R$ et de classe $\mathcal C^1$ (*i.e.* dans $\mathcal C^1 (U)$). Alors, en tout point $M \in U$, la différentielle de $\varphi$ en $M$
$$
\begin{array}{rcrcl}
d\varphi_M & \colon & \mathbb R^m & \longrightarrow & \mathbb R \\
& & \xi \equiv ( \xi_1 , \cdots , \xi_m) & \longmapsto & \displaystyle \sum_{i = 1}^m \xi_i \frac{\partial \varphi}{\partial x_i }(M)
\end{array}
$$
est un élément de $(\mathbb R^m)^\ast = \Lambda^1 (\mathbb R^m)^\ast$ et donc l’application différentielle $d\varphi : M \mapsto  d\varphi_M$ est une $1$-forme.

Ces deux exemples sont fondamentaux. A partir d’eux et en utilisant le produit extérieur $\Omega^p(U) \times \Omega^q(U)  \rightarrow  \Omega^{p+q}(U)$), il est possible de reconstituer toutes les $p$-formes différentielles sur un ouvert de $\mathbb R^m$ et pour tout $p$. De plus l’application
$$
\begin{array}{rcrcl}
d & \colon & \Omega^0(U) & \longrightarrow & \Omega^1(U) \\
& & f & \longmapsto & df
\end{array}
$$

conduit, via une extension sur $\Omega^\bullet (U) = \oplus_{p = 0}^m \Omega^p (U)$, à la construction de la *différentielle extérieure*, objet central dans le calcul différentiel extérieur.

# Les variétés

# Opérations sur les formes différentielles

>[!info]- Proposition (Règle de Leibniz graduée)
> Soit $U$ un ouvert de $\mathbb R^m$. Soit $\alpha \in  \Omega^p (U)$ et $\beta \in  \Omega^q (U)$, alors 
> $$
> d(\alpha \wedge  \beta) = d\alpha \wedge \beta  + (−1)^p \alpha  \wedge d\beta .
> $$

>[!info]- Théorème ($dd = 0$)
>Pour tout $\alpha \in \Omega^p (U)$, on a :
>$$
>d(d\alpha) = 0.
>$$



