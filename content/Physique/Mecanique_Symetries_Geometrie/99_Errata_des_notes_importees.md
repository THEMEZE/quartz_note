---
title: Errata et corrections des notes importées
tags:
  - Errata
lang: fr
---

> Retour : [[00_Index]]

# Corrections apportées aux notes importées

| Note | Problème | Correction |
|---|---|---|
| *Algèbre graduée* | graduation triviale : « $\mathcal A_i=\emptyset$ pour $i>0$ » | $\mathcal A_i=\{0\}$ (sous-espace vectoriel) — [[08_Algebres_graduees_ideaux_superalgebres]] |
| *Super-algèbre de Lie* | exemple « $\mathfrak{osp}(1\vert2)$ = $\{J_0,J_\pm\}$, $J_0$ pair, $J_\pm$ impairs, $\{J_+,J_-\}=2J_0$ » : le super-Jacobi échoue ($4[J_+,J_0]=-4J_+\neq0$) ; dimension attendue $(3\vert2)$ | présentation correcte avec $H,E,F,Q_\pm$ et vérification |
| *Super-algèbre de Lie* | formule $[x,y\}=xy-(-1)^{\|x\|\|y\|}yx$ présentée comme définition | valable seulement dans une algèbre **associative** graduée |
| *Calcul différentiel extérieur* | « $\Lambda V^/ast$ », « $\forall\dots\colon:$ », $\alpha_p(v_i)$ au lieu de $\alpha_p(v_1)$ dans le déterminant | coquilles corrigées dans [[02_Formes_differentielles_calcul_exterieur]] ; ajout de $d$, Cartan, Stokes, Hodge, Poincaré |
| *Notations pour théorie de jauge* | $\partial_{[\mu}F_{\nu\rho]}$ défini avec facteur $\frac12$ puis écrit comme somme cyclique sans $\frac13$ | convention $\frac1{3!}$ et forme cyclique explicite — [[03_Jauge_EM_YM_Gravite]] |
| idem | $A\wedge A\ne0$ « car $A_\mu A_\nu\ne A_\nu A_\mu$ » | $A\wedge A=\frac12[A,A]$ ; nul pour $U(1)$ — [[04_Connexions]] |
| idem | « $D*R=*T$ analogue exact de $d*F=*J$ » | faux : les équations de champ sont Einstein–Cartan ($\varepsilon_{abcd}e^b R^{cd}\propto\tau_a$, $\varepsilon_{abcd}e^cT^d\propto\sigma_{ab}$) ; $DR=0$ est une **identité** |
| idem | formule de Christoffel : dernier terme $\partial_\sigma g_{\beta\sigma}$ (annexe A de *Kerr_biblio*) | $-\partial_\sigma g_{\mu\nu}$ |
| *Théorie de jauge* (tableaux) | « Yang–Mills : portée infinie sans brisure de jauge » ; « cerle » ; gravité $SO(1,3)$ avec connexion affine $\Gamma$ | confinement/Higgs ; $\Gamma$ vit dans $GL(4)$, $\omega$ dans $SO(1,3)$ |
| *Supergravité* | « $\psi$ = gravition » | gravitino (spin 3/2) |
| idem | action $\bar\psi\wedge\gamma_5\gamma\wedge D\psi$ sans $e^a$ | $\bar\psi\wedge\gamma_5\gamma_aD\psi\wedge e^a$ — [[02_Supergravite_connexion_courbure]] |
| idem | action 11D sans $\frac1{2\kappa^2}$, $\star$, $\frac12$, $\frac16$ | $R\star1-\frac12G_4\wedge\star G_4-\frac16C_3G_4G_4$ |
| idem | $T^a=de^a+\omega e+\bar\psi\gamma^a\psi$ | coefficient $-\frac12$ à convention près |
| *Kerr_biblio* | (D.1)–(E.1) : $\partial_\theta S=-L$ (devrait être $\partial_\varphi S=-L$) ; $\mathcal M_{BL}$ défini avec $\mathcal M_{III}=\mathbb R\times]-\infty,r_-[\times S^2\setminus\mathcal R$ ; « $\mathbb R^2\times\mathbb S^2$ » pour $\mathbb R\times\mathbb R\times S^2$ | corrigé dans [[13_Kerr_trou_noir_en_rotation]], [[14_Kerr_horizons_ergoregion_extension_maximale]] |
| *Kerr_biblio* | « $A=1/(F_0G^2)$, $r\to\tilde r$ » : la détermination de $AB=1$ est annoncée comme hypothèse | prouvée par $R_{tt}e^{-2(\alpha-\beta)}+R_{rr}=\frac2r(\alpha'+\beta')=0$ — [[11_Schwarzschild_trou_noir]] |
