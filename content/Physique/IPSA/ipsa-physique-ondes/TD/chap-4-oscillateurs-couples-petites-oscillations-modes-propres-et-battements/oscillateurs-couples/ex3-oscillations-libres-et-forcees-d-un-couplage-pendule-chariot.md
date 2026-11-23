---
title: "Exercice 3 — Oscillations libres et forcées d'un couplage pendule-chariot"
tags:
  - td
  - chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/index|⬅ Retour]] · <a href="/pdfs/td4_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 3. Oscillations libres et forcées d'un couplage pendule-chariot

*Difficulté ●●●●○ · ⏱ 60 min · Type : Approfondissement, problème guidé*

On considère un pendule simple de longueur $\ell=OA$ et de masse $m$ supposée ponctuelle au point $A$, couplé au système oscillant constitué du chariot de masse $m$ et du ressort de raideur $k$, dont l'extrémité $O'$ est fixée. Le ressort qui est responsable du couplage est horizontal et de raideur $k_c$. L'extrémité $O$ du pendule est fixée. À l'équilibre, le pendule est vertical et les deux ressorts sont non déformés. On pose $\omega_1=\sqrt{\dfrac km}$, $\omega_2=\sqrt{\dfrac g\ell}$ et $\Omega=\sqrt{\dfrac{k_c}m}$. De plus, on considère que les déplacements $x_1(t)$ du centre de masse $G$ du chariot, et $x_2(t)$, de l'extrémité $A$ du pendule, à partir de leur position d'équilibre respectif, sont suffisamment petits pour admettre que les deux ressorts peuvent être considérés comme horizontaux.

**1\textsuperscript{ère} partie : Oscillations libres et modes propres** (questions $1$ à $3$ de l'énoncé, notées q1 à q3). **2\textsuperscript{ème} partie : Oscillations forcées** (questions $1$ à $3$ de l'énoncé, notées q4 à q6) : l'extrémité $O'$ du ressort de raideur $k$ est maintenant soumise à un déplacement sinusoïdal imposé $x_0'=a_0\cos(\omega t)$.

> [!question]+ 🎣 Accroche
> **Un pendule peut-il immobiliser un chariot ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *Un chariot est relié à un mur par un ressort ; on agite l'extrémité du ressort. Normalement le chariot oscille à la fréquence d'excitation. **Peut-on, en accrochant un pendule au chariot par un second ressort, rendre le chariot parfaitement immobile ?** À quelle fréquence ?*
>
> **Idée clé : à une fréquence bien choisie, le pendule exerce sur le chariot une force exactement opposée à celle de l'excitation.** À la pulsation $\omega^2=g/\ell+k_c/m$ (pulsation propre du pendule retenu par le ressort de couplage seul), la force du ressort de couplage compense la force imposée par l'extrémité $O'$, et le chariot reste immobile alors que le pendule oscille avec l'amplitude $-(k/k_c)a_0$. C'est le principe des amortisseurs à masse accordée.


