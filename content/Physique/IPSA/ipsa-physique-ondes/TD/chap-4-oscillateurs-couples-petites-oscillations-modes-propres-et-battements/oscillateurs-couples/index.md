---
title: "Oscillateurs couplés"
tags:
  - td
  - chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements
---

[[physique/IPSA/ipsa-physique-ondes/index|⬅ Physique des ondes]]


> [!info] ℹ️ Chap. 4 — Oscillateurs couplés : petites oscillations, modes propres et battements
> Séance 5



<a href="/pdfs/td4_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>


> [!question]- 🪝 Accroche
> **Deux balançoires reliées par une corde : pourquoi l'une s'arrête-t-elle quand l'autre repart ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *Deux enfants sont sur deux balançoires identiques voisines, reliées par une corde souple. L'un d'eux se balance, l'autre est au repos. Au bout d'un moment le premier ralentit puis s'immobilise tandis que le second s'est mis à se balancer, puis la situation se renverse. **Pourquoi, et au bout de combien de temps ?** Que se passe-t-il si les deux enfants se balancent exactement en même temps, dans le même sens ? Et s'ils se balancent en sens opposé ?*
>
> **Idée clé : un système couplé a plusieurs fréquences propres, et le mouvement général est leur superposition.** Pour deux oscillateurs identiques de pulsation $\omega_0$ couplés, il existe deux mouvements « purs » : en phase (le couplage ne travaille pas, $\omega_1=\omega_0$) et en opposition de phase (le couplage ajoute de la raideur, $\omega_2>\omega_0$). Un mouvement quelconque est la somme des deux ; comme les fréquences diffèrent légèrement, les deux composantes se déphasent lentement et l'énergie oscille d'un oscillateur à l'autre :
> $$x_1=a\sin\frac{\omega_2-\omega_1}2t\ \sin\frac{\omega_1+\omega_2}2t,\qquad x_2=a\cos\frac{\omega_2-\omega_1}2t\ \cos\frac{\omega_1+\omega_2}2t.$$



> [!abstract]- 🧠 À savoir avant
> **Mouvement du point matériel dans une base locale**
>
> Savoir exprimer position, vitesse et accélération d'un point en coordonnées cartésiennes puis en base polaire ; savoir que $\dfrac{\mathrm d\vec e_r}{\mathrm dt}=\dot\theta\,\vec e_\theta$ et $\dfrac{\mathrm d\vec e_\theta}{\mathrm dt}=-\dot\theta\,\vec e_r$ ; savoir projeter un vecteur sur un axe à l'aide d'un produit scalaire.
>
> **Oscillateur harmonique à un degré de liberté**
>
> Savoir que $\ddot x+\omega_0^2x=0$ a pour solution générale $x=A\cos(\omega_0t+\varphi)$ avec deux constantes fixées par $x(0)$ et $\dot x(0)$ ; connaître $\omega_0=\sqrt{k/m}$ pour un ressort et $\omega_0=\sqrt{g/\ell}$ pour un pendule simple de faible amplitude.
>
> **Principe fondamental de la dynamique et théorème du centre de masse**
>
> $m\vec a=\sum\vec F$ pour un point ; pour un système, $M_{\mathrm{tot}}\vec a_G=\sum\vec F_{\mathrm{ext}}$ : les forces intérieures (action-réaction) n'interviennent pas dans le mouvement du centre de masse.
>
> **Développements limités usuels**
>
> Connaître $\sin\theta=\theta-\dfrac{\theta^3}{6}+\dots$, $\cos\theta=1-\dfrac{\theta^2}{2}+\dots$, $\sqrt{1+\varepsilon}\simeq1+\dfrac\varepsilon2$ et savoir quel ordre conserver selon la grandeur étudiée (voir le point de cours « développements limités »).
>
> **Algèbre linéaire élémentaire**
>
> Systèmes $2\times2$, déterminant, valeurs et vecteurs propres d'une matrice $2\times2$, produit scalaire de deux vecteurs, matrice symétrique ; pour les compléments, matrices $3\times3$ et notion de base orthogonale.
>
> **Notation complexe**
>
> $\partial_t\to i\omega$ pour $e^{i\omega t}$ ; passage de $\mathrm{Re}\big[\underline Ae^{i\omega t}\big]$ à l'amplitude et à la phase ; formules de trigonométrie de somme et de produit.



> [!info]- 🎯 Ce que tu sauras faire
> **Comprendre ce que l'on projette**
>
> Savoir distinguer un vecteur de ses coordonnées, choisir une base adaptée (cartésienne ou locale), justifier chaque signe d'une projection à l'aide du schéma et d'un produit scalaire, et expliquer pourquoi une base locale varie avec le temps.
>
> **Passer des équations exactes aux équations linéarisées en connaissance de cause**
>
> Savoir écrire les équations exactes d'un système couplé simple, identifier les termes linéaires, non linéaires et de couplage, justifier physiquement et mathématiquement la linéarisation autour d'un équilibre, et estimer l'erreur commise.
>
> **Maîtriser les deux méthodes de découplage**
>
> Savoir découpler à la manière du physicien (somme, différence, centre de masse et mouvement relatif, symétrie) et à la manière du mathématicien (matrices $M$ et $K$, problème aux valeurs propres, diagonalisation), savoir dire quand la première fonctionne et pourquoi la seconde fonctionne toujours.
>
> **Interpréter les modes propres**
>
> Savoir décrire le mouvement de chaque élément dans chaque mode (phases, amplitudes relatives), relier les pulsations aux paramètres, décomposer un mouvement initial sur les modes, et reconnaître battements et échanges d'énergie.
>
> **Situer les équations différentielles linéaires dans un cadre général**
>
> Savoir ramener une équation d'ordre $N$ à un système du premier ordre $Y'=AY$, relier les solutions exponentielles aux valeurs propres de $A$, et ne pas confondre valeurs propres de $A$ et pulsations propres $\omega$ du problème mécanique.



