---
title: Synthèse, pièges, bibliographie
tags:
  - Physique
  - Mathematiques
lang: fr
partie: XVI
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Synthèse, pièges, bibliographie

## XVI.1 Tableau de synthèse : symétrie $\leftrightarrow$ charge $\leftrightarrow$ théorème

| Groupe | Générateurs | Charge de Noether | Théorème « mécanique » |
|---|---|---|---|
| translations $\mathbb R^n$ | $P_i$ | $\vec P$ | TRD |
| rotations $SO(n)$ | $L_{ij}$ | $L=\sum x\wedge p$ | TMC, forces centrales |
| temps | $H$ | $E$ | TEM |
| boosts galiléens | $K_i$ | $m\vec x_G-\vec Pt$ | mouvement de $G$ rectiligne uniforme |
| $E(n)$ | $(P,L)$ | **torseur** | Varignon $=\mathrm{Ad}^\ast$ |
| $SO(n+1)$ (Kepler) | $(L,A)$ | RLL | fermeture des orbites |
| $U(1)$ | $Q$ | charge électrique/proba | continuité |
| Poincaré | $(P^\mu,M^{\mu\nu})$ | spin = $\star(M\wedge P)$ | Wigner |
| super-Poincaré | $(P,M,Q)$ | $Q$ fermionique | $H\ge0$, BPS |
| difféomorphismes | $\xi^\mu$ | $T^{\mu\nu}$ conservé, $H\approx0$ | Einstein–Cartan, ADM |

## XVI.2 Pièges classiques

1. $\doteq$ pour *définir*, $=$ pour *démontrer* ; ne pas écrire $=$ à la place d'une définition.
2. Le produit vectoriel et « le moment est un vecteur » n'existent qu'en **3D** ; en général $M\in\Lambda^2E$. Signes : $M^{ij}=\varepsilon^{ijk}M_k$ mais $\Omega^{ij}=-\varepsilon^{ijk}\Omega_k$.
3. Le torseur cinématique $\{\Omega;v\}$ est de type **vitesse** ($v(B)=v(A)+\Omega\overrightarrow{AB}$) ; les autres de type **moment** ($M(B)=M(A)+\overrightarrow{BA}\wedge R$).
4. $D(A)=\dot L(A)+v_A\wedge P$ ; $D(A)=\dot L(A)$ seulement pour $A$ fixe ou $A=G$.
5. $E_{\text{totale}}$ conservée toujours ; $E_m$ sous conditions ; $E_c$ seulement pour les chocs élastiques ; **$\vec P$ se conserve même si $E_c$ non**.
6. $e\neq\alpha=E_c'/E_c$ ; $\alpha=e^2$ cas particulier seulement.
7. Règle des $90^\circ$ : masses égales, cible immobile, élastique, **sans rotation ni frottement**.
8. $L$ conservé avec la forme **forte** de la 3e loi.
9. Noether donne les charges des symétries **globales** ; les symétries locales donnent des identités (Noether II) et des contraintes.

## XVI.3 Exercices pour continuer

1. $(\star)$ Fusée $m_0=100$ t, $v_e=3$ km/s, $\Delta V=6$ km/s : $m_f/m_0=e^{-2}$, soit $\simeq86{,}5\%$ de carburant.
2. $(\star\star)$ Fronde frontale à contre-courant : $v_f=v_i+2U$ en norme ; pourquoi aucun gain depuis l'infini dans $\mathscr R_{\text{planète}}$.
3. $(\star\star)$ Collisionneur vs cible fixe pour des protons de 7 TeV : $\sqrt s=14$ TeV contre $\sqrt{2mc^2E}\simeq114$ GeV ; énergie équivalente cible fixe $\approx10^8$ GeV.
4. $(\star\star\star)$ Boules identiques en 1D : $\sum v_i^3$ conservée ; à masses différentes, faux en général.
5. $(\star\star)$ Montrer en dimension $n$ que le couple $(L,A)$ de Kepler a $\tfrac{n(n+1)}2$ composantes ; calculer $\{A_i,A_j\}$.
6. $(\star\star\star)$ Montrer que $M\wedge R$ est invariant de transport (III.3) et le relier à l'hélicité.
7. $(\star\star\star)$ SUSY-QM : vérifier que $H=\{d,\delta\}$ sur $S^2$ donne $\operatorname{Tr}(-1)^F=2$.
8. $(\star\star\star)$ Retrouver $T_{F1}=1/2\pi\ell_s^2$ à partir de $T_{M2}$ enroulée (fait en XV.3) puis $T_{D4}$ à partir de $T_{M5}$.

## XVI.4 Bibliographie

**Mécanique** : J. Fillette, J. Froustey, H. Roussille, *Physique pour l'agrégation* ; S. Olivier, H. Gié, J.-P. Sarmant, *Physique Spé PC\*/PC* ; B. Hauchecorne, *Formulaire MPSI-MP* ; B. Beaufils, *Formulaire PCSI-MPSI/PTSI-PSI* ; J. R. Taylor, *Classical Mechanics* (2005) ; L. Landau & E. Lifchitz, *Mécanique* (Mir, 1966) ; V. I. Arnold, *Méthodes mathématiques de la mécanique classique* ; J.-M. Souriau, *Structure des systèmes dynamiques* (1970) ; R. Abraham & J. Marsden, *Foundations of Mechanics*.
**Symétries** : E. Noether, *Invariante Variationsprobleme* (1918) ; V. Bargmann (1954) ; V. Fock, *Z. Phys.* 98 (1935) ; W. Pauli, *Z. Phys.* 36 (1926) ; E. Wigner (1939).
**Collisions et GGE** : M. Rigol et al., PRL 98, 050405 (2007) ; T. Kinoshita, T. Wenger, D. Weiss, Nature 440, 900 (2006) ; E. Lieb & W. Liniger, Phys. Rev. 130, 1605 (1963) ; O. Castro-Alvaredo, B. Doyon, T. Yoshimura, PRX 6, 041065 (2016) ; B. Bertini et al., PRL 117, 207201 (2016).
**Gravité/relativité** : B. P. Abbott et al. (LIGO/Virgo), PRL 116, 061102 (2016) ; P. Touboul et al. (MICROSCOPE), PRL 129, 121102 (2022).
**SUSY, sugra** : Coleman–Mandula (1967) ; Haag–Łopuszański–Sohnius (1975) ; J. Wess & J. Bagger, *Supersymmetry and Supergravity* ; E. Witten, *Nucl. Phys. B* 202 (1982) ; Freedman–Van Proeyen, *Supergravity* ; Cremmer–Julia–Scherk (1978) ; Nahm (1978).
**Gravité quantique, cordes** : C. Rovelli, *Quantum Gravity* ; C. Kiefer, *Quantum Gravity* ; J. Donoghue, PRD 50 (1994) ; J. Polchinski, *String Theory* ; Becker–Becker–Schwarz ; E. Witten, *Nucl. Phys. B* 443 (1995) ; Hořava–Witten (1996) ; Banks–Fischler–Shenker–Susskind (1997) ; J. Maldacena, *Adv. Theor. Math. Phys.* 2 (1998).

*Fin du document.*
