---
title: Connexion et courbure en supergravité
---


<style>
  /* === Base des détails === */
  details {
    border-radius: 10px;
    margin: 1rem 0;
    padding: 0.6rem 1rem;
    border: 1px solid #888; /* neutre pour s’adapter aux modes */
    overflow: hidden;
    transition:
      all 0.2s ease,
      background-color 0.3s,
      color 0.3s;
    font-family: "Courier New", Courier, monospace; /* effet “craie” */
    text-shadow: 0 0 1px rgba(255, 255, 255, 0.5); /* léger effet craie */
  }

  /* === Summary === */
  details summary {
    font-weight: 600;
    cursor: pointer;
    font-size: 1.05rem;
    padding: 0.6rem 1rem;
    margin: 0;
  }

  /* line under summary when open */
  details[open] summary {
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  }

  /* === Types === */
  details.theorem {
    border-left: 5px solid #1f77b4;
  }
  details.proof {
    border-left: 5px solid #2ca02c;
  }
  details.recall {
    border-left: 5px solid #9467bd;
  }
  details.calculation {
    border-left: 5px solid #ff7f0e;
  }
  details.warning {
    border-left: 5px solid #d62728;
  }
  details.example {
    border-left: 5px solid #17becf;
  }
  details.affirmation {
    border-left: 5px solid #17becf;
  }

  /* === Contenu interne === */
  details > *:not(summary) {
    padding: 0.6rem 1rem 1rem 1rem;
    line-height: 1.5rem;
  }

  /* === Mode clair === */
  @media (prefers-color-scheme: light) {
    details {
      /* background: #fdfdfd; */
      /* color: #222; */
      border-color: #ccc;
      /*text-shadow: 0 0 1px rgba(0, 0, 0, 0.2); /* craie légère sombre */ 
    }

    details[open] summary {
      border-bottom-color: #eee;;
    }
  }

  /* === Mode sombre === */
  @media (prefers-color-scheme: dark) {
    details {
      /* background: #111; */
      /* color: #eee; */
      
      border-color: #555;
      /*text-shadow: 0 0 2px rgba(255, 255, 255, 0.8); /* craie blanche */ 
    }
    details[open] summary {
      border-bottom-color:  #eee;;
    }
  }
</style>

<!-- === JS pour toggle MathJax et fermer tous les détails au chargement === -->
<script>
  function renderMath() {
    if (window.MathJax) MathJax.typesetPromise();
  }

  window.addEventListener("load", () => {
    renderMath();
    document
      .querySelectorAll("details")
      .forEach((d) => d.removeAttribute("open"));
  });

  document.querySelectorAll("details").forEach((d) => {
    d.addEventListener("toggle", renderMath);
  });
</script>

<!-- === MathJax === -->
<script>
  window.MathJax = {
    tex: {
      inlineMath: [
        ["\\(", "\\)"],
        ["$", "$"],
      ],
    },
    svg: { fontCache: "global" },
  };
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>


<!-- <details class="theorem" open>
  <summary>Théorème</summary>

Soit $M$ une variété... alors :
$$
R^{ab} = d\omega^{ab} + \omega^a{}_c \wedge \omega^{cb}
$$

</details> -->


# Connexion et courbure en supergravité


Nous partons de la **connexion de super-Poincaré**, notée 

$$
\mathcal A =\tfrac12\,\omega^{ab}J_{ab} + e^a P_a +  \bar\psi Q,
$$
où  $\omega^{ab}$ la connexion de spin (jauge de Lorentz) , $e^a$ est le vielbein (jauge des translations locales) et $\psi$ le gravitino (jauge de supersymétrie). Cette connexion de jauge unifiée prend ses valeurs dans l’algèbre de super-Poincaré $\mathfrak{g}$. 


<details class="affirmation">

  <summary>
    <!-- <strong> -->
    Affirmation  👉 L’écriture — <span class="math">\( A = \omega + e + \psi \)</span>  est un abus de notation 
    <!-- </strong>  -->
  </summary> 

>[!info]+ 👉 l’écriture
>$$
>A = \omega + e + \psi
>$$
>est **un abus de notation** pour alléger :
>*    $\omega \equiv \frac{1}{2}\omega^{ab} J_{ab}$ 
>*    $e \equiv e^a P_a$ 
>*    $\psi \equiv \bar{\psi} Q$ 
>
>| terme         | rôle                       |
| ------------- | -------------------------- |
>| $\omega^{ab}$ | connexion Lorentz          |
>| $e^a$         | "connexion" de translation |
>| $\psi$        | gravitino (spin 3/2)       |
>

</details>


<details class="affirmation">

  <summary>
    Affirmation  👉 La bonne structure est : — <span class="math">\( \text{superconnexion } \mathcal{A} \in \Omega^1(M, \mathfrak{g}_{\text{super}}) \)</span>   
  </summary> 

>[!note]+ La bonne structure est :
>$$
> \text{superconnexion } \mathcal{A} \in \Omega^1(M, \mathfrak{g}_{\text{super}}) 
>$$
>où :
>*    $\mathfrak{g}_{\text{super}}$  = **superalgèbre de Lie**
>*   contient :
>*    *   générateurs bosoniques (Lorentz, translations)
>*    *   générateurs fermioniques (supersymétrie)
>
>>[!note]- Superalgèbre de Poincaré
>>
>>📌 Générateurs
>>$$
>>\{ J_{ab}, \; P_a, \; Q_\alpha \}
>>$$
>>*    $J_{ab}$  : Lorentz
>>*    $P_a$  : translations
>>*    $Q_\alpha$  : supercharges (spinor)
</details>

<details class="affirmation">
  <summary>
    Superconnexion complète  
  </summary> 

> [!note]+ Superconnexion complète
> Je fixe les conventions (4D, signature  $\eta=\mathrm{diag}(-,+,+,+)$ , spineurs de Majorana) pour éviter toute ambiguïté.
> $$
>\mathcal A = e^a P_a + \tfrac12\,\omega^{ab}J_{ab} + \bar\psi Q,
>$$
>*    $\omega^{ab} = -\omega^{ba}$  1-forme bosonique
>*    $e^a$  1-forme bosonique (vielbein)
>*    $\psi$  1-forme fermionique (gravitino)  (Majorana)
>*    $\bar\psi = \psi^\mathrm{T} C$ , $C$  matrice de conjugaison de charge
>*   Matrices de Clifford :  $\gamma^a$ ,  $\gamma^{ab} = \frac12[\gamma^a,\gamma^b]$ 

</details>

<details class="affirmation">
  <summary>
    Superalgèbre Poincaré SUGRA ~ (AdS ( \(\mathfrak{osp}(1|4)\)))
  </summary> 

