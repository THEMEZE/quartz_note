---
title: Dynamique des systèmes matériels fermés
tags:
  - Agrégation
  - Physique
---
---
[^1]: Physique pour l'agrégation Jules Fillette - Julien Froustey - Hugo Roussille
[^2]: Physique Spé. PC*, PC Cours et exercices d'application Stéphane OLIVIER, Hubert GIÉ, Jean-Pierre SARMANT
[^3]: Formulaire MATHS, PHYSIQUE, CHIMIE, SII (2e édition), MPSI-MP , Bertrand Hauchecorne
[^4]: Formulaire MATHS, PHYSIQUE, CHIMIE, SII (3e édition), PCSI-MPSI/PTSI-PSI , Bertrand Beaufils

---


Système matériel $\mathscr S$  dans un référentiel galiléen $\mathscr R$. Nous avons déjà rencontrer les composant $\vec{\Omega}_{\mathscr S / \mathscr R}$ et $\vec{v}_{\mathscr S / \mathscr R}(A)$ du torseur cinématique, qui satisfont bien à la relation de Varignon, d'après la formule de composition des vitesse (cf  [[Physique/Mécanique du Solide/M1 Rappels et compléments#1. Vecteur-Rotation | 1. Vecteur-Rotation]],  [^1] p 120 , [^2] p 150 , [^3] p 177, [^4] p 199 )
$$
\overrightarrow{v}_{\mathscr S/ \mathscr R} (B) = \overrightarrow{v}_{\mathscr S/ \mathscr R}(A) +  \overrightarrow{BA} \wedge  \overrightarrow{\Omega}_{\mathscr S / \mathscr R},
$$

>[!tip]+ **Torseur cinématique**.
>
>Pour un solide $\mathscr S$ indéformable, le vecteur de rotation instantanée $\vec{\Omega}_{\mathscr S / \mathscr R}$ et la vitesse en un point définissent le $\vec{v}_{\mathscr S / \mathscr R}(A)$ définissent le **torseur cinématique** du solide :
>$$
>\mathscr V_{\mathscr S / \mathscr R}(A) =
>\left \{
>\begin{array}{c}
>\vec{\Omega}_{\mathscr S / \mathscr R} \\
>\vec{v}_{\mathscr S / \mathscr R}(A)
>\end{array}
>\right \},
>$$
>et ce en vertu de la loi de compositions des vitesses qui constituent, pour ce torseur, la relation de Varignon.

et d'après la formule de composition des moment cinétique
$$
\overrightarrow{L}_{\mathscr S/ \mathscr R} (B) = \overrightarrow{L}_{\mathscr S/ \mathscr R}(A) +  \overrightarrow{BA} \wedge  \overrightarrow{P}_{\mathscr S / \mathscr R},
$$

>[!tip]+ **Torseur cinétique**.
>
>Le **torseur cinétique** d'un solide $\mathscr S$ indéformable au point $A$ est constitué de la résultante cinétique $\vec P_{\mathscr S / \mathscr R}$ et du moment cinétique $\vec L_{\mathscr S / \mathscr R}(A)$ : 
>$$
>\mathscr C_{\mathscr S / \mathscr R}(A) =
>\left \{
>\begin{array}{c}
>\vec{P}_{\mathscr S / \mathscr R} \\
>\vec{L}_{\mathscr S / \mathscr R}(A)
>\end{array}
>\right \}.
>$$

Si on définie la **quantité d'accélération**, qui joue un rôle de résultante (cf  [[Physique/Mécanique du Solide/M1 Rappels et compléments#$ bullet$ Moment dynamique| Moment dynamique]],  [^1] p 120 , [^2] p 164 , [^3] p 177, [^4] p 199 ):
$$
\vec S_{\mathscr S / \mathscr R} = \iiint_{M \in \mathscr S} \vec{a}_{\mathscr S / \mathscr R}(M)\, dm(M),
$$

