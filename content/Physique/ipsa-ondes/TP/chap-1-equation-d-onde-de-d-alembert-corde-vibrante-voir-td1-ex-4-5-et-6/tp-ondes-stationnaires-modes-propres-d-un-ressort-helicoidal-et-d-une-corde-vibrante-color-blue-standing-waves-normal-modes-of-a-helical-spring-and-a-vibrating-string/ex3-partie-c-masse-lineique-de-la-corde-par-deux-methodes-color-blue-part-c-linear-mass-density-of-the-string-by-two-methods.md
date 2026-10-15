---
title: "Exercice 3 — Partie C — Masse linéique de la corde par deux méthodes {\\color{blue}(Part C — Linear mass density of the string by two methods)}"
tags:
  - tp
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6
---

[[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/index|⬅ Retour]] · [📄 Corrigé](/pdfs/tp1_PhV212_corrige.pdf) · [📄 Énoncé](/pdfs/tp1_PhV212_enonce.pdf) · [📄 Aides](/pdfs/tp1_PhV212_aides.pdf) · [📄 Fiche enseignant](/pdfs/tp1_PhV212_fiche.pdf)

### Exercice 3. Partie C — Masse linéique de la corde par deux méthodes {\color{blue}(Part C — Linear mass density of the string by two methods)}

On détermine $\mu$ (1) à partir des célérités de la partie B via $c^2=F/\mu$, (2) par mesure directe $\mu=m/L_0$, puis on compare et on prédit $c_{\text{th}}$ pour les trois tensions. **Question scientifique :** peut-on déterminer $\mu$ par deux méthodes indépendantes et cohérentes ?

<span style="color:blue">We determine $\mu$ (1) from the speeds of Part B through $c^2=F/\mu$, (2) by direct measurement $\mu=m/L_0$, then compare and predict $c_{\text{th}}$ for the three tensions. **Scientific question:** can $\mu$ be determined by two independent, consistent methods?</span>

**q1.** C1–C2 — Calculer $c_{\exp}^2$ pour chaque tension et tracer $c^2=f(F)$ (graphique C.1). Relever l'équation de l'ajustement.

<span style="color:blue">C1–C2 — Compute $c_{\exp}^2$ for each tension and plot $c^2$ versus $F$ (graph C.1). Read the fit equation.</span>

> [!tip]- 💡 Coup de pouce
> **Données {\color{blue}(Data)}**
>
> Reprendre les $c_{\exp}$ de la partie B et les élever au carré.
>
> <span style="color:blue">Take the $c_{\exp}$ of Part B and square them.</span>


> [!success]- ✅ Correction
> **Valeurs provisoires {\color{blue}(Provisional values)}**
>
> \begin{center}
> \begin{tabular}{|c|c|c|}
> \hline
> $F$ (N) & $c_{\exp}$ (m/s) & $c_{\exp}^2$ (m$^2$/s$^2$) \\ \hline
> 0,6 & 17,26 & 297,9 \\ \hline
> 0,8 & 19,92 & 396,8 \\ \hline
> 1,0 & 22,28 & 496,4 \\ \hline
> \end{tabular}
> \end{center}
> Ajustement : $c^2=497\,F+0{,}3$ (pente $\approx497$ m$^2$s$^{-2}$N$^{-1}$).
>
> <span style="color:blue">Table above. Fit: $c^2=497\,F+0.3$ (slope $\approx497$).</span>


