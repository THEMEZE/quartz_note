---
title: "Exercice 2 — Couplage de deux oscillateurs harmoniques dissymétriques"
tags:
  - td
  - chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/index|⬅ Retour]] · <a href="/pdfs/td4_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 2. Couplage de deux oscillateurs harmoniques dissymétriques

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 50 min · Type : Application / Problème guidé*

On considère deux oscillateurs mécaniques dissymétriques. Les masses sont identiques et égales à $m$, mais les ressorts sont de raideurs différentes $k$, $2k$, $4k$ de gauche à droite. À l'équilibre, ceux-ci sont tous à leur longueur à vide et possèdent la même longueur $d$. Les masses sont assujetties à se déplacer le long de l'axe des $x$ et on note $x_1(t)$ et $x_2(t)$ leurs positions en mouvement comptées depuis leur position d'équilibre respective.

> [!question]+ 🎣 Accroche
> **Et si les deux oscillateurs ne sont pas identiques ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *Dans l'exercice 1, les deux pendules étaient identiques et la somme et la différence de leurs écarts suffisaient. **Que devient cette idée si l'un des deux ressorts est quatre fois plus raide que l'autre ?** Les deux masses vont-elles encore bouger exactement en phase ou en opposition de phase dans un mode ?*
>
> **Idée clé : sans symétrie, les modes ont des amplitudes inégales, et il faut diagonaliser.** La matrice de raideur $K=k\begin{pmatrix}3&-2\\-2&6\end{pmatrix}$ a pour valeurs propres $2k$ et $7k$ et pour vecteurs propres $(2,1)$ et $(1,-2)$ : les deux masses sont toujours en phase ou en opposition de phase dans un mode, mais avec des amplitudes dans le rapport $2:1$.


> [!abstract]+ 📚 Prérequis
> **Allongement algébrique et force d'un ressort**
>
> L'allongement algébrique $e=\ell_s-\ell_0$ fixe le signe de la force : un ressort étiré ($e>0$) tire chacune de ses extrémités vers son centre.
>
> **Résolution de l'exercice 1**
>
> Savoir découpler deux oscillateurs identiques par somme et différence et connaître la condition (diagonale égale, couplage réciproque) pour que cela fonctionne.
>
> **Valeurs et vecteurs propres d'une matrice $2\times2$ symétrique**
>
> Équation caractéristique $\lambda^2-\mathrm{tr}(A)\lambda+\det A=0$ ; vecteurs propres d'une matrice symétrique orthogonaux.
>
> **Notation complexe**
>
> $x_j=\underline A_je^{i\omega t}$, $\ddot x_j=-\omega^2x_j$.


> [!info]+ 🎯 Objectifs
> **Mettre en équation un système de ressorts sans erreur de signe**
>
> Savoir calculer les allongements algébriques de trois ressorts, justifier le sens de chaque force, et vérifier les signes par un raisonnement par l'absurde.
>
> **Reconnaître l'échec d'un découplage et savoir passer à la méthode générale**
>
> Savoir expliquer pourquoi $S$ et $D$ ne découplent pas ici, chercher des combinaisons adaptées $x_1+\beta x_2$, puis retrouver le même résultat par diagonalisation de la matrice de raideur.
>
> **Interpréter des modes dissymétriques**
>
> Savoir décrire les deux modes (amplitudes inégales), écrire la solution générale, décomposer des conditions initiales sur les modes et discuter à quelles conditions des battements existent.