>[!tip]+ **Torseur dynamique**
>
>Le torseur dynamique d'un solide $\mathscr S$ indéformable s'exprime à partir de la quantité d'accélération $\vec S_{\mathscr S / \mathscr R}$ et du moment dynamique $\vec D_{\mathscr S / \mathscr R}(A)$ :
>$$
>\mathscr D_{\mathscr S / \mathscr R}(A) =
>\left \{
>\begin{array}{c}
>\vec{S}_{\mathscr S / \mathscr R} \\
>\vec{D}_{\mathscr S / \mathscr R}(A)
>\end{array}
>\right \}.
>$$

>[!tip]+ **Torseur**
>
>Un torseur $\mathscr T$ associé à un solide $\mathscr S$ dans le référentiel $\mathscr R$, exprimé au point $A$, est généralement noté
>$$
>\mathscr T_{\mathscr S/ \mathscr R}(A) =
>\left \{
>\begin{array}{c}
>\vec{R}_{\mathscr S / \mathscr R} \\
>\vec{\mathscr M}_{\mathscr S / \mathscr R}(A)
>\end{array}
>\right \},
>$$
>avec la résultante 
>$$
>\vec{R}_{\mathscr S / \mathscr R} \doteq \iiint_{M \in \mathscr S} d \vec R_{\mathscr S / \mathscr R}(M),
>$$
>et le moment 
>$$
>\vec{\mathscr M}_{\mathscr S / \mathscr R}(A) \doteq \iiint_{M \in \mathscr S} \overbrace{\overrightarrow{AM} \wedge d \vec R_{\mathscr S / \mathscr R}(M) }^{\displaystyle d \vec{\mathscr M}_{\mathscr S / \mathscr R}(A;M)},
>$$
>sujet à la relation de Varignon
>$$
>\vec{\mathscr M}_{\mathscr S / \mathscr R}(B) =  \vec{\mathscr M}_{\mathscr S / \mathscr R}(A) + \overrightarrow{BA} \wedge \vec{R}_{\mathscr S / \mathscr R},
>$$
>on retiendra **"BABAR"**.


# I. Torseur des forces 
## a. Premières définitions

### $\bullet$ Systèmes des forces réparties
([^2] p 181)
Les actions subis par un élément infinitésimal d'un système matériel $\mathscr S$, centré en $M$ et de masse $dm(M)$, sont décrites par une force infinitésimale $d \vec F_{\mathscr S / \mathscr R}(M)$

### $\bullet$ Résultante et moment d'un système de force

i) la **résultante des forces** comme la somme des forces élémentaires :
$$
\vec{F}_{\mathscr S / \mathscr R} \doteq \iiint_{M \in \mathscr S} d \vec F_{\mathscr S / \mathscr R}(M)
$$
ii) le **moment** en un point $A$ quelconque comme la somme des moments en $A$ des foeces élémentaires :
$$
\vec{\mathfrak{M}}_{\mathscr S / \mathscr R}(A) \doteq \iiint_{M \in \mathscr S} \overbrace{\overrightarrow{AM} \wedge d \vec F_{\mathscr S / \mathscr R}(M)}^{\displaystyle d \vec{\mathfrak{M}}_{\mathscr S / \mathscr R}(A;M)}
$$

### $\bullet$ Torseur des forces

$$
\vec{\mathfrak{M}}_{\mathscr S / \mathscr R}(B) = \vec{\mathfrak{M}}_{\mathscr S / \mathscr R}(A) + \overrightarrow{BA} \wedge \vec{F}_{\mathscr S / \mathscr R}
$$

# II. Théorèmes généraux de la dynamique des systèmes fermés

## a. Principe fondamental de la dynamique des systèmes fermés

### $\bullet$ Postulat

