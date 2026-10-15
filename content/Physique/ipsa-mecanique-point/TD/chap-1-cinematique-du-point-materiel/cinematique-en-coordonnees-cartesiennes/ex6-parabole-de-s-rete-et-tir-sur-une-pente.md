---
title: "Exercice 6 — Parabole de sûreté et tir sur une pente"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td1_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td1_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td1_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td1_PhV111_fiche.pdf)

### Exercice 6. Parabole de sûreté et tir sur une pente *(facultatif)*

Un pompier dispose d'une lance dont le jet sort, au niveau du sol, avec une vitesse de norme fixée $v_0=20~\mathrm{m\,s^{-1}}$ ; il peut
seulement choisir l'angle de tir $\alpha$ du jet avec l'horizontale. On néglige les frottements de l'air et on assimile une particule d'eau à un point matériel en chute libre dans le champ de pesanteur $g=9{,}81~\mathrm{m\,s^{-2}}$.
On choisit un repère $Oxz$ (le mouvement est plan), l'origine $O$ à la sortie de la lance, $Oz$ vertical ascendant. Les équations horaires sont celles de l'exercice « balle de golf » :
$$x(t)=v_0\cos\alpha\;t,\qquad z(t)=-\tfrac12\,g\,t^2+v_0\sin\alpha\;t,$$
d'où l'équation de la trajectoire
$$z(x)=x\tan\alpha-\frac{g\,x^2}{2v_0^2}\,\big(1+\tan^2\alpha\big).$$
Dans tout l'exercice, $v_0$ est fixé et **c'est $\alpha$ qui est l'inconnue**.

**q1.** - [(a)] Montrer que, pour atteindre le point $(x,z)$, l'angle de tir doit vérifier une équation du second degré dont l'inconnue est $u=\tan\alpha$.
- [(b)] À quelle condition sur $z$ (à $x$ fixé) cette équation a-t-elle des solutions réelles ? En déduire l'expression de la parabole de sûreté $z_s(x)$.
- [(c)] Une fenêtre est située à $x=25$ m et $z=10$ m. Peut-on l'atteindre ? Calculer les angles de tir possibles et les durées de vol correspondantes. Comparer les vitesses d'arrivée.

> [!tip]- 💡 Coup de pouce
> Pour (a), partez de $z=x\tan\alpha-\dfrac{g x^2}{2v_0^2}(1+\tan^2\alpha)$ et regroupez les termes en puissances de $u$. Pour (b), calculez $\Delta=B^2-4AC$ et résolvez $\Delta\ge0$ en $z$. Pour la vitesse d'arrivée, pensez à la conservation de l'énergie mécanique.


> [!success]- ✅ Correction
> $\dfrac{gx^2}{2v_0^2}u^2-xu+z+\dfrac{gx^2}{2v_0^2}=0$ ; atteignable ssi $z\le z_s(x)=\dfrac{v_0^2}{2g}-\dfrac{g x^2}{2v_0^2}$. Fenêtre : $z_s(25)\approx12{,}7$ m $>10$ m donc atteignable ; $\alpha_1\approx46{,}0^\circ$ ($t\approx1{,}80$ s) et $\alpha_2\approx65{,}8^\circ$ ($t\approx3{,}05$ s) ; même norme de vitesse d'arrivée $\approx14{,}3~\mathrm{m/s}$.


> [!example]- 📝 Solution détaillée
> **(a) Équation du second degré en $\tan\alpha$**
>
> On pose $k=\dfrac{g x^2}{2v_0^2}$ et $u=\tan\alpha$. Le point $(x,z)$ est atteint si
> $$z=x\,u-k\,(1+u^2)\iff\boxed{k\,u^2-x\,u+(z+k)=0}.$$
> C'est un trinôme en $u$ de coefficients $A=k$, $B=-x$, $C=z+k$.
>
> **(b) Condition d'existence et parabole de sûreté**
>
> Le discriminant vaut $\Delta=x^2-4k\,(z+k)$. Il est positif ou nul si
> $$z\le\frac{x^2}{4k}-k=\frac{v_0^2}{2g}-\frac{g\,x^2}{2v_0^2}.$$
> (On a utilisé $\dfrac{x^2}{4k}=\dfrac{x^2\cdot2v_0^2}{4g\,x^2}=\dfrac{v_0^2}{2g}$.) La frontière est donc
> $$\boxed{z_s(x)=\frac{v_0^2}{2g}-\frac{g\,x^2}{2v_0^2}}$$
> C'est la **parabole de sûreté** : un point est atteignable si et seulement s'il est sur ou sous cette courbe. À l'intérieur, $\Delta>0$ et il y a deux angles ; sur la parabole, $\Delta=0$ et il y en a un seul.
>
> **(c) Application à la fenêtre**
>
> Avec $v_0=20~\mathrm{m/s}$ : $\dfrac{v_0^2}{2g}\approx20{,}39$ m et $k=\dfrac{9{,}81\times625}{2\times400}\approx7{,}664$ m. D'où $z_s(25)\approx20{,}39-7{,}66\approx12{,}7$ m. Comme $z=10$ m $<12{,}7$ m, la fenêtre est atteignable.
>
> L'équation est $7{,}664\,u^2-25\,u+17{,}664=0$, avec $\Delta\approx83{,}5$ :
> $$u=\frac{25\pm9{,}14}{15{,}33}\Rightarrow u_1\approx1{,}035,\;u_2\approx2{,}227,$$
> soit $\boxed{\alpha_1\approx46{,}0^\circ\ \text{(tir tendu)},\quad\alpha_2\approx65{,}8^\circ\ \text{(tir en cloche)}}$.
>
> Durées de vol : $t=\dfrac{x}{v_0\cos\alpha}$, d'où $t_1\approx1{,}80$ s et $t_2\approx3{,}05$ s : le tir tendu est plus rapide.
>
> Vitesses d'arrivée : l'énergie mécanique étant conservée et les deux tirs partant de la même altitude à la même vitesse, la norme de la vitesse à l'altitude $z$ vérifie $v^2=v_0^2-2gz$ pour les deux angles, soit $v\approx\sqrt{400-196{,}2}\approx14{,}3~\mathrm{m/s}$. Seule la **direction** d'arrivée diffère (jet plus plongeant pour le tir en cloche).


