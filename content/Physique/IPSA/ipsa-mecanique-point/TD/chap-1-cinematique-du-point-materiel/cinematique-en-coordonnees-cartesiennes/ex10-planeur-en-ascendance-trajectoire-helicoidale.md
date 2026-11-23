---
title: "Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td1_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/test.pdf" target="_blank" rel="noopener">📄 PDF</a> · <a href="/pdfs/td1_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 10. Planeur en ascendance : trajectoire hélicoïdale *(facultatif)*

*Difficulté ●●●○○ · ⏱ 45 min · Type : Application / Approfondissement*

Un planeur spirale dans une ascendance thermique. Dans le référentiel terrestre, supposé galiléen, muni d'un repère cartésien $Oxyz$ avec $Oz$ vertical ascendant, on modélise son mouvement par les équations horaires
$$x(t)=R\cos(\omega t),\qquad y(t)=R\sin(\omega t),\qquad z(t)=z_0+v_z\,t,$$
avec $R=50$ m, $\omega=0{,}20~\mathrm{rad\,s^{-1}}$, $v_z=1{,}5~\mathrm{m\,s^{-1}}$ (taux de montée) et $z_0=600$ m. Le planeur est assimilé à un point matériel $M$. On prendra $g=9{,}81~\mathrm{m\,s^{-2}}$.

> [!question]+ 🎣 Accroche
> **Spirale ascendante : plus ou moins courbée qu'un cercle ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *Un planeur monte en spirale dans un thermique : vu de dessus, il décrit un cercle de $50$ m de rayon. **Sa trajectoire réelle est-elle plus ou moins courbée** que ce cercle ? Sa vitesse est-elle plus grande que celle de la projection ? Et si on lâche un objet, où tombe-t-il ?*
>
> **Idée clé : composer un mouvement circulaire uniforme et un mouvement rectiligne uniforme.** Les composantes du vecteur vitesse sont $(-R\omega\sin\omega t,\ R\omega\cos\omega t,\ v_z)$ : la partie horizontale tourne sans changer de norme, la partie verticale est constante. La norme est donc constante,
> $$\|\vec v\|=\sqrt{R^2\omega^2+v_z^2},$$
> et l'accélération vient uniquement de la rotation du vecteur vitesse horizontal :
> $$\vec a=-\omega^2(x\,\vec u_x+y\,\vec u_y),\qquad\|\vec a\|=R\omega^2 .$$


> [!abstract]+ 📚 Prérequis
> **Vecteurs position, vitesse, accélération en coordonnées cartésiennes**
>
> $\vec v=\dot x\,\vec u_x+\dot y\,\vec u_y+\dot z\,\vec u_z$ et $\vec a=\ddot x\,\vec u_x+\ddot y\,\vec u_y+\ddot z\,\vec u_z$. Les normes se calculent par la racine de la somme des carrés des composantes.
>
> **Longueur d'un arc de trajectoire**
>
> La distance parcourue entre $t_1$ et $t_2$ est $\ell=\displaystyle\int_{t_1}^{t_2}\|\vec v\|\,\mathrm dt$. Pour une vitesse de norme constante, $\ell=\|\vec v\|\,(t_2-t_1)$.
>
> **Accélération normale et rayon de courbure**
>
> Si $\vec a\perp\vec v$ à un instant donné, l'accélération est purement normale et $\|\vec a\|=\dfrac{v^2}{\rho}$, où $\rho$ est le rayon de courbure de la trajectoire.


> [!info]+ 🎯 Objectifs
> **Passer du 2D au 3D en cartésien et exploiter une symétrie**
>
> Savoir calculer $\vec v$ et $\vec a$ pour un mouvement hélicoïdal, montrer que la norme de la vitesse est constante, que l'accélération est orthogonale à la vitesse, en déduire le rayon de courbure de l'hélice, caractériser la géométrie (pas, angle de montée), puis réinvestir un tir de projectile quand un objet se détache du mobile.


