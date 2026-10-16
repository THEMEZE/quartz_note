---
title: "Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a> · <a href="/pdfs/td1_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_PhV212_fiche)</a> · <a href="/pdfs/td1_ex1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_ex1_fiche)</a> · <a href="/pdfs/td1_exs_maison_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_exs_maison_fiche)</a>

### Exercice 5. Corde fixée à ses deux extrémités et ondes stationnaires

Une corde homogène, de masse linéique $\mu$ et de longueur $L$, est fixée en ses deux extrémités $A(x=0)$ et $B(x=L)$. La corde de tension $F$, écartée de sa position d'équilibre, est abandonnée à l'instant $t=0$. Le déplacement transversal $y(x,t)$ obéit à l'équation de d'Alembert :
$$\frac{\partial^2 y}{\partial x^2} = \frac{\mu}{F} \frac{\partial^2 y}{\partial t^2}$$

<p style="text-align:center"><a href="/figures/td1_ex4_phv212_corde_fixe.svg" target="_blank" rel="noopener"><img src="/figures/td1_ex4_phv212_corde_fixe.svg" alt="" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>

**q1.** On admet la solution particulière $y(x,t) = f(x)\cdot g(t)$ (séparation des variables).
Montrer que $y(x,t) = A\cos(kx+\varphi)\cos(\omega t+\phi)$.
Quelle relation existe-t-il entre $k$, $\omega$ et la célérité $c$ ? (Relation de dispersion).

> [!tip]- 💡 Coup de pouce
> **Méthode simple**
>
> Injectez $y(x,t) = A\cos(kx+\varphi)\cos(\omega t+\phi)$ dans l'équation de d'Alembert, séparez les termes en $x$ et en $t$. Et on aura une relation entre $\omega$ , $k$ et $c$
>
> **Méthode de séparation**
>
> Injectez $y(x,t) = f(x)g(t)$ dans l'équation d'onde, séparez les termes en $x$ et en $t$ pour égaler chaque membre à une constante négative $-k^2$.


> [!question]- 🔭 Aller plus loin — Master : Séparation des variables pour l'équation de d'Alembert unidimensionnelle
> **1. Position du problème et cadre fonctionnel** \\
>
> On considère l'équation des ondes (d'Alembert) 1D sur un domaine spatial borné $\Omega = ]0, L[$ :\\
>
> $$\frac{\partial^2 y}{\partial x^2}(x,t) - \frac{1}{c^2} \frac{\partial^2 y}{\partial t^2}(x,t) = 0, \quad \forall (x,t) \in ]0, L[ \times \mathbb{R}^+_*$$
> avec $c = \sqrt{\frac{F}{\mu}} > 0$. Le champ scalaire $y \in C^2(\bar{\Omega} \times \mathbb{R}^+)$ est assujetti aux conditions aux limites de Dirichlet homogènes :
> $$y(0,t) = y(L,t) = 0, \quad \forall t \ge 0$$\\
>
> **2. Postulat de séparation des variables**\\
> La méthode de Fourier repose sur la recherche de solutions particulières non triviales à variables séparées sous forme de produit tensoriel d'espaces fonctionnels :
> $$y(x,t) = f(x) \cdot g(t) \quad \text{avec } f \in C^2([0, L], \mathbb{R}), \, g \in C^2(\mathbb{R}^+, \mathbb{R})$$
>
> **Motivation mathématique :** \\
>
>
>
> - **Réduction dimensionnelle :** Conversion d'un opérateur différentiel aux dérivées partielles d'ordre 2 en deux opérateurs différentiels ordinaires linéaires (EDO) univariés.
> - **Base de l'espace de Hilbert :** L'opérateur spatial $-\frac{\mathrm{d}^2}{\mathrm{d}x^2}$ muni des conditions de Dirichlet est auto-adjoint sur $L^2(0,L)$. Le théorème spectral garantit que ses fonctions propres $\{f_n\}_{n \ge 1}$ forment une base hilbertienne orthogonale.
> - **Interprétation physique :** Recherche des modes propres (ou régimes stationnaires) où le profil spatial $f(x)$ subit une modulation temporelle globale $g(t)$.
>
>
>
> **3. Principe de superposition et completude**\\
>
> En raison de la linéarité de l'opérateur de d'Alembert $\Box = \frac{\partial^2}{\partial x^2} - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}$, toute combinaison linéaire de solutions à variables séparées est encore solution. La solution générale s'exprime par le développement en série de Fourier :
> $$y(x,t) = \sum_{n=1}^{+\infty} f_n(x) \cdot g_n(t)$$
> La convergence de la série dépend de la régularité des données initiales $y(x,0)$ et $\frac{\partial y}{\partial t}(x,0)$.


