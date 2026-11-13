---
title: "Exercice 6 — (*) Chaîne qui glisse d'une table"
tags:
  - td
  - chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/index|⬅ Retour]]

### Exercice 6. (*) Chaîne qui glisse d'une table *(facultatif)*

Une chaîne homogène, flexible et inextensible, de longueur $L=1{,}00$ m et de masse $M$, repose sur une table horizontale **lisse** ; une longueur $x_0=0{,}10$ m pend initialement le long du bord de la table, l'arête étant arrondie et sans frottement. La chaîne est lâchée sans vitesse à $t=0$. On note $x(t)$ la longueur pendante, $\lambda_\ell=M/L$ la masse linéique et $g=9{,}81~\mathrm{m\,s^{-2}}$. Toute la chaîne se déplace avec la même vitesse (en norme) $\dot x$.

**q1.** - [(a)] Faire le bilan des forces sur l'ensemble de la chaîne. Lesquelles travaillent ? Que vaut le travail de la réaction de la table ?
- [(b)] Calculer l'énergie potentielle de pesanteur de la chaîne en fonction de $x$ (altitude $0$ sur la table). Tracer $E_p(x)$ et discuter l'équilibre en $x=0$.
- [(c)] Par conservation de $E_m$, exprimer $\dot x^2$ en fonction de $x$, $x_0$, $g$ et $L$. Retrouver l'équation du mouvement.

> [!tip]- 💡 Coup de pouce
> Seule la partie pendante a une énergie potentielle non nulle ; son centre de masse est à $x/2$ sous la table. Dériver $E_m=\text{cte}$ par rapport au temps pour obtenir $\ddot x$.


**q2.** - [(d)] Résoudre l'équation du mouvement avec les conditions initiales. Calculer l'instant $t_f$ où la chaîne quitte entièrement la table ($x=L$) et sa vitesse $v_f$ à cet instant. Application numérique ($L=1$ m, $x_0=0{,}10$ m). Que devient $t_f$ quand $x_0\to0$ ?
- [(e)] Avec un frottement cinétique $\mu$ sur la table (le frottement ne s'exerce que sur la partie posée), établir l'équation du mouvement, la longueur minimale $x_0$ pour que la chaîne démarre (adhérence $\mu_s=\mu$) et la solution pour $x_0=0{,}30$ m, $\mu=0{,}2$. Calculer la vitesse de sortie.

> [!tip]- 💡 Coup de pouce
> (d) $\kappa=\sqrt{g/L}$ ; $x=A\cosh\kappa t+B\sinh\kappa t$ ; $\dot x(0)=0\Rightarrow B=0$. (e) Frottement $\mu\lambda_\ell(L-x)g$ opposé au mouvement. Chercher une solution constante $x_e$ puis poser $y=x-x_e$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex2-theoreme-de-l-energie-cinetique|Exercice 2 — Théorème de l'énergie cinétique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex7-puits-de-potentiel-de-lennard-jones|Exercice 7 — (*) Puits de potentiel de Lennard-Jones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]]

