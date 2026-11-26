---
title: "Exercice 12 — (*) Équations horaires 2D ou 3D"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td1_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/test.pdf" target="_blank" rel="noopener">📄 PDF</a> · <a href="/pdfs/td1_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 12. (*) Équations horaires 2D ou 3D *(facultatif)*

*Difficulté ●●●●○ · ⏱ 45 min · Type : Entraînement / Approfondissement*

Un mobile assimilé à un point matériel $M$ est en mouvement dans un référentiel galiléen $\mathcal R$
d'origine $O$ et muni d'un repère cartésien $(Oxyz)$. Il est repéré par ses coordonnées cartésiennes
suivantes, dans six cas indépendants ($a,b,c$ désignant des constantes) :
$$
\begin{array}{llll}
1)\ \begin{cases}x=5t\\y=2\\z=15t\end{cases} &
2)\ \begin{cases}x=2\\y=0\\z=4t^2-8t\end{cases} &
3)\ \begin{cases}x=3\cos(10t)\\y=3\sin(10t)\\z=2\end{cases} \\[2em]
4)\ \begin{cases}x=at^2-bt+c\\y=2c\\z=0\end{cases} &
5)\ \begin{cases}x=3\cos(2t^2)\\y=3\sin(2t^2)\\z=0\end{cases} &
6)\ \begin{cases}x=2t\cos(4t)\\y=2t\sin(4t)\\z=0\end{cases}
\end{array}
$$
Déterminer, pour chaque cas, le vecteur position, le vecteur vitesse et le vecteur accélération du point $M$,
ainsi que leur norme, et caractériser le mouvement obtenu.


> [!question]- 🪝 Accroche
> **Lire un mouvement dans une formule**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *On vous donne six formules, sans dessin. En 10 secondes, peut-on dire sans rien dériver lesquelles décrivent une droite, un cercle, une spirale ? Que signifie « $\cos(2t^2)$ » : un cercle parcouru de plus en plus vite ? Quel mouvement est-il le plus facile à reconnaître dans quel repère ?*
>
> **Idée clé : savoir lire une loi horaire avant de la dériver.** Pour un mouvement plan, on identifie $r(t)=\sqrt{x^2+y^2}$ et $\theta(t)$ tels que $x=r\cos\theta$, $y=r\sin\theta$ :
>
>
> - $r$ constant, $\dot\theta$ constant : **cercle parcouru uniformément** ;
> - $r$ constant, $\dot\theta$ variable : **cercle parcouru non uniformément** (accélération tangentielle en plus de la centripète) ;
> - $r$ croissant, $\dot\theta$ constant : **spirale** ;
> - toutes les coordonnées affines ou quadratiques en $t$ : **mouvement rectiligne** uniforme ou uniformément varié.
>
>
> La méthode de calcul est unique (dériver terme à terme) ; la difficulté vient de la **dérivée d'un produit** et de la **dérivée composée**.




> [!abstract]- 🧠 À savoir avant
> **Boîte à outils de dérivation cartésienne**
>
> En base cartésienne fixe $(\vec\imath,\vec\jmath,\vec k)$, on dérive terme à terme : $\vec v=\dot x\,\vec\imath+\dot y\,\vec\jmath+\dot z\,\vec k$ et $\vec a = \ddot x\,\vec\imath+\ddot y\,\vec\jmath+\ddot z\,\vec k$, avec $\|\vec v\|=\sqrt{\dot x^2+\dot y^2+\dot z^2}$ et $\|\vec a\|=\sqrt{\ddot x^2+\ddot y^2+\ddot z^2}$. Il faut maîtriser la dérivation d'un produit de fonctions du temps (règle de Leibniz), utile dès que $t$ apparaît à la fois en facteur et à l'intérieur d'un $\cos$ ou d'un $\sin$ (cas 5 et 6 ci-dessous).
>
> **Décomposition polaire d'un mouvement plan**
>
> Pour un mouvement plan, il est souvent instructif de repérer $r(t)=\|\overrightarrow{OM}\|$ et $\theta(t)$ tels que $x=r\cos\theta$, $y=r\sin\theta$, même si le calcul est mené in fine en cartésien : cela permet d'anticiper et de vérifier les résultats obtenus, notamment via $\|\vec v\|^2 = \dot r^2 + r^2\dot\theta^2$ et les composantes radiale/orthoradiale de l'accélération, $a_r = \ddot r - r\dot\theta^2$ et $a_\theta = r\ddot\theta+2\dot r\dot\theta$ (résultats de cours qui seront redémontrés plus tard, mais utilisables ici comme moyen de vérification).




