#!/usr/bin/env python3
"""Génère l'encyclopédie (Obsidian/Quartz) depuis graphe.txt, valide le graphe, et produit l'explorateur interactif.
Usage : python3 build.py --vault ./content [--out ./content/Encyclopédie] [--static ./quartz/static]
Sûr : ne réécrit que les fichiers portant `generated: true`. Tes notes ne sont jamais modifiées."""
import re, os, sys, json, unicodedata, argparse, collections
nfc = lambda s: unicodedata.normalize('NFC', s)
ap = argparse.ArgumentParser()
ap.add_argument('--vault', default='content'); ap.add_argument('--out'); ap.add_argument('--static')
ap.add_argument('--graph', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'graphe.txt'))
a = ap.parse_args()
vault = a.vault; out = a.out or os.path.join(vault, 'Encyclopédie'); static = a.static or os.path.join(os.path.dirname(os.path.abspath(vault)), 'quartz', 'static')
NIV = {1: 'Fondations (L1)', 2: 'Licence (L2–L3)', 3: 'Master 1', 4: 'Master 2', 5: 'Doctorat'}
STAT = {0: 'à rédiger', 1: 'partiel'}

# ---------- lecture du graphe ----------
doms, nodes, paths, order = [], {}, [], []
cur = None
for ln in open(a.graph, encoding='utf-8'):
    ln = ln.rstrip('\n')
    if not ln.strip() or ln.startswith('#'): continue
    if ln.startswith('@'):
        k, n = [x.strip() for x in ln[1:].split('|')]; doms.append((k, n)); cur = k; continue
    f = ln.split('|')
    if f[0] == 'P':
        paths.append(dict(k=f[1], n=f[2], o=f[3], s=[x for x in f[4].split(';') if x])); continue
    f += [''] * (7 - len(f)); sp = lambda x: [y.strip() for y in x.split(';') if y.strip()]
    t = f[1].strip()
    assert t not in nodes, f'doublon {t}'
    nodes[t] = dict(ty=f[0], t=t, d=cur, n=int(f[2]), p=sp(f[3]), r=sp(f[4]), src=sp(f[5]), s=f[6].strip()); order.append(t)

# ---------- index du vault ----------
idx = {}
for r, _, fs in os.walk(vault):
    for fn in fs:
        if fn.endswith('.md'):
            rel = nfc(os.path.relpath(os.path.join(r, fn), vault))[:-3]
            if rel.startswith(nfc(os.path.relpath(out, vault))): continue
            idx[rel] = os.path.basename(rel)
def resolve(tok):
    anc = ''
    if '#' in tok: tok, anc = tok.split('#', 1)
    tok = nfc(tok)
    if tok.startswith('/'):
        c = [r for r in idx if r.endswith(tok + '/index')]
    else:
        c = [r for r, s in idx.items() if s == tok] or sorted(r for r, s in idx.items() if s.startswith(tok))
    if not c: return None
    r = c[0]
    return f"[[{r}{'#' + anc if anc else ''}|{idx[r][:55] + ('#' + anc[:30] if anc else '')}]]"

# ---------- validation ----------
warn = []
for t, n in nodes.items():
    for x in n['p'] + n['r']:
        if x not in nodes: warn.append(f'ERREUR  {t} : référence inconnue « {x} »')
    for x in n['p']:
        if x in nodes and nodes[x]['n'] > n['n']: warn.append(f'niveau   {t} (n{n["n"]}) a pour prérequis {x} (n{nodes[x]["n"]}) : prérequis plus avancé')
    n['res'] = [r for r in (resolve(s) for s in n['src']) if r]
    for s in n['src']:
        if not resolve(s): warn.append(f'source   {t} : « {s} » introuvable dans le vault')
col = {}
def dfs(t, st):
    col[t] = 1; st.append(t)
    for p in nodes[t]['p']:
        if p not in nodes: continue
        if col.get(p) == 1: warn.append('ERREUR  cycle de prérequis : ' + ' → '.join(st[st.index(p):] + [p]))
        elif p not in col: dfs(p, st)
    col[t] = 2; st.pop()
for t in nodes: 
    if t not in col: dfs(t, [])
for p in paths:
    pos = {t: i for i, t in enumerate(p['s'])}; p['sup'] = []
    for i, t in enumerate(p['s']):
        if t not in nodes: warn.append(f'ERREUR  parcours {p["k"]} : « {t} » inconnu'); continue
        for q in nodes[t]['p']:
            if q not in pos: 
                if q not in p['sup']: p['sup'].append(q)
            elif pos[q] > i: warn.append(f'ordre    parcours {p["k"]} : {q} doit venir avant {t}')
        nodes[t].setdefault('paths', []).append(p['k'])