> [!abstract]+ 📚 Prérequis
> **Pendule simple : tangente et base locale**
>
> Pour un pendule, $\vec e_\theta=\cos\theta\,\vec e_x+\sin\theta\,\vec e_y$ est perpendiculaire au fil ; la projection du principe fondamental sur $\vec e_\theta$ élimine la tension (voir l'exercice 1).
>
> **Exercices 1 et 2**
>
> Équations couplées, modes propres, déterminant, découplage par symétrie ou par diagonalisation.
>
> **Régime sinusoïdal forcé en notation complexe**
>
> $x_j=\mathrm{Re}\big[\underline A_je^{i\omega t}\big]$ ; en régime permanent, tous les éléments oscillent à la pulsation d'excitation ; on résout un système linéaire sur les amplitudes complexes (formules de Cramer).
>
> **Équation bicarrée**
>
> $\omega^4-s\,\omega^2+p=0$ se résout en $\omega^2$ : $\omega^2=\tfrac12\big(s\pm\sqrt{s^2-4p}\big)$.


> [!info]+ 🎯 Objectifs
> **Linéariser un système mixte (translation et rotation)**
>
> Savoir écrire les équations exactes d'un chariot couplé à un pendule, identifier les hypothèses « ressort horizontal » et « petits angles », et les justifier par l'ordre des termes négligés.
>
> **Déterminer pulsations et modes d'un système couplé asymétrique**
>
> Savoir obtenir l'équation bicarrée, ses racines, le rapport des amplitudes $a_2/a_1$ dans chaque mode, et en discuter le signe.
>
> **Résoudre un problème d'oscillations forcées**
>
> Savoir écrire les équations avec second membre, résoudre par les amplitudes complexes, identifier résonances et antirésonance, et calculer la période qui immobilise le chariot.


> [!note]- 🧮 Outils mathématiques
> **Linéarisation de la longueur d'un ressort presque horizontal**
>
> $\ell_s=\sqrt{u^2+h^2}=u+\dfrac{h^2}{2u}+\dots$ avec $h=\ell(1-\cos\theta)=O(\theta^2)$ : le terme correctif est d'ordre $4$.
>
> **Système linéaire $2\times2$ et règle de Cramer**
>
> Pour $\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}X\\Y\end{pmatrix}=\begin{pmatrix}f\\g\end{pmatrix}$ : $X=\dfrac{fd-bg}{ad-bc}$, $Y=\dfrac{ag-fc}{ad-bc}$.
>
> **Équation bicarrée et discriminant**
>
> Discriminant $(\omega_1^2-\omega_2^2)^2+4\Omega^4>0$ : les deux racines en $\omega^2$ sont réelles et distinctes.
>
> **Factorisation du dénominateur**
>
> $\Delta(\omega)=(\omega_1^2+\Omega^2-\omega^2)(\omega_2^2+\Omega^2-\omega^2)-\Omega^4=(\omega'^2-\omega^2)(\omega''^2-\omega^2)$ : les zéros sont les pulsations propres.
>
> **Application numérique**
>
> $\omega_2^2=g/\ell=9{,}81/0{,}66=14{,}86\ \mathrm{s^{-2}}$, $\Omega^2=k_c/m=1/0{,}1=10\ \mathrm{s^{-2}}$ ; $\omega^2=24{,}86$, $\omega=4{,}99\ \mathrm{rad\cdot s^{-1}}$.


**q1.** **(1\textsuperscript{ère} partie, question 1).** Écrire les deux équations différentielles du mouvement en $x_1(t)$ et $x_2(t)$, à l'aide des paramètres $\omega_1=\sqrt{\dfrac km}$, $\omega_2=\sqrt{\dfrac g\ell}$ et $\Omega=\sqrt{\dfrac{k_c}m}$.

> [!tip]- 💡 Coup de pouce
> **Deux systèmes, deux projections**
>
> Le chariot se déplace en translation : le principe fondamental projeté sur $\vec e_x$ suffit. Le pendule tourne : projetez sur la tangente $\vec e_\theta=\cos\theta\,\vec e_x+\sin\theta\,\vec e_y$ pour éliminer la tension du fil.
>
> **Le ressort de couplage**
>
> Calculez l'allongement algébrique de $k_c$ : $\overrightarrow{GA}$ a une composante horizontale $L_c+x_2-x_1$ et une composante verticale $h=\ell(1-\cos\theta)$. De quel ordre est $h$ ? Que devient l'allongement à l'ordre $1$ ?
>
> **Linéariser**
>
> $x_2=\ell\sin\theta\simeq\ell\theta$ ; $\sin\theta\simeq x_2/\ell$. Écrivez chaque équation en $x_1$ et $x_2$ et divisez par $m$.


> [!success]- ✅ Correction
> **Système**
>
> $$m\ddot x_1=-kx_1+k_c(x_2-x_1),\qquad m\ddot x_2=-k_c(x_2-x_1)-\frac{mg}\ell x_2,$$
> soit $\ddot x_1+(\omega_1^2+\Omega^2)x_1=\Omega^2x_2$ et $\ddot x_2+(\omega_2^2+\Omega^2)x_2=\Omega^2x_1$.


> [!example]- 📝 Solution détaillée
> **Système, repère, variables**
>
> Deux systèmes : le chariot $G$ (translation le long de l'axe horizontal $O'x$, variable $x_1$) et la masse $A$ du pendule (variable $\theta$). Référentiel du laboratoire galiléen ; axe $O'x$ vers la droite, $\vec e_y$ vers le haut. Le pendule est repéré par l'angle $\theta$ depuis la verticale descendante, positif vers $+x$ : base locale $\vec e_r=\sin\theta\,\vec e_x-\cos\theta\,\vec e_y$ (de $O$ vers $A$), $\vec e_\theta=\cos\theta\,\vec e_x+\sin\theta\,\vec e_y$ (voir l'exercice 1 pour la construction par produits scalaires). Par rapport à sa position d'équilibre, $A$ a pour coordonnées $\big(\ell\sin\theta,\ \ell(1-\cos\theta)\big)$ : $x_2=\ell\sin\theta$ *exactement*, et $h=\ell(1-\cos\theta)$ est d'ordre $2$.
>
> **Géométrie exacte du ressort de couplage**
>
> Soit $L_c$ la longueur à vide de $k_c$, égale à la distance $GA$ à l'équilibre. Alors $\overrightarrow{GA}=u\,\vec e_x+h\,\vec e_y$ avec $u=L_c+x_2-x_1$ et $\ell_s=\sqrt{u^2+h^2}$ : l'allongement algébrique est $\ell_s-L_c$. Le ressort étiré tire $A$ vers $G$ : $\vec F_A=-k_c(\ell_s-L_c)\,\overrightarrow{GA}/\ell_s$ et $\vec F_G=-\vec F_A$.
>
> **Équations exactes**
>
> - **Chariot** (projection sur $\vec e_x$ ; la composante verticale est équilibrée par le rail) : $m\ddot x_1=-kx_1+k_c(\ell_s-L_c)\dfrac{u}{\ell_s}$.
> - **Pendule** (projection sur $\vec e_\theta$ : le poids donne $-mg\sin\theta$, la tension $0$, le ressort $\vec F_A\cdot\vec e_\theta=-k_c\dfrac{\ell_s-L_c}{\ell_s}(u\cos\theta+h\sin\theta)$) : $m\ell\ddot\theta=-mg\sin\theta-k_c\dfrac{\ell_s-L_c}{\ell_s}(u\cos\theta+h\sin\theta)$.
>
>
> Ces équations sont non linéaires et couplées (comme à l'exercice 1) ; elles sont exactes. Elles ne sont ici *pas* intégrables analytiquement.
>
> **Linéarisation**
>
> On développe à l'ordre $1$ en $x_1,\theta$ : $\ell_s=u+h^2/(2u)+\dots$ avec $h=O(\theta^2)$, donc $\ell_s-L_c=x_2-x_1+O(4)$ ; $u/\ell_s=1+O(4)$ ; $(u\cos\theta+h\sin\theta)/\ell_s=\cos\theta+O(3)=1+O(2)$ ; $\sin\theta\simeq x_2/\ell$ ; $\ddot x_2=\ell\ddot\theta+O(3)$. Les hypothèses de l'énoncé (« ressorts horizontaux ») sont donc cohérentes à l'ordre $1$ : l'inclinaison du ressort est d'ordre $2$ et ne modifie sa force qu'à l'ordre $3$. Les équations linéarisées sont
> $$m\ddot x_1=-kx_1+k_c(x_2-x_1),\qquad m\ddot x_2=-\frac{mg}\ell x_2-k_c(x_2-x_1).$$
> (Le corrigé de l'établissement projette sur $\vec e_x$ la tension $F\simeq mg$ du fil, soit $F\sin\theta\simeq mg\,x_2/\ell$ : c'est correct à l'ordre $1$ car $T=mg+O(\theta^2)$, mais la projection tangentielle évite d'avoir à le justifier.)
>
> **Forme canonique et contrôles**
>
> En divisant par $m$ :
> $$\boxed{\ddot x_1+(\omega_1^2+\Omega^2)\,x_1-\Omega^2x_2=0},\qquad\boxed{\ddot x_2+(\omega_2^2+\Omega^2)\,x_2-\Omega^2x_1=0}.$$
> *Contrôles* : dimensions homogènes ($\mathrm s^{-2}$) ; $\Omega=0$ : chariot sur ressort et pendule indépendants ; les couplages $-\Omega^2$ sont égaux (réciprocité) ; le système n'est symétrique par échange des deux oscillateurs que si $\omega_1=\omega_2$.


**q2.** **(1\textsuperscript{ère} partie, question 2).** Établir l'équation du 4\textsuperscript{ème} degré en $\omega$ dont les solutions sont les pulsations propres $\omega'$ et $\omega''$ de ce système (calcul facultatif des pulsations propres).

> [!tip]- 💡 Coup de pouce
> **Solution harmonique**
>
> Cherchez $x_j=A_j\cos(\omega t+\varphi_j)$ (ou en complexe) : vous obtenez un système homogène en $A_1,A_2$. Quelle condition sur son déterminant ?
>
> **Équation bicarrée**
>
> Le déterminant ne contient que $\omega^2$. Posez $X=\omega^2$ et résolvez le trinôme.


> [!success]- ✅ Correction
> **Équation caractéristique**
>
> $$\omega^4-(\omega_1^2+\omega_2^2+2\Omega^2)\,\omega^2+\omega_1^2\omega_2^2+\Omega^2(\omega_1^2+\omega_2^2)=0,$$
> $$\omega'^2,\omega''^2=\frac12\Big[\omega_1^2+\omega_2^2+2\Omega^2\mp\sqrt{(\omega_1^2-\omega_2^2)^2+4\Omega^4}\Big].$$


> [!example]- 📝 Solution détaillée
> **Système sur les amplitudes et déterminant**
>
> Avec $\ddot x_j=-\omega^2x_j$ :
> $$(\omega_1^2+\Omega^2-\omega^2)A_1-\Omega^2A_2=0,\qquad-\Omega^2A_1+(\omega_2^2+\Omega^2-\omega^2)A_2=0.$$
> La solution $A_1=A_2=0$ correspond à l'équilibre ; une solution non nulle exige
> $$\Delta(\omega)=(\omega_1^2+\Omega^2-\omega^2)(\omega_2^2+\Omega^2-\omega^2)-\Omega^4=0.$$
> En développant : $\omega^4-(\omega_1^2+\omega_2^2+2\Omega^2)\omega^2+\omega_1^2\omega_2^2+\Omega^2(\omega_1^2+\omega_2^2)=0$ (les termes $\Omega^4$ se compensent).
>
> **Pulsations propres**
>
> L'équation est du quatrième degré en $\omega$ mais ne contient que $\omega^2$ : c'est une équation bicarrée. Son discriminant est $(\omega_1^2+\omega_2^2+2\Omega^2)^2-4\big[\omega_1^2\omega_2^2+\Omega^2(\omega_1^2+\omega_2^2)\big]=(\omega_1^2-\omega_2^2)^2+4\Omega^4>0$ : deux racines réelles distinctes en $\omega^2$,
> $$\omega'^2=\tfrac12\Big[\omega_1^2+\omega_2^2+2\Omega^2-\sqrt{(\omega_1^2-\omega_2^2)^2+4\Omega^4}\Big],\qquad\omega''^2=\tfrac12\Big[\omega_1^2+\omega_2^2+2\Omega^2+\sqrt{(\omega_1^2-\omega_2^2)^2+4\Omega^4}\Big].$$
> Elles sont strictement positives (produit $\omega_1^2\omega_2^2+\Omega^2(\omega_1^2+\omega_2^2)>0$ et somme $>0$) : on retient $\omega'>0$ et $\omega''>0$ ; les racines négatives en $\omega$ sont leurs opposées et décrivent les mêmes mouvements. Il y a donc deux modes, pas quatre.
>
> **Formulation matricielle**
>
> $M=mI$, $K=m\begin{pmatrix}\omega_1^2+\Omega^2&-\Omega^2\\-\Omega^2&\omega_2^2+\Omega^2\end{pmatrix}$ et $\det(K-\omega^2M)=m^2\Delta(\omega)$. Ce sont les valeurs propres de la matrice symétrique $M^{-1}K$ : $\omega'^2,\omega''^2=\dfrac{\mathrm{tr}}2\mp\sqrt{\big(\tfrac{a-c}2\big)^2+b^2}$ avec $a-c=\omega_1^2-\omega_2^2$ et $b=-\Omega^2$, ce qui redonne le discriminant ci-dessus.
>
> **Cas limites et anticroisement**
>
> - $\Omega\to0$ : $\omega'^2,\omega''^2\to\omega_1^2,\omega_2^2$ (oscillateurs indépendants).
> - $\omega_1=\omega_2$ : $\omega'^2=\omega_1^2$ et $\omega''^2=\omega_1^2+2\Omega^2$ : on retrouve les deux modes de l'exercice 1 (en phase et en opposition).
> - **Répulsion de niveaux** : $\omega''^2-\omega'^2=\sqrt{(\omega_1^2-\omega_2^2)^2+4\Omega^4}\ge2\Omega^2$ : les pulsations propres ne se croisent jamais, même à l'accord $\omega_1=\omega_2$.


**q3.** **(1\textsuperscript{ère} partie, question 3).** Calculer en fonction de $\Omega$, $\omega_1$ (ou $\omega_2$), $\omega'$ et $\omega''$, le rapport $\dfrac{a_2}{a_1}$ des amplitudes des oscillations de la masse $A$ et du centre de masse $G$ du chariot, pour chacun des deux modes propres du système.

> [!tip]- 💡 Coup de pouce
> **Utiliser une des deux équations**
>
> Reprenez la première équation sur les amplitudes : $(\omega_1^2+\Omega^2-\omega^2)A_1=\Omega^2A_2$. Que vaut $A_2/A_1$ ? Quel est le lien avec la seconde équation ?
>
> **Signe et interprétation**
>
> Comparez $\omega'^2$ et $\omega''^2$ aux nombres $\omega_1^2+\Omega^2$ et $\omega_2^2+\Omega^2$ : en déduire le signe de $a_2/a_1$ pour chaque mode.


> [!success]- ✅ Correction
> **Rapports d'amplitudes**
>
> $$\frac{a_2}{a_1}\Big|_{\omega'}=\frac{\omega_1^2+\Omega^2-\omega'^2}{\Omega^2}=\frac{\Omega^2}{\omega_2^2+\Omega^2-\omega'^2},\qquad\frac{a_2}{a_1}\Big|_{\omega''}=\frac{\omega_1^2+\Omega^2-\omega''^2}{\Omega^2}=\frac{\Omega^2}{\omega_2^2+\Omega^2-\omega''^2}.$$
> Mode bas : en phase ($a_2/a_1>0$) ; mode haut : en opposition de phase ($a_2/a_1<0$).


> [!example]- 📝 Solution détaillée
> **Calcul du rapport**
>
> Pour un mode de pulsation $\omega$, l'une ou l'autre des deux équations de la question 2 donne
> $$\frac{A_2}{A_1}=\frac{\omega_1^2+\Omega^2-\omega^2}{\Omega^2}=\frac{\Omega^2}{\omega_2^2+\Omega^2-\omega^2}.$$
> L'égalité des deux expressions équivaut à $\Delta(\omega)=0$ : c'est la condition de la question 2. Comme $A_2/A_1$ est *réel*, les deux masses oscillent en phase ($a_2/a_1>0$) ou en opposition de phase ($a_2/a_1<0$), avec $a_2/a_1=|A_2/A_1|$ pour le rapport des amplitudes (modules).
>
> **Signe : le mode bas est toujours en phase**
>
> La matrice $M^{-1}K=\begin{pmatrix}\omega_1^2+\Omega^2&-\Omega^2\\-\Omega^2&\omega_2^2+\Omega^2\end{pmatrix}$ a pour valeurs propres $\omega'^2<\omega''^2$. La plus petite valeur propre d'une matrice symétrique est inférieure à chacun de ses éléments diagonaux, et la plus grande leur est supérieure : $\omega'^2<\min(\omega_1^2,\omega_2^2)+\Omega^2$ et $\omega''^2>\max(\omega_1^2,\omega_2^2)+\Omega^2$. Donc $\omega_1^2+\Omega^2-\omega'^2>0$ : $A_2/A_1>0$ pour le mode bas (en phase, aucun nœud) ; $\omega_1^2+\Omega^2-\omega''^2<0$ : $A_2/A_1<0$ pour le mode haut (opposition, un nœud).
>
> **Cas limites**
>
> - $\omega_1=\omega_2$ : $\omega'^2=\omega_1^2$ donne $A_2/A_1=\Omega^2/\Omega^2=+1$ ; $\omega''^2=\omega_1^2+2\Omega^2$ donne $-1$ : modes en phase et en opposition de l'exercice 1.
> - $\Omega\to0$ avec $\omega_1<\omega_2$ : $\omega'\to\omega_1$ et $A_2/A_1\to0$ (le mode bas est celui du chariot seul) ; $\omega''\to\omega_2$ et $|A_2/A_1|\to\infty$ (le mode haut est celui du pendule seul) : les modes se localisent sur un oscillateur.
>
>
> **Interprétation.** Un mode d'un système couplé est « collectif » ; il se rapproche d'un mode d'oscillateur isolé quand le couplage devient petit devant l'écart des pulsations (voir l'angle de mélange à l'exercice 7).


**q4.** **(2\textsuperscript{ème} partie, question 1).** L'extrémité $O'$ du ressort de raideur $k$ est maintenant soumise à un déplacement sinusoïdal imposé $x_0'=a_0\cos(\omega t)$. Écrire les nouvelles équations différentielles en $x_1(t)$ et $x_2(t)$.

> [!tip]- 💡 Coup de pouce
> **Le ressort $k$ a changé**
>
> Quel est maintenant l'allongement algébrique du ressort $k$ ? L'extrémité $O'$ s'est déplacée de $x_0'$ et l'autre extrémité de $x_1$.


> [!success]- ✅ Correction
> **Équations forcées**
>
> $$\ddot x_1+(\omega_1^2+\Omega^2)x_1-\Omega^2x_2=\omega_1^2a_0\cos\omega t,\qquad\ddot x_2+(\omega_2^2+\Omega^2)x_2-\Omega^2x_1=0.$$


> [!example]- 📝 Solution détaillée
> **Nouvel allongement**
>
> La longueur du ressort $k$ est maintenant (position de $G$) $-$ (position de $O'$) ; l'allongement algébrique est $x_1-x_0'$. La force sur le chariot est donc $-k(x_1-x_0')=-kx_1+kx_0'$.
>
> **Équations**
>
> $$m\ddot x_1=-k(x_1-a_0\cos\omega t)+k_c(x_2-x_1),\qquad m\ddot x_2=-k_c(x_2-x_1)-\frac{mg}\ell x_2.$$
> Le pendule ne subit pas directement l'excitation. En divisant par $m$ :
> $$\boxed{\ddot x_1+(\omega_1^2+\Omega^2)x_1-\Omega^2x_2=\omega_1^2a_0\cos\omega t},\qquad\boxed{\ddot x_2+(\omega_2^2+\Omega^2)x_2-\Omega^2x_1=0}.$$
> L'excitation apparaît comme un second membre sur la première équation uniquement. Le système reste linéaire : solution = solution générale du système homogène (régime transitoire, qui s'amortit en présence de frottement) $+$ une solution particulière (régime permanent forcé).


**q5.** **(2\textsuperscript{ème} partie, question 2).** Déterminer les amplitudes complexes des mouvements de $G$ et $A$ en fonction de la pulsation $\omega$ de l'excitation et des paramètres $\Omega$, $\omega_1$ (ou $\omega_2$), $\omega'$ et $\omega''$.

> [!tip]- 💡 Coup de pouce
> **Régime forcé permanent**
>
> En régime permanent, tous les éléments oscillent à la pulsation $\omega$ de l'excitation : $x_j=\mathrm{Re}\big[\underline A_je^{i\omega t}\big]$. Reportez dans les équations et obtenez un système linéaire non homogène sur $\underline A_1,\underline A_2$.
>
> **Résolution**
>
> Résolvez par les formules de Cramer, puis factorisez le dénominateur en utilisant les pulsations propres.


> [!success]- ✅ Correction
> **Amplitudes complexes**
>
> $$\underline A_1=a_0\frac{\omega_1^2(\omega_2^2+\Omega^2-\omega^2)}{(\omega'^2-\omega^2)(\omega''^2-\omega^2)},\qquad\underline A_2=a_0\frac{\omega_1^2\Omega^2}{(\omega'^2-\omega^2)(\omega''^2-\omega^2)}.$$


> [!example]- 📝 Solution détaillée
> **Système sur les amplitudes complexes**
>
> Avec $\ddot x_j\to-\omega^2\underline A_j$ et le second membre $\omega_1^2a_0$ (amplitude complexe de $\omega_1^2a_0\cos\omega t$) :
> $$\begin{pmatrix}\omega_1^2+\Omega^2-\omega^2&-\Omega^2\\-\Omega^2&\omega_2^2+\Omega^2-\omega^2\end{pmatrix}\begin{pmatrix}\underline A_1\\\underline A_2\end{pmatrix}=\begin{pmatrix}\omega_1^2a_0\\0\end{pmatrix}.$$
> Le déterminant est $\Delta(\omega)$ de la question 2, non nul tant que $\omega\neq\omega',\omega''$ : le système a alors une solution unique (la matrice $K-\omega^2M$ est inversible).
>
> **Formules de Cramer**
>
> $$\underline A_1=\frac{\omega_1^2a_0(\omega_2^2+\Omega^2-\omega^2)-(-\Omega^2)\cdot0}{\Delta(\omega)}=a_0\frac{\omega_1^2(\omega_2^2+\Omega^2-\omega^2)}{\Delta(\omega)},\qquad\underline A_2=\frac{(\omega_1^2+\Omega^2-\omega^2)\cdot0+\Omega^2\omega_1^2a_0}{\Delta(\omega)}=a_0\frac{\omega_1^2\Omega^2}{\Delta(\omega)}.$$
> Comme $\Delta(\omega)=\omega^4-\dots$ a pour racines $\omega'^2$ et $\omega''^2$ : $\Delta(\omega)=(\omega'^2-\omega^2)(\omega''^2-\omega^2)=(\omega_1^2+\Omega^2-\omega^2)(\omega_2^2+\Omega^2-\omega^2)-\Omega^4$. Les amplitudes sont *réelles* (sans frottement) : les masses sont en phase ou en opposition de phase avec l'excitation ($\varphi_1,\varphi_2\in\{0,\pi\}$), le signe changeant à chaque passage par une résonance.
>
> **Interprétation**
>
> - **Résonances** : le dénominateur s'annule en $\omega=\omega'$ et $\omega=\omega''$ ; les amplitudes divergent (modèle sans frottement). Un frottement, même faible, les limite.
> - **Basse fréquence** ($\omega\to0$) : $\underline A_1\to a_0\dfrac{\omega_1^2(\omega_2^2+\Omega^2)}{\omega_1^2\omega_2^2+\Omega^2(\omega_1^2+\omega_2^2)}$ : le chariot suit l'excitation quasi statiquement (réduite par le ressort de couplage et le pendule).
> - **Haute fréquence** ($\omega\to\infty$) : $\underline A\to0$ comme $1/\omega^2$ : l'inertie empêche de suivre.


**q6.** **(2\textsuperscript{ème} partie, question 3).** On donne $g=9{,}81\ \mathrm{m\cdot s^{-2}}$, $\ell=0{,}66$ m, $m=0{,}1$ kg et $k_c=1$ N/m. Calculer la période $T$ de l'excitateur pour laquelle le chariot demeurera immobile.

> [!tip]- 💡 Coup de pouce
> **Quelle condition sur les amplitudes ?**
>
> Le chariot est immobile si $x_1(t)=0$ en régime permanent, c'est-à-dire si $\underline A_1=0$. Quel facteur du numérateur doit s'annuler ?


> [!success]- ✅ Correction
> **Résultat**
>
> $\omega^2=\omega_2^2+\Omega^2=\dfrac g\ell+\dfrac{k_c}m$ ; $\omega=4{,}99\ \mathrm{rad\cdot s^{-1}}$ ; $T=\dfrac{2\pi}\omega=1{,}26$ s (indépendant de $k$).


> [!example]- 📝 Solution détaillée
> **Condition d'immobilité**
>
> $\underline A_1=a_0\omega_1^2(\omega_2^2+\Omega^2-\omega^2)/\Delta(\omega)=0$ pour $\omega^2=\omega_2^2+\Omega^2$ (à condition que $\Delta$ ne s'annule pas en même temps : $\Delta=-\Omega^4\neq0$ à cette pulsation). C'est une *antirésonance* du chariot. La pulsation $\sqrt{\omega_2^2+\Omega^2}$ est celle d'un pendule dont le chariot serait immobile : le pendule seul, retenu par le ressort $k_c$ fixé à un point immobile, a pour pulsation $\sqrt{g/\ell+k_c/m}$.
>
> **Application numérique**
>
> $\omega_2^2=\dfrac{9{,}81}{0{,}66}=14{,}86\ \mathrm{s^{-2}}$ ; $\Omega^2=\dfrac1{0{,}1}=10\ \mathrm{s^{-2}}$ ; $\omega^2=24{,}86\ \mathrm{s^{-2}}$ ; $\omega=4{,}986\ \mathrm{rad\cdot s^{-1}}$ ;
> $$T=\frac{2\pi}{\omega}=1{,}26\ \mathrm s.$$
> La raideur $k$ du ressort d'excitation n'est pas donnée : le résultat n'en dépend pas.
>
> **Vérification physique par les forces**
>
> À cette pulsation, $\underline A_2=a_0\dfrac{\omega_1^2\Omega^2}{-\Omega^4}=-a_0\dfrac{\omega_1^2}{\Omega^2}=-\dfrac k{k_c}\,a_0$. Le bilan des forces sur le chariot immobile ($x_1=0$) s'écrit $0=k\,x_0'+k_c\,x_2$ : la force $kx_0'=ka_0\cos\omega t$ de l'excitation est exactement compensée par la force $k_cx_2$ du ressort de couplage, ce qui impose $x_2=-(k/k_c)\,a_0\cos\omega t$ : cohérent.
>
> **Validité et application**
>
> Le pendule doit rester à petit angle : $|A_2|/\ell=(k/k_c)\,a_0/\ell\ll1$. C'est le principe de l'amortisseur à masse accordée : le pendule absorbe l'excitation à la fréquence choisie et le chariot (la structure) reste immobile. En dehors de cette fréquence, l'effet est moindre et les deux résonances $\omega',\omega''$ encadrent l'antirésonance.


> [!note]- 🔗 Liens avec d'autres disciplines
> **Génie civil**
>
> Amortisseur à masse accordée : une masse suspendue (pendule) dans le sommet d'un gratte-ciel, accordée sur la fréquence propre de la structure, réduit sa réponse au vent ou au séisme.
>
> **Électrocinétique**
>
> Filtre coupe-bande : un circuit $LC$ parallèle placé en dérivation annule la transmission à sa fréquence de résonance, de même que le pendule annule le mouvement du chariot.
>
> **Acoustique**
>
> Le résonateur de Helmholtz fixé sur un conduit annule le bruit à sa fréquence propre (TD2, exercice 7).


> [!question]- 🔭 Aller plus loin — Licence : Anticroisement des niveaux
> Montrer que $\omega''^2-\omega'^2=\sqrt{(\omega_1^2-\omega_2^2)^2+4\Omega^4}\ge2\Omega^2$ : les deux pulsations propres ne peuvent pas se croiser quand on varie $\omega_1$ ou $\omega_2$ (répulsion de niveaux). Tracer $\omega'^2$ et $\omega''^2$ en fonction de $\omega_1^2-\omega_2^2$.


> [!question]- 🔭 Aller plus loin — Licence : Pourquoi le mode bas est toujours en phase
> Montrer que $\omega'^2<\min(\omega_1^2,\omega_2^2)+\Omega^2$ et $\omega''^2>\max(\omega_1^2,\omega_2^2)+\Omega^2$, ce qui donne $a_2/a_1>0$ pour le mode bas et $<0$ pour le mode haut : le mode fondamental n'a pas de nœud (cas particulier d'un théorème de Perron--Frobenius).


> [!question]- 🔭 Aller plus loin — Master : Amortisseur à masse accordée
> Avec un petit frottement visqueux sur le pendule, calculer la réponse du chariot à l'excitation ; montrer que l'amplitude du chariot est réduite dans une bande de fréquences autour de $\sqrt{\omega_2^2+\Omega^2}$, et optimiser le frottement.


> [!question]- 🔭 Aller plus loin — Master : Corrections non linéaires
> Les termes cubiques ($\sin\theta\simeq\theta-\theta^3/6$, courbure du ressort $k_c$) rendent les fréquences dépendantes de l'amplitude et peuvent désaccorder l'absorbeur ; voir la méthode de Poincaré--Lindstedt de l'exercice 8.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex2-couplage-de-deux-oscillateurs-harmoniques-dissymetriques|Exercice 2 — Couplage de deux oscillateurs harmoniques dissymétriques]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex4-frequence-propre-d-une-molecule-diatomique|Exercice 4 — Fréquence propre d'une molécule diatomique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex5-complement-niveau-1-cpge-pendules-couples-par-un-ressort-attache-a-mi-hauteur|Exercice 5 — Complément (niveau 1, CPGE) : pendules couplés par un ressort attaché à mi-hauteur]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex6-complement-niveau-2-ambitieux-trois-masses-quatre-ressorts-diagonalisation-et-perturbation|Exercice 6 — Complément (niveau 2, ambitieux) : trois masses, quatre ressorts, diagonalisation et perturbation]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex7-complement-niveau-2-ambitieux-oscillateurs-desaccordes-anticroisement-et-transfert-d-energie|Exercice 7 — Complément (niveau 2, ambitieux) : oscillateurs désaccordés, anticroisement et transfert d'énergie]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex8-complement-niveau-3-ens-modes-non-lineaires-de-deux-pendules-couples-stabilite-et-instabilite-parametrique|Exercice 8 — Complément (niveau 3, ENS) : modes non linéaires de deux pendules couplés, stabilité et instabilité paramétrique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex9-complement-niveau-3-ens-anneau-de-n-oscillateurs-modes-de-fourier-et-propagation-du-signal|Exercice 9 — Complément (niveau 3, ENS) : anneau de N oscillateurs, modes de Fourier et propagation du signal]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex1-pendules-couples-et-battements|Exercice 1 — Pendules couplés et battements]]

