---
title: "Exercice 6 — Contrôle ultrasonore d'une plaque immergée : train d'échos, épaisseur, atténuation et défaut de collage"
tags:
  - td
  - chap-3-interfaces-entre-deux-milieux
---

[[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/index|⬅ Retour]] · <a href="/pdfs/td3_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_PhV212_enonce)</a> · <a href="/pdfs/td3_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_enonce)</a> · <a href="/pdfs/td3_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td3_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td3_PhV212_corrige)</a> · <a href="/pdfs/td3_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td3_corrige)</a> · <a href="/pdfs/td3_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 6. Contrôle ultrasonore d'une plaque immergée : train d'échos, épaisseur, atténuation et défaut de collage *(facultatif)*

Pour contrôler une plaque d'aluminium d'épaisseur $e$ inconnue, on l'immerge dans l'eau et on envoie, sous
incidence normale, une impulsion ultrasonore brève (fréquence centrale $5$ MHz, durée $\simeq0{,}4~\mu$s) à l'aide d'une
sonde émettrice-réceptrice placée dans l'eau. La face arrière de la plaque est en contact avec l'air.
On enregistre sur la sonde un train d'échos notés $E_0$, $E_1$, $E_2,\dots$ : $E_0$ est l'écho de la face avant, $E_n$
($n\ge1$) celui qui a effectué $n$ allers-retours dans la plaque. On note $r_{ij}$ et $t_{ij}$ les coefficients de réflexion
et de transmission en *amplitude de pression* pour une onde allant du milieu $i$ au milieu $j$ :
$r_{ij}=\dfrac{Z_j-Z_i}{Z_i+Z_j}$, $t_{ij}=1+r_{ij}$.

Données : eau ($\rho_w=1000~\text{kg}\cdot\text{m}^{-3}$, $c_w=1500~\text{m}\cdot\text{s}^{-1}$), aluminium
($\rho_A=2700~\text{kg}\cdot\text{m}^{-3}$, $c_A=5110~\text{m}\cdot\text{s}^{-1}$), air ($Z_{\mathrm{air}}=442$ rayl).
On néglige l'atténuation sauf à la question 5, et on admet que le faisceau reste plan (pas de diffraction).

**q1.** Calculer les impédances $Z_w$ et $Z_A$, puis $r_{wA}$, $t_{wA}$, $r_{Aw}$, $t_{Aw}$ et $r_{A,\mathrm{air}}$.
Vérifier que $t_{wA}\,t_{Aw}=1-r_{wA}^2$. Comparer à l'interface air-aluminium de l'exercice 2.

> [!tip]- 💡 Coup de pouce
> $r_{ij}=(Z_j-Z_i)/(Z_i+Z_j)$ et $t_{ij}=1+r_{ij}$ ; $r_{ji}=-r_{ij}$.


> [!success]- ✅ Correction
> $Z_w=1{,}5\times10^6$ rayl, $Z_A=1{,}38\times10^7$ rayl ; $r_{wA}=+0{,}804$, $t_{wA}=1{,}804$, $r_{Aw}=-0{,}804$, $t_{Aw}=0{,}196$, $r_{A,\mathrm{air}}\approx-1$ ; produit $=0{,}354$.


> [!example]- 📝 Solution détaillée
> **Impédances**
>
> $Z_w=1000\times1500=1{,}5\times10^6$ rayl et $Z_A=2700\times5110=1{,}38\times10^7$ rayl (cf. exercice 2).
>
> **Coefficients**
>
> $$r_{wA}=\frac{Z_A-Z_w}{Z_A+Z_w}=\frac{12{,}3}{15{,}3}=+0{,}804,\qquad t_{wA}=1+r_{wA}=1{,}804,$$
> $$r_{Aw}=-0{,}804,\qquad t_{Aw}=1+r_{Aw}=0{,}196,\qquad r_{A,\mathrm{air}}=\frac{442-1{,}38\times10^7}{442+1{,}38\times10^7}\approx-0{,}99994\approx-1.$$
> On vérifie $t_{wA}t_{Aw}=1{,}804\times0{,}196=0{,}354=1-0{,}804^2$. Ici, l'eau est un bien meilleur milieu de couplage que l'air : la fraction d'énergie qui entre dans la plaque est $1-r_{wA}^2=0{,}354$, soit $35\ \%$, contre $1{,}3\times10^{-4}$ pour l'interface air-aluminium de l'exercice 2 ($\sim2\,700$ fois plus).


