---
title: "Exercice 5 — Pendule dans un wagon accéléré"
tags:
  - td
  - chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/index|⬅ Retour]] · <a href="/pdfs/td7_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td7_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 5. Pendule dans un wagon accéléré *(facultatif)*

*Difficulté ●●●○○ · ⏱ 45 min · Type : Complément original / Dynamique en référentiel non galiléen*

Un pendule simple (masse $m$ ponctuelle, fil inextensible de longueur $\ell=1{,}00$ m, de masse négligeable) est suspendu au plafond d'un wagon. Le wagon, référentiel $\mathcal R'$, est en mouvement rectiligne par rapport au sol $\mathcal R$ (galiléen) avec l'accélération constante $\vec a=a\,\vec e_x$, $a=2{,}00\ {\rm m\cdot s^{-2}}$ ; $g=9{,}81\ {\rm m\cdot s^{-2}}$. On repère le pendule par l'angle $\theta$ que fait le fil avec la verticale descendante, compté positivement dans le sens de $\vec e_x$. À $t=0$, le wagon démarre : le pendule est au repos **dans le wagon**, le fil vertical ($\theta=0$).


> [!question]- 🪝 Accroche
> **Pourquoi un pendule penche-t-il vers l'arrière quand le train démarre ?**
>
> *Durée de l'introduction : 3 min*
>
> *Dans un train qui démarre, un fil à plomb se penche vers l'arrière : quelle force le tire ? Existe-t-elle pour un observateur sur le quai ?*
>
> **Idée clé : dans $\mathcal R'$, tout se passe comme si la pesanteur valait $\vec g-\vec a$.** Pour l'observateur du quai, aucune force supplémentaire : c'est le fil qui accélère la masse.




> [!abstract]- 🧠 À savoir avant
> **Forces d'inertie**
>
> Dans un référentiel $\mathcal R'$ en translation accélérée ($\vec a_e=\vec a$, $\vec\Omega=\vec0$) : $\vec F_{ie}=-m\vec a$ et $\vec F_{ic}=\vec0$.
>
> **Pendule simple**
>
> $\ell\ddot\theta=-g\sin\theta$ ; petites oscillations $\omega_0=\sqrt{g/\ell}$.
>
> **Énergie potentielle**
>
> Une force constante $\vec F$ dérive de $E_p=-\vec F\cdot\vec r$.




> [!info]- 🎯 Ce que tu sauras faire
> **Écrire le PFD dans $\mathcal R'$ avec la force d'inertie d'entraînement**
>
> Savoir que tout se passe comme dans un champ de pesanteur effectif $\vec g_{\rm eff}=\vec g-\vec a$.
>
> **Équilibre relatif, stabilité, oscillations**
>
> Déterminer l'angle d'équilibre, la tension, la période de petites oscillations, l'amplitude des oscillations après le démarrage.




> [!tip]- 📖 Rappel de cours
> **Principe fondamental dans $\mathcal R'$**
>
> $m\vec a_r=m\vec g+\vec T-m\vec a=m\vec g_{\rm eff}+\vec T$ avec $\vec g_{\rm eff}=\vec g-\vec a$, $g_{\rm eff}=\sqrt{g^2+a^2}$.
>
> **Énergie potentielle effective**
>
> $E_{p,\rm eff}(\theta)=-m\ell\,\vec g_{\rm eff}\cdot\vec u_\ell=-mg\ell\cos\theta+ma\ell\sin\theta$ (pour $\theta$ compté vers $+\vec e_x$) ; on peut écrire $E_{p,\rm eff}=-mg_{\rm eff}\ell\cos(\theta+\alpha)$ avec $\tan\alpha=a/g$.




> [!note]- 🧮 Outils mathématiques
> **Composition de sinus et cosinus**
>
> $A\cos\theta+B\sin\theta=\sqrt{A^2+B^2}\cos(\theta-\varphi)$, $\tan\varphi=B/A$.
>
> **Petites oscillations**
>
> $\ddot\varphi+\omega_0^2\varphi=0$ pour $\varphi=\theta+\alpha$.
>
> **Conservation de l'énergie**
>
> $\tfrac12m\ell^2\dot\varphi^2-mg_{\rm eff}\ell\cos\varphi={\rm cte}$.



**q1.** - [(a)] Faire le bilan des forces sur la masse dans $\mathcal R'$ et écrire le principe fondamental.
- [(b)] Déterminer l'angle d'équilibre $\theta_{\rm eq}$ et la tension à l'équilibre. Applications numériques.
- [(c)] Retrouver ces résultats dans $\mathcal R$ (galiléen), sans force d'inertie.


> [!tip]- 💡 Coup de pouce
> (a) Poids, tension et $\vec F_{ie}=-m\vec a$. (b) À l'équilibre, $\vec a_r=\vec0$ : $m\vec g_{\rm eff}+\vec T=\vec0$. (c) La masse a l'accélération $\vec a$ : appliquer $m\vec a=m\vec g+\vec T$.



**q2.** - [(d)] Établir l'équation du mouvement de $\theta(t)$ dans $\mathcal R'$ et montrer qu'elle se met sous la forme $\ddot\varphi=-\dfrac{g_{\rm eff}}{\ell}\sin\varphi$ avec $\varphi=\theta+\alpha$.
- [(e)] Calculer la période des petites oscillations. Applications numériques.
- [(f)] À $t=0$ le fil est vertical et le pendule immobile dans le wagon. Quelle est l'amplitude du mouvement ultérieur, l'angle maximal atteint vers l'arrière et la tension maximale ?


> [!tip]- 💡 Coup de pouce
> (d) Projeter sur $\vec e_\theta$ : $m\ell\ddot\theta=-mg\sin\theta-ma\cos\theta$. Écrire $g\sin\theta+a\cos\theta=g_{\rm eff}\sin(\theta+\alpha)$. (f) Conservation de $\tfrac12\ell\dot\varphi^2-g_{\rm eff}\cos\varphi$ avec $\varphi(0)=\alpha$, $\dot\varphi(0)=0$. Pour $T$ : projeter sur le fil.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex6-perle-sur-un-cerceau-tournant|Exercice 6 — Perle sur un cerceau tournant]]