> [!info]- 🧑‍🏫 Objectifs pédagogiques (enseignant)
> **Trois exercices en un : composition, normes constantes, lâcher d'objet**
>
> L'exercice reprend le mouvement circulaire du TD et y ajoute un mouvement vertical uniforme : la composition est directe, mais la géométrie 3D est plus difficile à visualiser. On y découvre que **la courbure de l'hélice est plus faible que celle du cercle** ($\rho>R$), résultat que l'étudiant n'attend pas. La dernière question (lâcher d'un objet) oblige à redéfinir de nouvelles conditions initiales et à reconnaître un tir de projectile, avec la même vitesse (vecteur) que celle du planeur. L'exercice prépare l'étude du repère de Frenet et de l'accélération tangentielle/normale du cours suivant.


> [!note]+ 📖 Point de cours
> **Hélice circulaire**
>
> Les équations $x=R\cos\omega t$, $y=R\sin\omega t$, $z=z_0+v_zt$ décrivent une hélice sur un cylindre d'axe $Oz$ et de rayon $R$. Le **pas** est la hauteur gagnée en un tour : $p=\dfrac{2\pi v_z}{\omega}$. Le vecteur vitesse fait avec le plan horizontal un angle constant $\gamma$ tel que $\tan\gamma=\dfrac{v_z}{R\omega}$.


> [!note]- 🧮 Outils mathématiques
> **Identité $\cos^2+\sin^2=1$**
>
> Elle donne $\|\vec v\|^2=R^2\omega^2(\sin^2\omega t+\cos^2\omega t)+v_z^2=R^2\omega^2+v_z^2$ sans dépendance en $t$.
>
> **Produit scalaire en 3D**
>
> $\vec v\cdot\vec a=v_xa_x+v_ya_y+v_za_z$. Ici : $R^2\omega^3(\sin\omega t\cos\omega t-\cos\omega t\sin\omega t)+0=0$.
>
> **Longueur d'arc et tour complet**
>
> Un tour complet dure $T=2\pi/\omega$. La longueur d'une spire est $\ell=\|\vec v\|\,T=\sqrt{(2\pi R)^2+p^2}$ (théorème de Pythagore sur le développement du cylindre : base $2\pi R$, hauteur $p$).
>
> **Résolution d'une équation du second degré en $t$**
>
> $-\tfrac12gt^2+v_zt+z_0=0\Rightarrow t=\dfrac{v_z+\sqrt{v_z^2+2gz_0}}{g}$ (on garde la racine positive).
>
> **Arctangente pour un angle de pente**
>
> Pour $\tan\gamma=\dfrac{v_z}{R\omega}$, on a $\gamma=\arctan\dfrac{v_z}{R\omega}$ ; pour un angle faible, $\gamma\approx\dfrac{v_z}{R\omega}$ en radians.


**q1.** - [(a)] Déterminer le vecteur vitesse $\vec v$ et sa norme. Que remarque-t-on ?
- [(b)] Déterminer le vecteur accélération $\vec a$ et sa norme. Calculer $\vec v\cdot\vec a$. Que conclut-on sur le mouvement ?
- [(c)] Calculer numériquement $\|\vec v\|$ et $\|\vec a\|$.

> [!tip]- 💡 Coup de pouce
> Dérivez chaque coordonnée : le terme $z_0$ disparaît et $v_z$ est constante. Pour la norme, utilisez $\cos^2+\sin^2=1$. Pour le produit scalaire, développez composante par composante.


> [!success]- ✅ Correction
> $\vec v=(-R\omega\sin\omega t,\ R\omega\cos\omega t,\ v_z)$, $\|\vec v\|=\sqrt{R^2\omega^2+v_z^2}\approx10{,}1~\mathrm{m/s}$ constante ; $\vec a=-R\omega^2(\cos\omega t,\ \sin\omega t,\ 0)$, $\|\vec a\|=R\omega^2=2{,}0~\mathrm{m/s^2}$ ; $\vec v\cdot\vec a=0$.


> [!example]- 📝 Solution détaillée
> **(a) Vecteur vitesse et norme**
>
> $$\vec v=\boxed{-R\omega\sin(\omega t)\,\vec u_x+R\omega\cos(\omega t)\,\vec u_y+v_z\,\vec u_z}.$$
> Norme :
> $$\|\vec v\|^2=R^2\omega^2\big(\sin^2\omega t+\cos^2\omega t\big)+v_z^2=R^2\omega^2+v_z^2\;\Longrightarrow\;\boxed{\|\vec v\|=\sqrt{R^2\omega^2+v_z^2}}.$$
> La norme de la vitesse est **constante** : le mouvement est uniforme sur la trajectoire hélicoïdale, bien que la direction de $\vec v$ change.
>
> **(b) Vecteur accélération**
>
> $$\vec a=\boxed{-R\omega^2\cos(\omega t)\,\vec u_x-R\omega^2\sin(\omega t)\,\vec u_y}=-\omega^2\big(x\,\vec u_x+y\,\vec u_y\big),\qquad\|\vec a\|=R\omega^2 .$$
> L'accélération est **horizontale** et dirigée vers l'axe $Oz$ (accélération centripète de la projection circulaire).
>
> Produit scalaire :
> $$\vec v\cdot\vec a=R^2\omega^3\big(\sin\omega t\cos\omega t-\cos\omega t\sin\omega t\big)+v_z\cdot0=0 .$$
> Comme $\vec a\perp\vec v$ à chaque instant, l'accélération est **purement normale** (aucune composante tangentielle), ce qui est cohérent avec la vitesse de norme constante.
>
> **(c) Valeurs numériques**
>
> $R\omega=50\times0{,}20=10~\mathrm{m/s}$ donc
> $$\|\vec v\|=\sqrt{10^2+1{,}5^2}=\sqrt{102{,}25}\approx\boxed{10{,}1~\mathrm{m\,s^{-1}}}\ (\approx36~\text{km/h}),\qquad\|\vec a\|=R\omega^2=50\times0{,}04=\boxed{2{,}0~\mathrm{m\,s^{-2}}}\ (\approx0{,}2\,g).$$


**q2.** - [(d)] Déterminer le pas $p$ de l'hélice, l'angle $\gamma$ que fait la vitesse avec l'horizontale, et la longueur d'une spire. Application numérique.
- [(e)] Calculer le rayon de courbure $\rho$ de la trajectoire. Le comparer à $R$ et commenter.
- [(f)] Déterminer l'équation de la projection de la trajectoire dans le plan $Oxz$. De quelle courbe s'agit-il ?

> [!tip]- 💡 Coup de pouce
> Un tour dure $T=2\pi/\omega$ ; le pas est la hauteur gagnée pendant $T$. Pour $\rho$, utilisez $a=v^2/\rho$ car $\vec a\perp\vec v$. Pour (f), éliminez $t$ entre $x(t)$ et $z(t)$ en écrivant $\omega t=\omega(z-z_0)/v_z$.


> [!success]- ✅ Correction
> $p=\dfrac{2\pi v_z}{\omega}\approx47{,}1$ m ; $\gamma=\arctan\dfrac{v_z}{R\omega}\approx8{,}5^\circ$ ; spire $\approx317{,}7$ m ; $\rho=\dfrac{v^2}{a}=R+\dfrac{v_z^2}{R\omega^2}\approx51{,}1$ m $>R$ ; projection $x=R\cos\big[\omega(z-z_0)/v_z\big]$ : sinusoïde.


> [!example]- 📝 Solution détaillée
> **(d) Géométrie de l'hélice**
>
> La durée d'un tour est $T=\dfrac{2\pi}{\omega}\approx31{,}4$ s. Le pas est
> $$p=v_zT=\boxed{\frac{2\pi v_z}{\omega}}\approx\boxed{47{,}1~\text{m}}.$$
> L'angle de montée vérifie $\tan\gamma=\dfrac{v_z}{R\omega}=0{,}15$ : $\gamma\approx\boxed{8{,}5^\circ}$.
>
> Longueur d'une spire : $\ell=\|\vec v\|\,T\approx10{,}11\times31{,}4\approx317{,}7$ m. Vérification géométrique (développement du cylindre) : $\sqrt{(2\pi R)^2+p^2}=\sqrt{314{,}2^2+47{,}1^2}\approx317{,}7$ m. $\surd$
>
> **(e) Rayon de courbure**
>
> Comme $\vec a\perp\vec v$, l'accélération est purement normale : $a=\dfrac{v^2}{\rho}$, d'où
> $$\rho=\frac{v^2}{a}=\frac{R^2\omega^2+v_z^2}{R\omega^2}=\boxed{R+\frac{v_z^2}{R\omega^2}}\approx50+\frac{2{,}25}{2}\approx\boxed{51{,}1~\text{m}}.$$
> On a $\rho>R$ : la trajectoire de l'hélice est **moins courbée** que le cercle de sa projection horizontale (rayon $R$). Plus le planeur monte vite ($v_z$ grand), plus la trajectoire s'« aplatit » (le rayon de courbure augmente) ; à $v_z=0$, on retrouve $\rho=R$ (cercle).
>
> **(f) Projection dans le plan $Oxz$**
>
> De $z=z_0+v_zt$ on tire $t=\dfrac{z-z_0}{v_z}$. Alors
> $$\boxed{x=R\cos\left[\frac{\omega}{v_z}\,(z-z_0)\right]}.$$
> C'est une **sinusoïde** d'amplitude $R$ et de période spatiale (suivant $z$) $\dfrac{2\pi v_z}{\omega}=p$, égale au pas de l'hélice. Vue de côté, l'hélice ressemble à une onde ; vue de dessus, à un cercle.


**q3.** - [(g)] À $t=0$, le planeur est en $M_0=(R,0,z_0)$ et le pilote lâche un objet (sans vitesse relative par rapport au planeur). Déterminer la durée de chute jusqu'au sol ($z=0$) et le point d'impact. On néglige les frottements de l'air.
- [(h)] À quelle distance de l'axe $Oz$ l'objet touche-t-il le sol ? Que vaut la norme de sa vitesse à l'impact ?

> [!tip]- 💡 Coup de pouce
> L'objet quitte $M_0$ avec la vitesse $\vec v(0)=(0,\ R\omega,\ v_z)$, puis il est soumis à la seule pesanteur : $\vec a=-g\,\vec u_z$. Écrivez ses équations horaires, puis résolvez $z=0$. La norme de la vitesse à l'impact se trouve par la conservation de l'énergie mécanique.


> [!success]- ✅ Correction
> $t_c=\dfrac{v_z+\sqrt{v_z^2+2gz_0}}{g}\approx11{,}2$ s ; impact en $(R,\ R\omega t_c,\ 0)\approx(50,\ 112,\ 0)$ m ; distance à l'axe $\approx123$ m ; $v\approx109~\mathrm{m/s}$.


> [!example]- 📝 Solution détaillée
> **(g) Équations horaires et durée de chute**
>
> À $t=0$, l'objet est en $(R,0,z_0)$ avec $\vec v(0)=R\omega\,\vec u_y+v_z\,\vec u_z$ (vitesse du planeur, composante verticale $+v_z$ vers le haut comprise). Accélération : $-g\,\vec u_z$. Par intégration :
> $$x(t)=R,\qquad y(t)=R\omega\,t,\qquad z(t)=z_0+v_zt-\tfrac12gt^2 .$$
> L'objet touche le sol quand $z(t_c)=0$ :
> $$\tfrac12gt_c^2-v_zt_c-z_0=0\;\Longrightarrow\;t_c=\frac{v_z+\sqrt{v_z^2+2gz_0}}{g}=\frac{1{,}5+\sqrt{2{,}25+11772}}{9{,}81}\approx\boxed{11{,}2~\text{s}}.$$
>
> **(h) Point d'impact et vitesse**
>
> Point d'impact : $x=R=50$ m, $y=R\omega\,t_c\approx10\times11{,}21\approx112$ m, soit $(50;\ 112;\ 0)$ m.
>
> Distance à l'axe $Oz$ : $\sqrt{50^2+112^2}\approx\boxed{123~\text{m}}$. L'objet a quitté la trajectoire en ligne droite (tangente à l'hélice, à la vitesse horizontale $R\omega=10~\mathrm{m/s}$) et tombe donc bien plus loin que le rayon $R$ de la spire.
>
> Vitesse à l'impact : conservation de l'énergie mécanique,
> $$\tfrac12v_{\rm imp}^2=\tfrac12\|\vec v(0)\|^2+gz_0\Rightarrow v_{\rm imp}=\sqrt{102{,}25+2\times9{,}81\times600}\approx\boxed{109~\mathrm{m\,s^{-1}}}.$$
> La composante horizontale ($10~\mathrm{m/s}$) est négligeable devant la composante verticale ($\approx108~\mathrm{m/s}$).


> [!warning]- 🪤 Écueils classiques
> **Penser que le mouvement est circulaire uniforme**
>
> La projection sur $Oxy$ est bien un cercle parcouru à vitesse $R\omega$, mais la trajectoire 3D n'est pas un cercle : la vitesse totale vaut $\sqrt{R^2\omega^2+v_z^2}$ et le rayon de courbure $\rho=R+\dfrac{v_z^2}{R\omega^2}>R$.
>
> **Oublier que $v_z$ est une constante, donc $a_z=0$**
>
> L'accélération est purement horizontale : $\vec a=-R\omega^2(\cos\omega t\,\vec u_x+\sin\omega t\,\vec u_y)$. La composante verticale est nulle, ce qui est cohérent avec une montée à vitesse verticale constante.
>
> **Utiliser $\rho=R$ dans $a=v^2/\rho$**
>
> Avec la vitesse totale $v=\sqrt{R^2\omega^2+v_z^2}$ et l'accélération $R\omega^2$, on obtient $\rho=v^2/a\neq R$. Utiliser $\rho=R$ avec la vitesse totale conduit à une accélération erronée.
>
> **Oublier la vitesse verticale à la libération**
>
> L'objet lâché emporte la vitesse **complète** du planeur, composante verticale incluse ($+v_z$, vers le haut). Si on la néglige, le temps de chute est faussé.


> [!tip]- 🎙️ Conseils d'animation
> **Visualiser en 3D**
>
> Tracer l'hélice avec Python (\texttt{matplotlib}, projection 3D) ou GeoGebra 3D en faisant varier $v_z$ et $\omega$ : le pas change, l'inclinaison aussi. Montrer la vue de dessus (cercle) et la vue de côté (sinusoïde).
>
> **Donnée réelle**
>
> Les pilotes de vol à voile enregistrent leur trace GPS : le tracé d'une ascendance est une hélice. Si possible, faire estimer $R$, $\omega$, $v_z$ sur une trace réelle.


> [!note]- 🔗 Liens avec d'autres disciplines
> **Aéronautique et vol à voile**
>
> Les pilotes se centrent dans les thermiques en spiralant ; la trace GPS est une hélice ; le rayon dépend de la vitesse et de l'inclinaison de l'aile.
>
> **Physique des plasmas et électromagnétisme**
>
> Une particule chargée dans un champ magnétique uniforme suit une hélice (mouvement cyclotron) : même mathématique, avec $\omega=|q|B/m$.
>
> **Biologie moléculaire**
>
> L'ADN a la forme d'une double hélice, de pas $\approx3{,}4$ nm et de rayon $\approx1$ nm : les mêmes formules (pas, angle de pente) s'appliquent.
>
> **Génie civil et mécanique**
>
> Escaliers en colimaçon, ressorts hélicoïdaux, vis, rampes de parkings : l'hélice est omniprésente, avec pas et angle d'hélice comme paramètres de conception.
>
> **Mathématiques**
>
> Courbes dans l'espace, courbure et torsion, repère de Frenet--Serret ; l'hélice circulaire est la courbe de courbure et de torsion constantes.


> [!success]- 🏁 Bilan
> **L'hélice : vitesse constante, accélération centripète, courbure réduite**
>
> $\|\vec v\|=\sqrt{R^2\omega^2+v_z^2}$ constante ; $\vec a=-\omega^2(x\,\vec u_x+y\,\vec u_y)$ horizontale, orthogonale à $\vec v$, de norme $R\omega^2$ ; rayon de courbure $\rho=R+\dfrac{v_z^2}{R\omega^2}$ ; pas $p=\dfrac{2\pi v_z}{\omega}$ ; angle de montée $\tan\gamma=\dfrac{v_z}{R\omega}$. Avec les valeurs de l'énoncé : $v\approx10{,}1~\mathrm{m/s}$, $a=2{,}0~\mathrm{m/s^2}$, $\rho\approx51{,}1$ m, $p\approx47{,}1$ m.


> [!question]- 🔭 Aller plus loin — CPGE : Vitesse constante $\Rightarrow$ accélération orthogonale
> Montrer que, pour tout mouvement, $\dfrac{\mathrm d\|\vec v\|^2}{\mathrm dt}=2\,\vec v\cdot\vec a$. En déduire que si $\|\vec v\|$ est constante alors $\vec a\perp\vec v$ à tout instant, puis retrouver ce résultat pour l'hélice sans calcul de dérivées de $\sin$ et $\cos$.


> [!question]- 🔭 Aller plus loin — Licence : Torsion de l'hélice et repère de Frenet
> Pour une hélice de rayon $R$ et de pas réduit $c=v_z/\omega$, calculer le vecteur tangent unitaire $\vec\tau=\vec v/\|\vec v\|$, la courbure $\kappa=1/\rho=\dfrac{R}{R^2+c^2}$, puis la torsion $\tau_{\rm tors}=\dfrac{c}{R^2+c^2}$. Vérifier que $\kappa$ et $\tau_{\rm tors}$ sont constantes : c'est la propriété caractéristique de l'hélice circulaire.


> [!question]- 🔭 Aller plus loin — Master : Spirale non uniforme : le thermique qui s'évase
> Dans une vraie ascendance, $R$ et $v_z$ varient avec l'altitude : le pilote se centre dans le thermique et le rayon diminue. Étudier $x=R(t)\cos\omega t$, $y=R(t)\sin\omega t$, $z=v_zt$ avec $R(t)=R_0\,\mathrm e^{-t/\tau}$. Calculer $\vec v$, $\vec a$ et montrer que l'accélération a alors une composante tangentielle non nulle ; discuter l'effet sur la vitesse.


> [!question]- 🔭 Aller plus loin — Doctorat : Particule chargée dans un champ magnétique uniforme
> Une particule chargée dans un champ $\vec B=B\,\vec u_z$ uniforme suit une hélice d'axe $Oz$, avec $\omega=|q|B/m$ (pulsation cyclotron) et $R=mv_\perp/(|q|B)$. Retrouver $\vec a\perp\vec v$ comme conséquence de la force de Lorentz, et discuter la dérive du centre guide en présence d'un champ électrique $\vec E\perp\vec B$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex6-parabole-de-s-rete-et-tir-sur-une-pente|Exercice 6 — Parabole de sûreté et tir sur une pente]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex7-balle-rebondissante-et-paradoxe-de-zenon|Exercice 7 — Balle rebondissante et paradoxe de Zénon]]