> [!question]- 🔭 Aller plus loin — Master : Résolution par Transformée de Fourier spatiale et spectre continu
> **1. Transformation intégrale sur le domaine infini $\mathbb{R}$ **\\
>
> Pour une corde infinie $x \in \mathbb{R}$, on applique la Transformée de Fourier partielle en espace définie sur $\mathcal{S}(\mathbb{R})$ (espace de Schwartz) :
> $$\hat{y}(k,t) = \mathcal{F}_x [y(x,t)] = \int_{-\infty}^{+\infty} y(x,t) \, e^{-i k x} \, \mathrm{d}x$$
>
> **2. Réduction de l'EDP dans l'espace des fréquences spatiales **\\
> En utilisant la propriété d'échange dérivation/multiplication $\mathcal{F}_x\left[\frac{\partial^2 y}{\partial x^2}\right] = (ik)^2 \hat{y}(k,t) = -k^2 \hat{y}(k,t)$, l'équation de d'Alembert devient :
> $$-k^2 \hat{y}(k,t) - \frac{1}{c^2} \frac{\partial^2 \hat{y}}{\partial t^2}(k,t) = 0 \iff \frac{\partial^2 \hat{y}}{\partial t^2}(k,t) + (ck)^2 \hat{y}(k,t) = 0$$
>
> Pour chaque mode $k \in \mathbb{R}$, la solution d'EDO temporelle paramétrée par $k$ est :
> $$\hat{y}(k,t) = A(k) \, e^{-i c k t} + B(k) \, e^{i c k t}$$
>
> **3. Reconstruction par TF inverse et formule de d'Alembert **\\
> En appliquant la transformée de Fourier inverse :
> $$y(x,t) = \mathcal{F}_x^{-1}[\hat{y}(k,t)] = \frac{1}{2\pi} \int_{-\infty}^{+\infty} \hat{y}(k,t) \, e^{i k x} \, \mathrm{d}k$$
> $$y(x,t) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} A(k) e^{i k (x - c t)} \, \mathrm{d}k + \frac{1}{2\pi} \int_{-\infty}^{+\infty} B(k) e^{i k (x + c t)} \, \mathrm{d}k$$
>
> En posant $F(\xi) = \mathcal{F}^{-1}[A(k)](\xi)$ et $G(\xi) = \mathcal{F}^{-1}[B(k)](\xi)$, on retrouve la solution générale d'ondes progressives :
> $$y(x,t) = F(x - ct) + G(x + ct)$$
>
> **4. Dualité Séparation des Variables vs Transformée de Fourier **\\
>
> %| Propriété / Méthode | Séparation des variables (Fourier discret) | Transformée de Fourier (Continu) |
> %| :--- | :--- | :--- |
> %| **Géométrie de l'espace** | Domaine borné $\Omega = ]0, L[$ (Conditions aux limites) | Domaine infini $\Omega = \mathbb{R}$ (Conditions aux limites à l'infini) |
> %| **Spectre fréquentiel** | Discret ($k_n = \frac{n\pi}{L}, n \in \mathbb{N}^*$) | Continu ($k \in \mathbb{R}$) |
> %| **Représentation de la solution** | Série de Fourier : $\sum_{n} f_n(x) g_n(t)$ | Intégrale de Fourier : $\int_{\mathbb{R}} \hat{y}(k,t) e^{i k x} \mathrm{d}k$ |
> %| **Nature physique** | Superposition d'ondes stationnaires | Superposition d'ondes planes progressives |
>
> $$
> \begin{array}{ccc}
> \textbf{Propriété / Méthode} & \textbf{Séparation des variables (Fourier discret} & \textbf{Transformée de Fourier (Continu)} \\
> \hline 
> \textbf{Géométrie de l'espace} & \text{Domaine borné $\Omega = ]0, L[$ (Conditions aux limites)} & \text{Domaine infini $\Omega = \mathbb{R}$ (Conditions aux limites à l'infini)} \\
> \textbf{Spectre fréquentie} & \text{Discret ($k_n = \frac{n\pi}{L}, n \in \mathbb{N}^*$)} & \text{Continu ($k \in \mathbb{R}$))} \\
> \textbf{Représentation de la solution} & \text{Série de Fourier : $\sum_{n} f_n(x) g_n(t)$} & \text{Intégrale de Fourier : $\int_{\mathbb{R}} \hat{y}(k,t) e^{i k x} \mathrm{d}k$} \\
> \textbf{Nature physique} & \text{Superposition d'ondes stationnaires} & \text{Superposition d'ondes planes progressives} 
> \end{array}
> $$