out_of = collections.defaultdict(list)
for t, n in nodes.items():
    for q in n['p']: out_of[q].append(t)

# ---------- nommage / liens ----------
def fn(t): return re.sub(r'[\\/:*?"<>|]', '-', t)
stems = set(idx.values())
for t, n in nodes.items():
    n['file'] = fn(t) + (' (fiche)' if fn(t) in stems else '')
    n['dir'] = 'Chapitres' if n['ty'] == 'C' else 'Notions'
def L(t):
    if t not in nodes: return f'[[{t}]]'
    n = nodes[t]; return f"[[{n['file']}|{t}]]" if n['file'] != t else f"[[{t}]]"
q = lambda x: '"' + x.replace('"', '\\"') + '"'
dname = dict(doms)

def write(path, txt):
    path = os.path.join(out, path); os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path) and 'generated: true' not in open(path, encoding='utf-8').read(2000):
        warn.append(f'protégé  {path} existe et n\'est pas généré : non écrasé'); return
    open(path, 'w', encoding='utf-8').write(txt)

# ---------- pages nœuds ----------
for t in order:
    n = nodes[t]; st = 1 if n['res'] else 0; n['st'] = st
    pl = [p['k'] for p in paths if t in p['s']]
    fm = ['---', f'title: {q(t)}', f'type: {"chapitre" if n["ty"] == "C" else "notion"}', f'domaine: {q(dname[n["d"]])}',
          f'niveau: {n["n"]}', f'niveau_label: {q(NIV[n["n"]])}', f'status: {STAT[st]}', 'generated: true']
    for k, v in (('prerequisites', [L(x) for x in n['p']]), ('related', [L(x) for x in n['r']]), ('sources', n['res']),
                 ('paths', [f'[[Parcours {p}]]' for p in pl])):
        fm += [f'{k}:'] + [f'  - {q(x)}' for x in v] if v else [f'{k}: []']
    fm += ['tags:', '  - encyclopedie', f'  - {n["ty"] == "C" and "chapitre" or "notion"}', '---', '']
    b = [f'# {t}', '', f'> [!abstract] {n["s"] or "À rédiger"}', f'> **{dname[n["d"]]}** · niveau {n["n"]} ({NIV[n["n"]]}) · statut : {STAT[st]}', '']
    b += ['## Prérequis', ''] + ([f'- {L(x)} (n{nodes[x]["n"]})' for x in n['p']] or ['- aucun']) + ['']
    if n['res']:
        b += ['## Contenu déjà rédigé', ''] + [f'- {x}' for x in n['res']] + ['']
    if n['file'] != t and t in stems:
        b += [f'> [!note] Note de référence existante : [[{t}]]', '']
    if n['ty'] == 'C':
        b += ['## Plan type (à adapter)', '',
              '1. **Cadre et conventions** : espaces, métrique, notations, signes.',
              '2. **Énoncés** : théorèmes en callouts `>[!tip]+`, hypothèses explicites.',
              '3. **Démonstrations** : complètes, repliées `>[!note]-`, terminées par $\\square$.',
              '4. **Exemples** : calcul explicite, puis cas limite.',
              '5. **Symétries et conservation** : quelle symétrie, quel courant (fil de Noether).',
              '6. **Généralisations** : dimension $n$, variété, champs, quantique.',
              '7. **Contrôles de cohérence** : dimensions, limites, signes.',
              '8. **Formulaire** : tableau récapitulatif.', '']
    else:
        b += ['## Définition', '', '## Propriétés', '', '## Exemples', '']
    ds = out_of.get(t, [])
    b += ['## Pour continuer', ''] + ([f'- {L(x)}' for x in ds] or ['- (fin de branche)']) + ['']
    if n['r']: b += ['## Notions liées', ''] + [f'- {L(x)}' for x in n['r']] + ['']
    if pl: b += ['## Parcours', ''] + [f'- [[Parcours {k}]] — {next(p["n"] for p in paths if p["k"] == k)}' for k in pl] + ['']
    write(f'{n["dir"]}/{n["file"]}.md', '\n'.join(fm + b))

# ---------- parcours ----------
for p in paths:
    m = ['flowchart TD'] + [f'  n{i}["{t}"]' for i, t in enumerate(p['s'])] + [f'  n{i} --> n{i+1}' for i in range(len(p['s']) - 1)]
    b = ['---', f'title: {q("Parcours " + p["k"] + " — " + p["n"])}', 'type: parcours', 'generated: true', 'tags:', '  - parcours', '---', '',
         f'# Parcours {p["k"]} — {p["n"]}', '', f'> [!abstract] Objectif\n> {p["o"]}', '',
         f'**{len(p["s"])} étapes**, niveau {min(nodes[t]["n"] for t in p["s"])} → {max(nodes[t]["n"] for t in p["s"])}. Coche au fur et à mesure.', '', '## Étapes', '']
    b += [f'- [ ] {i+1}. {L(t)} · n{nodes[t]["n"]} · *{STAT[nodes[t]["st"]]}*' for i, t in enumerate(p['s'])]
    if p['sup']: b += ['', '> [!warning]- Prérequis supposés (hors parcours)', '> ' + ' · '.join(L(x) for x in p['sup'])]
    b += ['', '## Carte', '', '```mermaid'] + m + ['```', '']
    write(f'Parcours/Parcours {p["k"]}.md', '\n'.join(b))
    p['fname'] = f'Parcours {p["k"]}'

