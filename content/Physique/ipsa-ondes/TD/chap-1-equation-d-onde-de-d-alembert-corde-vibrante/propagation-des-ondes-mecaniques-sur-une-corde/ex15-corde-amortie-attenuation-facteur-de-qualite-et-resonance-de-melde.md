---
title: "Exercice 15 — Corde amortie : atténuation, facteur de qualité et résonance de Melde"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a> · <a href="/pdfs/td1_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_PhV212_fiche)</a> · <a href="/pdfs/td1_ex1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_ex1_fiche)</a> · <a href="/pdfs/td1_exs_maison_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_exs_maison_fiche)</a>

### Exercice 15. Corde amortie : atténuation, facteur de qualité et résonance de Melde *(facultatif)*

Une corde de masse linéique $\mu$, tendue avec la force $F$ ($c=\sqrt{F/\mu}$), vibre dans un fluide visqueux (air, eau). Le fluide exerce
sur chaque élément de corde une force de frottement fluide **linéique** $-\lambda\,\partial_ty$ (opposée à la vitesse transversale),
avec $\lambda>0$ en N$\cdot$s$\cdot$m$^{-2}$. On note $\gamma=\lambda/\mu$ (en s$^{-1}$). Pour de petits mouvements, l'équation du mouvement est
$$\frac{\partial^2y}{\partial t^2}+\gamma\,\frac{\partial y}{\partial t}=c^2\,\frac{\partial^2y}{\partial x^2}.$$
On étudie d'abord la propagation, puis les modes propres d'une corde de longueur $\ell$ fixée en $x=0$ et $x=\ell$, enfin le montage de
Melde (exercice 5) avec amortissement.

**q1.** **Propagation.**


(a) Chercher une solution $\underline y=\underline a\,\mathrm e^{j(\omega t-\underline kx)}$ et établir $\underline k^2=\dfrac{\omega^2-j\gamma\omega}{c^2}$.

(b) Pour $\gamma\ll\omega$, montrer que $\underline k\simeq\dfrac\omega c-j\dfrac\gamma{2c}$. En déduire la forme réelle de l'onde, la longueur d'atténuation $\delta$ (amplitude divisée par $\mathrm e$) et la célérité de phase. Commenter l'indépendance en $\omega$.

(c) Dans la limite opposée ($\omega\ll\gamma$), quelle équation aux dérivées partielles retrouve-t-on ? Quel est le comportement de $\underline k$ ?

> [!tip]- 💡 Coup de pouce
> **Dispersion**
>
> Remplacez $\partial_t\to j\omega$ et $\partial_x\to-j\underline k$ ; isolez $\underline k^2$.
>
> **Limite $\omega\ll\gamma$**
>
> Négligez $\partial_t^2y$ devant $\gamma\partial_ty$ : quelle équation obtient-on ?


> [!success]- ✅ Correction
> **Résultat**
>
> $\underline k=\dfrac\omega c\sqrt{1-j\gamma/\omega}\simeq\dfrac\omega c-j\dfrac\gamma{2c}$ ; $y=a\,\mathrm e^{-\gamma x/(2c)}\cos(\omega t-\omega x/c)$ ; $\delta=\dfrac{2c}\gamma$, **indépendante de $\omega$** ; limite $\omega\ll\gamma$ : équation de diffusion $\partial_ty=\dfrac{c^2}\gamma\partial_x^2y$, $\underline k\simeq\sqrt{\dfrac{\gamma\omega}{2c^2}}(1-j)$.


