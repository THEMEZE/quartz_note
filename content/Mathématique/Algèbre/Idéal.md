---
title: Idéal
tags:
  - Science
---
En [[Mathématique]]/[Mathématiques](https://fr.wikipedia.org/wiki/Math%C3%A9matiques "Mathématiques"), et plus particulièrement en [[Algèbre]]/[algèbre](https://fr.wikipedia.org/wiki/Alg%C3%A8bre "Algèbre"), un **idéal** est un sous-ensemble remarquable d'un [anneau](https://fr.wikipedia.org/wiki/Anneau_unitaire "Anneau unitaire") : c'est un [sous-groupe](https://fr.wikipedia.org/wiki/Sous-groupe "Sous-groupe") du groupe additif de l'anneau qui est, de plus, [stable](https://fr.wikipedia.org/wiki/Sous-espace_stable "Sous-espace stable") par multiplication par les éléments de l'anneau. À certains égards, les idéaux s'apparentent donc aux [sous-espaces vectoriels](https://fr.wikipedia.org/wiki/Sous-espace_vectoriel "Sous-espace vectoriel") — qui sont des sous-groupes additifs stables par une multiplication [externe](https://fr.wikipedia.org/wiki/Loi_de_composition_externe "Loi de composition externe") ; à d'autres égards, ils se comportent comme les [sous-groupes distingués](https://fr.wikipedia.org/wiki/Sous-groupe_distingu%C3%A9 "Sous-groupe distingué") — ce sont des sous-groupes additifs à partir desquels on peut construire une structure d'[anneau quotient](https://fr.wikipedia.org/wiki/Anneau_quotient "Anneau quotient").

Apparus à la fin du XIXe siècle en [théorie algébrique des nombres](https://fr.wikipedia.org/wiki/Th%C3%A9orie_alg%C3%A9brique_des_nombres "Théorie algébrique des nombres") pour généraliser à des [entiers algébriques](https://fr.wikipedia.org/wiki/Entier_alg%C3%A9brique "Entier algébrique") la [décomposition en facteurs premiers](https://fr.wikipedia.org/wiki/D%C3%A9composition_en_facteurs_premiers "Décomposition en facteurs premiers") des [entiers](https://fr.wikipedia.org/wiki/Entier_relatif "Entier relatif"), les idéaux ont rapidement joué un rôle central en [algèbre](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_g%C3%A9n%C3%A9rale "Algèbre générale") et en [géométrie algébrique](https://fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_alg%C3%A9brique "Géométrie algébrique"), en particulier à la suite des travaux d'[Emmy Noether](https://fr.wikipedia.org/wiki/Emmy_Noether "Emmy Noether") isolant l'importance des [conditions de chaîne](https://fr.wikipedia.org/wiki/Conditions_de_cha%C3%AEne "Conditions de chaîne"). Au-delà de l'algèbre, ils interviennent de façon centrale dans les développements du XXe siècle de certains chapitres d'[analyse fonctionnelle](https://fr.wikipedia.org/wiki/Analyse_fonctionnelle_\(math%C3%A9matiques\) "Analyse fonctionnelle (mathématiques)"), notamment l'étude des [algèbres de Banach](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_de_Banach "Algèbre de Banach") et l'[analyse harmonique commutative](https://fr.wikipedia.org/wiki/Analyse_harmonique_commutative "Analyse harmonique commutative").

En [algèbre commutative](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_commutative "Algèbre commutative"), deux types d'idéaux sont omniprésents : les [idéaux maximaux](https://fr.wikipedia.org/wiki/Id%C3%A9al_maximal "Idéal maximal") et, sans doute encore davantage, les [idéaux premiers](https://fr.wikipedia.org/wiki/Id%C3%A9al_premier "Idéal premier"). Dans l'anneau des entiers relatifs, tant les idéaux maximaux que les idéaux premiers (non nuls) sont les _p_**Z**, où _p_ est un [nombre premier](https://fr.wikipedia.org/wiki/Nombre_premier "Nombre premier") ; dans les [anneaux commutatifs](https://fr.wikipedia.org/wiki/Anneau_commutatif "Anneau commutatif") plus abstraits ces familles d'idéaux généralisent la notion de nombre premier.

En [théorie des anneaux](https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_anneaux "Théorie des anneaux") non commutatifs, il faut prendre garde à l'existence juxtaposée de deux concepts distincts d'idéaux : les **idéaux à gauche** (ou **à droite**), qui sont des [sous-modules](https://fr.wikipedia.org/wiki/Sous-module "Sous-module"), et les **idéaux bilatères**, ceux par lesquels on peut quotienter. Alors que la structure des anneaux non commutatifs les plus généraux peut être extrêmement complexe, on a plus de prise sur ceux vérifiant les conditions de finitude découvertes par [Emmy Noether](https://fr.wikipedia.org/wiki/Emmy_Noether "Emmy Noether") et [Emil Artin](https://fr.wikipedia.org/wiki/Emil_Artin "Emil Artin"), à savoir des [conditions de chaîne](https://fr.wikipedia.org/wiki/Conditions_de_cha%C3%AEne "Conditions de chaîne") sur leurs idéaux à gauche ou à droite.


# Définitions

Deux notions d'idéaux coexistent, qui coïncident dans le cas d'un [anneau commutatif](https://fr.wikipedia.org/wiki/Anneau_commutatif "Anneau commutatif") mais jouent des rôles bien différents sans hypothèse de commutativité de la multiplication.

## Les idéaux comme sous-modules : idéaux à gauche et à droite

Une partie _I_ d'un anneau _A_ est appelée un **idéal à gauche** (respectivement **à droite**) de _A_ lorsque[[1]](https://fr.wikipedia.org/wiki/Id%C3%A9al#cite_note-Bbk98-1) :

- _I_ est un [sous-groupe](https://fr.wikipedia.org/wiki/Sous-groupe "Sous-groupe") additif de _A_.
- Pour tout _a_ de _A_ et tout _x_ de _I_, _ax_ ∈ _I_ (resp. _xa_ ∈ _I_). Autrement dit, on demande à _I_ d'être stable sous multiplication à gauche (resp. à droite) par tout élément de _A_, même ceux qui ne sont pas dans _I_.

En utilisant le langage des [modules](https://fr.wikipedia.org/wiki/Module_sur_un_anneau "Module sur un anneau"), on peut définir plus brièvement[[2]](https://fr.wikipedia.org/wiki/Id%C3%A9al#cite_note-2) un idéal à gauche (resp. à droite) comme un [sous-module](https://fr.wikipedia.org/wiki/Sous-module "Sous-module") pour la structure de _A_-module à gauche (resp. à droite) sur _A_.

On appelle ensuite **idéal bilatère** de _A_ (ou **idéal** tout court lorsqu'il n'y a pas de risque de confusion) toute partie de _A_ qui est simultanément un idéal à gauche et un idéal à droite[[1]](https://fr.wikipedia.org/wiki/Id%C3%A9al#cite_note-Bbk98-1). Lorsque l'anneau est commutatif, ces notions se confondent toutes[[1]](https://fr.wikipedia.org/wiki/Id%C3%A9al#cite_note-Bbk98-1) mais elles jouent des rôles très dissemblables en algèbre non commutative. De fait, bien qu'intervenant occasionnellement en théorie non commutative (ainsi dans la définition des [anneaux simples](https://fr.wikipedia.org/wiki/Anneau_simple "Anneau simple")), les idéaux bilatères sont dans ce contexte difficiles à manipuler, et de ce fait moins omniprésents que les idéaux à gauche ou à droite[[3]](https://fr.wikipedia.org/wiki/Id%C3%A9al#cite_note-3). On peut remarquer[[4]](https://fr.wikipedia.org/wiki/Id%C3%A9al#cite_note-4) que les idéaux bilatères sont les sous-structures pour la structure de _A_-_A_-[bimodule](https://fr.wikipedia.org/wiki/Bimodule "Bimodule") sur _A_.

## Les idéaux comme noyaux : idéaux bilatères et anneaux-quotients

Article détaillé : [Anneau quotient](https://fr.wikipedia.org/wiki/Anneau_quotient "Anneau quotient").

En répétant ce qui vient d'être dit pour se focaliser sur les seuls idéaux bilatères, on peut réécrire explicitement leur définition :

Une partie _I_ d'un anneau _A_ est appelée un **idéal bilatère** de _A_ (ou **idéal** quand on ne craint pas de confusion, notamment en algèbre commutative) lorsque[[5]](https://fr.wikipedia.org/wiki/Id%C3%A9al#cite_note-5) :

- _I_ est un [sous-groupe](https://fr.wikipedia.org/wiki/Sous-groupe "Sous-groupe") additif de _A_ ;
- Pour tout _a_ de _A_ et tout _x_ de _I_, _ax_ ∈ _I_ et _xa_ ∈ _I_. Autrement dit, on demande à _I_ d'être stable sous multiplication par tout élément de _A_ (que ce soit à gauche ou à droite), même ceux qui ne sont pas dans _I_.

Un intérêt spécifique aux idéaux bilatères vient de ce qu'il est possible d'en donner une autre description, qui les lie au concept d'[anneau quotient](https://fr.wikipedia.org/wiki/Anneau_quotient "Anneau quotient"). Étant donné un idéal bilatère _I_ d'un anneau _A_, le [groupe quotient](https://fr.wikipedia.org/wiki/Groupe_quotient "Groupe quotient") _A_ / _I_ peut être muni d'une structure d'anneau, pour laquelle la [projection canonique](https://fr.wikipedia.org/wiki/Projection_canonique_sur_un_groupe_quotient "Projection canonique sur un groupe quotient") est un [morphisme d'anneaux](https://fr.wikipedia.org/wiki/Morphisme_d%27anneaux "Morphisme d'anneaux"), de [noyau](https://fr.wikipedia.org/wiki/Noyau_\(alg%C3%A8bre\) "Noyau (algèbre)") _I_. Réciproquement, tout noyau est un idéal bilatère. On peut synthétiser ces informations par l'énoncé suivant[[6]](https://fr.wikipedia.org/wiki/Id%C3%A9al#cite_note-6) :

> Un sous-ensemble _I_ d'un anneau _A_ est un idéal (bilatère) si et seulement s'il existe un morphisme d'anneaux dont _A_ est l'anneau de départ et dont le [noyau](https://fr.wikipedia.org/wiki/Noyau_\(alg%C3%A8bre\) "Noyau (algèbre)") est _I_.

Certaines propriétés des idéaux bilatères peuvent être lues à travers la structure de l'anneau quotient[[7]](https://fr.wikipedia.org/wiki/Id%C3%A9al#cite_note-7) : ainsi dans un [anneau commutatif](https://fr.wikipedia.org/wiki/Anneau_commutatif "Anneau commutatif"), un idéal bilatère est [maximal](https://fr.wikipedia.org/wiki/Id%C3%A9al_maximal "Idéal maximal") si et seulement si l'anneau quotient est un [corps](https://fr.wikipedia.org/wiki/Corps_commutatif "Corps commutatif").

# Exemples d'idéaux

- Si _A_ est un anneau, {0} et _A_ sont des idéaux de _A_, appelés **[idéaux triviaux](https://fr.wikipedia.org/wiki/Id%C3%A9aux_triviaux "Idéaux triviaux")**. On appelle **idéal propre** un idéal différent de _A_.