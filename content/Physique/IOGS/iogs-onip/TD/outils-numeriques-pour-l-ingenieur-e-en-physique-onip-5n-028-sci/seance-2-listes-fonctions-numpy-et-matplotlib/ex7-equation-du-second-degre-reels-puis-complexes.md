---
title: "Exercice 7 — Équation du second degré : réels puis complexes"
tags:
  - td
  - outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci
---

[[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/index|⬅ Retour]] · <a href="/pdfs/td2_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 7. Équation du second degré : réels puis complexes *(facultatif)*

On veut résoudre l'équation $a x^2 + b x + c = 0$. \\
1. Écrire une fonction \texttt{racines\_reelles(a, b, c)} pour $a$, $b$,
   $c$ réels, qui renvoie les racines réelles (aucune, une ou deux). \\
2. Écrire une fonction \texttt{racines(a, b, c)} qui renvoie toutes les
   racines dans $\mathbb{C}$ (module \texttt{cmath}), y compris lorsque
   $\Delta < 0$. \\
3. Faire fonctionner cette fonction avec $a$, $b$, $c$ eux-mêmes
   complexes, et traiter le cas $a = 0$. \\
4. Vérifier les résultats en calculant $|a x^2 + b x + c|$ pour chaque
   racine trouvée. \\
5. Écrire une version vectorisée avec Numpy, résolvant plusieurs
   équations d'un coup.

**q1.** Écrire \texttt{racines\_reelles(a, b, c)} et la tester sur
$x^2 - 3x + 2$, $x^2 + 2x + 1$ et $x^2 + x + 1$.

> [!tip]- 💡 Coup de pouce
> Trois cas selon le signe de $\Delta$ ; la racine carrée d'un réel
> positif s'écrit \texttt{delta**0.5}.


> [!success]- ✅ Correction
> Racines 1 et 2 ; racine double -1 ; aucune racine reelle.


> [!example]- 📝 Solution détaillée
> **Implémentation**
>
> Voir le code ci-dessus.


**q2.** Écrire \texttt{racines(a, b, c)} avec \texttt{cmath}, et la
tester sur $x^2 + 1$ et $x^2 + x + 1$.

> [!tip]- 💡 Coup de pouce
> Remplacer \texttt{delta**0.5} par \texttt{cmath.sqrt(delta)} :
> plus besoin de distinguer le signe de $\Delta$.


> [!success]- ✅ Correction
> x**2 + 1 : racines +i et -i ; x**2 + x + 1 : (-1 +- i*sqrt(3))/2.


> [!example]- 📝 Solution détaillée
> **Résultat**
>
> Pour $x^2 + 1$ : $\pm i$. Pour $x^2 + x + 1$ :
> $\dfrac{-1 \pm i\sqrt{3}}{2}$, soit environ $-0{,}5 \pm 0{,}866\,i$.


**q3.** Tester avec des coefficients complexes : $x^2 - (3+i)x + (2+2i) = 0$,
puis la même équation multipliée par $i$. Que constate-t-on ?
Traiter aussi $a = 0$.

> [!tip]- 💡 Coup de pouce
> Multiplier une équation par un complexe non nul ne change pas ses
> racines. Pour $a = 0$, l'équation est du premier degré.


> [!success]- ✅ Correction
> Racines 2 et 1+i dans les deux cas ; pour a = 0 : x = -c/b.


> [!example]- 📝 Solution détaillée
> **Interprétation**
>
> Les deux équations ont les mêmes racines, $2$ et $1+i$. Pour
> $a = 0$, on renvoie $-c/b$ (et on lève une erreur si aussi
> $b = 0$).


**q4.** Vérifier chaque solution en calculant $|a x^2 + b x + c|$.

> [!tip]- 💡 Coup de pouce
> Le résultat doit être nul à l'erreur d'arrondi près (de l'ordre de
> $10^{-16}$).


> [!success]- ✅ Correction
> Residus de l'ordre de 1e-16 ou nuls.


> [!example]- 📝 Solution détaillée
> **Vérification**
>
> Voir \texttt{verifie} ci-dessus : les résidus sont nuls ou de
> l'ordre de $10^{-16}$, ce qui valide les racines.


**q5.** Écrire une version vectorisée résolvant trois équations à la fois
avec des tableaux Numpy.

> [!tip]- 💡 Coup de pouce
> Convertir les entrées en complexes avec \texttt{dtype=complex} pour
> que \texttt{np.sqrt} accepte les discriminants négatifs.


> [!success]- ✅ Correction
> np.sqrt sur un tableau complexe ; comparer avec np.roots.


> [!example]- 📝 Solution détaillée
> **Implémentation**
>
> Voir \texttt{racines\_np} ci-dessus. Sans \texttt{dtype=complex},
> \texttt{np.sqrt} renverrait \texttt{nan} pour un discriminant
> négatif.


> [!note] 🔗 Voir aussi
> [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex2-fonction-texttt-get-list-et-mesure-du-temps-d-execution|Exercice 2 — Fonction \texttt{get\_list} et mesure du temps d'exécution]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex3-generation-d-un-vecteur-avec-numpy-vectorisation|Exercice 3 — Génération d'un vecteur avec Numpy : vectorisation]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex4-generation-de-signaux-et-affichage-avec-matplotlib|Exercice 4 — Génération de signaux et affichage avec matplotlib]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex5-fonction-porte-indexation-booleenne-numpy|Exercice 5 — Fonction porte : indexation booléenne Numpy]]