> [!info]+  Superalgèbre Poincaré SUGRA ~ (AdS ( $\mathfrak{osp}(1|4)$ ))
>$$
>\begin{aligned} 
>[J_{ab},J_{cd}] &= \eta_{bc} J_{ad} - \eta_{ac} J_{bd} - \eta_{bd} J_{ac} + \eta_{ad} J_{bc} \\ 
>[J_{ab},P_c] &= \eta_{bc} P_a - \eta_{ac} P_b \\ 
>[P_a,P_b] &= \frac{1}{\ell^2} J_{ab},\\ 
>[J_{ab},Q_\alpha] &= \frac12 (\gamma_{ab})_\alpha{}^\beta Q_\beta \\ 
>[P_a,Q_\beta] &= \frac{1}{2\ell} {(\gamma_a)^\alpha}_{\beta } Q_\alpha ,\\
>\{Q_\alpha,Q_\beta\} &= (C \gamma^a)_{\alpha\beta} P_a +\frac{1}{\ell}(C\gamma^{ab})_{\alpha\beta} J_{ab} 
>\end{aligned}
>$$
>
>>[!info]-👉  $\ell$  = rayon AdS  
>>
>>( $\Lambda \sim -1/\ell^2$ )
>>
>
>>[!info]-Cas plat (Poincaré) $\frac{1}\ell = 0$
>>
>>*    $e\wedge e = 0$ 
>>*   torsion purement SUSY
>
>>[!info]- Cas AdS  $\frac{1}\ell \neq 0$
>>*    **version FDA avec  $e\wedge e\neq 0$  (cosmologique / AdS)
>>*   la géométrie a une **courbure intrinsèque**
>>*   SUSY mélange :
>>*   *   translation
>>*   *   rotation
>>
</details>

On calcule la courbure 2-forme
$$
\mathcal F = d\mathcal A + \mathcal A\wedge\mathcal A.
$$

<details class="affirmation">
  <summary>
    Différentielle extérieure  — <span class="math">\( df \)</span>    
  </summary>

>[!info]+ Différentielle extérieure  $df$ 
>Soit une fonction scalaire :
>$$
>f : \mathcal M \to \mathbb{R}
>$$
>La différentielle extérieure est la 1-forme :
>$$
> df = \partial_\mu f \, dx^\mu. 
>$$
>>[!question]- Que signifie  $dx^\mu$  ?
>>
>>Soit une variété  $\mathcal M$  avec coordonnées  $x^\mu$ .
>>Les  $dx^\mu$  sont des **1-formes de base**.
>>> Définition rigoureuse
>>
>>Si  $f$  est une fonction :
>>$$
>>df = \partial_\mu f \, dx^\mu
>>$$
>>Les  $dx^\mu$  sont définis par dualité :
>>$$
>>dx^\mu(\partial_\nu) = \delta^\mu_\nu
>>$$
>>Donc :
>>*    $\partial_\mu$  = base tangentielle
>>*    $dx^\mu$  = base cotangentielle
>>Ils vivent dans :
>>$$
>>T^*\mathcal M
>>$$
>>
>>>[!example]- 🔹 Intuition
>>>
>>>$dx^\mu$  mesure la variation infinitésimale dans la direction  $x^\mu$ .
>>>Ce sont les “briques” des formes différentielles :
>>>$$
>>>A = A_\mu dx^\mu
>>>$$
>>>$$
>>>F = \frac12 F_{\mu\nu} dx^\mu \wedge dx^\nu
>>>$$
>>
>>>[!example]- Lien avec les connexions
>>>
>>>Une connexion s’écrit toujours sous la forme :
>>>$$
>>>\Gamma^\rho_{\ \sigma} = \Gamma^\rho_{\ \sigma\mu} dx^\mu
>>>$$
>>>ou
>>>$$
>>>A = A_\mu dx^\mu
>>>$$
>>>Donc :
>>>$$
>>>d = dx^\mu \partial_\mu
>>>$$
>
>Interprétation :
>$$
>df(X) = X(f)
>$$
>où  $X$  est un champ de vecteurs.
>
>🔹 Extension aux `p-formes`
>Pour une p-forme :
>$$
>\omega = \frac{1}{p!} \omega_{\mu_1 \dots \mu_p} dx^{\mu_1}\wedge \dots \wedge dx^{\mu_p}
>$$
>Alors :
>$$
> d\omega = \frac{1}{p!} \partial_\nu \omega_{\mu_1\dots\mu_p} dx^\nu \wedge dx^{\mu_1}\wedge\dots \wedge dx^{\mu_p}  
>$$
>Propriété fondamentale :
>$$
>d^2 = 0
>$$
>>[!hint]- Exemple **ÉléctroMagnétique** :
>>
>>$$
>>F = dA \Rightarrow dF = 0
>>$$
>>(identité de Bianchi).
</details>

<details class="calculation">
  <summary>
    Décomposition de  — <span class="math">\(d \mathcal A \)</span>    
  </summary>

>[!success]+ Décomposition de  $d \mathcal A = \frac12 d\omega^{ab} J_{ab} + de^a P_a + d\bar\psi Q $ 
>$$
>d \mathcal A = \frac12 d\omega^{ab} J_{ab} + de^a P_a + d\bar\psi Q
>$$

</details>

<details class="affirmation">
  <summary>
    Wedge — <span class="math">\( \mathcal A \wedge \mathcal A \)</span>  : règle exacte   
  </summary>
  