1. les forces d'interaction sont invariantes par tout changement de référentiel ;
2. il existe des référentiels galiléens; ces référentiels sont en translation rectiligne uniforme les un par rapport aux autres ;
3. pour tout point matériel mobile dans un référentiel galiléen et soumis a des forces de résultante $\vec{F}_{\mathscr S / \mathscr R}$, la loi de $\mathsf{Newton}$ s'écrit :
$$
m \, \vec{a}_{\mathscr S / \mathscr R}(M) = \vec F_{\mathscr S / \mathscr R},
$$
4. principe des actions réciproques : soit $\mathscr S_1$ et $\mathscr S_2$ deux systèmes disjoints ; alors le torseur des actions de $\mathscr S_1$ sur $\mathscr S_2$ est l'opposé du torseur des actions de  $\mathscr S_2$ sur $\mathscr S_1$ :
$$
\vec F_{2 \to 1 ; \mathscr S / \mathscr R} = - \vec F_{1 \to 2 ; \mathscr S / \mathscr R} \qquad \& \qquad \vec{\mathfrak{M}}_{2 \to 1 ; \mathscr S / \mathscr R}(A) = - \, \vec{\mathfrak{M}}_{1 \to 2 ; \mathscr S / \mathscr R}(A) \quad  \forall A
$$

## b. Théorème de la résultante dynamique 

### $\bullet$ Théorème de la résultante dynamique $(\mathsf{TRD})$

Soit un système fermé $\mathscr S$ en mouvement par rapport à un référentiel *galiléen* $\mathscr R$ , alors :
$$
m \, \vec{a}_{\mathscr S / \mathscr R}(M) = \vec F_{\mathscr S / \mathscr R}^{\text{ext}} \qquad \& \qquad \left . \frac{d \vec P_{\mathscr S / \mathscr R}}{dt} \right )_{\mathscr R} = \vec F_{\mathscr S / \mathscr R}^{\text{ext}},
$$
où $\vec F_{\mathscr S / \mathscr R}^{\text{ext}}$ est la résultante des forces extérieures.

$$
dm(M)\, \vec a_{\mathscr S / \mathscr R}(M) = d \vec F_{\text{ext} \to M ; \mathscr S / \mathscr R} + \iiint_{M' \in \mathscr S} d \vec F_{M' \to M ; \mathscr S / \mathscr R},
$$
avec $d \vec F_{M' \to M ; \mathscr S / \mathscr R}$ antisymétique.
$$
\iiint_{M' \in \mathscr S} dm(M)\, \vec a_{\mathscr S / \mathscr R}(M) = \underbrace{\iiint_{M' \in \mathscr S} d \vec F_{\text{ext} \to M ; \mathscr S / \mathscr R}}_{\displaystyle \vec F_{\mathscr S / \mathscr R}^{\text{ext}}} + \iiint_{M' \in \mathscr S}\iiint_{M' \in \mathscr S} d \vec F_{M' \to M ; \mathscr S / \mathscr R} = \vec F_{\mathscr S / \mathscr R}^{\text{ext}} 
 
+ \frac{1}{2} \underbrace{\iiint\!\!\!\iiint_{M , M' \in \mathscr S} \overbrace{\left (d \vec F_{M' \to M ; \mathscr S / \mathscr R} + d \vec F_{M \to M' ; \mathscr S / \mathscr R} \right)}^{\displaystyle  \vec 0}}_{ \displaystyle \vec 0 }
$$

## c. Les différents théorèmes du moment cinétique

### $\bullet$ Théorème du moment dynamique $(\mathsf{TMD})$
Soit un système *fermé* $\mathscr S$ en mouvement par rapport à un référentiel galiléen $\mathscr R$, soit $A$ un point quelconque, alors le moment dynamique en $A$ est égal au moment des forces extérieurs en $A$ :
$$
\vec D_{\mathscr S / \mathscr R}(A) = \vec{\mathfrak{M}}_{\mathscr S / \mathscr R}^{\text{ext}}(A).
$$
En effet 
$$
\vec D_{\mathscr S / \mathscr R}(A) = \iiint_{M \in \mathscr S}  \overrightarrow{AM} \wedge \overbrace{\left (d \vec F_{\text{ext} \to M ; \mathscr S / \mathscr R} + \iiint_{M' \in \mathscr S} d \vec F_{M' \to M ; \mathscr S / \mathscr R} \right)}^{\displaystyle dm(M)\,\vec a_{\mathscr S / \mathscr R}(M)}
=
\underbrace{\iiint_{M \in \mathscr S} \overrightarrow{AM} \wedge d \vec F_{\text{ext} \to M ; \mathscr S / \mathscr R}}_{\displaystyle \vec{\mathfrak{M}}_{\mathscr S / \mathscr R}^{\text{ext}}(A)}
+
\frac{1}{2}
\underbrace{\iiint\!\!\!\iiint_{M , M' \in \mathscr S} \overbrace{\left (\overrightarrow{AM} \wedge d \vec F_{M' \to M ; \mathscr S / \mathscr R} + \overrightarrow{AM'} \wedge \vec F_{M \to M' ; \mathscr S / \mathscr R} \right)}^{ \displaystyle d \vec{\mathfrak{M}}_{M' \to M ; \mathscr S / \mathscr R}(A) + d \vec{\mathfrak{M}}_{M \to M' ; \mathscr S / \mathscr R}(A)  = \vec 0}}_{\displaystyle  \vec 0 }.
$$

### $\bullet$ Théorème du moment cinétique barycentrique $(\mathsf{TMC^\ast})$

Soit un système *fermé* $\mathscr S$ en mouvement par rapport à un référentiel *galiléen* $\mathscr R$, alors la dérivée du moment cinétique barycentrique est égale au moment des forces extérieures eu centre d'inertie $G$ (cf [[Physique/Mécanique du Solide/M1 Rappels et compléments#$ bullet$ Théorème de Koening |Théorème de Koening  ]] et [[Physique/Mécanique du Solide/M1 Rappels et compléments#$ bullet$ Moment dynamique|Moment dynamique ]] )
$$
\left. \frac{d \vec L_{\mathscr S / \mathscr R^\ast}}{dt} \right )_{\mathscr R}  = \vec{\mathfrak{M}}_{\mathscr S / \mathscr R}^{\text{ext}}(G) = \vec{\mathfrak{M}}_{\mathscr S / \mathscr R}^{\text{ext}}(A) + \overbrace{\overrightarrow{AG} \wedge ( - m \, \vec{a}_{\mathscr S / \mathscr R}(G))}^{ \displaystyle \vec{\mathfrak{M}}_{\mathscr R^\ast / \mathscr R}^{\text{ie}}(A)}
$$

