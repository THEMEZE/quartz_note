---
title: Kerr — coordonnées régulières, extension analytique maximale et diagramme de Penrose
tags:
  - Physique
  - Relativite-generale
  - Trous-noirs
lang: fr
---

> Retour : [[00_Index]] · avant : [[13_Kerr_trou_noir_en_rotation]], [[12_Coordonnees_EF_Kruskal_Penrose_extension_maximale]]
> D'après *P.B. (annexes E–F, chapitre 1)*. $G=c=1$, $0<a<m$ ; $r_\pm=m\pm\sqrt{m^2-a^2}$ ($r_+r_-=a^2$, $r_++r_-=2m$).

# Kerr : prolongement à travers $\Delta=0$ et extension maximale

## 1. Coordonnée tortue de Kerr

Pour les géodésiques nulles principales : $\dfrac{dr_\ast}{dr}=\dfrac{r^2+a^2}\Delta=1+\dfrac{2mr}\Delta$ et, par fractions partielles $\dfrac{2mr}{(r-r_+)(r-r_-)}=\dfrac{2m}{r_+-r_-}\Big[\dfrac{r_+}{r-r_+}-\dfrac{r_-}{r-r_-}\Big]$ :
$$r_\ast=r+\frac{2m}{r_+-r_-}\Big[r_+\ln\Big|\frac{r-r_+}{2m}\Big|-r_-\ln\Big|\frac{r-r_-}{2m}\Big|\Big].$$
Pente de l'équation des rayons : $\dot\varphi=a/\Delta$ ⇒ $d\varphi=\tfrac a\Delta dr$ le long de $\ell_\pm$ (**le rayon spirale**).

## 2. Coordonnées de Kerr (entrantes) et de Kerr–Schild

Prendre $v=t+r_\ast$ et $\tilde\varphi=\varphi+\int\tfrac a\Delta dr$ :
$$d\tilde t\doteq dt+\frac{2mr}\Delta dr,\quad d\tilde\varphi=d\varphi+\frac a\Delta dr\quad(\tilde t=v-r).$$
(Les dérivées donnent bien $d\tilde t=dv-dr$ car $dv=dt+\tfrac{r^2+a^2}\Delta dr$.) Dans $(\tilde t,r,\theta,\tilde\varphi)$ :
$$ds^2=-\Big(1-\frac{2mr}{\rho^2}\Big)d\tilde t^2+\frac{4mr}{\rho^2}d\tilde t\,dr-\frac{4amr\sin^2\theta}{\rho^2}d\tilde t\,d\tilde\varphi+\Big(1+\frac{2mr}{\rho^2}\Big)dr^2-2a\Big(1+\frac{2mr}{\rho^2}\Big)\sin^2\theta\,dr\,d\tilde\varphi+\rho^2d\theta^2+\frac{\Sigma^2\sin^2\theta}{\rho^2}d\tilde\varphi^2 .$$
**Régulière** en $\Delta=0$ ($\det g=-\rho^4\sin^2\theta$ inchangé, plus de $1/\Delta$). Les vecteurs tangents entrants : $\tilde\ell_-=\partial_{\tilde t}-\partial_r$, **ne s'annulant jamais** et pointant vers le futur à grand $r$. Les rayons entrants sont les droites $\tilde t=v-r$ ; les sortants :
$$\tilde t=r+\frac{2m}{r_+-r_-}\Big(r_+\ln\Big|\frac{r-r_+}{2m}\Big|-r_-\ln\Big|\frac{r-r_-}{2m}\Big|\Big)+\text{cte}.$$
**Domaine étendu** : $\mathcal M\doteq\mathcal M_{BL}\cup\mathcal H\cup\mathcal H_{in}=\mathbb R^2\times S^2\setminus\mathcal R$ ($\mathcal R$ : anneau $r=0,\theta=\tfrac\pi2$). On voit que :
- une particule de $\mathcal M_{II}$ **ne peut éviter** $\mathcal H_{in}$ ($\tilde t$-future) ; l'horizon externe $\mathcal H$ se traverse dans le sens entrant seulement ;
- dans $\mathcal M_{III}$ (ligne $r\le r_-$) on a un **espace-temps où la singularité (anneau) est de genre temps** : une particule peut s'approcher de $\{r=0\}$ **ou l'éviter** et passer à $r<0$ à travers le disque (analytiquement continué), où la gravité est **répulsive** et où existent des CTC (§6 de [[13_Kerr_trou_noir_en_rotation]]).
La construction par coordonnées **sortantes** ($d\tilde t=dt-\tfrac{2mr}\Delta dr$, $d\tilde\varphi=d\varphi-\tfrac a\Delta dr$, renversement du temps $t\to-t$) étend de manière symétrique et traverse les horizons en sens inverse (région **trou blanc** correspondante), comme pour (EF$^+$) en Schwarzschild.

