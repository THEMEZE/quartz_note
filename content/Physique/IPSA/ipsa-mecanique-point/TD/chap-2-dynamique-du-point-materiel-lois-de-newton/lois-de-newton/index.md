---
title: "Lois de Newton"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/index|⬅ Mécanique du point — IPSA]]

> [!info] ℹ️ Chap. 2 — Dynamique du point matériel : lois de Newton
> Séance 4


<a href="/pdfs/td4_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

> [!question]+ 🎣 Accroche
> **Un seul principe, tous les mouvements : de l'ascenseur à la fusée**
>
> *Durée de l'introduction : 5 à 8 min, avant les exercices*
>
> *Pourquoi vous sentez-vous plus lourd quand un ascenseur démarre vers le haut, **mais pas** quand il roule à vitesse constante ? Comment une fusée de $2000$ tonnes peut-elle décoller ? Et pourquoi un virage relevé permet-il de rouler à une certaine vitesse **sans aucun frottement** ? Existe-t-il **un seul principe** qui répond à tout ?*
>
> **Idée clé : $\sum\vec F=m\vec a$, c'est l'accélération qui compte, pas la vitesse.**
>
>
> - **Système** : on isole l'objet étudié ; **forces** : on dresse la liste de **toutes** les actions extérieures ; **projection** : on écrit la 2\textsuperscript{e} loi sur des axes bien choisis.
> - **Équilibre ou mouvement uniforme** : $\sum\vec F=\vec0$ (ascenseur à vitesse constante, $T=mg$).
> - **Contraintes** : contact ($N\ge0$, décollage $N=0$), fil inextensible (accélérations liées), adhérence ($\|\vec f\|\le\mu N$).
> - **Accélération courbe** : centripète $-\dfrac{v^2}R\vec e_r$ (bosse, pendule conique, virage).
>
>
> Les forces fixent $\vec a$ ; la cinématique du TD1 donne alors $\vec v(t)$ et $\overrightarrow{OM}(t)$.

