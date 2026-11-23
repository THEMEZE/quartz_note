---
title: "Exercice 4 — Extension -- Choc élastique oblique : angle maximal de déviation et transfert d'énergie"
tags:
  - projet
  - application-a-la-propulsion-spatiale
---

[[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/index|⬅ Retour]] · <a href="/pdfs/projet1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/projet1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/Phv111_MP_Falcon9_Launch.xlsx" target="_blank" rel="noopener">📊 Fichier Excel – Falcon 9</a>

### Exercice 4. Extension -- Choc élastique oblique : angle maximal de déviation et transfert d'énergie *(facultatif)*

*Difficulté ●●●●● · ⏱ 45 min · Type : Approfondissement / Démonstration*

Un mobile $1$ de masse $m_1$, de vitesse $\vec v_0$, heurte de façon **élastique** un mobile $2$ de masse $m_2$ initialement au repos, sur une table à coussin d'air (système isolé). Le choc n'est pas forcément frontal : après le choc, le mobile 1 a la vitesse $\vec v_1'$ faisant l'angle $\theta_1$ avec $\vec v_0$, et le mobile 2 la vitesse $\vec v_2'$ faisant l'angle $\theta_2$ avec $\vec v_0$ (de l'autre côté). On pourra prendre pour application numérique $m_1=1{,}50$ kg et $m_2=1{,}00$ kg (masses de l'annexe).

> [!question]+ 🎣 Accroche
> **Pourquoi les boules de billard partent-elles à angle droit ?**
>
> *Durée de l'introduction : 3 min*
>
> *Au billard, une boule heurte de côté une boule immobile identique : les deux partent presque exactement à $90^\circ$ l'une de l'autre. Coïncidence ? Et si la boule immobile est plus lourde ou plus légère ?*
>
> **Idée clé : conservation de $\vec p$ et de $E_c$ dessinent un triangle de vecteurs.** Pour des masses égales, $\vec v_0=\vec v_1'+\vec v_2'$ et $v_0^2=v_1'^2+v_2'^2$ : c'est le théorème de Pythagore, donc $\vec v_1'\perp\vec v_2'$.


> [!abstract]+ 📚 Prérequis
> **Conservation de $\vec p$ et de $E_c$**
>
> Choc élastique d'un système isolé : $m_1\vec v_0=m_1\vec v_1'+m_2\vec v_2'$ et $\tfrac12m_1v_0^2=\tfrac12m_1v_1'^2+\tfrac12m_2v_2'^2$.
>
> **Produit scalaire**
>
> $\vec a\cdot\vec b=ab\cos\theta$ ; $\|\vec a+\vec b\|^2=a^2+b^2+2\,\vec a\cdot\vec b$ ; $\vec a\perp\vec b\iff\vec a\cdot\vec b=0$.
>
> **Centre de masse**
>
> $\vec v_G=\dfrac{m_1\vec v_1+m_2\vec v_2}{m_1+m_2}$ est constante pour un système isolé ; dans le référentiel $\mathcal R^*$ du centre de masse, $\vec p^*_{\rm tot}=\vec0$.


> [!info]+ 🎯 Objectifs
> **Résoudre un choc 2D élastique par la géométrie des vecteurs**
>
> Savoir déduire de la conservation de $\vec p$ et $E_c$ des résultats généraux : règle des $90^\circ$ pour des masses égales, angle de déviation maximal $\theta_{\max}$ pour $m_1>m_2$, transfert d'énergie maximal, et utiliser le référentiel du centre de masse.


> [!note]+ 📖 Point de cours
> **Cercle de Thalès des vitesses**
>
> Dans $\mathcal R^*$, un choc élastique ne change que la direction des vitesses. Dans $\mathcal R$ : $\vec v_1'=\vec v_G+\vec u_1'$ avec $\|\vec u_1'\|=\dfrac{m_2}{m_1+m_2}v_0$ fixée, $\|\vec v_G\|=\dfrac{m_1}{m_1+m_2}v_0$ : l'extrémité de $\vec v_1'$ décrit un cercle.


> [!note]- 🧮 Outils mathématiques
> **Théorème de Pythagore et réciproque**
>
> $\|\vec a+\vec b\|^2=\|\vec a\|^2+\|\vec b\|^2\iff\vec a\perp\vec b$.
>
> **Cercle et tangente depuis un point extérieur**
>
> Un cercle de centre $C$ et de rayon $r$, vu depuis $O$ avec $OC=d>r$, est sous-tendu par l'angle $\alpha$ tel que $\sin\alpha=r/d$.
>
> **Trigonométrie : loi des sinus et des cosinus**
>
> Dans un triangle de côtés $a,b,c$ : $c^2=a^2+b^2-2ab\cos\gamma$.


**q1.** - [(a)] Écrire les lois de conservation. Dans le cas $m_1=m_2$, montrer que $\vec v_1'\perp\vec v_2'$ (si le choc est oblique).
- [(b)] Dans le cas général, montrer que $\vec v_1'=\vec v_G+\vec u_1'$ avec $\|\vec u_1'\|=\dfrac{m_2}{m_1+m_2}v_0$ et $\|\vec v_G\|=\dfrac{m_1}{m_1+m_2}v_0$.

> [!tip]- 💡 Coup de pouce
> (a) Élevez au carré la conservation de $\vec p$ et comparez avec la conservation de $E_c$. (b) Dans $\mathcal R^*$ la norme des vitesses se conserve pour un choc élastique : $\|\vec u_1'\|=\|\vec u_1\|$.


**q2.** - [(c)] Pour $m_1>m_2$, montrer que l'angle de déviation $\theta_1$ du mobile 1 est limité : $\sin\theta_{1,\max}=\dfrac{m_2}{m_1}$. Application numérique pour $m_1=1{,}50$ kg, $m_2=1{,}00$ kg. Que se passe-t-il pour $m_1<m_2$ ?
- [(d)] Choc frontal : calculer la fraction de l'énergie cinétique initiale transférée au mobile 2. Pour quelle valeur de $m_2/m_1$ est-elle maximale ? Application numérique.

> [!tip]- 💡 Coup de pouce
> (c) Cercle de rayon $r=m_2v_0/(m_1+m_2)$ centré à la distance $d=m_1v_0/(m_1+m_2)$ de l'origine ; l'origine est à l'extérieur si $d>r$. Trouvez l'angle maximal sous lequel on voit le cercle. (d) Transférée à 2 : $\dfrac{\tfrac12m_2v_2'^2}{\tfrac12m_1v_0^2}$ avec $v_2'=\dfrac{2m_1}{m_1+m_2}v_0$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex1-seance-1-theorie-du-choc-et-quantite-de-mouvement|Exercice 1 — Séance 1 -- Théorie du choc et quantité de mouvement]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex3-seance-1-conservation-de-la-quantite-de-mouvement-et-bilan-d-energie-cinetique|Exercice 3 — Séance 1 -- Conservation de la quantité de mouvement et bilan d'énergie cinétique]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex5-seance-2-equation-de-tsiolkovski-propulsion-par-ejection-de-masse|Exercice 5 — Séance 2 -- Équation de Tsiolkovski : propulsion par éjection de masse]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex6-seance-2-application-un-lanceur-a-deux-etages-inspire-du-falcon-9|Exercice 6 — Séance 2 -- Application : un lanceur à deux étages inspiré du Falcon 9]]

