---
title: IX - Torseurs — classification, relations et généralisation (nD)
tags:
  - Physique
  - Mécanique
  - Calcul tensoriel
  - Algèbre extérieure
  - Théorème de Noether
niveau: Doctorat
version: 1
---

---
[^1]: Documents associés : *III - Mécanique du point au solide (nD)* (§3.2 torseur cinétique, §3.4 dynamique, §8 Noether, §10 solide), *V - Théorème de Varignon généralisé et théorie des moments (nD)*, *II - Dynamique des systèmes matériels fermés (3D - torseur)*, *VI - Cinématique et géométrie différentielle des référentiels*
---

> [!abstract] Plan et esprit du document
> On répond à : *quels torseurs existe-t-il (cinématique, cinétique, dynamique, d'action, … ) ? en quoi diffèrent-ils ? peut-on les généraliser, comme on généralise des charges conservées dans un GGE ?*
> Idée directrice : **un torseur n'est pas « deux vecteurs »**, c'est un objet de l'algèbre de Lie du groupe euclidien $SE(n)$ (type *vitesse*) ou de son dual (type *moment*). Cela explique les quatre torseurs usuels, la puissance (comoment), la nature de la rotation en dimension $n$, et le lien avec Noether.
> Conventions de III : $\wedge$ = produit extérieur (bivecteur), $\times$ seulement en dimension 3 ; « BABAR » : $\mathsf M(B)=\mathsf M(A)+\overrightarrow{BA}\wedge\vec R$.

# 1. Qu'est-ce qu'un torseur ?

## 1.1 Deux types de torseurs, deux lois de changement de point

Soit $\mathscr E$ un espace affine euclidien de dimension $n$, de direction $V$, de métrique $g$.

>[!tip]+ **Torseur de type « moment »** (actions, cinétique, dynamique)
>Un couple $\mathscr T(A)=\{\vec R\,;\,\mathsf M(A)\}$ avec $\vec R\in V$ (**résultante**, indépendante du point) et $A\mapsto\mathsf M(A)\in\Lambda^2V$ (**champ de moments**) tel que
>$$
>\boxed{\mathsf M(B)=\mathsf M(A)+\overrightarrow{BA}\wedge\vec R}\qquad(\text{BABAR}).
>$$

>[!tip]+ **Torseur de type « vitesse »** (cinématique)
>Un couple $\mathscr V(A)=\{\Omega\,;\,\vec v(A)\}$ avec $\Omega\in\mathfrak{so}(V,g)$ (**rotation**, indépendante du point) et $A\mapsto\vec v(A)\in V$ (**champ de vitesses**) tel que
>$$
>\boxed{\vec v(B)=\vec v(A)+\Omega(\overrightarrow{AB})=\vec v(A)-\Omega(\overrightarrow{BA})}.
>$$
>En dimension 3, $\Omega=\hat\omega$ et c'est $\vec v(B)=\vec v(A)+\overrightarrow{BA}\times\vec\omega$ (la forme « BABAR » de II).

Dans les deux cas : la partie « indépendante du point » est la **résultante**, l'autre est le **champ**. Les rôles sont **inversés** : pour un torseur d'action, la résultante est un vecteur et le champ est un bivecteur ; pour le torseur cinématique, la résultante est un bivecteur ($\Omega$) et le champ est un vecteur ($\vec v$). Les deux se déduisent l'un de l'autre par dualité (§5).

## 1.2 Dimension, et pourquoi pas « deux vecteurs »

$$
\dim\{\vec R;\mathsf M\}=n+\frac{n(n-1)}{2}=\frac{n(n+1)}{2}=\dim SE(n).
$$

| $n$ | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| translation | 1 | 2 | 3 | 4 |
| rotation $\dim\Lambda^2V$ | 0 | 1 | 3 | 6 |
| **torseur** | 1 | 3 | **6** | 10 |

Le « 6 » usuel n'est que le cas $n=3$, où $\Lambda^2V\simeq V$ par Hodge ($\mathsf M^{ij}=\varepsilon^{ijk}M_k$). En dimension 1 il n'y a plus de rotation : le torseur se réduit à une résultante.

>[!tip]- Interprétation de groupe
>- type vitesse : $\mathscr V\in\mathfrak{se}(n)=V\oplus\mathfrak{so}(n)$, l'algèbre de Lie de $SE(n)=V\rtimes SO(n)$ (mouvements rigides) ;
>- type moment : $\mathscr T\in\mathfrak{se}(n)^\ast$ (son dual) ;
>- la loi de changement de point est l'action de la translation $\overrightarrow{BA}$ sur ces espaces (coadjointe pour le type moment, adjointe pour le type vitesse).

# 2. Les quatre torseurs fondamentaux

| Torseur | Définition | Résultante | Moment / champ | Type |
| --- | --- | --- | --- | --- |
| **Cinématique** $\mathscr V_{\mathscr S/\mathscr R}(A)$ | mouvement d'un solide | $\Omega_{\mathscr S/\mathscr R}$ | $\vec v_{\mathscr S/\mathscr R}(A)$ | vitesse |
| **Cinétique** $\mathscr C_{\mathscr S/\mathscr R}(A)$ | $\int(\cdot)\,\vec v\,dm$ | $\vec P=\int\vec v\,dm=m\vec v_G$ | $\mathsf L(A)=\int\overrightarrow{AM}\wedge\vec v\,dm$ | moment |
| **Dynamique** $\mathscr D_{\mathscr S/\mathscr R}(A)$ | $\int(\cdot)\,\vec a\,dm$ | $\vec S=\int\vec a\,dm=m\vec a_G$ | $\mathsf D(A)=\int\overrightarrow{AM}\wedge\vec a\,dm$ | moment |
| **Actions** $\mathscr A_{\mathscr S/\mathscr R}(A)$ | $\int(\cdot)\,d\vec F$ | $\vec F=\int d\vec F$ | $\mathsf M(A)=\int\overrightarrow{AM}\wedge d\vec F$ | moment |

Chacun vérifie sa loi de changement de point (BABAR pour les trois derniers, $\vec v(B)=\vec v(A)-\Omega(\overrightarrow{BA})$ pour le premier).

## 2.1 Différence de nature entre les quatre

| Torseur | Contient une masse ? | Question | Dépend du référentiel ? |
| --- | --- | --- | --- |
| Cinématique | non | *comment le solide bouge-t-il ?* | oui |
| Cinétique | oui ($dm$) | *quel « contenu de mouvement » (impulsion, moment cinétique) ?* | oui |
| Dynamique | oui ($dm$) | *quelle « réponse inertielle » (masse × accélération) ?* | oui |
| Actions | non (forces) | *quelle sollicitation extérieure/intérieure s'exerce ?* | non (forces d'interaction invariantes) |

