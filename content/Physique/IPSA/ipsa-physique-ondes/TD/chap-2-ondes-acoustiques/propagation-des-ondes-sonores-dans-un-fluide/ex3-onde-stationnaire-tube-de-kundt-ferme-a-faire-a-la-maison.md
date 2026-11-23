---
title: "Exercice 3 — Onde stationnaire, tube de Kundt fermé (à faire à la maison)"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · <a href="/pdfs/td2_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_PhV212_enonce)</a> · <a href="/pdfs/td2_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_enonce)</a> · <a href="/pdfs/td2_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_aides)</a> · <a href="/pdfs/td2_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td2_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_PhV212_corrige)</a> · <a href="/pdfs/td2_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_corrige)</a>

### Exercice 3. Onde stationnaire, tube de Kundt fermé (à faire à la maison) *(facultatif)*

*Difficulté ●●●○○ · ⏱ 25 min (à la maison) · Type : Application (facultatif)*

Même dispositif que l'exercice 2, mais le tube est ouvert en $x=0$ et
fermé en $x=L$. Déplacement réfléchi : $\Psi_R(x,t)=-A_I e^{i(\omega t-k(2L-x))}$.

> [!question]+ 🎣 Accroche
> **Pourquoi la clarinette sonne-t-elle une octave plus grave ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *À longueur égale, une clarinette sonne environ une octave plus bas qu'une flûte, avec un timbre plus « creux ». Notre conduit auditif, fermé au fond par le tympan, mesure environ $2{,}5$ cm : à quelle fréquence résonne-t-il ? Et pourquoi y a-t-il **moins** de notes possibles quand on ferme un bout du tube ?*
>
> **Idée clé : fermer un bout change la condition aux limites, donc les fréquences.** Une paroi rigide impose un nœud de déplacement (ventre de pression) en $x=L$, tandis que l'extrémité ouverte est un nœud de pression en $x=0$. Le déplacement réfléchi change de signe : $\Psi_R=-A_Ie^{i(\omega t-k(2L-x))}$. Il vient $\tilde\theta\propto\cos(k(L-x))$ et la condition $\tilde\theta(0)=0$ donne $\cos(kL)=0$ :
> $$kL=(2n-1)\frac\pi2,\qquad f_n=(2n-1)\frac c{4L}.$$
> Le fondamental tient en **un quart de longueur d'onde** ($L=\lambda_1/4$), deux fois plus grave que pour un tube ouvert-ouvert, et **seuls les harmoniques impairs** existent.


> [!abstract]+ 📚 Prérequis
> **Résultats de l'exercice 2 (tube ouvert-ouvert)**
>
> Cet exercice réutilise directement la méthode de l'exercice 2 (construction de l'onde stationnaire par superposition, lien entre déplacement et surpression/dilatation via $\chi_S$). Il est vivement conseillé de le traiter après avoir bien assimilé le cas ouvert-ouvert, afin de se concentrer ici sur l'unique différence : la condition à l'extrémité $x=L$, désormais fermée.


> [!info]+ 🎯 Objectifs
> **Transposer une méthode à une nouvelle condition aux limites**
>
> Savoir adapter la méthode de résolution développée pour un cas (tube ouvert-ouvert) à un cas voisin (tube ouvert-fermé), en identifiant précisément ce qui change dans les conditions aux limites et ce qui reste inchangé dans la structure de la solution.


