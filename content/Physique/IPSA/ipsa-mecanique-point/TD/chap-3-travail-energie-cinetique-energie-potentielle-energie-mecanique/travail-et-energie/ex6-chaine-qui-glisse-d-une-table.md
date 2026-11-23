---
title: "Exercice 6 — (*) Chaîne qui glisse d'une table"
tags:
  - td
  - chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/index|⬅ Retour]] · <a href="/pdfs/td5_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td5_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 6. (*) Chaîne qui glisse d'une table *(facultatif)*

*Difficulté ●●●●○ · ⏱ 55 min · Type : Exercice non guidé / Système étendu*

Une chaîne homogène, flexible et inextensible, de longueur $L=1{,}00$ m et de masse $M$, repose sur une table horizontale **lisse** ; une longueur $x_0=0{,}10$ m pend initialement le long du bord de la table, l'arête étant arrondie et sans frottement. La chaîne est lâchée sans vitesse à $t=0$. On note $x(t)$ la longueur pendante, $\lambda_\ell=M/L$ la masse linéique et $g=9{,}81~\mathrm{m\,s^{-2}}$. Toute la chaîne se déplace avec la même vitesse (en norme) $\dot x$.

> [!question]+ 🎣 Accroche
> **Une chaîne qui glisse : de plus en plus vite**
>
> *Durée de l'introduction : 3 min*
>
> *Une chaîne posée sur une table lisse est tenue avec un petit bout qui pend. On la lâche. **L'accélération est-elle constante ?** Combien de temps pour tomber de la table si $10~\%$ pend au départ ?*
>
> **Idée clé : la force motrice (poids de la partie pendante) croît avec $x$.** $\ddot x=\dfrac gLx$ : accélération proportionnelle à $x$, solution en $\cosh$. L'énergie donne la vitesse finale directement.


> [!abstract]+ 📚 Prérequis
> **Énergie potentielle d'un système étendu**
>
> $E_p=\sum m_ig\,z_i$ : on repère la hauteur du centre de masse de chaque tronçon. Origine des altitudes au niveau de la table.
>
> **Intégrale première de l'énergie**
>
> Pour un seul degré de liberté $x$, $E_m=\tfrac12M\dot x^2+E_p(x)=\text{cte}$ donne $\dot x(x)$ sans résoudre l'équation du mouvement.
>
> **Fonctions hyperboliques**
>
> $\ddot x=\kappa^2x\Rightarrow x(t)=x_0\cosh\kappa t$ si $\dot x(0)=0$ ; $\cosh^{-1}$ ou $\operatorname{arcosh}$ pour inverser.


> [!info]+ 🎯 Objectifs
> **Appliquer l'énergie à un système étendu**
>
> Savoir calculer l'énergie potentielle d'une chaîne partiellement suspendue, établir $\dot x(x)$, retrouver l'équation du mouvement par dérivation, la résoudre (exponentielle croissante) et reconnaître un équilibre instable sur le diagramme d'énergie.


> [!note]+ 📖 Point de cours
> **Énergie potentielle d'une chaîne suspendue**
>
> La partie sur la table est à l'altitude $0$ : $E_p=0$. La partie pendante, de masse $\lambda_\ell x$ et de centre de masse à l'altitude $-x/2$, a pour énergie $E_p=-\lambda_\ell x\,g\,\dfrac x2=-\dfrac{Mg}{2L}x^2$.
>
> **Équation du mouvement par la dérivée de l'énergie**
>
> $\dfrac{\mathrm dE_m}{\mathrm dt}=0\Rightarrow M\dot x\ddot x+\dfrac{\mathrm dE_p}{\mathrm dx}\dot x=0$, soit $M\ddot x=-\dfrac{\mathrm dE_p}{\mathrm dx}=\dfrac{Mg}Lx$.


> [!note]- 🧮 Outils mathématiques
> **Équation $\ddot x=\kappa^2x$**
>
> Solution générale $A\,\mathrm e^{\kappa t}+B\,\mathrm e^{-\kappa t}$ ; avec $x(0)=x_0$, $\dot x(0)=0$ : $x=x_0\cosh\kappa t$, $\kappa=\sqrt{g/L}$.
>
> **Inversion de $\cosh$**
>
> $\cosh u=y\iff u=\ln\big(y+\sqrt{y^2-1}\big)=\operatorname{arcosh}y$ ; $\operatorname{arcosh}10=\ln(10+\sqrt{99})=2{,}993$.
>
> **Racine carrée**
>
> $\sqrt{9{,}81\times0{,}99}=\sqrt{9{,}712}=3{,}116$.


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