En une phrase : **cinématique** = champ de vitesses, **cinétique** = champ de vitesses *pondéré par la masse*, **dynamique** = champ d'accélérations pondéré par la masse, **actions** = ce qui *cause* la dynamique (PFD : $\mathscr D=\mathscr A^{\mathrm{ext}}$).

>[!warning]- Ne pas confondre « torseur d'action » et « action » $S=\int L\,dt$
>Homonymie. Le **torseur d'action(s) mécanique(s)** est $\{\vec F;\mathsf M\}$ (unités N et N·m). L'**action** variationnelle $S[q]=\int L\,dt$ (unité J·s) est une fonctionnelle, sans lien de structure avec les torseurs. Le seul lien est indirect : par Noether (§7), les composantes $\{\vec P;\mathsf L\}$ du torseur cinétique sont les charges associées aux symétries de $S$ par translation et rotation.

# 3. Relations entre les torseurs

## 3.1 Cinématique $\to$ cinétique : l'opérateur d'inertie

Pour un solide, $\vec v(M)=\vec v(A)+\Omega(\overrightarrow{AM})$ et, en intégrant :
$$
\vec P=m\,\vec v_G,\qquad \mathsf L(G)=\mathcal I_G(\Omega),\qquad \mathsf L(A)=\mathcal I_G(\Omega)+m\,\overrightarrow{AG}\wedge\vec v_G
$$
(Koenig, cf. III §3.3, §10.2) avec $\mathcal I_G:\mathfrak{so}(n)\to\Lambda^2V$, $\mathsf L=-(\Omega J+J\Omega)$ en base orthonormale. Donc
$$
\boxed{\mathscr C=\mathbb M\,\mathscr V}
$$
où $\mathbb M:\mathfrak{se}(n)\to\mathfrak{se}(n)^\ast$ est l'**opérateur d'inertie** (« matrice de masse » $\mathrm{diag}(m\,\mathrm{id},\mathcal I_G)$ exprimée au centre d'inertie). C'est ce que l'on appelle parfois, abusivement, « torseur d'inertie » : ce n'est **pas** un torseur, c'est l'application linéaire entre torseur cinématique et torseur cinétique.

## 3.2 Cinétique $\to$ dynamique : dérivation

Pour un point de réduction $A$ quelconque (III §3.4) :
$$
\vec S=\frac{d\vec P}{dt},\qquad \boxed{\mathsf D(A)=\frac{d\mathsf L(A)}{dt}\Big)_{\mathscr R}+\vec v_{\mathscr R}(A)\wedge\vec P}.
$$
Le terme correctif disparaît si $A$ est fixe, ou si $A=G$ (car $\vec v_G\wedge m\vec v_G=0$). Ainsi, $\mathscr D(A)\ne d\mathscr C(A)/dt$ en général : **la dérivée d'un torseur calculée à point mobile n'est pas un torseur** ; la bonne dérivée est la dérivée du champ à point *fixe* dans $\mathscr R$ (ou on rajoute $\vec v_A\wedge\vec P$).

