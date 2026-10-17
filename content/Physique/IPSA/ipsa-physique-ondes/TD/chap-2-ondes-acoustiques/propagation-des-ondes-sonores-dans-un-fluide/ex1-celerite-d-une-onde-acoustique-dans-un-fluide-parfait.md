---
title: "Exercice 1 — Célérité d'une onde acoustique dans un fluide parfait"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · <a href="/pdfs/td2_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_PhV212_enonce)</a> · <a href="/pdfs/td2_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_enonce)</a> · <a href="/pdfs/td2_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_aides)</a> · <a href="/pdfs/td2_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td2_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_PhV212_corrige)</a> · <a href="/pdfs/td2_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_corrige)</a> · <a href="/pdfs/td2_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 1. Célérité d'une onde acoustique dans un fluide parfait

Le fluide considéré est de l'air, modélisé comme un fluide parfait, de
rapport des capacités calorifiques $\gamma = C_P/C_V = 1.4$. Masse molaire
$M = 29$ g/mol, température $T = 293$ K, $R = 8.32$ J·mol$^{-1}$·K$^{-1}$.
On rappelle le coefficient de compressibilité $\chi = -\dfrac{1}{V}\dfrac{\partial V}{\partial P}$.

**q1.** On suppose que lors du passage de l'onde acoustique, le fluide subit
une transformation isotherme. En le modélisant comme un gaz parfait,
montrer que $c_T = \sqrt{RT/M}$.

> [!tip]- 💡 Coup de pouce
> Pour un gaz parfait en transformation isotherme, $PV=$ cte à $T$ fixé,
> donc $\chi_T = 1/P$. La célérité du son vérifie en général $c=\sqrt{1/(\rho\chi)}$
> (rappelée dans les prérequis).


> [!success]- ✅ Correction
> $c_T=\sqrt{RT/M}$.


> [!example]- 📝 Solution détaillée
> **Calcul de $\chi_T$ pour un gaz parfait isotherme**
>
> Pour une mole de gaz parfait, l'équation d'état s'écrit $PV_m=RT$ à $T$ fixé, où $V_m$ est le volume molaire. En dérivant à $T$ constant :
> $$\left(\frac{\partial V_m}{\partial P}\right)_T = -\frac{RT}{P^2} = -\frac{V_m}{P}.$$
> Par définition, on en déduit directement
> $$\chi_T = -\frac{1}{V_m}\left(\frac{\partial V_m}{\partial P}\right)_T = \frac{1}{P}.$$
>
> **Report dans la formule de célérité**
>
> On utilise la relation générale établie dans le prérequis, $c^2 = 1/(\rho\chi)$, avec $\chi=\chi_T=1/P$ et $\rho = M/V_m = MP/(RT)$ (masse volumique du gaz parfait, obtenue en écrivant $\rho = m/V = M/V_m$ puis en substituant $V_m=RT/P$) :
> \begin{eqnarray}
>   c_T^2 &=& \frac{1}{\rho\,\chi_T} = \frac{P}{\rho} = \frac{P}{MP/(RT)} = \frac{RT}{M}, \nonumber
> \end{eqnarray}
> d'où, en prenant la racine carrée (positive, car $c_T$ est une célérité) :
> $$\boxed{c_T = \sqrt{\frac{RT}{M}}}.$$


**q2.** Calculer $c_T$ numériquement. Est-ce en accord avec la mesure expérimentale ($\approx 340~m/s$) ? Conclure.

> [!tip]- 💡 Coup de pouce
> Attention aux unités SI : $M$ en kg/mol.


> [!success]- ✅ Correction
> $c_T=\sqrt{8.32\times293/0.029}\approx290$ m/s -- sous-estime la valeur mesurée ($\approx 340~m/s$).