**q2.** Établir l'expression de l'amplitude de l'écho $E_n$ et calculer numériquement $E_0$, $E_1$, $E_2$ et $E_3$ (l'amplitude de l'onde incidente
dans l'eau est prise égale à $1$). Quels sont les signes des échos ? Quel est le rapport $E_{n+1}/E_n$ ?

> [!tip]- 💡 Coup de pouce
> Suivez l'impulsion : aller dans la plaque ($t_{wA}$), réflexion sur la face arrière ($r_{Ab}$), retour dans l'eau ($t_{Aw}$) pour $E_1$ ; un aller-retour supplémentaire ajoute une réflexion sur la face avant vue de l'intérieur ($r_{Aw}$) puis sur la face arrière.


> [!success]- ✅ Correction
> $E_0=+0{,}804$ ; $E_1=-0{,}354$ ; $E_2=-0{,}284$ ; $E_3=-0{,}229$ ; rapport constant $r_{Aw}r_{Ab}=+0{,}804$.


> [!example]- 📝 Solution détaillée
> **Expression générale**
>
> $E_0=r_{wA}$ (réflexion directe). Pour $E_1$ : transmission dans la plaque, réflexion sur la face arrière, transmission dans l'eau : $E_1=t_{wA}\,r_{Ab}\,t_{Aw}$. Chaque aller-retour supplémentaire ajoute deux réflexions (face avant vue de l'intérieur, puis face arrière), soit le facteur $r_{Aw}r_{Ab}$ :
> $$E_n=t_{wA}\,t_{Aw}\,r_{Ab}\,\big(r_{Aw}\,r_{Ab}\big)^{n-1},\quad n\ge1.$$
>
> **Valeurs numériques**
>
> Avec $r_{Ab}\approx-1$ et $r_{Aw}r_{Ab}=(-0{,}804)(-1)=+0{,}804$ :
> $$E_0=+0{,}804,\quad E_1=0{,}354\times(-1)=-0{,}354,\quad E_2=-0{,}354\times0{,}804=-0{,}284,\quad E_3=-0{,}229.$$
> Les échos $E_n$ ($n\ge1$) sont tous de même signe, opposé à celui de $E_0$, et décroissent en progression géométrique de raison $0{,}804$ (soit $-1{,}9$ dB entre deux échos successifs).


**q3.** Vérifier que l'énergie se conserve : $\sum_{n\ge0}E_n^2=1$. Que représente chaque terme ? Quelle fraction de l'énergie
incidente est renvoyée par $E_0$ ? Par $E_1$, $E_2$, $E_3$ ?

> [!tip]- 💡 Coup de pouce
> $\sum_{n\ge1}E_n^2=(t_{wA}t_{Aw})^2\sum_{n\ge1}(r_{Aw}r_{Ab})^{2(n-1)}$ avec $r_{Ab}^2=1$ : série géométrique de raison $r_{wA}^2$.


> [!success]- ✅ Correction
> $E_0^2=0{,}646$ ; $E_1^2=0{,}125$ ; $E_2^2=0{,}081$ ; $E_3^2=0{,}052$ ; $\sum_{n\ge1}E_n^2=1-r_{wA}^2=0{,}354$ ; total $=1$.


