---
title: "Exercice 3 — Travail d'une force de rappel"
tags:
  - td
  - chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/index|⬅ Retour]] · <a href="/pdfs/td5_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td5_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 3. Travail d'une force de rappel

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 45 min · Type : Application / Cours actif*

Un cube $M$ de masse $m$, assimilé à un point matériel, est relié à un ressort de raideur $k=32~\mathrm{N\,m^{-1}}$ et glisse sur un plan horizontal. L'axe $(Ox)$ a pour origine $O$ la position d'équilibre. On écarte $M$ jusqu'à $x=a$ (point $A$) puis on le lâche avec la vitesse initiale $v_A$. Le poly ne donne pas $m$ : on prendra $m=6$ kg comme dans la correction officielle. Frottements négligés sauf aux questions (g) et suivantes.


> [!question]- 🪝 Accroche
> **L'énergie d'un ressort : de quoi dépend-elle ?**
>
> *Durée de l'introduction : 3 min*
>
> *Un ressort comprimé de $5$ cm lance un cube. Si on le comprime de $10$ cm, **quelle sera la vitesse** : deux fois plus, quatre fois plus ? Que devient l'énergie quand on double l'étirement ?*
>
> **Idée clé : l'énergie élastique est quadratique : $E_p=\tfrac12kx^2$.** Doubler la compression multiplie l'énergie par $4$ et la vitesse par $2$.




> [!abstract]- 🧠 À savoir avant
> **Force de rappel d'un ressort**
>
> $\vec F=-k\,x\,\vec u_x$ avec $x$ l'allongement algébrique (origine à la longueur à vide) ; conservative, $E_p=\tfrac12kx^2$.
>
> **Intégrale d'une force dépendant de la position**
>
> $W_{A\to B}=\displaystyle\int_{x_A}^{x_B}F(x)\,\mathrm dx$.




> [!info]- 🎯 Ce que tu sauras faire
> **Travail et énergie d'un ressort**
>
> Savoir intégrer le travail de la force de rappel, en déduire $E_p$, écrire $E_m$ et l'utiliser pour trouver une vitesse et une amplitude ; savoir prendre en compte un frottement constant.




> [!tip]- 📖 Rappel de cours
> **Énergie potentielle élastique**
>
> $\delta W=-kx\,\mathrm dx=-\mathrm d\big(\tfrac12kx^2\big)$, donc $E_p=\tfrac12kx^2$ (avec $E_p(0)=0$). $E_m=\tfrac12mv^2+\tfrac12kx^2$.
>
> **Oscillateur harmonique**
>
> $m\ddot x=-kx$, $\omega_0=\sqrt{k/m}$ ; l'énergie $E_m=\tfrac12kx_{\max}^2$ fixe l'amplitude ; $v_{\max}=\omega_0x_{\max}$ en $O$.
>
> **Frottement de glissement constant**
>
> Force $\vec f$ opposée à la vitesse, norme $f=\mu mg$ (plan horizontal) : $W_f=-f\,\ell$ avec $\ell$ la **distance parcourue** ; $\Delta E_m=W_f$.




> [!note]- 🧮 Outils mathématiques
> **Différentielle exacte**
>
> $\mathrm d\big(\tfrac12x^2\big)=x\,\mathrm dx$ ; une expression $\delta W=-kx\,\mathrm dx$ est une différentielle exacte.
>
> **Racine carrée**
>
> $\sqrt{2{,}8\times10^{-3}}=5{,}29\times10^{-2}$ ; vérifier toujours en élevant au carré.



**q1.** - [(a)] Quel est le travail de la force de rappel lorsque $M$ revient de $A$ à $O$ ?
- [(b)] Quelle est alors la vitesse $v_O$ de $M$ à son arrivée en $O$ ?
- [(c)] Montrer que la force de rappel est conservative. En déduire l'énergie potentielle associée et la représenter en fonction de $x$.
- [(d)] Donner l'expression de l'énergie mécanique. Est-elle conservée ? En quelle position $E_c$ est-elle maximale ? minimale ?


> [!tip]- 💡 Coup de pouce
> Force $\vec F=-kx\,\vec u_x$ : $\delta W=-kx\,\mathrm dx$. Reconnaître une différentielle exacte pour (c). Le TEC entre $A$ et $O$ donne la vitesse en (b).



**q2.** - [(e)] Exprimer l'énergie mécanique en $A$ et en $O$. Calculer sa valeur pour $v_A=4~\mathrm{cm/s}$, $a=5~\mathrm{cm}$ et $m=6$ kg. Compléter le graphique de (c) avec $E_m$.
- [(f)] Déterminer l'allongement maximal $x_{\max}$ du ressort et calculer sa valeur.
- [(g)] On suppose maintenant que le glissement de $M$ sur le plan se fait avec un frottement cinétique $\mu$, de norme $f=\mu mg$. Quelle est la vitesse de $M$ en $O$ ? Pour $\mu=0{,}1$, que se passe-t-il ? Quelle est la valeur maximale de $\mu$ pour que le cube atteigne $O$ ?


> [!tip]- 💡 Coup de pouce
> (e) $E_m(A)=\tfrac12mv_A^2+\tfrac12ka^2$, tout en SI. (f) $E_c=0$ en $x_{\max}$. (g) Ajouter le travail du frottement $-\mu mg\,a$ au TEC ; attention au signe sous la racine.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]]


