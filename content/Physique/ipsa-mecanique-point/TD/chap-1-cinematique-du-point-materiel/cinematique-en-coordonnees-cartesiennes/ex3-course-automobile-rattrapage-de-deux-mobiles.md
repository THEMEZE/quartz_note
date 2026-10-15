---
title: "Exercice 3 — Course automobile : rattrapage de deux mobiles"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td1_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td1_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td1_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td1_PhV111_fiche.pdf)

### Exercice 3. Course automobile : rattrapage de deux mobiles *(facultatif)*

Deux pilotes amateurs prennent le départ d'une course sur une longue ligne droite, depuis la même
ligne de départ. Le pilote $A$ démarre à $t=0$ s avec une accélération $a_A = 4~\mathrm{m\,s^{-2}}$.
Le pilote $B$, dont la voiture est plus puissante, démarre avec une accélération $a_B = 5~\mathrm{m\,s^{-2}}$.
$A$ a cependant plus de réflexes que $B$ et démarre une seconde avant lui.
On suppose que les deux voitures partent du repos et que leurs accélérations restent constantes.

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


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex4-le-dilemme-du-feu-orange|Exercice 4 — Le dilemme du feu orange]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex7-balle-rebondissante-et-paradoxe-de-zenon|Exercice 7 — Balle rebondissante et paradoxe de Zénon]]