> [!info]+ Produit  $\mathcal A \wedge \mathcal A$  : règle exacte
>Très important :
>$$
>\mathcal A \wedge \mathcal A = (\mathcal A^I T_I) \wedge (\mathcal A^J T_J) = \mathcal A^I \wedge \mathcal A^J \; T_I \cdot T_J,
>$$
>👉 Donc :
>*   le $\wedge$ agit sur les **formes**
>*   le produit $\cdot$ agit sur les **générateurs**
>
>>[!warning]-👉 Le point clé : on ne peut pas remplacer directement **$T_I \cdot T_J$** par un crochet sans faire attention à la graduation.
>>
>>$$
>>\mathcal A^I \wedge \mathcal A^J \;\frac{1}{2}[T_I , T_J]
>>$$
>>Ce n’est vrai que si :
>>- les générateurs sont bosoniques
>>- et que les formes sont de degré impair (1-formes classiques)
>>
>>Mais en supergravité :
>>
>>- $\psi$ est **fermionique**
>>- donc $Q$ est **odd**
>>
>>👉  il faut utiliser le super-commutateur
>
>>[!note]-✅ Bonne écriture : super-algèbre 👉 $T_I \cdot T_J = \frac{1}2 [T_I, T_J\}$
>>
>>Le bon objet est :
>>$$
>>[T_I, T_J\} = T_I T_J - (-1)^{|T_I||T_J|} T_J T_I
>>$$
>>où  $[\, \bullet , \bullet  \, \}$  est nomé  `super-commutateur` et $|T_I| = 0$ (boson) ou $1$ (fermion).
>>Plus simplement 
>>$$
>>[T_I,T_J\} = \begin{cases} [T_I,T_J] & \text{boson-boson}\\ [T_I,T_J] & \text{boson-fermion}\\ \{T_I,T_J\} & \text{fermion-fermion} \end{cases}.
>>$$
>
>👉 Donc :
>$$
>\mathcal A \wedge \mathcal A = (\mathcal A^I T_I) \wedge (\mathcal A^J T_J) = \mathcal A^I \wedge \mathcal A^J \;  \frac{1}{2} \; [T_I, T_J\}
>$$
>
>>[!warning]-👉 anti/commutation de $A \wedge \mathcal A$.
>>
>>👉 Donc :
>>$$
>>(\mathcal A^I T_I) \wedge (\mathcal A^J T_J) = \mathcal A^I \wedge \mathcal A^J \;  \frac{1}{2} \; [T_I, T_J\}
>>$$
>>👉 MAIS avec une subtilité essentielle :
>>Le signe total vient de deux sources :
>>1. le wedge :
>>$$
>>\mathcal A^I \wedge \mathcal A^J = - (-1)^{|A_I||A_J|} \mathcal A^J \wedge \mathcal A^I
>>$$
>>2. le super-commutateur $[T_I, T_J\}$
>>$$
>>[T_I, T_J\} =  (-1)^{|T_I||T_J|} [T_J, T_I\}
>>$$
>>👉 Donc $A \wedge \mathcal A$
>>$$
>>A \wedge \mathcal A =  (-1)^{|A_I||A_J|} (-1)^{|T_I||T_J|} \mathcal A^J \wedge \mathcal A^I  \; [T_J, T_I\}
>>$$
>>
>

</details>

<details class="affirmation">
  <summary>
    Wedge — <span class="math">\( \mathcal A \wedge \mathcal A \)</span>  : règle exacte   
  </summary>

>
>
>
>

</details>

<details class="affirmation">
  <summary>
    Wedge et parité — <span class="math">\( \mathcal A \wedge \mathcal B \)</span>  : règle exacte   
  </summary>

>[!note]+ Wedge et parité
> On a la règle générale **super-commutative** pour un  $p$ \-formes  $\mathcal A$  et $q$ \-formes $\mathcal B$  de parité  $|\mathcal A|,|\mathcal B|$  (0 = boson, 1 = fermion) :
> $$
>\mathcal A \wedge \mathcal B = (\mathcal A^I T_I)\wedge(\mathcal B^J G_J)= \mathcal A^I \wedge \mathcal B^J \;\frac12 [T_I, G_J\}
>$$
>Les deux sources de signes
>Tu dois distinguer
>* (A) degré différentiel (formes)
>$$
>\mathcal A^I \wedge \mathcal B^J=(-1)^{pq}(-1)^{|\mathcal A^I||\mathcal B^J|}\mathcal B^J \wedge \mathcal A^I
>$$
>*  * $p,q$  = degrés différentielles (formes)
>*  * $|\mathcal A^I| , |\mathcal B^J|$ = parité du coefficient/ Grassmann (0 = boson, 1 = fermion)
>* (B) parité Grassmann (super-algèbre)
>$$
>T_I G_J = (-1)^{|T_I||G_J|} G_J T_I + [T_I,G_J\}
>$$
>👉 Soit
>$$
>[T_I,G_J\} = -(-1)^{|T_I||G_J|} [G_J,T_I\}
>$$
>*  * $|T_I|,|G_J|$  = parité du générateur/ Grassmann (0 = boson, 1 = fermion)
>* Soit 
>$$
>\mathcal A \wedge \mathcal B =(-1)^{pq}(-1)^{|\mathcal A^I||\mathcal B^J|} \frac{1}{2}\left ( T_I G_J - (-1)^{|T_I||G_J|} G_J T_I \right ) \mathcal B^J \wedge \mathcal A^I
>$$
>>[!hint]- Parité $|\mathcal A^I T_I| = |\mathcal A^I| + |T_I|$
>> $$
>>|\mathcal A|, |A^I T_I| ,  |T_I| \in \mathbb{Z}_2
>>$$
>>$$
>>|\mathcal A^I T_I | = |\mathcal A^I| + |T_I| \quad (\mathrm{mod}\ 2)
>>$$
>
>👉 Donc :
>$$
>\mathcal A \wedge \mathcal B = (-1)^{pq} \frac{1}{2} \left ( (-1)^{|\mathcal A^I||\mathcal B^J|} T_I G_J - (-1)^{|\mathcal A^I T_I ||\mathcal B^I G_I | - |\mathcal A^I||\mathcal G_J| - |\mathcal B^J||\mathcal T_I|} G_J T_I \right )  \mathcal B^J \wedge \mathcal A^I
>$$
>
>> [!tip]- Cas pratique supergravité $|\mathcal A| = 2|\mathcal A^I| = 2|\mathcal T_I| =  0  \quad (\mathrm{mod}\ 2)$
>>
>>Si tu imposes la convention **super-fibré** $|\mathcal A^I| = |T_I|$ et $|\mathcal B^J| = |G_J|$, alors : 
>> $$
>>|2 \mathcal A^I| = 2 |T_I| = 0 \ (\text{mod }2), \quad  2|\mathcal B^I| =  2 |G_J| = 0 \ (\text{mod }2),
>>$$
>>et donc la formule se simplifie à :
>>$$
>>|\mathcal A | = 0 \ (\text{mod }2) , \quad |\mathcal B | = 0 \ (\text{mod }2) 
>>$$

</details>

En développant les crochets de super-algèbre on obtient les composantes classiques : 

<details class="calculation">
  <summary>
    Décomposition de  — <span class="math">\(\mathcal A \wedge \mathcal A = (\omega + e + \psi)\wedge(\omega + e + \psi) \)</span>    
  </summary>

