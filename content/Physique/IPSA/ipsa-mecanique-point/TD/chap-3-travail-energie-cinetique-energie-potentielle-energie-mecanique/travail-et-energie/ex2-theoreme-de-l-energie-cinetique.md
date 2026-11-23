---
title: "Exercice 2 — Théorème de l'énergie cinétique"
tags:
  - td
  - chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/index|⬅ Retour]] · <a href="/pdfs/td5_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td5_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 2. Théorème de l'énergie cinétique

*⭐ Indispensable · Difficulté ●●○○○ · ⏱ 45 min · Type : Application / Cours actif*

Le théorème de l'énergie cinétique (TEC) $\Delta E_c=\sum W$ est l'outil central du TD. On l'utilise d'abord pour des distances de freinage, puis pour confronter le calcul à une expérience (balle lancée vers le haut), enfin pour justifier la conservation de l'énergie mécanique (kangourou). On prendra $g=9{,}81~\mathrm{m\,s^{-2}}$.

> [!question]+ 🎣 Accroche
> **Freiner de $50$ à $100$ km/h : combien de mètres de plus ?**
>
> *Durée de l'introduction : 3 min*
>
> *Une voiture roule à $50$ km/h et s'arrête en $12$ m. **Quelle distance lui faut-il à $100$ km/h** avec le même freinage : $24$ m, $36$ m ou $48$ m ?*
>
> **Idée clé : le travail de la force de freinage doit annuler toute l'énergie cinétique.** $-F\,d=-\tfrac12mv^2$, donc $d=\dfrac{mv^2}{2F}$ : $d\propto v^2$, soit $4\times12=48$ m.


> [!abstract]+ 📚 Prérequis
> **Théorème de l'énergie cinétique**
>
> $E_c(B)-E_c(A)=\sum W_{A\to B}(\vec F)$ avec $E_c=\tfrac12mv^2$ ; valable pour toutes les forces, dans un référentiel galiléen.
>
> **Forces conservatives**
>
> $\delta W=-\mathrm dE_p$ ; poids : $E_p=mgz$ ($Oz$ vertical ascendant), à une constante près.
>
> **Conversion km/h $\to$ m/s**
>
> Diviser par $3{,}6$.


> [!info]+ 🎯 Objectifs
> **Appliquer le TEC et le justifier**
>
> Savoir identifier les forces qui travaillent, calculer leurs travaux, en déduire une distance, une vitesse ou le travail d'une force inconnue (frottement) ; savoir démontrer qu'une force est conservative et que $E_m$ se conserve.


> [!note]+ 📖 Point de cours
> **Théorème de l'énergie cinétique**
>
> $\Delta E_c=\sum W$. Pour une force constante colinéaire au mouvement : $-F\,d=0-\tfrac12mv^2$, donc $d=\dfrac{mv^2}{2F}$.
>
> **Du TEC à la conservation de $E_m$**
>
> Si toutes les forces qui travaillent sont conservatives, $\sum W=-\Delta E_p$ ; le TEC donne $\Delta E_c+\Delta E_p=0$, soit $\Delta E_m=0$.


> [!note]- 🧮 Outils mathématiques
> **Résolution d'une équation du premier degré**
>
> Isoler $d$ dans $Fd=\tfrac12mv^2$ ; isoler $v_0$ dans $\tfrac12mv_0^2=mgh$.
>
> **Racines carrées**
>
> $v=\sqrt{2gh}$ ; estimer $\sqrt{2\times9{,}81\times7}=\sqrt{137{,}3}\approx11{,}7$.


**q1.** - [1/] En utilisant le théorème de l'énergie cinétique, calculer la distance sur laquelle doit agir une force de $800$ N pour arrêter :
    

- [(a)] un tir de penalty arrivant à $165~\mathrm{km/h}$, la balle ayant une masse de $450$ g ;
- [(b)] un enfant sur une luge de $36$ kg glissant à $38~\mathrm{km/h}$ ;
- [(c)] un camion de $12$ t roulant à $110~\mathrm{km/h}$ ;
- [(d)] une Ferrari de $1400$ kg roulant à $280~\mathrm{km/h}$.

> [!tip]- 💡 Coup de pouce
> Le travail de la force d'arrêt (opposée au déplacement) vaut $-F\,d$. Le mobile s'arrête : $E_c$ final $=0$.


**q2.** - [2/] Une balle de $200$ g lancée verticalement vers le haut avec une vitesse initiale de $20~\mathrm{m/s}$ atteint la hauteur maximale de $18$ m. Déterminer :
    

- [(a)] sa variation d'énergie cinétique ;
- [(b)] le travail effectué par le poids ;
- [(c)] les valeurs calculées sont-elles égales ? Justifier et en déduire le travail des frottements.

> [!tip]- 💡 Coup de pouce
> Au sommet la vitesse est nulle. Le travail du poids ne dépend que de la différence d'altitude. S'il y a un écart, quelle force n'a pas été prise en compte ?


**q3.** - [3/] Un kangourou peut sauter à une hauteur de $7$ m.
    

- [(a)] Montrer que le poids est une force conservative et en déduire l'énergie potentielle associée.
- [(b)] Dans quel cas peut-on supposer que l'énergie mécanique du kangourou est conservée ? Le démontrer à partir du théorème de l'énergie cinétique.
- [(c)] Déterminer, dans ce cas, la vitesse du kangourou au départ du saut.

> [!tip]- 💡 Coup de pouce
> Conservative : le travail élémentaire s'écrit comme $-\mathrm d(\ldots)$. Pour (b), écrire le TEC et remplacer $W_P$ par $-\Delta E_p$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex6-chaine-qui-glisse-d-une-table|Exercice 6 — (*) Chaîne qui glisse d'une table]]

