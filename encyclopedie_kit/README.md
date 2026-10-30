# Kit encyclopédie

1. Dézipper à la racine du projet Quartz (là où il y a `content/` et `quartz/`).
2. Ouvrir `content/Encyclopédie/Accueil.md` dans Obsidian. Rien d'autre n'a été modifié dans le vault.
3. Pour faire évoluer le graphe, éditer **uniquement** `encyclopedie_kit/graphe.txt`, puis :
   `python3 encyclopedie_kit/build.py --vault content`
   (regénère les fiches, les parcours, `Rapport de cohérence.md` et `quartz/static/explorer.html`).
4. Une fiche générée porte `generated: true`. Dès que tu rédiges dedans, **supprime cette ligne** : le script ne l'écrasera plus jamais.
5. Quartz : `npx quartz build --serve` ; la page `Carte interactive` affiche l'explorateur (iframe vers `/static/explorer.html`). Si le site est sous un sous-chemin, changer `BASE` en haut du script de `explorer.tpl.html`.
