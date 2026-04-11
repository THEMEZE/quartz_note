---
title: Quantum fluids of light
---


Ce sujet est très riche, et il est clairement à l’interface **optique quantique / matière condensée / systèmes hors équilibre**.  On va roit aux concepts physiques sous-jacents.

* * *

# 1) Idée centrale : “faire de la matière condensée avec de la lumière”

Un réseau de résonateurs photoniques couplés réalise un **modèle de type tight-binding pour les photons**.
### Modèle effectif

On décrit les modes des cavités par des opérateurs bosoniques  $a_i$  :
$$
H = \sum_i \omega_i a_i^\dagger a_i - \sum_{\langle i,j \rangle} J_{ij} a_i^\dagger a_j + \text{interactions}
$$
*    $\omega_i$  : fréquence de la cavité
*    $J_{ij}$  : couplage tunnel (analogue du hopping électronique)
*   réseau périodique → **structure de bande**

👉 Exactement analogue aux électrons dans un cristal.

* * *
# 2) Pourquoi “quantum fluids of light” ?

Dans certaines plateformes (notamment exciton-polaritons) :

*   les photons héritent d’une **masse effective**
*   *   **interactions non linéaires** (via excitons)

>[!question]- Pourquoi les photons ont une **masse effective** (exciton-polaritons) ?
>
>>[!note]-  a) Photon libre
>>
>>Dans le vide :
>>$$
>>E = \hbar c k \quad (\text{dispersion linéaire})
>>$$
>>👉 pas de masse (toujours à  $c$ ).
>
>>[!note]- b) Photon dans une microcavité
>>
>>Dans une cavité (miroirs parallèles) :
>>*   quantification selon  $z$ 
>>*   propagation libre dans le plan  $x,y$ 
>>Dispersion :
>>$$
>>E(k_\parallel) = \hbar \omega_c + \frac{\hbar^2 k_\parallel^2}{2 m_{\text{ph}}}
>>$$
>>👉 **parabole → masse effective**
>>$E(k)=E_0+\frac{\hbar^2 k^2}{2m}$ 
>>avec :
>>$$
>>m_{\text{ph}} = \frac{\hbar \omega_c}{c^2}
>>$$
>>➡️ clé : **confinement → comportement de particule massive**
>
>>[!note]- c) Exciton-polariton
>>
>>Couplage fort :
>>*   photon + exciton (électron-trou lié)
>>Hamiltonien :
>>$$
>>H = \begin{pmatrix} E_{\text{ph}}(k) & \Omega_R \\ \Omega_R & E_{\text{exc}} \end{pmatrix}
>>$$
>>Diagonalisation → **deux branches** :
>>*   lower polariton (LP)
>>*   upper polariton (UP)
>>👉 Le polariton :
>>*   masse très légère (photon)
>>*   interactions fortes (exciton)
>>➡️ parfait pour **fluide quantique**
>



On obtient un Hamiltonien de type **Bose-Hubbard** :
$$
H = \sum_i \omega a_i^\dagger a_i - J \sum_{\langle i,j \rangle} a_i^\dagger a_j + \frac{U}{2} \sum_i a_i^\dagger a_i^\dagger a_i a_i
$$
👉 C’est un **fluide quantique bosonique**.
### Conséquence

*   condensation de Bose → cohérence macroscopique
*   régime superfluide → absence de dissipation

➡️ “la lumière devient superfluide”


>[!question]- Origine du terme d’interaction  $U$  (Bose-Hubbard)
>
>Le modèle :
>$$
>H = \sum_i \omega a_i^\dagger a_i - J \sum_{\langle i,j \rangle} a_i^\dagger a_j + \frac{U}{2} \sum_i n_i(n_i-1)
>$$
>Origine physique de  $U$ 
>
>Les photons seuls n’interagissent pas.
>
>👉 Mais via excitons :
>
>*   interaction Coulomb e–h
>*   saturation excitonique
>
>→ polaritons interagissent faiblement
>
>### Interprétation
>
>$$
>U \sim \text{énergie de répulsion locale}
>$$
>
>➡️ coût énergétique pour avoir 2 polaritons dans la même cavité
>
>* * *
>
>Conséquences physiques
>
>*    $U \ll J$  → superfluide
>*    $U \gg J$  → blocage (type Mott, plus difficile en photonique)
> * * *
>