> [!note]+
> $\frac{2!}{0!0!2!}+\frac{2!}{0!1!1!} + \frac{2!}{1!0!1!}+\frac{2!}{1!1!0!} + \frac{2!}{2!0!0!}  + \frac{2!}{0!2!0!}  = 3^2$ termes  [^1] 
>[^1]:$(a_1 + \cdots + a_n)^m=\sum_{\substack{k_1+\cdots+k_n = m \\ k_i \ge 0}}\frac{m!}{k_1!\cdots k_n!}\, a_1^{k_1} \cdots a_n^{k_n}$
>$$
>(\omega + e + \psi)\wedge(\omega + e + \psi) = \omega \wedge \omega + \omega \wedge e  + e \wedge  \omega + e \wedge  e + e \wedge \psi + \psi \wedge  e + \psi \wedge  \psi + \psi \wedge  \omega + \omega \wedge  \psi 
>$$
>
>>[!note]- $\omega \wedge e = e \wedge  \omega$ , $\omega \wedge \psi = \psi \wedge  \omega$  et  $e \wedge \psi = \psi \wedge  e$
>>
>>On a 
>>* 1-forme bosonique :  $|\omega^{ab}|=0$  et $|J_{ab}|=0$ ;
>>* 1-forme bosonique :  $|e^{a}|=0$  et $|P_{a}|=0$
>>* 1-forme fermionique :  $|\overline{\psi}|=1$  et et $|Q|=1$
>>
>>Soit plus généralement
>>* 1-forme bosonique :  $|\mathcal B^{I}|=0$ ;
>>* 1-forme fermionique :  $|\mathcal F^{I}|=1$ ;
>>
>>| Wedge| Degré | Parité | Signe du wedge |
>>| :---: | :---: | :---: | ---: |
>>|  $\mathcal B^{I} \wedge \mathcal B^{J}$  | 1*1 | 0*0 |  $(-1)^{1\ast1}(-1)^{0\ast0} = -1$  |
>>|  $\mathcal B^{I} \wedge \mathcal F^{J}$  | 1*1 | 0*1 |  $(-1)^{1\ast1}(-1)^{0\ast1} = -1$  |
>>|  $\mathcal F^{I} \wedge \mathcal F^{J}$  | 1*1 | 0*0 |  $(-1)^{1\ast1}(-1)^{0\ast1} = +1$  |
>>
>>Et
>>* bosonique :  $| G_{I}|=0$ ;
>>* fermionique :  $| H_{I}|=1$ ;
>>
>>| $[ \bullet , \bullet ]$ |  Parité | Signe  |
>>| :--------------: | :-------: |  :--------: |
>>|  $[G_{I}  , G_{J}]$  |  0*0 |  $-(-1)^{0\ast0} = -1$  |
>>|  $[ G_{I}  ,  H_{J} ]$  |  0*1 |  $-(-1)^{0\ast1} = -1$  |
>>|  $[H_{I} ,  H_{J}$]  |  1*1 |  $-(-1)^{1\ast1} = +1$  |
>> Alors soientt deux, 1-formes $\mathcal A = \mathcal A^I T_I$ et $\mathcal B = \mathcal B^I G_I$ de même ou de différenter nature (bosoniques ou fermioniques) et tel que  $|\mathcal A^{I}| = | T_{I}| $  et $|\mathcal B^{I}| = | G_{I}| $ alors .
>>$$
>>\mathcal A \wedge \mathcal B = \mathcal B \wedge \mathcal A
>>$$
>> Donc  $\omega\wedge e = e \wedge \omega$,  $\omega\wedge\psi = \psi\wedge \omega$ et $e wedge\psi = \psi \wedge e $ .  
>> ✅ C’est **la règle de signe pour les 1-formes**.
>
>Donc $\binom{3}{1} + \binom{3}{2} =6$ termes différents
>$$
>(\omega + e + \psi)\wedge(\omega + e + \psi) = \omega \wedge \omega + e \wedge e + \psi \wedge \psi + 2 \omega \wedge e  +   2 \omega \wedge \psi +  2 e \wedge \psi
>$$
>
>>[!note]- $ \omega \wedge \omega = \frac{1}2 \; {\omega^{a}}_c \wedge \omega^{cb} \, J_{ab} $
>>
>>$$
>> 8 \; \omega \wedge \omega  = \omega^{ab} \wedge \omega^{cd} [ J_{ab}, J_{cd}]
>>$$
>>avec $[J_{ab},J_{cd}] = \eta_{bc} J_{ad} - \eta_{ac} J_{bd} - \eta_{bd} J_{ac} + \eta_{ad} J_{bc}$ et $\eta=\mathrm{diag}(-,+,+,+)$, il vient que 
>>
>>$$
>>\omega^{ab} \wedge \omega^{cd}  [ J_{ab} , J_{cd}] = {\omega^{a}}_c \wedge \omega^{cd}  J_{ad} - {\omega_{c}}^b \wedge \omega^{cd}   J_{bd} - {\omega^{a}}_d \wedge \omega^{cd}   J_{ac} + {\omega_{d}}^b \wedge \omega^{cd}   J_{bc} 
>>$$
>>avec l'antisymétrie $\omega^{ab} = -\omega^{ba}$, il vient que 
>>$$
>>\omega^{ab} \wedge \omega^{cd}  [ J_{ab} , J_{cd}] = 4\; {\omega^{a}}_c \wedge \omega^{cd}  J_{ad} 
>>$$
>
>>[!note]- $ e \wedge e = \frac{1}{2} \, \frac{1}{\ell^2} \, e^a \wedge e^b \, J_{ab} $
>>
>>$$
>> 2 \, e \wedge e  = e^{a} \wedge e^{b} [ P_{a}, P_{b} ]
>>$$
>>avec $[ P_{a}, P_{b}] = \frac{1}{\ell^2} J_{ab}$, il vient que 
>>
>>$$
>>e^{a} \wedge e^{b} [ P_{a}, P_{b}] = \frac{1}{\ell^2} \, e^{a} \wedge e^{b} J_{ab} 
>>$$
>>
>
>>[!note]- $ \psi \wedge \psi = \frac{1}{2} \, \overline{\psi} \wedge \gamma^a \psi \, P_a  +  \frac{1}{2 \ell } \, \overline{\psi} \wedge \gamma^{ab} \psi \, J_{ab}$
>>
>>$$
>>2 \psi \wedge \psi  = \overline{\psi} \wedge \overline{\psi} \{Q, Q \}
>>$$
>>avec $\{Q, Q \} = (C\gamma^a)P_a + \frac{1}{\ell} (C\gamma^{ab})J_{ab}$, il vient que 
>>
>>$$
>>\overline{\psi} \wedge \overline{\psi} \{Q, Q \} = -\overline{\psi} \wedge \overline{\psi} (C\gamma^a)P_a  -  \overline{\psi} \wedge \overline{\psi} \frac{1}{\ell} (C\gamma^{ab})J_{ab}
>>$$
>> Plus généralement 
>>$$
>>\psi \wedge \psi = \frac12 (\psi^\alpha \wedge \psi^\beta)(C\gamma^a)_{\alpha\beta} P_a + \frac12 \frac{1}{\ell} (\psi^\alpha \wedge \psi^\beta)(C\gamma^{ab})_{\alpha\beta} J_{ab}
>>$$
>
>>[!note]- $2 \; \omega \wedge e = {\omega^{a}}_b \wedge e^b \, P_{a} $
>>
>>$$
>> 4 \; \omega \wedge e  = \omega^{ab} \wedge e^{c} [ J_{ab}, P_{c}]
>>$$
>>avec $[J_{ab},P_c] = \eta_{bc} P_a - \eta_{ac} P_b$ et $\eta=\mathrm{diag}(-,+,+,+)$, il vient que 
>>
>>$$
>>\omega^{ab} \wedge e^{cd}  [ J_{ab} , P_{c}] = {\omega^{a}}_c \wedge e^{c}  P_{a} - {\omega_{c}}^b \wedge e^{c}   P_{b} 
>>$$
>>avec l'antisymétrie $\omega^{ab} = -\omega^{ba}$, il vient que 
>>$$
>>\omega^{ab} \wedge e^{c}  [ J_{ab} , P_{c}] = 2\; {\omega^{a}}_b \wedge e^{b}  P_{a} 
>>$$
>
>>[!note]- $2 \; \omega \wedge \psi = \frac{1}{4} \omega^{ab} \wedge \overline{\psi} \, \gamma^{ab}  Q $
>>
>>$$
>> 4 \; \omega \wedge \psi   = \omega^{ab} \wedge \overline{\psi} [ J_{ab}, Q]
>>$$
>>avec $[J_{ab},Q] = \frac{1}{2} \gamma^{ab} Q $ , il vient que 
>>
>>$$
>>\omega^{ab} \wedge \overline{\psi} [ J_{ab}, Q] = \frac{1}{2} \omega^{ab} \wedge \overline{\psi} \, \gamma^{ab} Q
>>$$
>
>>[!note]- $2 \; e \wedge \psi = \frac{1}{2\ell} \,  e^{a} \wedge \overline{\psi} \, \gamma_a \,  Q  $
>>
>>$$
>> 2 \; e \wedge \psi   = e^{a} \wedge \overline{\psi} [ P_{a}, Q]
>>$$
>>avec $[ P_{a}, Q] =  \frac{1}{2\ell} \, \gamma_a \,  Q $ , il vient que 
>>
>>$$
>>e^{a} \wedge \overline{\psi} [ P_{a}, Q] = \frac{1}{2\ell} \,  e^{a} \wedge \overline{\psi} \, \gamma_a \,  Q 
>>$$
>
>Donc 
>$$
>(\omega + e + \psi)\wedge(\omega + e + \psi) = \frac{1}{2} \left (  {\omega^{a}}_c \wedge \omega^{ab} + \frac{1}{\ell^2} e^{a} \wedge e^{b}  -  \frac{1}{\ell} \overline{\psi} \wedge  \gamma^{ab} \psi   \right ) \, J_{ab} + \left ( {\omega^{a}}_b \wedge e^b - \frac{1}{2} \, \overline{\psi} \wedge \gamma^a \psi  \right )  P_{a}  + \left ( \frac{1}{4} \omega^{ab} \wedge \overline{\psi} \, \gamma^{ab} +  \frac{1}{2\ell} \,  e^{a} \wedge \overline{\psi} \, \gamma_a  \right)  Q
>$$
>
>