**q2.** - [(d)] Déterminer les points d'intersection de la parabole de sûreté avec le sol et avec l'axe $Oz$, et leur signification physique.
- [(e)] Pour un point $P(x,z_s(x))$ de la parabole de sûreté, déterminer l'unique angle de tir. Vérifier que la trajectoire correspondante est **tangente** à la parabole de sûreté en $P$.

> [!tip]- 💡 Coup de pouce
> Pour (e), à $\Delta=0$ la racine double est $u=-B/(2A)$. Pour la tangence, comparez la pente $\mathrm dz/\mathrm dx$ de la trajectoire en $P$ avec celle de $z_s$.


> [!success]- ✅ Correction
> $z_s(0)=\dfrac{v_0^2}{2g}$ (hauteur maximale, tir vertical) ; $z_s(x)=0$ en $x=\dfrac{v_0^2}{g}$ (portée maximale, $\alpha=45^\circ$). Sur la parabole : $\tan\alpha=\dfrac{v_0^2}{g\,x}$. Les deux courbes ont la même pente $-\dfrac{g x}{v_0^2}$ en $P$.


> [!example]- 📝 Solution détaillée
> **(d) Intersections avec les axes**
>
> En $x=0$ : $z_s(0)=\dfrac{v_0^2}{2g}\approx20{,}4$ m : c'est la hauteur maximale atteignable, par un tir vertical.
>
> En $z_s(x)=0$ : $x^2=\dfrac{v_0^4}{g^2}$, soit $x=\dfrac{v_0^2}{g}\approx40{,}8$ m : c'est la portée maximale, obtenue pour $\alpha=45^\circ$ (cohérent avec l'exercice « balle de golf »).
>
> **(e) Angle sur la frontière et tangence**
>
> Sur la parabole, $\Delta=0$ et la racine double vaut
> $$u=-\frac{B}{2A}=\frac{x}{2k}=\frac{x\cdot2v_0^2}{2g\,x^2}=\boxed{\frac{v_0^2}{g\,x}}.$$
> Pente de la trajectoire en $x$ : $\dfrac{\mathrm dz}{\mathrm dx}=u-\dfrac{g x}{v_0^2}(1+u^2)$. Avec $u=\dfrac{v_0^2}{g x}$ :
> $$\frac{g x}{v_0^2}\,u^2=\frac{v_0^2}{g x},\qquad\text{donc}\qquad\frac{\mathrm dz}{\mathrm dx}=\frac{v_0^2}{g x}-\frac{g x}{v_0^2}-\frac{v_0^2}{g x}=-\frac{g x}{v_0^2}.$$
> Pente de la parabole de sûreté : $z_s'(x)=-\dfrac{g x}{v_0^2}$. Les pentes sont égales et les courbes ont le point $P$ en commun : elles sont **tangentes**. Chaque trajectoire touche la parabole en un point, qui est son point le plus « avancé » dans la zone atteignable.