> [!abstract]+ 📚 Prérequis
> **Cinématique du point (TD1)**
>
> Vecteurs position, vitesse, accélération en cartésien ; intégration avec conditions initiales ; mouvement à accélération constante ; mouvement circulaire uniforme, base polaire et dérivées $\dfrac{\mathrm d\vec e_r}{\mathrm d\theta}=\vec e_\theta$, $\dfrac{\mathrm d\vec e_\theta}{\mathrm d\theta}=-\vec e_r$.
>
> **Notions de force et de masse**
>
> Une force est une action mécanique exercée par un objet identifiable sur le système ; elle s'exprime en newton ($1~\mathrm N=1~\mathrm{kg\,m\,s^{-2}}$). La masse $m$ mesure l'inertie ; le poids $\vec P=m\vec g$ est une force.
>
> **Forces usuelles**
>
> Poids $m\vec g$ ; réaction normale $\vec N$ d'un support (perpendiculaire au support, $N\ge0$) ; frottement solide de Coulomb ($\|\vec f\|\le\mu\|\vec N\|$ sans glissement, $=\mu\|\vec N\|$ avec glissement) ; tension d'un fil ; rappel élastique $-k(\ell-\ell_0)\vec u$ ; frottement fluide $-\lambda\vec v$ ; poussée d'Archimède.
>
> **Résolution d'équations et de systèmes**
>
> Systèmes linéaires de deux ou trois équations (élimination d'une inconnue), équation du second degré, équation différentielle du premier ordre à coefficients constants $\dot v+v/\tau=g$ (solution $v_\ell+C\mathrm e^{-t/\tau}$).
>
> **Trigonométrie et projection de vecteurs**
>
> Projection d'une force sur des axes inclinés (plan incliné : $mg\sin\varphi$ le long de la pente, $mg\cos\varphi$ perpendiculairement), valeurs remarquables ($30^\circ,45^\circ,60^\circ$), $\tan\varphi=\sin\varphi/\cos\varphi$, formule d'addition de la tangente.
>
> **Notion de référentiel galiléen**
>
> Un référentiel galiléen est un référentiel dans lequel le principe d'inertie est vérifié. Le référentiel terrestre est galiléen avec une très bonne approximation pour les mouvements de courte durée et de faible étendue.

> [!info]+ 🎯 Objectifs
> **Appliquer la méthode générale de la dynamique**
>
> Savoir définir le système, le référentiel et le repère, faire un schéma, dresser le bilan **complet** des forces, écrire la 2\textsuperscript{e} loi, la projeter sur des axes adaptés, résoudre pour l'accélération, une force inconnue (tension, réaction) ou une condition (décollage, rupture).
>
> **Utiliser la 1\textsuperscript{re} loi et la 3\textsuperscript{e} loi**
>
> Savoir reconnaître une situation d'équilibre ($\sum\vec F=\vec0$, y compris à vitesse constante), appliquer l'action--réaction pour des solides en contact ou reliés par un fil, et traduire l'inextensibilité d'un fil par une relation entre accélérations.
>
> **Exploiter les conditions de contact et d'adhérence**
>
> Savoir traduire « le contact est maintenu » par $N\ge0$ (décollage : $N=0$), « il y a glissement » par $\|\vec f\|=\mu N$ et obtenir des **conditions de seuil** sur une vitesse, un angle ou un instant.
>
> **Lier dynamique et cinématique**
>
> Savoir passer de $\sum\vec F$ à $\vec a$, puis à $\vec v(t)$ et $\overrightarrow{OM}(t)$ par intégration, y compris quand la force dépend du temps ($F=kt$) ou de la vitesse ($-\lambda v$, équation différentielle), et utiliser les coordonnées polaires et cylindriques pour un mouvement circulaire.
>
> **Valider et discuter un résultat**
>
> Savoir vérifier l'homogénéité, tester des cas limites (masses égales, $\lambda\to0$, $\beta\to0$), comparer à un ordre de grandeur, et confronter un modèle à une mesure en identifiant ses limites (navette Columbia).

> [!info]- 🧑‍🏫 Objectifs pédagogiques (enseignant)
> **Positionnement du TD**
>
> Ce TD fait la jonction entre la cinématique (TD1) et les théorèmes énergétiques ou le moment cinétique : la **2\textsuperscript{e} loi** y est l'outil unique, appliqué à des situations de complexité croissante (équilibre, accélération constante, systèmes liés, mouvement circulaire, frottements). Il installe la **méthode** (schéma, bilan, projection) et les **réflexes de contrôle** (cas limites, ordres de grandeur) pour toute la mécanique.
>
> **Trois parcours selon le temps disponible**
>
> **Parcours essentiel** (environ 3 h) : exercices indispensables — élémentaires (1), décollage d'un corps (2), machine d'Atwood (4), deux blocs (6), voiture sur une bosse (5).
>
> **Parcours renforcé** (environ $+1$ h) : ajouter la navette Columbia (3, esprit critique) et la chute avec frottement fluide (7, première équation différentielle).
>
> **Parcours approfondi** (CPGE/licence, séance supplémentaire ou travail personnel) : pendule conique (8) et virage relevé avec frottement (9), très proches de sujets de concours.
>
> **Compétences évaluables**
>
> **S'approprier** : lire l'énoncé, repérer le système, les données, les conditions initiales. **Analyser** : choisir repère et projections, traduire une condition physique en équation. **Réaliser** : calculs littéraux et numériques, résolution de systèmes et d'EDO. **Valider** : homogénéité, cas limites, comparaison à une mesure. **Communiquer** : schéma clair avec toutes les forces, rédaction ordonnée.
>
> **Points de vigilance sur la gestion de séance**
>
> Plusieurs exercices s'appuient sur une **figure** (angles de l'exercice 1, géométrie des exercices 4, 5 et 6) : vérifier qu'elle est distribuée. Imposer un schéma de forces avant toute équation et le valider par le voisin. Les exercices 5 et 9 demandent une maîtrise de la base polaire (rappel de 5 min sur $\dot{\vec e}_r=\dot\theta\vec e_\theta$ en début de séance).