## 3. Pourquoi deux horizons

En $a=0$ : $r_-=0$ (se confond avec la singularité), $r_+=2m$. Pour $a>0$ : **$\mathcal H_{in}=\{r=r_-\}$ = horizon de Cauchy** (limite du domaine de dépendance de données initiales sur la tranche asymptotique) ; il sépare $\mathcal M_{II}$ (où $r$ est une coordonnée **temporelle**, $\Delta<0$) de $\mathcal M_{III}$ (où $\Delta>0$ de nouveau et $r$ est spatiale).

## 4. Construction du diagramme de Carter–Penrose le long de l'axe

On se restreint à l'axe de symétrie $\theta=0$ (là $a$ disparaît de $\rho^2=r^2+a^2$, mais l'anneau n'est pas atteint) : métrique $ds^2_{(2)}=-\tfrac\Delta{r^2+a^2}dt^2+\tfrac{r^2+a^2}\Delta dr^2$ (**2D**), conformément $=\tfrac\Delta{r^2+a^2}(-dt^2+dr_\ast^2)$. On construit les coordonnées nulles $u=t-r_\ast$, $v=t+r_\ast$ et, **autour de chaque horizon** $r_\pm$, les analogues de Kruskal :
$$U_\pm=\mp e^{-\kappa_\pm u},\ \ V_\pm=e^{\kappa_\pm v},\quad\kappa_\pm=\pm\frac{r_+-r_-}{2(r_\pm^2+a^2)}\ (\kappa_+=\kappa,\ \kappa_-<0),$$
qui rendent la métrique régulière sur $\mathcal H$ resp. $\mathcal H_{in}$. Puis on compactifie par $\arctan$ (transformation de Penrose, [[12_Coordonnees_EF_Kruskal_Penrose_extension_maximale]] §5). On **recolle** ces cartes : $\mathcal M_I\to\mathcal M_{II}$ au travers de $\mathcal H$, $\mathcal M_{II}\to\mathcal M_{III}$ au travers de $\mathcal H_{in}$ ; chaque horizon a ses **deux** branches (entrante/sortante), d'où quatre exemplaires de chaque région adjacente à une même sphère de bifurcation. On obtient la **tour infinie** :
```
            ⋮                              ⋮
   𝓜'''_I  \   /  𝓜_III''   (r<r_-, anneau en r=0)
             ╳  H_in
   𝓜_II'   /   \  trou blanc / noir ...
   𝓜_I'   ╳ H   ╳   𝓜_I     (univers asymptotiques)
   𝓜_II   \   /
             ╳  H_in
   𝓜_III  /   \  𝓜_III'    (r→-∞ asympt. plat, gravité répulsive)
            ⋮
```
**Règles de lecture** (diagramme de Carter–Penrose de l'extension analytique maximale) :
1. Cônes de lumière à $45^\circ$ ; carrés = régions ; chaque point = une 2-sphère (sauf sur l'axe/anneau).
2. $\mathcal M_I$ : $r\in(r_+,\infty)$, bords $i^0,\mathscr I^\pm,i^\pm$ ; $\mathcal M_{II}$ : losange $r_-<r<r_+$ (entre les deux horizons) ; $\mathcal M_{III}$ : $r<r_-$, comprend $r\to0^+$ (avec l'anneau, **singularité de genre temps** donc **verticale** dans le diagramme), et se prolonge à $r<0$ (autre univers asymptotiquement plat avec $r\to-\infty$).
3. La **singularité n'est plus un mur horizontal** (spatial comme pour Schwarzschild) mais une **ligne verticale** (temporelle) : on peut l'éviter (confirmé par la note).
4. Une particule matérielle venant de $\mathcal M_I$ traverse $\mathcal H$ puis $\mathcal H_{in}$ et **remonte** dans le diagramme ; elle ne peut pas revenir (les horizons ne se traversent que dans un sens) ; elle peut atteindre un autre $\mathcal M_I'$ (autre univers) ou $\mathcal M_{III}$ (puis $r<0$).
5. En faisant $a\to0$ : $\mathcal H_{in}$ s'écrase sur $r=0$ et la tour se réduit au diagramme de Schwarzschild (diamant à singularité spatiale), après rotation de $90^\circ$ des motifs (cf. [[12_Coordonnees_EF_Kruskal_Penrose_extension_maximale]]).
6. $a>m$ : plus d'horizon, singularité nue.

## 5. Limites physiques de l'extension

- **Instabilité de l'horizon de Cauchy** (Penrose 1968) : une perturbation arrivant de l'infini (ou un flux de rayonnement) est **décalée vers le bleu** ($e^{\kappa_-v}$, $\kappa_-<0$) sur $\mathcal H_{in}$ (ou « horizon intérieur ») ⇒ divergence de l'énergie vue par un observateur qui le traverse. **Inflation de masse** (Poisson–Israel 1990) : la fonction de masse locale diverge, la singularité devient de genre **espace** et faiblement nulle. Donc l'extension analytique complète (univers multiples, anneau, $r<0$) **ne se réalise pas** pour un trou noir réaliste (formé par effondrement, non éternel, perturbé) : tout **trou noir de Kerr analytique est un objet éternel, dans le vide, instable sous la traversée d'une particule matérielle** (comme le dit la note).
- **Censure cosmique forte** (Penrose) : conjecture que l'horizon de Cauchy générique est une singularité ; état de l'art : vrai en $\mathcal C^2$, discuté en $\mathcal C^0$.
- **Régions $r<0$**, CTC, anneau nu : mathématiquement licites mais probablement non physiques.

## 6. Comparaison Schwarzschild / Kerr

| | Schwarzschild ($a=0$) | Kerr ($0<a<m$) |
|---|---|---|
| Killing | $\partial_t,\partial_\varphi$ et $SO(3)$ | $\partial_t,\partial_\varphi$ (axisymétrique) |
| Horizons | $r=2m$ | $r_\pm=m\pm\sqrt{m^2-a^2}$ |
| Ergorégion | aucune ($g_{tt}=0$ sur $\mathcal H$) | $r_+<r<r_{E+}(\theta)$ |
| Singularité | $r=0$ spatiale (point) | anneau, **temps** (évitable), $r<0$ |
| Trou blanc | oui (symétrie $T\to-T$ ) | oui, tours multiples |
| Diagramme maximal | diamant (4 régions) | tour infinie de régions |
| $\kappa$, $T_H$ | $\tfrac1{4m},\tfrac1{8\pi m}$ | $\tfrac{\sqrt{m^2-a^2}}{2mr_+}$ |
| Extraction d'énergie | non | oui (Penrose, jusqu'à 29 %) |
| Torseur $(M,J)$ | $J=0$ | $J=ma$ |

**Conclusion.** Schwarzschild fait une distinction stricte entre trou noir et trou blanc (statiques) et prévoit un univers $\mathcal M_{III}$ **inaccessible** (traverser l'unique horizon force à rencontrer une singularité spatiale). Kerr **double** l'horizon, rend la singularité évitable (genre temps) et permet de traverser $\mathcal H$ puis $\mathcal H_{in}$ vers d'autres univers, dans un seul sens ; mais l'instabilité de $\mathcal H_{in}$ interdit cette traversée pour un trou noir astrophysique.