**q3.** Le jet est maintenant dirigé vers un talus plan, montant, faisant l'angle $\beta=30^\circ$ avec l'horizontale (le plan du talus contient l'axe $Ox$ et la direction de plus grande pente). On note $d$ la distance, mesurée le long du talus, entre $O$ et le point d'impact.


- [(f)] Exprimer $d$ en fonction de $v_0$, $g$, $\alpha$ et $\beta$.
- [(g)] Déterminer l'angle $\alpha^\star$ qui maximise $d$ et la portée maximale $d_{\max}$ ; application numérique. Que devient le résultat sur un talus **descendant** de même angle ?
- [(h)] Retrouver $d_{\max}$ en utilisant la parabole de sûreté, et interpréter géométriquement $\alpha^\star$.

> [!tip]- 💡 Coup de pouce
> Le point d'impact est sur le talus : $(x,z)=(d\cos\beta,\,d\sin\beta)$. Reportez dans l'équation de trajectoire et simplifiez par $d\ne0$. Utilisez ensuite $2\cos\alpha\sin(\alpha-\beta)=\sin(2\alpha-\beta)-\sin\beta$. Pour (h), cherchez l'intersection de la droite $z=x\tan\beta$ avec $z_s(x)$.


> [!success]- ✅ Correction
> $d(\alpha)=\dfrac{2v_0^2\cos\alpha\sin(\alpha-\beta)}{g\cos^2\beta}$ ; $\alpha^\star=\dfrac\pi4+\dfrac\beta2=60^\circ$, $d_{\max}=\dfrac{v_0^2}{g(1+\sin\beta)}\approx27{,}2$ m ; en descente : $\alpha^\star=30^\circ$ et $d_{\max}=\dfrac{v_0^2}{g(1-\sin\beta)}\approx81{,}5$ m.


> [!example]- 📝 Solution détaillée
> **(f) Portée sur la pente**
>
> En reportant $x=d\cos\beta$, $z=d\sin\beta$ dans $z=x\tan\alpha-\dfrac{g x^2}{2v_0^2\cos^2\alpha}$ et en divisant par $d\ne0$ :
> $$\sin\beta=\cos\beta\tan\alpha-\frac{g\,d\cos^2\beta}{2v_0^2\cos^2\alpha}.$$
> D'où
> $$d=\frac{2v_0^2\cos^2\alpha\,(\cos\beta\tan\alpha-\sin\beta)}{g\cos^2\beta}=\boxed{\frac{2v_0^2\cos\alpha\,\sin(\alpha-\beta)}{g\cos^2\beta}}.$$
> Pour $\beta=0$, on retrouve $d=\dfrac{v_0^2\sin2\alpha}{g}$.
>
> **(g) Angle optimal et portée maximale**
>
> On linéarise : $2\cos\alpha\sin(\alpha-\beta)=\sin(2\alpha-\beta)-\sin\beta$. Ce terme est maximal quand $\sin(2\alpha-\beta)=1$, soit $2\alpha-\beta=\dfrac\pi2$ :
> $$\boxed{\alpha^\star=\frac\pi4+\frac\beta2},\qquad d_{\max}=\frac{v_0^2\,(1-\sin\beta)}{g\cos^2\beta}=\boxed{\frac{v_0^2}{g\,(1+\sin\beta)}},$$
> en utilisant $\cos^2\beta=(1-\sin\beta)(1+\sin\beta)$.
>
> Application : $\beta=30^\circ$, $\alpha^\star=45^\circ+15^\circ=\mathbf{60^\circ}$ et $d_{\max}=\dfrac{40{,}77}{1{,}5}\approx\boxed{27{,}2~\text{m}}$ (contre $40{,}8$ m sur sol plat).
>
> **Talus descendant** : on remplace $\beta$ par $-\beta$. Alors $\alpha^\star=\dfrac\pi4-\dfrac\beta2=30^\circ$ et $d_{\max}=\dfrac{v_0^2}{g(1-\sin\beta)}\approx\boxed{81{,}5~\text{m}}$, soit exactement $3$ fois la portée en montée : le rapport vaut $\dfrac{1+\sin\beta}{1-\sin\beta}=3$ pour $\beta=30^\circ$.
>
> **(h) Méthode par la parabole de sûreté ; interprétation**
>
> Le point d'impact le plus lointain sur le talus est le point où la droite $z=x\tan\beta$ sort de la zone atteignable, c'est-à-dire où elle coupe la parabole de sûreté. Avec $X=\dfrac{g x}{v_0^2}$, l'équation $x\tan\beta=z_s(x)$ s'écrit
> $$X^2+2X\tan\beta-1=0\Longrightarrow X=\frac{1-\sin\beta}{\cos\beta},$$
> d'où $d_{\max}=\dfrac{x}{\cos\beta}=\dfrac{v_0^2}{g}\,\dfrac{1-\sin\beta}{\cos^2\beta}=\dfrac{v_0^2}{g\,(1+\sin\beta)}$ : même résultat, sans maximiser aucune fonction de $\alpha$.
>
> Interprétation : $\alpha^\star=\dfrac\pi4+\dfrac\beta2=\dfrac12\Big(\beta+\dfrac\pi2\Big)$ est l'angle de la **bissectrice** entre la direction de la pente (angle $\beta$) et la verticale (angle $\pi/2$) : pour tirer le plus loin sur une pente, on vise à mi-chemin entre la pente et le zénith.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex7-balle-rebondissante-et-paradoxe-de-zenon|Exercice 7 — Balle rebondissante et paradoxe de Zénon]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]]