> [!note]+ 📖 Point de cours
> **Les trois lois de Newton**
>
> **Principe d'inertie** : dans un référentiel galiléen, si $\sum\vec F=\vec0$ le mouvement est rectiligne uniforme (ou le repos), et réciproquement. **Principe fondamental** : $\sum\vec F=m\vec a=\dfrac{\mathrm d\vec p}{\mathrm dt}$ avec $\vec p=m\vec v$. **Action--réaction** : $\vec F_{A\to B}=-\vec F_{B\to A}$ (mêmes norme et droite d'action, sens opposés).
>
> **Méthode pour résoudre un problème de dynamique**
>
> (1) Système et référentiel galiléen. (2) Schéma avec repère adapté. (3) Bilan **exhaustif** des forces (contact : réaction, tension, frottement ; à distance : poids). (4) $\sum\vec F=m\vec a$, écrite avec $\vec a$ dans le repère choisi. (5) Projection sur les axes et résolution. (6) Intégrations pour $\vec v$ et $\overrightarrow{OM}$ avec les conditions initiales. (7) Vérifications.
>
> **Lois du frottement solide (Coulomb)**
>
> Sans glissement : $\|\vec f\|\le\mu_s\|\vec N\|$. Avec glissement : $\vec f$ opposé à la vitesse de glissement, $\|\vec f\|=\mu_d\|\vec N\|$. Angle de frottement $\varphi$ : $\tan\varphi=\mu$ ; la réaction totale reste dans un cône d'angle $\varphi$ autour de la normale.
>
> **Conditions de contact et de liaison**
>
> Un support ne pousse que : $N\ge0$ ; le décollage correspond à $N=0$. Un fil ne tire que : $T\ge0$ ; il se détend si $T=0$. Un fil inextensible impose des relations de déplacement et donc d'accélération entre les points reliés ; une poulie idéale conserve la tension.
>
> **Accélération en coordonnées polaires et cylindriques**
>
> $\vec a=(\ddot r-r\dot\theta^2)\,\vec e_r+(r\ddot\theta+2\dot r\dot\theta)\,\vec e_\theta+\ddot z\,\vec e_z$. Mouvement circulaire uniforme : $\vec a=-r\omega^2\vec e_r=-\dfrac{v^2}r\vec e_r$. La somme des forces est alors **centripète**.
>
> **Ordres de grandeur**
>
> Poids d'un kilogramme : $\approx10$ N ; accélération d'une voiture $2$ à $4~\mathrm{m\,s^{-2}}$ ; freinage d'urgence $\approx8~\mathrm{m\,s^{-2}}$ ; ascenseur $\approx1~\mathrm{m\,s^{-2}}$ ; adhérence pneu--route sèche $\mu\approx0{,}7$, mouillée $\approx0{,}3$, verglacée $\approx0{,}1$ ; poussée d'un lanceur $\approx1{,}2$ à $1{,}5$ fois son poids au décollage.

