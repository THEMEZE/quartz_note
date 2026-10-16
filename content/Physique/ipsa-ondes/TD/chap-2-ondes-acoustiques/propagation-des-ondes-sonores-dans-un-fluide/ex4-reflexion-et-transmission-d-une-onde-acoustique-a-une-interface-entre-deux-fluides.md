---
title: "Exercice 4 — Réflexion et transmission d'une onde acoustique à une interface entre deux fluides"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · <a href="/pdfs/td2_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_PhV212_enonce)</a> · <a href="/pdfs/td2_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_enonce)</a> · <a href="/pdfs/td2_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_aides)</a> · <a href="/pdfs/td2_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_exs_maison_aide)</a>

### Exercice 4. Réflexion et transmission d'une onde acoustique à une interface entre deux fluides *(facultatif)*

On considère deux fluides parfaits semi-infinis séparés par une interface
plane en $x=0$ : le fluide (1), de masse volumique $\rho_1$ et de célérité
du son $c_1$, occupe la région $x<0$ ; le fluide (2), de masse volumique
$\rho_2$ et de célérité $c_2$, occupe la région $x>0$. On définit
l'impédance acoustique caractéristique de chaque fluide par $Z_i=\rho_i c_i$.

Une onde acoustique plane, de pression $\tilde p_I(x,t)=A\,e^{i(\omega t-k_1x)}$
($k_1=\omega/c_1$), est envoyée depuis le fluide (1) vers l'interface, en
incidence normale. Elle donne naissance à une onde réfléchie dans le fluide
(1) et à une onde transmise dans le fluide (2) :
$$\tilde p_R(x,t) = R\,A\,e^{i(\omega t+k_1x)}, \qquad \tilde p_T(x,t) = T\,A\,e^{i(\omega t-k_2x)}, \qquad k_2=\omega/c_2.$$

**q1.** Définir l'impédance acoustique caractéristique $Z=\rho c$ d'un fluide et
donner son interprétation physique (on pourra s'appuyer sur l'analogie
avec l'impédance électrique). Écrire, en notation complexe, les
expressions de la vitesse particulaire associée à chacune des trois
ondes (incidente, réfléchie, transmise) en fonction de la pression et
des impédances $Z_1$, $Z_2$.

> [!tip]- 💡 Coup de pouce
> Pour une onde plane progressive $\tilde p = A e^{i(\omega t \mp kx)}$, l'équation d'Euler linéarisée $\rho_0\partial_t \tilde v = -\partial_x \tilde p$ donne directement $\tilde v = \pm \tilde p /Z$ selon le sens de propagation (cf. point cours de l'exercice 1 pour l'équation d'Euler linéarisée).


**q2.** En écrivant la continuité de la pression et de la vitesse particulaire
en $x=0$, établir les expressions des coefficients de réflexion $R$ et
de transmission $T$ en amplitude de pression, en fonction de $Z_1$ et $Z_2$.

> [!tip]- 💡 Coup de pouce
> Deux équations, deux inconnues ($R$ et $T$) : substituez l'une dans l'autre (cf. les deux équations déjà posées dans le point cours).


**q3.** Application numérique : calculer $R$, $T$, et les coefficients
énergétiques $R_I$ et $T_I$ pour une onde issue de l'air
($\rho_1=1{,}2\text{ kg}\cdot\text{m}^{-3}$, $c_1=340\text{ m}\cdot\text{s}^{-1}$)
incidente sur une surface d'eau
($\rho_2=1000\text{ kg}\cdot\text{m}^{-3}$, $c_2=1500\text{ m}\cdot\text{s}^{-1}$).
Commenter en lien avec l'expérience quotidienne.

> [!tip]- 💡 Coup de pouce
> Calculez d'abord $Z_1$ et $Z_2$ séparément, en gardant les unités SI.


**q4.** On envoie maintenant l'onde depuis l'eau vers l'air (mêmes fluides
qu'en question 3, ordre inversé). Recalculer $R$ et commenter le signe
obtenu. Ce résultat est-il cohérent avec le principe de retour inverse
de la lumière (ici, du son) ?

> [!tip]- 💡 Coup de pouce
> Échangez les rôles de $Z_1$ et $Z_2$ dans l'expression de $R$ établie en question 2.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex5-energie-intensite-acoustique-et-niveau-sonore-de-l-oreille-humaine-a-l-onde-stationnaire|Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex6-tube-d-impedance-mesurer-l-absorption-d-un-materiau-avec-une-onde-stationnaire-partielle|Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex7-resonateur-de-helmholtz-la-bouteille-qui-chante|Exercice 7 — Résonateur de Helmholtz : la bouteille qui chante]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex1-celerite-d-une-onde-acoustique-dans-un-fluide-parfait|Exercice 1 — Célérité d'une onde acoustique dans un fluide parfait]]

