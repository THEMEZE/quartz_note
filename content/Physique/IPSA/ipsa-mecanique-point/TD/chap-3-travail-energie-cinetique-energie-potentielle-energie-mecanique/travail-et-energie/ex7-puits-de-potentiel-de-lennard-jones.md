---
title: "Exercice 7 — (*) Puits de potentiel de Lennard-Jones"
tags:
  - td
  - chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/index|⬅ Retour]]

### Exercice 7. (*) Puits de potentiel de Lennard-Jones *(facultatif)*

Deux atomes de gaz rare (argon) interagissent par le potentiel de Lennard-Jones
$$E_p(r)=4\varepsilon\left[\Big(\frac\sigma r\Big)^{12}-\Big(\frac\sigma r\Big)^{6}\right],$$
où $r$ est la distance entre les centres, $\varepsilon>0$ la profondeur du puits et $\sigma$ une longueur. Pour l'argon : $\varepsilon/k_B=120$ K (soit $\varepsilon=1{,}66\times10^{-21}$ J $=10{,}3$ meV), $\sigma=0{,}34$ nm, masse atomique $m=39{,}95$ u $=6{,}63\times10^{-26}$ kg. On étudie le mouvement **relatif** (une dimension, selon la droite des centres) ; la particule fictive a pour masse la **masse réduite** $\mu_r=m/2$. On néglige tout rayonnement.

**q1.** - [(a)] Montrer que $E_p(\sigma)=0$ et étudier le comportement de $E_p$ pour $r\to0$ et $r\to\infty$. Quel terme est répulsif ? attractif ?
- [(b)] Établir l'expression de la force $F(r)$. Déterminer la distance d'équilibre $r_{\rm eq}$ et la valeur $E_p(r_{\rm eq})$. L'équilibre est-il stable ?
- [(c)] Montrer que la force attractive est maximale en $r_i=\big(\tfrac{26}7\big)^{1/6}\sigma$ et calculer sa valeur. Application numérique pour l'argon : quelle force faut-il exercer pour séparer les deux atomes ?

> [!tip]- 💡 Coup de pouce
> Poser $x=(\sigma/r)^6$ : $E_p=4\varepsilon(x^2-x)$. Équilibre : $E_p'=0$. La force est extrêmale quand $F'(r)=0$, c'est-à-dire $E_p''(r)=0$ (point d'inflexion).


**q2.** - [(d)] Établir la raideur effective $k_{\rm eff}$ des petites oscillations autour de $r_{\rm eq}$ puis la période et la fréquence de vibration du dimère d'argon (masse réduite $m/2$). Comparer au cas d'un atome oscillant dans un puits fixe.
- [(e)] On donne l'énergie mécanique $E$ du mouvement relatif. Montrer que les rebroussements vérifient $r_\pm=\sigma\Big[\tfrac12\big(1\pm\sqrt{1+E/\varepsilon}\big)\Big]^{-1/6}$. Pour quelles valeurs de $E$ le mouvement est-il lié ? Calculer $r_\pm$ pour $E=-\varepsilon/2$.
- [(f)] Pour $E=+\varepsilon$ (état de diffusion) : calculer la distance minimale d'approche. Quelle vitesse relative minimale faut-il communiquer à un dimère lié au repos en $r_{\rm eq}$ pour le dissocier ?

> [!tip]- 💡 Coup de pouce
> (d) $\omega_0=\sqrt{k_{\rm eff}/\mu_r}$. (e) À un rebroussement, $E_c=0$ donc $E_p(r)=E$, soit $4\varepsilon(x^2-x)=E$ : équation du second degré en $x$. (f) Dissociation : $E_m\ge0$ ; énergie cinétique relative $\tfrac12\mu_rv^2$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex6-chaine-qui-glisse-d-une-table|Exercice 6 — (*) Chaîne qui glisse d'une table]]

