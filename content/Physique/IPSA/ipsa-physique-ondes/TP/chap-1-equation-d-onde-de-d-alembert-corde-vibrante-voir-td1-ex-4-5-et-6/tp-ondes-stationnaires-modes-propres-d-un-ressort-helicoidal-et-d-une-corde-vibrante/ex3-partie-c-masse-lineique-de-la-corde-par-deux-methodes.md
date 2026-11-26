---
title: "Exercice 3 — Partie C — Masse linéique de la corde par deux méthodes"
tags:
  - tp
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6
---

[[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/index|⬅ Retour]] · <a href="/pdfs/tp1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/tp1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

<p><span style="color:#1565C0">(Part C — Linear mass density of the string by two methods)</span></p>

### Exercice 3. Partie C — Masse linéique de la corde par deux méthodes <span style="color:#1565C0">(Part C — Linear mass density of the string by two methods)</span>

*⭐ Indispensable · Difficulté ●●●●○ · ⏱ 60 min · Type : Analyse de données et incertitudes*

On détermine $\mu$ (1) à partir des célérités de la partie B via $c^2=F/\mu$, (2) par mesure directe $\mu=m/L_0$, puis on compare et on prédit $c_{\text{th}}$ pour les trois tensions. **Question scientifique :** peut-on déterminer $\mu$ par deux méthodes indépendantes et cohérentes ?

<span style="color:#1565C0">We determine $\mu$ (1) from the speeds of Part B through $c^2=F/\mu$, (2) by direct measurement $\mu=m/L_0$, then compare and predict $c_{\text{th}}$ for the three tensions. **Scientific question:** can $\mu$ be determined by two independent, consistent methods?</span>


> [!question]- 🪝 Accroche
> **Peser une corde sans la peser <span style="color:#1565C0">(Weighing a string without weighing it)</span>**
>
> *Durée de l'introduction : 3 min, avant les calculs*
>
> *On a mesuré des fréquences et une tension, jamais la masse de la corde. Peut-on en déduire la masse par mètre ? Quelle droite faut-il tracer pour que la pente donne directement $\mu$ ou $1/\mu$ ?
>
> <span style="color:#1565C0">We measured frequencies and a tension, never the mass of the string. Can we deduce the mass per meter? Which line must be plotted so that the slope gives $\mu$ or $1/\mu$ directly?</span>*
>
> **Idée clé : linéariser.** $c^2=F/\mu$ est une droite de pente $1/\mu$ en variables $(F,c^2)$ ; la mesure directe $\mu=m/L_0$ donne une valeur indépendante pour comparer.
>
> <span style="color:#1565C0">**Key idea: linearize.** $c^2=F/\mu$ is a line of slope $1/\mu$ in the variables $(F,c^2)$; the direct measurement $\mu=m/L_0$ gives an independent value to compare with.</span>




> [!note]- 🧮 Outils mathématiques
> **Différentielle logarithmique <span style="color:#1565C0">(Logarithmic differential)</span>**
>
> $\mu=m/L_0$ : $\dfrac{\Delta\mu}{\mu}=\dfrac{\Delta m}{m}+\dfrac{\Delta L_0}{L_0}$. $c=\sqrt{F/\mu}$ : $\dfrac{\Delta c}{c}=\dfrac12\left(\dfrac{\Delta F}{F}+\dfrac{\Delta\mu}{\mu}\right)$.
>
> <span style="color:#1565C0">$\mu=m/L_0$: $\dfrac{\Delta\mu}{\mu}=\dfrac{\Delta m}{m}+\dfrac{\Delta L_0}{L_0}$. $c=\sqrt{F/\mu}$: $\dfrac{\Delta c}{c}=\dfrac12\left(\dfrac{\Delta F}{F}+\dfrac{\Delta\mu}{\mu}\right)$.</span>
>
> **Compatibilité de deux valeurs <span style="color:#1565C0">(Compatibility of two values)</span>**
>
> Deux valeurs $x_1\pm\Delta_1$ et $x_2\pm\Delta_2$ sont compatibles si $|x_1-x_2|\le\Delta_1+\Delta_2$.
>
> <span style="color:#1565C0">Two values $x_1\pm\Delta_1$ and $x_2\pm\Delta_2$ are compatible if $|x_1-x_2|\le\Delta_1+\Delta_2$.</span>
>
> **Unités SI <span style="color:#1565C0">(SI units)</span>**
>
> $3{,}0$ g $=3{,}0\times10^{-3}$ kg ; vérifier $\mu\sim10^{-3}$ kg/m pour une ficelle fine.
>
> <span style="color:#1565C0">3.0 g $=3.0\times10^{-3}$ kg; check $\mu\sim10^{-3}$ kg/m for a thin string.</span>