> [!example]- 📝 Solution détaillée
> **(a) Relation de dispersion**
>
> En remplaçant : $-\omega^2+j\gamma\omega=-c^2\underline k^2$, soit $\underline k^2=\dfrac{\omega^2-j\gamma\omega}{c^2}=\dfrac{\omega^2}{c^2}\left(1-\dfrac{j\gamma}\omega\right)$.
>
> **(b) Amortissement faible**
>
> Pour $\gamma\ll\omega$ : $\underline k=\dfrac\omega c\sqrt{1-j\gamma/\omega}\simeq\dfrac\omega c\left(1-\dfrac{j\gamma}{2\omega}\right)=\dfrac\omega c-j\dfrac\gamma{2c}$, soit $k'=\dfrac\omega c$ et $k''=\dfrac\gamma{2c}$. L'onde réelle est
> $$y(x,t)=a\,\mathrm e^{-\gamma x/(2c)}\cos\!\left(\omega t-\frac\omega cx\right).$$
> La célérité de phase reste $c$ et l'amplitude est divisée par $\mathrm e$ sur $\delta=\dfrac1{k''}=\boxed{\dfrac{2c}\gamma}$, **indépendante de $\omega$** : toutes les fréquences sont atténuées de la même façon (propagation quasi sans distorsion). C'est une spécificité du frottement visqueux ; pour des pertes internes, $\gamma$ dépend de $\omega$ et un signal se déforme.
>
> **(c) Amortissement fort**
>
> Pour $\omega\ll\gamma$, $\partial_t^2y$ est négligeable devant $\gamma\partial_ty$ : $\partial_ty=\dfrac{c^2}\gamma\partial_x^2y$ : une **équation de diffusion** (comme la chaleur), de coefficient $D=c^2/\gamma$. Alors $\underline k^2\simeq-j\gamma\omega/c^2$, $\underline k=\sqrt{\dfrac{\gamma\omega}{2c^2}}(1-j)$ : $k'=k''$, la propagation n'est plus ondulatoire (atténuation sur une longueur d'onde divisée par $\mathrm e^{2\pi}$) ; la profondeur de pénétration est $\delta=\sqrt{2c^2/(\gamma\omega)}$ qui dépend de $\omega$.


**q2.** **Modes propres de la corde de longueur $\ell$, fixée aux deux extrémités.**


(a) On cherche des solutions $y=\sin(k_nx)\,\Theta_n(t)$. Établir $\ddot\Theta_n+\gamma\dot\Theta_n+\omega_n^2\Theta_n=0$ avec $\omega_n=n\pi c/\ell$. Résoudre pour $\gamma<2\omega_n$ et montrer que tous les modes sont amortis par le même facteur $\mathrm e^{-\gamma t/2}$.

(b) Déterminer la pseudo-pulsation $\omega_n'$ et le facteur de qualité $Q_n=\omega_n/\gamma$. Comment $Q_n$ dépend-il de $n$ ? Interpréter : pour quel $n$ le mode devient-il surcritique ?

(c) Application : corde de $\ell=0{,}65$ m, $c=143$ m/s, $\gamma=2{,}0$ s$^{-1}$ (cf. ex. 12). Calculer $f_1$, $Q_1$, la durée $\tau$ au bout de laquelle l'amplitude est divisée par $\mathrm e$ et le nombre d'oscillations correspondant.

> [!tip]- 💡 Coup de pouce
> **Séparation**
>
> $\sin(k_nx)\,[\ddot\Theta+\gamma\dot\Theta]=-c^2k_n^2\sin(k_nx)\,\Theta$ (en notant $\omega_n=ck_n$).
>
> **Équation caractéristique**
>
> $\Theta=\mathrm e^{st}$ : $s^2+\gamma s+\omega_n^2=0$.


> [!success]- ✅ Correction
> **Résultats**
>
> $\Theta_n=\mathrm e^{-\gamma t/2}\big(A\cos\omega_n't+B\sin\omega_n't\big)$, $\omega_n'=\sqrt{\omega_n^2-\gamma^2/4}$ ; $Q_n=\dfrac{\omega_n}\gamma\propto n$ ; AN : $f_1=110$ Hz, $Q_1\approx346$, $\tau=2/\gamma=1{,}0$ s, soit $\approx110$ oscillations.


> [!example]- 📝 Solution détaillée
> **(d) Équation différentielle temporelle**
>
> En reportant $y=\sin(k_nx)\Theta_n(t)$ dans l'équation (avec $k_n=n\pi/\ell$ imposé par les conditions aux limites) : $\sin(k_nx)(\ddot\Theta_n+\gamma\dot\Theta_n)=-c^2k_n^2\sin(k_nx)\Theta_n$, soit $\ddot\Theta_n+\gamma\dot\Theta_n+\omega_n^2\Theta_n=0$ avec $\omega_n=ck_n=\dfrac{n\pi c}\ell$. L'équation caractéristique $s^2+\gamma s+\omega_n^2=0$ donne $s=-\dfrac\gamma2\pm j\sqrt{\omega_n^2-\gamma^2/4}$ ; pour $\gamma<2\omega_n$,
> $$\Theta_n(t)=\mathrm e^{-\gamma t/2}\left[A_n\cos\omega_n't+B_n\sin\omega_n't\right].$$
> Le facteur $\mathrm e^{-\gamma t/2}$ est **le même pour tous les modes** (frottement visqueux uniforme) : la forme du profil ne se déforme pas, seule son amplitude décroît.
>
> **(e) Pseudo-pulsation et facteur de qualité**
>
> $\omega_n'=\sqrt{\omega_n^2-\gamma^2/4}\simeq\omega_n\left(1-\dfrac{\gamma^2}{8\omega_n^2}\right)$ et $Q_n=\dfrac{\omega_n}\gamma=\dfrac{n\pi c}{\ell\gamma}\propto n$ : les modes d'ordre élevé sont **moins** amortis, en proportion de leur fréquence. Le mode $n$ n'oscille plus quand $\gamma\ge2\omega_n$ (régime apériodique) : seuls les modes avec $n<\dfrac{\gamma\ell}{2\pi c}$ sont surcritiques, nombre très inférieur à $1$ pour une vraie corde ; en revanche, pour une corde dans le miel, tous les modes bas sont apériodiques.
>
> **(f) Application numérique**
>
> $f_1=\dfrac c{2\ell}=\dfrac{143}{1{,}30}=110$ Hz, $\omega_1=691$ rad/s. $Q_1=\dfrac{691}{2{,}0}\approx346$. L'amplitude est divisée par $\mathrm e$ après $\tau=\dfrac2\gamma=1{,}0$ s, soit $f_1\tau\approx110$ oscillations ($\approx Q_1/\pi$ $\surd$). Ordre de grandeur réaliste pour une corde de guitare dans l'air (sustain de quelques secondes) ; le frottement visqueux de l'air n'est qu'une partie de la dissipation, dominée en pratique par les pertes internes de la corde et par le rayonnement dans la caisse.


**q3.** **Melde amorti.** Le vibreur impose $y(0,t)=a\,\mathrm e^{j\omega t}$ ; la corde est fixée en $x=\ell$.


(a) Montrer que $\underline y(x,t)=a\,\dfrac{\sin\!\big(\underline k(\ell-x)\big)}{\sin(\underline k\ell)}\,\mathrm e^{j\omega t}$ avec $\underline k$ de la question (a).

(b) À la fréquence $\omega=\omega_N$ ($k'\ell=N\pi$), montrer que l'amplitude des ventres vaut $A_v\simeq\dfrac{2ca}{\gamma\ell}=\dfrac{2Q_N}{N\pi}\,a$ pour $\gamma\ll\omega_N$. Interpréter.

(c) Un expérimentateur mesure, à la résonance fondamentale ($c=50$ m/s, $\ell=0{,}50$ m), un rapport $A_v/a=40$. Déterminer $\gamma$, $Q_1$, la largeur de la résonance $\Delta f$ et la durée d'extinction libre $\tau$ après arrêt du vibreur.

> [!tip]- 💡 Coup de pouce
> **Transposer ex. 5**
>
> L'équation de Helmholtz $\underline Y''+\underline k^2\underline Y=0$ avec $\underline Y(0)=a$ et $\underline Y(\ell)=0$ a la même solution que pour la corde idéale, avec $k\to\underline k$.
>
> **Sinus complexe**
>
> $\sin(N\pi-jb)=-(-1)^N\,j\sinh b$ avec $b=k''\ell$.


> [!question]- 🔭 Aller plus loin — Licence : Condition d'Heaviside : ligne sans distorsion
> Ajoutons à l'équation un terme de rappel élastique $\omega_0^2y$ (corde sur un lit de ressorts). Montrer que $\underline k^2=(\omega^2-j\gamma\omega-\omega_0^2)/c^2$ et que l'onde se propage **sans distorsion** (célérité de phase $c$ indépendante de $\omega$, atténuation $\mathrm e^{-\gamma x/(2c)}$) si et seulement si $\omega_0=\gamma/2$. Faire le lien avec la condition d'Heaviside $R/L=G/C$ pour les lignes télégraphiques.


> [!question]- 🔭 Aller plus loin — Master : Théorème fluctuation-dissipation (corde thermique)
> À température $T$, chaque mode d'une corde a une énergie moyenne $k_BT$ (équipartition). Estimer l'amplitude quadratique moyenne du fondamental d'une corde de guitare à $300$ K ($k_BT=4{,}1\times10^{-21}$ J, $\mu=5$ g/m, $\ell=0{,}65$ m) et comparer à un atome. Discuter le rôle de $\gamma$ dans la fonction de corrélation $\langle y(t)y(0)\rangle\propto\mathrm e^{-\gamma t/2}\cos\omega_1t$.


> [!success]- ✅ Correction
> **Résultats**
>
> $|\sin\underline k\ell|=\sinh(k''\ell)\simeq k''\ell=\dfrac{\gamma\ell}{2c}$ à la résonance : $A_v\simeq\dfrac a{k''\ell}=\dfrac{2ca}{\gamma\ell}$. AN : $\gamma=\dfrac{2c}{40\,\ell}=5{,}0$ s$^{-1}$, $Q_1=\dfrac{2\pi\times50}5\approx63$, $\Delta f=\dfrac\gamma{2\pi}\approx0{,}8$ Hz, $\tau=\dfrac2\gamma=0{,}4$ s.


> [!example]- 📝 Solution détaillée
> **(g) Profil complexe**
>
> En régime forcé, $\underline y=\underline Y(x)\mathrm e^{j\omega t}$ avec $\underline Y''+\underline k^2\underline Y=0$, $\underline Y(0)=a$, $\underline Y(\ell)=0$. La résolution de l'exercice 5 (avec $k$ remplacé par $\underline k$) donne $\underline Y(x)=a\,\dfrac{\sin\underline k(\ell-x)}{\sin\underline k\ell}$.
>
> **(h) Résonance**
>
> Posons $\underline k=k'-jk''$ avec $k''=\gamma/(2c)\ll k'$. À $k'\ell=N\pi$ : $\sin\underline k\ell=\sin(N\pi-jk''\ell)=-(-1)^Nj\sinh(k''\ell)$, de module $\sinh(k''\ell)\simeq k''\ell=\dfrac{\gamma\ell}{2c}$. Au ventre, $|\sin\underline k(\ell-x)|^2=\sin^2k'u+\sinh^2k''u\simeq1$ ($u=\ell-x$). D'où
> $$\boxed{A_v\simeq\frac{a}{k''\ell}=\frac{2ca}{\gamma\ell}=\frac{2Q_N}{N\pi}\,a},\qquad Q_N=\frac{N\pi c}{\ell\gamma}.$$
> L'amplitude ne diverge plus : elle est finie, de l'ordre de $Q\,a$ ; elle est d'autant plus grande que l'amortissement est faible. Pour $\gamma\to0$, on retrouve $A_v\to\infty$ (exercice 5).
>
> **(i) Application numérique**
>
> $A_v/a=\dfrac{2c}{\gamma\ell}=40\Rightarrow\gamma=\dfrac{2\times50}{40\times0{,}5}=5{,}0$ s$^{-1}$. $\omega_1=\dfrac{\pi c}\ell=314$ rad/s, donc $Q_1=\dfrac{314}5\approx63$ (cohérent avec $A_v/a=2Q_1/\pi=40$ $\surd$). La résonance a une largeur à mi-puissance $\Delta\omega=\gamma$, soit $\Delta f=\dfrac\gamma{2\pi}\approx0{,}8$ Hz pour une fréquence centrale de $50$ Hz : il faut régler le vibreur à mieux que $0{,}4$ Hz pour observer le maximum. Après arrêt du vibreur, l'amplitude décroît en $\mathrm e^{-\gamma t/2}$ : $\tau=\dfrac2\gamma=0{,}4$ s, soit $\sim20$ oscillations. **Validation** : on retrouve l'ordre de grandeur du « phénomène » visible à l'œil sur le montage de Melde (fuseaux nets, dérive lente si la fréquence est décalée).


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex14-corde-de-piano-raide-dispersion-et-inharmonicite|Exercice 14 — Corde de piano raide : dispersion et inharmonicité]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex6-experience-de-melde-oscillations-forcees-d-une-corde-resonance|Exercice 6 — Expérience de Melde, oscillations forcées d'une corde, résonance]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex3-mesurer-la-vitesse-de-la-lumiere-avec-un-four-a-micro-ondes-et-du-chocolat|Exercice 3 — Mesurer la vitesse de la lumière avec un four à micro-ondes et du chocolat]]