* * *

# 3) Graphene avec la lumière

Dans un réseau **hexagonal (type graphène)** :

*   structure de bande → **cônes de Dirac**
*   dispersion linéaire :
    
$$
E(\mathbf{k}) \sim v_F |\mathbf{k}|
$$

👉 Les photons se comportent comme des **fermions de Dirac massless** (sans être fermions !)

Conséquences :

*   pseudo-spin (sous-réseaux A/B)
*   interférences topologiques
*   transport anormal

>[!info]- Mini-cours : **bandes d’énergie**
>
>>[!note]- a) Réseau périodique → théorème de Bloch
>>
>>$$
>>\psi_k(r) = e^{i k \cdot r} u_k(r)
>>$$
>>👉  $k$  = quasi-moment
>>
>
>>[!note]- b) Tight-binding (cas du stage)
>>
>>$$
>>E(k) = -2J \cos(ka)
>>$$
>> $E(k)=-2J\cos(ka)$ 
>>
>>En 2D → surfaces de dispersion.
>
>>[!note]- c) Graphene (important ici)
>>
>>*   2 sous-réseaux → matrice  $2 \times 2$ 
>>*   points de Dirac :   
>>$$
>>E(k) \sim \pm v_F |k|
>>$$
>

* * *

>[!info]- **Comment on mesure les bandes en expé ?**
>
>👉 Question centrale pour ton stage.
>
>>[!note]- a) Spectroscopie en angle (très standard)
>>
>>On mesure :
>>*   intensité lumineuse
>>*   en fonction de :
>>    *   fréquence  $\omega$ 
>>    *   angle  $\theta$ 
>
>>[!note]-b) Correspondance angle ↔ moment
>>
>>$$
>>k_\parallel = \frac{\omega}{c} \sin \theta
>>$$
>>👉 L’image en espace angulaire = espace des  $k$ 
>>
>>➡️ **oui : tu es automatiquement dans l’espace de Fourier**
>
>>[!note]- c) Ce que tu observes
>>
>>Une image typique :
>>*   axe horizontal :  $k$ 
>>*   axe vertical : énergie
>>
>>👉 directement :
>>$$
>>E(k)
>>$$
>>
>>➡️ **structure de bande expérimentale**
>
>>[!note]- d) En pratique
>>
>>Tu mesures :
>>*   spectre résolu en angle
>>*   ou caméra dans plan de Fourier
>>
>



* * *

# 4) Champ magnétique synthétique


Les photons sont neutres → pas de champ magnétique réel.

👉 On crée un **champ magnétique artificiel** via des phases de Peierls :

$$
J_{ij} \to J e^{i \phi_{ij}}
$$

avec :

$$
\sum_{\text{plaquette}} \phi_{ij} = \Phi
$$

➡️ analogue du flux magnétique

* * *
### Résultat physique

*   bandes de Hofstadter
*   nombres de Chern non nuls
*   **phases topologiques**

* * *

# 5) États de bord topologiques

Dans ces systèmes :

👉 apparition de **modes de bord chiraux**

Car :

*   bulk → invariant topologique (Chern)
*   bord → états protégés

### Propriété clé

*   propagation unidirectionnelle
*   **robuste aux défauts et désordre**

➡️ pas de diffusion → transport sans perte

C’est ce que le texte appelle :

> “immune to scattering by impurities”

* * *

# 6) Système hors équilibre (très important)

Contrairement aux électrons :

*   pertes (fuites photons)
*   pompage externe

👉 système **driven-dissipative**

Équation typique :

$$
i \frac{d\psi}{dt} = (H - i\kappa)\psi + F
$$
*    $\kappa$  : pertes
*    $F$  : pompe

➡️ physique non hermitienne  
➡️ états stationnaires non triviaux

* * *

# 7) Lien avec les références