</details>

<details class="affirmation">
  <summary>
    Définition rigoureuse de  — <span class="math">\( D \)</span>    
  </summary>

>[!note]+ Définition rigoureuse de $D$   
>
>$$
>D = d + \omega
>$$
>mais $\omega$ agit dans **une représentation donnée**
>
>>[!example]- Sur un tenseur $D\omega^{ab} = d\omega^{ab} + \omega^a{}_c \wedge \omega^{cb}$
>
>>[!example]- Sur un vecteur $De^a = de^a + \omega^a{}_b \wedge e^b$
>
>>[!example]- Sur un spineur $D\psi = d\psi + \frac14 \omega^{ab} \wedge \gamma_{ab} \psi$
>>
>>$$
>>D\bar\psi = d\bar\psi - \frac14 \bar\psi \wedge \omega^{ab} \gamma_{ab}
>>$$
>

</details>

<details class="calculation">
  <summary>
    Décomposition de  — <span class="math">\( d \mathcal A + \mathcal A \wedge \mathcal A = \frac{1}{2} R^{ab} J_{ab} +T^a P_a + \overline{\rho} Q   \)</span>    
  </summary>

>[!note]+  $d \mathcal A + \mathcal A \wedge \mathcal A = \frac{1}{2} R^{ab} J_{ab} +T^a P_a + \overline{\rho} Q $   
>
>$$
>d \mathcal A = \frac12 d\omega^{ab} J_{ab} + de^a P_a + d\overline\psi Q 
>$$
>et 
>$$
>\mathcal A \wedge \mathcal A = \frac{1}{2} \left (  {\omega^{a}}_c \wedge \omega^{ab} + \frac{1}{\ell^2} e^{a} \wedge e^{b}  -  \frac{1}{\ell} \overline{\psi} \wedge  \gamma^{ab} \psi   \right ) \, J_{ab} + \left ( {\omega^{a}}_b \wedge e^b - \frac{1}{2} \, \overline{\psi} \wedge \gamma^a \psi  \right )  P_{a}  + \left ( \frac{1}{4} \omega^{ab} \wedge \overline{\psi} \, \gamma^{ab} +  \frac{1}{2\ell} \,  e^{a} \wedge \overline{\psi} \, \gamma_a  \right)  Q
>$$
>donc avec la desfinirion de $D$, il vient que 
>$$
>d \mathcal A + \mathcal A \wedge \mathcal A = \frac{1}{2} R^{ab} J_{ab} +T^a P_a + \overline{\rho} Q 
>$$
>avec 
>$$
>\begin{aligned} R^{ab} &= D\omega^{ab} + \frac{1}{\ell} e^{a} \wedge e^{b}  -  \frac{1}{\ell} \overline{\psi} \wedge  \gamma^{ab} \psi =  \underbrace{\overbrace{d\omega^{ab} + \omega^a{}_c \wedge \omega^{cb}}^{D\omega^{ab}}}_{D\omega^{ab} \text{ : Lorentz pur}} + \underbrace{\frac{1}{\ell^2} e^{a} \wedge e^{b}}_{\text{cosmo}}  -  \underbrace{\frac{1}{\ell} \overline{\psi} \wedge  \gamma^{ab} \psi}_{\text{fermion}} \\ T^a &= De^a - \frac12 \bar\psi \wedge \gamma^a \psi = \overbrace{de^a + \omega^a{}_b \wedge e^b}^{De^a} - \frac12 \bar\psi \wedge \gamma^a \psi \\ \rho &= D\psi  +  \frac{1}{2\ell} \,  e^{a} \wedge \overline{\psi} \, \gamma_a  = \overbrace{d\psi + \frac14 \omega^{ab} \wedge \gamma_{ab} \psi}^{D\psi} +  \frac{1}{2\ell} \,  e^{a} \wedge {\psi} \, \gamma_a  \end{aligned}
>$$
>
>| terme | origine |
>| --- | --- |
>|  $R$  | algèbre de Lorentz |
>|  $T$  | translation + SUSY |
>|  $\rho$  | transport spinoriel |
>
>
>>[!note]- notation abusive  $\mathcal F = R + T +  \rho $ 
>>
>>$$
>>\begin{aligned} R \equiv \frac{1}2 R^{ab}J_{ab}  &, \; R \doteq \underbrace{\overbrace{d\omega + \omega \wedge \omega}^{D\omega}}_{D\omega \text{ : Lorentz pur}} + \underbrace{ e \wedge e }_{\text{cosmo}}  + \underbrace{ \left. \psi \wedge \psi \right \vert_{J_{ab}} }_{\text{fermion}} \\ T \equiv T^a P_a  &, \; T\doteq  \overbrace{de +2 \,  \omega \wedge e}^{De} + \left . \psi \wedge  \psi \right \vert_{P_{a}} \\ \rho \equiv \bar \rho Q  &, \;  \rho   = \overbrace{d\psi + 2 \,  \omega \wedge  \psi}^{D \psi}  +    2 \, e \wedge \psi  \end{aligned}
>>$$