> [!example]- 📝 Solution détaillée
> **Application numérique**
>
> On convertit d'abord $M$ en unités SI : $M = 29~\text{g/mol} = 0{,}029~\text{kg/mol}$. On calcule alors :
> $$c_T = \sqrt{\frac{RT}{M}} = \sqrt{\frac{8{,}32 \times 293}{0{,}029}} = \sqrt{\frac{2437{,}8}{0{,}029}} = \sqrt{84062} \approx 290~\text{m}\cdot\text{s}^{-1}.$$
>
> **Comparaison à l'expérience et conclusion**
>
> La valeur mesurée expérimentalement pour la vitesse du son dans l'air à température ambiante est $c_{\text{exp}} \approx 340~\text{m}\cdot\text{s}^{-1}$. L'écart relatif est
> $$\frac{c_{\text{exp}}-c_T}{c_{\text{exp}}} \approx \frac{340-290}{340} \approx 15~\%,$$
> ce qui est bien trop important pour être attribué à une simple imprécision expérimentale ou à un arrondi sur les données ($T$, $M$, $R$). Le modèle isotherme sous-estime donc significativement la célérité réelle du son : l'hypothèse d'une transformation isotherme lors du passage de l'onde acoustique doit être remise en cause (voir question 3).


**q3.** À quel type de transformation correspond alors la propagation de l'onde sonore ? Définir cette transformation.

> [!tip]- 💡 Coup de pouce
> L'écart avec l'isotherme suggère une transformation trop rapide pour un échange de chaleur : pensez à l'adiabatique réversible (isentropique).


> [!success]- ✅ Correction
> Transformation adiabatique réversible (isentropique) : rapide devant les temps d'échange thermique, sans échange de chaleur ni irréversibilité.


> [!example]- 📝 Solution détaillée
> **Argument d'échelle de temps**
>
> Le point cours de thermodynamique rappelle qu'une transformation isotherme suppose un équilibre thermique permanent avec un thermostat extérieur, ce qui nécessite un temps caractéristique d'échange thermique par diffusion suffisamment court devant la période de l'onde. Or, pour un son audible ($f\sim 1~\text{kHz}$, période $T_{\text{ac}}\sim 1~\text{ms}$), le temps de diffusion thermique sur une distance de l'ordre d'une longueur d'onde ($\lambda \sim 0{,}3~\text{m}$) est très supérieur à $T_{\text{ac}}$ : la chaleur n'a pas le temps de s'évacuer d'une zone comprimée vers une zone détendue pendant une période acoustique. La transformation est donc **adiabatique** (pas d'échange de chaleur avec l'extérieur pendant le temps caractéristique du phénomène).
>
> **Réversibilité et définition complète**
>
> Par ailleurs, les amplitudes de perturbation mises en jeu dans une onde sonore usuelle sont infinitésimales (surpressions typiquement inférieures au pascal, à comparer à $P_0\sim 10^5~\text{Pa}$) : il n'y a donc pas de dissipation irréversible notable par viscosité ou par gradients de température finis. La transformation est donc également **réversible**.
>
> On retient : la propagation du son correspond, en première approximation, à une transformation **adiabatique réversible**, c'est-à-dire **isentropique** (à entropie constante), ce qui justifie l'usage du coefficient de compressibilité $\chi_S$ plutôt que $\chi_T$.


**q4.** Montrer que pour ce type de transformation, $c_S=\sqrt{\gamma RT/M}$. Calculer numériquement et commenter.

> [!tip]- 💡 Coup de pouce
> Pour une transformation isentropique d'un gaz parfait, $PV^\gamma=$ cte, donc $\chi_S=1/(\gamma P)$ (cf. point cours de thermodynamique).


> [!success]- ✅ Correction
> $c_S=\sqrt{\gamma RT/M}\approx 343$ m/s -- en excellent accord avec la mesure.