> [!note]- 🧮 Outils mathématiques
> **Projection et trigonométrie des plans inclinés**
>
> Poids sur un plan d'angle $\varphi$ : $mg\sin\varphi$ (le long de la pente), $mg\cos\varphi$ (perpendiculaire). Valeurs : $\sin30^\circ=\tfrac12$, $\sin60^\circ=\tfrac{\sqrt3}2$, $\cos30^\circ=\tfrac{\sqrt3}2$, $\cos60^\circ=\tfrac12$.
>
> **Systèmes linéaires et substitution**
>
> Deux équations de Newton + une contrainte : éliminer la tension par addition ou soustraction, puis isoler $a$. Contrôler en reportant dans l'autre équation (par exemple, $T$ doit être identique pour les deux blocs).
>
> **Équation différentielle du premier ordre**
>
> $\dot v+\dfrac v\tau=g$ : solution $v=v_\ell+C\,\mathrm e^{-t/\tau}$ avec $v_\ell=g\tau$ ; $C$ par la condition initiale. $\tau$ est le temps caractéristique ($63\%$ à $t=\tau$, $99\%$ à $4{,}6\,\tau$).
>
> **Développements limités**
>
> $\mathrm e^{-x}\approx1-x+\tfrac{x^2}2$, $\ln(1+x)\approx x-\tfrac{x^2}2$, $\cos\theta\approx1-\tfrac{\theta^2}2$ : pour tester une limite ($t\ll\tau$, $\lambda\to0$, petits angles).
>
> **Division membre à membre pour éliminer une inconnue**
>
> Deux projections $N\sin\beta+\dots=\dfrac{mv^2}R$ et $N\cos\beta-\dots=mg$ : leur rapport élimine $N$ et $m$ ; $\tan\beta=\dfrac{v^2}{gR}$ sans frottement.
>
> **Formule d'addition de la tangente et angle de frottement**
>
> $\tan(\beta\pm\varphi)=\dfrac{\tan\beta\pm\tan\varphi}{1\mp\tan\beta\tan\varphi}$ avec $\mu=\tan\varphi$ : écriture compacte des vitesses limites d'un virage relevé.
>
> **Minimum d'une fonction sur un intervalle**
>
> Condition vraie pour tout $\theta\in[-\alpha,\alpha]$ : chercher le cas le plus contraignant (le minimum de $\cos\theta$ est en $\pm\alpha$).
>
> **Analyse dimensionnelle**
>
> $[F]=\mathrm{kg\,m\,s^{-2}}$ ; $[k]=\mathrm{kg\,m\,s^{-3}}$ pour $F=kt$ ; $[\lambda]=\mathrm{kg\,s^{-1}}$ pour $-\lambda v$ ; $[\tau]=[m/\lambda]=\mathrm s$.


## Exercices

- [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]]

> [!warning]- 🪤 Écueils classiques
> **Bilan de forces incomplet ou avec une « force de mouvement »**
>
> Il n'existe pas de force « dans le sens du mouvement » : chaque force a un auteur identifiable. À l'inverse, oublier la réaction du support ou une composante de frottement est la première cause d'erreur. Toujours demander : « qui exerce cette force ? »
>
> **Confondre vitesse et accélération**
>
> Un mobile en mouvement rectiligne uniforme est en équilibre ($\sum\vec F=\vec0$) ; une tension de câble de cabine d'ascenseur ne dépend que de $\vec a$ (et pas de la vitesse) ; au sommet d'une trajectoire, $\vec v\ne\vec0$ en général mais $\vec a\ne\vec0$ aussi.
>
> **Erreur de projection et de repère**
>
> Composante du poids le long d'une pente : $mg\sin\varphi$ ; perpendiculairement : $mg\cos\varphi$. En coordonnées polaires, $\vec e_r$ n'est pas fixe : écrire $\vec a$ avant de projeter. Choisir un axe adapté (le long de la pente, vers le centre) simplifie le calcul.
>
> **Négliger la contrainte cinématique d'un fil**
>
> Pour des solides liés par un fil inextensible, il faut **trois** relations (deux lois de Newton et la contrainte $a_1=\pm a_2$) pour trois inconnues $(a_1,a_2,T)$ ; la contrainte oubliée conduit à un système sous-déterminé. Le signe dépend des axes choisis.
>
> **Tension égale au poids**
>
> $T=mg$ n'est vrai que si $a=0$. Dans la machine d'Atwood, $m_1g<T<m_2g$ ; dans un ascenseur qui accélère, $T=m(g+a)$ ; dans un pendule conique, $T=m\omega^2L$.
>
> **Masse variable ou force variable traitées comme constantes**
>
> $a=F/m-g$ suppose $F$ et $m$ constantes (la navette Columbia consomme plusieurs tonnes de carburant par seconde). Une force dépendant du temps donne $a(t)$ et non une accélération constante ; une force dépendant de la vitesse donne une équation différentielle.
>
> **Mauvais sens du frottement ou de la tendance au glissement**
>
> Le frottement s'oppose à la vitesse de glissement (ou à la **tendance** au glissement s'il n'y en a pas). Dans un virage relevé, le sens change selon que $v>v_0$ ou $v<v_0$. Au seuil seulement, $f=\mu N$.
>
> **Résultat sans unité ni vérification**
>
> Toujours vérifier l'homogénéité ($[k]$ pour $F=kt$), le signe, un cas limite ($m_1=m_2$, $\lambda\to0$, $\beta\to0$) et l'ordre de grandeur (une voiture qui décolle à $7$ m/s, une masse de $88$ g).

