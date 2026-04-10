---
title: Algèbre totale des formes différentielles à valeurs dans une super-algèbre de Lie
tags:
  - Science
---

# 1. Cadre général

> [!note]- On définit l’algèbre totale - $\mathcal{E} \equiv  \Omega^\bullet(U) \otimes \mathfrak g  $
>On travaille sur un ouvert $U \subset \mathbb{R}^m$ .
>On définit l’algèbre totale :
>$$
>\mathcal{E} \equiv  \Omega^\bullet(U) \otimes \mathfrak g  
>$$
>où :
>- $\Omega^\bullet(U)$ : formes différentielles (cf [Voir la section](Calcul-differentiel-exterieur-geometrie.md#formes-diff) ) 
>- $\mathfrak g$ : super-algèbre de Lie (cf [[Super-algèbre de Lie]])

Une **super-connexion** s’écrit :
$$
\mathcal A = \omega + e + \psi \in \Omega^1(U)\otimes \mathfrak g  
$$
(voir [[Connexion et courbure en supergravité]])
# 2. Formes différentielles

## Définition

Une p-forme est une application :
$$
\alpha : (TU)^p \to \mathbb{R}  
$$
telle que :
- multilinéaire
- alternée

(cf [Voir la section](Calcul-differentiel-exterieur-geometrie.md#algebre-ext))
## Base locale
$$
\alpha = \sum \alpha_{i_1 \cdots i_p}(x), dx^{i_1} \wedge \cdots \wedge dx^{i_p}  
$$
où :
- $dx^i$: base duale de ${ \displaystyle \frac{\partial}{\partial x^i}}$


# 3. Produit extérieur

## Définition
$$ 
\wedge : \Omega^p \times \Omega^q \to \Omega^{p+q}  
$$
(cf [Voir la section](Forme-différentielle.md#opérations-algébrique))
(cf [Voir la section](Calcul-differentiel-exterieur-geometrie.md#algebre-ext))

## Propriétés

### (1) Associativité
$$ 
(\alpha \wedge \beta)\wedge \gamma = \alpha \wedge (\beta \wedge \gamma)  
$$
### (2) Commutativité graduée

$$
\alpha \wedge \beta = (-1)^{pq} \beta \wedge \alpha  
$$

# 4. Degré et parité (Grassmann)

Pour $\alpha \in \Omega^p$ :
$$
|\alpha| = p \quad \text{(degré)}  
$$
Parité :
$$
\tilde{\alpha} = p \mod 2  
$$
# 5. Dérivée extérieure

## Définition
$$ 
d : \Omega^p \to \Omega^{p+1}  
$$

## Expression locale
$$
d\alpha =  
\sum_i \frac{\partial \alpha}{\partial x^i} dx^i \wedge (\cdots)  
$$
## Propriétés

### (1) Nilpotence
$$
d^2 = 0  
$$
### (2) Règle de Leibniz graduée
$$
d(\alpha \wedge \beta) = d\alpha \wedge \beta  +  (-1)^p \alpha \wedge d\beta  
$$
#  6. Produit intérieur (contraction)

Soit ( $X \in \mathfrak X(U)$ ).

## Définition
$$
\iota_X : \Omega^p \to \Omega^{p-1}  
$$
## Propriétés

### (1) Dérivation (Cartan)
$$
\iota_X(\alpha \wedge \beta)=\iota_X \alpha \wedge \beta  +  (-1)^p \alpha \wedge \iota_X \beta  
$$
# 7. Lemme de Cartan

## Dérivée de Lie
$$
\mathcal L_X = d \iota_X + \iota_X d  
$$

#  8. Interprétation opératorielle

On identifie :
- $\alpha \in \Omega^\bullet$ avec $L_\alpha : \beta \mapsto \alpha \wedge \beta$
Alors :
$$
d\alpha = [d,\alpha\}  
$$
où :
$$
[A,B\} = AB - (-1)^{|A||B|} BA  
$$

#  9. Crochet gradué (général)

Définition universelle :
$$
[A,B\} = AB - (-1)^{|A||B|} BA  
$$
## Propriétés

### (1) Antisymétrie graduée
$$
[A,B\} = -(-1)^{|A||B|}[B,A\}  
$$
### (2) Identité de Jacobi graduée
$$ 
[A,[B,C\}\} = [[A,B\},C\} + (-1)^{|A||B|}[B,[A,C\}\}  
$$
# 10. Super-algèbre de Lie

Dans $ \mathfrak g $ :
$$
[X,Y\} = XY - (-1)^{|X||Y|} YX  
$$
# 11. Produit total dans $\Omega^\bullet \otimes \mathfrak g $

Pour $\alpha \otimes X $, $ \beta \otimes Y$ :
$$
(\alpha \otimes X)(\beta \otimes Y)=  
(\alpha \wedge \beta)\otimes (XY)  
$$
# 12. Crochet total
$$
[\alpha \otimes X, \beta \otimes Y\}  = (\alpha \wedge \beta)\otimes [X,Y\}  
$$

#  13. Connexion et courbure

## Connexion
$$ 
\mathcal A \in \Omega^1(U)\otimes \mathfrak g  
$$
## Courbure
$$
F = d\mathcal A + \tfrac12[\mathcal A,\mathcal A\}  
$$

## Différentielle covariante
$$
D = d + \mathcal A  
$$

## Propriétés fondamentales
$$
D^2 = F  
$$
$$
DF = 0 \quad \text{(identité de Bianchi)}  
$$

---

#  14. Résumé conceptuel
$$ 
\Omega^\bullet(U)\otimes \mathfrak g = \text{algèbre graduée différentielle + super-Lie}  
$$

avec :

- degré de forme
- degré de Grassmann
- produit wedge + produit de Lie
- commutateur gradué unifié


#  15. Point clé

Il existe **trois niveaux** :

1. Formes : ( \Omega^\bullet(U) )
2. Super-algèbre : ( \mathfrak g )
3. Algèbre totale : mélange des deux

$$
\text{Toute la structure vient d’un seul principe : le commutateur gradué}  
$$
