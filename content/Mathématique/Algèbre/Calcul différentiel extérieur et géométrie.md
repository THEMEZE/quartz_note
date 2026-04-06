---
title: Calcul différentiel extérieur et géométrie
tags:
  - Science
---
[Frédéric Hélein M2 Calcul différentiel extérieur et géométrie](https://webusers.imj-prg.fr/~frederic.helein/caldiffext.pdf)


# Les bases du calcul différentiel extérieur
## L’algèbre extérieure

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
>Nous conviendrons que $\Lambda^p V^\ast = \mathbb R$, autrement dit une **0-forme sur $V$** est un nombre réel.

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

>[!example]
>(i) Si $\alpha \in \Lambda^0 V^\ast = \mathbb R $ et si $\beta \in \Lambda^q V^\ast$, $\alpha \wedge \beta = \alpha \beta $,  expression dans laquelle le scalaire $\alpha$ multiple la q-forme $\beta$.
>	








> **Preuve.**  
>  
> $$  
> \begin{aligned}  
> (x+y)^3 &= (x+y)(x+y)^2 \\  
> &= (x+y)(x^2 + 2xy + y^2) \\  
> &= x^3 + 3x^2y + 3xy^2 + y^3  
> \end{aligned}  
> $$

>

