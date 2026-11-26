---
title: "Exercice 2 — Onde stationnaire, tube de Kundt ouvert"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · <a href="/pdfs/td2_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_PhV212_enonce)</a> · <a href="/pdfs/td2_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_enonce)</a> · <a href="/pdfs/td2_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_aides)</a> · <a href="/pdfs/td2_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td2_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_PhV212_corrige)</a> · <a href="/pdfs/td2_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_corrige)</a>

### Exercice 2. Onde stationnaire, tube de Kundt ouvert

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 40 min · Type : Application*

Un haut-parleur en $x=0$ émet une onde acoustique dans un tube d'air de
longueur $L$, ouvert aux deux extrémités ($x=0$ et $x=L$). Déplacement
incident $\Psi_I(x,t)=A_I e^{i(\omega t - kx)}$, avec $k=\omega/c$. À la
réflexion en $x=L$ (extrémité ouverte), le déplacement réfléchi s'écrit
$\Psi_R(x,t)=A_I e^{i(\omega t - k(2L-x))}$.


> [!question]- 🪝 Accroche
> **Pourquoi un tuyau ouvert sonne-t-il sur des notes précises ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *Soufflez en travers d'une bouteille ou d'un tube : il ne résonne que sur certaines notes. Dans un tube ouvert aux deux bouts, que se passe-t-il à l'extrémité ouverte : le fluide y est-il **immobile** ou **libre de bouger** ? Et la pression, y est-elle maximale ou égale à la pression ambiante ?*
>
> **Idée clé : une onde stationnaire est la somme d'une onde incidente et d'une onde réfléchie.** Pour une extrémité ouverte, le déplacement est maximal (ventre de déplacement) mais la surpression est nulle (nœud de pression, car l'extérieur impose la pression atmosphérique) :
> $$\Psi=2A_I\cos\big(k(L-x)\big)e^{i(\omega t-kL)},\qquad\tilde p=-2A_I\rho_0c\,\omega\sin\big(k(L-x)\big)e^{i(\omega t-kL)}.$$
> Les profils de $\Psi$ et de $p$ sont en **quadrature spatiale** ($\cos$ contre $\sin$). La condition $p(0)=0$ impose $\sin(kL)=0$, donc $f_n=n\,c/(2L)$ : **tous** les harmoniques sont permis.




> [!abstract]- 🧠 À savoir avant
> **Notation complexe et onde progressive**
>
> Connaître le principe de la notation complexe en acoustique : une grandeur physique réelle $\psi(x,t)$ est associée à une grandeur complexe $\tilde\psi(x,t)$ telle que $\psi = \mathrm{Re}(\tilde\psi)$, ce qui permet de manipuler des exponentielles plutôt que des sinus/cosinus tout en linéarisant les opérations de dérivation.
>
> Connaître la forme générale d'une onde acoustique plane progressive dans la direction $+x$, $\tilde\Psi(x,t) = A\,e^{i(\omega t - kx)}$, avec $k = \omega/c$ la relation de dispersion (non dispersive) des ondes acoustiques dans un fluide homogène.
>
> Savoir que le principe de superposition s'applique : toute combinaison linéaire de solutions de l'équation de d'Alembert en est encore solution.




> [!info]- 🎯 Ce que tu sauras faire
> **Construire une onde stationnaire par superposition**
>
> Savoir construire explicitement une onde stationnaire comme la somme d'une onde incidente et d'une onde réfléchie, factoriser la partie spatiale et la partie temporelle, et interpréter physiquement cette séparation des variables (immobilité du profil spatial, oscillation uniquement temporelle).
>
> Savoir traduire une condition aux limites physique (extrémité ouverte ou fermée) en une condition mathématique sur le champ de déplacement ou de pression, et en déduire les fréquences propres du système.




> [!tip]- 📖 Rappel de cours
> **Ondes stationnaires et conditions aux limites acoustiques**
>
> Une onde stationnaire résulte de la superposition d'une onde incidente et d'une onde réfléchie de même amplitude, de sens de propagation opposés. Pour le déplacement,
> $$\tilde\Psi(x,t) = \tilde\Psi_I(x,t) + \tilde\Psi_R(x,t),$$
> et le calcul mène systématiquement à une forme du type $\tilde\Psi(x,t) = f(x)\,e^{i(\omega t + \varphi)}$ : la dépendance spatiale $f(x)$ (réelle, à un facteur de phase près) est figée dans le temps, seule la phase temporelle $e^{i\omega t}$ évolue — d'où le qualificatif de « stationnaire », par opposition à une onde progressive dont le profil se translate.
>
> La condition physique à une extrémité **ouverte** est que la pression y reste égale à la pression atmosphérique extérieure (imposée par un réservoir infini d'air ambiant) : c'est donc un **nœud de surpression**, $p=0$. Réciproquement, le fluide y est libre de se déplacer : c'est un **ventre de déplacement**.
>
> La condition physique à une extrémité **fermée** (paroi rigide) est que le fluide ne peut pas traverser la paroi : la vitesse normale, donc le déplacement, y est nul — c'est un **nœud de déplacement**, et par conséquent un **ventre de surpression** (la pression peut y varier librement).
>
> Pour un tube ouvert aux deux extrémités, on impose donc un nœud de pression en $x=0$ *et* en $x=L$ : cette double condition, tout à fait analogue à celle d'une corde vibrante fixée à ses deux extrémités (mais portant ici sur la pression et non le déplacement), sélectionne un ensemble discret de fréquences propres — les harmoniques du tube.
>
> **Remarque méthodologique importante** (utile pour les questions 4 et 5) : l'expression de $\Psi_R$ donnée dans l'énoncé encode déjà, par construction, la condition de nœud de pression en $x=L$ (c'est ce qui a permis de l'écrire). La quantification des fréquences propres provient donc de l'imposition de la *même* condition à l'*autre* extrémité $x=0$.




> [!note]- 🧮 Outils mathématiques
> **Notation complexe et partie réelle**
>
> Une grandeur réelle est la partie réelle de sa représentation complexe : $\psi=\operatorname{Re}\tilde\psi=2A_I\cos(k(L-x))\cos(\omega t-kL)$. La dérivation d'une exponentielle est plus simple que celle d'un produit trigonométrique.
>
> **Formules d'Euler : $e^{iu}+e^{-iu}=2\cos u$ et $e^{iu}-e^{-iu}=2i\sin u$**
>
> Elles permettent de factoriser la somme des deux ondes : $e^{ik(L-x)}+e^{-ik(L-x)}=2\cos(k(L-x))$. Il faut mettre en facteur $e^{-ikL}$ et ne pas le perdre en route.
>
> **Dérivée d'une fonction composée**
>
> $\dfrac{\mathrm d}{\mathrm dx}\cos\big(k(L-x)\big)=+k\sin\big(k(L-x)\big)$ : le signe $-x$ dans l'argument change le signe de la dérivée.
>
> **Quadrature : $\cos\!\left(u-\dfrac\pi2\right)=\sin u$**
>
> Dériver par rapport à $x$ décale la phase spatiale de $\pi/2$ : le profil de $p$ est décalé d'un quart de longueur d'onde par rapport à celui de $\Psi$. Un ventre de l'un est un nœud de l'autre.
>
> **Zéros du sinus et quantification**
>
> $\sin(kL)=0\Leftrightarrow kL=n\pi$ ($n\in\mathbb N^*$) ; avec $k=2\pi f/c$, $f_n=nc/(2L)$. Le cas $n=0$ est exclu (fréquence nulle).
>
> **Relation $1/\chi_S=\rho_0c^2$ et $k/\chi_S=\rho_0c\,\omega$**
>
> Pour passer de $\partial\Psi/\partial x$ à $\tilde p$, on remplace $\chi_S$ en fonction de $c$ et $\rho_0$, puis $k=\omega/c$. Vérifier l'homogénéité : $\rho_0c\,\omega\,\Psi$ est bien une pression.
>
> **Dénombrement des nœuds et ventres**
>
> Le mode $n$ a $n+1$ nœuds de pression ($x=L(1-m/n)$, $m=0,\dots,n$) et $n$ ventres au milieu de chaque intervalle, séparés de $\lambda_n/2=L/n$.



**q1.** Justifier cette expression du déplacement réfléchi par un schéma.


> [!tip]- 💡 Coup de pouce
> Une extrémité ouverte est un ventre de déplacement (pas de nœud) : le déplacement n'est pas inversé au retour, contrairement à une réflexion sur paroi rigide.




> [!example]- 📝 Solution détaillée
> **Réflexion sans inversion de signe**
>
> On peut construire l'expression de $\Psi_R$ en imaginant que l'onde incidente $\Psi_I$ poursuit fictivement sa route au-delà de $x=L$ jusqu'à un point image $x'=2L-x$ symétrique de $x$ par rapport à $L$, sans changement de signe ni d'amplitude, puis en associant à ce trajet fictif une onde réellement réfléchie qui repart vers les $x$ décroissants : $\Psi_R(x,t)=A_I e^{i(\omega t-k(2L-x))}$. Physiquement, cela traduit le fait qu'une extrémité ouverte est un **ventre de déplacement** : le fluide y oscille librement, avec la même amplitude et le même signe que l'onde incidente, exactement comme l'extrémité libre d'une corde qui réfléchit une impulsion sans l'inverser (à la différence d'une extrémité fixée, qui inverse le signe — cf. exercice 3).
>
> **Vérification directe sur la formule**
>
> On vérifie qu'en $x=L$, $\Psi_I(L,t)=A_I e^{i(\omega t-kL)}$ et $\Psi_R(L,t)=A_I e^{i(\omega t-k(2L-L))}=A_I e^{i(\omega t-kL)}$ : les deux contributions sont bien identiques en $x=L$ (même amplitude, même phase), ce qui correspond à un maximum de déplacement (ventre) et non à une annulation (nœud).



**q2.** Montrer que le déplacement résultant s'écrit
$\Psi(x,t)=2A_I\cos\big(k(L-x)\big)e^{i(\omega t-kL)}$. Justifier le nom d'onde stationnaire.


> [!tip]- 💡 Coup de pouce
> Sommez $\Psi_I+\Psi_R$ et factorisez ; une onde stationnaire a un profil spatial et une évolution temporelle qui se séparent (le terme $\cos(k(L-x))$ ne dépend pas de $t$).




> [!success]- ✅ Correction
> $\Psi(x,t)=\Psi_I+\Psi_R=2A_I\cos(k(L-x))e^{i(\omega t - kL)}$ : l'amplitude spatiale $\cos(k(L-x))$ est fixe dans le temps, seule la phase temporelle oscille -- onde stationnaire.




> [!example]- 📝 Solution détaillée
> **Calcul de la somme**
>
> On part de
> $$\Psi(x,t) = \Psi_I(x,t)+\Psi_R(x,t) = A_I e^{i(\omega t-kx)} + A_I e^{i(\omega t-k(2L-x))}.$$
> On met en facteur $A_I e^{i\omega t}$ :
> $$\Psi(x,t) = A_I e^{i\omega t}\left[e^{-ikx} + e^{-ik(2L-x)}\right] = A_I e^{i\omega t}\left[e^{-ikx} + e^{ikx-2ikL}\right].$$
> On met maintenant en facteur $e^{-ikL}$ à l'intérieur du crochet :
> $$\Psi(x,t) = A_I e^{i\omega t} e^{-ikL}\left[e^{-ik(x-L)} + e^{ik(x-L)}\right] = A_I e^{i(\omega t-kL)}\left[e^{ik(L-x)} + e^{-ik(L-x)}\right].$$
> En reconnaissant $e^{iu}+e^{-iu}=2\cos u$ avec $u=k(L-x)$, on obtient bien :
> $$\boxed{\Psi(x,t) = 2A_I\cos\big(k(L-x)\big)\,e^{i(\omega t-kL)}}.$$
>
> **Interprétation : pourquoi « onde stationnaire »**
>
> Cette expression est bien du type $f(x)\,e^{i(\omega t+\varphi_0)}$ annoncé dans le point cours : le facteur $f(x)=2A_I\cos(k(L-x))$ ne dépend pas du temps (à un facteur de phase global $e^{-ikL}$ près, indépendant de $x$), tandis que le facteur $e^{i\omega t}$ ne dépend pas de $x$. La partie réelle physique,
> $$\psi(x,t) = 2A_I\cos(k(L-x))\cos(\omega t - kL),$$
> décrit donc un profil spatial *figé* (dont l'amplitude est modulée par $\cos(k(L-x))$) qui oscille globalement en phase, sans jamais se déplacer le long de l'axe $x$ : contrairement à une onde progressive, aucun point de la courbe ne « voyage », chaque point du tube oscille sur place avec une amplitude qui dépend de sa position — d'où le nom d'onde **stationnaire**.



**q3.** Exprimer la surpression acoustique (notation complexe) $\tilde p(x,t)=-\dfrac{1}{\chi_S}\dfrac{\partial\Psi}{\partial x}$.


> [!tip]- 💡 Coup de pouce
> Dérivez simplement l'expression de $\Psi(x,t)$ trouvée en 2) par rapport à $x$, puis utilisez $1/\chi_S=\rho_0 c^2$ (cf. point cours de l'exercice 1) et $k=\omega/c$ pour simplifier.




> [!example]- 📝 Solution détaillée
> **Dérivation spatiale de $\Psi$**
>
> On dérive $\Psi(x,t) = 2A_I\cos(k(L-x))\,e^{i(\omega t-kL)}$ par rapport à $x$, en n'oubliant pas la dérivée de la fonction composée (la dérivée de $\cos(k(L-x))$ par rapport à $x$ fait apparaître un signe $+k\sin$ à cause du signe « $-x$ » à l'intérieur) :
> $$\frac{\partial\Psi}{\partial x} = 2A_I\,k\,\sin\big(k(L-x)\big)\,e^{i(\omega t-kL)}.$$
>
> **Expression de la surpression**
>
> En reportant dans $\tilde p = -\dfrac{1}{\chi_S}\dfrac{\partial\Psi}{\partial x}$ :
> $$\tilde p(x,t) = -\frac{2A_I k}{\chi_S}\sin\big(k(L-x)\big)\,e^{i(\omega t-kL)}.$$
> Or, d'après la relation $c^2=1/(\rho_0\chi_S)$ établie dans le point cours de l'exercice 1, on a $1/\chi_S=\rho_0 c^2$ ; en utilisant de plus $k=\omega/c$, il vient $k/\chi_S = \rho_0 c^2\times\omega/c=\rho_0 c\,\omega$. On obtient finalement l'expression compacte :
> $$\boxed{\tilde p(x,t) = -2A_I\,\rho_0 c\,\omega\,\sin\big(k(L-x)\big)\,e^{i(\omega t-kL)}}.$$
> On remarque que le profil spatial de la pression, en $\sin(k(L-x))$, est en **quadrature** avec celui du déplacement, en $\cos(k(L-x))$ : là où $\Psi$ est maximal (ventre), $p$ s'annule (nœud), et réciproquement — conformément à ce qu'annonçait le point cours.



**q4.** En déduire les fréquences $f_n$ de résonance en surpression, en fonction de $n\in\mathbb{N}^*$, $c$ et $L$.


> [!tip]- 💡 Coup de pouce
> Un tube ouvert-ouvert a un ventre de déplacement (donc un nœud de surpression) à chaque extrémité : condition analogue à une corde fixée aux deux bouts mais sur la pression. La condition en $x=L$ est déjà satisfaite automatiquement par construction (cf. remarque du point cours) ; il reste à imposer la même condition en $x=0$.




> [!success]- ✅ Correction
> $f_n = n\,c/(2L)$, $n\in\mathbb{N}^*$.




> [!example]- 📝 Solution détaillée
> **Vérification du nœud de pression en $x=L$ (automatique)**
>
> À partir de l'expression de $\tilde p(x,t)$ trouvée en question 3, on vérifie qu'en $x=L$ : $\sin(k(L-L))=\sin(0)=0$, donc $\tilde p(L,t)=0$ *quelle que soit la valeur de $k$* (donc de la fréquence). Ce nœud de pression en $x=L$ était en fait déjà encodé dans l'expression de $\Psi_R$ donnée dans l'énoncé (cf. remarque du point cours) : il ne fournit donc aucune information nouvelle sur la fréquence.
>
> **Condition de nœud de pression en $x=0$ : quantification**
>
> Le tube étant *également* ouvert en $x=0$, la même condition physique (nœud de pression) doit y être satisfaite :
> $$\tilde p(0,t) = -2A_I\rho_0 c\,\omega\,\sin(kL)\,e^{i(\omega t-kL)} = 0 \quad\Longrightarrow\quad \sin(kL)=0.$$
> Cette équation n'est vérifiée que pour des valeurs discrètes de $k$ :
> $$kL = n\pi, \qquad n\in\mathbb{N}^*.$$
> (on exclut $n=0$, qui correspondrait à $k=0$, c'est-à-dire à une fréquence nulle, non physique). En utilisant $k=\omega/c=2\pi f/c$, on obtient :
> $$\frac{2\pi f_n}{c}L = n\pi \quad\Longrightarrow\quad \boxed{f_n = \frac{n\,c}{2L}}, \qquad n\in\mathbb{N}^*.$$
> C'est cette discrétisation des valeurs possibles de $f$ (et donc de $k$) qui constitue la résonance du tube : seules ces fréquences particulières permettent d'établir une onde stationnaire compatible avec les deux conditions aux limites simultanément.



**q5.** Positions des maxima/minima de surpression ; représenter graphiquement jusqu'à la 3e harmonique (n=4).


> [!tip]- 💡 Coup de pouce
> Les nœuds de pression sont aux extrémités ouvertes, les ventres au milieu des segments -- comme les nœuds/ventres de déplacement pour une corde fixée.




> [!example]- 📝 Solution détaillée
> **Formule générale des nœuds et ventres pour l'harmonique $n$**
>
> Pour le mode propre $n$, on a $k_n = n\pi/L$, soit une longueur d'onde $\lambda_n = 2\pi/k_n = 2L/n$. Le profil spatial de la surpression, en $|\sin(k_n(L-x))|$, s'annule (nœuds) lorsque $k_n(L-x)=m\pi$ ($m$ entier), soit :
> $$x_m^{\text{nœud}} = L - \frac{m\lambda_n}{2} = L\left(1-\frac{m}{n}\right), \qquad m=0,1,\dots,n,$$
> ce qui donne $n+1$ nœuds régulièrement espacés de $L/n$, incluant nécessairement les deux extrémités $x=0$ et $x=L$ (cohérent avec le fait que les deux bouts sont ouverts). Les ventres (maxima de $|p|$) se situent exactement à mi-chemin entre deux nœuds consécutifs, soit
> $$x_m^{\text{ventre}} = L\left(1-\frac{2m-1}{2n}\right), \qquad m=1,\dots,n.$$
>
> **Application aux quatre premiers harmoniques**
>
> - $n=1$ ($f_1=c/2L$) : 2 nœuds (en $x=0$ et $x=L$), 1 ventre unique au milieu $x=L/2$.
> - $n=2$ ($f_2=c/L$) : 3 nœuds ($x=0,\,L/2,\,L$), 2 ventres ($x=L/4,\,3L/4$).
> - $n=3$ ($f_3=3c/2L$) : 4 nœuds ($x=0,\,L/3,\,2L/3,\,L$), 3 ventres ($x=L/6,\,L/2,\,5L/6$).
> - $n=4$ ($f_4=2c/L$) : 5 nœuds ($x=0,\,L/4,\,L/2,\,3L/4,\,L$), 4 ventres ($x=L/8,\,3L/8,\,5L/8,\,7L/8$).
>
>
> On retrouve la structure classique : le mode $n$ possède $n$ ventres et $n+1$ nœuds, régulièrement répartis, tout à fait analogue aux modes propres d'une corde vibrante (mais avec les rôles de nœud/ventre échangés entre déplacement et pression).




> [!note]- 🔗 Liens avec d'autres disciplines
> **Cordes vibrantes (chapitre 1)**
>
> Les nœuds de pression d'un tube ouvert-ouvert jouent le rôle des nœuds de déplacement d'une corde fixée aux deux extrémités : mêmes fréquences $f_n=nc/(2L)$ avec $c=\sqrt{F/\mu}$ remplacé par la célérité du son.
>
> **Musique et lutherie**
>
> Flûte traversière, flûte à bec, tuyau d'orgue ouvert : tube ouvert-ouvert, tous les harmoniques, donc un timbre « brillant ». L'instrumentiste modifie $L$ en bouchant ou en ouvrant des trous.
>
> **Optique et lasers**
>
> Une cavité laser ou un résonateur de Fabry-Pérot sélectionne des fréquences telles que $L=n\lambda/2$ : même condition de quantification.
>
> **Mécanique quantique**
>
> La particule dans un puits de largeur $L$ a des fonctions d'onde en $\sin(n\pi x/L)$ : nœuds aux bords, comme la pression dans un tube ouvert-ouvert.
>
> **Ingénierie acoustique**
>
> Les silencieux, conduits de ventilation et tuyaux d'échappement ont des résonances dues à ces ondes stationnaires. La correction de longueur d'extrémité ($\approx0{,}6\,r$ par bout ouvert) est nécessaire pour accorder un instrument.




> [!question]- 🔭 Aller plus loin — Licence : Correction de longueur d'extrémité (« end correction »)
> En pratique, une extrémité ouverte n'est pas un nœud de pression parfait : le rayonnement acoustique dans l'espace libre au-delà du tube introduit une « longueur effective » supplémentaire, de l'ordre de $0{,}6\,r$ ($r$ rayon du tube) par extrémité ouverte. Les fréquences de résonance réelles sont alors légèrement décalées : $f_n \approx n\,c/(2(L+2\times 0{,}6\,r))$. On pourra proposer une mesure expérimentale simple (mesure de $f_1$ à $L$ et $r$ connus) pour mettre en évidence cet écart avec le modèle idéal.




> [!question]- 🔭 Aller plus loin — Master : Guides d'onde acoustiques avec écoulement moyen
> Dans un conduit parcouru par un écoulement moyen (silencieux automobile, conduit de ventilation), l'équation de propagation se modifie (équation convective) et les modes propres dépendent du nombre de Mach de l'écoulement ; on peut également s'intéresser aux modes de section variable (équation de Webster) qui gouvernent, par exemple, l'acoustique des instruments à vent de forme conique.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex3-onde-stationnaire-tube-de-kundt-ferme-a-faire-a-la-maison|Exercice 3 — Onde stationnaire, tube de Kundt fermé (à faire à la maison)]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex5-energie-intensite-acoustique-et-niveau-sonore-de-l-oreille-humaine-a-l-onde-stationnaire|Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex6-tube-d-impedance-mesurer-l-absorption-d-un-materiau-avec-une-onde-stationnaire-partielle|Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]]


