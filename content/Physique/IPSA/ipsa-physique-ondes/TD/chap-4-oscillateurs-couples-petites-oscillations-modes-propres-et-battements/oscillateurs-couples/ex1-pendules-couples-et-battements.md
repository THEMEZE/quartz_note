---
title: "Exercice 1 — Pendules couplés et battements"
tags:
  - td
  - chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/index|⬅ Retour]] · <a href="/pdfs/td4_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 1. Pendules couplés et battements

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 75 min · Type : Problème de synthèse guidé*

Deux pendules simples identiques, de même longueur $\ell$, de même masse $m$, sont suspendus en deux points $I_1$ et $I_2$ situés dans un même plan horizontal et distants de $d$. Les deux masses, toutes deux égales à $m$, sont situées en $P_1$ et $P_2$ et sont reliées par un ressort de raideur $k$ et de longueur $d$ : lorsque la distance $P_1P_2$ est $(d\pm\epsilon)$, la force de rappel du ressort a pour module $k\epsilon$. On n'étudie que les oscillations de faible amplitude de ces pendules, autour de leurs positions d'équilibre respectives $O_1$ et $O_2$ et l'on désigne par $x_1$ et $x_2$ les petits déplacements de $P_1$ et $P_2$ sur l'axe horizontal $O_1O_2x$.

> [!question]+ 🎣 Accroche
> **Deux pendules, un ressort : combien de fréquences ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *Deux pendules identiques suspendus côte à côte sont reliés par un ressort. Sans ressort, chacun oscille à la période $T_0=2\pi\sqrt{\ell/g}$. **Avec le ressort, quelle est la période d'un pendule quand on écarte les deux de la même façon du même côté ? Et quand on les écarte symétriquement de part et d'autre ?** Qu'observe-t-on si l'on n'écarte qu'un seul des deux ?*
>
> **Idée clé : deux pendules couplés ont deux mouvements « purs », chacun avec sa fréquence.** Quand les deux masses bougent exactement ensemble, le ressort garde sa longueur et ne joue aucun rôle : $\omega_1=\sqrt{g/\ell}$. Quand elles bougent en sens opposés, le ressort travaille et ajoute de la raideur : $\omega_2=\sqrt{g/\ell+2k/m}>\omega_1$. Tout autre mouvement est une superposition des deux, ce qui produit des battements et un transfert périodique d'énergie d'un pendule à l'autre.


> [!abstract]+ 📚 Prérequis
> **Pendule simple et base polaire**
>
> Savoir que, pour un point matériel relié à un point fixe par un fil de longueur $\ell$, $\vec v=\ell\dot\alpha\,\vec e_\alpha$ et $\vec a=\ell\ddot\alpha\,\vec e_\alpha-\ell\dot\alpha^2\vec e_r$ ; savoir que la tension du fil est dirigée selon $-\vec e_r$ et ne travaille pas.
>
> **Loi de Hooke et allongement algébrique**
>
> Un ressort de raideur $k$ et de longueur à vide $\ell_0$, de longueur $\ell_s$, exerce sur chacune de ses extrémités une force $k(\ell_s-\ell_0)$ dirigée vers l'autre extrémité si $\ell_s>\ell_0$ (ressort étiré) et en sens inverse si $\ell_s<\ell_0$. Les deux forces sont opposées (troisième loi de Newton).
>
> **Développements limités de $\sin$ et $\cos$**
>
> $\sin\alpha=\alpha-\alpha^3/6+\dots$ et $\cos\alpha=1-\alpha^2/2+\dots$ ; savoir majorer l'erreur par le premier terme négligé (voir le point de cours du TD).
>
> **Équation $\ddot y+\omega^2y=0$**
>
> Solution générale $y=A\cos(\omega t+\varphi)$, deux constantes d'intégration fixées par $y(0)$ et $\dot y(0)$.
>
> **Formules de somme et de produit**
>
> $\cos p-\cos q=-2\sin\dfrac{p+q}2\sin\dfrac{p-q}2$ et $\cos p+\cos q=2\cos\dfrac{p+q}2\cos\dfrac{p-q}2$.


