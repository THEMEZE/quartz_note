---
title: "Exercice 3 — Célérité d’une onde sur une corde homogène"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a>

### Exercice 3. Célérité d’une onde sur une corde homogène

*⭐ Indispensable · Difficulté ●○○○○ · ⏱ 5 min · Type : Application directe du cours*

Deux cordes ont été nouées ensemble au point $O$ et leurs autres extrémités
ont été attachées à deux supports rigides. La première corde est soumise à
une tension de $400$ N. Les longueurs et masses linéiques des deux cordes
sont : $L_1 = 3$ m, $L_2 = 2$ m, $\mu_1 = 1.4\times10^{-4}$ kg·m$^{-1}$,
$\mu_2 = 2.8\times10^{-4}$ kg·m$^{-1}$.

<p style="text-align:center"><a href="/figures/td1_ex2_cordes_nouees.svg" target="_blank" rel="noopener"><img src="/figures/td1_ex2_cordes_nouees.svg" alt="Cordes nouées au point O." loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>

> [!question]+ 🎣 Accroche
> **Course entre deux impulsions**
>
> *Durée de l'introduction : 3 min, avant de lire l'énoncé*
>
> *Deux cordes sont nouées l'une à l'autre : l'une est deux fois plus lourde au mètre, mais plus courte. On envoie en même temps une impulsion depuis chaque extrémité. **Laquelle arrive la première au nœud ?** Le plus court trajet l'emporte-t-il forcément ?*
>
> **Idée clé : la vitesse d'une impulsion est fixée par le milieu, pas par l'impulsion.** Sur une corde de tension $F$ et de masse linéique $\mu$, $c=\sqrt{F/\mu}$ ; la durée d'un trajet de longueur $L$ est donc $t=L/c=L\sqrt{\mu/F}$. Comme le nœud est de masse nulle, la **tension est la même** des deux côtés ; seule la masse linéique change, donc la célérité.


> [!note]- 🧮 Outils mathématiques
> **Racine carrée et comparaison de rapports**
>
> Comparer $t_1$ et $t_2$ sans calculatrice : $\dfrac{t_1}{t_2}=\dfrac{L_1}{L_2}\sqrt{\dfrac{\mu_1}{\mu_2}}=\dfrac32\times\dfrac1{\sqrt2}\approx1{,}06>1$. Un rapport suffit, inutile de connaître $F$.
>
> **Proportionnalités**
>
> $c\propto\mu^{-1/2}$ : doubler $\mu$ divise $c$ par $\sqrt2$ ($\approx1{,}41$, d'où $c_1/c_2=1690/1195$). Savoir lire une loi en puissance.
>
> **Notation scientifique et ordres de grandeur**
>
> $1{,}4\times10^{-4}$ kg/m, $1{,}7\times10^3$ m/s, $1{,}8\times10^{-3}$ s. Une corde de piano typique a des vitesses de l'ordre de quelques centaines de m/s : les durées sont de l'ordre de la milliseconde.
>
> **Relation distance-vitesse-durée**
>
> $t=L/c$ : application directe de la cinématique à un signal qui avance à vitesse constante.


**q1.** Simultanément, de chaque extrémité est envoyée une impulsion vers $O$.
Quelle est celle qui atteint $O$ la première ?

> [!tip]- 💡 Coup de pouce
> **Calcul des vitesses et durées**
>
> Calculez la vitesse de propagation dans chaque corde avec $c_i = \sqrt{F/\mu_i}$
> (la tension $F$ est identique de chaque côté), puis comparez les temps de parcours $t_i = L_i / c_i$.


> [!question]- 🔭 Aller plus loin — Licence : Que se passe-t-il au nœud O ?
> Lorsque l'impulsion atteint la jonction $O$, une partie de l'onde est transmise dans l'autre corde et une partie est réfléchie. C'est l'objet de l'étude des coefficients de réflexion et de transmission (TD 3).


> [!success]- ✅ Correction
> **Résultat synthétique**
>
> $c_1 \approx 1690$ m/s, $c_2 \approx 1195$ m/s ; $t_1 = L_1/c_1 \approx 1.78$ ms, $t_2 = L_2/c_2 \approx 1.67$ ms.
> C'est l'impulsion provenant de la **corde 2** qui atteint le point $O$ en premier.


> [!example]- 📝 Solution détaillée
> **Calculs détaillés pas à pas**
>
> - \underline*\bf Corde 1 :*
>
>
> - **Célérité :** $c_1 = \sqrt{\dfrac{F}{\mu_1}} = \sqrt{\dfrac{400}{1.4\times 10^{-4}}} \approx 1690\ \text{m/s}$.
> - **Durée du trajet :** $t_1 = \dfrac{L_1}{c_1} = \dfrac{3}{1690} \approx 1.78\times 10^{-3}\ \text{s} = 1.78\ \text{ms}$.
> - \underline*\bf Corde 2 :*
>
>
> - **Célérité :** $c_2 = \sqrt{\dfrac{F}{\mu_2}} = \sqrt{\dfrac{400}{2.8\times 10^{-4}}} \approx 1195\ \text{m/s}$.
> - **Durée du trajet :** $t_2 = \dfrac{L_2}{c_2} = \dfrac{2}{1195} \approx 1.67\times 10^{-3}\ \text{s} = 1.67\ \text{ms}$.
>
>
>
> Puisque $t_2 < t_1$, l'impulsion sur la corde 2 met moins de temps à parcourir la distance $L_2$ et atteint le nœud $O$ en premier.


> [!note]- 🔗 Liens avec d'autres disciplines
> **Optique**
>
> Une corde lourde joue le rôle d'un milieu où l'onde va plus lentement, comme la lumière dans le verre (indice $n=c_0/c$). Au passage d'un milieu à l'autre, une partie de l'onde est réfléchie et une partie transmise : même phénomène qu'à la surface d'une vitre.
>
> **Électronique et télécommunications**
>
> La réflectométrie envoie une impulsion dans un câble et mesure le temps d'écho : la distance à un défaut est $d=c\,\Delta t/2$. Même principe qu'au nœud entre deux cordes.
>
> **Sismologie**
>
> Les ondes sismiques sont partiellement réfléchies et transmises aux interfaces entre couches de nature différente : la mesure des retards permet de reconstituer la structure du sous-sol (prospection pétrolière).


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex2-corde-de-nylon|Exercice 2 — Corde de nylon]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex3-partie-c-masse-lineique-de-la-corde-par-deux-methodes|Exercice 3 — Partie C — Masse linéique de la corde par deux méthodes]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex5-synthese-scientifique-du-tp|Exercice 5 — Synthèse scientifique du TP]] · [[physique/IPSA/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex11-une-perle-sur-la-corde-reflexion-transmission-et-filtre-passe-bas-mecanique|Exercice 11 — Une perle sur la corde : réflexion, transmission et filtre passe-bas mécanique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex12-adaptation-d-impedance-lame-quart-d-onde-entre-deux-cordes|Exercice 12 — Adaptation d'impédance : lame quart d'onde entre deux cordes]]