> [!example]- 📝 Solution détaillée
> **Calcul de $\chi_S$ à partir de la loi de Laplace**
>
> La loi de Laplace pour une transformation isentropique d'un gaz parfait s'écrit $PV_m^\gamma = \text{cte}$. En différenciant logarithmiquement à entropie constante :
> $$\frac{\mathrm{d}P}{P} + \gamma\,\frac{\mathrm{d}V_m}{V_m} = 0 \quad\Longrightarrow\quad \left(\frac{\partial V_m}{\partial P}\right)_S = -\frac{V_m}{\gamma P},$$
> d'où, par définition,
> $$\chi_S = -\frac{1}{V_m}\left(\frac{\partial V_m}{\partial P}\right)_S = \frac{1}{\gamma P}.$$
>
> **Report dans la formule de célérité et calcul numérique**
>
> En reprenant le même calcul qu'à la question 1, avec $\chi_S=1/(\gamma P)$ au lieu de $\chi_T=1/P$, et $\rho=MP/(RT)$ :
> $$c_S^2 = \frac{1}{\rho\,\chi_S} = \frac{\gamma P}{\rho} = \frac{\gamma RT}{M} \quad\Longrightarrow\quad \boxed{c_S = \sqrt{\frac{\gamma RT}{M}}}.$$
> Numériquement :
> $$c_S = \sqrt{\frac{1{,}4 \times 8{,}32 \times 293}{0{,}029}} = \sqrt{\frac{3412{,}9}{0{,}029}} = \sqrt{117686} \approx 343~\text{m}\cdot\text{s}^{-1}.$$
> Cette valeur est en excellent accord (à moins de $1\%$) avec la mesure expérimentale $c_{\text{exp}}\approx 340$–$343~\text{m}\cdot\text{s}^{-1}$, ce qui confirme que le modèle isentropique est le bon modèle thermodynamique pour décrire la propagation du son dans un gaz parfait. On note aussi que $c_S/c_T = \sqrt{\gamma}\approx 1{,}18$, cohérent avec l'écart d'environ $15\%$ observé à la question 2.


**q5.** Comparer la vitesse du son au niveau de la mer et au sommet de l'Everest (densité de l'air environ 3 fois plus faible, composition chimique identique).

> [!tip]- 💡 Coup de pouce
> $c_S=\sqrt{\gamma P/\rho}$ ; à composition chimique et température fixées, comment $P/\rho$ varie-t-il avec l'altitude ?


> [!success]- ✅ Correction
> À température égale, $c_S=\sqrt{\gamma RT/M}$ ne dépend pas de $\rho$ ni de $P$ séparément, seulement de $T$ : la vitesse du son est quasiment la même (elle varie surtout avec la température, qui baisse en altitude, donc $c$ diminue légèrement -- pas d'un facteur 3).


> [!example]- 📝 Solution détaillée
> **Piège de l'énoncé : ne pas confondre $\rho$, $P$ et $T$**
>
> On pourrait être tenté d'utiliser directement $c_S=\sqrt{\gamma P/\rho}$ et de penser que, $\rho$ étant environ 3 fois plus faible au sommet de l'Everest, la vitesse du son serait modifiée d'un facteur $\sqrt{3}$. C'est une erreur : $P$ diminue également avec l'altitude (loi de l'atmosphère isotherme ou standard), et le rapport $P/\rho$ n'est pas indépendant de $\rho$ seul. Il faut repartir de l'expression $c_S=\sqrt{\gamma RT/M}$, obtenue à la question 4, qui ne fait plus intervenir $P$ ni $\rho$ séparément mais uniquement la température $T$ (à composition chimique $M$, $\gamma$ fixée).
>
> **Effet réel : la dépendance en température**
>
> En utilisant le modèle de l'atmosphère standard (gradient thermique $\mathrm{d}T/\mathrm{d}z \approx -6{,}5\times10^{-3}~\text{K}\cdot\text{m}^{-1}$ dans la troposphère), la température à l'altitude de l'Everest ($z\approx 8849~\text{m}$) est réduite d'environ :
> $$\Delta T \approx 6{,}5\times10^{-3}\times 8849 \approx 57{,}5~\text{K}.$$
> En partant de $T_0=293~\text{K}$ au niveau de la mer, on obtient $T\approx 235{,}5~\text{K}$ au sommet, soit :
> $$c_S(\text{sommet}) = \sqrt{\frac{1{,}4\times 8{,}32\times 235{,}5}{0{,}029}} \approx 308~\text{m}\cdot\text{s}^{-1},$$
> à comparer à $c_S(\text{mer})\approx 343~\text{m}\cdot\text{s}^{-1}$ : soit une baisse d'environ $10\%$, uniquement due à la baisse de température, et non un facteur 3 comme le suggérerait un raisonnement naïf basé sur $\rho$ seul.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex7-resonateur-de-helmholtz-la-bouteille-qui-chante|Exercice 7 — Résonateur de Helmholtz : la bouteille qui chante]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex4-reflexion-et-transmission-d-une-onde-acoustique-a-une-interface-entre-deux-fluides|Exercice 4 — Réflexion et transmission d'une onde acoustique à une interface entre deux fluides]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]]