> [!note]- 🧮 Outils mathématiques
> **Équation caractéristique d'une matrice $2\times2$**
>
> $\lambda^2-\mathrm{tr}(A)\,\lambda+\det A=0$. Ici $\lambda^2-9\lambda+14=(\lambda-2)(\lambda-7)$.
>
> **Vecteurs propres et orthogonalité**
>
> Pour $\lambda=2$ : $(3-2)A_1-2A_2=0$, donc $A_1=2A_2$. Pour $\lambda=7$ : $-4A_1-2A_2=0$, donc $A_2=-2A_1$. Produit scalaire $(2,1)\cdot(1,-2)=0$.
>
> **Décomposition sur une base orthogonale**
>
> $X_0=c'u'+c''u''$ avec $c'=\dfrac{X_0\cdot u'}{u'\cdot u'}$, $c''=\dfrac{X_0\cdot u''}{u''\cdot u''}$.
>
> **Angle de mélange**
>
> Pour $\begin{pmatrix}a&b\\b&c\end{pmatrix}$ : $\tan2\theta=\dfrac{2b}{a-c}$. Ici $\tan2\theta=\dfrac43$, $\theta=\arctan\dfrac12\simeq26{,}6^\circ$.
>
> **Produit de deux cosinus**
>
> $\cos p+\cos q=2\cos\dfrac{p+q}2\cos\dfrac{p-q}2$ ; permet de voir quand une somme de deux sinusoïdes s'écrit comme un produit.


**q1.** Quels sont les allongements des trois ressorts ?

> [!tip]- 💡 Coup de pouce
> **Longueur instantanée moins longueur à vide**
>
> Repérez chaque extrémité de ressort par son abscisse. L'allongement est la longueur instantanée moins la longueur à vide $d$.


> [!success]- ✅ Correction
> **Allongements**
>
> Ressort de gauche (raideur $k$) : $x_1$ ; ressort central ($2k$) : $x_2-x_1$ ; ressort de droite ($4k$) : $-x_2$.


> [!example]- 📝 Solution détaillée
> **Repérage**
>
> Plaçons l'origine au mur de gauche, le mur de droite étant en $x=3d$. À l'équilibre, la masse $m_1$ est en $d$ et la masse $m_2$ en $2d$. En mouvement, leurs abscisses sont $d+x_1$ et $2d+x_2$ ($x_i$ algébrique, positif vers la droite).
>
> **Longueurs et allongements**
>
> - Ressort de gauche : longueur $\ell_a=(d+x_1)-0=d+x_1$, allongement $e_a=\ell_a-d=x_1$.
> - Ressort central : longueur $\ell_b=(2d+x_2)-(d+x_1)=d+x_2-x_1$, allongement $e_b=x_2-x_1$.
> - Ressort de droite : longueur $\ell_c=3d-(2d+x_2)=d-x_2$, allongement $e_c=-x_2$.
>
>
> **Signification des signes.** Si $x_1>0$, la masse 1 s'éloigne du mur de gauche : le ressort de gauche est étiré ($e_a>0$). Si $x_2>0$, la masse 2 se rapproche du mur de droite : le ressort de droite est comprimé ($e_c<0$). Le ressort central est étiré si $x_2>x_1$ (les masses s'écartent).


**q2.** Établir, en utilisant le raisonnement par l'absurde, le système d'équations différentielles couplées que vérifient les deux variables du mouvement $x_1(t)$ et $x_2(t)$ lors des oscillations libres. Le changement de variables $S=x_1+x_2$ et $D=x_1-x_2$ est-il adapté ici ? Le calcul n'est pas demandé.

> [!tip]- 💡 Coup de pouce
> **Règle des forces**
>
> Un ressort d'allongement algébrique $e$ et de raideur $K$ exerce $+Ke$ (vers la droite) sur son extrémité de gauche et $-Ke$ (vers la gauche) sur son extrémité de droite. Appliquez cette règle à chaque masse.
>
> **Raisonnement par l'absurde**
>
> Supposez le signe contraire pour l'une des forces. Prenez par exemple $x_2>x_1$ : que ferait alors le ressort central ? Est-ce compatible avec un système stable ?
>
> **Adapté ou non ?**
>
> Comparez les coefficients de $x_1$ dans la première équation et de $x_2$ dans la seconde : sont-ils égaux ? Rappelez-vous la condition trouvée à l'exercice 1.


> [!success]- ✅ Correction
> **Système**
>
> $$m\ddot x_1=-kx_1+2k(x_2-x_1),\qquad m\ddot x_2=-2k(x_2-x_1)-4kx_2,$$
> soit, avec $\omega_0^2=k/m$ : $\ddot x_1+3\omega_0^2x_1-2\omega_0^2x_2=0$ et $\ddot x_2+6\omega_0^2x_2-2\omega_0^2x_1=0$. Le changement $S,D$ n'est pas adapté.