# ---------- domaines, accueil, rapport ----------
for k, name in doms:
    b = ['---', f'title: {q(name)}', 'type: domaine', 'generated: true', '---', '', f'# {name}', '']
    for lv in range(1, 6):
        ts = [t for t in order if nodes[t]['d'] == k and nodes[t]['n'] == lv]
        if ts: b += [f'## Niveau {lv} — {NIV[lv]}', ''] + [f'- {L(t)} *({"chapitre" if nodes[t]["ty"] == "C" else "notion"}, {STAT[nodes[t]["st"]]})*' for t in ts] + ['']
    write(f'Domaines/{name}.md', '\n'.join(b))
home = ['---', 'title: Encyclopédie de physique', 'generated: true', '---', '', '# Encyclopédie de physique', '',
        '> [!abstract] Un corpus, plusieurs chemins\n> Complet, compact, progressif, rigoureux, général : chaque nœud est défini une fois (**notion**), développé dans un **chapitre**, rangé dans un **domaine**, et parcouru par des **parcours**.', '',
        '[[Carte interactive]] : graphe, niveaux, progression.', '', '## Par parcours', ''] + [f'- [[{p["fname"]}|{p["k"]} — {p["n"]}]] ({len(p["s"])} étapes)' for p in paths]
home += ['', '## Par domaine', ''] + [f'- [[{name}]]' for _, name in doms] + ['', '## Niveaux', ''] + [f'- **{k}** : {v}' for k, v in NIV.items()]
write('Accueil.md', '\n'.join(home) + '\n')
write('Carte interactive.md', '---\ntitle: Carte interactive\ngenerated: true\n---\n\n<iframe src="/static/explorer.html" style="width:100%;height:85vh;border:1px solid #888;border-radius:8px"></iframe>\n\nOuvrir en [plein écran](/static/explorer.html).\n')
cnt = collections.Counter((n['ty'], n['st']) for n in nodes.values())
rp = ['---', 'title: Rapport de cohérence', 'generated: true', '---', '', '# Rapport de cohérence', '',
      f'{len(nodes)} nœuds ({sum(1 for n in nodes.values() if n["ty"]=="C")} chapitres, {sum(1 for n in nodes.values() if n["ty"]=="N")} notions), {sum(len(n["p"]) for n in nodes.values())} arêtes de prérequis, {len(paths)} parcours.',
      f'Déjà couverts (partiel) : {sum(1 for n in nodes.values() if n["st"])} · à rédiger : {sum(1 for n in nodes.values() if not n["st"])}.', '', '## Avertissements', ''] + ([f'- `{w}`' for w in warn] or ['- aucun'])
write('Rapport de cohérence.md', '\n'.join(rp) + '\n')

# ---------- explorateur interactif ----------
slug = lambda s: re.sub(r'[?#]', '', s.replace('&', '-and-').replace(' ', '-'))
SH = dict(M='Maths', C='Méca. classique', O='Ondes & EM', T='Thermo & stat', Q='Quantique', R='Relativité', F='Champs', A='Avancée')
data = dict(dom=[dict(k=k, n=v, s=SH.get(k, k)) for k, v in doms], niv=NIV,
            nodes=[dict(t=t, ty=n['ty'], d=n['d'], n=n['n'], p=n['p'], r=n['r'], s=n['s'], st=n['st'], u=slug(f'Encyclopédie/{n["dir"]}/{n["file"]}')) for t, n in ((t, nodes[t]) for t in order)],
            par=[dict(k=p['k'], n=p['n'], o=p['o'], s=p['s'], u=slug(f'Encyclopédie/Parcours/{p["fname"]}')) for p in paths])
tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'explorer.tpl.html'), encoding='utf-8').read()
os.makedirs(static, exist_ok=True)
open(os.path.join(static, 'explorer.html'), 'w', encoding='utf-8').write(tpl.replace('__DATA__', json.dumps(data, ensure_ascii=False)))
print(f'{len(nodes)} nœuds, {len(paths)} parcours → {out}\nexplorateur → {static}/explorer.html')
print('\n'.join(warn) or 'aucun avertissement')