### Amo & Bloch (2016)

*   polaritons dans réseaux
*   simulateur quantique non linéaire

### Thouless pumping (PRL 2025)

*   transport quantifié :
    
$$
Q = C \in \mathbb{Z}
$$

➡️ topologie dynamique

### Non-Abelian geometry

*   connexion de Berry matricielle
*   espaces de bandes dégénérées

👉 très avancé (géométrie quantique)

* * *

# 8) Partie expérimentale du stage

## Spectroscopie optique

On mesure :

*   modes propres
*   bandes
*   dispersion

## Conditions extrêmes

*   **4 K** → réduire décohérence
*   **champ magnétique 7 T** → agir sur excitons/polaritons

* * *

# 9) Modélisation théorique attendue

Tu devras probablement manipuler :

### 1\. Tight-binding

*   calcul de bandes
*   diagonalisation

### 2\. Topologie

*   courbure de Berry :
    
$$
\Omega(\mathbf{k})
$$
*   nombre de Chern :
    
$$
C = \frac{1}{2\pi} \int \Omega(\mathbf{k}) d^2k
$$

>[!info]- Topologie : courbure de Berry
>
>On considère une bande  $|u_n(k)\rangle$ 
>
>>[!note]- a) Connexion de Berry
>>
>>$$
>>A(k) = i \langle u(k) | \nabla_k u(k) \rangle
>>$$
>
>>[!note]- b) Courbure de Berry
>>
>>$$
>>\Omega(k) = \nabla_k \times A(k)
>>$$
>👉 analogue d’un champ magnétique en espace des  $k$ 
>
>>[!note]- c) Interprétation physique
>>
>>*   déviation transverse
>>*   transport anormal
>>*   Hall sans champ réel
>

>[!info]- Nombre de Chern
>
>$$
>C = \frac{1}{2\pi} \int_{\text{BZ}} \Omega(k)\, d^2k
>$$
>
>## Propriétés
>
>*   entier (quantification topologique)
>*   invariant global
>
>>[!note]- a) Lien avec physique
>>
>>👉 Si  $C \neq 0$  :
>>
>>*   états de bord apparaissent
>>*   transport unidirectionnel
>>*   robuste aux défauts
>


>[!question]- Comment mesurer la topologie en photonique ?
>
>Pas direct comme en électronique → méthodes indirectes :
>
>>[!note]- a) Observation des bords
>>
>>*   injection lumière au bord
>>*   propagation sans diffusion
>
>>[!note]- b) Pumping (réf PRL 2025)
>>
>>*   transport quantifié
>
>>[!note]- c) Reconstruction de Berry
>>
>>*   interférométrie
>>*   polarisation (réf Stokes)
>

>[!tip]- Lien avec la géometrie des courbure
>
>$$
>\mathcal F = d\mathcal A + \mathcal A \wedge \mathcal A
>$$
>👉 c’est exactement :
>
>*    $\mathcal A$  = connexion de Berry
>*    $\mathcal F$  = courbure
>
>(cf [[Connexion et courbure en supergravité]] [[Calcul-differentiel-exterieur-geometrie]] [[Forme-différentielle]])
>

### 3\. Dynamique hors équilibre

*   Lindblad / équations effectives

* * *

# 10) Lecture globale du sujet

Ce stage = essayer de démontrer expérimentalement :

👉 que la lumière peut :

*   simuler des électrons
*   exhiber des phases topologiques
*   avoir un transport robuste

➡️ **simulateur quantique photonique**

>[!tip]- Lecture synthétique du stage
>
>Tu vas :
>
>### Expé
>
>*   mesurer  $E(k)$  via Fourier
>*   voir bandes / gaps
>*   détecter états de bord
>
>### Théorie
>
>*   diagonaliser Hamiltoniens
>*   calculer Berry / Chern
>*   modéliser pertes (non-hermitien)
>