## 3.3 Dynamique $=$ actions : le PFD des systèmes fermés

Dans $\mathscr R$ galiléen (II, III §4) :
$$
\boxed{\mathscr D_{\mathscr S/\mathscr R}(A)=\mathscr A^{\mathrm{ext}}(A)}\iff\begin{cases}\vec S=\vec F^{\mathrm{ext}}&(\text{TRD})\\ \mathsf D(A)=\mathsf M^{\mathrm{ext}}(A)&(\text{TMD})\end{cases}
$$
La suppression du torseur des actions intérieures exige la 3e loi **forte** (forces centrales), pas seulement la 3e loi faible (III §4.3).

## 3.4 Chaîne complète

$$
\underbrace{\mathscr V}_{\text{cinématique}}\ \xrightarrow{\ \mathbb M\ }\ \underbrace{\mathscr C}_{\text{cinétique}}\ \xrightarrow{\ d/dt\ (+\vec v_A\wedge\vec P)\ }\ \underbrace{\mathscr D}_{\text{dynamique}}\ \xrightarrow{\ \text{PFD galiléen}\ }\ \underbrace{\mathscr A^{\mathrm{ext}}}_{\text{actions}}
$$

# 4. Puissance, énergie : le comoment

## 4.1 Dualité entre type vitesse et type moment

>[!tip]+ **Comoment (puissance virtuelle).** Pour $\mathscr T=\{\vec R;\mathsf M(A)\}$ et $\mathscr V=\{\Omega;\vec v(A)\}$,
>$$
>\boxed{\langle\mathscr T,\mathscr V\rangle:=\vec R\cdot\vec v(A)+\tfrac12\,\mathsf M^{ij}(A)\,\Omega_{ji}}\quad\text{indépendant de }A .
>$$
>En dimension 3 : $\vec R\cdot\vec v(A)+\vec M(A)\cdot\vec\omega$.
>
>*Indépendance de $A$.* Avec $\vec v(B)=\vec v(A)-\Omega(\overrightarrow{BA})$ et $\mathsf M(B)=\mathsf M(A)+\overrightarrow{BA}\wedge\vec R$, la variation vaut $-\vec R\cdot\Omega(\overrightarrow{BA})+\tfrac12(b^iR^j-b^jR^i)\Omega_{ji}=-\vec R\cdot\Omega(\vec b)+b^iR^j\Omega_{ji}$ ; or $R^j\Omega_{ji}b^i=-R^j\Omega_{ij}b^i=-g(\vec R,\Omega\vec b)$ avec les signes de la convention de III ; les deux termes se compensent par antisymétrie de $\Omega$. On vérifie la normalisation en $n=3$ : $\tfrac12\varepsilon^{ijk}M_k\,\varepsilon_{ijl}\omega^l=M_k\omega^k$.

