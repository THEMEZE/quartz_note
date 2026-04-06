---
title: Forme différentielle
tags:
  - Science
---

Pour les articles homonymes, voir [Forme](https://fr.wikipedia.org/wiki/Forme "Forme").

En [géométrie différentielle](https://fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_diff%C3%A9rentielle "Géométrie différentielle"), une **[forme différentielle](https://fr.wikipedia.org/wiki/Forme_diff%C3%A9rentielle)** est la donnée d'un champ d'[applications multilinéaires alternées](https://fr.wikipedia.org/wiki/Application_multilin%C3%A9aire#Application_altern%C3%A9e "Application multilinéaire") sur les [espaces tangents](https://fr.wikipedia.org/wiki/Espace_tangent "Espace tangent") d'une [variété différentielle](https://fr.wikipedia.org/wiki/Vari%C3%A9t%C3%A9_diff%C3%A9rentielle "Variété différentielle") possédant une certaine régularité. Le **degré** des formes différentielles désigne le degré des applications multilinéaires. La [différentielle](https://fr.wikipedia.org/wiki/Diff%C3%A9rentielle "Différentielle") d'une fonction numérique peut être regardée comme un champ de [formes linéaires](https://fr.wikipedia.org/wiki/Forme_lin%C3%A9aire "Forme linéaire") : c'est le premier exemple de formes différentielles. Au-delà de cet exemple, non seulement les formes différentielles interviennent naturellement dans les problèmes de géométrie différentielle, mais elles permettent de définir des structures importantes, comme les [formes volumes](https://fr.wikipedia.org/wiki/Forme_volume "Forme volume"), les [formes symplectiques](https://fr.wikipedia.org/wiki/Forme_symplectique "Forme symplectique"), les [formes de contact](https://fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_de_contact "Géométrie de contact") ou encore les [connexions](https://fr.wikipedia.org/wiki/Connexion_\(math%C3%A9matiques\) "Connexion (mathématiques)").

La manipulation des formes différentielles fait intervenir un certain nombre d'opérations, dont le [produit extérieur](https://fr.wikipedia.org/wiki/Produit_ext%C3%A9rieur "Produit extérieur"), le [produit intérieur](https://fr.wikipedia.org/wiki/Produit_int%C3%A9rieur "Produit intérieur"), la [dérivée extérieure](https://fr.wikipedia.org/wiki/D%C3%A9riv%C3%A9e_ext%C3%A9rieure "Dérivée extérieure") et la [dérivée de Lie](https://fr.wikipedia.org/wiki/D%C3%A9riv%C3%A9e_de_Lie "Dérivée de Lie"). En particulier, la dérivée extérieure permet de distinguer les [formes fermées](https://fr.wikipedia.org/wiki/Forme_diff%C3%A9rentielle_ferm%C3%A9e "Forme différentielle fermée") et les [formes exactes](https://fr.wikipedia.org/wiki/Diff%C3%A9rentielle_exacte "Différentielle exacte"). Cette distinction permet dans un second temps de définir les espaces de [cohomologie de De Rham](https://fr.wikipedia.org/wiki/Cohomologie_de_De_Rham "Cohomologie de De Rham").

Les problèmes de régularité ne sont pas abordés dans cet article. On fera donc implicitement l'hypothèse que les fonctions introduites sont de [classe $\mathcal C^\infty$](https://fr.wikipedia.org/wiki/Classe_de_r%C3%A9gularit%C3%A9 "Classe de régularité").


[![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Differential_Form_1.png/250px-Differential_Form_1.png)](https://commons.wikimedia.org/wiki/File:Differential_Form_1.png?uselang=fr)

Exemple visuel d’une forme différentielle en géométrie différentielle.

## Définitions

### Forme différentielle de degré 1

Article détaillé : [Forme différentielle de degré 1](https://fr.wikipedia.org/wiki/Forme_diff%C3%A9rentielle_de_degr%C3%A9_un "Forme différentielle de degré un").

Les formes différentielles de degré 1 – ou 1-formes – sont des champs de [formes linéaires](https://fr.wikipedia.org/wiki/Forme_lin%C3%A9aire "Forme linéaire") sur une variété différentielle. Dit autrement, on se donne une forme linéaire en chaque espace tangent ${\displaystyle T_{x}M}$ avec une dépendance régulière en ${\displaystyle x}$. La dépendance en ${\displaystyle x}$ peut facilement être précisée par l'expression dans des [cartes locales](https://fr.wikipedia.org/wiki/Vari%C3%A9t%C3%A9_\(g%C3%A9om%C3%A9trie\) "Variété (géométrie)"). On les appelle parfois **covecteurs** ou **champs de covecteurs** ; ces outils ont des propriétés analogues aux [champs de vecteurs](https://fr.wikipedia.org/wiki/Champs_de_vecteurs "Champs de vecteurs"). Il existe en réalité un isomorphisme une fois introduite, par exemple, une [métrique riemannienne](https://fr.wikipedia.org/wiki/M%C3%A9trique_riemannienne "Métrique riemannienne"). Si ${\displaystyle f}$ est une fonction réelle différentiable, sa différentielle ${\displaystyle \mathrm {d} f}$ est une 1-forme différentielle (dite exacte) qui en chaque point ${\displaystyle x}$ vaut la forme linéaire ${\displaystyle \mathrm {d} f(x)}$. Localement, les 1-formes différentielles s'expriment comme combinaisons de différentielles de fonctions.

Plus exactement, le [dual](https://fr.wikipedia.org/wiki/Espace_dual "Espace dual") de l'espace vectoriel réel ${\displaystyle \mathbb {R} ^{n}}$ est un [espace vectoriel](https://fr.wikipedia.org/wiki/Espace_vectoriel "Espace vectoriel") de [dimension](https://fr.wikipedia.org/wiki/Dimension_d%27un_espace_vectoriel "Dimension d'un espace vectoriel") $n$ . Si ${\displaystyle (x_{1},...,x_{n})}$  désigne les coordonnées dans ${\displaystyle \mathbb {R} ^{n}}$ , alors on note ${\displaystyle \mathrm {d} x_{i}}$ l'application ${\displaystyle i}$-ème coordonnée ${\displaystyle (x_{1},\ldots ,x_{n})\mapsto x_{i}}$. Les formes linéaires sur ${\displaystyle \mathbb {R} ^{n}}$ s'expriment comme des combinaisons à coefficients réels des formes linéaires ${\displaystyle \mathrm {d} x_{1},...,\mathrm {d} x_{n}}$. Les 1-formes différentielles ${\displaystyle \lambda }$ s'expriment alors comme des combinaisons des ${\displaystyle \mathrm {d} x_{1},...,\mathrm {d} x_{n}}$ dont les coefficients ${\displaystyle \lambda _{i}}$ dépendent de manière ${\displaystyle {\mathcal {C}}^{\infty }}$ du point de base ${\displaystyle x\in \mathbb {R} ^{n}}$ :
$$
{\displaystyle \lambda _{x}=\lambda _{1}(x)\cdot \mathrm {d} x_{1}+\dots +\lambda _{n}(x)\cdot \mathrm {d} x_{n}}
$$

Sur une variété différentielle _M_, une 1-forme différentielle s'exprime localement comme ci-dessus dans les cartes locales. L'exemple le plus simple est la [différentielle](https://fr.wikipedia.org/wiki/Diff%C3%A9rentielle "Différentielle") d'une fonction ${\displaystyle f:\mathbb {R} ^{n}\to \mathbb {R} }$ en un point _a_
$$
{\displaystyle \mathrm {d} _{a}f=\sum _{i=1}^{n}{\frac {\partial f}{\partial x_{i}}}(a)\mathrm {d} x_{i}\quad \in (T_{a}\mathbb {R} ^{n})^{*}}
$$

Si _X_ est un champ de vecteurs sur _M_ et λ est une 1-forme différentielle, alors ${\displaystyle \lambda (X):x\in M\to \lambda _{x}(X(x))\in \mathbb {R} }$ est différentiable ; cette fonction est linéaire en _X_. Cela permet de regarder une 1-forme différentielle comme une forme linéaire sur le [module](https://fr.wikipedia.org/wiki/Module_sur_un_anneau "Module sur un anneau") des champs de vecteurs sur _M_ (dont l'anneau de base est l'ensemble des fonctions de _M_ dans ℝ).

### Définition comme champ de formes multilinéaires alternées

Les formes différentielles se définissent comme une extension en géométrie différentielle des [formes multilinéaires](https://fr.wikipedia.org/wiki/Forme_multilin%C3%A9aire "Forme multilinéaire") [alternées](https://fr.wikipedia.org/wiki/Application_multilin%C3%A9aire#Application_altern%C3%A9e "Application multilinéaire").

Pour une variété différentielle _M_, une **forme différentielle ω de degré _k_** sur _M_ est un champ d'applications _k_-linéaires alternées sur les espaces tangents ${\displaystyle T_{x}M}$ avec une dépendance régulière en _x_ : pour tous champs de vecteurs ${\displaystyle X_{1},...,X_{k}}$, la fonction ${\displaystyle x\mapsto \omega _{x}(X_{1}(x),\dots ,X_{k}(x))}$ est de classe $\mathcal C^\infty$.

De même que pour les 1-formes différentielles, il est possible de donner l'expression locale des formes différentielles de degré _k_ grâce au produit extérieur (voir plus bas).

### Définition comme section d'un fibré

L'ensemble des applications multilinéaires alternées sur ${\displaystyle T_{x}M}$ forme un espace vectoriel noté ${\displaystyle \Lambda ^{k}T_{x}^{*}M}$. L'ensemble de ces espaces forme ce qu'on appelle un [fibré vectoriel](https://fr.wikipedia.org/wiki/Fibr%C3%A9_vectoriel "Fibré vectoriel") sur _M_, noté ${\displaystyle \Lambda ^{k}T^{*}M}$, formellement la _k_-ième puissance du [fibré cotangent](https://fr.wikipedia.org/wiki/Fibr%C3%A9_cotangent "Fibré cotangent") de _M_. Une forme différentielle de degré _k_ peut se redéfinir comme une [section](https://fr.wikipedia.org/wiki/Section_d%27un_fibr%C3%A9 "Section d'un fibré") globale de ce fibré vectoriel.

Cette approche permet non seulement de donner une meilleure signification à la régularité de la forme différentielle, mais permet aussi d'étendre la définition des formes différentielles. Si _E_ est un fibré vectoriel sur _M_, une forme différentielle de degré _k_ à valeurs dans _E_ est une section globale du [produit tensoriel](https://fr.wikipedia.org/wiki/Produit_tensoriel "Produit tensoriel") ${\displaystyle \Lambda ^{k}T^{*}M\otimes E}$. C'est donc un champ d'applications multilinéaires alternées à valeurs dans les fibres de _E_. De telles formes peuvent aussi être définies comme des applications multilinéaires alternées du module _X_(_M_) dans le module des sections globales de _E_.

## Opérations sur les formes différentielles

La manipulation des formes différentielles en pratique exige un ensemble d'opérations élémentaires. Certaines sont purement algébriques et se définissent en réalité pour toutes applications multilinéaires alternées. D'autres sont propres à la [topologie différentielle](https://fr.wikipedia.org/wiki/Topologie_diff%C3%A9rentielle "Topologie différentielle") et aux formes différentielles.

### Opérations algébriques

Par définition, l'ensemble des formes différentielles (réelles) de degré _k_ sur une variété différentielle _M_ forme un module ${\displaystyle \Omega ^{k}(M)}$ sur C∞(_M_). En particulier, les formes différentielles de degré _k_ s'additionnent ou peuvent être multipliées par des fonctions réelles :
$$
{\displaystyle (\alpha +\beta )_{x}(v_{1},\dots ,v_{k})=\alpha _{x}(v_{1},\dots ,v_{k})+\beta _{x}(v_{1},\dots ,v_{k})} ;
$$
$$
{\displaystyle (f\alpha )_{x}(v_{1},\dots ,v_{k})=f(x)\cdot \alpha _{x}(v_{1},\dots ,v_{k})}.
$$

Produit intérieur

Le [produit intérieur](https://fr.wikipedia.org/wiki/Produit_int%C3%A9rieur "Produit intérieur") se définit en [algèbre linéaire](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_lin%C3%A9aire "Algèbre linéaire"), définition qui s'étend naturellement aux formes différentielles. Si _X_ est un champ de vecteurs et α une forme différentielle de dimension _k_, on définit une forme différentielle de degré _k_ – 1, par :
$$
{\displaystyle (\iota _{X}\alpha )_{x}(v_{2},\dots ,v_{k})=\alpha _{x}(X(x),v_{2},\dots ,v_{k})}.
$$
Produit extérieur

Le [produit extérieur](https://fr.wikipedia.org/wiki/Produit_ext%C3%A9rieur "Produit extérieur") de deux formes différentielles α et β de degrés respectifs _k_ et _q_ se définit comme suit :
$$
{\displaystyle (\alpha \wedge \beta )_{x}(v_{1},\dots ,v_{k+q})=\sum \varepsilon (\sigma )\cdot \alpha _{x}(v_{\sigma (1)},\dots ,v_{\sigma (k)})\cdot \beta _{x}(v_{\sigma (k+1)},\dots ,v_{\sigma (k+q)})},
$$

où ${\displaystyle \varepsilon (\sigma )}$ désigne la signature de la permutation σ et la somme porte sur toutes les [permutations](https://fr.wikipedia.org/wiki/Permutation "Permutation") σ de [1, _k + q_] croissantes sur les _k_ premiers entiers et croissantes sur les _q_ derniers. Le résultat est une forme de degré _k + q_.

Ces opérations munissent ${\displaystyle \Omega (M)=\oplus \Omega ^{k}(M)}$ d'une structure d'[algèbre graduée](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_gradu%C3%A9e "Algèbre graduée") commutative. Ici, [commutatif](https://fr.wikipedia.org/wiki/Commutatif "Commutatif") signifie que pour toutes formes différentielles α et β de degrés respectifs _k_ et _q_, on a :
$$
{\displaystyle \alpha \wedge \beta =(-1)^{kq}\beta \wedge \alpha .}
$$

[Image réciproque (pullback)](https://fr.wikipedia.org/wiki/Image_r%C3%A9ciproque_\(g%C3%A9om%C3%A9trie_diff%C3%A9rentielle\) "Image réciproque (géométrie différentielle)")

Si ${\displaystyle f:M\rightarrow N}$ est une application de classe $\mathcal C^1$ et si α est une forme différentielle de degré _k_ sur _N_, on définit ${\displaystyle f^{*}\alpha }$ comme une forme différentielle de degré _k_ sur _M_ par :
$$
{\displaystyle (f^{*}\alpha )_{x}(v_{1},\dots ,v_{k})=\alpha _{f(x)}(\mathrm {d} f_{x}(v_{1}),\dots ,\mathrm {d} f_{x}(v_{k}))}.
$$

L'application ${\displaystyle f^{*}:\Omega (N)\rightarrow \Omega (M)}$ définit un morphisme d'algèbres graduées.

### Dérivée extérieure

Article détaillé : [Dérivée extérieure](https://fr.wikipedia.org/wiki/D%C3%A9riv%C3%A9e_ext%C3%A9rieure "Dérivée extérieure").

La dérivée extérieure est définie comme l'unique application ${\displaystyle \mathrm {d} :\Omega (M)\to \Omega (M)}$, transformant les _k_-formes en (_k_ + 1)-formes, et vérifiant :

- si _f_ est une [fonction lisse](https://fr.wikipedia.org/wiki/Classe_de_r%C3%A9gularit%C3%A9 "Classe de régularité"), la [1-forme](https://fr.wikipedia.org/wiki/Forme_diff%C3%A9rentielle_de_degr%C3%A9_un "Forme différentielle de degré un") d_f_ est la [différentielle](https://fr.wikipedia.org/wiki/Vari%C3%A9t%C3%A9_diff%C3%A9rentielle#Vecteurs_tangents_et_diff%C3%A9rentielle_d'une_application "Variété différentielle") de _f_ ;
- pour toutes formes α et β, où α est de degré _p_ : ${\displaystyle \mathrm {d} (\alpha \wedge \beta )=\mathrm {d} \alpha \wedge \beta +(-1)^{p}(\alpha \wedge \mathrm {d} \beta )}$ ;
- le [carré](https://fr.wikipedia.org/wiki/Composition_de_fonctions#Puissances_fonctionnelles "Composition de fonctions") de d est nul : d(dω) = 0.

Une forme différentielle ω pouvant s'écrire comme une dérivée extérieure (ω = dξ) est dite [exacte](https://fr.wikipedia.org/wiki/Diff%C3%A9rentielle_exacte "Différentielle exacte").

Une forme différentielle ω dont la dérivée est nulle (dω = 0) est dite [fermée](https://fr.wikipedia.org/wiki/Forme_diff%C3%A9rentielle_ferm%C3%A9e "Forme différentielle fermée").

Les formes exactes et les formes fermées sont donc, respectivement, l'[image](https://fr.wikipedia.org/wiki/Image_d%27une_application "Image d'une application") et le [noyau](https://fr.wikipedia.org/wiki/Noyau_\(alg%C3%A8bre\)#Noyau_d'une_application_lin%C3%A9aire "Noyau (algèbre)") de d.

Le troisième axiome se reformule en : « toute forme exacte est fermée ».

La [réciproque](https://fr.wikipedia.org/wiki/R%C3%A9ciproque "Réciproque") n'est pas vraie en général, et l'étude des liens entre formes exactes et formes fermées conduit à la théorie de la [cohomologie de De Rham](https://fr.wikipedia.org/wiki/Cohomologie_de_De_Rham "Cohomologie de De Rham").

### Dérivée de Lie

Article détaillé : [Dérivée de Lie](https://fr.wikipedia.org/wiki/D%C3%A9riv%C3%A9e_de_Lie "Dérivée de Lie").

Une 0-forme différentielle est une fonction différentiable ${\displaystyle f}$ ; considérer sa dérivée selon un champ de vecteurs _X_ consiste à introduire la fonction ${\displaystyle \mathrm {d} f(X)}$. La dérivée de Lie d'une forme différentielle α de degré _k_ selon un champ de vecteurs _X_ est une forme différentielle de degré _k_ notée ${\displaystyle {\mathcal {L}}_{X}\alpha }$ définie par :
$$
{\displaystyle {\mathcal {L}}_{X}\alpha ={\frac {d}{dt}}\varphi _{t}^{\ast }(\alpha )\mid _{t=0}.}
$$
On démontre (formule de Cartan) que
$$
{\displaystyle {\mathcal {L}}_{X}\alpha =\mathrm {d} \iota _{X}\alpha +\iota _{X}d\alpha .}
$$

## Expression locale

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Logo_travaux_orange-simple.svg/20px-Logo_travaux_orange-simple.svg.png)](https://commons.wikimedia.org/wiki/File:Logo_travaux_orange-simple.svg?uselang=fr)

Cette section est vide, insuffisamment détaillée ou incomplète. [Votre aide](https://fr.wikipedia.org/wiki/Sp%C3%A9cial:EditPage/Forme_diff%C3%A9rentielle "Spécial:EditPage/Forme différentielle") est la bienvenue ! [Comment faire ?](https://fr.wikipedia.org/wiki/Aide:Comment_modifier_une_page "Aide:Comment modifier une page")

## Intégration des formes

Les formes différentielles de degré _k_ sont intégrées sur des [chaînes](https://fr.wikipedia.org/wiki/Complexe_simplicial#Homologie_simpliciale "Complexe simplicial") de dimension _k_. Si _k_ est nul, alors il s'agit d'une évaluation des fonctions aux points considérés. D'autres valeurs de _k_, avec _k_ > 0, correspondent aux [intégrales curvilignes](https://fr.wikipedia.org/wiki/Int%C3%A9grale_curviligne "Intégrale curviligne"), [de surface](https://fr.wikipedia.org/wiki/Int%C3%A9grale_de_surface "Intégrale de surface"), de volume, etc.

Soit
$$
{\displaystyle \omega =\sum a_{i_{1},\cdots ,i_{k}}({\mathbf {x} })\,\mathrm {d} x_{i_{1}}\wedge \cdots \wedge \mathrm {d} x_{i_{k}}}
$$

une forme différentielle et _S_ un ouvert d'une [variété orientée](https://fr.wikipedia.org/wiki/Vari%C3%A9t%C3%A9_diff%C3%A9rentielle "Variété différentielle") de dimension _k_ [plongée dans **R**_n_](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_plongement_de_Whitney "Théorème de plongement de Whitney"), paramétré par :
$$
{\displaystyle S({\mathbf {u} })=(x_{1}({\mathbf {u} }),\cdots ,x_{n}({\mathbf {u} }))}
$$

avec **u** un paramètre dans le domaine _D_. Alors [Rudin 1976](https://fr.wikipedia.org/wiki/Forme_diff%C3%A9rentielle#Rudin1976) définit l'intégrale de la forme différentielle sur _S_ par :
$$
{\displaystyle \int _{S}\omega =\int _{D}\sum a_{i_{1},\cdots ,i_{k}}(S({\mathbf {u} })){\frac {\partial (x_{i_{1}},\cdots ,x_{i_{k}})}{\partial (u_{1},\cdots ,u_{k})}}\,\mathrm {d} {\mathbf {u} }}
$$

où
$$
{\displaystyle {\frac {\partial (x_{i_{1}},\cdots ,x_{i_{k}})}{\partial (u_{1},\cdots ,u_{k})}}}
$$

est le déterminant [jacobien](https://fr.wikipedia.org/wiki/Jacobien "Jacobien").

D'après le [théorème de changement de variables](https://fr.wikipedia.org/wiki/Int%C3%A9grale_multiple#Changement_de_variables "Intégrale multiple"), cette définition ne dépend pas du paramétrage (compatible avec l'orientation) de l'ouvert.

Article connexe : [Théorème de Stokes](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Stokes "Théorème de Stokes").

## Références

- (en) Cet article est partiellement ou en totalité issu de l’article de Wikipédia en anglais intitulé « [Differential form](https://en.wikipedia.org/wiki/Differential_form?oldid=23329898) » ([voir la liste des auteurs](https://en.wikipedia.org/wiki/Differential_form?action=history)).
- (en) [Raoul Bott](https://fr.wikipedia.org/wiki/Raoul_Bott "Raoul Bott") et Loring W. Tu, Differential Forms in Algebraic Topology, [Springer](https://fr.wikipedia.org/wiki/Springer_Verlag "Springer Verlag"), coll. « [GTM](https://fr.wikipedia.org/wiki/Graduate_Texts_in_Mathematics "Graduate Texts in Mathematics") » (no 82), 1982 ([lire en ligne](https://books.google.com/books?id=COuPBAAAQBAJ) [[archive](https://archive.wikiwix.com/cache/?url=https%3A%2F%2Fbooks.google.com%2Fbooks%3Fid%3DCOuPBAAAQBAJ "archive sur Wikiwix")])
- (en) [Walter Rudin](https://fr.wikipedia.org/wiki/Walter_Rudin "Walter Rudin"), Principles of Mathematical Analysis, New York, McGraw-Hill, 1976 ([ISBN](https://fr.wikipedia.org/wiki/International_Standard_Book_Number "International Standard Book Number") [978-0-07054235-8](https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Ouvrages_de_r%C3%A9f%C3%A9rence/978-0-07054235-8 "Spécial:Ouvrages de référence/978-0-07054235-8"))
- (en) [Michael Spivak](https://fr.wikipedia.org/wiki/Michael_Spivak "Michael Spivak"), _Calculus on Manifolds_, Benjamin, 1965 ([ISBN](https://fr.wikipedia.org/wiki/International_Standard_Book_Number "International Standard Book Number") [978-0-80539021-6](https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Ouvrages_de_r%C3%A9f%C3%A9rence/978-0-80539021-6 "Spécial:Ouvrages de référence/978-0-80539021-6")) [[lire en ligne](https://books.google.fr/books?id=oMGc3zwvw34C) [[archive](https://archive.wikiwix.com/cache/?url=https%3A%2F%2Fbooks.google.fr%2Fbooks%3Fid%3DoMGc3zwvw34C "archive sur Wikiwix")]]
- (en) Vladimir A. Zorich, _Mathematical Analysis II_, Springer, 2004 ([ISBN](https://fr.wikipedia.org/wiki/International_Standard_Book_Number "International Standard Book Number") [978-3-540-40633-4](https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Ouvrages_de_r%C3%A9f%C3%A9rence/978-3-540-40633-4 "Spécial:Ouvrages de référence/978-3-540-40633-4")) [[lire en ligne](https://books.google.fr/books?id=XF8W9W-eyrgC) [[archive](https://archive.wikiwix.com/cache/?url=https%3A%2F%2Fbooks.google.fr%2Fbooks%3Fid%3DXF8W9W-eyrgC "archive sur Wikiwix")]]
- (fr) Henri Cartan,_Formes différentielles_, Hermann, 1967 plusieurs rééditions, la dernière en 2007

## Voir aussi

- [Variété (géométrie)](https://fr.wikipedia.org/wiki/Vari%C3%A9t%C3%A9_\(g%C3%A9om%C3%A9trie\) "Variété (géométrie)")
- [Forme différentielle complexe](https://fr.wikipedia.org/wiki/Forme_diff%C3%A9rentielle_complexe "Forme différentielle complexe")
- [Différentielle de Kähler](https://fr.wikipedia.org/wiki/Diff%C3%A9rentielle_de_K%C3%A4hler "Différentielle de Kähler")

| Variété différentielle |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Variétés               | - [Variété différentielle](https://fr.wikipedia.org/wiki/Vari%C3%A9t%C3%A9_diff%C3%A9rentielle "Variété différentielle")<br>- [Variété riemannienne](https://fr.wikipedia.org/wiki/Vari%C3%A9t%C3%A9_riemannienne "Variété riemannienne")<br>- [Variété pseudo-riemannienne](https://fr.wikipedia.org/wiki/Vari%C3%A9t%C3%A9_pseudo-riemannienne "Variété pseudo-riemannienne")<br>- [Fibré tangent](https://fr.wikipedia.org/wiki/Fibr%C3%A9_tangent "Fibré tangent")<br>- [Fibré cotangent](https://fr.wikipedia.org/wiki/Fibr%C3%A9_cotangent "Fibré cotangent")                                                                                                                                                                                                                |
| Champs                 | - [Champ](https://fr.wikipedia.org/wiki/Champ_\(math%C3%A9matiques\) "Champ (mathématiques)")<br>- [Champ de vecteurs](https://fr.wikipedia.org/wiki/Champ_de_vecteurs "Champ de vecteurs")<br>- [Champ tensoriel](https://fr.wikipedia.org/wiki/Champ_tensoriel "Champ tensoriel")<br>- [Flot (mathématiques)](https://fr.wikipedia.org/wiki/Flot_\(math%C3%A9matiques\) "Flot (mathématiques)")<br>- Forme différentielle                                                                                                                                                                                                                                                                                                                                                        |
| Connexions             | - [Connexion (mathématiques)](https://fr.wikipedia.org/wiki/Connexion_\(math%C3%A9matiques\) "Connexion (mathématiques)")<br>- [Connexion de Koszul](https://fr.wikipedia.org/wiki/Connexion_de_Koszul "Connexion de Koszul")<br>- [Connexion de Levi-Civita](https://fr.wikipedia.org/wiki/Connexion_de_Levi-Civita "Connexion de Levi-Civita")<br>- [Connexion affine](https://fr.wikipedia.org/wiki/Connexion_affine "Connexion affine")<br>- [Connexion d'Ehresmann](https://fr.wikipedia.org/wiki/Connexion_d%27Ehresmann "Connexion d'Ehresmann")<br>- [Dérivée covariante](https://fr.wikipedia.org/wiki/D%C3%A9riv%C3%A9e_covariante "Dérivée covariante")<br>- [Symboles de Christoffel](https://fr.wikipedia.org/wiki/Symboles_de_Christoffel "Symboles de Christoffel") |
| Géométrie              | - [Courbure](https://fr.wikipedia.org/wiki/Courbure "Courbure")<br>- [Géodésique](https://fr.wikipedia.org/wiki/G%C3%A9od%C3%A9sique "Géodésique")<br>- [Équation des géodésiques](https://fr.wikipedia.org/wiki/%C3%89quation_des_g%C3%A9od%C3%A9siques "Équation des géodésiques")<br>- [Holonomie](https://fr.wikipedia.org/wiki/Holonomie "Holonomie")                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Opérateurs             | - [Crochet de Lie](https://fr.wikipedia.org/wiki/Crochet_de_Lie "Crochet de Lie")<br>- [Crochet de Poisson](https://fr.wikipedia.org/wiki/Crochet_de_Poisson "Crochet de Poisson")<br>- [Dérivée de Lie](https://fr.wikipedia.org/wiki/D%C3%A9riv%C3%A9e_de_Lie "Dérivée de Lie")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

-  [![icône décorative](https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Circle-icons-rulertriangle.svg/40px-Circle-icons-rulertriangle.svg.png)](https://fr.wikipedia.org/wiki/Portail:G%C3%A9om%C3%A9trie "Portail de la géométrie") [Portail de la géométrie](https://fr.wikipedia.org/wiki/Portail:G%C3%A9om%C3%A9trie "Portail:Géométrie")

[Catégories](https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Accueil "Catégorie:Accueil") : 

- [Topologie différentielle](https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Topologie_diff%C3%A9rentielle "Catégorie:Topologie différentielle")
- [Forme différentielle](https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Forme_diff%C3%A9rentielle "Catégorie:Forme différentielle")
