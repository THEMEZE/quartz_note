---
title: "Exercice 9 — Virage relevé et frottement solide"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 9. Virage relevé et frottement solide *(facultatif)*

*Difficulté ●●●●● · ⏱ 55 min · Type : Approfondissement / Exercice non guidé*

Une voiture, assimilée à un point matériel $M$ de masse $m$, prend un virage circulaire de rayon $R=100$ m dont la chaussée est **relevée** d'un angle $\beta=10^\circ$ vers l'intérieur du virage (la route est inclinée comme un plan incliné, le bord intérieur étant plus bas). La voiture roule à vitesse constante $v$ sur un cercle horizontal de rayon $R$ et centre $C$ sur l'axe vertical du virage. Le contact route--pneus est modélisé par la loi de Coulomb du frottement solide : la réaction $\vec R=\vec N+\vec f$ avec $\vec N$ normale à la route et $\vec f$ tangentielle (dans le plan incliné, perpendiculaire à la vitesse donc dirigée dans la **pente**), $\|\vec f\|\le\mu\|\vec N\|$ où $\mu$ est le coefficient d'adhérence. On prendra $g=9{,}81~\mathrm{m\,s^{-2}}$. On travaille dans le référentiel terrestre galiléen, avec un repère $(\vec e_r,\vec e_\varphi,\vec u_z)$ cylindrique d'axe vertical passant par $C$.


> [!question]- 🪝 Accroche
> **Pourquoi relève-t-on les virages ?**
>
> *Durée de l'introduction : 4 min*
>
> *Les routes de montagne et les autodromes ont des virages **inclinés vers l'intérieur**. Pourquoi ? Existe-t-il une vitesse pour laquelle **on n'aurait plus besoin d'adhérence du tout** ? Que se passe-t-il à vitesse très faible sur une route verglacée ?*
>
> **Idée clé : la réaction oblique fournit la force centripète.** La composante horizontale de $\vec N$ ($N\sin\beta$) pointe vers le centre du virage. Pour $v_0=\sqrt{gR\tan\beta}$ elle suffit, sans frottement. Au-delà ou en deçà, le frottement (borné par $\mu N$) doit compléter : cela borne $v$ entre $v_{\min}$ et $v_{\max}$.




> [!abstract]- 🧠 À savoir avant
> **Lois de Coulomb du frottement solide**
>
> Sans glissement : $\|\vec f\|\le\mu\|\vec N\|$ ($\mu$ = coefficient d'adhérence). Au seuil de glissement : $\|\vec f\|=\mu\|\vec N\|$, la force de frottement s'oppose à la vitesse de glissement (ou à la tendance au glissement).
>
> **Accélération du mouvement circulaire uniforme**
>
> $\vec a=-\dfrac{v^2}R\,\vec e_r$ : horizontale, dirigée vers l'axe du virage.
>
> **Projection des forces sur un plan incliné**
>
> Sur une route inclinée de $\beta$ : le vecteur normal fait l'angle $\beta$ avec la verticale ; $\vec N=N(\sin\beta\,(-\vec e_r)+\cos\beta\,\vec u_z)$ (vers l'intérieur du virage et vers le haut).




> [!info]- 🎯 Ce que tu sauras faire
> **Encadrer une vitesse par des conditions d'adhérence**
>
> Savoir poser un problème de seuil de glissement : écrire la 2\textsuperscript{e} loi avec une réaction oblique, projeter horizontalement et verticalement, éliminer $N$, et obtenir deux vitesses limites (maximale et minimale), puis discuter selon la valeur de $\mu$ par rapport à $\tan\beta$.




