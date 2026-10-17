---
title: "Exercice 1 — Dérivation de fonctions en physique"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/index|⬅ Retour]] · <a href="/pdfs/td2_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td2_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 1. Dérivation de fonctions en physique

En Physique, les variables et les fonctions changent souvent de nom, d'où l'intérêt d'utiliser la notation différentielle lors du calcul de dérivées. De plus, les fonctions contiennent des paramètres (grandeurs constantes) souvent représentés par des lettres : il faut donc bien distinguer variables et paramètres.
Notation en Physique sur les dérivées par rapport au temps $t$ : la dérivée $\frac{\mathrm{d}x}{\mathrm{d}t}$ se note $\dot{x}$.\\

Déterminer la dérivée des fonctions suivantes (en utilisant la notation diﬀérentielle) :



{
        %\fontsize{10pt}{10pt}\selectfont

        \[
        \begin{array}{rrcllcrrcll}
        \textbf{(a)} & f(x) & = & k\, \ln x  & k \, \text{constant}  && \textbf{(d)} & r(\theta) & = & a \, \cos \theta + b \, \sin \theta &  \text{$a$ et $b$ constants}
        \\[2mm]

        \textbf{(b)} & g(t) & = & R \, \cos( 2 \omega t ) & \text{$R$ et $\omega$ constants} && \textbf{(e)} & x(t) 
        & = & a \, \cos ( \alpha t^2 ) & \text{$a$ et $\alpha$ constants}
        \\[2mm]

        \textbf{(c)} & h(t)
        & = & \sin^2(\omega t) & \text{$\omega$ constant}
        && \textbf{(f)} & z(t)
        & = & a \, t^2 - b t  & \text{$a$ et $b$ constants}
        \end{array}
        \]

      

    }

**1.**

  **a)** Déterminer la dérivée de $f(x) = k \ln(x)$ avec $k$ constant.

> [!tip]- 💡 Coup de pouce
> **différentielle $d(k\ln)$
> **
>
> Le paramètre $k$ est en facteur, il reste inchangé lors de la dérivation. Et\\
> $$
> \mathrm{d}(\ln x ) = \frac{\mathrm{d}x}{x}.
> $$


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$
> \begin{array}{rcl}
> \mathrm{d}f(x) & = & \mathrm{d}(k\,\ln)(x)\\
> & = & k \, \mathrm{d}(\ln)(x) \\
> & = & {\displaystyle k \,  \frac{\mathrm{d}x}{x} } 
> \end{array}
> $$
> Donc 
> $$\frac{\mathrm{d}f}{\mathrm{d}x} = k \, \cdot \frac{1}{x} = \frac{k}{x}.$$


  **b)** Déterminer la dérivée de $g(t) = R \cos(2\omega t)$ avec $R$ et $\omega$ constants.

> [!tip]- 💡 Coup de pouce
> **Différentiel de $\cos(u)$
> **
>
> $$ \mathrm{d}(\cos u ) = -\sin(u) \cdot \mathrm{d}(u)$$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> soit $h(x) = R \, \cos x $ et $u(t) = 2\omega t$, tel que $g(t) = h(u(t))$
> $$
> \begin{array}{rcl}
> \mathrm{d}g(t) & = & \mathrm{d}(R \, h \circ u )(t),\\
> & = & R \,  \mathrm{d}(h \circ u )(t), \\
> & = & R \, h'(u)(t) \cdot \mathrm{d}(u)(t) \\
> \end{array}
> $$
>
> Or $h'(x) = - \sin x $ et $\mathrm{d}(u)(t) = 2\omega \, \mathrm{d}t$
>
> Donc 
>
> $$
> \mathrm{d}g(t) ~ = ~ - 2 R \omega \sin ( 2\omega t )\, \mathrm{d}t,
> $$
>
> donc 
>
> $$\dot{g}(t) \equiv  \frac{\mathrm{d}g}{\mathrm{d}t} = R \cdot (-2\omega \sin(2\omega t)) = -2 R \omega \sin(2\omega t)$$


  **c)** Déterminer la dérivée de $h(t) = \sin^2(\omega t)$ avec $\omega$ constant.