> [!example]- 📝 Solution détaillée
> **Forces sur chaque masse (règle des extrémités)**
>
> - Masse 1 : elle est l'extrémité *droite* du ressort de gauche, force $-k\,e_a=-kx_1$ ; elle est l'extrémité *gauche* du ressort central, force $+2k\,e_b=+2k(x_2-x_1)$.
> - Masse 2 : extrémité *droite* du ressort central, force $-2k\,e_b=-2k(x_2-x_1)$ ; extrémité *gauche* du ressort de droite, force $+4k\,e_c=-4kx_2$.
>
>
> Le mouvement est horizontal : la pesanteur et la réaction du support se compensent ; le principe fondamental projeté sur $\vec e_x$ est exact (les ressorts sont rectilignes) : ici *aucune approximation n'est nécessaire*, le système est linéaire exactement. **Équations :**
> $$m\ddot x_1=-kx_1+2k(x_2-x_1)=-3kx_1+2kx_2,\qquad m\ddot x_2=-2k(x_2-x_1)-4kx_2=2kx_1-6kx_2.$$
>
> **Contrôle des signes par l'absurde**
>
> Supposons, par l'absurde, que le ressort central exerce sur $m_1$ la force $-2k(x_2-x_1)$ (et donc $+2k(x_2-x_1)$ sur $m_2$). Pour $x_2>x_1>0$, cette force pousse $m_1$ vers la gauche et $m_2$ vers la droite : la distance entre les masses *augmente*, donc $x_2-x_1$ augmente encore, et ainsi de suite : le mouvement diverge exponentiellement et l'énergie cinétique croît sans borne alors que le système est conservatif et en équilibre stable. C'est absurde : un ressort étiré rapproche ses extrémités. Le signe retenu est le bon. De même, un signe opposé pour la force du ressort de gauche ($+kx_1$) éloignerait $m_1$ de $x=0$.
>
> **Forme canonique**
>
> Avec $\omega_0^2=k/m$ :
> $$\boxed{\ddot x_1+3\omega_0^2x_1-2\omega_0^2x_2=0},\qquad\boxed{\ddot x_2+6\omega_0^2x_2-2\omega_0^2x_1=0}.$$
> Le corrigé de l'établissement écrit « $\omega_0^2=\sqrt{k/m}$ » : c'est $\omega_0^2=k/m$.
>
> **Le changement de variables $S$, $D$ est-il adapté ?**
>
> La condition établie à l'exercice 1 est : coefficients diagonaux égaux et couplage réciproque. Ici les diagonales valent $3\omega_0^2$ et $6\omega_0^2$ : elles diffèrent, car la masse 1 est reliée à un ressort $k$ et la masse 2 à un ressort $4k$. Le système n'est pas invariant par échange des deux masses. **La réponse est non.**
>
> Pour s'en convaincre, *sans que le calcul soit demandé*, on obtient en additionnant et en soustrayant et en posant $x_1=(S+D)/2$, $x_2=(S-D)/2$ :
> $$\ddot S+\omega_0^2\Big(\tfrac52S-\tfrac32D\Big)=0,\qquad\ddot D+\omega_0^2\Big(-\tfrac32S+\tfrac{13}2D\Big)=0.$$
> Les équations restent couplées : on a seulement remplacé un couplage par un autre. (Les équations en $S$ et $D$ du corrigé de l'établissement ne sont pas correctes : coefficients $\omega_0^2/2$ au lieu de $5\omega_0^2/2$ dans la première, et rôles de $S$ et $D$ intervertis dans la seconde.) L'idée reste valable sous une forme généralisée : voir la question suivante.


**q3.** Chercher les modes propres et écrire l'expression de la solution générale du régime libre. Quels battements est-il possible d'obtenir et à quelles conditions ?

> [!tip]- 💡 Coup de pouce
> **Chercher une solution harmonique**
>
> Posez $x_j=A_je^{i\omega t}$ et reportez : vous obtenez un système homogène $2\times2$ sur $A_1,A_2$. Quand admet-il une solution non nulle ?
>
> **Deux méthodes**
>
> (a) *Physicien* : cherchez une combinaison $c=x_1+\beta x_2$ telle que $\ddot c=-\omega^2c$. (b) *Mathématicien* : écrivez $\ddot X=-\omega_0^2\begin{pmatrix}3&-2\\-2&6\end{pmatrix}X$ et diagonalisez.
>
> **Battements**
>
> Une somme de deux cosinus se factorise en produit. Quelles relations entre amplitudes l'autorisent ? Quelle condition sur les pulsations donne une enveloppe lente ?


> [!success]- ✅ Correction
> **Modes propres**
>
> $\omega'^2=2\omega_0^2$, mode $A_1=2A_2$ (en phase) ; $\omega''^2=7\omega_0^2$, mode $A_2=-2A_1$ (opposition de phase).
>
> **Solution générale**
>
> $$x_1=A'\cos(\omega't+\varphi')+A''\cos(\omega''t+\varphi''),\qquad x_2=\frac{A'}2\cos(\omega't+\varphi')-2A''\cos(\omega''t+\varphi'').$$
>
> **Battements**
>
> Possibles sur $x_1$ seule si $A'=\pm A''$, sur $x_2$ seule si $A'=\pm4A''$, jamais sur les deux ; mais $\omega''/\omega'=\sqrt{7/2}\simeq1{,}87$ : pas d'enveloppe lente, donc pas de battement au sens usuel.