>[!example]- **Hamiltonien  $2\times2$ ** avec un gap (type Haldane simplifié / Dirac massif)
>
>On va faire un **calcul explicite, propre et standard** sur un modèle 2 bandes de type graphene modifié, i.e. un **Hamiltonien  $2\times2$ ** avec un gap (type Haldane simplifié / Dirac massif).
>
>>[!note]- 1) Modèle : Hamiltonien 2 bandes
>>
>>On prend :
>>
>>$$
>>H(\mathbf{k}) = \mathbf{d}(\mathbf{k}) \cdot >>\boldsymbol{\sigma}
>>$$
>>
>>avec :
>>
>>*    $\boldsymbol{\sigma} = (\sigma_x,\sigma_y,\sigma_z)$ 
>>*    $\mathbf{d}(\mathbf{k}) = (d_x, d_y, d_z)$ 
>>
>>
>>## Cas Dirac massif (graphene modifié)
>>
>>
>>$$
>>d_x = k_x,\quad d_y = k_y,\quad d_z = m
>>$$
>>👉  $m \neq 0$  ouvre un gap.
>>
>>
>>## Énergies
>>
>>$$
>>E_\pm(\mathbf{k}) = \pm |\mathbf{d}|
>>$$
>>
>>avec :
>>
>>$$
>>|\mathbf{d}| = \sqrt{k_x^2 + k_y^2 + m^2}
>>$$
>
>>[!note]- 2) États propres
>>
>>On paramètre :
>>
>>$$
>>\hat{\mathbf{d}} = \frac{\mathbf{d}}{|\mathbf{d}|}
>>$$
>>
>>avec angles sphériques :
>>
>>$$
>>\cos\theta = \frac{m}{|\mathbf{d}|}, \quad \phi = \arg(k_x + i k_y)
>>$$
>>
>>## État de la bande basse ( $-$ )
>>
>>$$
>>|u_-(\mathbf{k})\rangle = \begin{pmatrix} \sin(\theta/2) e^{-i\phi} \\ -\cos(\theta/2) \end{pmatrix}
>>$$
>
>>[!note]- 3) Connexion de Berry
>>
>>Définition :
>>
>>$$
>>A(\mathbf{k}) = i \langle u_- | \nabla_k u_- \rangle
>>$$
>>
>>## Calcul (résultat standard)
>>
>>En coordonnées polaires :
>>$$
>>A_\phi = \frac{1}{2}(1 - \cos\theta), \quad A_r = 0
>>$$
>
>>[!note]- 4) Courbure de Berry
>>
>>
>>On prend le rotationnel :
>>
>>$$
>>\Omega(\mathbf{k}) = \nabla_k \times A
>>$$
>>
>>Résultat (important !) :
>>
>> $\Omega(k)=\frac{1}{2}\frac{m}{(k_x^2+k_y^2+m^2)^{3/2}}$ 
>>
>>## Interprétation
>>
>>*   pic centré en  $k=0$  (point de Dirac)
>>*   signe donné par  $m$ 
>>
>>👉 c’est une **charge topologique localisée**
>>
>
>>[!note]- 5) Calcul du nombre de Chern
>>
>>$$
>>C = \frac{1}{2\pi} \int \Omega(k)\, d^2k
>>$$
>>
>>## Intégration
>>
>>On passe en polaire :
>>
>>$$
>>d^2k = k\, dk\, d\phi
>>$$
>>
>>Donc :
>>
>>$$
>>C = \frac{1}{2\pi} \int_0^{2\pi} d\phi \int_0^\infty dk \; k \cdot \frac{1}{2} \frac{m}{(k^2 + m^2)^{3/2}}
>>$$
>>
>>## Intégrale radiale
>>
>>$$
>>\int_0^\infty \frac{k\, dk}{(k^2 + m^2)^{3/2}} = \frac{1}{|m|}
>>$$
>>
>>## Résultat final
>>
>>$$
>>C = \frac{1}{2} \, \mathrm{sign}(m)
>>$$
>
>>[!warning]-  Point crucial ⚠️
>>
>>On trouve **½** → ce n’est pas un entier !
>>
>>👉 Pourquoi ?
>>
>>Parce qu’on a :
>>
>>*   un seul cône de Dirac
>>*   espace  $k$  non compact
>
>>[!note]- 6) Cas physique réel (réseau)
>>
>>Dans un vrai réseau (graphene, Haldane) :
>>
>>*   il y a **2 points de Dirac**
>>*   contributions s’additionnent
>>
>>👉 Résultat final :
>>
>>$$
>>C \in \mathbb{Z}
>>$$
>
>>[!note]- 7) Lecture physique
>>
>>## Si  $m > 0$ 
>>
>>*   courbure positive
>>*   chiralité donnée
>>
>>## Si  $m < 0$ 
>>
>>*   courbure négative
>>*   inversion topologique
>>
>>👉 transition topologique à  $m=0$ 
>
>>[!note]- 8) Lien avec ton stage
>>
>>Ce calcul correspond exactement à :
>>
>>*   réseaux photoniques bipartites
>>*   ouverture de gap (déséquilibre sous-réseaux ou phases)
>>*   mesure indirecte de  $\Omega(k)$ 
>
>>[!note]- 9) Lien profond avec ta géométrie
>>
>>Tu reconnais :
>>
>>*    $A(k)$  = connexion
>>*    $F = dA$  = courbure
>>
>>Et en non-abélien :
>>
>>$$
>>F = dA + A \wedge A
>>$$
>>
>>👉 exactement ce que tu manipules déjà.
>
>>[!note]- 10) Vision intuitive (très importante)
>>
>>
>>Le mapping :
>>
>>$$
>>\mathbf{k} \mapsto \hat{\mathbf{d}}(\mathbf{k}) \in S^2
>>$$
>>👉 le Chern = nombre d’enroulements autour de la sphère
>