> [!tip]- 🎙️ Conseils d'animation
> **Expérience flash en ouverture**
>
> Lâcher une masse accrochée à un dynamomètre dans un ascenseur (ou simuler avec un smartphone et un capteur d'accéléromètre) : le « poids apparent » varie avec l'accélération. Cela donne un sens immédiat à $T=m(g+a)$.
>
> **Schéma de forces en binômes**
>
> Pour chaque exercice, demander à deux binômes de dresser indépendamment le bilan et de comparer. Beaucoup d'erreurs se corrigent à ce stade, avant tout calcul. Faire annoncer à voix haute « qui exerce chaque force ».
>
> **Prédire avant de calculer**
>
> Machine d'Atwood : que se passe-t-il si $m_1=m_2$ ? si $m_2\gg m_1$ ? Deux blocs : quel bloc descend ? Virage : existe-t-il une vitesse sans frottement ? Une prédiction qualitative suivie d'un calcul qui la confirme (ou la contredit) installe l'intuition.
>
> **Exploiter Python pour les EDO**
>
> Pour l'exercice 7, faire intégrer $\dot v=g-v/\tau$ par la méthode d'Euler ($\Delta t\ll\tau$) et comparer à la solution exacte. De même pour la montée en vitesse de la navette avec masse variable (esprit critique).
>
> **Gestion de l'hétérogénéité**
>
> Les étudiants rapides abordent les exercices 3, 7, 8, 9. Les autres consolident la méthode sur les exercices 1, 2, 4, 6. Réserver cinq minutes en fin de séance pour la comparaison des méthodes et des erreurs récurrentes.
>
> **Insister sur la phase « Valider »**
>
> Après chaque exercice, poser : « Quel cas limite testez-vous ? Quel ordre de grandeur attendez-vous ? » Exemples : $m_2\to m_1$, $\lambda\to0$, $\beta\to0$, $\omega\to\sqrt{g/L}$.

> [!note]- 🔗 Liens avec d'autres disciplines
> **Mathématiques**
>
> Systèmes linéaires, équations différentielles du premier ordre, trigonométrie, développements limités, inégalités et recherche de seuils.
>
> **Génie civil et transports**
>
> Dimensionnement de câbles et d'ascenseurs, ralentisseurs et profils de route (dos-d'âne), virages relevés et dévers ferroviaires, pistes de course.
>
> **Astronautique et aéronautique**
>
> Poussée d'un lanceur, rapport poussée/poids, équation de Tsiolkovski, facteur de charge d'un avion en virage.
>
> **Mécanique des fluides**
>
> Frottement visqueux (loi de Stokes), vitesse limite de sédimentation, viscosimètre à bille, nombre de Reynolds.
>
> **Électricité**
>
> L'équation $\dot v+v/\tau=g$ est la même que la charge d'un condensateur ($\tau=RC$) ou l'établissement du courant dans une bobine ($\tau=L/R$).
>
> **Histoire des sciences**
>
> Principia de Newton (1687) ; machine d'Atwood (1784) pour mesurer $g$ ; régulateur à boules de Watt (pendule conique).
>
> **Sport et biomécanique**
>
> Ski (pente et frottements), cyclisme et motocyclisme en virage (inclinaison $\tan\psi=v^2/(gR)$), saut, plongeon et parachutisme (vitesse limite).