> [!example]- 📝 Solution détaillée
> **Système sur les amplitudes**
>
> Avec $x_j=\underline A_je^{i\omega t}$ : $(3\omega_0^2-\omega^2)\underline A_1-2\omega_0^2\underline A_2=0$ et $-2\omega_0^2\underline A_1+(6\omega_0^2-\omega^2)\underline A_2=0$. La solution $\underline A_1=\underline A_2=0$ est l'équilibre, sans intérêt. Une solution non nulle exige $\det=0$.
>
> **Méthode du mathématicien : déterminant et vecteurs propres**
>
> Posons $\lambda=\omega^2/\omega_0^2$ :
> $$\det\begin{pmatrix}3-\lambda&-2\\-2&6-\lambda\end{pmatrix}=(3-\lambda)(6-\lambda)-4=\lambda^2-9\lambda+14=(\lambda-2)(\lambda-7).$$
> Donc $\omega'^2=2\omega_0^2$ et $\omega''^2=7\omega_0^2$ ; contrôle : $\mathrm{tr}=9=2+7$, $\det=14=2\times7$.
>
> **Vecteurs propres.** $\lambda=2$ : $(3-2)A_1-2A_2=0$, donc $A_1=2A_2$, vecteur $u'=(2,1)$. $\lambda=7$ : $(3-7)A_1-2A_2=0$, donc $A_2=-2A_1$, vecteur $u''=(1,-2)$. Ils sont orthogonaux : $u'\cdot u''=2-2=0$ (matrice symétrique, $M=mI$).
>
> **Méthode du physicien : combinaisons qui se referment**
>
> Cherchons $c=x_1+\beta x_2$ avec $\ddot c=-\omega^2c$. On calcule $\ddot c=-\omega_0^2\big[(3-2\beta)x_1+(6\beta-2)x_2\big]$. Pour que ce soit proportionnel à $c$, il faut $\dfrac{6\beta-2}{3-2\beta}=\beta$, soit $2\beta^2+3\beta-2=0$, de racines $\beta=\tfrac12$ et $\beta=-2$. Les combinaisons sont donc
> $$q'=x_1+\tfrac12x_2\ \propto\ 2x_1+x_2:\ \ddot q'=-2\omega_0^2q',\qquad q''=x_1-2x_2:\ \ddot q''=-7\omega_0^2q''.$$
> (Vérification : $2\ddot x_1+\ddot x_2=-\omega_0^2(4x_1+2x_2)$ et $\ddot x_1-2\ddot x_2=-7\omega_0^2(x_1-2x_2)$.) Dans le cas symétrique de l'exercice 1 la même équation donne $\beta=\pm1$, c'est-à-dire $S$ et $D$ : **$S$ et $D$ étaient le cas particulier $\beta=\pm1$**. Ici les bons coefficients sont $\tfrac12$ et $-2$ ; leur produit vaut $-1$, ce qui traduit l'orthogonalité des modes. On retrouve exactement les valeurs propres, sans le dire.
>
> **Angle de mélange.** Les axes propres sont tournés de $\theta=\arctan\tfrac12\simeq26{,}6^\circ$ par rapport aux axes $(x_1,x_2)$, avec $\tan2\theta=\dfrac{2b}{a-c}=\dfrac43$ (en prenant $a=3$, $c=6$, $b=-2$). Le cas symétrique $a=c$ donnerait $\theta=45^\circ$.
>
> **Description des modes**
>
> - **Mode bas** $\omega'=\sqrt2\,\omega_0$, $(x_1,x_2)\propto(2,1)$ : les masses vont dans le même sens ; la masse 1 (côté du ressort mou $k$) a une amplitude double de celle de la masse 2 (côté du ressort raide $4k$, qui la retient). Allongements pour $A_2=A$ : $x_1=2A$, $x_2-x_1=-A$, $-x_2=-A$ : le ressort central est faiblement déformé, d'où la pulsation basse. Pas de nœud.
> - **Mode haut** $\omega''=\sqrt7\,\omega_0$, $(x_1,x_2)\propto(1,-2)$ : les masses vont en sens opposés ; la masse 2 a l'amplitude double ; le ressort central est fortement déformé ($x_2-x_1=-3A$), d'où la pulsation élevée. Un nœud entre les masses.
>
>
> **Vérification énergétique (Rayleigh).** Mode bas avec $A_2=A$ : $E_{p,\max}=\tfrac12\big[k(2A)^2+2kA^2+4kA^2\big]=5kA^2$ et $E_{c,\max}/\omega^2=\tfrac12m(4+1)A^2=\tfrac52mA^2$, donc $\omega^2=2k/m$. Mode haut avec $A_1=A$, $A_2=-2A$ : $E_{p,\max}=\tfrac12\big[kA^2+2k(3A)^2+4k(2A)^2\big]=\tfrac{35}2kA^2$ et $E_{c,\max}/\omega^2=\tfrac12m(1+4)A^2=\tfrac52mA^2$, donc $\omega^2=7k/m$.
>
> **Solution générale et conditions initiales**
>
> Superposition des modes :
> $$x_1(t)=A'\cos(\omega't+\varphi')+A''\cos(\omega''t+\varphi''),\qquad x_2(t)=\frac{A'}2\cos(\omega't+\varphi')-2A''\cos(\omega''t+\varphi'').$$
> Les quatre constantes $A',A'',\varphi',\varphi''$ sont fixées par $x_1(0),x_2(0),\dot x_1(0),\dot x_2(0)$. Grâce à l'orthogonalité, on les trouve sans résoudre un système $4\times4$ : par exemple les composantes initiales sur les modes sont $c'=\dfrac{2x_1(0)+x_2(0)}5$ et $c''=\dfrac{x_1(0)-2x_2(0)}5$ (projection sur $u'$ et $u''$ de normes carrées $5$), et $A'=2c'$ (avec la vitesse nulle), $A''=c''$. Excitation sélective d'un mode : choisir les conditions initiales proportionnelles à $u'$ (ou $u''$).
>
> **Quels battements et à quelles conditions ?**
>
> Une somme de deux cosinus se factorise en produit si leurs amplitudes sont égales en module : pour $x_1$, $A'=\pm A''$ ; pour $x_2$, $\tfrac{A'}2=\pm2A''$, soit $A'=\pm4A''$. Ces deux conditions sont incompatibles (sauf mouvement nul) : *on ne peut pas avoir d'enveloppe annulée sur les deux masses à la fois*, et l'énergie ne peut pas être transférée complètement d'une masse à l'autre.
>
> **Condition physique supplémentaire.** Un battement est une modulation *lente* de l'amplitude, ce qui demande $|\omega''-\omega'|\ll\omega'+\omega''$. Ici $\omega''/\omega'=\sqrt{7/2}\simeq1{,}87$ : la pulsation de modulation $(\omega''-\omega')/2=0{,}62\,\omega_0$ est du même ordre que celle de la porteuse $(\omega''+\omega')/2=2{,}03\,\omega_0$. La factorisation est mathématiquement possible, mais il n'y a pas de véritable phénomène de battement. Des battements nets existeraient pour des oscillateurs presque identiques et faiblement couplés (exercices 1 et 7).


