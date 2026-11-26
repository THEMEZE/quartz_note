---
title: "Exercice 9 — Complément (niveau 3, ENS) : anneau de N oscillateurs, modes de Fourier et propagation du signal"
tags:
  - td
  - chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/index|⬅ Retour]] · <a href="/pdfs/td4_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 9. Complément (niveau 3, ENS) : anneau de N oscillateurs, modes de Fourier et propagation du signal *(facultatif)*

*Difficulté ●●●●● · ⏱ 120 min · Type : Complément original, problème de type ENS, passerelle vers les ondes*

**Exercice complémentaire original (niveau 3, type ENS).** $N$ masses identiques $m$ ($N\ge3$) glissent sans frottement sur un rail circulaire fixe. Chaque masse est reliée à ses deux voisines par un ressort de raideur $k$, idéalisé de façon à rester tangent au rail (ressorts « curvilignes ») ; à l'équilibre, les masses sont régulièrement espacées d'une longueur $a$ et tous les ressorts sont à leur longueur à vide. On numérote les masses $n=0,1,\dots,N-1$ et on note $x_n(t)$ l'écart (algébrique, le long du rail) de la masse $n$ à sa position d'équilibre ; les indices sont comptés modulo $N$ ($x_N=x_0$, $x_{-1}=x_{N-1}$). On pose $\omega_0=\sqrt{k/m}$.

C'est l'exercice 6 sans parois : la symétrie par rotation (invariance par $n\to n+1$) remplace la symétrie miroir, et la diagonalisation devient une *transformation de Fourier discrète*.


> [!question]- 🪝 Accroche
> **Un anneau de $N$ masses : de quelle taille est le problème ?**
>
> *Durée de l'introduction : 5 min*
>
> *On relie $N=100$ masses identiques en anneau par des ressorts. Faut-il calculer le déterminant d'une matrice $100\times100$ ? Existe-t-il une solution sans calcul ?*
>
> **Idée clé : la symétrie par translation impose la forme des modes.** Tous les sites sont équivalents : si $x_n(t)$ est solution, $x_{n+1}(t)$ l'est aussi. Les modes sont donc des ondes planes discrètes $\mathrm e^{\mathrm i(\omega t-n\theta)}$ et le déterminant n'est jamais à calculer.




> [!abstract]- 🧠 À savoir avant
> **Exercices 4 et 6 du TD4**
>
> Mode de translation ($\omega=0$), matrice $K$, déterminant, décomposition modale, formule $\omega_p=2\omega_0\sin\dfrac{p\pi}{2(N+1)}$ pour les chaînes à parois.
>
> **Nombres complexes et racines de l'unité**
>
> $\mathrm e^{2\mathrm i\pi p/N}$, $p=0,\dots,N-1$ sont les $N$ racines $N$-ièmes de $1$ ; $\sum_{n=0}^{N-1}\mathrm e^{2\mathrm i\pi pn/N}=N\delta_{p0}$ (modulo $N$).
>
> **Fonctions de Bessel (facultatif)**
>
> $J_\nu(z)$ solution de $z^2y''+zy'+(z^2-\nu^2)y=0$ ; représentation $J_n(z)=\dfrac1{2\pi}\displaystyle\int_{-\pi}^{\pi}\mathrm e^{\mathrm i(z\sin\phi-n\phi)}\mathrm d\phi$ ; $J_n(z)\simeq0$ si $|n|>z$.