### $\bullet$ Théorème du moment cinétique en un point fixe $(\mathsf{TMC})$

Soit un système *fermé* $\mathscr S$ en mouvement par rapport à un référentiel *galiléen* $\mathscr R$. Soit $A$ un point f*fixe* dans $\mathscr R$. Alors la dérivée du moment cinétique en $A$ est égale au moment des forces *extérieures* au point $A$ (cf [[Physique/Mécanique du Solide/M1 Rappels et compléments#$ bullet$ Moment dynamique|Moment dynamique ]] )
$$
\left. \frac{d \vec L_{\mathscr S / \mathscr R}(A)}{dt} \right )_{\mathscr R}  = \vec{\mathfrak{M}}_{\mathscr S / \mathscr R}^{\text{ext}}(A).
$$

### $\bullet$ Torseur d'action, Théorème de la résultante dynamique $(\mathsf{TRD})$ et Théorème du moment dynamique $(\mathsf{TMD})$

>[!tip]+ **Torseur d'action**
>
>Le **torseur des actions** d'un solide $\mathscr S$ indéformable s'exprime à partir de la résultante des force $\vec F_{\mathscr S / \mathscr R}$ et du moment $\vec {\mathfrak{M}}_{\mathscr S / \mathscr R}(A)$ :
>$$
>\mathscr A_{\mathscr S / \mathscr R}(A) =
>\left \{
>\begin{array}{c}
>\vec{F}_{\mathscr S / \mathscr R} \\
>\vec{\mathfrak{M}}_{\mathscr S / \mathscr R}(A)
>\end{array}
>\right \}.
>$$

et 
$$
\mathscr D_{\mathscr S / \mathscr R}(A) = \mathscr A_{\mathscr S / \mathscr R}(A)
$$
et si $\mathscr R$ est galiléen 
$$
\mathscr D_{\mathscr S / \mathscr R}(A) = \mathscr A_{\mathscr S / \mathscr R}^{\text{ext}}(A).
$$