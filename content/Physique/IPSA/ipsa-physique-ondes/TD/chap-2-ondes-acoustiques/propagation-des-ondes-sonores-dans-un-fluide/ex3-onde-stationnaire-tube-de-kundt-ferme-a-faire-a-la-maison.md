---
title: "Exercice 3 — Onde stationnaire, tube de Kundt fermé (à faire à la maison)"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · <a href="/pdfs/td2_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_PhV212_enonce)</a> · <a href="/pdfs/td2_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_enonce)</a> · <a href="/pdfs/td2_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_aides)</a> · <a href="/pdfs/td2_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td2_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_PhV212_corrige)</a> · <a href="/pdfs/td2_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_corrige)</a> · <a href="/pdfs/td2_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 3. Onde stationnaire, tube de Kundt fermé (à faire à la maison) *(facultatif)*

Même dispositif que l'exercice 2, mais le tube est ouvert en $x=0$ et
fermé en $x=L$. Déplacement réfléchi : $\Psi_R(x,t)=-A_I e^{i(\omega t-k(2L-x))}$.

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


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex2-onde-stationnaire-tube-de-kundt-ouvert|Exercice 2 — Onde stationnaire, tube de Kundt ouvert]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex5-energie-intensite-acoustique-et-niveau-sonore-de-l-oreille-humaine-a-l-onde-stationnaire|Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex6-tube-d-impedance-mesurer-l-absorption-d-un-materiau-avec-une-onde-stationnaire-partielle|Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]]