> [!info]- 🧑‍🏫 Objectifs pédagogiques
> **Exercice de synthèse sur le frottement et le mouvement circulaire**
>
> Trois ingrédients : mouvement circulaire uniforme, réaction oblique, loi de Coulomb. L'étudiant découvre qu'il existe une **vitesse idéale** $v_0=\sqrt{gR\tan\beta}$ pour laquelle aucun frottement n'est nécessaire (c'est le principe des virages relevés), et que le frottement élargit l'intervalle de vitesses permises. Piège : au seuil de glissement **par le bas** (vitesse trop faible), le frottement change de sens ; si $\mu>\tan\beta$, il n'existe plus de vitesse minimale (on peut s'arrêter dans le virage sans glisser). C'est l'exercice le plus difficile du TD ; prévoir des coups de pouce progressifs.




> [!tip]- 📖 Rappel de cours
> **Seuil de glissement**
>
> Les équations de Newton projetées donnent $\|\vec f\|$ et $\|\vec N\|$ ; la condition de non-glissement est $\|\vec f\|\le\mu\|\vec N\|$. Chercher les bornes de $v$ revient à résoudre $\|\vec f\|=\mu\|\vec N\|$, avec le bon sens pour $\vec f$ (vers le haut de la pente pour un risque de glissement vers le bas, vers le bas de la pente dans l'autre cas).




> [!note]- 🧮 Outils mathématiques
> **Projection avec une réaction oblique**
>
> Horizontale (vers le centre) : $N\sin\beta+f\cos\beta=\dfrac{mv^2}R$ ; verticale : $N\cos\beta-f\sin\beta=mg$ (frottement dirigé vers le haut de la pente comptée positive ; signe de $f$ à adapter).
>
> **Élimination de $N$ par division**
>
> En divisant les deux équations avec $f=\pm\mu N$ : $\dfrac{v^2}{gR}=\dfrac{\sin\beta\pm\mu\cos\beta}{\cos\beta\mp\mu\sin\beta}=\dfrac{\tan\beta\pm\mu}{1\mp\mu\tan\beta}$.
>
> **Formule d'addition de la tangente**
>
> $\tan(\beta+\varphi)=\dfrac{\tan\beta+\tan\varphi}{1-\tan\beta\tan\varphi}$ avec $\mu=\tan\varphi$ ($\varphi$ = angle de frottement). On en déduit $v_{\max}^2=gR\tan(\beta+\varphi)$ et $v_{\min}^2=gR\tan(\beta-\varphi)$ : écriture compacte.
>
> **Comparer deux inégalités**
>
> Vérifier $v_{\min}\le v_0\le v_{\max}$ : le frottement ne fait qu'élargir l'intervalle autour de $v_0$.



**q1.** - [(a)] Faire le schéma en coupe du virage (plan vertical contenant l'axe) et le bilan des forces s'exerçant sur $M$ dans le cas **sans frottement**.
- [(b)] Écrire la 2\textsuperscript{e} loi de Newton et la projeter horizontalement (sur $-\vec e_r$, vers le centre) et verticalement. En déduire l'expression de la vitesse $v_0$ pour laquelle la voiture reste sur la trajectoire sans aucun frottement. Application numérique.


> [!tip]- 💡 Coup de pouce
> Sans frottement, il ne reste que le poids et la réaction normale, inclinée de $\beta$ par rapport à la verticale. L'accélération est horizontale, dirigée vers l'axe.




> [!success]- ✅ Correction
> $N\cos\beta=mg$ et $N\sin\beta=mv_0^2/R$ ; $v_0=\sqrt{gR\tan\beta}\approx13{,}2$ m/s $\approx47$ km/h.




> [!example]- 📝 Solution détaillée
> **(a) Forces sans frottement**
>
> Deux forces : poids $-mg\,\vec u_z$ et réaction normale $\vec N$, perpendiculaire à la chaussée : elle fait l'angle $\beta$ avec la verticale et pointe vers le haut et vers l'**intérieur** du virage : $\vec N=N\big(-\sin\beta\,\vec e_r+\cos\beta\,\vec u_z\big)$.
>
> **(b) Vitesse sans frottement**
>
> Accélération : $\vec a=-\dfrac{v^2}R\vec e_r$. Projections :
> $$\text{(vertical)}:\ N\cos\beta-mg=0,\qquad\text{(vers le centre)}:\ N\sin\beta=\frac{mv^2}R .$$
> En divisant : $\tan\beta=\dfrac{v^2}{gR}$, soit
> $$\boxed{v_0=\sqrt{gR\tan\beta}}=\sqrt{9{,}81\times100\times0{,}1763}\approx\boxed{13{,}2~\mathrm{m/s}}\approx47~\text{km/h}.$$
> Indépendante de la masse. C'est la vitesse de dimensionnement du virage.



**q2.** On tient maintenant compte de l'adhérence de coefficient $\mu$.


- [(c)] Pour $v>v_0$, dans quel sens la voiture a-t-elle tendance à glisser ? Quel est le sens de la force de frottement $\vec f$ ? Écrire les projections de la 2\textsuperscript{e} loi.
- [(d)] Exprimer la condition de non-glissement $\|\vec f\|\le\mu N$ et en déduire la vitesse maximale $v_{\max}$ en fonction de $g$, $R$, $\beta$, $\mu$.
- [(e)] Application numérique pour $\mu=0{,}1$ (route mouillée) et $\mu=0{,}7$ (route sèche).


> [!tip]- 💡 Coup de pouce
> À vitesse élevée, la voiture « part vers l'extérieur » : elle tend à remonter la pente. Le frottement s'y oppose, donc il est dirigé vers le bas de la pente. Au seuil, $f=\mu N$. Divisez les deux projections pour éliminer $N$.




> [!success]- ✅ Correction
> $f$ dirigée vers le bas de la pente ; $N\sin\beta+f\cos\beta=mv^2/R$, $N\cos\beta-f\sin\beta=mg$ ; $v_{\max}^2=gR\dfrac{\tan\beta+\mu}{1-\mu\tan\beta}$ ; $\mu=0{,}1$ : $16{,}6$ m/s ($60$ km/h) ; $\mu=0{,}7$ : $31{,}3$ m/s ($113$ km/h).




> [!example]- 📝 Solution détaillée
> **(c) Tendance au glissement et projections**
>
> Pour $v>v_0$, la réaction normale ne fournit plus assez de force centripète : la voiture tend à glisser vers l'**extérieur** du virage, c'est-à-dire à remonter la pente. Le frottement s'y oppose : $\vec f$ est tangent à la chaussée, dirigé vers le **bas de la pente** (vers l'intérieur et vers le bas) : $\vec f=f\big(-\cos\beta\,\vec e_r-\sin\beta\,\vec u_z\big)$. Projections :
> $$\text{(vers le centre)}:\ N\sin\beta+f\cos\beta=\frac{mv^2}R,\qquad\text{(vertical)}:\ N\cos\beta-f\sin\beta=mg .$$
>
> **(d) Vitesse maximale**
>
> Seuil de glissement : $f=\mu N$. En remplaçant :
> $$N(\sin\beta+\mu\cos\beta)=\frac{mv^2}R,\qquad N(\cos\beta-\mu\sin\beta)=mg .$$
> On divise membre à membre :
> $$\frac{v_{\max}^2}{gR}=\frac{\sin\beta+\mu\cos\beta}{\cos\beta-\mu\sin\beta}\ \Rightarrow\ \boxed{v_{\max}=\sqrt{gR\,\frac{\tan\beta+\mu}{1-\mu\tan\beta}}}.$$
> (Avec $\mu=\tan\varphi$ : $v_{\max}^2=gR\tan(\beta+\varphi)$.) Pour $\mu=0$ on retrouve $v_0$ ; pour $\beta=0$, $v_{\max}=\sqrt{\mu gR}$.
>
> **(e) Applications numériques**
>
> $\tan\beta=0{,}1763$ et $gR=981~\mathrm{m^2\,s^{-2}}$.
>
> $\mu=0{,}1$ : $v_{\max}=\sqrt{981\times\dfrac{0{,}2763}{0{,}9824}}\approx\boxed{16{,}6~\mathrm{m/s}}\approx60$ km/h.
>
> $\mu=0{,}7$ : $v_{\max}=\sqrt{981\times\dfrac{0{,}8763}{0{,}8766}}\approx\boxed{31{,}3~\mathrm{m/s}}\approx113$ km/h.
>
> Sans relèvement ($\beta=0$) on aurait seulement $\sqrt{\mu gR}$ : $9{,}9$ m/s ($36$ km/h) et $26{,}2$ m/s ($94$ km/h).



**q3.** - [(f)] Pour $v<v_0$, dans quel sens la voiture a-t-elle tendance à glisser ? En déduire la vitesse minimale $v_{\min}$ en dessous de laquelle elle glisse vers l'intérieur du virage.
- [(g)] Quelle condition sur $\mu$ et $\beta$ assure qu'il n'existe aucune vitesse minimale ? Discuter pour $\mu=0{,}1$ et $\mu=0{,}7$.
- [(h)] Écrire $v_{\min}$ et $v_{\max}$ à l'aide de l'angle de frottement $\varphi$ défini par $\tan\varphi=\mu$. Commenter.


> [!tip]- 💡 Coup de pouce
> À basse vitesse, la voiture « tombe vers l'intérieur » : elle tend à descendre la pente. Le frottement est alors dirigé vers le haut de la pente : changez le signe de $\mu$ dans les formules précédentes. Pour (h), utilisez la formule d'addition de la tangente.




> [!success]- ✅ Correction
> $v_{\min}^2=gR\dfrac{\tan\beta-\mu}{1+\mu\tan\beta}$ si $\mu<\tan\beta$ ; $\mu=0{,}1$ : $8{,}6$ m/s ($31$ km/h) ; si $\mu\ge\tan\beta$ ($0{,}7$) : pas de minimum ; $v_{\min}=\sqrt{gR\tan(\beta-\varphi)}$, $v_{\max}=\sqrt{gR\tan(\beta+\varphi)}$.




> [!example]- 📝 Solution détaillée
> **(f) Vitesse minimale**
>
> Pour $v<v_0$, la voiture tend à glisser vers le bas de la pente ; le frottement est dirigé vers le **haut de la pente** : $\vec f=f\big(\cos\beta\,\vec e_r+\sin\beta\,\vec u_z\big)$. Les projections deviennent $N\sin\beta-f\cos\beta=\dfrac{mv^2}R$ et $N\cos\beta+f\sin\beta=mg$. Au seuil $f=\mu N$ :
> $$\frac{v_{\min}^2}{gR}=\frac{\sin\beta-\mu\cos\beta}{\cos\beta+\mu\sin\beta}\ \Rightarrow\ \boxed{v_{\min}=\sqrt{gR\,\frac{\tan\beta-\mu}{1+\mu\tan\beta}}}\quad(\mu<\tan\beta).$$
> Pour $\mu=0{,}1$ : $v_{\min}=\sqrt{981\times\dfrac{0{,}0763}{1{,}0176}}\approx\boxed{8{,}6~\mathrm{m/s}}\approx31$ km/h.
>
> **(g) Absence de vitesse minimale**
>
> Si $\mu\ge\tan\beta$, le numérateur est négatif ou nul : aucune vitesse (même nulle) ne provoque le glissement vers le bas, car l'adhérence suffit à retenir la voiture sur la pente seule ($v=0$). Condition : $\boxed{\mu\ge\tan\beta}$, c'est-à-dire que l'angle de frottement $\varphi$ dépasse l'angle de la pente. Ici $\tan\beta=0{,}176$ : route mouillée ($\mu=0{,}1<0{,}176$) : une voiture à l'arrêt **glisserait** vers l'intérieur et il y a un minimum à $31$ km/h ; route sèche ($\mu=0{,}7>0{,}176$) : $v_{\min}=0$.
>
> **(h) Écriture avec l'angle de frottement**
>
> Avec $\mu=\tan\varphi$ et $\tan(\beta\pm\varphi)=\dfrac{\tan\beta\pm\mu}{1\mp\mu\tan\beta}$ :
> $$\boxed{v_{\max}=\sqrt{gR\tan(\beta+\varphi)}},\qquad\boxed{v_{\min}=\sqrt{gR\tan(\beta-\varphi)}}\ (\varphi<\beta).$$
> Le frottement élargit symétriquement l'angle effectif de la réaction : la réaction totale $\vec R$ peut s'incliner de $\beta-\varphi$ à $\beta+\varphi$ par rapport à la verticale (cône de frottement). Si $\beta+\varphi\ge90^\circ$, $v_{\max}$ diverge : la voiture ne peut plus glisser (à $\mu=0{,}7$ ici, $\beta+\varphi=10^\circ+35^\circ=45^\circ<90^\circ$, donc $v_{\max}$ reste fini).




> [!note]- 🔗 Liens avec d'autres disciplines
> **Génie civil routier et ferroviaire**
>
> Le dévers des routes et des voies ferrées est dimensionné pour la vitesse de référence $v_0=\sqrt{gR\tan\beta}$ ; les trains « à dévers » (pendulaires) compensent en inclinant la caisse.
>
> **Sport automobile et cyclisme**
>
> Pistes ovales (NASCAR), vélodromes à virages relevés (jusqu'à $42^\circ$), pistes de bobsleigh.
>
> **Aéronautique**
>
> Un avion en virage s'incline : la portance joue le rôle de $\vec N$ et le facteur de charge vaut $1/\cos\beta$ ($2$ pour $60^\circ$).




> [!warning]- 🪤 Écueils classiques
> **Mettre le frottement horizontal**
>
> Sur une route inclinée, le frottement est tangent à la **route** (parallèle à la pente), pas horizontal : sa composante horizontale est $f\cos\beta$ et sa composante verticale $\pm f\sin\beta$.
>
> **Prendre $N=mg$**
>
> Avec une route inclinée et une accélération horizontale, $N\ne mg$ : $N=\dfrac{m g}{\cos\beta-\mu\sin\beta}$ au seuil haut, $N=\dfrac{m g}{\cos\beta+\mu\sin\beta}$ au seuil bas.
>
> **Mauvais sens du frottement au seuil bas**
>
> À vitesse trop grande, la voiture a tendance à glisser vers l'**extérieur** (vers le haut de la pente) : $\vec f$ est dirigé vers le bas de la pente, vers l'intérieur du virage. À vitesse trop faible, c'est l'inverse : $\vec f$ est dirigé vers le haut de la pente.
>
> **Oublier de discuter $\mu$ par rapport à $\tan\beta$**
>
> Si $\mu\ge\tan\beta$ (ici $\tan10^\circ=0{,}176$ : route sèche), la voiture ne glisse jamais vers le bas, même à l'arrêt, et $v_{\min}=0$.




> [!tip]- 🎙️ Conseils d'animation
> **Piste de course**
>
> Les circuits ovales (NASCAR, Indianapolis) ont des virages relevés de $9$ à $33^\circ$ : les pilotes y roulent à plus de $300$ km/h. Calculer $v_0=\sqrt{gR\tan\beta}$ pour $R=300$ m et $\beta=30^\circ$.
>
> **Comparer avec un virage plat**
>
> Pour $\beta=0$, la condition de non-glissement devient $v\le\sqrt{\mu gR}$ : $35{,}7$ km/h seulement pour $\mu=0{,}1$ (route verglacée ou mouillée), $94$ km/h pour $\mu=0{,}7$. Le relèvement ajoute $\approx25$ km/h dans le cas mouillé ($\mu=0{,}1$).




> [!success]- 🏁 Bilan pédagogique
> **Virage relevé**
>
> Vitesse sans frottement : $v_0=\sqrt{gR\tan\beta}\approx13{,}2$ m/s ($47$ km/h). Avec adhérence : $v_{\min}=\sqrt{gR\dfrac{\tan\beta-\mu}{1+\mu\tan\beta}}$ (si $\mu<\tan\beta$, sinon $0$) et $v_{\max}=\sqrt{gR\dfrac{\tan\beta+\mu}{1-\mu\tan\beta}}$. Pour $\mu=0{,}1$ : $v\in[8{,}6;\,16{,}6]$ m/s ($31$ à $60$ km/h) ; pour $\mu=0{,}7$ : $v\le31{,}3$ m/s ($113$ km/h), pas de minimum. Avec $\beta=0$ : $v_{\max}=\sqrt{\mu gR}$.




> [!question]- 🔭 Aller plus loin — CPGE : Moto et angle d'inclinaison
> Une moto n'a pas de chaussée relevée : elle s'incline de l'angle $\psi$ avec $\tan\psi=\dfrac{v^2}{gR}$ pour que la résultante des forces passe par le centre de gravité. Calculer $\psi$ pour $v=80$ km/h et $R=100$ m, et la vitesse maximale pour $\mu=0{,}8$ (angle limite $\arctan\mu\approx38{,}7^\circ$).




> [!question]- 🔭 Aller plus loin — Licence : Dimension du véhicule et basculement
> Le véhicule a une hauteur de centre de gravité $h$ et une voie $\ell$. Montrer que le basculement (renversement) précède le glissement si $\mu>\ell/(2h)$ et déterminer la vitesse de renversement $v=\sqrt{gR\,\dfrac{\ell}{2h}}$ en route plate.




> [!question]- 🔭 Aller plus loin — Master : Vitesse variable dans le virage
> Si la voiture accélère le long du virage (accélération tangentielle $a_t$), le frottement a deux composantes (une pour l'accélération centripète, une pour $a_t$). Écrire la condition $\sqrt{f_{\rm lat}^2+f_{\rm long}^2}\le\mu N$ (cercle de frottement) et discuter le compromis freinage/virage.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex6-chaine-qui-glisse-d-une-table|Exercice 6 — (*) Chaîne qui glisse d'une table]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]]