</details>

<details class="recal">
  <summary>
    Vers la théorie-M   
  </summary>


| théorie | connexion | courbure | équation |
| --- | --- | --- | --- |
| EM |  $A$  |  $F$  |  $dF=0,\ d*F=J$  |
| YM |  $A$  |  $F$  |  $DF=0,\ D*F=J$  |
| Gravité |  $(e,\omega)$  |  $(T,R)$  |  $DR=0,\ D*R=T$  |

| théorie | groupe |
| --- | --- |
| EM |  $U(1)$  |
| YM |  $SU(N)$  |
| Gravité |  $SO(1,3)$  |
| SUGRA | Super-Poincaré |

🔹 Fibré principal


$$
P(M, G)
$$

avec :

$$
G = SO(1,3) \quad \text{ou Super-Poincaré}
$$


🔹 Connexion


$$
\omega \in \Omega^1(P, \mathfrak g)
$$



🔹 Courbure


$$
\boxed{ F = d\omega + \frac{1}{2}[\omega,\omega] }
$$



🔥 Identification


| théorie | groupe |
| --- | --- |
| EM |  $U(1)$  |
| YM |  $SU(N)$  |
| Gravité |  $SO(1,3)$  |
| SUGRA | Super-Poincaré |



5) 🔷 Passage à 10D : supercordes




🔹 Pourquoi 10D ?


annulation des anomalies :

$$
D=10
$$



🔹 Types


| théorie | groupe |
| --- | --- |
| Type I | SO(32) |
| IIA | non-chirale |
| IIB | chirale |
| hétérotique |  $E_8 \times E_8$  |



🔹 Champs


*   métrique  $g$ 
*   2-forme  $B$ 
*   dilaton  $\phi$ 



🔹 Courbure généralisée


$$
H = dB + \text{corrections}
$$



6) 🔷 Théorie M (11D)



🔹 Supergravité 11D


champ fondamental :

$$
\boxed{ (g_{\mu\nu}, \psi_\mu, C_{\mu\nu\rho}) }
$$



🔹 3-forme


$$
\boxed{ G_4 = dC_3 }
$$



🔹 Action


$$
S = \int d^{11}x \sqrt{-g} R - \frac{1}{2} |G_4|^2 - C_3 \wedge G_4 \wedge G_4
$$



🔥 Structure profonde


| objet | rôle |
| --- | --- |
|  $C_3$  | champ de jauge généralisé |
|  $G_4$  | courbure |
| branes | sources |



7) 🔷 Hiérarchie complète




🔥 Vue unifiée


$$
\boxed{ \begin{aligned} \text{EM} &: A \\ \text{YM} &: A \\ \text{GR} &: (e,\omega) \\ \text{SUGRA} &: (e,\omega,\psi) \\ \text{M} &: (g,\psi,C_3) \end{aligned} }
$$



8) 🔷 Interprétation géométrique ultime




🔹 Tout est une connexion


$$
\boxed{ \text{Physique} = \text{géométrie de fibrés} }
$$



🔹 Courbures généralisées


$$
F,\quad R,\quad G_4
$$



🔹 Identités


$$
DF=0,\quad DR=0,\quad dG_4=0
$$


9) 🔷 Intuition finale

🔥 supersymétrie


$$
\boxed{ \text{bosons} \leftrightarrow \text{fermions} }
$$



🔥 supergravité


$$
\boxed{ \text{gravité + SUSY locale} }
$$



🔥 théorie M


$$
\boxed{ \text{unification géométrique ultime (11D)} }
$$

$$
(\omega + e + \psi)\wedge(\omega + e + \psi)
$$

</details>

                        ┌───────────────┐
                        │      X        │
                        │ bosonique     │
                        └───────────────┘
                               │
                               ▼
                    Puissances : X, X², X³, ...
                    [X, X^n\} = 0 pour tout n
                               │
                               ▼
                         Commute toujours

─────────────────────────────────────────────────────────────

                        ┌───────────────┐
                        │      X        │
                        │ fermionique   │
                        │ général       │
                        └───────────────┘
                               │
                               ▼
                    Puissances : X, X², X³, X⁴, ...
                    [X, X^1\} = 2 X²
                    [X, X^2\} = X X² - X² X
                    [X, X^3\} = X X³ + X³ X
                    [X, X^4\} = X X⁴ - X⁴ X
                               │
                               ▼
                  Ne simplifie pas naïvement ± 2 X^{n+1}
                  Dépend du produit exact (super-algèbre)

─────────────────────────────────────────────────────────────

                        ┌───────────────┐
                        │      X        │
                        │ fermionique   │
                        │ nilpotent     │
                        │ (X² = 0)     │
                        └───────────────┘
                               │
                               ▼
                    Puissances : X, 0, 0, 0, ...
                    [X, X^1\} = 2 X² = 0
                    [X, X^2\} = 0
                    [X, X^3\} = 0
                    [X, X^n≥2\} = 0
                               │
                               ▼
                      Tout super-commutateur nul
                      (très pratique en supersymétrie)

