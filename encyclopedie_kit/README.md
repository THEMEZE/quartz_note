# Kit encyclopédie
1. Dézipper à la racine du projet Quartz (là où il y a `content/` et `quartz/`). Aucune de tes notes n'est modifiée.
2. Ouvrir `content/Encyclopédie/Accueil.md`.
3. Structure : `graphe.txt` (nœuds, prérequis, parcours) · `contenu/<Titre>.md` (texte rédigé d'une fiche) · `build.py` (génère tout).
4. Rédiger ou corriger une fiche : éditer `contenu/<Titre>.md`, puis `python3 encyclopedie_kit/build.py --vault content`.
   Une fiche avec un fichier `contenu/` passe en statut « rédigé (à relire) ».
5. Pour éditer une fiche directement dans Obsidian à la place, supprimer `generated: true` dans son en-tête : le script ne l'écrasera plus.
6. `Rapport de cohérence.md` signale cycles, niveaux incohérents et sources introuvables.