> [!info]- 🎯 Ce que tu sauras faire
> **Exploiter une symétrie de translation**
>
> Reconnaître que l'invariance par $n\to n+1$ impose des modes de la forme $x_n\propto\mathrm e^{\mathrm i(\omega t-n\theta)}$ et que la périodicité de l'anneau quantifie $\theta=2\pi p/N$.
>
> **Interpréter la dégénérescence et le mode nul**
>
> Identifier les paires de modes de même fréquence ($p\leftrightarrow N-p$, ondes se propageant dans les deux sens), le mode $p=0$ (rotation d'ensemble, $\omega=0$) et, pour $N$ pair, le mode $p=N/2$ (alternance $+,-$).
>
> **Faire le lien avec une équation différentielle d'ordre $2N$**
>
> Relier le système $M\ddot X+KX=0$ au système d'ordre $1$ de dimension $2N$ et à son polynôme caractéristique $\lambda^2\prod_{p}(\lambda^2+\omega_p^2)$, où le facteur $\lambda^2$ traduit la double racine nulle (bloc de Jordan).
>
> **Voir émerger la propagation**
>
> Pour $N$ grand, une perturbation initiale locale se propage à la vitesse maximale $\omega_0$ (masses par seconde) ; calculer $x_n(t)=a_0J_{2n}(2\omega_0t)$ et le front.




> [!note]- 🧮 Outils mathématiques
> **Ondes discrètes**
>
> $x_n=\mathrm{Re}\big[A\mathrm e^{\mathrm i(\omega t-n\theta)}\big]$ ; $x_{n\pm1}=\mathrm{Re}[A\mathrm e^{\mathrm i(\omega t-n\theta)}\mathrm e^{\mp\mathrm i\theta}]$ ; $x_{n+1}+x_{n-1}=2\cos\theta\,x_n$.
>
> **Relation trigonométrique**
>
> $2-2\cos\theta=4\sin^2\dfrac\theta2$.
>
> **Matrice circulante**
>
> Matrice de coefficients $C_{nm}=c_{(m-n)\bmod N}$ : ses vecteurs propres sont les vecteurs de Fourier $(\mathrm e^{-\mathrm i\theta_pn})_n$ et ses valeurs propres sont $\sum_jc_j\mathrm e^{\mathrm i\theta_pj}$.
>
> **Intégrale de Bessel**
>
> $\dfrac1{2\pi}\displaystyle\int_{-\pi}^{\pi}\cos(2\omega_0t\sin\tfrac\theta2)\,\mathrm e^{\mathrm in\theta}\,\mathrm d\theta=J_{2n}(2\omega_0t)$ pour $n$ entier.



**q1.** **Question 1.** Établir l'équation du mouvement de la masse $n$ et la mettre sous la forme $M\ddot X+KX=0$ ; préciser $K$ pour $N=4$ puis pour $N$ quelconque. Cette équation est-elle exacte ?


> [!tip]- 💡 Coup de pouce
> **Deux ressorts**
>
> Les ressorts voisins ont pour allongements $x_{n+1}-x_n$ (à droite) et $x_n-x_{n-1}$ (à gauche) ; le ressort de droite tire la masse $n$ vers l'avant s'il est allongé.
>
> **Cas $N=4$**
>
> Écrivez les quatre équations en tenant compte que $x_4=x_0$ et $x_{-1}=x_3$.




> [!success]- ✅ Correction
> **Équations**
>
> $m\ddot x_n=k(x_{n+1}-2x_n+x_{n-1})$ ; $K=k\begin{pmatrix}2&-1&0&-1\\-1&2&-1&0\\0&-1&2&-1\\-1&0&-1&2\end{pmatrix}$ pour $N=4$ ; $K=k(2I-S-S^{-1})$ avec $S$ la matrice de décalage $(Sx)_n=x_{n+1}$. Équation exacte (déplacements le long du rail, ressorts curvilignes idéaux).




> [!example]- 📝 Solution détaillée
> **Forces et allongements**
>
> Allongement algébrique du ressort entre $n$ et $n+1$ : $e_n=x_{n+1}-x_n$ (nul à l'équilibre : ressorts non déformés). Sur la masse $n$ : le ressort de droite (allongement $e_n$) exerce $+ke_n$, celui de gauche (allongement $e_{n-1}$) exerce $-ke_{n-1}$ : $m\ddot x_n=k(e_n-e_{n-1})=k(x_{n+1}-2x_n+x_{n-1})$.
>
> **Matrice**
>
> Pour $N=4$ : $x_{-1}=x_3$ et $x_4=x_0$ ajoutent les termes « de coin » $K_{03}=K_{30}=-k$. Pour $N$ quelconque, $K=k(2I-S-S^{-1})$ : symétrique, *circulante* (chaque ligne est la précédente décalée d'un cran).
>
> **Exactitude**
>
> L'équation est exacte parce que les ressorts sont supposés idéaux et tangents au rail : leur allongement est exactement la différence des abscisses curvilignes. Pour des ressorts rectilignes (cordes entre masses d'un anneau), la géométrie (angle entre les cordes) introduirait des termes non linéaires, linéarisables à petits déplacements avec une raideur effective modifiée ; on s'en affranchit ici (comparer avec le TD sur les petits angles).
>
> **Contrôles**
>
> $K(1,\dots,1)^{\mathsf T}=0$ (la somme de chaque ligne est nulle) : la rotation d'ensemble ne déforme aucun ressort, donc il existe un mode de fréquence nulle. Somme des équations : $\sum_n\ddot x_n=0$, la quantité de mouvement totale (tangentielle) est conservée.



**q2.** **Question 2.** *Approche du physicien : onde discrète.* On cherche des solutions $x_n=\mathrm{Re}[A\mathrm e^{\mathrm i(\omega t-n\theta)}]$. (a) Montrer que $\omega^2=4\omega_0^2\sin^2(\theta/2)$. (b) Quelle condition la périodicité de l'anneau impose-t-elle à $\theta$ ? (c) Combien de modes distincts, quelle dégénérescence ?


> [!tip]- 💡 Coup de pouce
> **Reporter dans l'équation**
>
> Calculez $x_{n+1}+x_{n-1}-2x_n$ pour l'onde : le facteur $\mathrm e^{-\mathrm in\theta}$ est commun, il reste $\mathrm e^{-\mathrm i\theta}+\mathrm e^{\mathrm i\theta}-2$.
>
> **Périodicité**
>
> $x_{n+N}=x_n$ pour tout $n$ : que doit valoir $\mathrm e^{-\mathrm iN\theta}$ ?




> [!success]- ✅ Correction
> **Résultat**
>
> $-\omega^2=\omega_0^2(2\cos\theta-2)$, soit $\omega^2=4\omega_0^2\sin^2\frac\theta2$ ; $\mathrm e^{\mathrm iN\theta}=1$ donne $\theta_p=\dfrac{2\pi p}N$, $p=0,\dots,N-1$ ; $\omega_p=2\omega_0\sin\dfrac{\pi p}N$. $\omega_p=\omega_{N-p}$ : dégénérescence deux fois ; $p=0$ : mode nul ; $p=N/2$ ($N$ pair) : non dégénéré.




> [!example]- 📝 Solution détaillée
> **Relation de dispersion**
>
> Pour $x_n=\mathrm{Re}[A\mathrm e^{\mathrm i(\omega t-n\theta)}]$ : $\ddot x_n=-\omega^2x_n$ et $x_{n+1}+x_{n-1}=2\cos\theta\,x_n$, d'où $-\omega^2=\omega_0^2(2\cos\theta-2)$, soit $\omega^2=2\omega_0^2(1-\cos\theta)=4\omega_0^2\sin^2\dfrac\theta2$ : $\omega=2\omega_0\big|\sin\dfrac\theta2\big|$. C'est la *relation de dispersion* du réseau. Elle est périodique en $\theta$ (de période $2\pi$) et bornée : $\omega\le2\omega_0$ (aucune onde ne se propage au-dessus de $2\omega_0$ : la chaîne se comporte comme un filtre passe-bas).
>
> **Quantification par la périodicité**
>
> $x_{n+N}=x_n$ exige $\mathrm e^{-\mathrm iN\theta}=1$, donc $\theta_p=2\pi p/N$ avec $p$ entier ; $p$ et $p+N$ décrivent la même onde (le déphasage $\theta$ n'est défini que modulo $2\pi$), d'où $p\in\{0,\dots,N-1\}$ : $N$ modes pour $N$ masses (cohérent).
>
> **Dégénérescence**
>
> $\omega_p=2\omega_0\sin\dfrac{\pi p}{N}$ vérifie $\omega_{N-p}=\omega_p$ : les ondes $\mathrm e^{\mathrm i(\omega t-n\theta_p)}$ et $\mathrm e^{\mathrm i(\omega t+n\theta_p)}$ (progressive vers $+n$ et vers $-n$) ont la même fréquence ; leurs combinaisons réelles donnent deux ondes stationnaires indépendantes $\cos(n\theta_p)$ et $\sin(n\theta_p)$. Seuls les modes $p=0$ et (si $N$ pair) $p=N/2$ ne sont pas dégénérés.
>
> **Exemples**
>
> - $N=3$ : $\omega=0$ ; $\omega=\sqrt3\,\omega_0$ (double).
> - $N=4$ : $\omega=0$ ; $\sqrt2\omega_0$ (double, modes $(1,0,-1,0)$ et $(0,1,0,-1)$) ; $2\omega_0$ (mode $(1,-1,1,-1)$).
> - $N=6$ (benzène) : $0$ ; $\omega_0$ (double) ; $\sqrt3\omega_0$ (double) ; $2\omega_0$.
> - $N=2$ : $\omega_1=2\omega_0\sin\frac\pi2=2\omega_0$ ; cohérent avec deux ressorts en parallèle de raideur $2k$ et masse réduite $m/2$ : $\omega^2=2k/(m/2)=4\omega_0^2$.
>
> **Mode nul**
>
> $p=0$ : $\theta=0$, $\omega=0$ : $x_n=a+bt$ pour tout $n$ (rotation d'ensemble de l'anneau à vitesse constante) : ce n'est pas une oscillation. Il correspond à la racine double $\lambda=0$ du système d'ordre $1$ : bloc de Jordan, d'où le terme $bt$.



**q3.** **Question 3.** *Approche du mathématicien.* (a) Montrer que $K$ est diagonalisée par la base de Fourier et retrouver les valeurs propres $4\sin^2(\pi p/N)$. (b) Écrire le système d'ordre $1$ de dimension $2N$ et son polynôme caractéristique. (c) Que vaut la solution générale ? Combien de constantes d'intégration ?


> [!tip]- 💡 Coup de pouce
> **Matrice de décalage**
>
> $(Sx)_n=x_{n+1}$ ; $S^N=I$ ; les valeurs propres de $S$ sont les racines $N$-ièmes de l'unité $\mathrm e^{\mathrm i\theta_p}$ avec les vecteurs propres $v^{(p)}_n=\mathrm e^{\mathrm i\theta_pn}$.
>
> **Ordre 1**
>
> $Y=(X,\dot X)$, $\dot Y=\mathcal AY$ avec $\mathcal A=\begin{pmatrix}0&I\\-M^{-1}K&0\end{pmatrix}$ ; $\lambda^2=-\omega^2$.




> [!success]- ✅ Correction
> **Résultat**
>
> $Sv^{(p)}=\mathrm e^{\mathrm i\theta_p}v^{(p)}$, $S^{-1}v^{(p)}=\mathrm e^{-\mathrm i\theta_p}v^{(p)}$ ; $Kv^{(p)}=k(2-2\cos\theta_p)v^{(p)}=4k\sin^2(\pi p/N)\,v^{(p)}$. $\chi_{\mathcal A}(\lambda)=\lambda^2\prod_{p=1}^{N-1}(\lambda^2+\omega_p^2)$ ; solution générale : $2N$ constantes.




> [!example]- 📝 Solution détaillée
> **Diagonalisation de $K$**
>
> $K=k(2I-S-S^{-1})$ est un polynôme en $S$ : elle a les mêmes vecteurs propres que $S$. $S$ est un décalage cyclique : $Sv^{(p)}=\mathrm e^{\mathrm i\theta_p}v^{(p)}$ avec $v^{(p)}_n=\mathrm e^{\mathrm i\theta_pn}$ (la périodicité $\mathrm e^{\mathrm i\theta_pN}=1$ est exactement la condition de l'anneau). Donc $Kv^{(p)}=k(2-\mathrm e^{\mathrm i\theta_p}-\mathrm e^{-\mathrm i\theta_p})v^{(p)}=k(2-2\cos\theta_p)v^{(p)}=4k\sin^2\dfrac{\pi p}Nv^{(p)}$. Les $N$ vecteurs $v^{(p)}$ sont orthogonaux (relation $\sum_n\mathrm e^{\mathrm i(\theta_p-\theta_q)n}=N\delta_{pq}$) : base de Fourier, la matrice de passage $F_{np}=\mathrm e^{\mathrm i\theta_pn}/\sqrt N$ est unitaire. Les vecteurs sont complexes : en combinant $v^{(p)}$ et $v^{(N-p)}=\overline{v^{(p)}}$ on obtient les vecteurs réels $\cos\theta_pn$ et $\sin\theta_pn$ de la valeur propre double.
>
> **Système d'ordre 1 et polynôme caractéristique**
>
> $\mathcal A$ a pour taille $2N\times2N$. Si $(\vec u,\lambda\vec u)$ est vecteur propre, $\lambda^2=-\omega^2$ avec $\omega^2$ valeur propre de $M^{-1}K$ : le polynôme caractéristique est $\prod_{p=0}^{N-1}(\lambda^2+\omega_p^2)=\lambda^2\prod_{p=1}^{N-1}(\lambda^2+\omega_p^2)$, de degré $2N$. Les valeurs propres de $\mathcal A$ sont donc $\pm\mathrm i\omega_p$, et *pas* les $\omega_p^2$ du problème mécanique. La racine $\lambda=0$ est double (algébriquement) mais le noyau de $\mathcal A$ n'est que de dimension $1$ pour ce mode (un seul vecteur propre $(1,\dots,1;0,\dots,0)$) : bloc de Jordan $\begin{pmatrix}0&1\\0&0\end{pmatrix}$, d'où $\mathrm e^{\mathcal At}$ contient un terme polynomial $t$.
>
> **Solution générale**
>
> $$x_n(t)=a+bt+\sum_{p=1}^{N-1}\big[c_p\cos(\omega_pt)+d_p\sin(\omega_pt)\big]\cos(\theta_pn+\varphi_p)\quad(\text{à regrouper selon la dégénérescence}),$$
> soit au total $2N$ constantes réelles d'intégration (position et vitesse initiales de chaque masse) : $a,b$ pour le mode nul et deux par mode oscillant.
>
> **Comparaison des deux approches**
>
> L'approche du physicien (onde plane) est la même que celle du mathématicien (vecteurs propres de $S$) : l'invariance par translation *impose* que les modes soient les vecteurs propres de $S$. Pour un anneau, aucune matrice $N\times N$ n'a à être diagonalisée : le calcul revient à une transformée de Fourier discrète (FFT).



**q4.** **Question 4.** *Cas $N=4$ en détail.* Retrouver les modes de l'anneau de $4$ masses en utilisant les symétries (méthode du physicien : $x_0\pm x_2$, $x_1\pm x_3$) puis décomposer le mouvement issu de $x_0(0)=a_0$, les autres masses au repos, vitesses initiales nulles.


> [!tip]- 💡 Coup de pouce
> **Combinaisons**
>
> Posez $P=x_0+x_2$, $Q=x_0-x_2$, $R=x_1+x_3$, $S=x_1-x_3$. Écrivez les équations de $P$, $Q$, $R$, $S$.




> [!success]- ✅ Correction
> **Résultat**
>
> $\ddot P=-2\omega_0^2(P-R)$ , $\ddot R=-2\omega_0^2(R-P)$ , $\ddot Q=-2\omega_0^2Q$ , $\ddot S=-2\omega_0^2S$ : modes $P=R$ ($\omega=0$), $P=-R$ ($\omega=2\omega_0$), $Q$ et $S$ ($\omega=\sqrt2\omega_0$, double). Avec $x_0(0)=a_0$ : $x_0=\dfrac{a_0}4\big(1+\cos2\omega_0t\big)+\dfrac{a_0}2\cos\sqrt2\omega_0t$ ; $x_1=x_3=\dfrac{a_0}4(1-\cos2\omega_0t)$ ; $x_2=\dfrac{a_0}4\big(1+\cos2\omega_0t\big)-\dfrac{a_0}2\cos\sqrt2\omega_0t$.




> [!example]- 📝 Solution détaillée
> **Équations de $P,Q,R,S$**
>
> Avec $x_4=x_0$ : $\ddot x_0=\omega_0^2(x_1+x_3-2x_0)$ et $\ddot x_2=\omega_0^2(x_1+x_3-2x_2)$ ; en additionnant : $\ddot P=\omega_0^2(2R-2P)$ ; en soustrayant : $\ddot Q=-2\omega_0^2Q$. De même $\ddot x_1=\omega_0^2(x_0+x_2-2x_1)$ et $\ddot x_3=\omega_0^2(x_0+x_2-2x_3)$ : $\ddot R=\omega_0^2(2P-2R)$ et $\ddot S=-2\omega_0^2S$. Le découplage « par addition/soustraction » réussit en deux étapes (symétrie de l'anneau sous la rotation de $\pi$).
>
> **Sous-système $(P,R)$**
>
> $\ddot P+2\omega_0^2P-2\omega_0^2R=0$ et $\ddot R+2\omega_0^2R-2\omega_0^2P=0$ : somme $\ddot{(P+R)}=0$ (mode nul : $P+R=A+Bt$, translation d'ensemble de la somme des déplacements) ; différence $\ddot{(P-R)}+4\omega_0^2(P-R)=0$ : $\omega=2\omega_0$ (masses voisines en opposition : $(1,-1,1,-1)$).
>
> **Conditions initiales**
>
> $x_0(0)=a_0$, les autres nuls : $P(0)=a_0$, $Q(0)=a_0$, $R(0)=S(0)=0$ ; vitesses nulles. Donc $P+R=a_0$ (constante), $P-R=a_0\cos2\omega_0t$, $Q=a_0\cos\sqrt2\omega_0t$, $S=0$. D'où $P=\tfrac{a_0}2(1+\cos2\omega_0t)$, $R=\tfrac{a_0}2(1-\cos2\omega_0t)$, $x_0=\dfrac{P+Q}2$, $x_2=\dfrac{P-Q}2$, $x_1=x_3=\dfrac R2$ : résultat de la correction. Vérifications : $x_0(0)=\tfrac{a_0}2+\tfrac{a_0}2=a_0$ ; $x_2(0)=0$ ; $x_1(0)=0$ ; somme $\sum x_n=P+R=a_0$ constante (conservation de la quantité de mouvement avec vitesse initiale nulle).
>
> **Interprétation**
>
> La masse $2$ (opposée) ne bouge qu'après que le mouvement est passé par les voisins ($x_1=x_3$). Les deux fréquences $2\omega_0$ et $\sqrt2\omega_0$ sont incommensurables ($\sqrt2$ irrationnel) : le mouvement n'est pas périodique. L'énergie reste répartie sur les trois modes non nuls, et le « centre de masse » $\tfrac14\sum x_n=a_0/4$ ne bouge pas (conservation de la quantité de mouvement).



**q5.** **Question 5.** *Propagation d'un signal ($N$ grand).* À $t=0$, on déplace la masse $0$ de $a_0$ (les autres au repos, vitesses nulles). (a) Montrer que $x_n(t)=\dfrac{a_0}N\sum_{p=0}^{N-1}\cos(\omega_pt)\cos(\theta_pn)$. (b) Pour $N\to\infty$, montrer que $x_n(t)=a_0J_{2n}(2\omega_0t)$ et interpréter. (c) Quelle est la vitesse maximale de propagation ? Quelle est la limite de validité ?


> [!tip]- 💡 Coup de pouce
> **Projection**
>
> Les modes de Fourier réels $\cos\theta_pn$ sont orthogonaux ; la composante de $X(0)=a_0\delta_{n0}$ sur le mode $p$ est $a_0/N$ (par $\sum_n\mathrm e^{\mathrm i\theta_pn}\delta_{n0}=1$).
>
> **Passage à l'intégrale**
>
> Pour $N\to\infty$ : $\dfrac1N\sum_p\to\dfrac1{2\pi}\int_0^{2\pi}\mathrm d\theta$, avec $\omega=2\omega_0|\sin\frac\theta2|$ : reconnaître la représentation intégrale de $J_{2n}$.
>
> **Vitesse**
>
> La vitesse de groupe est $\dfrac{\mathrm d\omega}{\mathrm d\theta}=\omega_0\cos\dfrac\theta2$ (en masses par seconde).




> [!success]- ✅ Correction
> **Résultat**
>
> (a) $x_n(t)=\dfrac{a_0}N\sum_p\cos(\omega_pt)\cos(\theta_pn)$. (b) $x_n(t)\to a_0J_{2n}(2\omega_0t)$. (c) Vitesse de groupe $v_g=\omega_0\cos(\theta/2)\le\omega_0$ ; $J_{2n}(z)\simeq0$ pour $z<2|n|$ : le signal atteint la masse $n$ à $t\simeq|n|/\omega_0$ ; valable tant que $t<N/(2\omega_0)$ (les deux fronts se rejoignent à l'antipode).




> [!example]- 📝 Solution détaillée
> **Décomposition modale**
>
> $X(0)=a_0\vec e_0$. Les modes $v^{(p)}$ sont orthogonaux avec $\|v^{(p)}\|^2=N$ ; $\vec e_0=\dfrac1N\sum_pv^{(p)}$ (la somme des $\mathrm e^{\mathrm i\theta_pn}$ vaut $N\delta_{n0}$). Vitesses nulles : $x_n(t)=\dfrac{a_0}N\sum_p\cos(\omega_pt)\,\mathrm e^{\mathrm i\theta_pn}$ ; la somme étant réelle par symétrie $p\leftrightarrow N-p$, $x_n(t)=\dfrac{a_0}N\sum_p\cos(\omega_pt)\cos(\theta_pn)$. Contrôle : à $t=0$, $x_n=a_0\delta_{n0}$.
>
> **Limite $N\to\infty$**
>
> La somme devient $\dfrac1{2\pi}\displaystyle\int_0^{2\pi}\cos\Big(2\omega_0t\sin\dfrac\theta2\Big)\cos(n\theta)\,\mathrm d\theta$, c'est-à-dire (en posant $\theta=2\phi$) $\dfrac1\pi\displaystyle\int_0^{\pi}\cos(2\omega_0t\sin\phi)\cos(2n\phi)\,\mathrm d\phi=J_{2n}(2\omega_0t)$ (représentation intégrale de Bessel). Donc $x_n(t)=a_0J_{2n}(2\omega_0t)$ (vérifié numériquement avec $N=400$ pour $2\omega_0t\le10$ : écart $<10^{-6}$).
>
> **Interprétation et front**
>
> $J_\nu(z)$ est négligeable pour $z<\nu$ (zone « classiquement interdite ») et oscille pour $z>\nu$ : $x_n$ est quasi nul tant que $2\omega_0t<2|n|$, soit $t<|n|/\omega_0$. Le signal avance donc à la vitesse $\omega_0$ masses par seconde, soit $c=\omega_0a=a\sqrt{k/m}$ mètres par seconde : c'est la vitesse maximale de groupe $\omega_0\cos(\theta/2)\le\omega_0$ (celle des grandes longueurs d'onde, $\theta\to0$). En avant du front, $J_{2n}$ décroît exponentiellement : le signal est négligeable, sans être strictement nul (le modèle de ressorts linéaires n'est pas relativiste).
>
> **Limite continue**
>
> Pour $p\ll N$, $\omega_p\simeq\omega_0\theta_p=\omega_0ak_p$ avec $k_p=2\pi p/(Na)$ le nombre d'onde et $Na$ la circonférence : $\omega=ck$ avec $c=\omega_0a$ : ondes non dispersives de vitesse $c$, solutions de $\partial_t^2x=c^2\partial_s^2x$. Pour les $p$ proches de $N/2$, la dispersion devient forte ($\omega\to2\omega_0$ plafond, vitesse de groupe $\to0$) : la propagation est dispersive et le signal s'étale (hors programme).
>
> **Validité**
>
> Pour un anneau de $N$ masses, la formule vaut tant que les deux fronts partis dans les deux sens ne se sont pas rencontrés, soit $t<N/(2\omega_0)$ ; ensuite le signal revient et interfère avec lui-même (récurrences ; période $\sim N/\omega_0$). Les petits déplacements ($a_0\ll a$) sont nécessaires pour la linéarité du modèle.




> [!note]- 🔗 Liens avec d'autres disciplines
> **Physique du solide**
>
> Phonons d'un cristal unidimensionnel avec conditions aux limites périodiques de Born--von Kármán : $\omega(k)=2\omega_0|\sin(ka/2)|$.
>
> **Chimie**
>
> Modes de vibration d'une molécule cyclique (benzène, $N=6$) : fréquences $0$, deux fois $\omega_0$, deux fois $\sqrt3\omega_0$, une fois $2\omega_0$.
>
> **Mathématiques**
>
> Diagonalisation des matrices circulantes par la transformée de Fourier discrète (FFT).




> [!question]- 🔭 Aller plus loin — Licence : Limite continue
> Montrer que pour $\lambda=Na\gg a$ (donc $p\ll N$) : $\omega_p\simeq\omega_0\dfrac{2\pi p}{N}=c\,k_p$ avec $k_p=2\pi p/(Na)$ et $c=\omega_0a$. Retrouver l'équation $\partial_t^2x=c^2\partial_s^2x$ (d'Alembert) comme limite de $m\ddot x_n=k(x_{n+1}-2x_n+x_{n-1})$.




> [!question]- 🔭 Aller plus loin — Master : Anneau avec une masse différente
> Remplacer la masse $0$ par $m(1+\varepsilon)$. Montrer que le décalage au premier ordre de $\omega_p^2$ est $-\varepsilon\,\omega_p^2/N$ pour les modes non dégénérés, et que la dégénérescence $p\leftrightarrow N-p$ est partiellement levée (modes en $\cos$ et en $\sin$).




> [!question]- 🔭 Aller plus loin — Master : Fréquence de Debye
> Dénombrer les modes de fréquence inférieure à $\omega$ : $\simeq N\omega/(\pi\omega_0)$ à basse fréquence ; en déduire la densité d'états $g(\omega)$ et son comportement près de $\omega=2\omega_0$ (singularité de van Hove).




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex2-couplage-de-deux-oscillateurs-harmoniques-dissymetriques|Exercice 2 — Couplage de deux oscillateurs harmoniques dissymétriques]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex3-oscillations-libres-et-forcees-d-un-couplage-pendule-chariot|Exercice 3 — Oscillations libres et forcées d'un couplage pendule-chariot]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex4-frequence-propre-d-une-molecule-diatomique|Exercice 4 — Fréquence propre d'une molécule diatomique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex5-complement-niveau-1-cpge-pendules-couples-par-un-ressort-attache-a-mi-hauteur|Exercice 5 — Complément (niveau 1, CPGE) : pendules couplés par un ressort attaché à mi-hauteur]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex6-complement-niveau-2-ambitieux-trois-masses-quatre-ressorts-diagonalisation-et-perturbation|Exercice 6 — Complément (niveau 2, ambitieux) : trois masses, quatre ressorts, diagonalisation et perturbation]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex7-complement-niveau-2-ambitieux-oscillateurs-desaccordes-anticroisement-et-transfert-d-energie|Exercice 7 — Complément (niveau 2, ambitieux) : oscillateurs désaccordés, anticroisement et transfert d'énergie]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex8-complement-niveau-3-ens-modes-non-lineaires-de-deux-pendules-couples-stabilite-et-instabilite-parametrique|Exercice 8 — Complément (niveau 3, ENS) : modes non linéaires de deux pendules couplés, stabilité et instabilité paramétrique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex1-pendules-couples-et-battements|Exercice 1 — Pendules couplés et battements]]


