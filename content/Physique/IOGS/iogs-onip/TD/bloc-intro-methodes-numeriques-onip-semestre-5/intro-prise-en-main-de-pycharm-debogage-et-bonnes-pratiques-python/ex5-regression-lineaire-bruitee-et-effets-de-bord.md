---
title: "Exercice 5 — Régression linéaire bruitée et effets de bord"
tags:
  - td
  - bloc-intro-methodes-numeriques-onip-semestre-5
---

[[physique/IOGS/iogs-onip/TD/bloc-intro-methodes-numeriques-onip-semestre-5/intro-prise-en-main-de-pycharm-debogage-et-bonnes-pratiques-python/index|⬅ Retour]] · <a href="/pdfs/td1_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 5. Régression linéaire bruitée et effets de bord

On fournit \texttt{linear\_regression\_and\_noise0.py}, qui ajoute du
bruit à des données idéales, effectue une régression linéaire avec
scikit-learn, puis affiche le résultat pour sept niveaux de bruit
croissants. Le script ne plante pas, mais son graphique est trompeur :
le bruit affiché semble s'accumuler d'un niveau à l'autre.

**q1.** Exécuter \texttt{linear\_regression\_and\_noise0.py}. Comparer
visuellement l'allure du nuage de points affiché pour le niveau de
bruit « 0.5 » et celui affiché pour le niveau « 10 ». Que
remarquez-vous d'anormal si l'on observe successivement toutes les
figures produites ?

> [!tip]- 💡 Coup de pouce
> La variable \texttt{y} est-elle réinitialisée à chaque appel de la
> fonction, ou réutilisée telle qu'elle a été laissée par l'appel
> précédent ?


> [!success]- ✅ Correction
> Le bruit affiché à chaque niveau contient en réalité la somme de tous les bruits précédents.


> [!example]- 📝 Solution détaillée
> **Diagnostic de l'accumulation**
>
> La ligne \texttt{y += noise} modifie \texttt{y} en place. Comme
> la même variable \texttt{y}, définie une seule fois avant la
> boucle, est passée à chaque appel de
> \texttt{plot\_linear\_regression\_with\_noise}, chaque appel
> ajoute son propre bruit à un \texttt{y} déjà modifié par les
> appels précédents : le bruit s'accumule d'un niveau au suivant,
> au lieu de repartir des données idéales à chaque fois.


**q2.** Le graphique légendé « Noisy data » affiche-t-il vraiment les
données bruitées, ou autre chose ? Justifier en suivant la
succession des affectations à la variable \texttt{y} dans la
fonction.

> [!tip]- 💡 Coup de pouce
> Repérez toutes les lignes où \texttt{y} apparaît à gauche du signe
> \texttt{=} (ou de \texttt{+=}) à l'intérieur de la fonction.


> [!success]- ✅ Correction
> y est réaffecté à model.predict(...) avant le tracé : le scatter affiche la prédiction, pas le bruit.


> [!example]- 📝 Solution détaillée
> **Traçage des affectations**
>
> Dans la fonction originale, \texttt{y} désigne successivement :
> (1) les données idéales bruitées (après \texttt{y += noise}),
> puis (2) les valeurs prédites par le modèle (après
> \texttt{y = model.predict(x\_reshaped)}). Le
> \texttt{plt.scatter(x, y, ..., label='Noisy data ...')} est
> exécuté *après* cette seconde affectation : il affiche donc
> la prédiction du modèle, superposée avec la droite de régression
> elle-même tracée juste après — le nuage « bruité » légendé n'a
> en réalité plus rien de bruité.


**q3.** Corriger les deux problèmes en introduisant des noms de variables
distincts pour les données idéales, les données bruitées et la
prédiction du modèle. Vérifier que chaque sous-figure ne contient
plus que le bruit correspondant à son propre niveau.

> [!tip]- 💡 Coup de pouce
> Une seule règle suffit : ne jamais réaffecter (ni modifier en place)
> une variable qui doit encore servir de référence pour les appels
> suivants.


> [!success]- ✅ Correction
> Introduire \texttt{y\_noisy = y + noise et y\_predicted = model.predict(...)} sans jamais modifier y.


> [!example]- 📝 Solution détaillée
> **Correction**
>
> En remplaçant \texttt{y += noise} par
> \texttt{y\_noisy = y + noise} (nouvelle variable, \texttt{y}
> inchangé) et \texttt{y = model.predict(...)} par
> \texttt{y\_predicted = model.predict(...)}, chaque appel repart
> bien des données idéales d'origine : les sept sous-figures
> affichent alors chacune un bruit indépendant, cohérent avec son
> propre niveau, et un nuage de points réellement bruité distinct
> de la droite de régression.


> [!note] 🔗 Voir aussi
> [[physique/IOGS/iogs-onip/TD/bloc-intro-methodes-numeriques-onip-semestre-5/intro-prise-en-main-de-pycharm-debogage-et-bonnes-pratiques-python/ex3-tri-a-bulles-texttt-bubble-sort-et-mutation-en-place|Exercice 3 — Tri à bulles (\texttt{bubble\_sort}) et mutation en place]]