> [!info]+ 🎯 Objectifs
> **Mettre en équation sans rien deviner**
>
> Savoir construire la base locale d'un pendule, projeter poids, tension et force de rappel du ressort en justifiant chaque signe par un produit scalaire, et obtenir les *équations exactes* du mouvement des deux masses.
>
> **Comprendre et utiliser l'approximation des petits angles**
>
> Savoir identifier dans les équations exactes les termes linéaires, non linéaires et de couplage ; savoir expliquer physiquement et mathématiquement pourquoi l'on peut linéariser simultanément les deux équations ; savoir estimer l'erreur commise.
>
> **Découpler deux équations couplées de deux façons**
>
> Savoir faire apparaître le mode en phase et le mode en opposition par somme et différence, comprendre pourquoi cela marche (symétrie d'échange), puis retrouver le même résultat par la matrice de raideur et les valeurs propres.
>
> **Interpréter modes propres et battements**
>
> Savoir décrire le mouvement des deux masses dans chaque mode, calculer les pulsations propres, résoudre le problème avec conditions initiales, mettre la solution sous forme de battements et interpréter l'échange d'énergie.


> [!note]+ 📖 Point de cours
> **Fiche de synthèse : équations exactes, équations linéarisées**
>
> Avec $x_i=\ell\sin\alpha_i$ exactement, $u=d+x_2-x_1$, $v=\ell(\cos\alpha_1-\cos\alpha_2)$ et $\ell_s=\sqrt{u^2+v^2}$ :
> $$
> \begin{array}{l|l}
>   \textbf{Exact} & \textbf{Linéarisé (ordre 1)}\\
>   \hline
>   m\ell\ddot\alpha_1=-mg\sin\alpha_1+k\dfrac{\ell_s-d}{\ell_s}(u\cos\alpha_1+v\sin\alpha_1) & m\ddot x_1=-\dfrac{mg}\ell x_1+k(x_2-x_1)\\[2mm]
>   m\ell\ddot\alpha_2=-mg\sin\alpha_2-k\dfrac{\ell_s-d}{\ell_s}(u\cos\alpha_2+v\sin\alpha_2) & m\ddot x_2=-\dfrac{mg}\ell x_2-k(x_2-x_1)
> \end{array}
> $$
> Pulsations propres : $\omega_1=\sqrt{g/\ell}$ (en phase) et $\omega_2=\sqrt{g/\ell+2k/m}$ (en opposition de phase) ; coordonnées normales $S=x_1+x_2$ et $D=x_1-x_2$.


> [!note]- 🧮 Outils mathématiques
> **Produit scalaire et coordonnées d'un vecteur unitaire**
>
> $\vec e_r\cdot\vec e_x=\cos\big(\tfrac\pi2-\alpha\big)=\sin\alpha$, $\vec e_r\cdot\vec e_y=\cos(\pi-\alpha)=-\cos\alpha$ ; coordonnée de $\vec F$ sur $\vec e_\alpha$ : $\vec F\cdot\vec e_\alpha$.
>
> **Développement limité de $\sqrt{u^2+v^2}$**
>
> Pour $|v|\ll u$ : $\sqrt{u^2+v^2}=u\sqrt{1+v^2/u^2}\simeq u+\dfrac{v^2}{2u}$. Le terme correctif est d'ordre $4$ si $v$ est d'ordre $2$.
>
> **Développements limités de $\sin$ et $\cos$**
>
> $\sin\alpha\simeq\alpha-\alpha^3/6$ ; $\cos\alpha\simeq1-\alpha^2/2$ ; erreurs relatives $\alpha^2/6$ et $\alpha^2/2$ à l'ordre $0$ en $\alpha$.
>
> **Somme et différence de deux équations**
>
> Pour des coefficients $a_{ij}$ avec $a_{11}=a_{22}$ et $a_{12}=a_{21}$ : $(1)+(2)$ et $(1)-(2)$ éliminent le couplage.
>
> **Solution de $\ddot y+\omega^2y=0$ sous trois formes**
>
> $y=C\cos\omega t+D\sin\omega t=A\cos(\omega t+\varphi)=\mathrm{Re}\big[\underline Ae^{i\omega t}\big]$ ; $A=\sqrt{C^2+D^2}$, $\tan\varphi=-D/C$.
>
> **Somme de deux cosinus**
>
> $\cos p\pm\cos q$ se factorise en produit ; permet d'identifier porteuse et enveloppe.


**q1.** Écrire les équations différentielles des mouvements de $P_1$ et de $P_2$ et rechercher un changement de variables permettant d'obtenir deux équations différentielles indépendantes.

> [!tip]- 💡 Coup de pouce
> **Choisir la projection qui élimine l'inconnue**
>
> Chaque fil exerce sur sa masse une force de tension inconnue. Pour ne pas avoir à la déterminer, projetez le principe fondamental sur la direction *perpendiculaire au fil*. Dessinez cette direction pour une masse écartée d'un angle $\alpha>0$ et calculez ses coordonnées dans la base cartésienne à l'aide de produits scalaires.
>
> **Géométrie du ressort**
>
> L'allongement algébrique du ressort est $\ell_s-d$. La composante horizontale de $\overrightarrow{P_1P_2}$ vaut *exactement* $d+x_2-x_1$ ; sa composante verticale est d'ordre $2$ en les angles. Que devient alors la force du ressort projetée sur la tangente, à l'ordre $1$ ?
>
> **Découplage**
>
> Écrivez les deux équations linéarisées l'une sous l'autre : les coefficients de $x_1$ dans la première et de $x_2$ dans la seconde sont-ils égaux ? Que se passe-t-il quand on additionne les équations ? quand on les soustrait ? Pourquoi la somme est-elle liée au centre de masse des deux pendules ?


> [!success]- ✅ Correction
> **Équations exactes**
>
> Avec $x_i=\ell\sin\alpha_i$, $u=d+x_2-x_1$, $v=\ell(\cos\alpha_1-\cos\alpha_2)$, $\ell_s=\sqrt{u^2+v^2}$ :
> $$m\ell\ddot\alpha_1=-mg\sin\alpha_1+k\frac{\ell_s-d}{\ell_s}(u\cos\alpha_1+v\sin\alpha_1),\qquad m\ell\ddot\alpha_2=-mg\sin\alpha_2-k\frac{\ell_s-d}{\ell_s}(u\cos\alpha_2+v\sin\alpha_2).$$
>
> **Équations linéarisées**
>
> $$\ddot x_1+\Big(\frac g\ell+\frac km\Big)x_1-\frac kmx_2=0,\qquad \ddot x_2+\Big(\frac g\ell+\frac km\Big)x_2-\frac kmx_1=0.$$
>
> **Changement de variables**
>
> $S=x_1+x_2$ et $D=x_1-x_2$ : $\ \ddot S+\dfrac g\ell S=0$ et $\ddot D+\Big(\dfrac g\ell+\dfrac{2k}m\Big)D=0$.


> [!example]- 📝 Solution détaillée
> **1. Comprendre la situation physique**
>
> Chaque pendule est soumis à deux origines de rappel : la pesanteur, propre à chaque masse, et le ressort, qui les relie. Sans ressort ($k=0$), les deux pendules sont indépendants et oscillent à la pulsation $\sqrt{g/\ell}$. Le ressort transmet à chaque masse une force qui dépend de la position de l'autre : c'est le *couplage*.
>
> Chaque masse est reliée à son point d'attache par un fil inextensible : elle est contrainte de rester sur un cercle de rayon $\ell$, et sa position est entièrement repérée par *un angle*. Le système possède donc deux degrés de liberté, $\alpha_1$ et $\alpha_2$. La tension du fil est une force de liaison inconnue : la mise en équation consiste à projeter le principe fondamental dans une direction où cette force n'apparaît pas.
>
> **2. Système, référentiel, repère, variables**
>
> **Systèmes** : les points matériels $P_1$, puis $P_2$ (un principe fondamental par masse). **Référentiel** : le laboratoire, supposé galiléen.
>
> **Repère** $(O_1,\vec e_x,\vec e_y)$ : $O_1$ est la position d'équilibre de $P_1$ ; $\vec e_x$ est horizontal, dirigé de $O_1$ vers $O_2$ ; $\vec e_y$ est vertical vers le haut ; $\vec e_z=\vec e_x\wedge\vec e_y$ sort de la figure. Alors $I_1=(0,\ell)$, $I_2=(d,\ell)$ et $O_2=(d,0)$.
>
> **Angles** : $\alpha_i$ est l'angle orienté entre la verticale descendante $-\vec e_y$ et le fil $I_iP_i$, positif lorsque la masse part vers les $x$ positifs. Les deux pendules sont repérés de la même façon : c'est ce qui préserve la symétrie du problème.
>
> **Positions exactes** : $\overrightarrow{I_iP_i}=\ell\,\vec e_{r,i}$ (coordonnées de $\vec e_{r,i}$ à l'étape suivante), donc
> $$P_1=\big(\ell\sin\alpha_1,\ \ell(1-\cos\alpha_1)\big),\qquad P_2=\big(d+\ell\sin\alpha_2,\ \ell(1-\cos\alpha_2)\big).$$
> Le déplacement horizontal de l'énoncé est donc, *exactement*, $x_i=\ell\sin\alpha_i$, et seulement à l'ordre $1$ $x_i\simeq\ell\alpha_i$.
>
> **3. Deux bases : la base cartésienne et la base locale de chaque pendule**
>
> La base cartésienne $(\vec e_x,\vec e_y)$ est fixe : ses vecteurs ne dépendent pas du temps. Pour chaque pendule $i$, on définit une *base locale* liée à l'angle $\alpha_i$ :
>
>
> - $\vec e_{r,i}$ : vecteur unitaire de $I_i$ vers $P_i$, donc le long du fil ;
> - $\vec e_{\alpha,i}$ : vecteur unitaire perpendiculaire au fil, dans le sens des $\alpha_i$ croissants.
>
>
> **Coordonnées par produits scalaires.** Sur le schéma, l'angle entre $\vec e_{r}$ et $\vec e_x$ vaut $\tfrac\pi2-\alpha$ et l'angle entre $\vec e_{r}$ et $\vec e_y$ vaut $\pi-\alpha$. Donc
> $$\vec e_r\cdot\vec e_x=\cos\Big(\frac\pi2-\alpha\Big)=\sin\alpha,\qquad\vec e_r\cdot\vec e_y=\cos(\pi-\alpha)=-\cos\alpha\ \Longrightarrow\ \boxed{\vec e_r=\sin\alpha\,\vec e_x-\cos\alpha\,\vec e_y}.$$
> Le vecteur $\vec e_\alpha$ s'obtient en tournant $\vec e_r$ de $+\pi/2$ (sens des $\alpha$ croissants) : $\boxed{\vec e_\alpha=\cos\alpha\,\vec e_x+\sin\alpha\,\vec e_y}$.
>
> **Vérifications.** $\|\vec e_r\|^2=\sin^2\alpha+\cos^2\alpha=1$, $\vec e_r\cdot\vec e_\alpha=\sin\alpha\cos\alpha-\cos\alpha\sin\alpha=0$ : base orthonormée. Orientation directe : $\vec e_r\wedge\vec e_\alpha=(\sin^2\alpha+\cos^2\alpha)\,\vec e_z=\vec e_z$. Cas limites : pour $\alpha=0$, $\vec e_r=-\vec e_y$ (le fil est vertical, vers le bas, c'est cohérent) et $\vec e_\alpha=\vec e_x$ (augmenter $\alpha$ déplace la masse vers la droite) ; pour $\alpha=\pi/2$, $\vec e_r=\vec e_x$ et $\vec e_\alpha=\vec e_y$.
>
> **Pourquoi cette base varie avec le temps.** Ses vecteurs sont attachés à l'orientation du fil, donc à $\alpha(t)$. En dérivant : $\dfrac{\mathrm d\vec e_r}{\mathrm dt}=\dot\alpha(\cos\alpha\,\vec e_x+\sin\alpha\,\vec e_y)=\dot\alpha\,\vec e_\alpha$ et $\dfrac{\mathrm d\vec e_\alpha}{\mathrm dt}=\dot\alpha(-\sin\alpha\,\vec e_x+\cos\alpha\,\vec e_y)=-\dot\alpha\,\vec e_r$. Il y a *une base locale par pendule* : tant que $\alpha_1\neq\alpha_2$, les deux bases sont différentes.
>
> **4. Vitesse et accélération exactes**
>
> Comme $\overrightarrow{OP_i}=\overrightarrow{OI_i}+\ell\,\vec e_{r,i}$ avec $\overrightarrow{OI_i}$ et $\ell$ constants,
> $$\vec v_i=\ell\dot\alpha_i\,\vec e_{\alpha,i},\qquad\vec a_i=\ell\ddot\alpha_i\,\vec e_{\alpha,i}+\ell\dot\alpha_i\Big(\frac{\mathrm d\vec e_{\alpha,i}}{\mathrm dt}\Big)=\ell\ddot\alpha_i\,\vec e_{\alpha,i}-\ell\dot\alpha_i^2\,\vec e_{r,i}.$$
> Le premier terme est l'accélération tangentielle (variation de la vitesse), le second l'accélération centripète : $-\vec e_r$ pointe vers le point d'attache.
>
> **5. Forces sur $P_1$ et projections justifiées**
>
> **Poids** $m\vec g=-mg\,\vec e_y$. Sa coordonnée tangentielle est $-mg\,\vec e_y\cdot\vec e_{\alpha}=-mg\sin\alpha_1$ (car $\vec e_y\cdot\vec e_\alpha=\sin\alpha_1$) et sa coordonnée radiale $-mg\,\vec e_y\cdot\vec e_r=+mg\cos\alpha_1$. Contrôle du signe : pour $\alpha_1>0$ la masse est à droite de la verticale ; le poids la ramène vers la gauche, c'est-à-dire dans le sens des $\alpha$ décroissants, donc la coordonnée tangentielle est négative.
>
> **Tension du fil** $\vec T_1=-T_1\vec e_{r,1}$ avec $T_1>0$ : le fil tire vers $I_1$. Sa coordonnée tangentielle est $-T_1\,\vec e_r\cdot\vec e_\alpha=0$ : *la tension disparaît de la projection tangentielle*. (La projection radiale la déterminerait, mais nous n'en avons pas besoin.)
>
> **Force du ressort** $\vec F_1$ : voir l'étape suivante, où l'on construit sa géométrie exacte.
>
> **6. Géométrie exacte du ressort**
>
> Le vecteur $\overrightarrow{P_1P_2}=\overrightarrow{OP_2}-\overrightarrow{OP_1}$ s'écrit, d'après les positions de l'étape 2,
> $$\overrightarrow{P_1P_2}=\underbrace{\big[d+\ell(\sin\alpha_2-\sin\alpha_1)\big]}_{u=d+x_2-x_1}\vec e_x+\underbrace{\ell(\cos\alpha_1-\cos\alpha_2)}_{v}\,\vec e_y.$$
> La longueur du ressort est $\ell_s=\sqrt{u^2+v^2}$ et son allongement algébrique est $\ell_s-d$. Le ressort, de longueur à vide $d$, exerce sur $P_1$ la force dirigée vers $P_2$ si $\ell_s>d$ :
> $$\vec F_1=k(\ell_s-d)\frac{\overrightarrow{P_1P_2}}{\ell_s},\qquad\vec F_2=-\vec F_1\ \ \text{(action et réaction).}$$
> Son signe est contrôlé : $\ell_s>d$ (ressort étiré) donne bien une force sur $P_1$ dans le sens de $\overrightarrow{P_1P_2}$.
>
> **Projection tangentielle.** Par produit scalaire avec $\vec e_{\alpha,1}=\cos\alpha_1\vec e_x+\sin\alpha_1\vec e_y$ :
> $$\vec F_1\cdot\vec e_{\alpha,1}=k\,\frac{\ell_s-d}{\ell_s}\big(u\cos\alpha_1+v\sin\alpha_1\big),\qquad\vec F_2\cdot\vec e_{\alpha,2}=-k\,\frac{\ell_s-d}{\ell_s}\big(u\cos\alpha_2+v\sin\alpha_2\big).$$
> **Remarque importante.** La composante horizontale de la longueur du ressort est *exactement* $u=d+x_2-x_1$ : c'est ce qui donnera, après linéarisation, $k(x_2-x_1)$. La composante verticale $v$ est la différence de hauteur des deux masses : d'ordre $2$ en les angles (voir étape 10).
>
> **7. Les équations exactes du mouvement**
>
> Le principe fondamental $m\vec a_i=\sum\vec F$, projeté sur $\vec e_{\alpha,i}$ (la coordonnée tangentielle de $\vec a_i$ est $\ell\ddot\alpha_i$), donne
> $$\boxed{m\ell\,\ddot\alpha_1=-mg\sin\alpha_1+k\,\frac{\ell_s-d}{\ell_s}\big(u\cos\alpha_1+v\sin\alpha_1\big)}$$
> $$\boxed{m\ell\,\ddot\alpha_2=-mg\sin\alpha_2-k\,\frac{\ell_s-d}{\ell_s}\big(u\cos\alpha_2+v\sin\alpha_2\big)}$$
> avec $u=d+\ell(\sin\alpha_2-\sin\alpha_1)$, $v=\ell(\cos\alpha_1-\cos\alpha_2)$, $\ell_s=\sqrt{u^2+v^2}$. Ces deux équations sont *exactes* : aucune approximation n'a été faite, ni sur les angles, ni sur la géométrie. Elles coïncident avec les équations d'Euler--Lagrange du lagrangien $L=\tfrac12m\ell^2(\dot\alpha_1^2+\dot\alpha_2^2)+mg\ell(\cos\alpha_1+\cos\alpha_2)-\tfrac12k(\ell_s-d)^2$ (vérifiable en « Aller plus loin »).
>
> **8. Structure des équations exactes : ce qui est linéaire, non linéaire, couplé**
>
> - **Terme de gravité** $-mg\sin\alpha_i$ : non linéaire en $\alpha_i$, *sans couplage* (ne dépend que de l'angle de la masse $i$).
> - **Terme de ressort** : il dépend à la fois de $\alpha_1$ et de $\alpha_2$ à travers $u$, $v$ et $\ell_s$ : c'est lui qui *couple* les équations ; il contient une racine carrée et des sinus et cosinus, donc il est lui aussi non linéaire.
> - **Couplage non linéaire** : l'équation de $\alpha_1$ contient $\alpha_2$ de façon non linéaire (par $\sin\alpha_2$, $\cos\alpha_2$, $\ell_s$).
>
>
> **Pourquoi ce système est difficile.** C'est un système de deux équations différentielles couplées et non linéaires. Même un pendule simple isolé ne se résout qu'avec des fonctions elliptiques ; ici, avec deux degrés de liberté, il n'existe en général pas de solution analytique (le mouvement peut même devenir chaotique à grande amplitude). On résout donc numériquement, ou l'on linéarise.
>
> **Solutions exactes remarquables.** (i) Si $\alpha_1=\alpha_2=\alpha(t)$, alors $u=d$, $v=0$, $\ell_s=d$ : le ressort garde sa longueur à vide et sa force est nulle ; chaque pendule suit $\ddot\alpha=-(g/\ell)\sin\alpha$ : *le mouvement en phase est une solution exacte, quelle que soit l'amplitude*. (ii) Équilibres : $\alpha_1=\alpha_2=0$ (stable) et $\alpha_1=\alpha_2=\pi$ (pendules renversés, instable) ; ce sont les seuls équilibres *à ressort relâché*. Nous étudions les petites oscillations autour de $(0,0)$.
>
> **9. Pourquoi et comment linéariser : la physique des petits angles**
>
> **Pourquoi s'intéresser à de petites oscillations autour de l'équilibre ?** Autour d'un équilibre stable, une petite perturbation reste petite : le système oscille près de $(0,0)$, et c'est là que l'on peut remplacer les fonctions par leurs développements. De plus, l'énergie potentielle d'un système régulier est, près d'un minimum, une parabole (le terme linéaire disparaît à l'équilibre) : les forces de rappel sont donc proportionnelles aux écarts, quelle que soit leur origine.
>
> **Que signifie « un angle petit » ?** Un angle est petit lorsque $\alpha^2\ll6$ rad$^2$ (termes suivants du sinus négligeables), mais il faut surtout comparer la précision cherchée à $\alpha^2$ : pour $\alpha=0{,}1$ rad ($5{,}7^\circ$), on commet $0{,}17\ \%$ en remplaçant $\sin\alpha$ par $\alpha$ ; pour $0{,}2$ rad ($11^\circ$), $0{,}67\ \%$.
>
> **Pourquoi le déplacement est proportionnel à l'angle.** La masse se déplace sur un arc de cercle. Pour $\alpha$ petit, l'arc $\ell\alpha$ et la corde $2\ell\sin(\alpha/2)$ sont presque confondus : la trajectoire est quasi rectiligne et horizontale, et $x=\ell\sin\alpha\simeq\ell\alpha$. L'élévation $\ell(1-\cos\alpha)\simeq\ell\alpha^2/2$ est du *second ordre* : elle est négligeable devant $x$ (rapport $\alpha/2$).
>
> **Pourquoi les forces de rappel deviennent linéaires.** La coordonnée tangentielle du poids $-mg\sin\alpha\simeq-mg\,x/\ell$ est proportionnelle au déplacement horizontal : la pesanteur joue le rôle d'un ressort de raideur $mg/\ell$. De même la force du ressort réel devient $k(x_2-x_1)$ (voir étape 10).
>
> **Pourquoi les équations deviennent linéaires, et ce que l'on y gagne.** Quand tous les termes sont proportionnels aux $x_i$ ou à leurs dérivées, on a un système linéaire à coefficients constants : le principe de superposition s'applique, les solutions sont des exponentielles ou des sinusoïdes, et le système couplé se ramène à de l'algèbre linéaire (valeurs propres). **Ce que l'on perd** : l'isochronisme ($T$ dépend de l'amplitude : $+0{,}19\ \%$ à $10^\circ$, $+1{,}7\ \%$ à $30^\circ$, $+18\ \%$ à $90^\circ$), les harmoniques du mouvement, les échanges d'énergie entre modes dus aux non-linéarités et d'éventuelles instabilités.
>
> **Pourquoi linéariser les deux équations ensemble.** Les écarts $\alpha_1$ et $\alpha_2$ sont petits *en même temps* (le système entier est près de son équilibre). Un produit comme $\alpha_1\alpha_2$ est d'ordre $2$, de même nature que $\alpha_1^2$ : on le néglige au même titre. Une linéarisation partielle (garder $\sin\alpha_1$ mais pas $\sin\alpha_2$, par exemple) mélangerait les ordres et détruirait la symétrie du système.
>
> **10. Ce que disent les développements limités**
>
> Les développements de Taylor des fonctions qui apparaissent donnent (en ne gardant que les ordres pertinents) :
>
>
> - $\sin\alpha_i=\alpha_i-\dfrac{\alpha_i^3}6+\dots$ : l'écart de $\sin\alpha_i$ à $\alpha_i$ est d'ordre $3$ ; $\cos\alpha_i=1-\dfrac{\alpha_i^2}2+\dots$ : l'écart de $\cos\alpha_i$ à $1$ est d'ordre $2$ ; ces deux fonctions n'ont pas le même ordre dominant parce que le sinus est impair et le cosinus pair.
> - $x_i=\ell\sin\alpha_i=\ell\alpha_i+O(\alpha_i^3)$, donc $\ddot x_i=\ell\ddot\alpha_i\cos\alpha_i-\ell\dot\alpha_i^2\sin\alpha_i=\ell\ddot\alpha_i+O(3)$.
> - **Composante verticale du ressort :** $v=\ell(\cos\alpha_1-\cos\alpha_2)=\dfrac{\ell}2(\alpha_2^2-\alpha_1^2)+O(4)$, d'ordre $2$.
> - **Longueur du ressort :** $\ell_s=\sqrt{u^2+v^2}=u+\dfrac{v^2}{2u}+\dots$, d'où $\ell_s-d=(x_2-x_1)+\dfrac{v^2}{2u}+\dots$ : le terme correctif est d'ordre $4$ (carré d'un ordre $2$) devant $x_2-x_1$ d'ordre $1$ : l'allongement est $x_2-x_1$ à une erreur relative d'ordre $3$.
> - **Facteur de projection :** $\dfrac{u\cos\alpha_1+v\sin\alpha_1}{\ell_s}=\cos\alpha_1+O(3)$.
>
>
> Conséquence : la force du ressort projetée sur la tangente vaut $k(x_2-x_1)\cos\alpha_1+O(4)=k(x_2-x_1)+O(3)$ ; il n'y a *aucun terme quadratique* (les termes non linéaires commencent à l'ordre $3$). Ainsi, jusqu'à l'ordre $3$,
> $$\ddot\alpha_1=-\frac g\ell\sin\alpha_1+\frac km(\sin\alpha_2-\sin\alpha_1)\cos\alpha_1+O(4).$$
>
> **Trois notions à distinguer.** Le **développement limité** est un outil mathématique ; l'**approximation des petits angles** en est l'application au premier ordre à $\sin$ et $\cos$ ; la **linéarisation** est la démarche physique qui consiste à ne garder que le premier ordre dans les équations de mouvement (le second ordre dans l'énergie). On a donc utilisé ici trois développements différents (sinus, cosinus, racine carrée), pas seulement $\sin\alpha\simeq\alpha$.
>
> **11. Équations linéarisées**
>
> On garde l'ordre $1$ en $\alpha_1$, $\alpha_2$ : $\sin\alpha_i\simeq\alpha_i\simeq x_i/\ell$, $\cos\alpha_i\simeq1$, $\ell_s-d\simeq x_2-x_1$, $\ddot x_i\simeq\ell\ddot\alpha_i$. Les équations exactes de l'étape 7 deviennent
> $$m\ddot x_1=-\frac{mg}\ell\,x_1+k(x_2-x_1),\qquad m\ddot x_2=-\frac{mg}\ell\,x_2-k(x_2-x_1).$$
> Interprétation de chaque terme : $-\dfrac{mg}\ell x_i$ est la force de rappel de la pesanteur sur la masse $i$ ; $+k(x_2-x_1)$ sur $P_1$ : si $x_2>x_1$ le ressort est étiré et tire $P_1$ vers la droite ; $-k(x_2-x_1)$ sur $P_2$ : il tire $P_2$ vers la gauche. Les deux forces sont opposées (troisième loi de Newton), ce qui rend le couplage *réciproque*. Sous forme canonique, avec $\omega_0^2=g/\ell$ et $\omega_c^2=k/m$ :
> $$\boxed{\ddot x_1+(\omega_0^2+\omega_c^2)\,x_1-\omega_c^2\,x_2=0},\qquad\boxed{\ddot x_2+(\omega_0^2+\omega_c^2)\,x_2-\omega_c^2\,x_1=0}.$$
>
> **12. Vérifications : dimensions et cas limites**
>
> - **Dimensions** : $[g/\ell]=\mathrm{m\,s^{-2}/m}=\mathrm s^{-2}$ et $[k/m]=\mathrm{N\,m^{-1}/kg}=\mathrm s^{-2}$ : chaque terme est homogène à $[x]\,\mathrm s^{-2}$.
> - $k=0$ : on retrouve deux pendules indépendants $\ddot x_i+\omega_0^2x_i=0$.
> - **Symétrie** : le système est inchangé quand on échange les deux pendules ($x_1\leftrightarrow x_2$) ; la matrice des coefficients est symétrique, conséquence du principe d'action et de réaction.
> - **Cohérence des signes** : si $x_1=x_2$, le couplage $-\omega_c^2(x_2-x_1)$ s'annule (le ressort n'est pas déformé).
>
> **13. Découplage à la manière du physicien : somme et différence**
>
> **Observer les équations.** Les coefficients de $x_1$ (équation 1) et de $x_2$ (équation 2) sont identiques, et les coefficients de couplage sont égaux : le système est symétrique par échange des deux pendules. On en tire de l'information en *additionnant* puis en *soustrayant* les équations.
>
> **Somme** : $\dfrac{\mathrm d^2}{\mathrm dt^2}(x_1+x_2)+(\omega_0^2+\omega_c^2)(x_1+x_2)-\omega_c^2(x_1+x_2)=0$, soit, avec $S=x_1+x_2$ :
> $$\ddot S+\omega_0^2\,S=0.$$
> **Différence** : $\ddot D+(\omega_0^2+\omega_c^2)D+\omega_c^2D=0$, soit, avec $D=x_1-x_2$ :
> $$\ddot D+(\omega_0^2+2\omega_c^2)\,D=0.$$
> Les deux équations sont maintenant *indépendantes* : chacune ne contient qu'une variable. Ce sont deux oscillateurs harmoniques.
>
> **Interprétation physique.** (i) $S/2$ est la position du *centre de masse* des deux pendules. Les forces du ressort sont des forces intérieures, égales et opposées : elles s'annulent dans la somme et le centre de masse n'est soumis qu'à la pesanteur, d'où $\omega_0=\sqrt{g/\ell}$. (ii) $D$ est le mouvement *relatif* : au premier ordre, l'élongation du ressort est $x_2-x_1=-D$, et le ressort agit sur chaque masse avec une force de module $kD$ ; comme $D$ est la différence de deux déplacements, l'effet du ressort sur $D$ est doublé, d'où $\omega_0^2+2\omega_c^2$ (le ressort agit comme une raideur $2k$ sur une « masse réduite » $m/2$). (iii) Le mode $S$ est le mode symétrique (pour l'échange des coordonnées) et $D$ le mode antisymétrique.
>
> **14. Pourquoi cela fonctionne : symétrie et condition nécessaire et suffisante**
>
> Écrivons le système sous la forme $\ddot X=-AX$ avec $X=(x_1,x_2)^{\mathsf T}$ et $A=\begin{pmatrix}a&b\\c&d'\end{pmatrix}$. Les vecteurs $(1,1)$ et $(1,-1)$ sont vecteurs propres de $A$ si et seulement si $A(1,1)^{\mathsf T}=(a+b,c+d')^{\mathsf T}\propto(1,1)^{\mathsf T}$ et $A(1,-1)^{\mathsf T}=(a-b,c-d')^{\mathsf T}\propto(1,-1)^{\mathsf T}$, c'est-à-dire $a+b=c+d'$ et $a-b=d'-c$. En additionnant puis en soustrayant : $a=d'$ et $b=c$. **Le changement $S$, $D$ découple donc si et seulement si les coefficients diagonaux sont égaux et le couplage est réciproque et symétrique.**
>
> Ici $a=d'=\omega_0^2+\omega_c^2$ et $b=c=-\omega_c^2$ : la condition est satisfaite. Physiquement, les deux pendules ont la même masse et la même longueur (diagonale identique) et le ressort exerce des forces égales et opposées (couplage symétrique). Mathématiquement, $A$ commute avec la matrice d'échange $P=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ dont $(1,\pm1)$ sont les vecteurs propres. **La symétrie du système est la raison du découplage.** Si l'on casse la symétrie (masses ou raideurs différentes, exercice 2), $S$ et $D$ ne sont plus découplées.
>
> **15. Découplage à la manière du mathématicien : matrices de masse et de raideur**
>
> **Énergies.** Pour les petits mouvements, l'énergie cinétique est $E_c=\tfrac12m(\dot x_1^2+\dot x_2^2)=\tfrac12\dot X^{\mathsf T}M\dot X$ avec $M=m\begin{pmatrix}1&0\\0&1\end{pmatrix}$, et l'énergie potentielle (pesanteur linéarisée $\tfrac12m\omega_0^2x_i^2$, plus ressort) est
> $$E_p=\tfrac12m\omega_0^2(x_1^2+x_2^2)+\tfrac12k(x_2-x_1)^2=\tfrac12X^{\mathsf T}KX,\qquad K=m\begin{pmatrix}\omega_0^2+\omega_c^2&-\omega_c^2\\-\omega_c^2&\omega_0^2+\omega_c^2\end{pmatrix}.$$
> Le terme $-\omega_c^2$ hors de la diagonale de $K$ *est* le couplage ; les équations du mouvement sont $M\ddot X+KX=0$.
>
> **Recherche d'une solution harmonique.** On pose $X=\mathrm{Re}\big[\underline A\,e^{i\omega t}\big]$ avec $\underline A=(A_1,A_2)^{\mathsf T}$ : $\ddot X=-\omega^2X$, d'où le problème aux valeurs propres généralisé $(K-\omega^2M)\underline A=0$, ici $\big(M^{-1}K-\omega^2I\big)\underline A=0$ puisque $M=mI$ est inversible. Une solution non nulle n'existe que si
> $$\det\begin{pmatrix}\omega_0^2+\omega_c^2-\omega^2&-\omega_c^2\\-\omega_c^2&\omega_0^2+\omega_c^2-\omega^2\end{pmatrix}=(\omega_0^2+\omega_c^2-\omega^2)^2-\omega_c^4=(\omega_0^2-\omega^2)(\omega_0^2+2\omega_c^2-\omega^2)=0,$$
> en utilisant $a^2-b^2=(a-b)(a+b)$. Les valeurs propres sont $\omega_1^2=\omega_0^2$ et $\omega_2^2=\omega_0^2+2\omega_c^2$.
>
> **Vecteurs propres.** Pour $\omega^2=\omega_1^2$ : $\omega_c^2A_1-\omega_c^2A_2=0\Rightarrow A_1=A_2$, vecteur $u_1=(1,1)$. Pour $\omega^2=\omega_2^2$ : $-\omega_c^2A_1-\omega_c^2A_2=0\Rightarrow A_1=-A_2$, vecteur $u_2=(1,-1)$. Ces vecteurs sont orthogonaux ($u_1\cdot u_2=0$), comme le garantit le théorème spectral pour une matrice symétrique.
>
> **Diagonalisation explicite.** Avec $P=\dfrac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ (orthogonale, $P^{-1}=P^{\mathsf T}=P$) : $P^{\mathsf T}KP=m\,\mathrm{diag}(\omega_1^2,\omega_2^2)$. Les coordonnées normales $q_1=(x_1+x_2)/\sqrt2$ et $q_2=(x_1-x_2)/\sqrt2$ sont exactement $S$ et $D$ à un facteur près : la méthode du physicien *était* une diagonalisation, rendue évidente par la symétrie.
>
> **Contrôles.** $\mathrm{tr}\big(M^{-1}K\big)=2(\omega_0^2+\omega_c^2)=\omega_1^2+\omega_2^2$ ; $\det\big(M^{-1}K\big)=(\omega_0^2+\omega_c^2)^2-\omega_c^4=\omega_1^2\omega_2^2$ ; $K$ est définie positive donc $\omega_1^2,\omega_2^2>0$ et l'équilibre est stable.
>
> **16. Comparaison des deux méthodes**
>
> - **Physicien :** repère la symétrie, additionne et soustrait. Hypothèses : diagonale égale, couplage réciproque. Avantages : rapide, interprétation directe (centre de masse, mouvement relatif). Limite : échoue sans symétrie (exercice 2).
> - **Mathématicien :** écrit $M\ddot X+KX=0$ et diagonalise. Hypothèses : aucune sur la symétrie ($K$ et $M$ symétriques, $M>0$ suffisent). Avantages : général, vaut pour $N$ degrés de liberté, fournit les vecteurs propres. Limite : plus abstrait, l'interprétation physique est à reconstruire.
> - **Lien :** quand la symétrie existe, les vecteurs propres sont imposés par elle ($(1,\pm1)$ ici) ; le calcul du déterminant ne fait que retrouver ce que la symétrie donnait gratuitement.


**q2.** Intégrer ces équations pour obtenir la solution générale du mouvement.

> [!tip]- 💡 Coup de pouce
> **Reconnaître les équations**
>
> Les deux équations découplées sont de la forme $\ddot y+\omega^2y=0$. Quelle est la solution générale d'une telle équation ? Combien de constantes d'intégration comporte-t-elle ?
>
> **Écrire la solution**
>
> Écrivez $S(t)$ et $D(t)$ avec une amplitude et une phase chacune, puis revenez à $x_1$ et $x_2$ en utilisant $x_1=(S+D)/2$ et $x_2=(S-D)/2$.


> [!success]- ✅ Correction
> **Solution générale**
>
> $$x_1(t)=A_1\cos(\omega_1t+\varphi_1)+A_2\cos(\omega_2t+\varphi_2),\qquad x_2(t)=A_1\cos(\omega_1t+\varphi_1)-A_2\cos(\omega_2t+\varphi_2),$$
> avec $\omega_1=\sqrt{g/\ell}$, $\omega_2=\sqrt{g/\ell+2k/m}$ et quatre constantes $A_1,A_2,\varphi_1,\varphi_2$ fixées par les conditions initiales.


> [!example]- 📝 Solution détaillée
> **Équation de l'oscillateur harmonique**
>
> On cherche les solutions de $\ddot y+\omega^2y=0$ de la forme $y=e^{rt}$ : $r^2+\omega^2=0$, donc $r=\pm i\omega$ et $y=c_+e^{i\omega t}+c_-e^{-i\omega t}$. Les solutions réelles forment un espace de dimension $2$ engendré par $\cos\omega t$ et $\sin\omega t$ : $y=C\cos\omega t+D'\sin\omega t$, soit encore $y=A\cos(\omega t+\varphi)$ avec $A=\sqrt{C^2+D'^2}$ et $\tan\varphi=-D'/C$. Les deux constantes sont fixées par $y(0)$ et $\dot y(0)$. (Le corrigé de l'établissement écrit par erreur « $y''+ay'=0$ » : c'est $y''+ay=0$.)
>
> **Application à $S$ et $D$**
>
> $$S(t)=2A_1\cos(\omega_1t+\varphi_1),\qquad D(t)=2A_2\cos(\omega_2t+\varphi_2),$$
> avec $\omega_1^2=\dfrac g\ell$ et $\omega_2^2=\dfrac g\ell+\dfrac{2k}m$ (on a choisi la notation $2A_i$ pour que les résultats qui suivent soient simples).
>
> **Retour aux variables $x_1$ et $x_2$**
>
> $$x_1=\frac{S+D}2=A_1\cos(\omega_1t+\varphi_1)+A_2\cos(\omega_2t+\varphi_2),\qquad x_2=\frac{S-D}2=A_1\cos(\omega_1t+\varphi_1)-A_2\cos(\omega_2t+\varphi_2).$$
> **Vérification par substitution** dans la première équation : $\ddot x_1+(\omega_0^2+\omega_c^2)x_1-\omega_c^2x_2=(\omega_0^2-\omega_1^2)A_1\cos(\omega_1t+\varphi_1)+(\omega_0^2+2\omega_c^2-\omega_2^2)A_2\cos(\omega_2t+\varphi_2)=0$. Les quatre constantes correspondent à deux positions et deux vitesses initiales : un système de deux équations du second ordre a une solution qui dépend de quatre constantes.
>
> **Interprétation**
>
> Le mouvement général est la superposition de deux sinusoïdes de pulsations différentes. En général il n'est pas périodique (il l'est si $\omega_2/\omega_1$ est rationnel). Sous forme vectorielle, $X(t)=A_1\cos(\omega_1t+\varphi_1)\begin{pmatrix}1\\1\end{pmatrix}+A_2\cos(\omega_2t+\varphi_2)\begin{pmatrix}1\\-1\end{pmatrix}$ : les deux vecteurs sont les modes propres de la question suivante.


**q3.** Chercher dans quelles conditions les deux pendules peuvent avoir un mouvement purement sinusoïdal de même pulsation. Calculer les deux valeurs, $\omega_1$ et $\omega_2$, des pulsations possibles et dans ces deux cas décrire les mouvements des pendules.

> [!tip]- 💡 Coup de pouce
> **Poser la forme cherchée**
>
> Cherchez $x_1=A_1\cos(\omega t+\varphi)$ et $x_2=A_2\cos(\omega t+\varphi)$ avec la *même* pulsation et la même phase (ou une phase opposée). Reportez dans les équations linéarisées : que devient chaque équation ?
>
> **Résoudre sur les amplitudes**
>
> Vous obtenez deux équations linéaires homogènes en $A_1$ et $A_2$. Additionnez-les et soustrayez-les : pour quelles valeurs de $\omega$ existe-t-il une solution non nulle ?
>
> **Interpréter**
>
> Dans chaque cas, calculez le rapport $A_2/A_1$ et décrivez le mouvement : que fait le ressort ? quelle est la raideur effective ressentie par chaque pendule ?


> [!success]- ✅ Correction
> **Résultat**
>
> Mode en phase ($A_2=A_1$) : $\omega_1=\sqrt{g/\ell}$ ; mode en opposition de phase ($A_2=-A_1$) : $\omega_2=\sqrt{g/\ell+2k/m}$. Les conditions initiales doivent être proportionnelles à $(1,1)$ ou à $(1,-1)$ (positions et vitesses).


> [!example]- 📝 Solution détaillée
> **Que signifie « purement sinusoïdal, de même pulsation » ?**
>
> On cherche les mouvements où les deux masses oscillent à une même pulsation $\omega$ avec des amplitudes dans un rapport fixe : ce sont les *modes propres*. On pose en notation complexe $x_j=\underline A_j\,e^{i\omega t}$, $j=1,2$. Les équations sont à coefficients *réels* : on peut choisir les $\underline A_j$ réels à un facteur de phase global près ; les deux pendules sont donc *en phase ou en opposition de phase* (jamais déphasés d'un angle quelconque). On écrit donc $x_j=A_j\cos(\omega t+\varphi)$, avec $A_j$ réel de signe quelconque.
>
> **Système sur les amplitudes**
>
> En reportant dans les équations linéarisées ($\ddot x_j=-\omega^2x_j$) :
> $$(\omega_0^2+\omega_c^2-\omega^2)A_1-\omega_c^2A_2=0,\qquad-\omega_c^2A_1+(\omega_0^2+\omega_c^2-\omega^2)A_2=0.$$
>
> **Méthode du physicien : somme et différence**
>
> En additionnant : $(\omega_0^2-\omega^2)(A_1+A_2)=0$. En soustrayant : $(\omega_0^2+2\omega_c^2-\omega^2)(A_1-A_2)=0$. Une solution non nulle exige $A_1+A_2\neq0$ ou $A_1-A_2\neq0$.
>
>
> - Si $A_1+A_2\neq0$ : $\omega^2=\omega_0^2$, et la seconde relation impose alors $(2\omega_c^2)(A_1-A_2)=0$, donc $A_1=A_2$ (car $k\neq0$).
> - Si $A_1-A_2\neq0$ : $\omega^2=\omega_0^2+2\omega_c^2$, et la première relation impose $A_1+A_2=0$.
>
>
> Les deux cas ne peuvent pas coexister puisque $\omega_0^2\neq\omega_0^2+2\omega_c^2$. Il y a donc exactement deux modes.
>
> **Méthode du mathématicien : déterminant**
>
> Le système homogène a une solution non nulle si et seulement si son déterminant est nul : $(\omega_0^2+\omega_c^2-\omega^2)^2-\omega_c^4=(\omega_0^2-\omega^2)(\omega_0^2+2\omega_c^2-\omega^2)=0$. On retrouve les deux pulsations $\omega_1=\omega_0=\sqrt{g/\ell}$ et $\omega_2=\sqrt{g/\ell+2k/m}$, avec les vecteurs propres $(1,1)$ et $(1,-1)$. La factorisation par $a^2-b^2$ montre que la symétrie de la matrice rend le calcul immédiat. (Le corrigé de l'établissement écrit « $\omega=g/\ell+k/m\mp k/m$ » : il manque le carré, c'est $\omega^2=g/\ell+k/m\mp k/m$.)
>
> **Premier mode : les deux pendules en phase**
>
> $x_1=x_2=A\cos(\omega_1t+\varphi)$, $\omega_1=\sqrt{g/\ell}$. L'élongation du ressort $x_2-x_1$ est nulle à chaque instant (et même exactement, voir l'étape 8 de la première question) : le ressort ne travaille pas, c'est comme s'il n'était pas là. Chaque pendule oscille à sa pulsation propre sans couplage. L'énergie du mode est entièrement gravitationnelle et cinétique.
>
> **Deuxième mode : les deux pendules en opposition de phase**
>
> $x_1=-x_2=A\cos(\omega_2t+\varphi)$. Le ressort est étiré quand les masses s'écartent et comprimé quand elles se rapprochent ; son milieu reste immobile par symétrie. Chaque moitié du ressort, de longueur $d/2$, a une raideur $2k$ (deux ressorts en série d'égale raideur $K$ ont la raideur $K/2$, donc $K/2=k$ soit $K=2k$). Chaque pendule est donc soumis à la pesanteur et à un ressort de raideur $2k$ fixé à un point immobile : $\omega_2^2=\dfrac g\ell+\dfrac{2k}m$.
>
> **Vérification énergétique (quotient de Rayleigh).** Avec $x_1=-x_2=A\cos\omega t$ : $E_{c,\max}=\tfrac12m\omega^2(2A^2)=m\omega^2A^2$ et $E_{p,\max}=\tfrac12m\omega_0^2(2A^2)+\tfrac12k(2A)^2=(m\omega_0^2+2k)A^2$. L'égalité $E_{c,\max}=E_{p,\max}$ donne $\omega^2=\omega_0^2+2k/m$ : cohérent.
>
> **Pourquoi deux fréquences, et pourquoi $\omega_2>\omega_1$ ?**
>
> Pour $k=0$, les deux « modes » ont la même pulsation $\omega_0$ : n'importe quel mouvement est alors sinusoïdal à $\omega_0$ (on dit que la fréquence est *dégénérée*). Le couplage lève cette dégénérescence : le ressort ne joue aucun rôle dans le mode en phase, mais il ajoute de la raideur dans le mode en opposition (il est déformé). Un rappel supplémentaire ne peut qu'augmenter la fréquence : $\omega_2>\omega_1$. Un système de $N$ degrés de liberté possède $N$ modes ; ici $N=2$.
>
> **Conditions initiales pour un mouvement purement sinusoïdal**
>
> Un mouvement purement sinusoïdal à $\omega_1$ (ou $\omega_2$) exige que le vecteur des positions *et* celui des vitesses initiales soient proportionnels à $(1,1)$ (ou $(1,-1)$). Par exemple : lâcher sans vitesse les deux pendules après les avoir écartés du même côté de la même quantité $\to$ mode $\omega_1$ ; de part et d'autre de la même quantité $\to$ mode $\omega_2$. Toute autre condition initiale excite les deux modes.


