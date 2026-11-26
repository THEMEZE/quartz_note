---
title: "Exercice 3 — Course automobile : rattrapage de deux mobiles"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td1_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/test.pdf" target="_blank" rel="noopener">📄 PDF</a> · <a href="/pdfs/td1_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 3. Course automobile : rattrapage de deux mobiles *(facultatif)*

*Difficulté ●●○○○ · ⏱ 20 min · Type : Entraînement / Exercice non guidé*

Deux pilotes amateurs prennent le départ d'une course sur une longue ligne droite, depuis la même
ligne de départ. Le pilote $A$ démarre à $t=0$ s avec une accélération $a_A = 4~\mathrm{m\,s^{-2}}$.
Le pilote $B$, dont la voiture est plus puissante, démarre avec une accélération $a_B = 5~\mathrm{m\,s^{-2}}$.
$A$ a cependant plus de réflexes que $B$ et démarre une seconde avant lui.
On suppose que les deux voitures partent du repos et que leurs accélérations restent constantes.


> [!question]- 🪝 Accroche
> **Celui qui part en retard peut-il rattraper celui qui part en avance ?**
>
> *Durée de l'introduction : 3 à 5 min, avant de lire l'énoncé*
>
> *Dans une course en ligne droite, un pilote A part une seconde avant son rival B, mais B a une voiture plus puissante. **Qui est devant au bout de 3 secondes ? de 10 secondes ?** Le plus puissant gagne-t-il « tout de suite » ? Peut-on prévoir l'instant exact du dépassement, et même savoir s'il aura lieu ?*
>
> **Idée clé : une loi horaire n'est valable qu'à partir de l'instant de départ.** Pour un mouvement rectiligne uniformément accéléré partant du repos à $t_d$ :
> $$v(t)=a\,(t-t_d),\qquad x(t)=\tfrac12\,a\,(t-t_d)^2\qquad(t\ge t_d).$$
> Le décalage temporel s'applique à la **variable $t$** (on remplace $t$ par $t-t_d$) et non au résultat. « Se rencontrer » signifie **avoir la même abscisse au même instant** : $x_A(t^\star)=x_B(t^\star)$. Une équation du second degré donne deux racines, et **la physique décide** laquelle garder.




> [!abstract]- 🧠 À savoir avant
> **Mouvement rectiligne uniformément accéléré (MRUA)**
>
> Pour un mouvement sur un axe $Ox$ d'accélération constante $a$, partant du repos en $x=0$ à l'instant $t_d$ :
> $$v(t) = a\,(t-t_d), \qquad x(t) = \tfrac{1}{2}\,a\,(t-t_d)^2 \qquad (t \ge t_d).$$
> Avant $t_d$, le mobile est immobile en $x=0$. La loi horaire n'est valable qu'à partir de l'instant de départ.




> [!info]- 🎯 Ce que tu sauras faire
> **Modéliser une situation de rattrapage**
>
> Savoir écrire les lois horaires de deux mobiles avec des origines des temps différentes, poser la condition de rencontre $x_A(t)=x_B(t)$, résoudre l'équation obtenue et **discriminer les solutions physiquement acceptables**.




> [!info]- 🧑‍🏫 Objectifs pédagogiques
> **Exercice non guidé : poser soi-même le problème**
>
> Aucune sous-question n'est donnée : l'étudiant doit choisir l'origine des temps, écrire les deux lois horaires, traduire « B rattrape A » par une égalité de positions, résoudre une équation du second degré et interpréter les deux racines. C'est un bon exercice pour évaluer l'autonomie de modélisation.




> [!tip]- 📖 Rappel de cours
> **Condition de rencontre**
>
> Deux mobiles se rencontrent à l'instant $t^\star$ si et seulement si leurs abscisses coïncident : $x_A(t^\star)=x_B(t^\star)$. Une équation du second degré fournit en général deux racines ; il faut vérifier que chacune est compatible avec le domaine de validité des lois horaires utilisées.




