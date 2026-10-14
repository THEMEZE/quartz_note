#!/usr/bin/env python3

import subprocess
from collections import defaultdict


def git(*args):
    """Exécute une commande Git et retourne sa sortie."""
    return subprocess.check_output(
        ["git", *args],
        text=True,
        stderr=subprocess.DEVNULL,
    ).strip()


def main():
    # Vérifie que l'on est dans un dépôt Git
    try:
        git("rev-parse", "--is-inside-work-tree")
    except subprocess.CalledProcessError:
        print("Erreur : ce dossier n'est pas un dépôt Git.")
        return

    # Récupère les branches distantes et locales
    print("Synchronisation des références distantes...")
    subprocess.run(
        ["git", "fetch", "--all", "--prune"],
        check=False,
    )

    branches = git(
        "for-each-ref",
        "--format=%(refname:short)",
        "refs/heads",
        "refs/remotes",
    ).splitlines()

    # Élimine les références symboliques du type origin/HEAD
    branches = [
        b for b in branches
        if not b.endswith("/HEAD")
    ]

    if not branches:
        print("Aucune branche trouvée.")
        return

    # HEAD actuel
    current = git("branch", "--show-current")

    # Identifie les commits de chaque branche
    commits = {}
    for branch in branches:
        try:
            commits[branch] = set(
                git("rev-list", branch).splitlines()
            )
        except subprocess.CalledProcessError:
            continue

    branches = list(commits)

    # Nombre total de commits accessibles et commits uniques
    print("\n=== RÉSUMÉ DES BRANCHES ===\n")

    for branch in sorted(
        branches,
        key=lambda b: len(commits[b]),
        reverse=True,
    ):
        unique = len(
            commits[branch]
            - set().union(
                *(commits[b] for b in branches if b != branch)
            )
        )

        marker = "  <-- branche courante" if branch == current else ""
        print(
            f"{branch:30} "
            f"{len(commits[branch]):5} commits "
            f"{unique:5} commits uniques{marker}"
        )

    # Relation entre chaque paire de branches
    print("\n=== RELATIONS ENTRE BRANCHES ===\n")

    for i, a in enumerate(sorted(branches)):
        for b in sorted(branches)[i + 1:]:
            only_a = commits[a] - commits[b]
            only_b = commits[b] - commits[a]

            if not only_a and not only_b:
                relation = "identiques"
            elif not only_a:
                relation = f"{b} contient {a}"
            elif not only_b:
                relation = f"{a} contient {b}"
            else:
                relation = "divergentes"

            print(
                f"{a} <-> {b} : "
                f"{len(only_a)} spécifiques à {a}, "
                f"{len(only_b)} spécifiques à {b} "
                f"=> {relation}"
            )

    # Graphe visuel des branches et des commits
    print("\n=== ARBRE DES COMMITS ===\n")
    subprocess.run([
        "git", "log",
        "--graph",
        "--oneline",
        "--decorate",
        "--all",
        "--date-order",
        "-40",
    ])

    # Analyse des branches maximales selon l'inclusion des commits
    maximal = [
        b for b in branches
        if not any(
            commits[b] < commits[other]
            for other in branches
        )
    ]

    print("\n=== CONCLUSION ===\n")

    if len(maximal) == 1:
        print(f"Branche la plus avancée : {maximal[0]}")
        print("Elle contient tous les commits des autres branches.")
    else:
        print("Plusieurs branches maximales :")
        for branch in maximal:
            print(
                f"  - {branch} "
                f"({len(commits[branch])} commits accessibles)"
            )
        print(
            "Ces branches ne sont pas toutes incluses les unes "
            "dans les autres. Il faut examiner le graphe avant "
            "de choisir une branche de référence."
        )


if __name__ == "__main__":
    main()