> [!question]- 🔭 Aller plus loin — Licence : Pour aller plus loin : interprétation géométrique et représentations complexes
> **1. Interprétation vectorielle dans le plan réel (Produit scalaire)**
>
> La combinaison linéaire $C\cos(a) + B\sin(a)$ s'interprète directement comme le produit scalaire euclidien de deux vecteurs du plan $\mathbb{R}^2$ :
>
>
> - Un vecteur de commande dépendant des amplitudes : $\vec{V} = \begin{pmatrix} C \\ B \end{pmatrix}$
> - Un vecteur unitaire variant avec la phase : $\vec{u}(a) = \begin{pmatrix} \cos(a) \\ \sin(a) \end{pmatrix}$
>
>
>
> En exprimant le produit scalaire via les normes et l'angle interpolé :
> $$C\cos(a) + B\sin(a) = \vec{V} \cdot \vec{u}(a) = \|\vec{V}\| \, \|\vec{u}(a)\| \cos\big(\widehat{(\vec{V}, \vec{u}(a))}\big)$$
>
>
>
> - La norme vaut $\|\vec{V}\| = \sqrt{C^2 + B^2} = R$.
> - L'argument polarisé de $\vec{V}$ est $\theta = \operatorname{atan2}(B, C)$, d'où l'angle orienté $\widehat{(\vec{V}, \vec{u}(a))} = a - \theta$.
> - On retrouve géométriquement : $R\cos(a - \theta)$.
>
>
>
> **2. Formalisme des nombres complexes et phaseurs**
>
> En physique mathématique et en traitement du signal, cette contraction s'effectue via le passage dans l'espace des phaseurs sur $\mathbb{C}$.
>
> Considérons la partie réelle du produit d'un nombre complexe par $e^{i a}$ :
> $$Z = C - i B = R e^{-i \theta} \quad \text{avec } R = \sqrt{C^2 + B^2} \text{ et } \theta = \operatorname{atan2}(B, C)$$
>
> L'expression initiale s'écrit alors :
> $$C\cos(a) + B\sin(a) = \operatorname{Re}\left( (C - i B) e^{i a} \right) = \operatorname{Re}\left( R e^{-i \theta} e^{i a} \right) = \operatorname{Re}\left( R e^{i(a - \theta)} \right) = R\cos(a - \theta)$$
>
> **3. Application au calcul des conditions initiales de l'onde**
>
> Dans le cadre de la corde vibrante, la solution temporelle s'écrit sous forme séparée :
> $$g(t) = C \cos(\omega t) + B \sin(\omega t) = R \cos(\omega t - \theta)$$
>
> L'introduction de l'amplitude globale $R$ et du déphasage temporel $\theta$ permet une identification directe de l'état initial du système à $t=0$ :
> $$\begin{cases}
> g(0) = R \cos(\theta) = C & \text{(position initiale)} \\[4pt]
> g'(0) = \omega R \sin(\theta) = \omega B & \text{(vitesse initiale)}
> \end{cases}$$
>
> L'énergie mécanique totale du mode $n$ est alors directement proportionnelle au carré de l'amplitude contractée $R_n^2 = C_n^2 + B_n^2$.


> [!success]- ✅ Correction
> **Directe**
>
> Si on on injecte $y(x,t) = A\cos(kx+\varphi)\cos(\omega t+\phi)$ dans $\frac{\partial^2 y}{\partial x^2} - \frac{\mu}{F} \frac{\partial^2 y}{\partial t^2} = 0$ , on obtient directement $\omega = k c$.
>
> **Résultat**
>
> On obtient $f''(x) + k^2 f(x) = 0$ et $g''(t) + \omega^2 g(t) = 0$.
> La relation de dispersion est $\omega = c\cdot k$ avec $c = \sqrt{F/\mu}$.