## 4.2 Conséquences

- **Puissance** des actions sur un solide : $\mathscr P=\langle\mathscr A,\mathscr V\rangle$.
- **TEC du solide** : $\dfrac{d\mathcal E_c}{dt}=\langle\mathscr D,\mathscr V\rangle=\langle\mathscr A^{\mathrm{ext}},\mathscr V\rangle$ (car $\int\vec a\cdot\vec v\,dm=\vec S\cdot\vec v_A+\tfrac12\mathsf D^{ij}\Omega_{ji}$) ; la puissance des actions intérieures est nulle pour un solide.
- **Énergie cinétique** : $\mathcal E_c=\tfrac12\langle\mathscr C,\mathscr V\rangle=\tfrac12\,m\|\vec v_G\|^2+\tfrac12\langle\mathsf L^\ast,\Omega\rangle$ (Koenig).
- **Liaison parfaite** : le torseur d'action de liaison $\mathscr A_{\mathrm{liaison}}$ vérifie $\langle\mathscr A_{\mathrm{liaison}},\mathscr V_{\mathrm{rel}}\rangle=0$ pour le mouvement relatif admis ; par exemple une pivot parfaite : seuls les moments transversaux à l'axe et les trois forces sont transmis.

# 5. Y a-t-il d'autres torseurs ?