- **Courbure de Lorentz** $R^{ab}$ (2-forme) :
$$
R^{ab} \;=\; d\omega^{ab} + \omega^a{}_c\wedge \omega^{cb}.
$$
- **Torsion super-symmétrique** $T^a$ (2-forme) : 
$$
T^a \;=\; D e^a \;-\;\tfrac12\,\bar\psi\wedge\gamma^a\psi 
\;=\; de^a + \omega^a{}_b\wedge e^b \;-\;\tfrac12\,\bar\psi\wedge\gamma^a\psi.
$$
Le terme fermionique $-\tfrac12\,\bar\psi\wedge\gamma^a\psi$ provient du crochet anticommutateur $\{Q,Q\}\sim \gamma^aP_a$ de l’algèbre super-Poincaré. 

- **Courbure du gravitino** $\rho$ (2-forme) : 
$$
\rho = D\psi \;=\; d\psi + \tfrac14\,\omega^{ab}\wedge \gamma_{ab}\,\psi,
$$
où $D\psi$ est la dérivée covariante spinorielle. 

On peut écrire globalement :
$$
\boxed{\mathcal F \;=\; \tfrac12\,R^{ab}J_{ab} \;+\; T^aP_a \;+\;  \bar\rho\,Q},
$$
ce qui regroupe torsion, courbure de spin et super-courbure du gravitino. 

# Identités de Bianchi (principe général)

Dans toute théorie de jauge, le fait que $\mathcal F=d\mathcal A+\mathcal A\wedge\mathcal A$ implique une identité de **Bianchi généralisée** : la dérivée covariante de la courbure s’annule identiquement. Autrement dit, en notant $D=\;d+[\mathcal A,\cdot]$ la dérivée covariante associée à $\mathcal A$, on a toujours

$$
D\mathcal F = d\mathcal F + [\mathcal A,\mathcal F] \;=\;0.
$$

Cette formule (facteur de Jacobi) n’est pas une équation du mouvement mais une conséquence **géométrique** du fait que $D^2$ agit par commutateur sur les formes. On peut citer notamment :  

> **Théorème (Bianchi)** – Pour toute connexion $\mathcal A$ sur un fibré principal, la courbure $\mathcal F$ satisfait $D\mathcal F=0$【37†L2537-L2544】. 

En pratique, en projetant cette identité sur chaque générateur on obtient : 
- $DR^{ab}=0$ (courbure de Lorentz coïncide avec celle d’une connexion),  
- $DT^a = R^a{}_b\wedge e^b \;-\;\bar\psi\wedge\gamma^a\rho$ (torsion couplée à la fermionique),  
- $D\rho = \tfrac14 R^{ab}\wedge \gamma_{ab}\psi$.  

En forme locale, pour tout champ de jauge $A$, cela se traduit par  
$$
dF + [A,F] = 0 \quad\Longleftrightarrow\quad D F = 0,
$$ 
avec $F=dA+A\wedge A$. Ainsi pour l’électromagnétisme ou la Yang–Mills, on a $dF=0$ (ou $DF=0$) comme identité de Bianchi.

# Actions et équations du mouvement

Nous passons maintenant aux actions invariantes et à l’application du principe variationnel, dans les trois cas principaux :

- **Électromagnétisme (U(1))** : la connexion $A$ est un 1-forme abélienne, $F=dA$. L’action de Maxwell usuelle est 
  $$
  S_{\rm EM} = -\tfrac14\int F\wedge *F + \int A\wedge *J.
  $$
  Les équations de Maxwell qui en résultent (en présence d’un courant de charge $J$) sont  
  $$
  dF = 0, \qquad d * F = J.
  $$
  La première ( $dF=0$ ) est précisément l’identité de Bianchi (ici triviale puisque $F=dA$). La seconde est l’équation d’inhomogène, obtenue par variation de $S$ par rapport à $A$.

- **Yang–Mills (groupe non abélien $G$)** : la connexion $A$ est à valeurs dans $\mathfrak g$, et $F=dA + A\wedge A$. L’action standard est 
  $$
  S_{\rm YM} = -\frac14\int \mathrm{Tr}(F\wedge *F).
  $$
  En variant $S_{\rm YM}$ on obtient les équations de Yang–Mills couplées à une source $J$ (courant de couleur) :
  $$
  DF = 0 \quad(\text{Bianchi identique}), 
  \qquad D * F = J,
  $$
  où $D*F = d*F + [A,*F]$. Ici encore $DF=0$ est l’identité de Bianchi intégrable (générale) et $D*F=J$ est l’équation d’inhomogène du mouvement. 

- **Gravité (formalisme de Cartan)** : on traitera $e^a$ et $\omega^{ab}$ comme champs indépendants (*formalisme première ordre*). L’action d’Einstein–Hilbert avec constante cosmologique $\Lambda$ s’écrit en formes :
  $$
  S_{\rm EH} = \frac{1}{16\pi G}\int \epsilon_{abcd}\Bigl(e^a\wedge e^b\wedge R^{cd} + \frac{\Lambda}{6}\,e^a\wedge e^b\wedge e^c\wedge e^d\Bigr).
  $$
  On peut ajouter l’action des champs supplémentaires (matière, Maxwell, etc.) pour générer le tenseur énergie-impulsion $T_{\mu\nu}$. La variation s’effectue en deux étapes : 

  1. **Variation en $\omega^{ab}$** : on utilise $\delta R^{ab}=D(\delta\omega^{ab})$. Après intégration par parties, on obtient l’équation $T^a=0$ (torsion nulle) : le champ $\omega$ devient la connexion de Levi-Civita.  
  2. **Variation en $e^a$** : on obtient l’équation équivalente à $G_{ab} + \Lambda\,g_{ab} = 8\pi G\,T_{ab}$. Formellement :  
     $$
     \epsilon_{abcd}\Bigl(e^b\wedge R^{cd} + \Lambda\,e^b\wedge e^c\wedge e^d\Bigr) = 8\pi G\,\tau_a,
     $$
     qui se traduit sous forme tensorielle par 
     $$
     R_{\mu\nu}-\frac12R\,g_{\mu\nu}+\Lambda g_{\mu\nu} = 8\pi G\,T_{\mu\nu}.
     $$
     Cette équation d’Einstein avec $\Lambda$ est la conséquence du principe variationnel【12†L531-L536】. 

En résumé, on retrouve ainsi dans chaque cas que la partie homogène est l’identité de Bianchi ($dF=0$ ou $DF=0$), et la partie inhomogène provient de la variation de l’action. Pour l’Electromagnétisme : $d*F=J$. Pour Yang–Mills : $D*F=J$. Pour la gravité : équation d’Einstein $G+\Lambda g=8\pi G\,T$ (avec torsion nulle). 

# Géométrie de Cartan et fibrés principaux