> [!success]- 🏁 Bilan
> **Ce qu'il faut savoir faire à la fin du TD**
>
> Faire un schéma de forces complet et projeter la 2\textsuperscript{e} loi dans un repère adapté ; retrouver $a$ à partir des forces puis $v(t)$ et $x(t)$ ; traiter un système lié par fil (deux lois plus contrainte) ; utiliser la condition de contact $N\ge0$ et la loi de Coulomb pour obtenir des seuils ; écrire $\vec a$ en polaires et cylindriques pour un mouvement circulaire.
>
> **Résultats marquants du TD**
>
> Ascenseur : $T=m(g+a)$ ; plan incliné : $a=g\sin\alpha$ ; décollage avec $F=kt$ : $t_d=\dfrac{mg}{k\sin\alpha}$ ; Atwood : $a=\dfrac{m_2-m_1}{m_1+m_2}g$, $T=\dfrac{2m_1m_2}{m_1+m_2}g$ ; bosse : $v\le\sqrt{gR\cos\alpha}$ ; chute avec frottement linéaire : $v_\ell=mg/\lambda$, $\tau=m/\lambda$ ; pendule conique : $\cos\theta=\dfrac g{\omega^2L}$ ; virage relevé : $v_0=\sqrt{gR\tan\beta}$, $v_{\max,\min}=\sqrt{gR\tan(\beta\pm\varphi)}$.
>
> **Ce qui sera réutilisé dans la suite**
>
> La méthode (système, bilan, projection) servira pour le travail et l'énergie (TD suivants), où on retrouvera les mêmes situations par une méthode énergétique plus rapide ; le pendule conique et le virage relevé préparent le moment cinétique et les forces centrales ; l'équation différentielle du premier ordre reviendra en électricité (circuit RC, RL).

> [!question]- 🔭 Aller plus loin — CPGE : Référentiels non galiléens et forces d'inertie
> Refaire l'exercice de l'ascenseur et celui du virage dans le référentiel du véhicule (non galiléen) en introduisant la force d'inertie d'entraînement $-m\vec a_e$ (force centrifuge dans le virage). Montrer que les résultats sont identiques et discuter le choix du référentiel le plus commode.

> [!question]- 🔭 Aller plus loin — CPGE : Résolution numérique d'une équation de mouvement
> Intégrer numériquement (Euler, puis \texttt{scipy.integrate.solve\_ivp}) le mouvement d'un projectile avec frottement quadratique $-k\,v\,\vec v$. Comparer à la parabole du modèle sans frottement et déterminer l'angle de portée maximale (inférieur à $45^\circ$).

> [!question]- 🔭 Aller plus loin — Licence : Masse variable : équation de Tsiolkovski
> Écrire $\dfrac{\mathrm d\vec p}{\mathrm dt}=\vec F_{\rm ext}$ pour une fusée qui éjecte des gaz à la vitesse relative $-u\vec u_z$ et établir $v(t)=-u\ln(1-Dt/m_0)-gt$. Appliquer à Columbia et expliquer l'écart du modèle à masse constante.

> [!question]- 🔭 Aller plus loin — Licence : Frottement quadratique et vitesse limite
> Chute avec $-kv^2$ : $m\dot v=mg-kv^2$, solution $v=v_\ell\tanh(gt/v_\ell)$ avec $v_\ell=\sqrt{mg/k}$. Estimer $v_\ell$ d'un parachutiste en chute libre (bras écartés : $\approx55$ m/s) et sous parachute ouvert ($\approx5$ m/s).

> [!question]- 🔭 Aller plus loin — Master : Dynamique du solide : roulement sans glissement sur un plan incliné
> Pour un cylindre de moment d'inertie $J=\tfrac12mr^2$ qui roule sans glisser, montrer que $a=\dfrac{g\sin\alpha}{1+J/(mr^2)}=\tfrac23g\sin\alpha$ et que la condition de non-glissement est $\mu\ge\tfrac13\tan\alpha$. Comparer à un bloc qui glisse sans frottement ($a=g\sin\alpha$).

> [!question]- 🔭 Aller plus loin — Doctorat : Limites de la mécanique newtonienne
> Pour une particule dont la vitesse approche $c$, la 2\textsuperscript{e} loi $\dfrac{\mathrm d\vec p}{\mathrm dt}=\vec F$ reste valable avec $\vec p=\gamma m\vec v$, mais $\vec a$ n'est plus parallèle à $\vec F$. Montrer que $\vec F=\gamma m\vec a+\gamma^3m\dfrac{(\vec v\cdot\vec a)}{c^2}\vec v$ et discuter les masses « longitudinale » $\gamma^3m$ et « transversale » $\gamma m$.

