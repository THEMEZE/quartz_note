---
title: Algèbres graduées, formes différentielles et structure de superalgèbre de Lie
tags:
  - Science
---

---

# 1. Algèbre graduée

(cf [[Algèbre graduée|Définition]] pour une définition plus détailler de Algèbre graduée )

On définie  $E^p$ un espace vectoriel  sur un corps $\mathbb K$ (cf [Corps](Algèbre.md#Corps)). 

>[!example]-
>En particulier, ici on pense à :
>- L’ensemble des **p-formes sur $V$** forme un espace vectoriel, que l’on note $\Lambda^p V^\ast$ où $V$ désigne un espace vectoriel et on note $V^\ast$ son dual (cf [Espace vectoriel des $p$-formes différentielles sur un ouvert de $\mathbb R^m$ ](Calcul-differentiel-exterieur-geometrie.md#algebre-ext)).
>- L'espace vectoriel des **p-formes différentielles sur un ouvert  $U \subset \mathbb R^m$**  noté $\Omega^p(U)$  (cf [Formes différentielles et champs de vecteur sur un ouvert de $\mathbb R^m$ ](Calcul-differentiel-exterieur-geometrie.md#formes-diff))
>- L'ensemble de élément de parité de Grasmann paire ou impaire $\mathfrak g_{i \mod 2}$ (cf [[Super-algèbre de Lie]])
>- On vera aussi l'espace vectorielle des application linéaire de dégrès $k$ de $E^p$ dans $E^{p+k}$ de dégrés $p$ : $\mathcal L^k (E^p , E^{p+k})$ acec $E^p \in \{ \Lambda^p V^\ast , \Omega^p(U) , \mathfrak g_{i \mod 2} \}$.

>[!success]-  $(E^p, +)$ est un *groupe  additif abélien*.
>- $(E^p, +)$ est un groupe abélien  (cf [Groupes](Algèbre.md#Groupes)))

>[!note]- Définition des opérateur mutiplicative externe $\ast$
>On suppose donnée une application bilinéaire :
>$$
>\ast : E^p \times E^q \longrightarrow E^{p+q}
>$$
>
>satisfaisant :
>
>- bilinéarité
>- associativité [exemple $\wedge$](Calcul-differentiel-exterieur-geometrie.md#algebre-ext)
>- compatibilité au degré
>
>>[!example]- 
>>- Pour $E^p \in \{  \Lambda^p V^\ast , \Omega^p(U) ,  \Lambda^p \mathfrak g_{i \mod 2}^\ast \} $, l'opérateur $\ast$ est notée $\wedge$ définie en [Définition](Calcul-differentiel-exterieur-geometrie.md#algebre-ext).
>>- Pour $E^p = \mathfrak g_{i \mod 2}$,  l'opérateur $\ast$ est la multiplication/composition notée $\cdot$.
>>- Dans $E^p = \mathcal L^p(E^k , E^{k+p} )$, l'opérateur $\ast$ est la multiplication/composition notée $\circ$.

> [!failure]- $E^p$ non-stable pas $\ast$
> **Remarque fondamentale**
>
>Pour un degré fixé $p$,
>$$
>E^p \ast E^p \subset E^{2p} \neq E^p
>$$
>donc :
>$$
>(E^p, +, \ast) \text{ n’est pas un anneau en général.}
>$$
>
> - il n’y a pas, en général, de structure multiplicative interne sur $E^p$

>[!note]- Définition (Produit intérieur $\, \lrcorner \, $ )
>Pour toute p-forme $\alpha \in E^p$  et pour tout vecteur $\xi \in Y$ ( avec $Y = V , \mathcal X(U) , \mathfrak g_i$  si respectivement $E^p = \Lambda^p V^\ast , \Omega^p ,   \Lambda^p \mathfrak g_i ^\ast$ (cf [produit interieur](Calcul-differentiel-exterieur-geometrie.md#algebre-ext))) , on définit le **produit intérieur** de $\alpha$ par $\xi$ comme étant la (p − 1)-forme notée $\iota_\xi \alpha$ ou $\xi \, \lrcorner \,   \alpha \in E^{p−1}$ définie par 
>$$
>\forall v_2 , \cdots , v_p \in Y \, \colon \, \iota_\xi \alpha (v_2 , \cdots , v_p ) = \alpha ( \xi , v_2 , \cdots ,v_p ).
>$$
>Si $p = 0$ et si $\alpha \in E^0= \mathbb R $ , on convient de poser $\iota_\xi \alpha = 0$. Alors l’application 
>$$
>\begin{array}{rcrcl}
>\lrcorner & \colon & Y \times E^p & \longrightarrow & E^{p-1}  \\
>&& (\xi , \alpha) & \longmapsto & \iota_\xi \alpha
>\end{array}
>$$
> est bilinéaire. On peut d’ailleurs l’étendre de façon unique en une application bilinaire de $Y \times E^\bullet $ vers $E^\bullet$ . Le produit intérieur satisfait en outre les propriétés suivantes. 
> (cf [produit interieur](Calcul-differentiel-exterieur-geometrie.md#algebre-ext))) 
> o
>> [!info]- Proposition
>> 
>>$\forall \xi , \eta \in V \, \colon \,  \forall \alpha \in \Lambda^p V^\ast\, \colon \, $ 
>> $$
>> \iota_\xi \iota_\eta \alpha + \iota_\eta \iota_\xi \alpha = 0,
>> $$
>> donc en particulier 
>> $$
>> \iota_\eta \iota_\eta \alpha = 0.
>> $$
> 


>[!note]- Définition  (Parité / Degrès de Grassmann - $\quad   \vert   \bullet \vert \, \colon \,  E^p \ni x \mapsto p \in \mathbb Z $) 
>(cf [[Super-algèbre de Lie|Déf app degrès]] pour une définition restrainte à la super-algèbre de Lie)

>[!note]- Définition  ( Opérateurs gradués ) 
>
>On définie l'opérateur $T$ de dégrè $k$ : 
>$$
>\mathcal L^k (E^p , E^{p+k}) \ni T \, \colon \, E^p \longrightarrow E^{p+k}
>$$
>avec $E^p \in \{ \Lambda^p V^\ast , \Omega^p(U) , \mathfrak g_{i \mod 2} , \mathcal L^p (E^k , E^{k+p} ) \}$.
>
>>[!example]-
>>- $\mathcal L^k (E^p , E^{p+k}) \ni \varepsilon(\alpha) \, \colon \, E^p \in x  \longmapsto \alpha \ast x \in  E^{p+k}$ avec $\alpha \in E^{k}$.
>>- $\mathcal L^1 (E^p , E^{p+1}) \ni d \, \colon \, E^p \in x  \longmapsto d \ast x \in  E^{p+1}$ avec $ E^{p} \in \{ \Lambda^p V^\ast ,  \Lambda^p \mathfrak g_{i \mod 2} ,  \Omega^p(U)  ,  \mathcal L^p (E^k , E^{k+p})\} $.
>>- $\mathcal L^{-1} (E^p , E^{p-1}) \ni \iota_\xi \, \colon \, E^p \in x  \longmapsto \iota_\xi \ast x \in  E^{p-1}$ avec $ E^{p} \in \{ \Lambda^p V^\ast ,  \Lambda^p \mathfrak g_{i \mod 2} ,  \Omega^p(U)  ,  \mathcal L^p (E^k , E^{k+p})\} $ et $\xi \in Y $ définie plus haut  (cf [produit interieur](app://obsidian.md/Calcul-differentiel-exterieur-geometrie.md#algebre-ext))). 

>[!info]- Les deux opérateurs fondamentaux (Création/Annihilation)
>
>>[!note]- Création $\varepsilon(\alpha)[\beta] = \alpha \ast \beta$ 
>>$$
>>\mathcal L^k (E^p , E^{p+k}) \ni \varepsilon(\alpha) \, \colon \, E^p \in x  \longmapsto \alpha \ast x \in  E^{p+k}$ avec $\alpha \in E^{k}.
>>$$
>
>>[!note]- Annihilation $\iota_\xi \circ \alpha $
>>$$
>>\mathcal L^{-1} (E^p , E^{p-1}) \ni \iota_\xi \, \colon \, E^p \in x  \longmapsto \iota_\xi \ast x \in  E^{p-1}
>>$$
>> avec $ E^{p} \in \{ \Lambda^p V^\ast ,  \Lambda^p \mathfrak g_{i \mod 2} ,  \Omega^p(U)  ,  \mathcal L^p (E^k , E^{k+p})\} $ et $\xi \in Y $ définie plus haut  (cf [produit interieur](app://obsidian.md/Calcul-differentiel-exterieur-geometrie.md#algebre-ext))). 
>> *   diminue le degré.
>
>>[!question]- Pourquoi “création / annihilation” ?
>>
>>Parce qu’ils satisfont exactement une **algèbre de type fermionique**.
>>f
>>Si  $\alpha \in V^*$ ,  $X \in V$ , alors :
>>$$
>>\iota_X (\alpha) = \alpha(X)
>>$$
>>et surtout :
>>$$
>>\iota_X (\alpha \wedge \omega) = \alpha(X)\,\omega - \alpha \wedge \iota_X \omega
>>$$
>>
>>👉 ce qui implique la relation clé :
>>
>>$$
>>\{\iota_X, \alpha \wedge\} = \alpha(X)
>>$$
>
>>[!note]- Interprétation fermionique
>>
>>Compare avec les opérateurs de Fock :
>>
>>| géométrie différentielle | Fock fermionique |
>>| --- | --- |
>>|  $\alpha \wedge$  |  $a^\dagger$  (création) |
>>|  $\iota_X$  |  $a$  (annihilation) |
>>
>>et :
>>
>>$$
>>\{a, a^\dagger\} = 1
>>$$
>>
>>👉 exactement la même structure !
>>
>
>
>>[!node]- Lecture physique
>>
>>
>>Une  $p$ \-forme :
>>
>>$$
>>\omega = \alpha_1 \wedge \cdots \wedge \alpha_p
>>$$
>>
>>\= état avec  $p$  “particules fermioniques”
>>
>>*    $\alpha \wedge$  : ajoute une particule
>>*    $\iota_X$  : en enlève une
>>
>>👉 d’où :
>>
>>*   **création** = wedge
>>*   **annihilation** = contraction
>
>
>
>>[!question]- Pourquoi fermionique ?
>>
>>
>>Parce que :
>>
>>$$
>>\alpha \wedge \beta = - \beta \wedge \alpha
>>$$
>>
>>👉 antisymétrie ⇒ statistique fermionique
>>
>>Donc :
>>
>>$$
>>(\alpha \wedge)^2 = 0
>>$$
>>
>>comme :
>>
>>$$
>>(a^\dagger)^2 = 0
>>$$
>
>
>>[!tip]- Vision algébrique propre
>>
>>
>>On a une représentation de l’algèbre de Clifford :
>>
>>$$
>>\mathrm{Cl}(V \oplus V^*)
>>$$
>>
>>avec :
>>
>>$$
>>c(\alpha) = \alpha \wedge + \iota_{g^{-1}(\alpha)}
>>$$
>>
>>👉 c’est la construction derrière :
>>
>>*   spineurs
>>*   Dirac
>>*   supersymétrie
>
>
>
>>[!abstract]- Conclusion
>>
>>
>>✔️ On dit :
>>
>>*   **création** :  $\alpha \wedge$ 
>>*   **annihilation** :  $\iota_X$ 
>>
>>👉 parce qu’ils vérifient :
>>
>>*   une **algèbre d’anticommutation fermionique**
>>*   une **variation du degré ±1**
>>*   une **interprétation en espace de Fock**
>
>
>
>>[!abstract]- Point subtil (important)
>>
>>
>>Ce n’est pas juste une analogie :
>>
>>👉  $\Lambda^\bullet V^*$  **est** un espace de Fock fermionique
>>

>[!info]- Différentielle extérieure $d$
>$$
>d : E^p\to E^{p+1},
>$$
>pour $E^p \in \{ \Lambda^p V^\ast , \Lambda^p \mathfrak g_i^\ast , \Omega^p(U) \}$.
>
>- degré : \(+1\)
>- nilpotent d'ordre 2 :
>$$
>d^2 = 0
>$$
>(cf [différentiel extérieur](app://obsidian.md/Calcul-differentiel-exterieur-geometrie.md#algebre-ext)))

>[!info]- Proposition (règle de Leibniz graduée)
>Pour  $E^p \in \{ \Lambda^p V^\ast , \Lambda^p \mathfrak g_i^\ast , \Omega^p(U) \}$
>le priduit interieur et et la deriver exterieurs satifont la régle de Liebniz graduée :
>$$ 
>\iota_\xi(\alpha \ast  \beta ) = (\iota_\xi \circ \alpha ) \ast\beta + (-1)^p \alpha \ast( \iota_\xi \circ  \beta)
>$$
>$$
>d(\alpha \ast \beta ) = (d \circ \alpha )\ast \beta + (-1)^p \alpha \ast ( d \circ \beta)
>$$
>(cf [[Calcul-differentiel-exterieur-geometrie]])
>
>>[!question]- $\forall ( \alpha , \beta , T )  \in E^i \times E^j \times \mathcal L(E^{i+j} , E^{i+j+k}) \, \colon \, T(\alpha \ast \beta ) = T(\alpha) \ast \beta + (-1)^{\vert T \vert \vert \alpha \vert } \alpha \ast T(\beta) $ ?
>>
>>
>
>

>[!info]- Super-commutateur $[x,y\}$
>
>Sur toute algèbre graduée associative (même dans l'espace des opérateur linéaire gradué d'oredre $k$ ( $\mathcal L^k(E^p , E^{p+k})$) on définit le **super-commutateur** :
>$$
>[x,y\} = x \ast y - (-1)^{|x||y|} y \ast x
>$$
>
>Il vérifie :
>
>>[!note]- antisymétrie graduée ou **Super anti-symétrie**:  
>>$$
>>{\displaystyle \forall (x,y)\in E^i\times E^j\; \vert \; (i , j) \in \mathbb Z^2 \, \colon \quad [x,y\} =-(-1)^{|x||y|}[y,x\}}
>>$$
>
>>[!note]- identité de Jacobi graduée ou **Super-[relation de Jacobi](https://fr.wikipedia.org/wiki/Relation_de_Jacobi "Relation de Jacobi")**  
>>$$
>>{\displaystyle \forall (x,y,z) \in E^i \times  E^j \times  E^k \; \vert \;  (i, j , k) \in \mathbb Z^3  \, \colon  \quad (-1)^{|x||z|}[x,[y,z\}\} +(-1)^{|y||x|}[y,[z,x\}\} +(-1)^{|z||y|}[z,[x,y\}\} =0}
>>$$
>
>(cf [[Super-algèbre de Lie|Déf $\vert \bullet \vert $]] pour une définition restrainte à la super-algèbre de Lie)
>
>
>>[!note]- (Règle de Leibniz graduée pour $E^p \ni y \mapsto [x , y \} $ avec $ x \in E^i$)
>>$$
>>{\displaystyle \forall (x,y,z) \in E^i \times  E^j \times  E^k \; \vert \;  (i, j , k) \in \mathbb Z^3  \, \colon  \quad [ x , y \ast z \} = [ x , y \}\ast z + (-1)^{\vert x \vert \vert y \vert  } \, y \ast [ x , z \}}
>>$$

>[!node]- Super-commutative
>
>Si $E^pt$ est *super-commutative* (ex : $\Lambda^\bullet V^*$, $\Omega^\bullet(U)$) :
>
>$$
>[x,y\} = 0
>$$
>(cf [Proposition  (Le produit extérieur est commutatif gradué ](Calcul-differentiel-exterieur-geometrie.md#algebre-ext) pour $x , y \in \Lambda^p V^\ast$) 
>
>
>La structure de Lie est alors **triviale** ( sans *dynamique*) .
>

>[!note]- Dérivée de Lie
>
 >$\mathcal{L}_X = [d, \iota_X]$ 
>
>*   degré  $0$ 

>[!note] Relations fondamentales (Cartan)
>
>$$
>[ \varepsilon , \varepsilon  \} = 0
>$$
>
>$$
>[ \iota , \iota \} = 0
>$$
>
>$$
>[\iota_X, \varepsilon(\alpha) \} = \alpha(X)
>$$
>
>$$
>[d,d\} = 0
>$$
 >
>$$
>[d,\iota_X\} = \mathcal L_X
>$$
 >
>$$
>[\mathcal L_X,\iota_Y\} = \iota_{[X,Y]}
>$$
>
>👉 C’est **une vraie super-algèbre de Lie**.


# 2. Espace vectoriel gradué

Soit un espace vectoriel gradué :
$$
E^\bullet = \bigoplus_{p \in \mathbb{Z}} E^p
$$
Chaque composante $E^p$ est un espace vectoriel sur un corps $\mathbb K$ (cf [Corps](Algèbre.md#Corps)). En particulier :

- $(E^p, +)$ est un groupe abélien  (cf [Groupes](Algèbre.md#Groupes)))
- il n’y a pas, en général, de structure multiplicative interne sur $E^p$

Alors :

$$
(E^\bullet, +, \ast)
$$
est une **algèbre graduée**, **anneau gradué** , **algèbre associative**, **supercommutative** .


>[!example]- Exemples fondamentaux
>
>>[!note]- Algèbre extérieure
>>
>>$$
>>E^\bullet = \Lambda^\bullet V^*
>>$$
>>(cf [[Forme-différentielle]] et [[Calcul-differentiel-exterieur-geometrie]])
>>- produit : $\wedge$
>>- algèbre graduée
>>- associative
>>- supercommutative :
>>$$
>>\alpha \wedge \beta = (-1)^{|\alpha||\beta|} \beta \wedge \alpha
>>$$
>
>
>>[!note]- Formes différentielles
>>
>>$$
>>E^\bullet = \Omega^\bullet(U)
>>$$
>>
>>avec :
>>$$
>>\Omega^p(U) = \mathcal C^\infty(U, \Lambda^p(\mathbb{R}^m)^*)
>>$$
>>
>>- produit : $\wedge$ (point par point)
>>- algèbre graduée sur $\mathcal C^\infty(U)$
>>(cf [Espace vectoriel des $p$-formes différentielles sur un ouvert de $\mathbb R^m$ ](Calcul-differentiel-exterieur-geometrie.md#formes-diff))
>
>
>>[!note]- Superalgèbre
>>$$
>>E^\bullet = \mathcal A = \mathcal A_0 \oplus \mathcal A_1
>>$$
>>- produit : $\cdot$
>>- graduation modulo 2
>>
>>(cf [[Super-algèbre de Lie]])
>>
>
>
>>[!note]- Endomorphismes
>>
>>$$
>>E^\bullet = \mathrm{End}(F^\bullet)
>>$$
>>
>>- produit : composition $\circ$
>>- algèbre graduée par le degré des opérateurs
>>
>


>[!info]- Superalgèbre de Lie
>
>Ainsi :
>$$
>(E^\bullet, [\ ,\ \})
>$$
>est une **superalgèbre de Lie**.
>
>
>
>>[!note]- Cas particulier
>>
>>Si $E^\bullet$ est supercommutative (ex : $\Lambda^\bullet V^*$, $\Omega^\bullet(U)$) :
>>
>>$$
>>[x,y\} = 0
>>$$
>>(cf [Proposition  (Le produit extérieur est commutatif gradué ](Calcul-differentiel-exterieur-geometrie.md#algebre-ext) pour $x , y \in \Lambda^p V^\ast$) 
>>
>>La structure de Lie est alors **triviale** ( sans *dynamique*) .
>


>[!info]- Endomorphismes homogènes gradués
>
>On considère :
>
>$$
>\mathcal L^\bullet(E^\bullet) = \bigoplus_{k \in \mathbb{Z}} \mathcal L^k(E^\bullet)
>$$
>
>où :
>$$
>T \in \mathcal L^k(E^\bullet) \iff T : E^p \to E^{p+k}
>$$
>
>Alors :
>
>- $(\mathcal L^\bullet(E^\bullet), + , \circ)$ est une algèbre graduée
>- $(\mathcal L^\bullet(E^\bullet), +, [\ ,\ \})$ est une superalgèbre de Lie non triviale
>


>[!note]- Interprétation fermionique
>
>On identifie :
>
>$$
>\Lambda^\bullet V^* \simeq \text{espace de Fock fermionique}
>$$
>
>avec :
>
>| Structure mathématique | Interprétation physique  |
>| ----------------------- | ------------------------ |
>| \(\varepsilon\)        | opérateur de création    |
>| \(\iota\)               | opérateur d’annihilation |
>| degré                   | nombre de fermions       |
>| \(d\)                   | supercharge              |


>[!info]- Structure globale
>
>On distingue deux niveaux :
>
>### Niveau 1 : algèbre graduée
>
>$$
>(E^\bullet, + , \ast)
>$$
>
>### Niveau 2 : superalgèbre de Lie
>
>$$
>(\mathcal L^\bullet(E^\bullet), + ,  [\ ,\ \})
>$$
>
>

>[!info]- Conclusion
>
>- Chaque $E^p$ est un espace vectoriel (*groupe abélien*)
>- seule la somme graduée $E^\bullet$ porte une *structure d’algèbre*
>- les objets *super-commutatifs* ont une structure de Lie triviale
>- la structure dynamique apparaît dans les endomorphismes
>- la géométrie différentielle réalise une représentation fermionique naturelle


# 3. Quelques applications linéaires graduées sur  super-algèbre Lie

On se place dans une **super-algèbre de Lie**  $\mathfrak{g}$  (ou plus généralement une super-algèbre associative graduée), avec le **super-commutateur** :

$$
[a,b\} = a\ast b - (-1)^{|a||b|} b \ast a
$$

et une dérivation homogène  $d$  de degré  $|d|$ , satisfaisant la règle de Leibniz graduée :

$$
d(a\ast b) = d(a)\ast b + (-1)^{|d||a|} a \ast d(b)
$$

## Opérateur linéaire graduée d'ordre $k$  sur  $a^n$ 
On suppose  $a$  homogène.

On note $a^n$, la loi "$\ast$" est associative donc l'ecriture
$$
a^n = \underbrace{a\ast \cdots \ast a }_{\text{n termes}},
$$
à un sens.

Par récurrence avec Leibniz gradué :

$$
\forall (n , p, a , T ) \in  \mathbb N \times \mathbb Z \times E^p \times \mathcal L^k(E^\bullet) \,  \colon \,  T(a^n) = \sum_{k=0}^{n-1} (-1)^{|T||a|k} \, a^k  \ast T(a) \ast a^{n-1-k},
$$
où $E^p$ peut étre aussi $\mathcal L^k(E^\bullet)$.
>[!tip]- Autre écritures
>Sans se perdre dans les notations de comutations, juste en faisant des manupulation d'indice on peut écrire par exemple:
>$$
>T(a^n) = \sum_{k=1}^{n} (-1)^{|T||a|k} \, a^{n-k} \ast T(a) \ast  a^{k-1}
>$$

>[!success]- On reconnais ...
>👉 Cas important :
>
>*   si  $|T| = 0$  (paire) :
>    
>$$
>T(a^n) = \sum_{k=0}^{n-1} a^k \ast T(a) \ast a^{n-1-k}
>$$
>*   si  $a$  est pair ( $|a|=0$ ) :
 >   
>$$
>d(a^n) = \sum_{k=0}^{n-1} a^k\ast  d(a) \ast a^{n-1-k}
>$$
>
>👉 Si en plus  $a$  commute avec  $d(a)$  :
>
>$$
>T(a^n) = n \, a^{n-1} \ast T(a) = n \, T(a) \ast a^{n-1}
>$$

### Dérivée de  $a^n$ 

Par récurrence avec Leibniz gradué :

$$
d(a^n) = \sum_{k=0}^{n-1} (-1)^{|d||a|k} \, a^k  \ast d(a) \ast a^{n-1-k}
$$
>[!tip]- Autre écritures
>Sans se perdre dans les notations de comutations, juste en faisant des manupulation d'indice on peut écrire par exemple:
>$$
>d(a^n) = \sum_{k=1}^{n} (-1)^{|d||a|k} \, a^{n-k} \ast d(a) \ast  a^{k-1}
>$$

>[!success]- On reconnais ...
>👉 Cas important :
>
>*   si  $|d| = 0$  (dérivation paire) :
>    
>$$
>d(a^n) = \sum_{k=0}^{n-1} a^k \ast d(a) \ast a^{n-1-k}
>$$
>*   si  $a$  est pair ( $|a|=0$ ) :
 >   
>$$
>d(a^n) = \sum_{k=0}^{n-1} a^k\ast  d(a) \ast a^{n-1-k}
>$$
>
>👉 Si en plus  $a$  commute avec  $d(a)$  :
>
>$$
>d(a^n) = n \, a^{n-1} \ast d(a) = n \, d(a) \ast a^{n-1}
>$$

### Dérivée de  $d (f(a))$ 

 Si $f(x) = \sum_{n \in \mathbb Z}  a_n x^n $, tel que $a_n \in \mathbb K$,  est bien définie (algèbre complétée ou formelle) .
 
Par récurrence avec Leibniz gradué :

$$
d(f(a)) = \sum_{n=-\infty }^\infty a_n \sum_{k=0}^{n-1} (-1)^{|d||a|k} \, a^k  \ast d(a) \ast a^{n-1-k}.
$$
>[!success]- On reconnais ...
>En particulier si $a$ et $d(a)$ commutent , On définie la différentielle de $f$ en $a$ la fonction  >:
>$$
>df_a \, \colon \, h \longmapsto f'(a)\ast h,
>$$
>et 
>
>$$
>d(f\circ g)_a = df_{g(a)} \circ dg_a .
>$$

>[!example]- Applications :
>En particulier pour $f(x) = e^x$ , 
>$$
>d(e^a) = \sum_{n=0 }^\infty \frac{1}{n!} \sum_{k=0}^{n-1} (-1)^{|d||a|k} \, a^k  \ast d(a) \ast a^{n-1-k}.
>$$
>
>En particulier si $a$ et $d(a)$ commutent et  $f(x) = e^x $ et $g(x) = \lambda x $ avec $ \lambda \in \mathbb K$. On retrouve que 
>$$
>d(e^{\lambda a }) = \lambda \, e^{\lambda a }\ast d(a).
>$$

###   $[x, y^n \}$ 

Par récurrence avec Leibniz gradué :

$$
\forall (x, y , p , \ell , n  ) \in \times E^p \times E^\ell \times  \mathbb Z^2 \times \mathbb N   \,  \colon \,  [x,y^n\}  = \sum_{k=0}^{n-1} (-1)^{|x||y|k} \, y^k  \ast [x , y \} \ast y^{n-1-k}
$$
>[!tip]- Autre écritures
>Sans se perdre dans les notations de comutations, juste en faisant des manupulation d'indice on peut écrire par exemple:
>$$
>[x,y^n\} = \sum_{k=1}^{n} (-1)^{|x||y|k} \, y^{n-k} \ast [x,y\} \ast  y^{k-1}
>$$

>[!success]- On reconnais ...
>👉 Cas important :
>
>*   si  $|x| = 0$  (paire) :
>    
>$$
>[x , y^n\}  = \sum_{k=0}^{n-1} y^k \ast [x,y\}  \ast y^{n-1-k}
>$$
>*   si  $a$  est pair ( $|y|=0$ ) :
 >   
>$$
>[x , y^n\} \sum_{k=0}^{n-1} y^k \ast [x,y\}  \ast y^{n-1-k}
>$$
>
>👉 Si en plus  $y$  commute avec  $[x,y\}$  :
>
>$$
>[x , y^n\} = n \, y^{n-1} \ast [x,y\} = n \, [x,y\} \ast y^{n-1}
>$$
>
>👉 Si en plus  $y = x$  alors $[x , y\} = x\ast x -(-1)^{\vert x\vert \vert x \vert}  x\ast x  = (1 - (-1)^{\vert x \vert }) x^2$ :
>on peut donc procéder par recurrence sur $n$ , ou utiliser la définition du super-commutateur, ou mème utiliser la règle de Leibniz pour trouver que 
>$$
>[x , x^n \} = (1 - (-1)^{\vert x \vert })\,  x^{n+1}
>$$

###   $[x, f(x) \}$ , avec $f =f_{\text pair} + f_{\text impair} $ (*i.e.* $f(z)=\sum_{n \in \mathbb Z } a_{2n} z^{2n} +\sum_{n \in \mathbb Z } a_{2n+1} z^{2n+1} $) 
On peut démontrer que  si $f(x) = \sum_{n \in \mathbb Z}  a_n x^n $, tel que $a_n \in \mathbb K$,  est bien définie (algèbre complétée ou formelle) , alors :
$$
\forall x \in E^p \, \colon \, [x , f(x)\} = (1-(-1)^{\vert x \vert }) \, x \ast f_{\text{impaire}}(x) = (1-(-1)^{\vert x \vert }) \, f_{\text impaire}(x) \ast x ,
$$
avec $f_{\text{paire}} (x)= (f(x) +f(-x))/2 $ et $f_{\text impaire} (x)= (f(x) -f(-x))/2 $. et en particulers
$$
[x , f_{\text paire}(x)\} = 0.
$$
Par exemple :
$$
[x , e^{x}\} = (1-(-1)^{\vert x \vert }) \, x \ast \sinh(x) = (1-(-1)^{\vert x \vert }) \, \sinh (x) \ast x.
$$

# 4. Application $\text{Ad}_X$ et $\text{ad}_X$ sur l'algèbre et la super-algèbre le Lie

## Définition de $\text{Ad}_X$ et $\text{ad}_X$ et liens 

$$
\forall (X , Y ) \in E^\bullet \times (E^\bullet)' \, \colon, \, \text{Ad}_X(Y) = X \ast Y \ast X^{-1},
$$
et 
$$
\forall (X , Y ) \in E^\bullet \times (E^\bullet)' \, \colon, \, \text{ad}_X(Y) = [X , Y] = X \ast Y - Y \ast X ,
$$

Et 
$$
\forall X \in E^\bullet  \, \colon, \, \text{Ad}_{e^X} =  e^{\text{ad}_{X}},
$$
ou $E^\bullet$ et $(E^\bullet)'$ peuvent etre différent algèbres graduée (même un ensemble d' application linéaire graduées sur un ensemble graduée ). 

(cf [Wifi Baker–Campbell–Hausdorff formula](https://en.wikipedia.org/wiki/Baker%E2%80%93Campbell%E2%80%93Hausdorff_formula) , [Wiki Derivative of the exponential map
](https://en.wikipedia.org/wiki/Derivative_of_the_exponential_map), [Wiki Adjoint representation](https://en.wikipedia.org/wiki/Adjoint_representation#Adjoint_representation_of_a_Lie_algebra), [Wiki Stone–von Neumann theorem](https://en.wikipedia.org/wiki/Stone%E2%80%93von_Neumann_theorem) , [Wiki Tetrad formalism](https://en.wikipedia.org/wiki/Tetrad_formalism))

>[!question]- Pourquoi $\text{Ad}_{e^X} = e^{\text{ad}_X}$ ?
>Soit $f(s)[Y] = \text{Ad}_{e^sX}(Y) = e^{sX} \ast  Y \ast   e^{-sX}$, 
>$$
>\frac{d f}{ds}(s)[Y] = \frac{d e^{sX}}{ds}  \ast  Y \ast   e^{-sX} + e^{sX}  \ast  Y \ast   \frac{d e^{-sX}}{ds},
>$$
>car $d/ds$ est paire $\vert d/ds \vert = 0 \mod 2 $ . Et $X$ et  $d(sX)/ds = X $ commutent alors 
>$$
>\frac{d e^{sX}}{ds} = X \ast e^{sX} = e^{sX} \ast X , \quad \frac{d e^{-sX}}{ds} = -X \ast e^{-sX} = -e^{-sX} \ast X,
>$$
>donc 
>$$
>\frac{d f}{ds}(s)[Y] = e^{sX} \ast X   \ast  Y \ast   e^{-sX} - e^{sX}  \ast  Y  \ast  X \ast   e^{-sX} = \text{Ad}_{e^{sX}}(\text{ad}_X (Y)) = f(s) [\text{ad}_X (Y)],
>$$
>et 
>$$
>\frac{d f}{ds}(s)[Y] = \ast X  \ast  e^{sX}   \ast  Y \ast   e^{-sX} - e^{sX}  \ast  Y  \ast  e^{-sX} \ast  X    = \text{ad}_{X}(\text{Ad}_{e^{sX}} (Y)) = \text{ad}_X[ f(s)[Y]] ,
>$$
>donc 
>>$$
>> [\text{Ad}_{e^{sX}} , \text{ad}_{X}  ] = 0 , \quad \& \quad  f' = \text {ad}_X(f) \quad \text{avec}\; f = \text{Ad}_{e^{sX}},
>>$$
>On peut avouer si $f(0) =1$, alors : 
>>$$
>>\text{Ad}_{e^{X}} = e^{\text{ad}_X}
>>$$
>

>[!tip]- Resoudre $f'(s) = g(f(s))$
>
>>[!info]- Cadre
>>
>>On considère :
>>
>>$$
>>f'(s) = g(f(s))
>>$$
>>
>>où :
>>
>>*    $M$  est une variété (ou une algèbre vue comme variété)
>>*    $g \in \Gamma(TM)$  est un **champ de vecteurs**
>>*    $f : I \to M$  est une courbe intégrale
>
>>[!info]- Définition du flot
>>
>>
>>Un **flot** de  $g$  est une application :
>>
>>$
>>\varphi : I \times M \to M
>>$$
>>
>>telle que :
>>- (i) équation différentielle
>>
>>$$
>>\frac{d}{ds}\varphi_s(x) = g(\varphi_s(x))
>>$$
>>- (ii) condition initiale
>>
>>$$
>>\varphi_0(x) = x
>>$$
>>
>>- (iii) propriété de groupe local
>>
>>$$
>>\varphi_{s+t} = \varphi_s \circ \varphi_t
>>$$
>
>
>
>>[!info]- Construction de la solution
>>
>>
>>Fixons une condition initiale :
>>
>>$$
>>f(0) = x_0
>>$$
>>
>>Définissons :
>>
>>$$
>>h(s) := \varphi_s(x_0)
>>$$
>>
>>
>>[!info]- Vérification que  $h$  est solution
>>
>>
>>On dérive :
>>
>>$$
>>\frac{d}{ds} h(s) = \frac{d}{ds} \varphi_s(x_0)
>>$$
>>
>>Par définition du flot :
>>
>>$$
>>\frac{d}{ds} \varphi_s(x) = g(\varphi_s(x))
>>$$
>>
>>Donc :
>>
>>$$
>>h'(s) = g(\varphi_s(x_0)) = g(h(s))
>>$$
>>
>>👉 donc :
>>
>>$$
>>h'(s) = g(h(s))
>>$$
>>
>
>
>>[!info]- Condition initiale
>>
>>
>>$$
>>h(0) = \varphi_0(x_0) = x_0
>>$$
>
>
>
>>[!info]- Unicité (théorème fondamental)
>>
>>
>>Le théorème de **Cauchy–Lipschitz (Picard–Lindelöf)** sur variétés dit :
>>
>>> Si  $g$  est suffisamment régulière (au moins  $C^1$ ), alors l’EDO
>>
>>$$
>>f' = g(f), \quad f(0)=x_0
>>$$
>>
>>admet une **unique solution locale**.
>>
>
>
>>[!info]- Conclusion logique
>>
>>
>>On a montré :
>>
>>*    $\varphi_s(x_0)$  est une solution
>>*   la solution est unique
>>
>>Donc toute solution  $f$  vérifie :
>>
>>$$
>>\boxed{ f(s) = \varphi_s(f(0)) }
>>$$
>
>
>>[!info]- Interprétation géométrique
>>
>>
>>*    $g$  = champ de vecteurs
>>*    $f(s)$  = trajectoire intégrale
>>*    $\varphi_s$  = transport le long du champ
>>
>>👉 donc :
>>
>>$$
>>\text{solution} = \text{flux du champ appliqué au point initial}
>>$$
>
>
>
>>[!info]- Lien direct avec ton cas Lie / super-Lie
>>
>>
>>Si :
>>
>>$$
>>g(x) = [a,x\}
>>$$
>>
>>alors :
>>
>>$$
>>\varphi_s(x) = e^{s\,\mathrm{ad}_a}(x)
>>$$
>>
>>donc :
>>
>>$$
>>f(s) = e^{s\,\mathrm{ad}_a}(f(0))
>>$$
>
>
>
>>[!info]-💡 10. Résumé conceptuel
>>
>>
>>$$
>>\boxed{ f' = g(f) \quad \Longleftrightarrow \quad f(s) = \text{flux de } g \text{ appliqué à } f(0) }
>>$$
>>
>
>
>>[!tip]-
>>
>>*   BCH comme **composition de flots**
>>*   ou  $e^{sa} b e^{-sa}$  comme **action de groupe vs action adjointe** (c’est exactement la même structure déguisée)
>>


>[!note]- **Baker–Campbell–Hausdorff (BCH)** via la **composition de flots**
>
>On va relier :
>
>$$
>f' = g(f) \quad \Longleftrightarrow \quad f(s)=\varphi_s(f(0))
>$$
>
>à la formule de **Baker–Campbell–Hausdorff (BCH)** via la **composition de flots**.
>
>
>
>>[!info]- Deux champs de vecteurs
>>
>>
>>Sur une algèbre de Lie (ou super-Lie), considère :
>>
>>$$
>>X(x) = [a,x\}, \qquad Y(x) = [b,x\}
>>$$
>>
>>👉 Ce sont deux champs de vecteurs (linéaires).
>>
>
>
>>[!info]-  Leurs flots
>>
>>
>>Par ce qu’on a démontré :
>>
>>$$
>>\varphi_s^X(x) = e^{s\,\mathrm{ad}_a}(x), \quad \varphi_t^Y(x) = e^{t\,\mathrm{ad}_b}(x)
>>$$
>
>
>>[!info]-  Composition des flots
>>
>>
>>On regarde :
>>
>>$$
>>\varphi_s^X \circ \varphi_t^Y (x) = e^{s\,\mathrm{ad}_a} \Big( e^{t\,\mathrm{ad}_b}(x) \Big)
>>$$
>>
>>👉 donc :
>>
>>$$
>>= \big( e^{s\,\mathrm{ad}_a} e^{t\,\mathrm{ad}_b} \big)(x)
>>$$
>
>
>
>>[!info]-  Problème central
>>
>>
>>👉 Peut-on écrire :
>>
>>$$
>>e^{s\,\mathrm{ad}_a} e^{t\,\mathrm{ad}_b} = e^{\mathrm{ad}_{Z(s,t)}}
>>$$
>>
>>pour un certain  $Z(s,t)$  ?
>>
>
>
>>[!info]- 🔥  Réponse = BCH
>>
>>
>>Oui :
>>
>>$$
>>\boxed{ e^{s\,\mathrm{ad}_a} e^{t\,\mathrm{ad}_b} = e^{\mathrm{ad}_{\mathrm{BCH}(sa,tb)}} }
>>$$
>>
>>avec :
>>
>>$$
>>\mathrm{BCH}(sa,tb) = sa + tb + \frac{1}{2}[sa,tb\} + \cdots
>>$$
>
>
>
>>[!info]-  Interprétation dynamique
>>
>>
>>👉 Composer deux flots :
>>
>>*   avancer selon  $Y$  pendant  $t$ 
>>*   puis selon  $X$  pendant  $s$ 
>>
>>équivaut à :
>>
>>$$
>>\text{un seul flot engendré par } Z = \mathrm{BCH}(sa,tb)
>>$$
>
>
>
>>[!info]-   Traduction en équation différentielle
>>
>>
>>Considère :
>>
>>$$
>>f(s,t) = \varphi_s^X \circ \varphi_t^Y (x)
>>$$
>>
>>Alors :
>>
>>*   dérivée en  $s$  → champ  $X$ 
>>*   dérivée en  $t$  → champ  $Y$ 
>>
>>Mais ces champs **ne commutent pas** :
>>
>>$$
>>[X,Y] = \mathrm{ad}_{[a,b\}}
>>$$
>
>
>
>>[!info]- 🔥  Structure profonde
>>
>>
>>👉 BCH encode le fait que :
>>
>>$$
>>\text{composer des flots non commutatifs} \neq \text{additionner les générateurs}
>>$$
>>
>>mais :
>>
>>$$
>>\boxed{ Z = a + b + \tfrac{1}{2}[a,b\} + \tfrac{1}{12}[a,[a,b\}\} - \cdots }
>>$$
>
>
>
>>[!info]-  Version groupe (plus concrète)
>>
>>
>>Dans une algèbre associative :
>>
>>$$
>>e^{sa} e^{tb} = e^{Z(s,t)}
>>$$
>>
>>et en conjuguant sur  $x$  :
>>
>>$$
>>e^{sa} e^{tb} x e^{-tb} e^{-sa} = e^{Z(s,t)} x e^{-Z(s,t)}
>>$$
>>
>>👉 donc :
>>
>>$$
>>e^{s\,\mathrm{ad}_a} e^{t\,\mathrm{ad}_b} = e^{\mathrm{ad}_{Z(s,t)}}
>>$$
>
>
>
>>[!info]-   Résumé conceptuel
>>
>>
>>>** ✔️ Équation différentielle **
>>>
>>>$$
>>>f' = [a,f\} \Rightarrow f = \text{flot}
>>>$$
>>
>>
>>
>>>**✔️ Composition de flots **
>>>
>>>$$
>>>\varphi_s^X \circ \varphi_t^Y = \varphi_1^{Z(s,t)}
>>>$$
>>
>>
>>
>>>** ✔️ BCH **
>>>
>>>$$
>>>\boxed{ Z(s,t) = \mathrm{BCH}(sa,tb) }
>>>$$
>>
>
>
>>[!info]-🔥 Insight final (important)
>>
>>
>>👉 BCH = **loi de composition des flots infinitésimaux**
>>
>>👉 C’est la version locale de :
>>
>>*   composition dans le groupe
>>*   non-commutativité encodée par les crochets imbriqués
>>
>
>
>>[!info]-💡 Lecture physique
>>
>>
>>*    $a,b$  = générateurs (jauge, symétries)
>>*    $e^{sa}, e^{tb}$  = évolutions
>>*   BCH = **évolution effective**
>>
>
>
>>[!tip]-
>>
>>*   te faire la **démonstration BCH via Dynkin à partir des flots**
>>*   ou te montrer la version **géométrique avec courbure (F = D²)** où BCH apparaît naturellement
>

>[!tip]-
>
>
>On va relier proprement :
>
>$$
>e^{sa}\, b\, e^{-sa}
>$$
>
>à :
>
>*   **action de groupe (conjugaison)**
>*   **action adjointe (via  $\mathrm{ad}$ )**
>*   et donc à **BCH comme composition de flots**
>
>
>>[!info]-  Action de groupe (niveau global)
>>
>>
>>Dans une algèbre associative (ou groupe de Lie) :
>>
>>$$
>>\boxed{ \mathrm{Ad}_{g}(b) := g\, b\, g^{-1} }
>>$$
>>
>>Ici :
>>
>>$$
>>g = e^{sa}
>>$$
>>
>>donc :
>>
>>$$
>>\boxed{ \mathrm{Ad}_{e^{sa}}(b) = e^{sa} b e^{-sa} }
>>$$
>>
>>👉 c’est une **action du groupe sur l’algèbre**.
>>
>
>
>>[!info]-  Passage infinitésimal = action adjointe
>>
>>
>>On dérive en  $s=0$  :
>>
>>$$
>>\frac{d}{ds}\Big|_{s=0} e^{sa} b e^{-sa} = ab - ba
>>$$
>>
>>👉 donc :
>>
>>$$
>>\boxed{ \mathrm{ad}_a(b) := [a,b] }
>>$$
>>
>>(et en super :  $[a,b\}$ )
>
>
>
>>[!info]-  Équation différentielle
>>
>>
>>Posons :
>>
>>$$
>>X(s) = e^{sa} b e^{-sa}
>>$$
>>
>>Alors :
>>
>>$$
>>\boxed{ X'(s) = [a,X(s)] } \quad (\text{ou } [a,X\} \text{ si cadre super cohérent})
>>$$
>>
>>👉 Donc  $X$  est le **flot du champ** :
>>
>>$$
>>g(x) = [a,x]
>>$$
>>
>
>
>>[!info]-  Solution comme flot
>>
>>
>>Par ce qu’on a démontré :
>>
>>$$
>>\boxed{ X(s) = e^{s\,\mathrm{ad}_a}(b) }
>>$$
>>
>
>
>>[!info]- 🔥  Identification clé
>>
>>
>>$$
>>\boxed{ \mathrm{Ad}_{e^{sa}} = e^{s\,\mathrm{ad}_a} }
>>$$
>>
>>👉 **action de groupe = exponentielle de l’action infinitésimale**
>>
>
>
>>[!info]-  Développement explicite
>>
>>
>>$$
>>e^{sa} b e^{-sa} = b + s[a,b] + \frac{s^2}{2!}[a,[a,b]] + \cdots
>>$$
>>
>>👉 série en crochets imbriqués = action adjointe exponentielle
>>
>>
>
>
>>[!info]-  Lien direct avec BCH
>>
>>
>>Considère deux actions successives :
>>
>>$$
>>e^{sa} e^{tb} \, x \, e^{-tb} e^{-sa}
>>$$
>>
>>👉 c’est :
>>
>>$$
>>\mathrm{Ad}_{e^{sa}} \circ \mathrm{Ad}_{e^{tb}} (x)
>>$$
>>
>>
>>
>>Mais :
>>
>>$$
>>\mathrm{Ad}_{e^{sa}} \circ \mathrm{Ad}_{e^{tb}} = \mathrm{Ad}_{e^{sa} e^{tb}}
>>$$
>>
>>
>>
>>[!info]- 🔥 BCH apparaît
>>
>>
>>$$
>>e^{sa} e^{tb} = e^{\mathrm{BCH}(sa,tb)}
>>$$
>>
>>donc :
>>
>>$$
>>\boxed{ \mathrm{Ad}_{e^{sa}} \circ \mathrm{Ad}_{e^{tb}} = \mathrm{Ad}_{e^{\mathrm{BCH}(sa,tb)}} }
>>$$
>>
>
>
>>[!info]-  Traduction infinitésimale
>>
>>
>>$$
>>e^{s\,\mathrm{ad}_a} e^{t\,\mathrm{ad}_b} = e^{\mathrm{ad}_{\mathrm{BCH}(sa,tb)}}
>>$$
>>
>>👉 cohérence parfaite entre :
>>
>>*   groupe (conjugaison)
>>*   algèbre (crochets)
>>
>
>
>>[!info]- Lecture en termes de flots
>>
>>
>>*    $e^{sa} b e^{-sa}$  = flot de  $[a,\cdot]$ 
>>*    $e^{tb}$  = autre flot
>>*   composer les flots ⇒ BCH
>>
>
>
>>[!info]- 🔥  Schéma global
>>
>>
>>$$
>>\boxed{ \text{Groupe : } g b g^{-1} \quad \Longleftrightarrow \quad \text{Algèbre : } e^{\mathrm{ad}} }
>>$$
>>
>>$$
>>\boxed{ \text{Composition : } g_1 g_2 \quad \Longleftrightarrow \quad \text{BCH} }
>>$$
>
>
>
>>[!info]- 🔥 Insight final (niveau recherche)
>>
>>
>>👉 Toute la structure repose sur :
>>
>>$$
>>\boxed{ \mathrm{Ad}_{e^a} = e^{\mathrm{ad}_a} }
>>$$
>>
>>et
>>
>>$$
>>\boxed{ \text{BCH = loi de groupe transportée dans l’algèbre} }
>>$$
>>
>
>
>>[!info]- 💡 En physique
>>
>>
>>*    $e^{sa}$  = transformation de jauge / évolution
>>*    $b$  = observable / champ
>>*   conjugaison = **transport**
>>*   BCH = **composition non triviale des transformations**
>
>
>>[!tip]-
>>
>>*   la preuve complète via **Dynkin (ultra propre)**
>>*   ou te montrer comment ça donne directement
>>   
>>$$
>>F = dA + \tfrac12 [A,A\}
>>$$
>>
>>comme obstruction à la commutation des flots
>

>[!info]- **preuve “propre” via Dynkin**
>
>Voici une **preuve “propre” via Dynkin** qui relie directement  
>$\mathrm{Ad}_{e^a}=e^{\mathrm{ad}_a}$  et la **formule de BCH** dans le cadre (super-)algébrique. J’indique les signes **super** en filigrane ; si  $a,b$  sont pairs, tout se réduit au cas classique.
>
>
>>[!info]- Préliminaires
>>
>>
>>*   Super-commutateur :  $[x,y\}=xy-(-1)^{|x||y|}yx$ .
>>*    $\mathrm{ad}_x(y):=[x,y\}$ .
>>*   Identité de Jacobi graduée (garantit que  $\mathrm{ad}_x$  est une dérivation de degré  $|x|$ ).
>>
>>On travaille dans une algèbre associative graduée complétée (pour donner un sens aux séries exponentielles).
>
>
>
>>[!info]- Lemme clé : conjugaison = exponentielle de  $\mathrm{ad}$ 
>>
>>
>>Posons  $X(s)=e^{s a}\, b\, e^{-s a}$ . Alors (dérivation en  $s$ , paire) :
>>
>>$$
>>X'(s)=aX(s)-X(s)a=[a,X(s)] \quad(\text{commutateur ordinaire}).
>>$$
>>
>>Si  $a$  est **pair**,  $[a,\cdot]=[a,\cdot\}$ , donc
>>
>>$$
>>X'(s)=\mathrm{ad}_a(X(s)),\qquad X(0)=b.
>>$$
>>
>>Par unicité de l’EDO linéaire :
>>
>>$$
>>\boxed{\;\mathrm{Ad}_{e^{sa}}(b)=e^{s\,\mathrm{ad}_a}(b)\;}
>>$$
>>
>>(et plus généralement on lit l’EDO dans l’algèbre associative ; le développement donne les crochets imbriqués).
>>
>
>
>>[!info]- Réduction de BCH à une identité d’opérateurs  $\mathrm{ad}$ 
>>
>>
>>On veut  $e^a e^b=e^{Z(a,b)}$  avec  $Z=\mathrm{BCH}(a,b)$ .  
>>Appliquons  $\mathrm{Ad}$  des deux côtés à un élément  $x$  :
>>
>>$$
>>\mathrm{Ad}_{e^a e^b}(x) = \mathrm{Ad}_{e^a}\big(\mathrm{Ad}_{e^b}(x)\big) = e^{\mathrm{ad}_a} e^{\mathrm{ad}_b}(x).
>>$$
>>
>>D’un autre côté :
>>
>>$$
>>\mathrm{Ad}_{e^{Z}}(x)=e^{\mathrm{ad}_{Z}}(x).
>>$$
>>
>>Comme ceci vaut pour tout  $x$  :
>>
>>$$
>>\boxed{\;e^{\mathrm{ad}_a} e^{\mathrm{ad}_b}=e^{\mathrm{ad}_{Z(a,b)}}\;}
>>$$
>>
>>et donc  $\mathrm{ad}_{Z}=\log\!\big(e^{\mathrm{ad}_a}e^{\mathrm{ad}_b}\big)$ .
>>
>>👉 Toute la difficulté est donc de **remonter** de l’égalité d’opérateurs à une **expression de  $Z$ ** en crochets imbriqués de  $a,b$ . C’est exactement la **formule de Dynkin**.
>>
>
>
>>[!info]- Outil : l’opérateur de Dynkin
>>
>>
>>Définis l’opérateur linéaire (sur séries formelles en  $\mathrm{ad}_a,\mathrm{ad}_b$ ) :
>>
>>$$
>>\;\mathcal{D}(T) :=\sum_{n\ge1}\frac{(-1)^{n-1}}{n}\,(T-1)^n\;
>>$$
>>
>>de sorte que  $\mathcal{D}(T)=\log T$ .
>>
>>On l’applique à  $T=e^{\mathrm{ad}_a}e^{\mathrm{ad}_b}$ .
>>
>
>
>>[!info]- Identité de Dynkin (forme opérateur → forme “algèbre”)
>>
>>
>>Dynkin montre que, pour tout opérateur  $T$  construit à partir de  $\mathrm{ad}_a,\mathrm{ad}_b$ ,
>>
>>$$
>>\mathcal{D}(T) = \sum_{n\ge1}\frac{(-1)^{n-1}}{n} \sum_{\substack{\text{mots }w\\ |w|=n}} \frac{1}{\#w}\,\mathrm{ad}_{w},
>>$$
>>
>>où  $w$  parcourt les mots en lettres  $a,b$ ,  $|w|$  est la longueur,  $\#w$  est un facteur combinatoire, et  $\mathrm{ad}_w$  signifie l’itération imbriquée de  $\mathrm{ad}$  correspondant au mot  $w$ .
>>
>>En évaluant cette identité sur l’élément  $a+b$  (ou en identifiant terme à terme), on obtient une **expression fermée de  $Z$ ** en crochets imbriqués.
>>
>
>
>>[!info]- Formule explicite de Dynkin pour  $Z=\mathrm{BCH}(a,b)$ 
>>
>>
>>Une écriture standard (équivalente) est :
>>
>>$$
>> Z = \sum_{n\ge1}\frac{(-1)^{n-1}}{n} \!\!\!\sum_{\substack{r_i+s_i>0}} \frac{ (\mathrm{ad}_a)^{r_1}(\mathrm{ad}_b)^{s_1}\cdots (\mathrm{ad}_a)^{r_n}(\mathrm{ad}_b)^{s_n}(a+b) }{ \big(\sum_{i=1}^n(r_i+s_i)\big)\,\prod_{i=1}^n r_i!\,s_i! } 
>>$$
>>
>>où la somme porte sur des entiers  $r_i,s_i\ge0$  non tous nuls.
>>
>>👉 Cette formule donne **directement** une combinaison de **crochets imbriqués** de  $a$  et  $b$ .  
>>En cadre super, chaque  $\mathrm{ad}$  est le **super-adjoint**  $[\,\cdot\,,\,\cdot\,\}$ , donc les signes  $(-1)^{|\,\cdot\,||\,\cdot\,|}$  apparaissent automatiquement lors des itérations.
>>
>
>
>>[!info]-  Développement aux premiers ordres
>>
>>
>>En extrayant les premiers termes :
>>
>>$$
>> Z = a + b + \tfrac12 [a,b\} + \tfrac{1}{12}[a,[a,b\}\} - \tfrac{1}{12}[b,[a,b\}\} + \cdots 
>>$$
>
>
>
>>[!info]-  Conclusion (chaîne logique complète)
>>
>>
>>1.   $\mathrm{Ad}_{e^a}=e^{\mathrm{ad}_a}$  (lemme par EDO).
>>2.  Donc  $e^{\mathrm{ad}_a}e^{\mathrm{ad}_b}=e^{\mathrm{ad}_Z}$ .
>>3.  Appliquer  $\log$  via **Dynkin** donne  $ \mathrm{ad}_Z=\log(e^{\mathrm{ad}_a}e^{\mathrm{ad}_b})$ .
>>4.  Dynkin fournit **une expression explicite** de  $Z$  en **crochets imbriqués** ⇒ BCH.
>>
>
>
>>[!info]- 🔥 Point conceptuel clé
>>
>>
>>*   **Groupe (conjugaison)** :  $g\,(\cdot)\,g^{-1}$ 
>>*   **Algèbre (infinitésimal)** :  $\mathrm{ad}$ 
>>*   **Passage global → infinitésimal** :  $\mathrm{Ad}_{e^a}=e^{\mathrm{ad}_a}$ 
>>*   **Composition** :  $e^a e^b = e^{\mathrm{BCH}(a,b)}$   
>>    obtenue en **prenant le logarithme** au niveau des  $\mathrm{ad}$ .
>
>
>>[!tip]-
>>On peutdétailler **pas à pas** le passage de  $\mathcal{D}(e^{\mathrm{ad}_a}e^{\mathrm{ad}_b})$  à la somme indexée  $(r_i,s_i)$  (combinatoire des mots + coefficients), ou vérifier explicitement les termes jusqu’à l’ordre 3 avec les signes super.
>>
>


>[!note]- Passage Dynkin → somme indexée  $(r_i,s_i)$
>Voici le **passage Dynkin → somme indexée  $(r_i,s_i)$**, détaillé et sans saut conceptuel. Je garde les signes **super** implicites via  $\mathrm{ad}_x(y)=[x,y\}$  (les signes apparaissent automatiquement quand on compose des  $\mathrm{ad}$ ).
>
>
>>[!info]-  Notation compacte
>>
>>
>>Posons
>>
>>$$
>>A\equiv \mathrm{ad}_a,\qquad B \equiv \mathrm{ad}_b.
>>$$
>>
>>On veut développer
>>
>>$$
>>\mathrm{ad}_Z=\log\!\big(e^{A}e^{B}\big)=:\mathcal D\!\big(e^{A}e^{B}\big).
>>$$
>
>
>
>>[!info]-  Définition de Dynkin (série de logarithme)
>>
>>
>>$$
>> \mathcal D(T)=\log T=\sum_{n\ge1}\frac{(-1)^{n-1}}{n}\,(T-1)^n 
>>$$
>>
>>Appliqué à  $T=e^{A}e^{B}$  :
>>
>>$$
>>\mathrm{ad}_Z = \sum_{n\ge1}\frac{(-1)^{n-1}}{n}\,\big(e^{A}e^{B}-1\big)^n.
>>$$
>
>
>
>>[!info]-  Développer  $e^{A}e^{B}-1$ 
>>
>>
>>Écrivons les exponentielles :
>>
>>$$
>>e^{A}=\sum_{r\ge0}\frac{A^r}{r!},\qquad e^{B}=\sum_{s\ge0}\frac{B^s}{s!}.
>>$$
>>
>>Donc
>>
>>$$
>>e^{A}e^{B} = \sum_{r,s\ge0}\frac{A^r B^s}{r!\,s!}.
>>$$
>>
>>Enlevant le terme identité  $(r=s=0)$  :
>>
>>$$
>> e^{A}e^{B}-1 = \sum_{\substack{r,s\ge0\\(r,s)\neq(0,0)}}\frac{A^r B^s}{r!\,s!} 
>>$$
>
>
>
>>[!info]-  Puissance  $n$ \-ième : produit de  $n$  blocs
>>
>>
>>On élève à la puissance  $n$  :
>>
>>$$
>>\big(e^{A}e^{B}-1\big)^n = \sum_{\substack{(r_i,s_i)\neq(0,0)\\ i=1,\dots,n}} \prod_{i=1}^n \frac{A^{r_i} B^{s_i}}{r_i!\,s_i!}.
>>$$
>>
>>👉 Interprétation combinatoire :
>>
>>*   on choisit  $n$  blocs
>>*   chaque bloc est  $A^{r_i}B^{s_i}$  avec  $(r_i,s_i)\neq(0,0)$ 
>
>
>
>>[!info]-  Passage aux “mots”
>>
>>
>>Le produit
>>
>>$$
>>A^{r_1}B^{s_1}\cdots A^{r_n}B^{s_n}
>>$$
>>
>>correspond à un **mot**  $w$  sur l’alphabet  $\{A,B\}$  :
>>
>>$$
>>w = \underbrace{A\cdots A}_{r_1} \underbrace{B\cdots B}_{s_1} \cdots \underbrace{A\cdots A}_{r_n} \underbrace{B\cdots B}_{s_n}.
>>$$
>>
>>👉 Longueur totale :
>>
>>$$
>>|w| = \sum_{i=1}^n (r_i+s_i).
>>$$
>
>
>
>>[!info]- Réécriture de  $\mathcal D$ 
>>
>>
>>En injectant dans Dynkin :
>>
>>$$
>>\mathrm{ad}_Z = \sum_{n\ge1}\frac{(-1)^{n-1}}{n} \sum_{\substack{(r_i,s_i)\neq(0,0)}} \frac{ A^{r_1}B^{s_1}\cdots A^{r_n}B^{s_n} }{ \prod_{i=1}^n r_i!\,s_i! }.
>>$$
>
>
>
>>[!info]-  Du produit d’opérateurs à l’action sur  $a+b$ 
>>
>>
>>Pour remonter à  $Z$  lui-même, on utilise :
>>
>>$$
>>\mathrm{ad}_Z = [Z,\cdot\}.
>>$$
>>
>>Dynkin donne une identité clé : on peut **reconstruire  $Z$ ** en faisant agir cette série sur  $a+b$  et en normalisant par la longueur.
>>
>>👉 Heuristique (rigoureuse dans la preuve complète) :
>>
>>*   chaque mot  $w$  d’opérateurs  $A,B$  correspond à une **itération imbriquée** de crochets appliquée à  $a+b$ 
>>    
>>$$
>>A^{r_1}B^{s_1}\cdots (a+b) \;\leadsto\; (\mathrm{ad}_a)^{r_1}(\mathrm{ad}_b)^{s_1}\cdots (a+b)
>>$$
>>
>
>
>>[!info]- Facteur de normalisation  $\frac{1}{|w|}$ 
>>
>>
>>C’est le point subtil.
>>
>>👉 Pourquoi apparaît
>>
>>$$
>>\frac{1}{\sum_i(r_i+s_i)} \; ?
>>$$
>>
>>Parce que :
>>
>>*    $\mathrm{ad}_Z$  agit comme dérivation
>>*   pour reconstruire  $Z$ , on “intègre” l’action adjointe
>>*   chaque mot de longueur  $k$  apparaît  $k$  fois quand on remonte via  $[Z,\cdot]$ 
>>
>>👉 Donc on doit diviser par la longueur :
>>
>>$$
>>|w| = \sum_i(r_i+s_i)
>>$$
>>
>
>
>>[!info]- ) Formule finale (Dynkin)
>>
>>
>>On obtient :
>>
>>$$
>> Z = \sum_{n\ge1}\frac{(-1)^{n-1}}{n} \!\!\!\sum_{\substack{(r_i,s_i)\neq(0,0)}} \frac{ (\mathrm{ad}_a)^{r_1}(\mathrm{ad}_b)^{s_1} \cdots (\mathrm{ad}_a)^{r_n}(\mathrm{ad}_b)^{s_n}(a+b) }{ \big(\sum_{i=1}^n (r_i+s_i)\big)\; \prod_{i=1}^n r_i!\,s_i! } 
>>$$
>>
>
>
>>[!info]-  Où sont les signes super ?
>>
>>
>>Ils sont **déjà inclus** :
>>
>>*   chaque  $\mathrm{ad}_a$  agit par  $[a,\cdot\}$ 
>>*   les compositions produisent automatiquement les facteurs
>>
>>$$
>>(-1)^{|a||x|},\quad (-1)^{|b||x|}
>>$$
>>
>>👉 donc aucun signe supplémentaire à rajouter dans la formule.
>
>
>
>>[!info]-  🔥  Lecture combinatoire claire
>>
>>
>>Chaque terme correspond à :
>>
>>*   une **suite de blocs**  $(r_i,s_i)$ 
>>*   donc un **mot ordonné**
>>*   coefficient :
>>    *    $\frac{(-1)^{n-1}}{n}$  (logarithme)
>>    *    $\frac{1}{r_i! s_i!}$  (exponentielle)
>>    *    $\frac{1}{|w|}$  (reconstruction de  $Z$ )
>
>
>
>>[!info]-  Exemple (ordre 2)
>>
>>
>>Prends  $n=1$ ,  $(r_1,s_1)=(1,1)$  :
>>
>>$$
>>\frac{1}{2}[a,b\}
>>$$
>>
>>👉 exactement le terme BCH :
>>
>>$$
>>\frac12[a,b\}
>>$$
>>
>
>
>>[!abstract]-   Résumé conceptuel
>>
>>
>>$$
>>\log(e^A e^B) = \text{somme sur mots en } A,B \ \longrightarrow\ \text{crochets imbriqués en } a,b 
>>$$
>
>
>
>>[!info]-  🔥 Insight final
>>
>>
>>👉 BCH =  
>>**logarithme combinatoire des chemins (mots) dans l’algèbre libre**,  
>>puis **projection via  $\mathrm{ad}$ ** vers l’algèbre de Lie.
>
>
>>[!tip]-
>>
>>*   expliciter **tous les termes jusqu’à ordre 3 ou 4 avec signes**
>>*   ou te montrer la version encore plus conceptuelle via  
>>    **algèbres de Lie libres / séries de Hall / base de Lyndon** (niveau recherche réel)
>

## Autre définition de $d(e^a)$

>[!note]- $d(e^a) =  e^a \ast  \phi\left (- \text{ad}_a\right)(d(a)) =  \phi\left ( \text{ad}_a\right)    ( d(a))   \ast e^a $  avec $\phi(z) \equiv \frac{e^{z} - 1 }{z} = \sum_{n = 0}^{\infty} \frac{z^n}{(n+1)!}$
>
>(cf [Wiki Derivative of the exponential map](https://en.wikipedia.org/wiki/Derivative_of_the_exponential_map))
>On va extrapoler le fais que 
>$$
> f_n \, \colon \mathbb C \longrightarrow \mathbb C \quad z \longmapsto \left ( 1 + \frac{z}n \right )^n 
>$$
>converge uniformement sur tous comptact de $\mathbb C$ vers $f \, \colon \; z \mapsto e^z$.
>(cf [Gourdon Analyse p 224 ed 2]())
>
>On veuc caluler 
>$$
>d(e^a)
>$$
>or on admet que 
>$$
>e^a = \lim_{n \to \infty} \left ( 1 + \frac{a}n \right )^n 
>$$
>soit en amdmetant que $d$ et $\underset{n \to \infty}{\lim}$ commutent :
>$$
>d(e^a) = \lim_{n \to \infty} \left \{ d  \left [ \left ( 1 + \frac{a}n \right )^n  \right ] \right \}
>$$
>On a vus que 
>$$
>d(A^n) = \sum_{k=1}^n (-1)^{\vert d \vert \vert A \vert (n - k) } A^{n-k} \ast   d(A) \ast A^k
>$$
>ou en encore $ d(A^n) = \sum_{k=0}^{n-1} (-1)^{\vert d \vert \vert A \vert k} A^k \ast   d(A) \ast A^{n-1-k}$.
>Or
>$$
>A = 1 + \frac{a}n  \Rightarrow \vert A \vert = \vert a \vert , \quad d(A) = \frac{1}{n} d(a) 
>$$
>donc
>$$
>d  \left [ \left ( 1 + \frac{a}n \right )^n  \right ]  = \sum_{k =1}^n (-1)^{\vert d \vert \vert A \vert (n - k) }  \left ( 1 + \frac{a}n \right )^{n-k} \ast   \frac{1}{n}d(a) \ast  \left ( 1 + \frac{a}n \right )^k
>$$
>or 
>$$
>\frac{\Delta k}n \underset{\underset{\Delta k = 1}{n \to \infty}}{\longrightarrow} ds , \quad \frac{k}n \underset{n \to \infty}{\longrightarrow} s, \quad \sum_{k = 1}^n \frac{\Delta k}n \underset{n \to \infty}{\longrightarrow} \int_0^1 ds
>$$
>donc 
>$$
>k \underset{n \to \infty}{\longrightarrow} n s , \quad n - k \underset{n \to \infty}{\longrightarrow} n(1- s)
>$$
>et 
>$$
>\left ( 1 + \frac{a}n \right )^k = \left ( 1 + \frac{sa}{sn} \right )^k \underset{n \to \infty}{\longrightarrow} \lim_{sn \to \infty} \left \{\left ( 1 + \frac{sa}{sn} \right )^{sn} \right \} = e^{sa} ,
>$$
>et 
>$$
>\left ( 1 + \frac{a}n \right )^{n-k} = \left ( 1 + \frac{(1-s)a}{(1-s)n} \right )^{n-k} \underset{n \to \infty}{\longrightarrow} \lim_{(1-s)n \to \infty} \left \{\left ( 1 + \frac{(1-s)a}{(1-s)n} \right )^{(1-s)n} \right \} = e^{(1-s)a},
>$$
>donc 
>$$
>d  \left [ \left ( 1 + \frac{a}n \right )^n  \right ]  = \sum_{k =1}^n (-1)^{\vert d \vert \vert A \vert (n - k) }  \left ( 1 + \frac{a}n \right )^{n-k} \ast   \frac{1}{n}d(a) \ast  \left ( 1 + \frac{a}n \right )^k \underset{n \to \infty}{\longrightarrow} \lim_{n \to \infty} \int_0^1  (-1)^{\vert d \vert \vert a \vert n (1-s) }  e^{(1-s)a}  \ast d(a)  \ast e^{sa}\, ds 
>$$
>Donc comme ${\displaystyle d(e^a) = \lim_{n \to \infty} \left \{ d  \left [ \left ( 1 + \frac{a}n \right )^n  \right ] \right \}} $ on a 
>$$
>d(e^a) = \lim_{n \to \infty} \left \{ \int_0^1  (-1)^{\vert d \vert \vert a \vert n (1-s) }  e^{(1-s)a}  \ast d(a)  \ast e^{sa} \, ds \right \}   \underset{u = 1-s}{=}  \lim_{n \to \infty}  \left \{ \int_0^1  (-1)^{\vert d \vert \vert a \vert ns }  e^{sa}  \ast d(a)  \ast e^{(1-s)a} \,  ds  \right \} 
>$$
>donc 
>$$
>d(e^a) = \lim_{n \to \infty}  \left \{ (-1)^{\vert d \vert \vert a \vert n  } e^a \ast  \int_0^1  (-1)^{-\vert d \vert \vert a \vert n s }  e^{-sa}  \ast d(a)  \ast e^{sa} \, ds  \right \}  \underset{u = 1-s}{=}  \lim_{n \to \infty}  \left \{ \int_0^1  (-1)^{\vert d \vert \vert a \vert ns }  e^{sa}  \ast d(a)  \ast e^{-sa} \,  ds  \right \}  \ast e^a . 
>$$
>On fait quelquel chose de désespérer :
>$$
>(-1)^{\alpha} = e^{i\pi \alpha} ,
>$$
>>[!danger]- Pourquoi le passage avec $e^{i\pi n}$ est faux 
>>
>>en faisant 
>>$$
>>(-1)^{n\alpha} = e^{i\pi n\alpha}
>>$$
>>Puis
>>$$
>>e^{i\pi n s \alpha}
>>$$
>>👉 problème :
>>- tu passes de discret → continu
>>- tu crées une oscillation artificielle
>>- la limite $n \to \infty$ n’existe pas
>>
>>C’est pour ça que tu obtiens :
>>>"limite définie que si …"
>>
>>👉 ça signale une erreur de modèle.
>>
>
>et $i\pi \alpha$ etais une scalaire comment avec $sa$ donc $e^{i\pi \alpha} e^{\lambda a } =  e^{i\pi \alpha + \lambda a }$ soit , 
>$$
>d(e^a) = e^a \ast  \lim_{n \to \infty} \left \{ (-1)^{\vert d \vert \vert a \vert n  }  \int_0^1   e^{-s(i\pi\vert d \vert \vert a \vert n + a)}  \ast d(a)  \ast e^{sa} \, ds  \right \}  \underset{u = 1-s}{=}  \lim_{n \to \infty} \left \{ \int_0^1   e^{s(i\pi\vert d \vert \vert a \vert n +  a)}  \ast d(a)  \ast e^{-sa} \,  ds  \right \}  \ast e^a . 
>$$
>Mauvaise idée partons de 
>$$
>d(e^a) =  e^a \ast \lim_{n \to \infty}  \left \{ (-1)^{\vert d \vert \vert a \vert n  }  \int_0^1   e^{-s(i\pi\vert d \vert \vert a \vert n)} e^{-sa} \ast d(a)  \ast e^{sa} \, ds \right \}  \underset{u = 1-s}{=}  \lim_{n \to \infty} \left \{ \int_0^1   e^{s(i\pi\vert d \vert \vert a \vert n)} e^{sa} \ast d(a)  \ast e^{-sa} \,  ds \right \}  \ast e^a . 
>$$
>Or $e^{\lambda X} Y e^{-\lambda X} = e^{ \lambda \text{ad}_X}(Y)$ , donc 
>$$
>d(e^a) =  e^a \ast \lim_{n \to \infty}  \left \{ (-1)^{\vert d \vert \vert a \vert n  }  \int_0^1   e^{-s(i\pi\vert d \vert \vert a \vert n)} e^{-s \, \text{ad}_a } \, ds  \right \} ( d(a)) \underset{u = 1-s}{=}  \lim_{n \to \infty} \int_0^1  \left \{  e^{s(i\pi\vert d \vert \vert a \vert n)} e^{s \,  \text{ad}_a } \,  ds \right \}  ( d(a))   \ast e^a . 
>$$
>si $i\pi \alpha$ etais une scalaire comment avec $\text{ad}_a$ donc $e^{i\pi \alpha} e^{\lambda \text{ad}_a } =  e^{i\pi \alpha + \lambda \text{ad}_a }$ soit , 
>$$
>d(e^a) =  e^a \ast  \lim_{n \to \infty} \left \{ (-1)^{\vert d \vert \vert a \vert n  } \int_0^1    e^{-s ( i\pi\vert d \vert \vert a \vert n + \text{ad}_a) } \, ds \right \}  ( d(a)) \underset{u = 1-s}{=}  \lim_{n \to \infty} \left \{ \int_0^1   e^{s ( i\pi\vert d \vert \vert a \vert n +  \text{ad}_a) } \,  ds \right \}   ( d(a))   \ast e^a . 
>$$
>Or 
>$$
> \int_0^1 e^{s \alpha } \, ds = \phi(\alpha) \equiv \frac{e^{\alpha} - 1 }{\alpha} = \sum_{n = 0}^{\infty} \frac{\alpha^n}{(n+1)!}
>$$
>donc 
>$$
>d(e^a) =  e^a \ast  \lim_{n \to \infty}  \left \{ (-1)^{\vert d \vert \vert a \vert n  } \phi\left (-(i\pi\vert d \vert \vert a \vert n + \text{ad}_a)\right) \right \}  ( d(a)) =  \lim_{n \to \infty} \left \{ \phi\left (i\pi\vert d \vert \vert a \vert n + \text{ad}_a\right) \right \}   ( d(a))   \ast e^a . 
>$$
>avec $\phi(z) \equiv \frac{e^{z} - 1 }{z} = \sum_{n = 0}^{\infty} \frac{z^n}{(n+1)!}$.
>
>>[!fail]- Limite définie que pour $\vert d \vert \vert a \vert = 0 \mod 2$
>>
>> Pour $d$ ou $a$ boson .
>
>>[!success]- Supposons que $\vert d \vert \vert a \vert = 0 \mod 2$
>>
>> Pour $d$ ou $a$ boson .
>
>$$
>d(e^a) =  e^a \ast  \phi\left (- \text{ad}_a\right)(d(a)) =  \phi\left ( \text{ad}_a\right)    ( d(a))   \ast e^a . 
>$$
>avec 
>$$
>\phi(z) \equiv \frac{e^{z} - 1 }{z} = \sum_{n = 0}^{\infty} \frac{z^n}{(n+1)!}
>$$
>
>>[!success]- Si $a$ et $d(a)$ commutent on retrouve :
>>
>> $\text{ad}_a(d(a)) =0$ et $\phi(\text{ad}_a)[d(a)]\frac{e^{\text{ad}_a(d(a))} - 1 }{\text{ad}_a(d(a))} = \sum_{n = 0}^{\infty} \frac{\text{ad}_a(d(a))^n}{(n+1)!} = d(a)$
>> soit 
>>$$
>>d(e^a) =  e^a \ast  d(a) =  d(a)  \ast e^a . 
>>$$
>
>

## Courbure $\mathcal F$

>[!note]- $D^2 = \mathrm{ad}_{\mathcal F}  \quad \text{avec} \quad \mathcal F = d(\mathcal A)  + \tfrac12 [\mathcal A,\mathcal A\}$ et si $D = e^{-a}\circ d \circ e^{a} = d + e^{-a}\circ d(e^{a} )$ , $ D^2 = 0$
>
>On considère l’opérateur :
>$$
>D \equiv  e^{-a} \circ d \circ e^a
>$$
>Agissons sur une forme $\omega$ :
>$$
>D(\omega) = e^{-a} \circ  d(e^a \ast \omega )
>$$
>Prennons le cas $a$ boson.
>
>Appliquer Leibniz graduée
>$$
>d(e^a \ast \omega) = (d ( e^a)) \ast  \omega + e^a  \ast  d(\omega)
>$$
>Donc :
>$$
>D(\omega) = e^{-a} \circ (d (e^a)) \ast  \omega + d(\omega)
>$$
>Résultat clé
>$$
>e^{-a} \circ  d \circ  e^a = d + e^{-a} \circ  (d (e^a))
>$$
>👉 donc :
>$$
> D = d + \mathcal A = e^{-a} \circ d  \circ e^a
>$$
>avec :
>$$
>\mathcal A = e^{-a} \circ (d (e^a)) =  \phi\left (- \text{ad}_a\right)(d(a)) =  e^{-a} \circ \phi\left ( \text{ad}_a\right)    ( d(a))   \circ e^a \quad    \text{avec} \quad  \phi(z) \equiv \frac{e^{z} - 1 }{z} = \sum_{n = 0}^{\infty} \frac{z^n}{(n+1)!}
>$$
>
>>[!causion]- Deux cadres différents (à ne pas confondre)
>>
>>>[!fail]- (A) $D$ comme dérivation
>>>
>>> Classiquement :
>>>$$
>>> D(\omega) = d(\omega) + \mathcal A \ast \omega
>>>$$
>>>👉 ici :
>>>- $\mathcal A$ agit par multiplication à gauche
>>>- pas de crochet
>>
>>>[!success]- (B) $D$ comme opérateur interne (super-adjoint)
>>>
>>>$$
>>>D(\omega) \doteq  [d + \mathcal A,\omega\}
>>>$$
>>>
>>>👉 ici :
>>>- $d$ et $\mathcal A$ sont vus dans une super-algèbre d’endomorphismes
>>>- $D$ agit par commutateur gradué
>>>
>>> (i) Calcul de $[d,\omega\}$
>>>$$
>>>[d,\omega\}(\alpha) = d(\omega \ast \alpha ) - (-1)^{\vert d \vert \vert \omega \vert } \omega \ast d(\alpha)
>>>$$
>>> aved Leibniz $d(\omega \ast \alpha ) = d(\omega) \ast \alpha + (-1)^{\vert d \vert \vert \omega \vert } \omega \ast d(\alpha)$ donc 
>>>$$
>>>[d,\omega\}(\alpha) = d(\omega) \ast \alpha + (-1)^{\vert d \vert \vert \omega \vert } \omega \ast d(\alpha) - (-1)^{\vert d \vert \vert \omega \vert } \omega \ast d(\alpha) = d(\omega) \ast \alpha 
>>>$$
>>>donc 
>>>$$
>>>[d,\omega\} = d(\omega)
>>>$$
>>>✔️ correct
>>>
>>> (ii) Version commutateur :
>>>
>>>$$
>>> D = d + \mathrm{ad}_{\mathcal A}
>>>$$
>>
>
>On retiendra
>
>$$
> D = d + \text{ad}_{\mathcal A} = e^{-a} \circ d  \circ e^a
>$$
>avec :
>$$
>\mathcal A = e^{-a} \circ (d (e^a)) =  \phi\left (- \text{ad}_a\right)(d(a)) =  e^{-a} \circ \phi\left ( \text{ad}_a\right)    ( d(a))   \circ e^a \quad    \text{avec} \quad  \phi(z) \equiv \frac{e^{z} - 1 }{z} = \sum_{n = 0}^{\infty} \frac{z^n}{(n+1)!}
>$$
>et 
>$$ 
>\vert a \vert = 0 , \quad \vert \mathcal A \vert = \vert d \vert 
>$$
>
>Donc 
>$$
>D^2 = e^{-a} \circ d  \circ e^a  \circ e^{-a} \circ d  \circ e^a  = e^{-a} \circ d^2  \circ e^a = 0
>$$
>et 
>$$
>D(\omega) = d(\omega) + [\mathcal A,\omega\}
>$$
>Donc :
>$$
>D^2(\omega) = D(D(\omega)) = D^2 \omega = d(d(\omega) + [\mathcal A,\omega\}) +[\mathcal A,\, d(\omega)  + [\mathcal A,\omega\}\}
>$$
>
>>[!tip]- *Simplification*
>>
>>>[!note]- (i) $d(d(\omega)) = 0 $
>>>
>>>$$
>>>d^2 = 0
>>>$$
>>
>>>[!note]- (ii) dérivation du crochet $d([\mathcal A,\omega\}) = [d( \mathcal A) ,\omega\} - [\mathcal A,d(\omega)\} $
>>>
>>>$$
>>>d([\mathcal A,\omega\}) = [d( \mathcal A) ,\omega\} + (-1)^{\vert d \vert \vert \mathcal A \vert }[\mathcal A,d(\omega)\}
>>>$$
>>>avec $|\mathcal A |=1$ et $ |d|=1$ .
>>
>>>[!note]- (iii) second terme $[\mathcal A, d(\omega) + [\mathcal A,\omega\}\} = [\mathcal A,d(\omega) \} + [\mathcal A,[ \mathcal A,\omega\}\} $
>>
>>[!tip]- Regroupement $D^2(\omega)  = [d (\mathcal A) ,\omega\} + [\mathcal A,[\mathcal A,\omega\}\}$
>>
>>$$
>>D^2 (\omega) = [d(\mathcal A) ,\omega\} - [\mathcal A,d(\omega) \} + [\mathcal A,d(\omega) \} + [ \mathcal A,[ \mathcal A,\omega\}\}
>>$$
>>Les termes $ [ \mathcal A,d(\omega)\} $ s’annulent :
>>$$
>>D^2(\omega)  = [d (\mathcal A) ,\omega\} + [\mathcal A,[\mathcal A,\omega\}\}
>>$$
>>
>
>>[!tip]- Utilisation de l’identité de Jacobi graduée $[\mathcal A,[\mathcal A,\omega\}\} = \frac{1}{2} [[\mathcal A,\mathcal A\},\omega\}$
>>
>>👉 (identité standard en super-algèbre)
>
>
>>[!tip]- Conclusion $D^2 = \mathrm{ad}_{\mathcal F}  \quad \text{avec} \quad \mathcal F = d(\mathcal A)  + \tfrac12 [\mathcal A,\mathcal A\}$
>>
>>$$
>>D^2(\omega) = [d(\mathcal A) + \tfrac12 [ \mathcal A, \mathcal A\}, \omega\}
>>$$
>
>>[!tip]- Recaputulatif des définitions
>>$$
>>\begin{aligned}
>>D &= d + \mathrm{ad}_{\mathcal A}\\
>>\mathcal F &= d(\mathcal A)  + \tfrac12 [\mathcal A,\mathcal A\}\\
>>D(\omega) &= d(\omega) + [\mathcal A,\omega\}
>>\end{aligned}
>>$$
>>
>
>
>>[!tip]- Identité de Bianchi : $D( \mathcal F ) = 0$
>>
>>Calculons :
>>$$
>>D(\mathcal F = d(\mathcal F) + [\mathcal A,\mathcal F\})
>>$$
>>
>>>[!note]- dériver $d ( \mathcal F ) =  \tfrac12 d[\mathcal A,\mathcal A\}$
>>>
>>>$$
>>>\begin{aligned}
>>>d( \mathcal F ) &= d(d((\mathcal  A) + \tfrac12 [\mathcal  A,\mathcal  A\})\\
>>>&= d^2(\mathcal  A) + \tfrac12 d[\mathcal  A,\mathcal  A\}\\
>>>&= 0 + \tfrac12 d[\mathcal  A,\mathcal  A\}\\
>>>\end{aligned}
>>>$$
>>
>>>[!note]- dérivation du crochet $d[\mathcal  A,\mathcal  A\} = [d(\mathcal A),\mathcal A\} - [\mathcal A,d(\mathcal A) \}$
>>>
>>> Leibniz
>>>$$
>>>d[\mathcal A,\mathcal A\} = [d(\mathcal A) ,\mathcal A\} + (-1)^{\vert d \vert \vert \mathcal A \bvert } [\mathcal A,d(\mathcal A) \}
>>>$$
>>>(dérivation graduée, $|\mathcal A|=\vert d \vert = 1 $ ) , 
>>>Donc :
>>>$$
>>>d(\mathcal F ) = \tfrac12 \big( [d(\mathcal A) , \mathcal A\} - [\mathcal A,d( \mathcal A) \} \big)
>>>$$
>>
>>
>>>[!note]- ajouter $[\mathcal A,\mathcal F\} = [ \mathcal A,d (\mathcal A)\} + \tfrac12 [\mathcal A,[\mathcal A,\mathcal A\}\}$
>>>
>>>$$
>>>[\mathcal A,\mathcal F\} = [ \mathcal A,d (\mathcal A)\} + \tfrac12 [\mathcal A,[\mathcal A,\mathcal A\}\}
>>>$$
>>>
>>
>>>[!note]- somme $D(\mathcal F) = \tfrac12 [d(\mathcal A),\mathcal A\} - \tfrac12 [\mathcal A,d(\mathcal A)\} + [\mathcal A,d(\mathcal A)\} + \tfrac12 [\mathcal A,[\mathcal A,\mathcal A\}\}$
>>>
>>
>>>[!note]- simplification $D(\mathcal F) = \tfrac12 [d(\mathcal A),\mathcal A\} + \tfrac12 [\mathcal A,d(\mathcal A)\}  + \tfrac12 [\mathcal A,[\mathcal A,\mathcal A\}\}$
>>>
>>>$$
>>>- \tfrac12 [\mathcal A,d(\mathcal A)\} + [\mathcal A,d(\mathcal A)\} = \tfrac12 [\mathcal A,d(\mathcal A)\}
>>>$$
>>>Donc 
>>>$$
>>>D(\mathcal F) = \tfrac12 [d(\mathcal A),\mathcal A\} + \tfrac12 [\mathcal A,d(\mathcal A)\}  + \tfrac12 [\mathcal A,[\mathcal A,\mathcal A\}\}
>>>$$
>>
>>
>>>[!note]- Jacobi graduée : $[\mathcal A,[\mathcal A,\mathcal A\}\} = [d(\mathcal A),\mathcal A\} + [\mathcal A,d(\mathcal A)\} = 0$
>>>
>>>On utilise :
>>>$$
>>>[\mathcal A,[\mathcal A,\mathcal A\}\} = 0
>>>$$
>>>👉 (Jacobi super, avec $\mathcal A$ impair)
>>>Et :
>>>$$
>>>[d(\mathcal A),\mathcal A\} + [\mathcal A,d(\mathcal A)\} = 0
>>>$$
>>> (car antisymétrie graduée)
>>
>> ✅ Conclusion
>>$$
>>D(\mathcal F)  = 0
>>$$
>>
>>>[!note]-Interprétation profonde
>>>
>>>👉 $D(\mathcal F)  = 0$ est une **identité géométrique universelle**
>>>- indépendante des équations du mouvement
>>>- purement structurelle
>>
>>>[!question]-Pourquoi $D(\mathcal F)  = 0$ en général ?
>>>
>>>$$
>>>\mathcal F = d(\mathcal A)  + \tfrac12 [\mathcal A,\mathcal A\}
>>>$$
>>>- mesure la courbure
>>>- obstruction à $D^2 =0$
>>>
>>>>[!note]- Cas particulier :
>>>>$$
>>>>\mathcal A = g^{-1} \circ d(g) \Rightarrow \mathcal F = 0
>>>>$$
>>>>👉 connexion **pure**
>>>
>>
>>>[!note]- Lien avec Yang–Mills
>>>
>>>Équation de Yang–Mills :
>>>$$
>>>D^\mu \mathcal F_{\mu \nu } = 0
>>>$$
>>>👉 analogue de Maxwell :
>>>$$
>>>\partial^\mu \mathcal F_{\mu\nu} = 0
>>>$$
>>>
>>>Structure complète :
>>>| Type      | Équation               |
>>>| --------- | ---------------------- |
>>>| Bianchi   | $D\mathcal F = 0$              |
>>>| Dynamique | $D^\mu \mathcal F_{\mu\nu} = 0$ |
>>>
>>> Vision physique
>>>
>>>- $D\mathcal F = 0$ : identité → pas d’information dynamique
>>>- $D^\mu \mathcal F_{\mu\nu} = 0$ : équation du mouvement
>>>
>>>Analogie Maxwell
>>>
>>>$$
>>>\begin{aligned}
>>>d(\mathcal F) &= 0 \quad (\text{Bianchi})\\
>>>d^\star ( \mathcal F ) &= 0 \quad (\text{dynamique})
>>>\end{aligned}
>>>$$
>>
>>Structure complète
>>
>>$$
>>\begin{aligned}
>>\mathcal F &= d(\mathcal A)  + \tfrac12 [\mathcal A,\mathcal A\}\\
>>D &= d + \mathrm{ad}_{\mathcal A}\\
>>D^2 &= \mathrm{ad}_{\mathcal F}\\
>>D(\mathcal F) &= 0
>>\end{aligned}
>>$$
>>
>>>[!tip]- 🔥 Insight final
>>>
>>>$D(\mathcal F) = 0$ est une conséquence directe de :
>>>
>>>$$
>>>D^2 = \mathrm{ad}_{\mathcal F}
>>>$$
>>>et de l’identité de Jacobi.
>>>
>>>
>>>- ✔️ $\mathcal F=0$ ⇔ connexion pure
>>>- ✔️ $\mathcal F\neq 0$ ⇔ champ de jauge réel
>>>
>>>👉 Toute la théorie de jauge tient dans :
>>>$$
>>>D^2 = \mathrm{ad}_{\mathcal F} \quad\text{et}\quad D(\mathcal F) = 0
>>>$$
>>>
>>>Prochaine étape naturelle : dériver Yang–Mills à partir d’une action :
>>>$$
>>>S = \int \mathrm{Tr}(\mathcal F \wedge \star \mathcal F)
>>>$$
>>>(et là tu touches directement la physique des champs).
>>
>


(cf [[Supergravité]] [[Théorie de jauge]] )





* * *