> [!example]- 📝 Solution détaillée
> **Somme de la série**
>
> $E_n^2=(1-r^2)^2r^{2(n-1)}$ avec $r=r_{wA}$ (et $r_{Ab}^2=1$). Donc
> $$\sum_{n\ge1}E_n^2=(1-r^2)^2\sum_{n\ge1}r^{2(n-1)}=\frac{(1-r^2)^2}{1-r^2}=1-r^2,\qquad\sum_{n\ge0}E_n^2=r^2+(1-r^2)=1.$$
>
> **Interprétation numérique**
>
> Les échos reçus dans l'eau emportent chacun une fraction $E_n^2$ de l'énergie incidente : $64{,}6\ \%$ pour $E_0$ (face avant), puis $12{,}5\ \%$, $8{,}1\ \%$, $5{,}2\ \%$ pour $E_1$, $E_2$, $E_3$, et les suivants se partagent les $9{,}6\ \%$ restants. Toute l'énergie incidente revient finalement vers la sonde : la plaque ne dissipe rien, et la face arrière réfléchit la totalité de l'énergie transmise ; c'est la preuve que les coefficients utilisés (en pression) sont cohérents avec le bilan énergétique.


**q4.** On mesure $\Delta t=4{,}70~\mu$s entre deux échos successifs. Calculer $e$. L'impulsion de durée
$0{,}4~\mu$s permet-elle de séparer les échos ? Quelle est l'incertitude relative sur $e$ pour une résolution de $10$ ns ?
Quelle fréquence minimale pour séparer les échos d'une plaque de $2$ mm avec une impulsion de $2$ périodes ?

> [!success]- ✅ Correction
> $e=c_A\Delta t/2=12{,}0$ mm ; échos séparés ($0{,}4<4{,}7~\mu$s) ; $\Delta e/e\approx0{,}2\ \%$ ; $\Delta t=0{,}78~\mu$s pour $2$ mm, d'où $f>2{,}6$ MHz.


> [!example]- 📝 Solution détaillée
> **Épaisseur**
>
> Entre deux échos successifs, l'impulsion a fait un aller-retour de plus dans la plaque : $\Delta t=2e/c_A$, donc
> $$e=\frac{c_A\Delta t}{2}=\frac{5110\times4{,}70\times10^{-6}}{2}\approx1{,}20\times10^{-2}~\text{m}=12{,}0~\text{mm}.$$
>
> **Résolution temporelle et précision**
>
> La durée de l'impulsion ($0{,}4~\mu$s) est très inférieure à $\Delta t=4{,}7~\mu$s : les échos sont bien séparés. La précision relative est $\Delta e/e=\Delta(\Delta t)/\Delta t=10~\text{ns}/4{,}7~\mu\text{s}\approx0{,}2\ \%$ (soit $0{,}026$ mm). Pour une plaque de $2$ mm, $\Delta t=2\times2\times10^{-3}/5110=0{,}78~\mu$s : une impulsion de $2$ périodes dure $2/f$ et reste séparable si $2/f<0{,}78~\mu$s, soit $f>2{,}6$ MHz. Plus la plaque est mince, plus la fréquence doit être élevée, au prix d'une atténuation croissante.


**q5.** En réalité, on mesure $E_2/E_1=0{,}78$ au lieu de la valeur théorique. En déduire le facteur d'atténuation
sur un aller-retour, puis le coefficient d'atténuation $\alpha$ de l'aluminium à $5$ MHz (en Np/m et en dB/m).
Que peut-on déduire de $E_2/E_1$ si on ignore l'impédance de la plaque et si l'atténuation est négligeable ?

> [!tip]- 💡 Coup de pouce
> Si $\mathcal A$ est le facteur d'atténuation sur un aller-retour, $E_2/E_1=\mathcal A\,r_{Aw}r_{Ab}$. Pour la dernière question, inversez $|r|=(Z_A-Z_w)/(Z_A+Z_w)$.


> [!success]- ✅ Correction
> $\mathcal A=0{,}78/0{,}804=0{,}970$ ; $\alpha=-\ln\mathcal A/(2e)\approx1{,}3$ Np/m $\approx11$ dB/m ; sans atténuation, $Z_A/Z_w=(1+|r|)/(1-|r|)$.