> [!tip]- 💡 Coup de pouce
> **Composition multiple**
>
> Pose $u(t) = \sin(\omega t)$. Alors $h = u^2$. Et utilise $\mathrm{d}(u^n)  =  n \, u^{n-1} \cdot \mathrm{d}u$


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> On pose $h = u^2$ avec $u(t) = \sin(\omega t)$.
> \[
> \mathrm{d}h(t) = \mathrm{d}(u^2)(t) = 2 \, u(t) \cdot \mathrm{d}u(t) = 2 \, \overbrace{\sin(\omega t)}^{u(t)} \cdot \overbrace{\omega \cos(\omega t) \mathrm{d}t}^{\mathrm{d}u(t)} = \omega \, \underbrace{2 \, \sin(\omega t) \, \cos(\omega t)}_{\sin(2 \omega t)} \, \mathrm{d}t,
> \]
>
> ou encore
>
> \[
> \dot{h}(t) \equiv \frac{\mathrm{d}h}{\mathrm{d}t}(t) = 2 \cdot \sin(\omega t) \cdot (\omega \cos(\omega t))
> \]
>
> En utilisant la formule trigonométrique $2\sin(x)\cos(x) = \sin(2x)$ :
> \[
> \dot{h}(t) = \omega \sin(2\omega t)
> \]


  **d)** Déterminer la dérivée de $r(\theta) = a \cos(\theta) + b \sin(\theta)$ avec $a$ et $b$ constants.

> [!tip]- 💡 Coup de pouce
> **Variable $\theta$
> **
>
> Ici la variable est $\theta$. On dérive chaque terme indépendamment.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$
> \mathrm{d}r(\theta) = \mathrm{d}(a \cos + b \sin)(\theta) = a\, \mathrm{d}\cos(\theta) + b\, \mathrm{d} \sin(\theta) = (- a \, \sin + b \, \cos ) (\theta)  \, \mathrm{d}\theta
> $$
> Donc 
> $$\frac{\mathrm{d}r}{\mathrm{d}\theta} = -a \sin(\theta) + b \cos(\theta).$$
> Mieux 
> $$r' = -a \sin + b \cos).$$


  **e)** Déterminer la dérivée de $x(t) = a \cos(\alpha t^2)$ avec $a$ et $\alpha$ constants.

> [!tip]- 💡 Coup de pouce
> **Dérivée de l'argument**
>
> L'argument est $u(t) = \alpha t^2$, dont la dérivée temporelle est $u'(t) = 2\alpha t$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$ \begin{array}{rcl} \mathrm{d}x(t)  & = &  \mathrm{d}(a \, \cos (u))(t) \\ & =  & a \, \mathrm{d}(\cos (u))(t) \\ & =  & a \, \cos'(u(t)) \cdot  \mathrm{d}(u)(t)\\ & = & a \, \overbrace{-\sin(\alpha t^2)}^{\cos'(u(t))} \cdot  \overbrace{2 \alpha t \mathrm{d} t}^{\mathrm{d}(u)(t)} \\ & =  & -2 a \alpha t \sin(\alpha t^2)  \mathrm{d} t \end{array} $$
> Encore
>
> $$\dot{x}(t) \equiv \frac{\mathrm{d}x}{\mathrm{d}t} = a \cdot (-2\alpha t \sin(\alpha t^2)) = -2 a \alpha t \sin(\alpha t^2)$$


  **f)** Déterminer la dérivée de $z(t) = a t^2 - b t$ avec $a$ et $b$ constants.

> [!tip]- 💡 Coup de pouce
> **Dérivation terme à terme**
>
> Applique la règle de puissance sur chaque terme en $t$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$ \mathrm{d}z(t) = (2a t - b) \mathrm{d}t $$
> Soit 
> $$\dot{z}(t) = \frac{\mathrm{d}z}{\mathrm{d}t} = 2a t - b.$$


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex2-interpretation-de-la-differentielle-petite-variation-calcul-d-incertitude|Exercice 2 — Interprétation de la différentielle : petite variation $\&$ calcul d'incertitude]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex3-derivees-de-fonctions-composees|Exercice 3 — Dérivées de fonctions composées]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex4-differentielle-logarithmique|Exercice 4 — Différentielle logarithmique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex5-derivation-de-fonctions-en-physique-approfondissement|Exercice 5 — Dérivation de fonctions en physique (approfondissement)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex6-interpretation-de-la-differentielle-approfondissement-volume-pendule-approximations|Exercice 6 — Interprétation de la différentielle : approfondissement (volume, pendule, approximations)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex7-derivees-de-fonctions-composees-approfondissement-taux-lies|Exercice 7 — Dérivées de fonctions composées : approfondissement (taux liés)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex8-differentielle-logarithmique-approfondissement-incertitudes-en-situation-reelle|Exercice 8 — Différentielle logarithmique : approfondissement (incertitudes en situation réelle)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex9-combiner-les-incertitudes-somme-absolue-p-1-quadratique-p-2-puissance-p-et-cas-p-0|Exercice 9 — Combiner les incertitudes : somme absolue ($p=1$), quadratique ($p=2$), puissance $p$ et cas $p=0$]]