> [!example]- 📝 Solution détaillée
> **Injection**
>
> $y'(x,t) = - A k \sin(kx+\varphi)\cos(\omega t+\phi)$ et $y''(x,t) = - A k^2 \cos(kx+\varphi)\cos(\omega t+\phi)$ et //
> $\dot{y}(x,t) = - A \omega \cos(kx+\varphi)\sin(\omega t+\phi)$ et $\ddot{y}(x,t) = - A \omega^2 \cos(kx+\varphi)\cos(\omega t+\phi)$. Donc avec $\frac{\partial^2 y}{\partial x^2} - \frac{\mu}{F} \frac{\partial^2 y}{\partial t^2} = 0$ \\
>
> $$
> \omega^2 = k^2 c^2.
> $$
>
> **Démonstration complète**
>
> En injectant $y(x,t) = f(x)g(t)$ dans l'équation d'onde :
> $$f''(x)g(t) = \frac{1}{c^2}f(x)g''(t) \implies \frac{f''(x)}{f(x)} = \frac{1}{c^2}\frac{g''(t)}{g(t)} = -k^2$$
> On obtient deux équations différentielles harmoniques :
>
>
> - [1.] $f''(x) + k^2 f(x) = 0 \implies f(x) = C_1\cos(kx+\varphi)$
> - [2.] $g''(t) + \omega^2 g(t) = 0 \implies g(t) = C_2\cos(\omega t+\phi)$
>
>
>
> Par produit, $y(x,t) = A\cos(kx+\varphi)\cos(\omega t+\phi)$ avec $A = C_1 C_2$.
> La constante de séparation impose la relation de dispersion : $\omega = c\cdot k$, soit $k = \dfrac{\omega}{c}$ avec $c = \sqrt{\dfrac{F}{\mu}}$.


**q2.** Montrer que les fréquences de vibration sont des multiples entiers d'une fréquence fondamentale $f_1$ ($f_N = N f_1$). Exprimer $f_1$ en fonction de $F$, $L$ et $\mu$.

> [!tip]- 💡 Coup de pouce
> **Conditions aux limites**
>
> Appliquez les conditions aux limites $y(0,t) = 0$ et $y(L,t) = 0$ pour déterminer $k$ puis $f_N$.


> [!success]- ✅ Correction
> **Résultat**
>
> $f_N = N f_1$ avec $f_1 = \dfrac{1}{2L}\sqrt{\dfrac{F}{\mu}}$.


> [!example]- 📝 Solution détaillée
> **Calcul détaillé**
>
> - En $x=0$ : $y(0,t) = 0 \implies \cos(\varphi) = 0 \implies \varphi = \dfrac{\pi}{2} [\pi]$, donc $f(x) \propto \sin(kx)$.
> - En $x=L$ : $y(L,t) = 0 \implies \sin(kL) = 0 \implies kL = N\pi \quad (N \in \mathbb{N}^*)$.
>
> Comme $k = \dfrac{2\pi f}{c}$, on a $\dfrac{2\pi f_N}{c} L = N\pi \implies f_N = N \dfrac{c}{2L}$.
> Le fondamental ($N=1$) s'écrit $f_1 = \dfrac{c}{2L} = \dfrac{1}{2L}\sqrt{\dfrac{F}{\mu}}$, d'où $f_N = N f_1$.


**q3.** Application : Pour la 3ème corde de guitare ($\ell = 63$ cm, $\rho = 1200\text{ kg}\cdot\text{m}^{-3}$, $S = 0.42\text{ mm}^2$), calculer la tension $F$ pour $f_1 = 147$ Hz.

> [!tip]- 💡 Coup de pouce
> **Masse linéique**
>
> Calculez d'abord $\mu = \rho\cdot S$, puis isolez $F$ dans la formule de $f_1$.


> [!success]- ✅ Correction
> **Résultat**
>
> $\mu = 5.04\times 10^{-4}\text{ kg/m}$, $F \approx 17.3\text{ N}$.


> [!example]- 📝 Solution détaillée
> **Application numérique**
>
> $\mu = \rho S = 1200 \times (0.42\times 10^{-6}) = 5.04\times 10^{-4}\text{ kg/m}$.
> De $f_1 = \dfrac{1}{2\ell}\sqrt{\dfrac{F}{\mu}}$, on tire $F = \mu (2\ell f_1)^2$.
> $$F = 5.04\times 10^{-4} \times (2 \times 0.63 \times 147)^2 \approx 17.3\text{ N}$$


**q4.** Exprimer, en fonction de la longueur $L$, les longueurs d'ondes possibles $\lambda_N$.

> [!tip]- 💡 Coup de pouce
> **Relation $k_N$ et $\lambda_N$
> **
>
> Utilisez $k_N = \dfrac{2\pi}{\lambda_N} = \dfrac{N\pi}{L}$.


> [!success]- ✅ Correction
> **Résultat**
>
> $\lambda_N = \dfrac{2L}{N}$ pour $N \ge 1$.


> [!example]- 📝 Solution détaillée
> **Détail**
>
> Comme $k_N L = N\pi$ et $k_N = \dfrac{2\pi}{\lambda_N}$, on obtient immédiatement :
> $$\lambda_N = \frac{2L}{N}$$