**q1.** C1–C2 — Calculer $c_{\exp}^2$ pour chaque tension et tracer $c^2=f(F)$ (graphique C.1). Relever l'équation de l'ajustement.

<span style="color:#1565C0">C1–C2 — Compute $c_{\exp}^2$ for each tension and plot $c^2$ versus $F$ (graph C.1). Read the fit equation.</span>


> [!tip]- 💡 Coup de pouce
> **Données <span style="color:#1565C0">(Data)</span>**
>
> Reprendre les $c_{\exp}$ de la partie B et les élever au carré.
>
> <span style="color:#1565C0">Take the $c_{\exp}$ of Part B and square them.</span>



**q2.** C3 — Déduire de la pente la masse linéique $\mu_{\text{ondes}}$.

<span style="color:#1565C0">C3 — Deduce from the slope the linear mass density $\mu_{\text{waves}}$.</span>


> [!tip]- 💡 Coup de pouce
> **Pente <span style="color:#1565C0">(Slope)</span>**
>
> La pente vaut $1/\mu$.
>
> <span style="color:#1565C0">The slope equals $1/\mu$.</span>



**q3.** C4–C5 — Calculer $\mu_{\text{direct}}=m/L_0$ et son incertitude.

<span style="color:#1565C0">C4–C5 — Compute $\mu_{\text{direct}}=m/L_0$ and its uncertainty.</span>


> [!tip]- 💡 Coup de pouce
> **Incertitude <span style="color:#1565C0">(Uncertainty)</span>**
>
> Différentielle logarithmique du quotient : les incertitudes relatives s'ajoutent.
>
> <span style="color:#1565C0">Logarithmic differential of a quotient: relative uncertainties add up.</span>



**q4.** C6 — Avec $\mu_{\text{direct}}$, calculer $c_{\text{th}}=\sqrt{F/\mu_{\text{direct}}}$ pour les trois tensions, $\Delta c_{\text{th}}$ et l'écart relatif avec $c_{\exp}$. Les valeurs sont-elles compatibles ?

<span style="color:#1565C0">C6 — With $\mu_{\text{direct}}$, compute $c_{\text{th}}=\sqrt{F/\mu_{\text{direct}}}$ for the three tensions, $\Delta c_{\text{th}}$ and the relative deviation from $c_{\exp}$. Are the values compatible?</span>


> [!tip]- 💡 Coup de pouce
> **Propagation <span style="color:#1565C0">(Propagation)</span>**
>
> $\dfrac{\Delta c_{\text{th}}}{c_{\text{th}}}=\dfrac12\left(\dfrac{\Delta F}{F}+\dfrac{\Delta\mu}{\mu}\right)$ avec $\Delta F=0{,}03$ N.
>
> <span style="color:#1565C0">$\dfrac{\Delta c_{\text{th}}}{c_{\text{th}}}=\dfrac12\left(\dfrac{\Delta F}{F}+\dfrac{\Delta\mu}{\mu}\right)$ with $\Delta F=0.03$ N.</span>



**q5.** C7 — Les deux déterminations de $\mu$ et la comparaison $c_{\text{th}}/c_{\exp}$ donnent-elles une description cohérente de la corde ? Justifier quantitativement.

<span style="color:#1565C0">C7 — Do the two determinations of $\mu$ and the comparison $c_{\text{th}}/c_{\exp}$ give a consistent description of the string? Justify quantitatively.</span>


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex2-corde-de-nylon|Exercice 2 — Corde de nylon]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex3-celerite-d-une-onde-sur-une-corde-homogene|Exercice 3 — Célérité d’une onde sur une corde homogène]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex5-synthese-scientifique-du-tp|Exercice 5 — Synthèse scientifique du TP]] · [[physique/IPSA/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]]