>[!example]- **Exemple minimal mais propre** : calcul de
>
>1.  structure de bande
>2.  courbure de Berry
>3.  nombre de Chern
>
>sur un modèle standard : **modèle de Haldane simplifié (2 bandes)**.
>
>>[!note]- 1) Idée du code
>>
>>On va :
>>
>>*   définir  $H(k_x,k_y)$ 
>>*   diagonaliser → états propres
>>*   calculer la Berry curvature via méthode discrète (Fukui)
>>*   intégrer → Chern
>
>>[!note]- 2) Code Python (numpy pur)
>>
>>
>>```
>>import numpy as np
>>
>># =========================
>># Paramètres du modèle
>># =========================
>>t1 = 1.0      # hopping NN
>>t2 = 0.1      # hopping NNN (complex)
>>phi = np.pi/2 # phase
>>M = 0.5       # masse (gap)
>>
>># Grille k
>>Nk = 101
>>kx_vals = np.linspace(-np.pi, np.pi, Nk)
>>ky_vals = np.linspace(-np.pi, np.pi, Nk)
>>
>># =========================
>># Hamiltonien H(k)
>># =========================
>>def H(kx, ky):
>>    # réseau hexagonal simplifié (approx continu type Dirac)
>>    dx = np.sin(kx)
>>    dy = np.sin(ky)
>>    dz = M + 2*t2*(np.sin(kx) - np.sin(ky))
>>    
>>    return np.array([
>>        [dz, dx - 1j*dy],
>>        [dx + 1j*dy, -dz]
>>    ])
>>
>># =========================
>># Stockage états propres
>># =========================
>>eigvecs = np.zeros((Nk, Nk, 2), dtype=complex)
>>
>>for i, kx in enumerate(kx_vals):
>>    for j, ky in enumerate(ky_vals):
>>        w, v = np.linalg.eigh(H(kx, ky))
>>        eigvecs[i, j] = v[:, 0]  # bande basse
>>
>># =========================
>># Méthode de Fukui (Berry)
>># =========================
>>def link(u, v):
>>    return np.vdot(u, v) / np.abs(np.vdot(u, v))
>>
>>chern = 0.0
>>
>>for i in range(Nk-1):
>>    for j in range(Nk-1):
>>        u = eigvecs[i, j]
>>        u_x = eigvecs[i+1, j]
>>        u_y = eigvecs[i, j+1]
>>        u_xy = eigvecs[i+1, j+1]
>>        
>>        # Liens de Berry
>>        U1 = link(u, u_x)
>>        U2 = link(u_x, u_xy)
>>        U3 = link(u_xy, u_y)
>>        U4 = link(u_y, u)
>>        
>>        # flux de Berry
>>        F = np.log(U1 * U2 * U3 * U4)
>>        
>>        chern += F.imag
>>
>>chern /= (2 * np.pi)
>>
>>print("Chern number =", chern.real)
>>```
>>
>
>>[!note]- 3) Explication des étapes (important)
>>
>>>[!todo]- a) Diagonalisation
>>>
>>>
>>>```
>>>w, v = np.linalg.eigh(H(kx, ky))
>>>```
>>>
>>>*    $w$  = énergies → bandes
>>>*    $v$  = vecteurs propres → états de Bloch
>>>
>>>👉 on prend la bande basse :
>>>
>>>```
>>>v[:, 0]
>>>```
>>
>>>[!question]- b) Pourquoi Fukui ?
>>>
>>>
>>>Problème :
>>>
>>>*    $A(k)$  dépend du choix de phase
>>>*   dérivées numériques instables
>>>
>>>👉 Fukui = **formulation gauge-invariante discrète**
>>>
>>
>>>[!abstract]- c) Principe
>>>
>>>On calcule des **liens de Berry** :
>>>
>>>$$
>>>U_\mu(k) = \langle u(k) | u(k+\delta k_\mu) \rangle
>>>$$
>>>
>>>Puis le flux sur une plaquette :
>>>
>>>$$
>>>F = \log(U_1 U_2 U_3 U_4)
>>>$$
>>
>>>[!success]- d) Somme → Chern
>>>
>>>$$
>>>C = \frac{1}{2\pi} \sum F
>>>$$
>>
>
>>[!note]- 4) Visualiser les bandes
>>
>>Ajoute ça :
>>
>>```
>>import matplotlib.pyplot as plt
>>
>>E1 = np.zeros((Nk, Nk))
>>E2 = np.zeros((Nk, Nk))
>>
>>for i, kx in enumerate(kx_vals):
>>    for j, ky in enumerate(ky_vals):
>>        w, _ = np.linalg.eigh(H(kx, ky))
>>        E1[i,j] = w[0]
>>        E2[i,j] = w[1]
>>
>>plt.imshow(E1, extent=[-np.pi, np.pi, -np.pi, np.pi])
>>plt.title("Bande basse")
>>plt.colorbar()
>>plt.show()
>>```
>
>>[!tip]- 5) Résultat attendu
>>
>>Selon paramètres :
>>
>>*    $C = 0$  → trivial
>>*    $C = \pm 1$  → phase topologique
>>
>>👉 change  $M$ ,  $t_2$ ,  $\phi$  pour voir transition
>>
>
>>[!tip]- 6) Ce que ça simule (lien stage)
>>
>>Ce code reproduit exactement :
>>
>>*   structure de bande photonique
>>*   courbure de Berry
>>*   invariant topologique
>>
>>👉 ce que tu mesureras indirectement en expé
>
>>[!tip]- 7) Extensions utiles (si tu veux te démarquer)
>>
>>Tu peux facilement ajouter :
>>
>>>[!note]- a) États de bord
>>>
>>>*   géométrie ruban (open boundary)
>>
>>>[!note]- b) Dynamique
>>>
>>>*   propagation d’un paquet d’onde
>>
>>>[!note]- c) Non-hermitien (réaliste photonique)
>>>
>>>```
>>>H_eff = H(kx, ky) - 1j * gamma * np.eye(2)
>>>```
>>
>
>>[!tip]- 8) Niveau entretien
>>
>>Si tu montres que tu comprends :
>>
>>*   Fukui method
>>*   lien Berry ↔ observable
>>*   structure de bande
>>
>

* * *

# 11) Ce qu’on attend du candidat (traduction implicite)


*   optique quantique ✔️
*   MQ / théorie des champs ✔️
*   algèbre / géométrie (Berry, connexions) ✔️


