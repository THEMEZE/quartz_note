---
title: "Exercice 3 — Séance 1 -- Conservation de la quantité de mouvement et bilan d'énergie cinétique"
tags:
  - projet
  - application-a-la-propulsion-spatiale
---

[[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/index|⬅ Retour]] · <a href="/pdfs/projet1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/projet1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/Phv111_MP_Falcon9_Launch.xlsx" target="_blank" rel="noopener">📊 Fichier Excel – Falcon 9</a>

### Exercice 3. Séance 1 -- Conservation de la quantité de mouvement et bilan d'énergie cinétique

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 30 min · Type : Travail expérimental / Synthèse*

On reprend la chronophotographie de l'annexe ($m_A=1{,}50$ kg, $m_B=1{,}00$ kg, $\tau=0{,}1$ s) et les vitesses obtenues dans la partie précédente : $\vec v_A\approx(0{,}17;0{,}49)$, $\vec v_B\approx(-0{,}20;0{,}54)$ avant le choc ; $\vec v_A'\approx(-0{,}07;0{,}42)$, $\vec v_B'\approx(0{,}11;0{,}63)$ après, en m/s dans le repère $(Ox,Oy)$ de la feuille. On cherche à vérifier expérimentalement la conservation de la quantité de mouvement du système $\{A+B\}$ et à classifier le choc.


> [!question]- 🪝 Accroche
> **Où est passée l'énergie ?**
>
> *Durée de l'introduction : 3 min*
>
> *La quantité de mouvement avant et après est la même. Et l'énergie cinétique ? Si elle diminue, où va-t-elle ? Et peut-elle **augmenter** dans un choc ?*
>
> **Idée clé : la quantité de mouvement est conservée dans tout choc isolé, l'énergie cinétique seulement dans un choc élastique.** Dans un choc réel, l'énergie cinétique macroscopique diminue ; elle peut augmenter s'il y a libération d'énergie interne (explosion, ressort relâché) : c'est ce qui se passe dans une fusée.




> [!abstract]- 🧠 À savoir avant
> **Démonstration de la conservation de $\vec p_{\rm tot}$**
>
> Pour un système isolé, $\vec p_{\rm tot}$ est conservée (voir la partie théorique). Les vecteurs $\vec p$ ont été tracés dans la partie précédente.
>
> **Énergie cinétique**
>
> $E_c=\tfrac12mv^2$ est une grandeur **scalaire** : l'énergie cinétique d'un système est la somme arithmétique des énergies cinétiques de ses parties.




> [!info]- 🎯 Ce que tu sauras faire
> **Vérifier une loi de conservation avec une barre d'erreur**
>
> Construire $\vec p_{\rm tot}$ avant et après, comparer les deux à l'incertitude de mesure, calculer $E_c$ avant et après, déterminer le type de choc et conclure avec un esprit critique.




> [!tip]- 📖 Rappel de cours
> **Critère de classification**
>
> On compare $E_c'/E_c$ à $1$ en tenant compte de l'incertitude $\delta E_c/E_c\approx2\,\delta v/v$ : choc élastique si $|E_c'-E_c|\lesssim\delta E_c$ ; partiellement élastique si la perte est significative ; mou si les corps repartent ensemble.




> [!note]- 🧮 Outils mathématiques
> **Somme vectorielle par composantes**
>
> $\vec p_{\rm tot}=(p_{A,x}+p_{B,x},\,p_{A,y}+p_{B,y})$, norme $\sqrt{p_x^2+p_y^2}$.
>
> **Écart relatif**
>
> $\varepsilon=\dfrac{|X'-X|}{X}$ ; on le compare à l'incertitude relative de la grandeur. Pour $E_c=\tfrac12mv^2$, l'incertitude relative est doublée.



**q1.** - [10.] Construire le vecteur $\vec p_{\rm tot}=\vec p_A+\vec p_B$ avant le choc, puis $\vec p_{\rm tot}'=\vec p_A'+\vec p_B'$ après le choc. Comparer ces deux vecteurs.
- [11.] Calculer les variations $\Delta\vec p_A$ et $\Delta\vec p_B$ en composantes et en déduire $\Delta\vec p_A+\Delta\vec p_B$. Que vaut cette somme dans un système isolé ?
- [12.] Quelles sont les causes d'écart avec la conservation parfaite de la quantité de mouvement ?


> [!tip]- 💡 Coup de pouce
> Faites la somme composante par composante. Pour les causes d'écart, pensez à la mesure (pointage, échelle) et à la physique (coussin d'air imparfait, table non horizontale).



**q2.** - [13.] Calculer l'énergie cinétique totale du système $\{A+B\}$ avant puis après le choc.
- [14.] Le choc est-il élastique, partiellement élastique ou mou ? Estimer l'incertitude sur $E_c$ pour justifier la réponse.
- [15.] Que ferait-on pour qu'un choc soit mou ? Que vaudrait alors $\vec v_f$ et $E_c$ pour les données de l'annexe ?


> [!tip]- 💡 Coup de pouce
> $E_c=\tfrac12m_Av_A^2+\tfrac12m_Bv_B^2$. L'incertitude relative sur $E_c$ est le double de celle sur $v$. Pour le choc mou : $\vec v_f=\dfrac{\vec p_{\rm tot}}{m_A+m_B}$.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex1-seance-1-theorie-du-choc-et-quantite-de-mouvement|Exercice 1 — Séance 1 -- Théorie du choc et quantité de mouvement]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex4-extension-choc-elastique-oblique-angle-maximal-de-deviation-et-transfert-d-energie|Exercice 4 — Extension -- Choc élastique oblique : angle maximal de déviation et transfert d'énergie]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex5-seance-2-equation-de-tsiolkovski-propulsion-par-ejection-de-masse|Exercice 5 — Séance 2 -- Équation de Tsiolkovski : propulsion par éjection de masse]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex6-seance-2-application-un-lanceur-a-deux-etages-inspire-du-falcon-9|Exercice 6 — Séance 2 -- Application : un lanceur à deux étages inspiré du Falcon 9]]