Pour être complet, on peut formuler tout ce qui précède rigoureusement via la géométrie des fibrés principaux. On considère un fibré principal $P\to M$ de groupe $G$ (par exemple $G=\mathrm{SO}(1,3)$ ou $G=\mathrm{Poincaré}$ ou une extension supersymétrique). Une **connexion** sur $P$ est une 1-forme $\Omega\in\Omega^1(P,\mathfrak g)$ satisfaisant des propriétés d’équvariance. Le champ local $A$ sur la base $M$ est son pullback par une section locale. La courbure $\Omega$ vérifie l’**équation structurelle de Cartan** $\Omega = d_P\omega + \omega\wedge\omega$. 

Les identités de Bianchi découlent alors du fait que $D_P\Omega=0$ sur $P$【37†L2512-L2518】. En revenant sur la base $M$ (pullback local), ceci donne $DF=dF+[A,F]=0$【37†L2537-L2544】, s’écrivant explicitement $dF= -[A,F]$. Dans nos exemples :  
- Pour $G=U(1)$, $DF=dF=0$ exactement.  
- Pour $G$ non abélien, $DF=0$ signifie $dF + [A,F]=0$.  
- Pour la connexion de gravité (Cartan-Poincaré), on a les **équations de structure de Cartan** :
  $$
  T^a = de^a + \omega^a{}_b\wedge e^b, 
  \quad R^{ab} = d\omega^{ab} + \omega^a{}_c\wedge\omega^{cb},
  $$
  et les Bianchi correspondantes : $DT^a = R^a{}_b\wedge e^b$, $DR^{ab}=0$. 

La géométrie de Cartan généralise la géométrie riemannienne : on se donne un **espace modèle homogène** $G/H$ (e.g. Minkowski, de Sitter, Anti-de Sitter) et un fibré principal $H\to P\to M$ (structure locale de $G/H$). Une **connexion de Cartan** est une $\mathfrak g$-valeur combinant la coframe $e^a$ (dans $\mathfrak g/\mathfrak h$) et la connexion $\omega^{ab}$ (dans $\mathfrak h$).  Par exemple, $\mathfrak g = \mathfrak{so}(1,4)$ pour AdS ou $\mathfrak{osp}(1|4)$ en supergravité AdS.

# Formulation de MacDowell–Mansouri (AdS)

Dans la version **MacDowell–Mansouri** de la gravité (et supergravité AdS), on combine $e^a$ et $\omega^{ab}$ en une **connexion unique du groupe de symétrie** (par exemple $SO(2,3)$ ou son extension supersymétrique). Derek Wise souligne que « la géométrie de Cartan donne un sens géométrique clair à l’astuce de MacDowell–Mansouri qui consiste à combiner la connexion de Levi-Civita et la coframe en un seul champ physique »【49†L53-L61】. En pratique, on choisit un groupe $G$ plus grand (comme $SO(2,3)$ ou $OSp(1|4)$) de dimension de Lie $\mathfrak g$ contenant la Lorentz comme sous-groupe $H$. La connexion globale $A$ de $G$-fibré s’écrit (par exemple en AdS) 
$$
A = \omega^{ab}J_{ab} + \frac{1}{\ell}\,e^a P_a + \cdots,
$$
et la courbure associe contient le "torsion" et la courbure de Lorentz « boostées ». L’action de MacDowell–Mansouri est construite à partir de la projection du carré de cette courbure dans $\mathfrak h$, ce qui reproduit Einstein+Λ. Cela met en évidence l’analogie : **gravité** = théorie de jauge d’un groupe homogène, avec connexion de Cartan. 

# Liens vers 11D et la forme $C$

En supergravité 11 dimensions (11D SUGRA), on ajoute au spectre le fameux **potentiel 3-forme** $C$ (à la différence du simple $(e,\omega,\psi)$ de 4D). En effet, la théorie de Cremmer–Julia–Scherk contient un **tenseur de champ** $C_{\mu\nu\rho}$ dont la 4-forme de champ $G=dC$ apparaît dans les équations. Wikipédia résume : *« Elle contient un graviton, un gravitino et un champ de jauge 3-forme, leurs interactions étant déterminées par la supersymétrie »*【45†L120-L124】. Ce champ 3-forme n’est pas inclut comme connexion sur un groupe simple, mais on peut le voir via des algèbres étendues ou l’approche de D’Auria–Fré, ou encore via des formulismes Chern–Simons (cf. Troncoso–Zanelli pour $OSp(32|1)$ en D=11【2†L53-L61】). L’existence de $C$ relie 11D SUGRA à la théorie-M, où le "C-field" joue un rôle central. 

# Synthèse

- **Connexions de jauge** $\mathcal A$ englobent EM, YM et Gravité (ainsi que leurs versions supersymétriques).  
- La **courbure** $\mathcal F=d\mathcal A+\mathcal A\wedge\mathcal A$ donne les champs de force (F, R, T, ρ, …).  
- Les **identités de Bianchi** $D\mathcal F=0$ sont géométriques (Cartan)【37†L2537-L2544】.  
- Les **actions** invariantes conduisent, par variation, à :  
  - $dF=0,\ d*F=J$ pour Maxwell (source $J$),  
  - $DF=0,\ D*F=J$ pour Yang–Mills,  
  - $G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T_{\mu\nu}$ (avec torsion nulle) pour Einstein–Hilbert【12†L531-L536】.  
- En version **Cartan** sur fibrés, la gravité est vue comme un champ de jauge (connexion) d’un groupe homogène. MacDowell–Mansouri combine le vielbein et la spin-connexion en un seul champ de connexion géométrique【49†L53-L61】.  
- En 11D SUGRA apparaît en plus le **champ 3-forme** $C$ (fait reconnaître comme champ de jauge de haut rang)【45†L120-L124】, ouvrant la voie à la théorie-M.

Ainsi, d’une connexion généralisée $\mathcal A$ et de $F=d\mathcal A+\mathcal A^2$ on extrait l’ensemble des champs classiques (torsion, courbure, forces de jauge…) et, via l’invariance de jauge et l’action géométrique, les équations de la physique (Maxwell, Yang–Mills, Einstein, Rarita–Schwinger, etc.). Les identités de Bianchi proviennent simplement du fait que $d^2=0$ (ou $D^2=[F,\cdot]$)【37†L2512-L2518】【37†L2537-L2544】. 

**Sources :** Traitements standards de la géométrie de jauge et de la supergravité (voir notamment les sections Cartan et superconnexion dans les ouvrages de Freedman–Van Proeyen, Townsend, Van Nieuwenhuizen) et références en géométrie (voir par ex. 【37†L2512-L2518】【12†L531-L536】【41†L5579-L5582】【49†L53-L61】【45†L120-L124】).