> [!tip]- 📖 Rappel de cours
> **Projeter correctement : bases cartésienne et locale, vecteurs et coordonnées**
>
> **Un vecteur n'est pas ses coordonnées.** Le vecteur $\vec F$ est un objet géométrique (une flèche) qui existe indépendamment de tout repère ; ses *coordonnées* ne sont que sa « lecture » dans une base : $\vec F=F_x\vec e_x+F_y\vec e_y=F_r\vec e_r+F_\alpha\vec e_\alpha$. Changer de base change les coordonnées, pas le vecteur.
>
>
>
> 1. **Base cartésienne** $(\vec e_x,\vec e_y,\vec e_z)$, fixe dans le référentiel du laboratoire : ses vecteurs sont constants, $\mathrm d\vec e_x/\mathrm dt=\vec 0$. Orientation directe : $\vec e_z=\vec e_x\wedge\vec e_y$.
> 2. **Base locale d'un pendule.** L'angle $\alpha$ est mesuré à partir de la verticale descendante, positif lorsque la masse part vers $+x$ (sens trigonométrique si $\vec e_y$ est dirigé vers le haut) :
>     $$\vec e_r=\sin\alpha\,\vec e_x-\cos\alpha\,\vec e_y\ \ (\text{du point d'attache vers la masse}),\qquad \vec e_\alpha=\cos\alpha\,\vec e_x+\sin\alpha\,\vec e_y\ \ (\text{sens des }\alpha\text{ croissants}).$$
>     Ces coordonnées se lisent sur le schéma à l'aide de produits scalaires : $\vec e_r\cdot\vec e_x=\cos\big(\tfrac\pi2-\alpha\big)=\sin\alpha$ et $\vec e_r\cdot\vec e_y=\cos(\pi-\alpha)=-\cos\alpha$. La base est orthonormée directe : $\vec e_r\cdot\vec e_\alpha=0$, $\|\vec e_r\|=\|\vec e_\alpha\|=1$, $\vec e_r\wedge\vec e_\alpha=\vec e_z$.
> 3. **Règle de projection.** La coordonnée d'un vecteur sur un vecteur *unitaire* est le produit scalaire avec ce vecteur : $F_\alpha=\vec F\cdot\vec e_\alpha$. Projeter, c'est mesurer « combien de $\vec F$ » pointe dans la direction choisie.
> 4. **Une base locale tourne avec le système.** $\vec e_r$ et $\vec e_\alpha$ dépendent de $\alpha(t)$ : $\dfrac{\mathrm d\vec e_r}{\mathrm dt}=\dot\alpha\,\vec e_\alpha$ et $\dfrac{\mathrm d\vec e_\alpha}{\mathrm dt}=-\dot\alpha\,\vec e_r$. Pour une masse à la distance fixe $\ell$ du point d'attache : $\vec v=\ell\dot\alpha\,\vec e_\alpha$ et $\vec a=\ell\ddot\alpha\,\vec e_\alpha-\ell\dot\alpha^2\,\vec e_r$ (accélération tangentielle et centripète).
> 5. **Pourquoi choisir la base locale ?** La tension du fil est le long de $\vec e_r$ : en projetant sur $\vec e_\alpha$, elle disparaît de l'équation, et l'on obtient directement une équation différentielle en la seule variable $\alpha$ (on élimine une force de liaison inconnue).
>
>
>
> **Protocole pour justifier un signe** : (a) dessiner le vecteur pour une valeur *positive* de la variable ; (b) comparer son sens avec le sens positif de l'axe de projection ; (c) le confirmer par un produit scalaire ; (d) tester sur un cas limite ($\alpha=0$, $\alpha=\pi/2$) où la réponse est évidente.
>
> **Pourquoi étudier de petites oscillations autour d'un équilibre ?**
>
> Une position d'équilibre $q_0$ est un point où l'énergie potentielle $V(q)$ est stationnaire, $V'(q_0)=0$ (force nulle) ; elle est *stable* si $V''(q_0)>0$ (minimum). Une petite perturbation reste alors petite : le système oscille au voisinage de $q_0$ et c'est dans ce voisinage seulement que l'approximation a un sens. Au voisinage d'un minimum, la formule de Taylor donne
> $$V(q)=V(q_0)+\frac12V''(q_0)\,(q-q_0)^2+O\big((q-q_0)^3\big).$$
> Le terme linéaire a disparu (équilibre) : *toute* énergie potentielle régulière est, près de son minimum, une parabole. La force $-V'(q)\simeq-V''(q_0)(q-q_0)$ est donc une force de rappel linéaire de raideur $k_{\mathrm{eff}}=V''(q_0)$, quelle que soit l'origine physique du potentiel. C'est pourquoi l'oscillateur harmonique est universel : pendule ($V=mg\ell(1-\cos\alpha)$ donne $k_{\mathrm{eff}}=mg\ell$), liaison chimique ($k=V''(r_0)$, exercice 4), cristal, pont, circuit.
>
> Avec plusieurs variables $q_i$, le même raisonnement donne $V\simeq V_0+\tfrac12\sum_{i,j}K_{ij}(q_i-q_{i0})(q_j-q_{j0})$ avec la *matrice hessienne* $K_{ij}=\partial^2V/\partial q_i\partial q_j$ évaluée à l'équilibre. Elle est symétrique (théorème de Schwarz) et l'équilibre est stable si elle est définie positive. On linéarise *simultanément* toutes les équations parce que tous les écarts $q_j-q_{j0}$ sont petits en même temps : un produit comme $\alpha_1\alpha_2$ est d'ordre $2$, de même nature que $\alpha_1^2$, et se néglige pour la même raison.
>
> **Petits angles, développements limités, linéarisation : trois notions à ne pas confondre**
>
> - Un **développement limité** (DL) est un énoncé *mathématique* sur une fonction : $f(\theta)=f(0)+f'(0)\theta+\dots+\dfrac{f^{(n)}(0)}{n!}\theta^n+o(\theta^n)$. Il est toujours vrai ; il ne dit rien de la physique et ne suppose pas que $\theta$ soit « petit » avant que l'on demande une valeur numérique.
> - L'**approximation des petits angles** est une *application* de ce DL : pour $|\theta|\ll1$ rad, on remplace $\sin\theta$ et $\tan\theta$ par $\theta$ et $\cos\theta$ par $1$ (ou $1-\theta^2/2$ si l'ordre $1$ ne suffit pas).
> - La **linéarisation** est une *démarche physique* : on développe les équations du mouvement (ou l'énergie) autour de l'équilibre et on ne garde que les termes du premier ordre dans les équations (du second ordre dans l'énergie). Elle contient les petits angles mais aussi d'autres développements : $\sqrt{u^2+v^2}-d\simeq u-d$ pour la longueur d'un ressort presque horizontal, par exemple.
>
>
>
> **Ordre en fonction de l'objet développé.** Si $\varepsilon$ désigne la taille typique des angles, l'équation du mouvement est d'ordre $1$ ($\ddot\alpha\sim\varepsilon$) et l'énergie d'ordre $2$ ($E\sim\varepsilon^2$). On a donc $\cos\theta\simeq1$ dans une force qui est déjà multipliée par un petit paramètre, mais $1-\cos\theta\simeq\theta^2/2$ dans l'énergie potentielle du pendule : prendre $\cos\theta\simeq1$ dans $V=mg\ell(1-\cos\alpha)$ donnerait $V=0$ et aucune force de rappel. Ces deux écritures ne se contredisent pas : $F=-\mathrm dV/\mathrm d\alpha=-mg\ell\sin\alpha\simeq-mg\ell\alpha$ est la dérivée de $V\simeq\tfrac12mg\ell\alpha^2$.
>
> **Physique de l'approximation pour un pendule.**
>
>
> 1. La masse se déplace sur un arc de cercle ; pour $\alpha$ petit, l'arc $\ell\alpha$ et la corde $2\ell\sin(\alpha/2)$ sont presque confondus : le mouvement est quasiment rectiligne et horizontal. Son abscisse $x=\ell\sin\alpha\simeq\ell\alpha$ est proportionnelle à l'angle.
> 2. Son élévation $\ell(1-\cos\alpha)\simeq\ell\alpha^2/2$ est du second ordre : elle est négligeable devant $x$ (rapport $\alpha/2$) ; la tension du fil vaut $mg$ à l'ordre $0$.
> 3. La force de rappel tangentielle $-mg\sin\alpha\simeq-mg\,x/\ell$ est proportionnelle au déplacement : le poids joue le rôle d'un ressort de raideur $mg/\ell$.
> 4. Une équation différentielle *linéaire à coefficients constants* possède le principe de superposition : toute combinaison de solutions est solution, les solutions s'obtiennent par des exponentielles $e^{rt}$, et un système couplé devient un problème d'algèbre linéaire (valeurs propres).
>
>
>
> **Ce que l'on perd.** L'isochronisme : la période $T(\theta_0)=T_0\Big(1+\dfrac{\theta_0^2}{16}+\dfrac{11\theta_0^4}{3072}+\dots\Big)$ dépend de l'amplitude (par exemple $+0{,}19\ \%$ à $10^\circ$, $+1{,}7\ \%$ à $30^\circ$, $+18\ \%$ à $90^\circ$). On perd aussi les harmoniques de rang supérieur (le mouvement n'est plus purement sinusoïdal), les couplages *non linéaires* entre modes (échange d'énergie entre modes supposés indépendants, instabilités paramétriques, chaos pour deux pendules à grande amplitude) et les écarts d'équilibre. On gagne une théorie analytique complète. Ordre de grandeur de validité : pour que l'écart sur la période reste inférieur à $1\ \%$, il faut $\theta_0\lesssim0{,}4$ rad ($\simeq23^\circ$).
>
> **Développements limités de $\sin$ et $\cos$ : lecture, ordre, erreur**
>
> **Énoncé (Taylor--Young).** Pour tout réel $\theta$,
> $$\sin\theta=\theta-\frac{\theta^3}{3!}+\frac{\theta^5}{5!}-\dots+(-1)^n\frac{\theta^{2n+1}}{(2n+1)!}+\dots,\qquad \cos\theta=1-\frac{\theta^2}{2!}+\frac{\theta^4}{4!}-\dots+(-1)^n\frac{\theta^{2n}}{(2n)!}+\dots$$
> Les signes alternent, et seuls apparaissent des puissances *impaires* pour le sinus (fonction impaire) et *paires* pour le cosinus (fonction paire) : c'est la raison pour laquelle les deux fonctions n'ont pas le même terme dominant. Le terme d'ordre $\theta^2$ du sinus est nul, donc $\sin\theta\simeq\theta$ à l'ordre $1$ *et* à l'ordre $2$ ; au contraire $\cos\theta\simeq1$ à l'ordre $1$ mais $\cos\theta\simeq1-\theta^2/2$ à l'ordre $2$.
>
> **Comment lire un développement.** Chaque terme est plus petit que le précédent d'un facteur $\theta^2/\big(2n(2n+1)\big)$ pour le sinus (resp. $\theta^2/\big((2n-1)2n\big)$ pour le cosinus) : pour $|\theta|<1$ la série décroît très vite. On garde les termes dont la contribution est supérieure à la précision cherchée *et* on veille à ce que le terme dominant ne s'annule pas (par exemple $1-\cos\theta\simeq\theta^2/2$, jamais $0$).
>
> **Estimer l'erreur.** (i) Reste de Taylor--Lagrange : les dérivées de $\sin$ et $\cos$ sont bornées par $1$, donc $\big|R_n(\theta)\big|\le\dfrac{|\theta|^{n+1}}{(n+1)!}$ pour tout $\theta$ : $|\sin\theta-\theta|\le\dfrac{|\theta|^3}{6}$, $|\cos\theta-1|\le\dfrac{\theta^2}{2}$ et $\big|\cos\theta-(1-\tfrac{\theta^2}{2})\big|\le\dfrac{\theta^4}{24}$. (ii) Série alternée à termes décroissants : l'erreur est majorée par le premier terme négligé. L'erreur relative sur $\sin\theta\simeq\theta$ vaut environ $\theta^2/6$ ; sur $\cos\theta\simeq1$, environ $\theta^2/2$, trois fois plus : l'ordre $0$ du cosinus est une approximation moins bonne que l'ordre $1$ du sinus.
> $$
> \begin{array}{c|ccccc}
>   \theta\ (\mathrm{rad}) & 0{,}05 & 0{,}1 & 0{,}2 & 0{,}5 & 1\\
>   \hline
>   \text{erreur relative de }\sin\theta\simeq\theta & 4\times10^{-4} & 1{,}7\times10^{-3} & 6{,}7\times10^{-3} & 4{,}3\times10^{-2} & 0{,}19\\
>   \text{erreur relative de }\cos\theta\simeq1 & 1{,}3\times10^{-3} & 5{,}0\times10^{-3} & 2{,}0\times10^{-2} & 0{,}14 & 0{,}85\\
>   \text{erreur relative de }\cos\theta\simeq1-\theta^2/2 & 3\times10^{-7} & 4\times10^{-6} & 7\times10^{-5} & 3\times10^{-3} & 7\times10^{-2}
> \end{array}
> $$
> **Intuition géométrique.** $\sin\theta<\theta$ exprime que la corde est plus courte que l'arc ; $1-\cos\theta\simeq\theta^2/2$ est la « flèche » de l'arc, c'est-à-dire la hauteur dont la masse s'élève : elle est du second ordre alors que le déplacement horizontal est du premier ordre.
>
> **Découpler à la manière du physicien : somme, différence, symétrie**
>
> **Méthode.** Pour des équations couplées, on commence par *regarder* : (i) écrire toutes les équations ; (ii) comparer les coefficients ; (iii) chercher une symétrie (échange de deux oscillateurs identiques, symétrie miroir) ; (iv) additionner et soustraire ; (v) chercher des combinaisons dont l'équation *se referme* sur elle-même. Pour deux oscillateurs identiques de coordonnées $x_1$ et $x_2$ on prend $S=x_1+x_2$ et $D=x_1-x_2$.
>
> **Pourquoi cela correspond à des mouvements physiques.** La somme est (au facteur $2$ près) la position du centre de masse : les forces de couplage sont des forces intérieures égales et opposées, elles s'annulent dans la somme. La différence est le mouvement relatif : l'élongation du ressort de couplage y est directement lisible. $S$ décrit le *mode symétrique* (les deux éléments bougent en phase) et $D$ le *mode antisymétrique* (en opposition de phase) au sens de l'échange $x_1\leftrightarrow x_2$ des coordonnées.
>
> **Quand cela marche.** Écrivons $\ddot X=-AX$ avec $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$. Les vecteurs $(1,1)$ et $(1,-1)$ sont vecteurs propres de $A$ si et seulement si $a+b=c+d$ et $a-b=d-c$, c'est-à-dire si et seulement si $a=d$ et $b=c$ : mêmes coefficients diagonaux (oscillateurs identiques vis-à-vis de l'extérieur) et couplage réciproque symétrique. Autrement dit, $A$ commute avec la matrice d'échange $P=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ dont $(1,\pm1)$ sont les vecteurs propres. La symétrie du système *est* la raison du découplage.
>
> **Quand cela échoue.** Pour des oscillateurs dissymétriques ($a\neq d$), $S$ et $D$ restent couplés (exercice 2). On généralise alors : on cherche $c=x_1+\beta x_2$ tel que $\ddot c=-\omega^2c$. L'identification des coefficients conduit à une équation du second degré en $\beta$ dont les deux racines fournissent les deux modes : c'est exactement le calcul de valeurs propres, mené sans le dire. Dans le cas de masses *inégales* (exercice 4) les bonnes combinaisons sont $m_1x_1+m_2x_2$ (centre de masse) et $x_2-x_1$ (mouvement relatif), et non $x_1\pm x_2$.
>
> **Découpler à la manière du mathématicien : $M\ddot X+KX=0$ et diagonalisation**
>
> **Mise en forme.** Pour $n$ coordonnées $X=(q_1,\dots,q_n)^{\mathsf T}$ d'un système conservatif, l'énergie cinétique et l'énergie potentielle sont, à l'ordre quadratique, $E_c=\tfrac12\dot X^{\mathsf T}M\dot X$ et $E_p=\tfrac12X^{\mathsf T}KX$, et les équations du mouvement sont
> $$M\ddot X+KX=0.$$
> $M$ est la *matrice de masse* (inertie ; symétrique définie positive ; diagonale si l'énergie cinétique ne contient pas de termes croisés) et $K$ la *matrice de raideur* (rappel ; symétrique ; sur la diagonale, la raideur « vue » par chaque coordonnée, hors diagonale l'opposé de la raideur de couplage). Un terme hors diagonale non nul dans $K$ *est* le couplage.
>
> **Résolution.**
>
>
> 1. On cherche une solution harmonique : $X(t)=\mathrm{Re}\big[A\,e^{i\omega t}\big]$ avec $A$ un vecteur constant (même pulsation et phases liées pour toutes les coordonnées : un *mode*).
> 2. On reporte, $\ddot X=-\omega^2X$ : $(K-\omega^2M)A=0$, *problème aux valeurs propres généralisé*.
> 3. Solution non triviale si et seulement si $\det(K-\omega^2M)=0$ : équation de degré $n$ en $\omega^2$.
> 4. Les $n$ racines $\omega_p^2$ sont les carrés des pulsations propres. Comme $M$ est inversible, on se ramène à un problème classique $\big(M^{-1}K-\omega^2I\big)A=0$.
> 5. Pour chaque $\omega_p^2$ on résout $(K-\omega_p^2M)A_p=0$ : vecteur propre $A_p$ défini à un facteur près.
> 6. Théorème spectral : $K$ et $M$ symétriques, $M>0$, $\Rightarrow$ les $\omega_p^2$ sont réels, positifs si l'équilibre est stable ($K>0$), et les vecteurs propres sont *$M$-orthogonaux* : $A_p^{\mathsf T}MA_q=0$ pour $p\neq q$ (orthogonaux au sens usuel si $M\propto I$).
> 7. Les solutions de la forme $A_p\cos(\omega_pt+\varphi_p)$ sont les *modes normaux*. Les coordonnées normales $\xi_p=A_p^{\mathsf T}MX/(A_p^{\mathsf T}MA_p)$ vérifient $\ddot\xi_p+\omega_p^2\xi_p=0$ : $n$ oscillateurs indépendants.
> 8. Superposition : $X(t)=\sum_p\big(c_p\cos\omega_pt+d_p\sin\omega_pt\big)A_p$.
> 9. Conditions initiales : si les $A_p$ sont $M$-normalisés ($A_p^{\mathsf T}MA_p=1$), $c_p=A_p^{\mathsf T}MX(0)$ et $d_p\omega_p=A_p^{\mathsf T}M\dot X(0)$.
>
>
>
> **Diagonalisation explicite à deux degrés de liberté.** Pour $M=mI$ et $K=m\begin{pmatrix}a&b\\b&c\end{pmatrix}$ : $\omega_\pm^2=\dfrac{a+c}2\pm\sqrt{\Big(\dfrac{a-c}2\Big)^2+b^2}$. Les vecteurs propres sont $u_\theta=(\cos\theta,\sin\theta)$ et $u_\theta^\perp=(-\sin\theta,\cos\theta)$ avec $\tan2\theta=\dfrac{2b}{a-c}$, $\theta$ étant l'angle dont tournent les axes. Pour identifier à quelle valeur propre correspond chaque vecteur, calculer $u^{\mathsf T}Ku/u^{\mathsf T}u$. Si $a=c$ (oscillateurs identiques), $\tan2\theta=\infty$, soit $\theta=45^\circ$ *quelle que soit la force du couplage* : on retrouve $S$ et $D$. Si $|a-c|\gg|b|$, $\theta\simeq b/(a-c)$ est petit : les modes sont presque localisés sur un seul oscillateur (couplage faible devant l'écart de fréquence).
>
> **Vérifications.** La somme des valeurs propres est la trace de $M^{-1}K$ et leur produit est son déterminant ; $K$ définie positive $\iff$ $\omega_p^2>0$ ; $k\to0$ redonne les oscillateurs libres.
>
> **Petit cours : équations différentielles linéaires d'ordre $N$, systèmes du premier ordre, exponentielle de matrice**
>
> **Trois objets à ne pas confondre.**
> $$
> \begin{array}{l|l|c}
>   \textbf{Objet} & \textbf{Écriture} & \textbf{Dimension de l'espace des solutions}\\
>   \hline
>   \text{équation scalaire d'ordre }N & y^{(N)}+a_{N-1}y^{(N-1)}+\dots+a_0y=0 & N\\
>   \text{système du 1\textsuperscript{er} ordre} & Y'=AY,\ Y\in\mathbb R^N & N\\
>   \text{système de }n\text{ équations du 2\textsuperscript{e} ordre} & M\ddot X+KX=0,\ X\in\mathbb R^n & 2n
> \end{array}
> $$
> Le nombre de constantes d'intégration est la dimension de l'espace des solutions : il faut autant de conditions initiales (positions *et* vitesses pour un système mécanique).
>
> **Équation scalaire d'ordre $N$ à coefficients constants.** On cherche $y=e^{rt}$ : $P(r)=r^N+a_{N-1}r^{N-1}+\dots+a_0=0$ (*polynôme caractéristique*). Racine simple $r_j$ : solution $e^{r_jt}$ ; racine de multiplicité $\nu$ : $e^{rt},te^{rt},\dots,t^{\nu-1}e^{rt}$ ; paire complexe $\sigma\pm i\omega$ : $e^{\sigma t}\cos\omega t$ et $e^{\sigma t}\sin\omega t$. Exemple : $y''+\omega^2y=0$, $r=\pm i\omega$.
>
> **Réduction au premier ordre.** Avec $Y=\big(y,y',\dots,y^{(N-1)}\big)^{\mathsf T}$ on a $Y'=AY$ où $A$ est la matrice *compagne*
> $$A=\begin{pmatrix}0&1&0&\cdots&0\\0&0&1&\cdots&0\\\vdots&&&\ddots&\vdots\\-a_0&-a_1&-a_2&\cdots&-a_{N-1}\end{pmatrix},\qquad \det(\lambda I-A)=P(\lambda).$$
> Les valeurs propres de $A$ sont exactement les racines caractéristiques. Exemple $N=2$ : $A=\begin{pmatrix}0&1\\-\omega^2&0\end{pmatrix}$, $\lambda=\pm i\omega$.
>
> **Solutions et exponentielle de matrice.** Si $Av=\lambda v$, alors $Y(t)=e^{\lambda t}v$ est solution. Si $A$ est diagonalisable, $A=P\,\mathrm{diag}(\lambda_j)\,P^{-1}$ et la solution générale est $Y(t)=\sum_jc_je^{\lambda_jt}v_j$, soit $Y(t)=e^{At}Y(0)$ avec $e^{At}=\sum_{k\ge0}\dfrac{A^kt^k}{k!}=P\,\mathrm{diag}(e^{\lambda_jt})\,P^{-1}$ ; on vérifie $\dfrac{\mathrm d}{\mathrm dt}e^{At}=Ae^{At}$. Si $A$ n'est pas diagonalisable (blocs de Jordan), des termes $t^je^{\lambda t}$ apparaissent : $\ddot x=0$ conduit à $x=a+bt$, valeur propre double $\lambda=0$ (c'est le mode de translation d'un système libre, exercices 4 et 9).
>
> **Lien avec les oscillateurs couplés.** Pour $M\ddot X+KX=0$ on pose $Z=(X,\dot X)^{\mathsf T}\in\mathbb R^{2n}$ :
> $$Z'=\mathcal A\,Z,\qquad \mathcal A=\begin{pmatrix}0&I\\-M^{-1}K&0\end{pmatrix}.$$
> Si $M^{-1}K\,u_p=\omega_p^2u_p$, alors $\mathcal A\begin{pmatrix}u_p\\\pm i\omega_pu_p\end{pmatrix}=\pm i\omega_p\begin{pmatrix}u_p\\\pm i\omega_pu_p\end{pmatrix}$. Il y a donc *trois* objets différents :
> $$
> \begin{array}{l|l|l}
>   \omega_p^2 & \text{valeur propre de }M^{-1}K\ (n\times n) & \mathrm{s^{-2}},\ \text{réelle positive}\\
>   \omega_p & \text{pulsation propre} & \mathrm{rad\cdot s^{-1}}\\
>   \lambda=\pm i\omega_p & \text{valeur propre de }\mathcal A\ (2n\times2n) & \mathrm s^{-1},\ \text{imaginaire pure},\ \lambda^2=-\omega_p^2
> \end{array}
> $$
> **Forme close.** On peut écrire $X(t)=\cos(\Omega t)X_0+\Omega^{-1}\sin(\Omega t)\dot X_0$ avec $\Omega=(M^{-1}K)^{1/2}$, racine carrée de matrice définie par diagonalisation : c'est la décomposition sur les modes de la rubrique précédente écrite sous forme compacte.
>
> **Modes propres, superposition, battements, échanges d'énergie**
>
> - Un **mode propre** est un mouvement où toutes les coordonnées oscillent à la *même* pulsation avec des amplitudes relatives fixées (phases égales ou opposées). Un système à $n$ degrés de liberté possède $n$ modes ; un couplage *lève la dégénérescence* des fréquences des oscillateurs identiques, car la raideur de couplage est « vue » différemment selon la forme du mode (nulle si le ressort n'est pas déformé, maximale si les éléments sont en opposition).
> - Le mode de plus basse fréquence est en phase (pas de nœud) ; le plus haut est le plus « alterné ». Plus un mode comporte de nœuds, plus sa pulsation est élevée. Le quotient de Rayleigh $\omega^2=\dfrac{A^{\mathsf T}KA}{A^{\mathsf T}MA}$ exprime que la pulsation est le rapport de l'énergie potentielle à l'énergie cinétique « réduite » du mode.
> - Toute solution est une **superposition** de modes ; le poids de chaque mode est fixé par les conditions initiales. **Excitation sélective :** un mouvement initial proportionnel à un vecteur propre (positions *et* vitesses) n'excite que ce mode ; sinon, tous les modes dont le poids est non nul sont présents.
> - **Battements.** La somme de deux mouvements sinusoïdaux de même amplitude et de pulsations proches s'écrit $\cos\omega_1t+\cos\omega_2t=2\cos\dfrac{\omega_2-\omega_1}2t\cos\dfrac{\omega_1+\omega_2}2t$ : porteuse à la pulsation moyenne, enveloppe lente de période $T_b=\dfrac{2\pi}{|\omega_2-\omega_1|}$. L'interprétation en « enveloppe lente » exige $|\omega_2-\omega_1|\ll\omega_1+\omega_2$ ; la factorisation reste mathématiquement exacte dans tous les cas.
> - **Échanges d'énergie.** Pour deux oscillateurs identiques faiblement couplés, l'énergie passe périodiquement de l'un à l'autre. Le transfert est *complet* si les fréquences sont égales avant couplage et si les deux modes ont le même poids ; il est partiel si les oscillateurs sont désaccordés (exercice 7).
> - **Réponse forcée.** En régime sinusoïdal forcé à la pulsation $\omega$, $(K-\omega^2M)\underline X=\underline F$ : l'amplitude diverge (idéalement) à chaque pulsation propre (résonances) et peut s'annuler en un point donné pour une pulsation particulière (antirésonance, exercice 3).



> [!note]- 🧮 Outils mathématiques
> **Produit scalaire et projection**
>
> $\vec u\cdot\vec v=\|\vec u\|\|\vec v\|\cos(\vec u,\vec v)=u_xv_x+u_yv_y$ ; coordonnée de $\vec F$ sur le vecteur unitaire $\vec e$ : $F_e=\vec F\cdot\vec e$.
>
> **Dérivation d'une base locale**
>
> $\dfrac{\mathrm d}{\mathrm dt}(\cos\alpha,\sin\alpha)=\dot\alpha(-\sin\alpha,\cos\alpha)$ : tourner un vecteur unitaire de $\pi/2$ donne le vecteur dérivé.
>
> **Développements limités de $\sin$, $\cos$, $\sqrt{1+\varepsilon}$**
>
> $\sin\theta=\theta-\dfrac{\theta^3}6+\dots$ ; $\cos\theta=1-\dfrac{\theta^2}2+\dots$ ; $\sqrt{1+\varepsilon}=1+\dfrac\varepsilon2-\dfrac{\varepsilon^2}8+\dots$ Erreur : premier terme négligé (séries alternées) ou reste de Taylor--Lagrange.
>
> **Formules de somme et de produit**
>
> $\cos p+\cos q=2\cos\dfrac{p+q}2\cos\dfrac{p-q}2$ ; $\cos p-\cos q=-2\sin\dfrac{p+q}2\sin\dfrac{p-q}2$ ; $\cos(a\pm b)=\cos a\cos b\mp\sin a\sin b$.
>
> **Équation $y''+\omega^2y=0$ et formes équivalentes**
>
> $y=C\cos\omega t+D\sin\omega t=A\cos(\omega t+\varphi)$ avec $A=\sqrt{C^2+D^2}$ et $\tan\varphi=-D/C$ ; deux constantes fixées par $y(0)$ et $y'(0)$.
>
> **Matrices symétriques $2\times2$**
>
> Valeurs propres $\lambda_\pm=\dfrac{a+c}2\pm\sqrt{\big(\tfrac{a-c}2\big)^2+b^2}$ ; vecteurs propres orthogonaux ; trace $=\lambda_++\lambda_-$ ; déterminant $=\lambda_+\lambda_-$.
>
> **Problème aux valeurs propres généralisé**
>
> $(K-\omega^2M)A=0$ ; $\det(K-\omega^2M)=0$ ; orthogonalité $A_p^{\mathsf T}MA_q=0$ pour $p\neq q$ ; décomposition $X_0=\sum_pc_pA_p$ avec $c_p=A_p^{\mathsf T}MX_0/(A_p^{\mathsf T}MA_p)$.
>
> **Équation du second degré et discriminant**
>
> Pour une équation *bicarrée* $\omega^4-s\,\omega^2+p=0$, on résout en $\omega^2$ : $\omega^2=\tfrac12\big(s\pm\sqrt{s^2-4p}\big)$, discriminant positif si les valeurs propres sont réelles.
>
> **Exponentielle de matrice**
>
> $e^{At}=\sum_kA^kt^k/k!$ ; $\dfrac{\mathrm d}{\mathrm dt}e^{At}=Ae^{At}$ ; $e^{P\,D\,P^{-1}t}=P\,e^{Dt}P^{-1}$ pour $D$ diagonale.



## Exercices

- [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex1-pendules-couples-et-battements|Exercice 1 — Pendules couplés et battements]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex2-couplage-de-deux-oscillateurs-harmoniques-dissymetriques|Exercice 2 — Couplage de deux oscillateurs harmoniques dissymétriques]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex3-oscillations-libres-et-forcees-d-un-couplage-pendule-chariot|Exercice 3 — Oscillations libres et forcées d'un couplage pendule-chariot]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex4-frequence-propre-d-une-molecule-diatomique|Exercice 4 — Fréquence propre d'une molécule diatomique]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex5-complement-niveau-1-cpge-pendules-couples-par-un-ressort-attache-a-mi-hauteur|Exercice 5 — Complément (niveau 1, CPGE) : pendules couplés par un ressort attaché à mi-hauteur]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex6-complement-niveau-2-ambitieux-trois-masses-quatre-ressorts-diagonalisation-et-perturbation|Exercice 6 — Complément (niveau 2, ambitieux) : trois masses, quatre ressorts, diagonalisation et perturbation]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex7-complement-niveau-2-ambitieux-oscillateurs-desaccordes-anticroisement-et-transfert-d-energie|Exercice 7 — Complément (niveau 2, ambitieux) : oscillateurs désaccordés, anticroisement et transfert d'énergie]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex8-complement-niveau-3-ens-modes-non-lineaires-de-deux-pendules-couples-stabilite-et-instabilite-parametrique|Exercice 8 — Complément (niveau 3, ENS) : modes non linéaires de deux pendules couplés, stabilité et instabilité paramétrique]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex9-complement-niveau-3-ens-anneau-de-n-oscillateurs-modes-de-fourier-et-propagation-du-signal|Exercice 9 — Complément (niveau 3, ENS) : anneau de N oscillateurs, modes de Fourier et propagation du signal]]


> [!note]- 🔗 Liens avec d'autres disciplines
> **Chimie et spectroscopie**
>
> Les vibrations d'une molécule sont des modes normaux ; la fréquence d'absorption infrarouge d'une liaison $\mathrm{C{=}O}$ ou $\mathrm{O{-}H}$ identifie les groupes fonctionnels. La constante de raideur d'une liaison covalente est de l'ordre de $10^2$ à $10^3\ \mathrm{N\cdot m^{-1}}$.
>
> **Électrocinétique**
>
> Deux circuits $LC$ couplés par une inductance mutuelle ou une capacité de couplage sont exactement les deux oscillateurs de l'exercice 1 ; les deux fréquences propres sont celles du transformateur à résonance (mode en phase et mode en opposition).
>
> **Mécanique quantique**
>
> Le système à deux niveaux (molécule d'ammoniac, double puits) obéit à la même algèbre que deux oscillateurs couplés : écart d'énergie minimal $2\hbar\Omega$ à la résonance (anticroisement) et oscillations de Rabi entre les deux états.
>
> **Optique**
>
> Deux guides d'onde voisins échangent périodiquement leur puissance le long de leur propagation (coupleur directionnel) : l'axe de propagation joue le rôle du temps et l'échange d'énergie est le battement des deux « supermodes » symétrique et antisymétrique.
>
> **Génie civil et sismique**
>
> Un bâtiment multi-étages se modélise par un empilement de masses reliées par des ressorts de cisaillement (matrices $M$ et $K$ tridiagonales) ; les pulsations propres commandent la réponse à un séisme, et les absorbeurs à masse accordée (pendule suspendu sous un gratte-ciel) exploitent l'antirésonance de l'exercice 3.
>
> **Musique**
>
> Deux cordes de piano accordées à l'unisson couplées par le chevalet donnent deux modes voisins : leur battement lent produit la « chorus » ; en les désaccordant, on obtient un fondu ou un battement rapide. L'accordeur règle les cordes en écoutant les battements.
>
> **Physique du solide**
>
> Un cristal est un très grand système d'oscillateurs couplés : ses modes normaux (phonons) obéissent à $\omega(k)=2\sqrt{K/m}\,|\sin(ka/2)|$ pour une chaîne monoatomique (exercice 9 et TD 1, exercice 9).



> [!question]- 🔭 Aller plus loin — Licence : Formalisme lagrangien : où naissent $M$ et $K$
> Avec $L=\tfrac12\dot X^{\mathsf T}M\dot X-V(X)$, les équations d'Euler--Lagrange donnent $M\ddot X=-\nabla V$ ; au voisinage d'un équilibre, $\nabla V\simeq KX$ avec $K$ la hessienne de $V$. Retrouver ainsi les équations de l'exercice 1 en deux lignes (potentiel $V=-mg\ell(\cos\alpha_1+\cos\alpha_2)+\tfrac12k(\ell_{\mathrm{ressort}}-d)^2$), et comprendre que la linéarisation est un développement de $V$ à l'ordre $2$.



> [!question]- 🔭 Aller plus loin — Licence : Anticroisement des niveaux et théorie des perturbations
> Pour deux oscillateurs de pulsations propres voisines $\omega_a,\omega_b$ et de couplage $\Omega^2$, les pulsations propres de l'ensemble ne se croisent jamais quand on fait varier $\omega_b-\omega_a$ : leur écart minimal vaut $2\Omega^2$ (exercices 3 et 7). Le même phénomène existe en mécanique quantique (système à deux niveaux) et en optique (guides couplés).



> [!question]- 🔭 Aller plus loin — Master : Instabilité paramétrique et modes non linéaires
> Pour deux pendules identiques couplés, le mode en phase est solution *exacte* des équations non linéaires pour toute amplitude (le ressort reste à sa longueur naturelle) ; sa stabilité face au mode en opposition se discute par une équation de Hill--Mathieu et présente un seuil d'amplitude (exercice 8).



> [!question]- 🔭 Aller plus loin — Master : De $N$ oscillateurs à la corde : limite continue
> Une chaîne de $N$ masses reliées par des ressorts possède $N$ modes ; pour $N\to\infty$ avec $a\to0$ ($L=Na$ fixé), les modes deviennent ceux de la corde vibrante du TD 1 et la relation $\omega_p=2\omega_0\sin(k_pa/2)$ devient $\omega=ck$ (exercice 9 et TD 1, exercice 9).



> [!question]- 🔭 Aller plus loin — Master : Spectroscopie de vibration
> Les nombres d'onde de vibration d'une molécule (infrarouge, Raman) donnent directement les constantes de raideur des liaisons ; les modes normaux d'une molécule polyatomique (par exemple $\mathrm{CO_2}$, $\mathrm{H_2O}$) se calculent par la diagonalisation de $M^{-1}K$ présentée ici.