| Objet | Est-ce un torseur ? | Commentaire |
| --- | --- | --- |
| **Torseur statique** | oui (c'est $\mathscr A$) | Pas un nouvel objet : $\mathscr A^{\mathrm{ext}}=0$ à l'équilibre. |
| **Torseur d'une liaison / d'un contact** | oui (type moment) | Torseur d'action particulier, forme imposée par la liaison. |
| **Couple** | oui (cas particulier) | $\vec R=0$, donc $\mathsf M$ **indépendant du point** (V, §5.3). |
| **Glisseur** | oui (cas particulier) | Il existe un point où $\mathsf M=0$ ; le lieu est une droite parallèle à $\vec R$ (V, §5.4). |
| **Torseur des forces d'inertie** | oui | $-\mathscr D$ (dans le référentiel d'inertie d'entraînement), cf. D'Alembert. |
| **Torseur des actions intérieures** | oui (nul si forces centrales) | $\mathscr A^{\mathrm{int}}=0$. |
| **Torseur cinétique barycentrique** | oui | $\{\vec 0;\mathsf L^\ast\}$ : résultante nulle, donc moment indépendant du point (III §3.3). |
| **« Torseur d'accélération »** $\{\vec a(A);\dot\Omega\}$ | **non** | Voir ci-dessous. |
| **« Torseur d'inertie »** | **non** | C'est le tenseur / opérateur d'inertie $\mathbb M$ (§3.1). |
| **Torseur de contrainte (milieu continu)** | oui, par intégration | $\{\int\sigma\cdot n\,dS;\int\overrightarrow{AM}\wedge\sigma\cdot n\,dS\}$ : torseur de cohésion en RDM. |

>[!warning]- Le champ des accélérations d'un solide n'est **pas** un torseur
>Dérivons $\vec v(B)=\vec v(A)+\Omega(\overrightarrow{AB})$ :
>$$
>\vec a(B)=\vec a(A)+\dot\Omega(\overrightarrow{AB})+\Omega\big(\Omega(\overrightarrow{AB})\big).
>$$
>Le terme $\Omega^2(\overrightarrow{AB})$ est **quadratique** en $\Omega$ : la loi de changement de point n'est pas linéaire en la « résultante » $\dot\Omega$, donc pas de structure de torseur (III §10.1). Seul le torseur **dynamique** $\{\vec S;\mathsf D\}$, obtenu en intégrant avec $dm$, en est un : l'intégration $\int\overrightarrow{AM}\wedge\vec a\,dm$ ré-injecte l'identité BABAR par bilinéarité de $\wedge$ (V §3.2).

# 6. Généralisation : un schéma unique

## 6.1 Construction générale

Soit $\beta:V\times U\to W$ bilinéaire (V, §4). Pour une famille de « vecteurs appliqués » $(M,\vec u)$ de densité $d\vec u$ :
$$
\vec R_U=\int d\vec u,\qquad\mathcal M_A^\beta=\int\beta(\overrightarrow{AM},d\vec u)\ \Longrightarrow\ \mathcal M_B^\beta=\mathcal M_A^\beta+\beta(\overrightarrow{BA},\vec R_U).
$$
Avec $\beta=\wedge$ et $d\vec u\in\{d\vec F,\ \vec v\,dm,\ \vec a\,dm\}$ on obtient les trois torseurs de type moment : **actions, cinétique, dynamique**. Toute grandeur « volumique de type vecteur appliqué » donne ainsi un torseur ; l'**intérêt physique** demande une loi (PFD, conservation, …), pas seulement l'algèbre.

>[!example]- Exemples à nouveaux torseurs, par la même recette
>- **Torseur de densité de courant de quantité de mouvement** (milieu continu) : $\{\int\sigma\cdot n\,dS;\ \int\overrightarrow{AM}\wedge\sigma\cdot n\,dS\}$ (efforts de surface).
>- **Torseur de flux d'énergie ou de masse** : la résultante est un vecteur, mais le moment $\overrightarrow{AM}\wedge\vec j$ n'a pas de rôle dynamique classique ; on peut le définir sans qu'il soit utile.
>- **Torseur électromagnétique** (impulsion et moment cinétique du champ) : $\vec P_{\mathrm{em}}=\int\varepsilon_0\vec E\times\vec B\,dV$, $\mathsf L_{\mathrm{em}}(A)=\int\overrightarrow{AM}\wedge\varepsilon_0(\vec E\times\vec B)\,dV$ ; le torseur total (matière + champ) est conservé pour un système isolé.

## 6.2 Les torseurs sont des charges de Noether du groupe euclidien

D'après III §8 : la symétrie par translations $\Rightarrow$ $\vec P$, par rotations $\Rightarrow$ $\mathsf L^{ij}$. **Le torseur cinétique $\{\vec P;\mathsf L\}$ est donc l'application moment du groupe $SE(n)$** agissant sur l'espace des phases : à chaque élément $\xi=\{\Omega;\vec v\}$ de $\mathfrak{se}(n)$ correspond la charge $\langle\mathscr C,\xi\rangle=\vec P\cdot\vec v+\tfrac12\mathsf L^{ij}\Omega_{ji}$ (au signe de convention près). Alors
$$
\frac{d}{dt}\langle\mathscr C,\xi\rangle=\langle\mathscr A^{\mathrm{ext}},\xi\rangle\quad\forall\xi\ \text{(fixe)}\ \Longleftrightarrow\ \mathscr D=\mathscr A^{\mathrm{ext}}
$$
au sens $\xi$ constant ($A$ fixe), et $\mathscr C$ est **conservé** si $\mathscr A^{\mathrm{ext}}=0$ (système isolé : $\vec P,\mathsf L$ conservés, dont $\tfrac{n(n+1)}{2}$ charges).

## 6.3 Lien avec le GGE : le torseur cinématique comme multiplicateur de Lagrange

Un équilibre statistique d'un système invariant par $SE(n)$ et Galilée-invariant peut porter, outre $H$ et $N$, les charges $\vec P$ et $\mathsf L$ :
$$
\hat\rho=\frac1Z\exp\!\big[-\beta\big(\hat H-\mu\hat N-\langle\hat{\mathscr C},\mathscr V\rangle\big)\big]=\frac1Z\exp\!\Big[-\beta\Big(\hat H-\mu\hat N-\vec u\cdot\hat{\vec P}-\tfrac12\Omega_{ji}\hat{\mathsf L}^{ij}\Big)\Big].
$$
Les multiplicateurs de Lagrange associés à $\vec P$ et $\mathsf L$ sont exactement les composantes $(\vec u,\Omega)$ d'un **torseur cinématique** : l'état d'équilibre est un état en **mouvement d'ensemble rigide** (translation $\vec u$ et rotation $\Omega$). Ceci est le GGE « géométrique » : il généralise le GGE à deux charges de $SE(n)$.
Pour un système intégrable (Lieb–Liniger) on ajoute les charges supplémentaires $\hat Q_k$ ($k\ge 2$) non géométriques ; en dimension $n=1$, $\mathfrak{se}(1)=\mathbb R$ : le torseur se réduit à $\vec P$, et la rotation disparaît. Les charges supplémentaires ne sont pas des torseurs : elles n'ont pas de loi de changement de point.

# 7. Checklist

>[!question]- Contrôles de cohérence
>1. Type moment : résultante $\in V$, champ $\in\Lambda^2V$, $\mathsf M(B)=\mathsf M(A)+\overrightarrow{BA}\wedge\vec R$.
>2. Type vitesse : résultante $\Omega\in\mathfrak{so}(V,g)$, champ $\vec v\in V$, $\vec v(B)=\vec v(A)+\Omega(\overrightarrow{AB})$.
>3. $\dim=n(n+1)/2$ ; le produit vectoriel n'existe qu'en $n=3$.
>4. Le torseur d'accélération et le torseur d'inertie **n'existent pas** comme torseurs ; ce sont un champ non affine ($\Omega^2$) et un opérateur.
>5. $\mathsf D(A)=\dot{\mathsf L}(A)+\vec v_A\wedge\vec P$ : point fixe ou $G$ pour simplifier.
>6. Puissance : $\langle\mathscr A,\mathscr V\rangle=\vec F\cdot\vec v_A+\tfrac12\mathsf M^{ij}\Omega_{ji}$, indépendante du point.
>7. « Torseur d'action » $\ne$ « action » variationnelle.

>[!warning]- Corrections par rapport à la note ChatGPT d'origine
>- « Torseur d'accélération » $(\vec a,\dot{\boldsymbol\Omega})$ est présenté comme un torseur : **faux**, à cause du terme $\Omega^2$.
>- « Torseur d'inertie » : appellation à éviter ; il s'agit du tenseur d'inertie / de l'opérateur $\mathbb M$.
>- « Torseur statique » : simple cas d'équilibre du torseur d'actions.
>- Le produit contracté « $\mathbf M_A:\boldsymbol\Omega$ » n'est pas normalisé : il faut le facteur $\tfrac12$ avec $\mathsf M^{ij}\Omega_{ji}$ (et il y a un signe selon l'ordre des indices) pour retrouver $\vec M\cdot\vec\omega$ en dimension 3.
>- La chaîne « cinétique $\to$ dynamique par dérivation » n'est vraie à point de réduction fixe (ou $A=G$) ; sinon, $\mathsf D=\dot{\mathsf L}+\vec v_A\wedge\vec P$.
>- La première réponse (densités, GGE) répondait à une autre question (densités conservées) ; le seul lien exact avec les torseurs est §6.2–6.3.

# 8. Formulaire

$$
\boxed{\mathscr C=\mathbb M\,\mathscr V},\quad \boxed{\mathsf D(A)=\dot{\mathsf L}(A)+\vec v_A\wedge\vec P},\quad \boxed{\mathscr D=\mathscr A^{\mathrm{ext}}}\ (\mathscr R\text{ galiléen})
$$
$$
\boxed{\langle\mathscr T,\mathscr V\rangle=\vec R\cdot\vec v_A+\tfrac12\mathsf M^{ij}\Omega_{ji}},\qquad \boxed{\mathcal E_c=\tfrac12\langle\mathscr C,\mathscr V\rangle},\qquad \boxed{\dot{\mathcal E}_c=\langle\mathscr A^{\mathrm{ext}},\mathscr V\rangle\ (\text{solide})}
$$