> [!note]+ 📖 Point de cours
> **Configuration « quart d'onde » et harmoniques impairs**
>
> Dans la configuration ouverte-fermée, la condition en $x=0$ reste un nœud de pression / ventre de déplacement (extrémité ouverte), tandis qu'en $x=L$ on impose désormais un nœud de déplacement / ventre de pression (extrémité fermée). La distance entre un nœud et le ventre adjacent valant $\lambda/4$, le mode fondamental correspond à un quart de longueur d'onde contenu dans le tube : $L = \lambda_1/4$.
>
> Cette dissymétrie des conditions aux limites a une conséquence remarquable : seuls les harmoniques **impairs** du mode fondamental sont des solutions du problème (contrairement au cas ouvert-ouvert où tous les harmoniques sont permis), d'où l'expression $f_n=(2n-1)c/(4L)$.
>
> **Remarque méthodologique** (comme dans l'exercice 2) : l'expression de $\Psi_R$ encode déjà, par construction, le nœud de déplacement en $x=L$. La quantification des fréquences provient donc, ici encore, de l'imposition de la condition à l'*autre* extrémité $x=0$ — mais cette condition porte cette fois sur la **dilatation** (nœud en $x=0$, car cette extrémité est ouverte), et non sur le déplacement.


> [!note]- 🧮 Outils mathématiques
> **Signe moins à la réflexion : $e^{i\pi}=-1$**
>
> Une réflexion sur paroi rigide inverse le déplacement, donc multiplie l'amplitude par $-1=e^{i\pi}$ (déphasage de $\pi$). Vérification : $\Psi_I(L)+\Psi_R(L)=A_Ie^{i(\omega t-kL)}-A_Ie^{i(\omega t-kL)}=0$.
>
> **Formule d'Euler : $e^{iu}-e^{-iu}=2i\sin u$**
>
> Avec $u=k(L-x)$ : $\Psi=2iA_I\sin(k(L-x))e^{i(\omega t-kL)}$. Contrairement au cas ouvert-ouvert (somme, $\cos$), on trouve ici une différence ($\sin$).
>
> **Dérivée de $\sin(k(L-x))$**
>
> $\dfrac{\partial}{\partial x}\sin\big(k(L-x)\big)=-k\cos\big(k(L-x)\big)$ : la dilatation $\tilde\theta=\partial_x\Psi$ varie en $\cos$, en quadrature avec le déplacement.
>
> **Zéros du cosinus : $\cos u=0\iff u=\dfrac{(2n-1)\pi}2$**
>
> $\cos(kL)=0$ impose $kL=\dfrac\pi2,\dfrac{3\pi}2,\dfrac{5\pi}2,\dots$ (multiples **impairs** de $\pi/2$) ; on renumérote $n=m+1$ pour que $n$ commence à $1$. À comparer avec $\sin(kL)=0$ du cas ouvert-ouvert, qui autorise tous les entiers.
>
> **Décalage de phase : $\sin\!\left(\dfrac\pi2-u\right)=\cos u$**
>
> Pour changer de repère (d'une extrémité à l'autre), un sinus devient un cosinus par décalage de $\pi/2$ : ce qui est nœud pour l'un est ventre pour l'autre.
>
> **Dénombrement**
>
> Le mode $n$ a exactement $n$ nœuds et $n$ ventres de dilatation, avec un nœud en $x=0$ et un ventre en $x=L$ ; les positions sont $x=L-(2m-1)\lambda_n/4$.


**q1.** Justifier ce signe moins par un schéma.

> [!tip]- 💡 Coup de pouce
> Une extrémité fermée (paroi rigide) impose un nœud de déplacement : le déplacement doit s'annuler en $x=L$, d'où le changement de signe à la réflexion.


> [!example]- 📝 Solution détaillée
> **Réflexion avec inversion de signe**
>
> À l'inverse de l'exercice 2, l'extrémité en $x=L$ est ici une paroi rigide : le fluide ne peut pas la traverser, donc son déplacement doit y être nul à tout instant, $\Psi(L,t)=0$. En reprenant l'idée de l'onde image utilisée en exercice 2, on constate qu'il faut cette fois imposer que la contribution réfléchie *s'oppose exactement* à la contribution incidente en $x=L$, ce qui impose un signe moins : $\Psi_R(x,t)=-A_I e^{i(\omega t-k(2L-x))}$. Physiquement, cela correspond exactement au cas de la réflexion d'une impulsion sur l'extrémité fixée d'une corde : l'onde repart inversée, contrairement au cas d'une extrémité libre (exercice 2).
>
> **Vérification directe**
>
> On vérifie qu'en $x=L$ : $\Psi_I(L,t)=A_I e^{i(\omega t-kL)}$ et $\Psi_R(L,t)=-A_I e^{i(\omega t-kL)}$, donc $\Psi_I(L,t)+\Psi_R(L,t)=0$ à tout instant $t$ et pour toute valeur de $k$ : le nœud de déplacement en $x=L$ est bien automatiquement vérifié, quelle que soit la fréquence — exactement comme le nœud de pression en $x=L$ était automatiquement vérifié dans l'exercice 2.


**q2.** Montrer que $\Psi(x,t)=2iA_I\sin(k(L-x))e^{i(\omega t-kL)}$. Justifier le nom d'onde stationnaire.

> [!tip]- 💡 Coup de pouce
> Même démarche qu'à l'exercice 2 : sommez $\Psi_I+\Psi_R$ et mettez le même facteur de phase en évidence.


> [!example]- 📝 Solution détaillée
> **Calcul de la somme**
>
> On part de
> $$\Psi(x,t) = A_I e^{i(\omega t-kx)} - A_I e^{i(\omega t-k(2L-x))}.$$
> En procédant exactement comme à l'exercice 2 (mise en facteur de $A_I e^{i\omega t}$ puis de $e^{-ikL}$) :
> $$\Psi(x,t) = A_I e^{i(\omega t-kL)}\left[e^{ik(L-x)} - e^{-ik(L-x)}\right].$$
> En reconnaissant $e^{iu}-e^{-iu}=2i\sin u$ avec $u=k(L-x)$ :
> $$\boxed{\Psi(x,t) = 2i A_I\sin\big(k(L-x)\big)\,e^{i(\omega t-kL)}}.$$
>
> **Interprétation stationnaire**
>
> Comme en exercice 2, cette expression se met sous la forme $f(x)\,e^{i(\omega t+\varphi_0)}$, avec ici $f(x)=2iA_I\sin(k(L-x))$ (le facteur $i$ supplémentaire n'introduit qu'un déphasage global constant de $\pi/2$ par rapport au cas ouvert-ouvert, sans changer la nature du phénomène) : le profil spatial est figé, seule la phase temporelle oscille — l'onde est donc bien stationnaire.


**q3.** La dilatation $\theta(x,t)=\Delta V/V$ vérifie $\tilde\theta=\partial\Psi/\partial x$. En déduire son expression.

> [!tip]- 💡 Coup de pouce
> Dérivez simplement l'expression de $\Psi(x,t)$ trouvée en 2) par rapport à $x$.


> [!example]- 📝 Solution détaillée
> **Dérivation et expression de $\tilde\theta$**
>
> On dérive $\Psi(x,t)=2iA_I\sin(k(L-x))\,e^{i(\omega t-kL)}$ par rapport à $x$ (attention au signe, comme en exercice 2, à cause de l'argument $k(L-x)$) :
> $$\frac{\partial\Psi}{\partial x} = 2iA_I\,k\,\cos\big(k(L-x)\big)\,e^{i(\omega t-kL)},$$
> d'où directement :
> $$\boxed{\tilde\theta(x,t) = 2iA_I\,k\,\cos\big(k(L-x)\big)\,e^{i(\omega t-kL)}}.$$
> On retrouve la même structure qu'en exercice 2 (à un facteur $i$ et $\rho_0 c\,\omega \leftrightarrow k$ près selon la grandeur choisie) : le profil de la dilatation, en cosinus, est en quadrature spatiale avec celui du déplacement, en sinus.


**q4.** Fréquences $f_n$ de résonance en dilatation, en fonction de $n\in\mathbb{N}^*$, $c$, $L$.

> [!tip]- 💡 Coup de pouce
> Extrémité ouverte (x=0) : ventre de déplacement / nœud de pression-dilatation. Extrémité fermée (x=L) : nœud de déplacement / ventre de dilatation. C'est la configuration "quart d'onde". Comme en exercice 2, la condition en $x=L$ est déjà automatiquement vérifiée ; il reste à imposer la bonne condition en $x=0$.


> [!success]- ✅ Correction
> $f_n=(2n-1)\,c/(4L)$, $n\in\mathbb{N}^*$ (harmoniques impairs seulement).


> [!example]- 📝 Solution détaillée
> **Vérification en $x=L$ (automatique)**
>
> À partir de l'expression de $\tilde\theta$ trouvée en question 3, on vérifie qu'en $x=L$ : $\cos(k(L-L))=\cos(0)=1\neq 0$ : la dilatation y est *maximale* (ventre), quelle que soit la fréquence — cohérent avec le fait que $x=L$ est une extrémité fermée (ventre de pression/dilatation, nœud de déplacement). Cette condition ne fournit donc, comme en exercice 2, aucune information nouvelle sur $k$.
>
> **Condition en $x=0$ (extrémité ouverte) : quantification**
>
> En $x=0$, l'extrémité est ouverte, donc un nœud de dilatation (pression) doit s'y trouver :
> $$\tilde\theta(0,t) = 2iA_I k \cos(kL)\,e^{i(\omega t-kL)} = 0 \quad\Longrightarrow\quad \cos(kL)=0.$$
> Cette équation n'est vérifiée que pour :
> $$kL = \frac{\pi}{2} + m\pi = \frac{(2m+1)\pi}{2}, \qquad m\in\mathbb{N},$$
> soit, en renumérotant $n=m+1$ (de sorte que $n$ démarre à $1$) :
> $$kL = \frac{(2n-1)\pi}{2}, \qquad n\in\mathbb{N}^*.$$
> En utilisant $k=2\pi f/c$ :
> $$\frac{2\pi f_n}{c}L = \frac{(2n-1)\pi}{2} \quad\Longrightarrow\quad \boxed{f_n = \frac{(2n-1)\,c}{4L}}, \qquad n\in\mathbb{N}^*.$$
> Seuls les harmoniques impairs de la fréquence $c/(4L)$ apparaissent : c'est la différence essentielle avec le tube ouvert-ouvert de l'exercice 2, où *tous* les harmoniques ($\sin(kL)=0$, condition moins restrictive que $\cos(kL)=0$) étaient permis.


**q5.** Position des maxima/minima de dilatation ; représenter jusqu'à la 3e harmonique (n=4).

> [!example]- 📝 Solution détaillée
> **Formule générale des nœuds et ventres**
>
> Pour le mode $n$, on a $k_n L = (2n-1)\pi/2$, soit une longueur d'onde $\lambda_n = 2\pi/k_n = 4L/(2n-1)$. Le profil $|\cos(k_n(L-x))|$ s'annule (nœuds de dilatation) lorsque $k_n(L-x) = (2m-1)\pi/2$, soit :
> $$x_m^{\text{nœud}} = L - (2m-1)\frac{\lambda_n}{4}, \qquad m=1,\dots,n,$$
> ce qui donne exactement $n$ nœuds (dont systématiquement $x=0$, l'extrémité ouverte). Les ventres se situent où $k_n(L-x)=m\pi$, soit :
> $$x_m^{\text{ventre}} = L - m\,\frac{\lambda_n}{2}, \qquad m=0,\dots,n-1,$$
> ce qui donne $n$ ventres, dont systématiquement $x=L$ (l'extrémité fermée).
>
> **Application aux quatre premiers harmoniques impairs**
>
> - $n=1$ ($f_1=c/4L$, $\lambda_1=4L$) : 1 seul nœud ($x=0$), 1 seul ventre ($x=L$) — le quart d'onde fondamental.
> - $n=2$ ($f_2=3c/4L$, $\lambda_2=4L/3$) : 2 nœuds ($x=0,\,2L/3$), 2 ventres ($x=L/3,\,L$).
> - $n=3$ ($f_3=5c/4L$, $\lambda_3=4L/5$) : 3 nœuds ($x=0,\,2L/5,\,4L/5$), 3 ventres ($x=L/5,\,3L/5,\,L$).
> - $n=4$ ($f_4=7c/4L$, $\lambda_4=4L/7$) : 4 nœuds ($x=0,\,2L/7,\,4L/7,\,6L/7$), 4 ventres ($x=L/7,\,3L/7,\,5L/7,\,L$).
>
>
> On retrouve la dissymétrie caractéristique de la configuration quart d'onde : chaque mode $n$ possède exactement $n$ nœuds et $n$ ventres (au lieu de $n$ ventres et $n+1$ nœuds dans le cas ouvert-ouvert), avec systématiquement un nœud en $x=0$ et un ventre en $x=L$.


> [!note]- 🔗 Liens avec d'autres disciplines
> **Musique**
>
> Clarinette, tuyau d'orgue bouché (bourdon), flûte de Pan : tubes fermés à un bout. Sans harmoniques pairs, le timbre est plus « creux » (ou « rond »), et la note est une octave plus grave qu'un tube ouvert de même longueur.
>
> **Physiologie de l'audition**
>
> Le conduit auditif ($L\approx2{,}5$ cm, fermé par le tympan) résonne à $f_1=c/(4L)\approx3{,}4$ kHz : c'est la zone où l'oreille est la plus sensible.
>
> **Cordes vibrantes (chapitre 1)**
>
> Une corde fixe-libre a les mêmes fréquences $f_N=(2N-1)c/(4L)$ : le tube fermé à un bout est l'analogue exact (exercice 6 du chapitre 1).
>
> **Électricité et antennes**
>
> L'antenne monopole quart d'onde sur plan de masse est un résonateur fermé à un bout : $L=\lambda/4$ et seulement les multiples impairs.
>
> **Mathématiques**
>
> Conditions aux limites de Dirichlet (la fonction s'annule) et de Neumann (la dérivée s'annule) : le mélange des deux (Dirichlet-Neumann) donne les valeurs propres $(2n-1)\pi/(2L)$.


> [!question]- 🔭 Aller plus loin — Licence : Timbre des instruments à vent : clarinette contre flûte
> La clarinette (anche fermant quasiment le tube côté bouche) se comporte acoustiquement comme un tube fermé-ouvert, tandis que la flûte traversière se comporte comme un tube ouvert-ouvert. On pourra expliquer pourquoi, à longueur de tube comparable, la clarinette sonne environ une octave plus grave que la flûte, et pourquoi son timbre est perçu comme plus « creux » (absence des harmoniques pairs dans le spectre théorique du tube fermé).


> [!question]- 🔭 Aller plus loin — Master : Facteur de qualité et pertes aux parois
> En réalité, les couches limites visqueuse et thermique au voisinage des parois du tube dissipent de l'énergie acoustique, ce qui élargit chaque résonance autour de $f_n$ (facteur de qualité $Q_n$ fini) au lieu d'un pic infiniment fin prédit par le modèle sans pertes. On pourra établir, à partir d'un modèle d'oscillateur amorti équivalent, comment $Q_n$ dépend de la fréquence, du rayon du tube et des propriétés de transport du fluide (viscosité, diffusivité thermique).


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex2-onde-stationnaire-tube-de-kundt-ouvert|Exercice 2 — Onde stationnaire, tube de Kundt ouvert]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex5-energie-intensite-acoustique-et-niveau-sonore-de-l-oreille-humaine-a-l-onde-stationnaire|Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex6-tube-d-impedance-mesurer-l-absorption-d-un-materiau-avec-une-onde-stationnaire-partielle|Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]]