**q4.** On donne les conditions initiales suivantes : pour $t=0$, $x_1=0$, $v_1=0$, $x_2=a$, $v_2=0$.
Quel est alors le mouvement des pendules ? Calculer la période des battements.

> [!tip]- 💡 Coup de pouce
> **Utiliser les bonnes variables**
>
> Écrivez les conditions initiales en termes de $S=x_1+x_2$ et $D=x_1-x_2$ : valeurs et dérivées à $t=0$. Chaque oscillateur découplé est alors immédiat, sans résoudre un système à quatre inconnues.
>
> **Transformer la somme de cosinus en produit**
>
> Vous obtenez $x_1=\tfrac a2(\cos\omega_1t-\cos\omega_2t)$ et $x_2=\tfrac a2(\cos\omega_1t+\cos\omega_2t)$. Utilisez les formules de somme et de produit pour faire apparaître la demi-somme et la demi-différence des pulsations.
>
> **Période des battements**
>
> La période des battements est l'intervalle de temps entre deux annulations successives de l'enveloppe d'un même pendule. Exprimez-la avec $\omega_2-\omega_1$, puis en couplage faible avec $k/m$ et $\omega_1$.


> [!success]- ✅ Correction
> **Mouvement**
>
> $$x_1=\frac a2(\cos\omega_1t-\cos\omega_2t)=a\sin\frac{\omega_2-\omega_1}2t\,\sin\frac{\omega_1+\omega_2}2t,\qquad x_2=\frac a2(\cos\omega_1t+\cos\omega_2t)=a\cos\frac{\omega_2-\omega_1}2t\,\cos\frac{\omega_1+\omega_2}2t.$$
>
> **Période des battements**
>
> $$T_b=\frac{2\pi}{\omega_2-\omega_1}\ \simeq\ \frac{2\pi\,\omega_1}{k/m}\quad\text{(couplage faible, }k/m\ll g/\ell).$$