**q5.** Exprimer $y_N(x,t)$ pour le mode $N$. Préciser le nombre et la position des nœuds et des ventres. Distance entre 2 ventres / 2 nœuds ?

> [!tip]- 💡 Coup de pouce
> **Positions récurrencielles**
>
> Les nœuds annulent le sinus ($\sin(k_N x) = 0$), les ventres le maximisent ($|\sin(k_N x)| = 1$).


> [!success]- ✅ Correction
> **Résultat**
>
> $y_N(x,t) = A_N \sin\left(\dfrac{N\pi}{L}x\right)\cos(\omega_N t + \phi_N)$.
> $N+1$ nœuds en $x_n = n\dfrac{L}{N}$ ($n \in \llbracket 0, N \rrbracket $).
> $N$ ventres en $x_v = \left(n+\dfrac{1}{2}\right)\dfrac{L}{N}$ ($n \in \llbracket 0, N-1 \rrbracket $).
> Distance entre deux nœuds ou deux ventres consécutifs : $\dfrac{\lambda_N}{2} = \dfrac{L}{N}$.


> [!example]- 📝 Solution détaillée
> **Analyse structurée**
>
> - **Forme du mode $N$ :** $y_N(x,t) = A_N \sin\left(\dfrac{N\pi x}{L}\right)\cos(\omega_N t + \phi_N)$.
> - **Nœuds ($y_N = 0$) :** $\dfrac{N\pi x}{L} = n\pi \implies x_n = n\dfrac{L}{N}$ avec $n \in \{0, 1, \dots, N\}$. Il y a $N+1$ nœuds.
> - **Ventres ($|y_N| = A_N$) :** $\dfrac{N\pi x}{L} = \left(n+\dfrac{1}{2}\right)\pi \implies x_v = \left(n+\dfrac{1}{2}\right)\dfrac{L}{N}$ avec $n \in \{0, \dots, N-1\}$. Il y a $N$ ventres.
> - **Distance inter-nœuds / inter-ventres :** $d = \dfrac{L}{N} = \dfrac{\lambda_N}{2}$.


**q6.** Dessiner la corde pour $N=1$ et $N=4$.

> [!tip]- 💡 Coup de pouce
> **Représentation**
>
> $N=1$ présente 1 fuseau (0 nœud interne), $N=4$ présente 4 fuseaux (3 nœuds internes).


> [!question]- 🔭 Aller plus loin — Licence : Analyse spectrale et séries de Fourier
> Une déformation initiale quelconque $y(x,0)$ se décompose comme une somme infinie de modes propres $\sum y_N(x,t)$ via la décomposition en séries de Fourier.


> [!success]- ✅ Correction
> **Allure**
>
> - **$N=1$** : Une demi-onde entre $0$ et $L$ (1 ventre au centre $x=L/2$).
> - **$N=4$** : Deux ondes complètes entre $0$ et $L$ (4 ventres, nœuds en $0, L/4, L/2, 3L/4, L$).


> [!example]- 📝 Solution détaillée
> **Tracé schématique**
>
> - $N=1$ (Fondamental) : \texttt{A (---) B} (1 seul fuseau de longueur $L$).
> - $N=4$ (Harmonique 4) : \texttt{A ()()()() B} (4 fuseaux de longueur $L/4$).
>
> <p style="text-align:center"><a href="/figures/td1_ex4_phv212_corde_fixe_mode.svg" target="_blank" rel="noopener"><img src="/figures/td1_ex4_phv212_corde_fixe_mode.svg" alt="" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex12-adaptation-d-impedance-lame-quart-d-onde-entre-deux-cordes|Exercice 12 — Adaptation d'impédance : lame quart d'onde entre deux cordes]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres-color-blue-part-d-compatibility-of-wavelengths-with-the-normal-mode-model|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres {\color{blue}(Part D — Compatibility of wavelengths with the normal-mode model)}]] · [[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex13-corde-pincee-timbre-harmoniques-absents-et-energie-des-modes|Exercice 13 — Corde pincée : timbre, harmoniques absents et énergie des modes]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex14-corde-de-piano-raide-dispersion-et-inharmonicite|Exercice 14 — Corde de piano raide : dispersion et inharmonicité]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex16-masse-en-bout-de-corde-condition-aux-limites-dynamique-et-equation-transcendante|Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex5-synthese-scientifique-du-tp-color-blue-scientific-summary-of-the-lab|Exercice 5 — Synthèse scientifique du TP {\color{blue}(Scientific summary of the lab)}]]