> [!example]- 📝 Solution détaillée
> **Facteur d'atténuation**
>
> $\dfrac{E_2}{E_1}=\mathcal A\,r_{Aw}r_{Ab}=0{,}804\,\mathcal A=0{,}78\Rightarrow\mathcal A=0{,}970$. Sur un aller-retour de longueur $2e=24$ mm, $\mathcal A=e^{-2\alpha e}$ :
> $$\alpha=\frac{-\ln0{,}970}{2e}=\frac{0{,}0301}{0{,}024}\approx1{,}3~\text{Np}\cdot\text{m}^{-1}\approx11~\text{dB}\cdot\text{m}^{-1}.$$
>
> **Utilisation du rapport comme mesure d'impédance**
>
> Si l'atténuation est négligeable, $|E_2/E_1|=|r_{Aw}|=\dfrac{Z_A-Z_w}{Z_A+Z_w}$, soit $\dfrac{Z_A}{Z_w}=\dfrac{1+|E_2/E_1|}{1-|E_2/E_1|}$ : pour $0{,}804$, on retrouve $9{,}2$. La mesure du rapport de deux échos successifs fournit donc l'impédance de la plaque, ou son atténuation si l'impédance est connue. Les deux effets ne se séparent qu'en connaissant l'un des deux ; on peut aussi les séparer en comparant la décroissance de plusieurs échos ($E_3/E_2$, etc.), ou en mesurant à plusieurs épaisseurs.


**q6.** La plaque est maintenant collée sur un polymère d'impédance $Z_3=3{,}0\times10^6$ rayl. Calculer le nouveau coefficient
$r_{A3}$, l'amplitude de $E_1'$ et le rapport $E_2'/E_1'$. De combien de décibels l'écho $E_1$ varie-t-il
lorsque le collage disparaît (lame d'air) ? Comment détecte-t-on le défaut ?

> [!success]- ✅ Correction
> $r_{A3}=-0{,}643$ ; $E_1'=-0{,}227$ ; $E_2'/E_1'=0{,}517$ ; décollement : $E_1$ passe de $-0{,}227$ à $-0{,}354$ : $+3{,}8$ dB.


> [!example]- 📝 Solution détaillée
> **Face arrière collée**
>
> $r_{A3}=\dfrac{Z_3-Z_A}{Z_3+Z_A}=\dfrac{3{,}0-13{,}8}{3{,}0+13{,}8}=-0{,}643$, d'où
> $$E_1'=t_{wA}t_{Aw}\,r_{A3}=0{,}354\times(-0{,}643)=-0{,}227,\qquad\frac{E_2'}{E_1'}=r_{Aw}r_{A3}=(-0{,}804)(-0{,}643)=0{,}517.$$
> Une partie de l'énergie passe dans le polymère à chaque aller-retour : les échos décroissent plus vite ($0{,}517$ au lieu de $0{,}804$).
>
> **Détection d'un décollement**
>
> Si le polymère se décolle, une lame d'air s'interpose et la face arrière redevient quasi parfaitement réfléchissante : $E_1$ revient à $-0{,}354$, soit une augmentation de $20\log_{10}(0{,}354/0{,}227)=20\log_{10}(1{,}56)\approx+3{,}8$ dB et des échos suivants beaucoup plus durables. En balayant la sonde sur la plaque, une zone où $E_1$ (et $E_2$) sont plus forts signale un décollement ; une zone où ils sont plus faibles signale un collage plus absorbant (ou une corrosion de la face arrière). C'est le principe de la cartographie de collage par ultrasons (C-scan).


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex2-interface-entre-deux-milieux-notion-d-impedance-acoustique|Exercice 2 — Interface entre deux milieux, notion d'impédance acoustique]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex4-incidence-oblique-lois-de-snell-descartes-angle-critique-reflexion-totale-et-onde-evanescente|Exercice 4 — Incidence oblique : lois de Snell-Descartes, angle critique, réflexion totale et onde évanescente]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex5-sismique-refraction-ondes-coniques-et-epaisseur-d-une-couche|Exercice 5 — Sismique réfraction : ondes coniques et épaisseur d'une couche]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex3-perle-sur-une-corde-jonction-massive-filtre-passe-bas-puis-passe-bande|Exercice 3 — Perle sur une corde : jonction massive, filtre passe-bas puis passe-bande]]

