---
title: "Exercice 7 — (*) Puits de potentiel de Lennard-Jones"
tags:
  - td
  - chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/index|⬅ Retour]] · <a href="/pdfs/td5_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td5_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 7. (*) Puits de potentiel de Lennard-Jones *(facultatif)*

*Difficulté ●●●●○ · ⏱ 60 min · Type : Exercice non guidé / Modélisation*

Deux atomes de gaz rare (argon) interagissent par le potentiel de Lennard-Jones
$$E_p(r)=4\varepsilon\left[\Big(\frac\sigma r\Big)^{12}-\Big(\frac\sigma r\Big)^{6}\right],$$
où $r$ est la distance entre les centres, $\varepsilon>0$ la profondeur du puits et $\sigma$ une longueur. Pour l'argon : $\varepsilon/k_B=120$ K (soit $\varepsilon=1{,}66\times10^{-21}$ J $=10{,}3$ meV), $\sigma=0{,}34$ nm, masse atomique $m=39{,}95$ u $=6{,}63\times10^{-26}$ kg. On étudie le mouvement **relatif** (une dimension, selon la droite des centres) ; la particule fictive a pour masse la **masse réduite** $\mu_r=m/2$. On néglige tout rayonnement.

> [!question]+ 🎣 Accroche
> **Pourquoi deux atomes forment-ils une molécule ?**
>
> *Durée de l'introduction : 4 min*
>
> *Deux atomes d'argon s'attirent à longue distance et se repoussent à courte distance. **Existe-t-il une distance d'équilibre ?** À quelle température cette « molécule » se dissocie-t-elle ? À quelle fréquence vibre-t-elle ?*
>
> **Idée clé : lire la physique dans la forme de $E_p(r)$.** Minimum $\Rightarrow$ équilibre stable ; profondeur $\Rightarrow$ énergie de liaison ; courbure $\Rightarrow$ fréquence des petites oscillations ; intersection avec $E_m$ $\Rightarrow$ rebroussements.


> [!abstract]+ 📚 Prérequis
> **Force et énergie potentielle**
>
> $F(r)=-\dfrac{\mathrm dE_p}{\mathrm dr}$ ; équilibre : $E_p'(r_{\rm eq})=0$ ; stabilité : $E_p''(r_{\rm eq})>0$.
>
> **Petites oscillations**
>
> Autour d'un minimum, $E_p\approx E_p(r_{\rm eq})+\tfrac12k_{\rm eff}(r-r_{\rm eq})^2$ avec $k_{\rm eff}=E_p''(r_{\rm eq})$ ; $T_0=2\pi\sqrt{\mu_r/k_{\rm eff}}$.
>
> **Masse réduite**
>
> Deux masses $m_1,m_2$ en interaction mutuelle : le mouvement relatif est celui d'une particule de masse $\mu_r=\dfrac{m_1m_2}{m_1+m_2}$ ; ici $\mu_r=m/2$.
>
> **Résolution d'une équation du second degré**
>
> $x^2-x-c=0\Rightarrow x=\dfrac{1\pm\sqrt{1+4c}}2$.


> [!info]+ 🎯 Objectifs
> **Exploiter un potentiel réel**
>
> Savoir tracer et analyser un potentiel, trouver l'équilibre, la profondeur, la force maximale, la raideur effective et la période des petites oscillations, déterminer les points de rebroussement pour une énergie donnée et distinguer états liés et états de diffusion.


> [!note]+ 📖 Point de cours
> **Force et équilibre**
>
> $F(r)=-E_p'(r)=\dfrac{24\varepsilon}r\Big[2\Big(\dfrac\sigma r\Big)^{12}-\Big(\dfrac\sigma r\Big)^6\Big]$ : répulsive à courte distance ($F>0$), attractive à longue distance ($F<0$).
>
> **États liés et états de diffusion**
>
> $E_m<0$ : mouvement borné entre deux rebroussements $r_-<r<r_+$ : état lié (molécule). $E_m>0$ : un seul rebroussement, la particule vient de l'infini et repart : diffusion.


> [!note]- 🧮 Outils mathématiques
> **Changement de variable $x=(\sigma/r)^6$**
>
> $E_p=4\varepsilon(x^2-x)$ ; $\dfrac{\mathrm dx}{\mathrm dr}=-\dfrac6rx$ ; extrema de $x^2-x$ en $x=\tfrac12$.
>
> **Dérivées successives de $r^{-n}$**
>
> $(r^{-n})'=-n\,r^{-n-1}$, $(r^{-n})''=n(n+1)\,r^{-n-2}$ ; d'où $E_p'=4\varepsilon\big[-12\sigma^{12}r^{-13}+6\sigma^6r^{-7}\big]$ et $E_p''=4\varepsilon\big[156\sigma^{12}r^{-14}-42\sigma^6r^{-8}\big]$.
>
> **Résolution de $x^2-x-c=0$**
>
> Avec $c=E/(4\varepsilon)$ : $x_\pm=\dfrac12\big(1\pm\sqrt{1+E/\varepsilon}\big)$.
>
> **Conversion énergie-température**
>
> $\varepsilon/k_B=120$ K ; à $300$ K, $k_BT=25{,}9$ meV $=2{,}5\,\varepsilon$.


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