> [!note]- 🧮 Outils mathématiques
> **Translation d'une fonction : $f(t-\tau)$**
>
> Le graphe de $t\mapsto f(t-\tau)$ est celui de $f$ **décalé de $\tau$ vers la droite** (retard). C'est exactement ce qui se passe pour $x_B(t)=\tfrac12a_B(t-1)^2$ par rapport à $\tfrac12a_Bt^2$.
>
> **Équation du second degré**
>
> $\alpha t^2+\beta t+\gamma=0\Rightarrow\Delta=\beta^2-4\alpha\gamma$ et $t=\dfrac{-\beta\pm\sqrt\Delta}{2\alpha}$. Les deux racines sont les abscisses des points d'intersection de deux paraboles ; toute racine doit être confrontée au domaine de validité ($t\ge1$ s ici).
>
> **Égalité de carrés et identité remarquable**
>
> $A^2=B^2\iff(A-B)(A+B)=0$. Ici $2t^2=2{,}5(t-1)^2$ devient $\sqrt{a_A}\,t=\pm\sqrt{a_B}\,(t-1)$ : le signe $+$ donne la racine physique, le signe $-$ la racine parasite. Le passage à la racine carrée fait donc le tri automatiquement.
>
> **Extremum par la dérivée**
>
> L'écart $d(t)=x_A-x_B$ est maximal quand $\dot d=0$, c'est-à-dire quand $v_A=v_B$. Un extremum se trouve là où la dérivée s'annule et change de signe.
>
> **Intégrale : l'aire sous la courbe $v(t)$**
>
> $x(t)=\displaystyle\int_{t_d}^{t}v(t')\,\mathrm dt'$. Avec $v=a(t'-t_d)$, l'aire est celle d'un **triangle** : $\tfrac12\times(t-t_d)\times a(t-t_d)=\tfrac12a(t-t_d)^2$. On retrouve la loi horaire sans calcul.



**q1.** À quel instant le pilote $B$ rattrape-t-il le pilote $A$ ?


> [!tip]- 💡 Coup de pouce
> Choisissez une origine des temps unique (le départ de $A$), écrivez la loi horaire de chaque voiture en tenant compte de l'instant de départ de $B$, puis traduisez « $B$ rattrape $A$ » par une égalité de positions.




> [!success]- ✅ Correction
> $t^\star = 5+2\sqrt5 \approx 9{,}5$ s après le départ de $A$ (soit $\approx 8{,}5$ s après le départ de $B$), à $\approx 179$ m de la ligne de départ.




> [!example]- 📝 Solution détaillée
> **Choix du repère et lois horaires**
>
> On choisit l'axe $Ox$ le long de la piste, orienté dans le sens de la course, l'origine $O$ sur la ligne de départ, et l'origine des temps au démarrage de $A$. Les deux voitures partent du repos avec des accélérations constantes :
> $$x_A(t) = \tfrac12\,a_A\,t^2 = 2\,t^2 \qquad (t\ge0),$$
> $$x_B(t) = \tfrac12\,a_B\,(t-1)^2 = 2{,}5\,(t-1)^2 \qquad (t\ge1~\mathrm{s}).$$
> Le décalage d'une seconde est appliqué à la variable temps de la loi horaire de $B$.
>
> **Condition de rattrapage**
>
> $B$ rattrape $A$ quand $x_A(t^\star)=x_B(t^\star)$ avec $t^\star\ge1$ s :
> $$2\,t^2 = 2{,}5\,(t-1)^2 \;\Longleftrightarrow\; 0{,}5\,t^2-5\,t+2{,}5=0 \;\Longleftrightarrow\; t^2-10\,t+5=0.$$
> Le discriminant vaut $\Delta=100-20=80$, d'où
> $$t=\frac{10\pm\sqrt{80}}{2}=5\pm2\sqrt5 .$$
>
> **Tri des racines**
>
> La racine $5-2\sqrt5\approx0{,}53$ s est inférieure à $1$ s : à cet instant $B$ n'a pas encore démarré et la loi $x_B(t)=2{,}5(t-1)^2$ n'est pas applicable. On la rejette. Il reste
> $$\boxed{t^\star = 5+2\sqrt5 \approx 9{,}47~\text{s}}.$$
>
> **Méthode alternative par racines carrées**
>
> Comme les deux positions sont positives, $x_A=x_B$ équivaut à $\sqrt{a_A}\,t=\sqrt{a_B}\,(t-1)$ pour $t\ge1$, soit
> $$t^\star=\frac{\sqrt{a_B}}{\sqrt{a_B}-\sqrt{a_A}}=\frac{1}{1-2/\sqrt5}=\frac{\sqrt5}{\sqrt5-2}=5+2\sqrt5 .$$
> Cette méthode ne fait apparaître que la racine physique.
>
> **Vérification et commentaires**
>
> Position de rencontre : $x_A(t^\star)=2\,(5+2\sqrt5)^2=90+40\sqrt5\approx179~\text{m}$. Vérification avec $B$ : $2{,}5\times(4+2\sqrt5)^2\approx2{,}5\times71{,}8\approx179~\text{m}$. $\surd$
>
> Vitesses au moment du dépassement : $v_A=a_A\,t^\star\approx37{,}9~\mathrm{m/s}\approx136$ km/h et $v_B=a_B\,(t^\star-1)\approx42{,}4~\mathrm{m/s}\approx153$ km/h. On a bien $v_B>v_A$ : $B$ dépasse effectivement $A$ au lieu de simplement le toucher.



**q2.** (*) Entraînement : à quel instant l'écart entre les deux voitures est-il maximal, et que vaut-il ?


> [!tip]- 💡 Coup de pouce
> L'écart $d(t)=x_A(t)-x_B(t)$ est maximal quand sa dérivée s'annule, c'est-à-dire quand les deux vitesses sont égales.




> [!success]- ✅ Correction
> L'écart est maximal à $t=5$ s et vaut $10$ m.




> [!example]- 📝 Solution détaillée
> **Écart maximal**
>
> Pour $t\ge1$, $d(t)=2t^2-2{,}5(t-1)^2$ et $\dot d(t)=v_A-v_B=4t-5(t-1)=5-t$. Cette dérivée s'annule en $t=5$ s, et $\dot d$ passe de positif à négatif : c'est un maximum. On a alors
> $$d_{\max}=2\times25-2{,}5\times16=50-40=10~\text{m}.$$
> Avant $t=5$ s, $A$ roule plus vite que $B$ et l'écart croît ; après, $B$ roule plus vite et l'écart se résorbe jusqu'à s'annuler en $t^\star\approx9{,}47$ s.




> [!note]- 🔗 Liens avec d'autres disciplines
> **Mathématiques**
>
> Intersection de deux courbes, discriminant, translation de graphe, aire sous une courbe.
>
> **Ondes et signaux**
>
> Le « retard » $t-\tau$ est le même que celui d'un signal qui se propage : $s(x,t)=f(t-x/c)$ en acoustique, optique, électronique (ligne à retard).
>
> **Sécurité routière**
>
> Distance de freinage $d=v^2/(2a)$ : même loi quadratique, qui explique pourquoi la distance de freinage quadruple quand la vitesse double.
>
> **Économie / gestion**
>
> « Rattraper un concurrent parti en avance » est un problème de croissance relative : le résultat dépend de l'écart entre les rythmes de croissance et du retard initial.




> [!warning]- 🪤 Écueils classiques
> **Écrire $x_B = \frac{1}{2}a_B t^2 - 1$ ou oublier le décalage au carré**
>
> Erreur très fréquente : retrancher la seconde de retard **à la position** ou écrire $\tfrac12 a_B t^2 - 1$, au lieu de remplacer $t$ par $(t-1)$ **dans la loi horaire**. Le décalage temporel s'applique à la variable $t$, pas au résultat.
>
> **Garder la racine non physique**
>
> L'équation du second degré admet deux racines, $t = 5 \pm 2\sqrt5$. La racine $5-2\sqrt5 \approx 0{,}53$ s est antérieure au départ de $B$ ($t<1$ s) : la loi horaire de $B$ n'y est pas valable. À rejeter explicitement.
>
> **Croire que le plus puissant gagne immédiatement**
>
> $B$ a une plus grande accélération mais part plus tard : l'écart initial se creuse d'abord, puis se résorbe. Faire tracer $x_A(t)$ et $x_B(t)$ pour visualiser que $B$ ne rattrape $A$ qu'après plusieurs secondes.




> [!tip]- 🎙️ Conseils d'animation
> **Deux méthodes, un seul résultat**
>
> Faire résoudre par deux groupes : l'un par l'équation du second degré, l'autre par passage à la racine carrée ($\sqrt{a_A}\,t = \sqrt{a_B}\,(t-1)$). Comparer les résultats et discuter pourquoi la seconde méthode supprime automatiquement la racine non physique.




> [!success]- 🏁 Bilan pédagogique
> **Rencontre de deux mobiles**
>
> Pour un problème de rattrapage : (1) choisir une origine des temps unique, (2) écrire chaque loi horaire en tenant compte de l'instant de départ, (3) poser $x_A=x_B$, (4) résoudre et vérifier que la solution appartient au domaine de validité de chaque loi. Ici $t^\star = 5+2\sqrt5 \approx 9{,}47$ s.




> [!question]- 🔭 Aller plus loin — Licence : Généralisation : retard $\tau$ et condition d'existence du rattrapage
> Pour un retard quelconque $\tau$ de $B$, la condition $\sqrt{a_A}\,t=\sqrt{a_B}\,(t-\tau)$ donne
> $$t^\star = \frac{\tau}{1-\sqrt{a_A/a_B}}.$$
> Le rattrapage n'existe que si $a_B>a_A$ ; si $a_B\le a_A$, $B$ ne rattrape jamais $A$. Discuter la limite $a_B\to a_A^{+}$ ($t^\star\to\infty$) et la limite $\tau\to0$ ($t^\star\to0$). Tracer la distance qui sépare les deux voitures en fonction du temps et déterminer l'instant où l'écart est maximal (c'est l'instant où $v_A=v_B$ : $4t = 5(t-1)$, soit $t=5$ s ; écart $=2\times25-2{,}5\times16=10$ m).




> [!question]- 🔭 Aller plus loin — Master : Une accélération constante est-elle réaliste ? Voiture à puissance constante
> La puissance du moteur est limitée. À puissance utile constante $P$, le théorème de l'énergie cinétique $\frac{\mathrm{d}}{\mathrm{d}t}\left(\tfrac12 m v^2\right) = P$ donne $v(t)=\sqrt{2Pt/m}$ et $x(t)=\tfrac{2}{3}\sqrt{2P/m}\;t^{3/2}$, très différent du MRUA. Refaire le problème du rattrapage avec ce modèle : l'équation $x_A(t)=x_B(t)$ devient une équation en $t^{3/2}$. Ajouter ensuite une résistance aérodynamique $\tfrac12\rho S C_x v^2$ et montrer l'existence d'une vitesse limite $v_\ell=\left(2P/\rho S C_x\right)^{1/3}$. Discuter dans quel régime l'hypothèse « accélération constante » est raisonnable (faibles vitesses, démarrage limité par l'adhérence : $a\le\mu g$).




> [!question]- 🔭 Aller plus loin — Doctorat : Mouvement hyperbolique : le rattrapage en relativité restreinte
> En relativité restreinte, une « accélération constante » signifie une **accélération propre** $\alpha$ constante, et la loi horaire est le mouvement hyperbolique
> $$x(t)=\frac{c^2}{\alpha}\left(\sqrt{1+\left(\frac{\alpha t}{c}\right)^2}-1\right),$$
> qui redonne $\tfrac12\alpha t^2$ pour $\alpha t\ll c$. Montrer que, avec deux accélérations propres différentes et un retard au départ, le rattrapage existe encore mais que les vitesses restent bornées par $c$. Pour la culture personnelle : cette trajectoire est une hyperbole d'équation $(x+c^2/\alpha)^2-c^2t^2=c^4/\alpha^2$ dans le diagramme d'espace-temps, et elle est à l'origine de l'horizon de Rindler et de l'effet Unruh.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex4-le-dilemme-du-feu-orange|Exercice 4 — Le dilemme du feu orange]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex7-balle-rebondissante-et-paradoxe-de-zenon|Exercice 7 — Balle rebondissante et paradoxe de Zénon]]