> [!example]- 📝 Solution détaillée
> **Conditions initiales sur $S$ et $D$**
>
> À $t=0$ : $S(0)=x_1(0)+x_2(0)=a$, $\dot S(0)=0$, $D(0)=x_1(0)-x_2(0)=-a$, $\dot D(0)=0$. Pour $\ddot y+\omega^2y=0$ avec $y(0)=y_0$ et $\dot y(0)=0$, la solution est $y_0\cos\omega t$. Donc
> $$S(t)=a\cos\omega_1t,\qquad D(t)=-a\cos\omega_2t.$$
> Cette méthode évite le système de quatre équations à quatre inconnues ($A_1,A_2,\varphi_1,\varphi_2$) : le découplage réduit le problème à deux conditions initiales par oscillateur.
>
> **Retour à $x_1$ et $x_2$**
>
> $$x_1=\frac{S+D}2=\frac a2\big(\cos\omega_1t-\cos\omega_2t\big),\qquad x_2=\frac{S-D}2=\frac a2\big(\cos\omega_1t+\cos\omega_2t\big).$$
> Vérification : $x_1(0)=0$, $x_2(0)=a$, et les vitesses $\dot x_{1,2}(0)=0$ car les sinus s'annulent. (On retrouve le corrigé de l'établissement, obtenu par résolution de quatre équations.)
>
> **Mise sous forme de battements**
>
> On utilise $\cos p-\cos q=-2\sin\dfrac{p+q}2\sin\dfrac{p-q}2$ et $\cos p+\cos q=2\cos\dfrac{p+q}2\cos\dfrac{p-q}2$ avec $p=\omega_1t$, $q=\omega_2t$. On pose $\Omega_0=\dfrac{\omega_1+\omega_2}2$ (pulsation moyenne) et $\Omega_m=\dfrac{\omega_2-\omega_1}2$ (pulsation de modulation) :
> $$\boxed{x_1=a\sin(\Omega_mt)\sin(\Omega_0t)},\qquad\boxed{x_2=a\cos(\Omega_mt)\cos(\Omega_0t)}.$$
>
> **Interprétation : porteuse, enveloppe, échange d'énergie**
>
> Si les pulsations sont proches ($\omega_2-\omega_1\ll\omega_1+\omega_2$, c'est-à-dire $\Omega_m\ll\Omega_0$), chaque pendule oscille à la pulsation rapide $\Omega_0$ avec une amplitude qui varie lentement : $a|\sin\Omega_mt|$ pour $P_1$ et $a|\cos\Omega_mt|$ pour $P_2$. À $t=0$, $P_2$ oscille seul avec l'amplitude $a$ ; son amplitude diminue pendant que celle de $P_1$ augmente ; quand $\Omega_mt=\pi/2$, $P_2$ est arrêté et $P_1$ a l'amplitude $a$ : l'énergie a été transférée *entièrement*. Comme $\sin^2+\cos^2=1$, la somme des carrés des enveloppes reste $a^2$ : l'énergie (proportionnelle au carré de l'amplitude, en couplage faible) est échangée sans perte.
>
> **Phases.** Les porteuses $\sin\Omega_0t$ (pour $P_1$) et $\cos\Omega_0t$ (pour $P_2$) sont en quadrature : le pendule qui cède l'énergie est en avance de $\pi/2$ sur celui qui la reçoit. À chaque annulation d'une enveloppe, le signe de $\sin\Omega_mt$ (ou $\cos\Omega_mt$) change, et la phase de la porteuse saute de $\pi$.
>
> **Période des battements**
>
> L'enveloppe de $P_1$, $a|\sin\Omega_mt|$, s'annule pour $\Omega_mt=n\pi$, soit $t=n\pi/\Omega_m$ ; l'intervalle entre deux annulations successives est
> $$T_b=\frac\pi{\Omega_m}=\frac{2\pi}{\omega_2-\omega_1}.$$
> C'est aussi la période de l'enveloppe de $P_2$ (zéros en $\Omega_mt=\pi/2+n\pi$, intervalle $\pi/\Omega_m$). Le transfert complet d'un pendule à l'autre dure $T_b/2=\pi/(\omega_2-\omega_1)$. (Le corrigé de l'établissement attribue la valeur $\pi/(\omega_2-\omega_1)$ à $P_2$ comme « période » : c'est la demi-période de transfert, et la période de l'enveloppe de $P_2$ est $2\pi/(\omega_2-\omega_1)$ comme celle de $P_1$.)
>
> **Couplage faible.** Si $\omega_c^2=k/m\ll\omega_0^2$ : $\omega_2=\omega_0\sqrt{1+2\omega_c^2/\omega_0^2}\simeq\omega_0+\omega_c^2/\omega_0$, d'où $\omega_2-\omega_1\simeq\omega_c^2/\omega_0=\dfrac{k}{m\omega_1}$ et
> $$T_b\simeq\frac{2\pi\omega_1}{k/m}=T_0\,\frac{mg}{k\ell}\qquad\Big(T_0=\frac{2\pi}{\omega_1}\Big).$$
> La période des battements est la période propre multipliée par le rapport de la raideur gravitationnelle $mg/\ell$ à la raideur du ressort : plus le ressort est faible, plus l'échange est lent.
>
> **Application numérique illustrative et validité**
>
> (Données choisies pour illustrer, l'énoncé n'en fournit pas.) Pour $\ell=1{,}00$ m, $m=200$ g, $k=0{,}10\ \mathrm{N\cdot m^{-1}}$ : $\omega_1=3{,}13\ \mathrm{rad\cdot s^{-1}}$ ($T_0=2{,}0$ s), $\omega_c^2=0{,}50\ \mathrm{s^{-2}}$, $\omega_2=3{,}29\ \mathrm{rad\cdot s^{-1}}$, $\omega_2-\omega_1=0{,}156\ \mathrm{rad\cdot s^{-1}}$ et $T_b=40$ s, soit vingt périodes propres avant le retour de l'énergie. L'approximation $T_b\simeq2\pi\omega_1/\omega_c^2=39$ s est correcte à $2{,}4\ \%$.
>
> **Validité.** Les résultats sont valables à l'ordre $1$ : l'amplitude $a$ doit rester petite devant $\ell$ (angles $\lesssim0{,}2$ rad). La factorisation en produit est exacte pour toutes pulsations ; l'interprétation en « enveloppe lente » exige $\omega_2-\omega_1\ll\omega_1+\omega_2$, soit un couplage faible. Pour un couplage fort, l'échange d'énergie existe toujours, mais la période de battement $T_b$ n'est plus grande devant la période $T_0$ des oscillations rapides : il n'y a plus de séparation d'échelles et la notion d'enveloppe perd son sens.


> [!note]- 🔗 Liens avec d'autres disciplines
> **Électrocinétique**
>
> Deux circuits $LC$ identiques couplés par un condensateur ou une inductance mutuelle ont les mêmes équations ; les modes en phase et en opposition correspondent aux deux fréquences de résonance du circuit couplé.
>
> **Mécanique quantique**
>
> Deux niveaux couplés (molécule d'ammoniac) : états symétrique et antisymétrique, séparés par $2\hbar\Omega$, et oscillations entre les états localisés.
>
> **Musique**
>
> Le battement entre deux cordes quasi unisson est utilisé pour accorder un instrument : la fréquence de battement vaut $|f_2-f_1|$.
>
> **Chimie**
>
> La molécule d'eau possède un mode d'élongation symétrique et un mode antisymétrique de fréquences voisines, exactement comme les deux modes de ce couplage.


> [!question]- 🔭 Aller plus loin — Licence : Énergie : qui contient quoi ?
> Vérifier que l'énergie totale $E=\tfrac12m(\dot x_1^2+\dot x_2^2)+\tfrac12m\omega_1^2(x_1^2+x_2^2)+\tfrac12k(x_2-x_1)^2$ est conservée, qu'elle se décompose en deux énergies de modes indépendantes, et que l'énergie du ressort ne dépasse jamais la fraction $\omega_c^2/(\omega_1^2+\omega_c^2)$ de $E$ pour les conditions initiales de la question 4 (voir l'exercice 5).


> [!question]- 🔭 Aller plus loin — Licence : Formalisme de Lagrange
> Écrire $L=\tfrac12m\ell^2(\dot\alpha_1^2+\dot\alpha_2^2)+mg\ell(\cos\alpha_1+\cos\alpha_2)-\tfrac12k(\ell_s-d)^2$ et retrouver les équations exactes de l'étape 7 par Euler--Lagrange ; la hessienne de $-L$ en $(0,0)$ est la matrice de raideur $K$ en variables angulaires.


> [!question]- 🔭 Aller plus loin — Master : Que reste-t-il du mode en phase à grande amplitude ?
> Pour $\alpha_1=\alpha_2$ le ressort garde exactement sa longueur $d$ : le mode en phase est solution des équations *exactes* pour toute amplitude (c'est un pendule simple non linéaire). Le mode en opposition se réduit à un problème à un degré de liberté. La stabilité du mode en phase face à une perturbation en opposition présente un seuil d'amplitude (exercice 8).


> [!question]- 🔭 Aller plus loin — Master : Généralisation à $N$ pendules
> $N$ pendules identiques couplés en chaîne par des ressorts possèdent $N$ modes dont les pulsations sont $\omega_p^2=g/\ell+(4k/m)\sin^2\!\big(p\pi/2(N+1)\big)$ (extrémités libres de se déplacer : voir l'exercice 9 pour la version périodique).


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex3-oscillations-libres-et-forcees-d-un-couplage-pendule-chariot|Exercice 3 — Oscillations libres et forcées d'un couplage pendule-chariot]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex5-complement-niveau-1-cpge-pendules-couples-par-un-ressort-attache-a-mi-hauteur|Exercice 5 — Complément (niveau 1, CPGE) : pendules couplés par un ressort attaché à mi-hauteur]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex8-complement-niveau-3-ens-modes-non-lineaires-de-deux-pendules-couples-stabilite-et-instabilite-parametrique|Exercice 8 — Complément (niveau 3, ENS) : modes non linéaires de deux pendules couplés, stabilité et instabilité paramétrique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex2-couplage-de-deux-oscillateurs-harmoniques-dissymetriques|Exercice 2 — Couplage de deux oscillateurs harmoniques dissymétriques]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex6-complement-niveau-2-ambitieux-trois-masses-quatre-ressorts-diagonalisation-et-perturbation|Exercice 6 — Complément (niveau 2, ambitieux) : trois masses, quatre ressorts, diagonalisation et perturbation]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex7-complement-niveau-2-ambitieux-oscillateurs-desaccordes-anticroisement-et-transfert-d-energie|Exercice 7 — Complément (niveau 2, ambitieux) : oscillateurs désaccordés, anticroisement et transfert d'énergie]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex9-complement-niveau-3-ens-anneau-de-n-oscillateurs-modes-de-fourier-et-propagation-du-signal|Exercice 9 — Complément (niveau 3, ENS) : anneau de N oscillateurs, modes de Fourier et propagation du signal]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex4-frequence-propre-d-une-molecule-diatomique|Exercice 4 — Fréquence propre d'une molécule diatomique]]