> [!example]- 📝 Solution détaillée
> **Contrôle {\color{blue}(Check)}**
>
> L'ordonnée à l'origine doit être proche de $0$ ($c^2=F/\mu$ passe par l'origine). Trois points seulement : insister sur le caractère indicatif de l'incertitude sur la pente.
>
> <span style="color:blue">The intercept should be close to $0$ ($c^2=F/\mu$ goes through the origin). Only three points: stress that the slope uncertainty is indicative.</span>


**q2.** C3 — Déduire de la pente la masse linéique $\mu_{\text{ondes}}$.

<span style="color:blue">C3 — Deduce from the slope the linear mass density $\mu_{\text{waves}}$.</span>

> [!tip]- 💡 Coup de pouce
> **Pente {\color{blue}(Slope)}**
>
> La pente vaut $1/\mu$.
>
> <span style="color:blue">The slope equals $1/\mu$.</span>


> [!success]- ✅ Correction
> **Valeur provisoire {\color{blue}(Provisional value)}**
>
> $\mu_{\text{ondes}}=1/497\approx2{,}01\times10^{-3}$ kg/m.
>
> <span style="color:blue">$\mu_{\text{waves}}=1/497\approx2.01\times10^{-3}$ kg/m.</span>


> [!example]- 📝 Solution détaillée
> **Rédaction {\color{blue}(Write-up)}**
>
> $c^2=\dfrac1\mu F$, donc la pente $p=1/\mu$ et $\mu_{\text{ondes}}=1/p=\dfrac{1}{497}=2{,}01\times10^{-3}$ kg/m. Incertitude indicative : $\Delta\mu/\mu\approx2\Delta c/c\approx2\,\%$, soit $\Delta\mu\approx0{,}04\times10^{-3}$ kg/m.
>
> <span style="color:blue">$c^2=\dfrac1\mu F$, so the slope $p=1/\mu$ and $\mu_{\text{waves}}=1/p=\dfrac{1}{497}=2.01\times10^{-3}$ kg/m. Indicative uncertainty: $\Delta\mu/\mu\approx2\Delta c/c\approx2\,\%$, i.e. $\Delta\mu\approx0.04\times10^{-3}$ kg/m.</span>


**q3.** C4–C5 — Calculer $\mu_{\text{direct}}=m/L_0$ et son incertitude.

<span style="color:blue">C4–C5 — Compute $\mu_{\text{direct}}=m/L_0$ and its uncertainty.</span>

> [!tip]- 💡 Coup de pouce
> **Incertitude {\color{blue}(Uncertainty)}**
>
> Différentielle logarithmique du quotient : les incertitudes relatives s'ajoutent.
>
> <span style="color:blue">Logarithmic differential of a quotient: relative uncertainties add up.</span>


> [!success]- ✅ Correction
> **Valeurs provisoires {\color{blue}(Provisional values)}**
>
> $\mu_{\text{direct}}=\dfrac{3{,}0\times10^{-3}}{1{,}500}=2{,}00\times10^{-3}$ kg/m ; $\Delta\mu=\mu\left(\dfrac{0{,}1}{3{,}0}+\dfrac{0{,}005}{1{,}500}\right)=2{,}00\times10^{-3}\times0{,}0367\approx7\times10^{-5}$ kg/m. Résultat : $\mu_{\text{direct}}=(2{,}00\pm0{,}07)\times10^{-3}$ kg/m.
>
> <span style="color:blue">$\mu_{\text{direct}}=(2.00\pm0.07)\times10^{-3}$ kg/m, with $m=3.0$ g, $L_0=1.500$ m, $\Delta m=0.1$ g, $\Delta L_0=0.005$ m.</span>


> [!example]- 📝 Solution détaillée
> **Remarque {\color{blue}(Remark)}**
>
> L'incertitude est dominée par celle sur $m$ ($3{,}3\,\%$) ; la longueur apporte seulement $0{,}3\,\%$. Rappeler la conversion g $\to$ kg.
>
> <span style="color:blue">The uncertainty is dominated by that on $m$ ($3.3\,\%$); the length contributes only $0.3\,\%$. Remind students of the g to kg conversion.</span>


**q4.** C6 — Avec $\mu_{\text{direct}}$, calculer $c_{\text{th}}=\sqrt{F/\mu_{\text{direct}}}$ pour les trois tensions, $\Delta c_{\text{th}}$ et l'écart relatif avec $c_{\exp}$. Les valeurs sont-elles compatibles ?

<span style="color:blue">C6 — With $\mu_{\text{direct}}$, compute $c_{\text{th}}=\sqrt{F/\mu_{\text{direct}}}$ for the three tensions, $\Delta c_{\text{th}}$ and the relative deviation from $c_{\exp}$. Are the values compatible?</span>

> [!tip]- 💡 Coup de pouce
> **Propagation {\color{blue}(Propagation)}**
>
> $\dfrac{\Delta c_{\text{th}}}{c_{\text{th}}}=\dfrac12\left(\dfrac{\Delta F}{F}+\dfrac{\Delta\mu}{\mu}\right)$ avec $\Delta F=0{,}03$ N.
>
> <span style="color:blue">$\dfrac{\Delta c_{\text{th}}}{c_{\text{th}}}=\dfrac12\left(\dfrac{\Delta F}{F}+\dfrac{\Delta\mu}{\mu}\right)$ with $\Delta F=0.03$ N.</span>


> [!success]- ✅ Correction
> **Valeurs provisoires {\color{blue}(Provisional values)}**
>
> \begin{center}
> \begin{tabular}{|c|c|c|c|c|}
> \hline
> $F$ (N) & $c_{\text{th}}$ (m/s) & $\Delta c_{\text{th}}$ (m/s) & $c_{\exp}$ (m/s) & écart (\%) \\ \hline
> 0,6 & 17,32 & 0,75 & 17,26 & $-0{,}3$ \\ \hline
> 0,8 & 20,00 & 0,74 & 19,92 & $-0{,}4$ \\ \hline
> 1,0 & 22,36 & 0,75 & 22,28 & $-0{,}4$ \\ \hline
> \end{tabular}
> \end{center}
> Compatibles : $|c_{\text{th}}-c_{\exp}|\le0{,}1\ll\Delta c_{\text{th}}$.
>
> <span style="color:blue">Table above. Compatible: $|c_{\text{th}}-c_{\exp}|\le0.1\ll\Delta c_{\text{th}}$.</span>


> [!example]- 📝 Solution détaillée
> **Exemple de calcul {\color{blue}(Worked example)}**
>
> Pour $F=0{,}6$ N : $c_{\text{th}}=\sqrt{0{,}6/2{,}00\times10^{-3}}=17{,}32$ m/s ; $\dfrac{\Delta c}{c}=\dfrac12(0{,}050+0{,}037)=0{,}043$, donc $\Delta c=0{,}75$ m/s ; écart relatif $=\dfrac{17{,}26-17{,}32}{17{,}32}=-0{,}3\ \%$.
>
> <span style="color:blue">For $F=0.6$ N: $c_{\text{th}}=\sqrt{0.6/2.00\times10^{-3}}=17.32$ m/s; $\dfrac{\Delta c}{c}=\dfrac12(0.050+0.037)=0.043$, so $\Delta c=0.75$ m/s; relative deviation $=-0.3\,\%$.</span>


**q5.** C7 — Les deux déterminations de $\mu$ et la comparaison $c_{\text{th}}/c_{\exp}$ donnent-elles une description cohérente de la corde ? Justifier quantitativement.

<span style="color:blue">C7 — Do the two determinations of $\mu$ and the comparison $c_{\text{th}}/c_{\exp}$ give a consistent description of the string? Justify quantitatively.</span>

> [!success]- ✅ Correction
> **Réponse attendue {\color{blue}(Expected answer)}**
>
> Oui : $\mu_{\text{ondes}}=2{,}01\times10^{-3}$ et $\mu_{\text{direct}}=(2{,}00\pm0{,}07)\times10^{-3}$ kg/m diffèrent de $0{,}5\ \%$, bien en dessous de l'incertitude ($3{,}7\ \%$). Les écarts sur $c$ sont inférieurs à $0{,}5\ \%$.
>
> <span style="color:blue">Yes: $\mu_{\text{waves}}=2.01\times10^{-3}$ and $\mu_{\text{direct}}=(2.00\pm0.07)\times10^{-3}$ kg/m differ by $0.5\,\%$, well below the uncertainty ($3.7\,\%$). Deviations on $c$ are below $0.5\,\%$.</span>


> [!example]- 📝 Solution détaillée
> **Conclusion type {\color{blue}(Typical conclusion)}**
>
> Le modèle $c=\sqrt{F/\mu}$ est validé à l'incertitude près ; la mesure par ondes est plus précise que la pesée ($\Delta m/m\approx3\ \%$). L'accord est un peu trop bon pour être sûr : ne pas surinterpréter avec seulement trois tensions.
>
> <span style="color:blue">The model $c=\sqrt{F/\mu}$ is validated within uncertainty; the wave method is more precise than weighing ($\Delta m/m\approx3\,\%$). The agreement is almost too good: do not over-interpret with only three tensions.</span>


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex2-corde-de-nylon|Exercice 2 — Corde de nylon]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex3-celerite-d-une-onde-sur-une-corde-homogene|Exercice 3 — Célérité d’une onde sur une corde homogène]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex5-synthese-scientifique-du-tp-color-blue-scientific-summary-of-the-lab|Exercice 5 — Synthèse scientifique du TP {\color{blue}(Scientific summary of the lab)}]] · [[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]]