> [!info]- 🎯 Ce que tu sauras faire
> **Automatiser le calcul vectoriel et reconnaître des mouvements-types**
>
> Savoir dériver rapidement et sans erreur des lois horaires variées (y compris avec $t$ apparaissant à plusieurs endroits, cas 5 et 6), et surtout savoir **reconnaître, derrière le calcul**, un mouvement-type déjà rencontré (rectiligne uniforme, rectiligne uniformément varié, circulaire uniforme) ou un mouvement nouveau (circulaire non uniforme, spirale) qui anticipe les prochains chapitres du cours.




> [!info]- 🧑‍🏫 Objectifs pédagogiques
> **Exercice de synthèse et de reconnaissance de formes**
>
> Cet exercice, plus long et facultatif, vise à entraîner le réflexe de calcul mais surtout la **lecture physique** d'une loi horaire : au-delà du résultat brut, on attend des étudiants qu'ils identifient à chaque fois la nature du mouvement (translation uniforme, MRUV, circulaire uniforme ou non, spirale). Les cas 5 et 6, plus délicats (dérivée d'un produit avec argument variable dans le cosinus/sinus), sont volontairement placés en fin d'exercice et gagnent à être reliés, en aparté, aux formules polaires $a_r, a_\theta$ vues en cours, sans exiger leur redémonstration ici.




> [!tip]- 📖 Rappel de cours
> **Circulaire uniforme vs. circulaire non uniforme**
>
> Un mouvement à trajectoire circulaire ($r=$ cte) est **uniforme** si $\dot\theta=\omega$ est constant (cas 3), et **non uniforme** si $\dot\theta$ varie avec le temps (cas 5, où $\theta(t)=2t^2$ donne $\dot\theta=4t$, croissant) : dans ce dernier cas apparaît une accélération tangentielle non nulle, en plus de l'accélération centripète.




> [!note]- 🧮 Outils mathématiques
> **Dérivée d'un produit : $(uv)'=u'v+uv'$**
>
> Pour $x=2t\cos(4t)$ : $\dot x=2\cos(4t)+2t\,\dot{(\cos4t)}=2\cos(4t)-8t\sin(4t)$. Oublier le facteur $2t$ à l'extérieur est l'erreur classique.
>
> **Dérivée composée : $\dfrac{\mathrm d}{\mathrm dt}\cos(g(t))=-g'(t)\sin(g(t))$**
>
> Pour $\cos(2t^2)$ : $g'=4t$, donc $\dot x=-12t\sin(2t^2)$ après le facteur $3$. On dérive « de l'extérieur vers l'intérieur » : la dérivée de la fonction extérieure fois la dérivée de l'argument.
>
> **Passage cartésien $\leftrightarrow$ polaire**
>
> $r=\sqrt{x^2+y^2}$, $\tan\theta=y/x$, $x=r\cos\theta$, $y=r\sin\theta$. L'identité $\cos^2+\sin^2=1$ donne immédiatement $r$ dans les cas 3, 5 et 6.
>
> **Pythagore vectoriel**
>
> En polaire $\|\vec v\|^2=\dot r^2+r^2\dot\theta^2$ : deux composantes perpendiculaires (radiale et orthoradiale) se composent comme les côtés d'un triangle rectangle. Idem pour $\|\vec a\|^2=a_r^2+a_\theta^2$.
>
> **Mettre en facteur sous une racine**
>
> $\sqrt{144+2304t^4}=\sqrt{144\,(1+16t^4)}=12\sqrt{1+16t^4}$ : sortir le facteur commun donne une expression lisible et montre le comportement aux temps courts et longs ($\to12$ en $t=0$, $\sim48t^2$ pour $t$ grand).
>
> **Primitive et phase : de $\dot\theta$ à $\theta$**
>
> $\theta(t)=\displaystyle\int\dot\theta\,\mathrm dt$ : si $\dot\theta=4t$, alors $\theta=2t^2+\theta_0$. Inversement, lire $\theta=2t^2$ donne $\dot\theta=4t$ (la vitesse angulaire croît linéairement).



**q1.** Cas 1 : $x(t) = 5t$, $y(t)=2$, $z(t)=15t$ (unités SI). Déterminer $\overrightarrow{OM}(t)$, $\vec v(t)$, $\vec a(t)$ et leurs normes ; caractériser le mouvement.


> [!tip]- 💡 Coup de pouce
> Toutes les coordonnées sont des fonctions affines de $t$ : quel type de mouvement cela évoque-t-il ?




> [!success]- ✅ Correction
> $\vec v=(5,0,15)$ constant, $\vec a=\vec 0$ : mouvement rectiligne uniforme, $\|\vec v\|=5\sqrt{10}\approx15{,}8$ m/s.




> [!example]- 📝 Solution détaillée
> **Vecteurs position, vitesse, accélération**
>
> $$\overrightarrow{OM}(t) = 5t\,\vec\imath + 2\,\vec\jmath + 15t\,\vec k.$$
> En dérivant chaque composante (constante $y=2$ donc $\dot y=0$) :
> $$\vec v(t) = 5\,\vec\imath + 15\,\vec k \quad (\text{constant}), \qquad \vec a(t) = \vec 0.$$
> $$\|\vec v\| = \sqrt{5^2+15^2} = \sqrt{250} = 5\sqrt{10} \approx 15{,}8~\text{m/s}, \qquad \|\vec a\| = 0.$$
>
> **Nature du mouvement**
>
> Les trois coordonnées étant des fonctions affines de $t$ (dont $y$ constante), le vecteur vitesse est constant et l'accélération est nulle : il s'agit d'un **mouvement rectiligne uniforme**, le long de la droite de vecteur directeur $5\,\vec\imath+15\,\vec k$, à l'altitude fixe $y=2$.



**q2.** Cas 2 : $x(t)=2$, $y(t)=0$, $z(t)=4t^2-8t$ (unités SI). Déterminer $\overrightarrow{OM}(t)$, $\vec v(t)$, $\vec a(t)$ et leurs normes ; caractériser le mouvement.


> [!tip]- 💡 Coup de pouce
> Seule la coordonnée $z$ varie, et de façon quadratique : quel est le mouvement le long de $Oz$ ?




> [!success]- ✅ Correction
> $\vec v=(0,0,8t-8)$, $\vec a=(0,0,8)$ constant : mouvement rectiligne uniformément accéléré le long de $Oz$, avec inversion du sens du mouvement à $t=1$ s.




> [!example]- 📝 Solution détaillée
> **Vecteurs position, vitesse, accélération**
>
> $$\overrightarrow{OM}(t) = 2\,\vec\imath + (4t^2-8t)\,\vec k.$$
> $$\vec v(t) = (8t-8)\,\vec k, \qquad \vec a(t) = 8\,\vec k \quad (\text{constant}).$$
> $$\|\vec v(t)\| = |8t-8|, \qquad \|\vec a\| = 8~\text{m/s}^2.$$
>
> **Nature du mouvement**
>
> Les coordonnées $x=2$ et $y=0$ sont constantes : le point $M$ se déplace uniquement le long de la droite verticale $x=2, y=0$ (parallèle à $Oz$). C'est un **mouvement rectiligne uniformément accéléré** ($\vec a$ constant), avec une vitesse initiale $\vec v(0) = -8\,\vec k$ (le mobile part donc vers les $z$ décroissants), qui s'annule à $t=1$ s puis change de signe : le mobile ralentit, s'arrête un instant à $z=4-8=-4$ m, puis repart en sens inverse (vers les $z$ croissants), avec une accélération constante orientée vers $+\vec k$ tout du long.



**q3.** Cas 3 : $x(t)=3\cos(10t)$, $y(t)=3\sin(10t)$, $z(t)=2$ (unités SI). Déterminer $\overrightarrow{OM}(t)$, $\vec v(t)$, $\vec a(t)$ et leurs normes ; caractériser le mouvement.


> [!tip]- 💡 Coup de pouce
> C'est le mouvement circulaire de l'exercice 3, mais décalé le long de $Oz$.




> [!success]- ✅ Correction
> Mouvement circulaire uniforme de rayon $R=3$ m, $\omega=10$ rad/s, dans le plan $z=2$. $\|\vec v\|=30$ m/s, $\|\vec a\|=300$ m/s².




> [!example]- 📝 Solution détaillée
> **Vecteurs position, vitesse, accélération**
>
> $$\overrightarrow{OM}(t) = 3\cos(10t)\,\vec\imath + 3\sin(10t)\,\vec\jmath + 2\,\vec k.$$
> $$\vec v(t) = -30\sin(10t)\,\vec\imath + 30\cos(10t)\,\vec\jmath \quad (\text{composante suivant } \vec k \text{ nulle, car } z \text{ constant}).$$
> $$\vec a(t) = -300\cos(10t)\,\vec\imath - 300\sin(10t)\,\vec\jmath = -100\big(x\,\vec\imath+y\,\vec\jmath\big).$$
> $$\|\vec v\| = \sqrt{900\sin^2(10t)+900\cos^2(10t)} = 30~\text{m/s} \ (\text{constant}), \qquad \|\vec a\| = 300~\text{m/s}^2 \ (\text{constant}).$$
>
> **Nature du mouvement**
>
> Dans le plan horizontal $z=2$, on reconnaît exactement la structure de l'exercice 3 ($R=3$ m, $\omega=10$ rad/s) : c'est un **mouvement circulaire uniforme**, de rayon $3$ m, parcouru à vitesse angulaire constante $10$ rad/s, dans le plan $z=2$ (l'axe du cercle est donc la droite $x=0,y=0$, parallèle à $Oz$). L'accélération, purement centripète, vérifie $\vec a=-\omega^2(\overrightarrow{OM}-2\vec k)$, pointant à chaque instant vers l'axe du cercle.



**q4.** Cas 4 : $x(t)=at^2-bt+c$, $y(t)=2c$, $z(t)=0$ ($a,b,c$ constantes). Déterminer $\overrightarrow{OM}(t)$, $\vec v(t)$, $\vec a(t)$ et leurs normes ; caractériser le mouvement.


> [!tip]- 💡 Coup de pouce
> Comparez à l'exercice 1, question 1 : ici c'est $Ox$ qui joue le rôle de l'axe du mouvement quadratique.




> [!success]- ✅ Correction
> $\vec v=(2at-b)\,\vec\imath$, $\vec a=2a\,\vec\imath$ constant : mouvement rectiligne uniformément accéléré le long de la droite $y=2c$, $z=0$.




> [!example]- 📝 Solution détaillée
> **Vecteurs position, vitesse, accélération**
>
> $$\overrightarrow{OM}(t) = (at^2-bt+c)\,\vec\imath + 2c\,\vec\jmath.$$
> $$\vec v(t) = (2at-b)\,\vec\imath \quad (\text{car } y, z \text{ constants}), \qquad \vec a(t) = 2a\,\vec\imath \quad (\text{constant}).$$
> $$\|\vec v(t)\| = |2at-b|, \qquad \|\vec a\| = 2|a|.$$
>
> **Nature du mouvement**
>
> Les coordonnées $y=2c$ et $z=0$ étant constantes, le mouvement est entièrement contenu sur la droite parallèle à $Ox$ passant par le point $(0,2c,0)$. La coordonnée $x(t)$ étant quadratique en $t$, à accélération $2a$ constante, il s'agit d'un **mouvement rectiligne uniformément varié** le long de cette droite (accéléré ou décéléré selon les signes relatifs de $a$ et de la vitesse instantanée $2at-b$), analogue à la situation étudiée en question 1(f) de l'exercice 1, mais ici le long de $Ox$ plutôt que de $Oy$.



**q5.** Cas 5 : $x(t)=3\cos(2t^2)$, $y(t)=3\sin(2t^2)$, $z(t)=0$ (unités SI). Déterminer $\overrightarrow{OM}(t)$, $\vec v(t)$, $\vec a(t)$ et leurs normes ; caractériser le mouvement.


> [!tip]- 💡 Coup de pouce
> Posez $\\theta(t)=2t^2$ : la trajectoire est-elle circulaire ? La vitesse angulaire $\dot\theta$ est-elle constante ?




> [!success]- ✅ Correction
> Mouvement circulaire de rayon 3 m, mais **non uniforme** ($\dot\theta=4t$ croissant) : $\|\vec v\|=12t$, $\|\vec a\|=\sqrt{144+2304t^4}=12\sqrt{1+16t^4}$.




> [!example]- 📝 Solution détaillée
> **Repérage polaire : rayon constant, angle non linéaire**
>
> On remarque que $x^2+y^2 = 9\cos^2(2t^2)+9\sin^2(2t^2) = 9$ : la trajectoire est donc bien un **cercle de rayon $R=3$ m**, mais avec un angle polaire $\theta(t) = 2t^2$ qui **n'est pas linéaire en $t$** : la vitesse angulaire $\dot\theta(t) = 4t$ croît avec le temps, le mouvement circulaire n'est donc pas uniforme.
>
> **Vecteur vitesse (dérivée d'un produit avec argument variable)**
>
> Il faut dériver un produit, l'argument du cosinus/sinus dépendant lui-même de $t$ :
> $$v_x = \frac{\mathrm d}{\mathrm dt}\big(3\cos(2t^2)\big) = -3\sin(2t^2)\cdot 4t = -12t\sin(2t^2),$$
> $$v_y = \frac{\mathrm d}{\mathrm dt}\big(3\sin(2t^2)\big) = 3\cos(2t^2)\cdot 4t = 12t\cos(2t^2).$$
> $$\vec v(t) = -12t\sin(2t^2)\,\vec\imath + 12t\cos(2t^2)\,\vec\jmath, \qquad \|\vec v\| = 12t\sqrt{\sin^2(2t^2)+\cos^2(2t^2)} = \boxed{12t}~\text{m/s (pour }t\geq0\text{)}.$$
> On retrouve directement ce résultat via $\|\vec v\| = R\dot\theta = 3\times 4t = 12t$ (vitesse purement orthoradiale puisque $R$ est constant, $\dot R=0$).
>
> **Vecteur accélération (par dérivation directe, puis vérification polaire)**
>
> En dérivant à nouveau chaque composante (règle du produit à trois facteurs) :
> $$a_x = -12\sin(2t^2) - 12t\cdot\cos(2t^2)\cdot 4t = -12\sin(2t^2) - 48t^2\cos(2t^2),$$
> $$a_y = 12\cos(2t^2) - 12t\cdot\sin(2t^2)\cdot 4t = 12\cos(2t^2) - 48t^2\sin(2t^2).$$
> On vérifie ce résultat plus simplement grâce aux formules polaires (cf. « aller plus loin ») : $R$ constant ($\dot R=0$) donne une accélération purement tangentielle constante $a_t = R\ddot\theta = 3\times 4 = 12$ (le cercle est parcouru avec une accélération angulaire $\ddot\theta=4$ constante), et une accélération centripète $a_n = R\dot\theta^2 = 3\times(4t)^2 = 48t^2$, croissante avec $t$. D'où :
> $$\|\vec a\| = \sqrt{a_t^2+a_n^2} = \sqrt{12^2+(48t^2)^2} = \boxed{12\sqrt{1+16t^4}}~\text{m/s}^2.$$
>
> **Nature du mouvement**
>
> Il s'agit d'un **mouvement circulaire non uniforme** : la trajectoire est un cercle de rayon fixe (3 m), mais parcouru à vitesse angulaire croissante ($\dot\theta=4t$), donc à vitesse (en norme) elle-même croissante ($\|\vec v\|=12t$). Contrairement au cas 3, l'accélération possède ici une composante tangentielle non nulle (et constante, $a_t=12$ m/s²) en plus de la composante centripète (croissante, $a_n=48t^2$).



**q6.** Cas 6 : $x(t)=2t\cos(4t)$, $y(t)=2t\sin(4t)$, $z(t)=0$ (unités SI). Déterminer $\overrightarrow{OM}(t)$, $\vec v(t)$, $\vec a(t)$ et leurs normes ; caractériser le mouvement.


> [!tip]- 💡 Coup de pouce
> Ici $r(t)=\|\overrightarrow{OM}\|=2t$ n'est plus constant : ce n'est plus un cercle. Identifiez $r(t)$ et $\theta(t)$ pour interpréter le mouvement.




> [!success]- ✅ Correction
> Mouvement en spirale ($r=2t$, $\theta=4t$) : $\|\vec v\|=2\sqrt{1+16t^2}$, $\|\vec a\|=16\sqrt{1+4t^2}$.




> [!example]- 📝 Solution détaillée
> **Repérage polaire : rayon croissant, angle linéaire**
>
> On remarque que $\sqrt{x^2+y^2} = 2t\sqrt{\cos^2(4t)+\sin^2(4t)} = 2t$ : le point $M$ s'éloigne donc de $O$ proportionnellement au temps ($r(t)=2t$), tout en tournant à vitesse angulaire constante $\dot\theta=4$ rad/s ($\theta(t)=4t$). Il ne s'agit donc plus d'un cercle mais d'une **spirale**.
>
> **Vecteur vitesse**
>
> Par dérivation d'un produit (deux facteurs dépendant de $t$) :
> $$v_x = 2\cos(4t) + 2t\times(-4\sin(4t)) = 2\cos(4t) - 8t\sin(4t),$$
> $$v_y = 2\sin(4t) + 2t\times 4\cos(4t) = 2\sin(4t) + 8t\cos(4t).$$
> $$\vec v(t) = \big(2\cos(4t)-8t\sin(4t)\big)\vec\imath + \big(2\sin(4t)+8t\cos(4t)\big)\vec\jmath.$$
> On peut vérifier ce résultat via la décomposition polaire $\vec v = \dot r\,\vec u_r + r\dot\theta\,\vec u_\theta$, avec ici $\dot r=2$ (composante radiale constante) et $r\dot\theta = 2t\times4=8t$ (composante orthoradiale croissante) :
> $$\|\vec v\| = \sqrt{\dot r^2 + (r\dot\theta)^2} = \sqrt{2^2+(8t)^2} = \boxed{2\sqrt{1+16t^2}}~\text{m/s}.$$
>
> **Vecteur accélération**
>
> Toujours via la décomposition polaire (avec $\ddot r=0$ puisque $\dot r=2$ est constant, et $\ddot\theta=0$ puisque $\dot\theta=4$ est constant) :
> $$a_r = \ddot r - r\dot\theta^2 = 0 - 2t\times16 = -32t, \qquad a_\theta = r\ddot\theta + 2\dot r\dot\theta = 0 + 2\times2\times4 = 16.$$
> $$\|\vec a\| = \sqrt{a_r^2+a_\theta^2} = \sqrt{(32t)^2+16^2} = \sqrt{1024t^2+256} = \boxed{16\sqrt{1+4t^2}}~\text{m/s}^2.$$
> (On peut vérifier que ce résultat coïncide avec celui obtenu en dérivant deux fois $x(t)$ et $y(t)$ directement en cartésien, calcul plus long mais équivalent.)
>
> **Nature du mouvement : une spirale**
>
> Le point $M$ décrit une **spirale** (spirale d'Archimède) : il s'éloigne de $O$ à vitesse radiale constante ($\dot r=2$ m/s) tout en tournant autour de $O$ à vitesse angulaire constante ($\dot\theta=4$ rad/s). Ni la norme de $\vec v$ ni celle de $\vec a$ ne sont constantes : elles croissent toutes deux avec $t$, à cause de l'augmentation continue du rayon $r(t)=2t$, qui amplifie la composante orthoradiale de la vitesse ($r\dot\theta$) et la composante centripète de l'accélération ($r\dot\theta^2$), bien que les grandeurs "purement radiales" ($\dot r$ et $a_\theta$, ici constantes) restent, elles, inchangées au cours du temps.




> [!note]- 🔗 Liens avec d'autres disciplines
> **Mathématiques**
>
> Courbes en coordonnées polaires, spirale d'Archimède $r=k\theta$ (ici $r=\theta/2$), dérivées d'un produit et composition de fonctions.
>
> **Traitement du signal / ondes**
>
> $\cos(2t^2)$ est un signal de phase quadratique : sa fréquence instantanée $\dot\theta/2\pi=4t/2\pi$ augmente linéairement avec le temps. C'est un « chirp », utilisé en radar, en sonar, par les chauves-souris, et observé dans le signal des ondes gravitationnelles.
>
> **Technologie**
>
> Le sillon d'un disque vinyle, l'enroulement d'un ruban sur une bobine, le ressort spiral d'une montre : spirales d'Archimède.
>
> **Mécanique**
>
> Cas 3 : un volant de rayon $3$ m à $\omega=10$ rad/s subirait $300$ m/s², soit $\approx30\,g$, ce qui montre pourquoi les pièces tournantes sont limitées en vitesse.




> [!warning]- 🪤 Écueils classiques
> **Dériver $t\cos(\omega t)$ comme si $t$ n'apparaissait qu'une fois**
>
> Dans les cas 5 et 6, une erreur très fréquente consiste à dériver uniquement l'argument du cosinus/sinus (comme au cas 3) en oubliant le facteur $t$ ou $2t$ multiplicatif à l'extérieur, qui impose une **dérivée de produit** : $\frac{\mathrm d}{\mathrm dt}\big(f(t)\cos(g(t))\big) = f'(t)\cos(g(t)) - f(t)g'(t)\sin(g(t))$.




> [!success]- 🏁 Bilan pédagogique
> **Une même méthode, des mouvements très variés**
>
> Cet exercice montre qu'une méthode unique et systématique (dérivation cartésienne terme à terme) permet de traiter des mouvements de natures très différentes : translation uniforme (cas 1), MRUV rectiligne (cas 2 et 4), circulaire uniforme (cas 3), circulaire non uniforme (cas 5), et spirale (cas 6). La difficulté n'est donc pas dans la méthode elle-même, mais dans la rigueur du calcul de dérivée et dans l'interprétation physique du résultat obtenu.




> [!question]- 🔭 Aller plus loin — CPGE : Retrouver les cas 3, 5 et 6 en coordonnées polaires
> On pourra reprendre les cas 3, 5 et 6 en identifiant $r(t)$ et $\theta(t)$, puis en utilisant directement les formules polaires $\vec v = \dot r\,\vec u_r + r\dot\theta\,\vec u_\theta$ et $\vec a = (\ddot r - r\dot\theta^2)\vec u_r + (r\ddot\theta+2\dot r\dot\theta)\vec u_\theta$ (établies plus tard dans le cours), pour constater que les normes obtenues coïncident avec celles calculées ici en cartésien, tout en simplifiant considérablement les calculs intermédiaires.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]]


