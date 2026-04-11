---
title: Algèbres graduées, formes différentielles et structure de superalgèbre de Lie
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
>(cf [[Super-algèbre de Lie|Déf $\vert \boullet \vert $]] pour une définition restrainte à la super-algèbre de Lie)

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

>[!info]- Super-commutateur $[x,y\}$
>
>Sur toute algèbre graduée associative, on définit le **supercommutateur** :
>$$
>[x,y\} = x \ast y - (-1)^{|x||y|} y \ast x
>$$
>
>Il vérifie :
>- antisymétrie graduée
>- identité de Jacobi graduée
>
>(cf [[Super-algèbre de Lie|Déf $\vert \bullet \vert $]] pour une définition restrainte à la super-algèbre de Lie)
>

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
>(E^\bullet, \ast)
>$$
>
>### Niveau 2 : superalgèbre de Lie
>
>$$
>(\mathrm{End}^\bullet(E^\bullet), [\ ,\ \})
>$$
>
>

>[!info]- Conclusion
>
>- Chaque \(E^p\) est un espace vectoriel (groupe abélien)
>- seule la somme graduée \(E^\bullet\) porte une structure d’algèbre
>- les objets supercommutatifs ont une structure de Lie triviale
>- la structure dynamique apparaît dans les endomorphismes
>- la géométrie différentielle réalise une représentation fermionique naturelle
>

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


>[!info]- Endomorphismes gradués
>
>On considère :
>
>$$
>\mathcall L^\bullet(E^\bullet) = \bigoplus_{k \in \mathbb{Z}} \mathcall L^k(E^\bullet)
>$$
>
>où :
>$$
>T \in \mathrm{End}^k \iff T : E^p \to E^{p+k}
>$$
>
>Alors :
>
>- $(\mathrm{End}^\bullet, \circ)$ est une algèbre graduée
>- $(\mathrm{End}^\bullet, [\ ,\ \})$ est une superalgèbre de Lie non triviale
>