> [!note]- 🔗 Liens avec d'autres disciplines
> **Physique des molécules**
>
> Les modes d'une molécule triatomique linéaire ($\mathrm{CO_2}$) se calculent exactement comme ici ; les amplitudes sont inégales quand les masses ou les liaisons diffèrent.
>
> **Génie civil**
>
> Un bâtiment à deux étages de raideurs différentes : mode fondamental avec les deux étages en phase (amplitude croissante avec la hauteur), second mode avec un nœud.


> [!question]- 🔭 Aller plus loin — Licence : Élimination et équation du quatrième ordre
> Éliminer $x_2$ entre les deux équations conduit à $x_1''''+9\omega_0^2x_1''+14\omega_0^4x_1=0$, équation scalaire d'ordre $4$ dont le polynôme caractéristique $(r^2+2\omega_0^2)(r^2+7\omega_0^2)$ redonne les pulsations propres (voir le petit cours sur les équations d'ordre $N$).


> [!question]- 🔭 Aller plus loin — Licence : Le ressort central est-il jamais au repos ?
> Il serait au repos pour tout $t$ si $x_2-x_1\equiv0$. Dans la solution générale, $x_2-x_1=-\tfrac32A'\cos(\omega't+\varphi')-3A''\cos(\omega''t+\varphi'')$ ne peut être identiquement nul que pour $A'=A''=0$ : pas de mouvement.


> [!question]- 🔭 Aller plus loin — Master : Perturbation d'un système symétrique
> Pour des raideurs $k$, $k(1+\delta)$, $k$ avec $\delta\ll1$, étudier comment la dissymétrie mélange les modes $(1,\pm1)$ et décale les fréquences (voir l'exercice 7).


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex3-oscillations-libres-et-forcees-d-un-couplage-pendule-chariot|Exercice 3 — Oscillations libres et forcées d'un couplage pendule-chariot]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex4-frequence-propre-d-une-molecule-diatomique|Exercice 4 — Fréquence propre d'une molécule diatomique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex5-complement-niveau-1-cpge-pendules-couples-par-un-ressort-attache-a-mi-hauteur|Exercice 5 — Complément (niveau 1, CPGE) : pendules couplés par un ressort attaché à mi-hauteur]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex6-complement-niveau-2-ambitieux-trois-masses-quatre-ressorts-diagonalisation-et-perturbation|Exercice 6 — Complément (niveau 2, ambitieux) : trois masses, quatre ressorts, diagonalisation et perturbation]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex7-complement-niveau-2-ambitieux-oscillateurs-desaccordes-anticroisement-et-transfert-d-energie|Exercice 7 — Complément (niveau 2, ambitieux) : oscillateurs désaccordés, anticroisement et transfert d'énergie]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex8-complement-niveau-3-ens-modes-non-lineaires-de-deux-pendules-couples-stabilite-et-instabilite-parametrique|Exercice 8 — Complément (niveau 3, ENS) : modes non linéaires de deux pendules couplés, stabilité et instabilité paramétrique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex9-complement-niveau-3-ens-anneau-de-n-oscillateurs-modes-de-fourier-et-propagation-du-signal|Exercice 9 — Complément (niveau 3, ENS) : anneau de N oscillateurs, modes de Fourier et propagation du signal]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex1-pendules-couples-et-battements|Exercice 1 — Pendules couplés et battements]]

