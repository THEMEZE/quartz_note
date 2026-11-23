---
title: "Exercice 4 — Réflexion et transmission d'une onde acoustique à une interface entre deux fluides"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · <a href="/pdfs/td2_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_PhV212_enonce)</a> · <a href="/pdfs/td2_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_enonce)</a> · <a href="/pdfs/td2_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_aides)</a> · <a href="/pdfs/td2_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td2_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_PhV212_corrige)</a> · <a href="/pdfs/td2_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_corrige)</a>

### Exercice 4. Réflexion et transmission d'une onde acoustique à une interface entre deux fluides *(facultatif)*

*Difficulté ●●●●○ · ⏱ 45 min · Type : Approfondissement / ouverture*

On considère deux fluides parfaits semi-infinis séparés par une interface
plane en $x=0$ : le fluide (1), de masse volumique $\rho_1$ et de célérité
du son $c_1$, occupe la région $x<0$ ; le fluide (2), de masse volumique
$\rho_2$ et de célérité $c_2$, occupe la région $x>0$. On définit
l'impédance acoustique caractéristique de chaque fluide par $Z_i=\rho_i c_i$.

Une onde acoustique plane, de pression $\tilde p_I(x,t)=A\,e^{i(\omega t-k_1x)}$
($k_1=\omega/c_1$), est envoyée depuis le fluide (1) vers l'interface, en
incidence normale. Elle donne naissance à une onde réfléchie dans le fluide
(1) et à une onde transmise dans le fluide (2) :
$$\tilde p_R(x,t) = R\,A\,e^{i(\omega t+k_1x)}, \qquad \tilde p_T(x,t) = T\,A\,e^{i(\omega t-k_2x)}, \qquad k_2=\omega/c_2.$$

> [!question]+ 🎣 Accroche
> **Pourquoi n'entend-on presque rien depuis sous l'eau ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *Dans une piscine, la tête sous l'eau, les voix des gens au bord de l'eau semblent très lointaines. Un échographe, lui, nécessite l'application d'un **gel** sur la peau. Un son qui passe de l'air à l'eau est-il très affaibli ? Par quel facteur, et pourquoi la **célérité** seule ne suffit-elle pas à répondre ?*
>
> **Idée clé : ce qui compte à l'interface, c'est le contraste d'impédance $Z=\rho c$.** On impose la continuité de la pression et de la vitesse normale, avec $\tilde v=\pm\tilde p/Z$ :
> $$R=\frac{Z_2-Z_1}{Z_1+Z_2},\qquad T=\frac{2Z_2}{Z_1+Z_2},\qquad R_I=R^2,\quad T_I=\frac{4Z_1Z_2}{(Z_1+Z_2)^2},\quad R_I+T_I=1.$$
> Air-eau : $Z_2/Z_1\approx3700$, donc $T_I\approx10^{-3}$ : $99{,}9\ \%$ de l'énergie est réfléchie. Le coefficient $R$ change de signe si l'onde va de l'eau vers l'air (déphasage de $\pi$), mais $R_I$ et $T_I$ restent les mêmes dans les deux sens.


> [!abstract]+ 📚 Prérequis
> **Notion d'impédance acoustique**
>
> Pour une onde plane progressive dans un fluide donné, la pression et la vitesse particulaire sont reliées, en tout point et à tout instant, par une relation de proportionnalité : $\tilde p = \pm Z\,\tilde v_x$ (signe $+$ pour une onde se propageant vers les $x$ croissants, signe $-$ pour les $x$ décroissants), où $Z=\rho c$ est l'impédance acoustique caractéristique du milieu. Cette relation, analogue à la loi d'Ohm en électrocinétique ($U=RI$), permet de traiter les problèmes de raccordement d'ondes à une interface de façon très systématique.


> [!info]+ 🎯 Objectifs
> **Traiter un problème de raccordement à une interface**
>
> Savoir écrire les conditions de continuité physiquement pertinentes à une interface fluide-fluide (continuité de la pression et de la vitesse normale), les combiner pour obtenir des coefficients de réflexion et de transmission, et interpréter physiquement un résultat en le comparant à un cas limite connu (interface avec un mur rigide, ou avec le vide).


> [!note]+ 📖 Point de cours
> **Continuité à une interface acoustique et coefficients de Fresnel acoustiques**
>
> À l'interface entre deux fluides parfaits, deux conditions physiques doivent être satisfaites à tout instant en $x=0$ :
>
> 1. **Continuité de la pression** (sinon la différence de pression de part et d'autre d'une interface de masse nulle produirait une accélération infinie) : $\tilde p_I(0,t)+\tilde p_R(0,t) = \tilde p_T(0,t)$.
>
> 2. **Continuité de la vitesse normale du fluide** (sinon les deux fluides se traverseraient ou une cavité se créerait à l'interface) : $\tilde v_I(0,t)+\tilde v_R(0,t) = \tilde v_T(0,t)$.
>
> En utilisant $\tilde v = \tilde p/Z$ pour une onde se propageant vers $x$ croissant et $\tilde v = -\tilde p/Z$ pour une onde se propageant vers $x$ décroissant, ces deux conditions s'écrivent, en notant $R$ et $T$ les coefficients de réflexion et de transmission en amplitude de pression :
> $$1+R = T, \qquad \frac{1-R}{Z_1} = \frac{T}{Z_2}.$$
>
> La résolution de ce système linéaire donne :
> $$\boxed{R = \frac{Z_2-Z_1}{Z_1+Z_2}}, \qquad \boxed{T = \frac{2Z_2}{Z_1+Z_2}}.$$
>
> Ces expressions sont formellement identiques aux coefficients de Fresnel de l'optique en incidence normale (avec l'impédance jouant le rôle de l'indice optique, à l'inverse près), ce qui illustre l'universalité des phénomènes de réflexion/transmission pour toute équation de propagation de type d'Alembert.


> [!note]- 🧮 Outils mathématiques
> **Équation d'Euler en notation complexe**
>
> Pour $\tilde p=Ae^{i(\omega t\mp kx)}$ : $\partial_x\to\mp ik$ et $\partial_t\to i\omega$. L'équation $\rho_0\partial_t\tilde v=-\partial_x\tilde p$ donne $\tilde v=\pm\tilde p/Z$ avec $k/\omega=1/c$.
>
> **Système linéaire $2\times2$**
>
> Les conditions de continuité $1+R=T$ et $\dfrac{1-R}{Z_1}=\dfrac T{Z_2}$ s'interprètent comme un système de deux équations à deux inconnues. Substituer la première dans la seconde : $Z_2(1-R)=Z_1(1+R)$.
>
> **Identité remarquable : $(a-b)^2+4ab=(a+b)^2$**
>
> Elle donne $R_I+T_I=\dfrac{(Z_2-Z_1)^2+4Z_1Z_2}{(Z_1+Z_2)^2}=1$ : conservation de l'énergie.
>
> **Développements pour un grand contraste**
>
> Pour $Z_2\gg Z_1$ : $R\approx1-\dfrac{2Z_1}{Z_2}$ et $T_I\approx\dfrac{4Z_1}{Z_2}$. Avec $Z_1/Z_2\approx2{,}7\times10^{-4}$ : $T_I\approx1{,}1\times10^{-3}$, valeur retrouvée par le calcul exact.
>
> **Décibels**
>
> $10\log_{10}T_I=10\log_{10}(1{,}09\times10^{-3})\approx-29{,}6$ dB : une perte de transmission d'environ $30$ dB, ordre de grandeur de l'atténuation air-eau.
>
> **Signe, déphasage et réciprocité**
>
> $R<0\Leftrightarrow Z_2<Z_1$ : déphasage de $\pi$ ($e^{i\pi}=-1$). L'expression de $T_I$ est symétrique en $Z_1\leftrightarrow Z_2$, d'où la même énergie transmise dans les deux sens.
>
> **Loi de Snell-Descartes (ouverture)**
>
> En incidence oblique, $\dfrac{\sin\theta_1}{c_1}=\dfrac{\sin\theta_2}{c_2}$ ; si $c_2>c_1$, il existe un angle critique $\theta_c=\arcsin(c_1/c_2)$ au-delà duquel l'onde est totalement réfléchie.


**q1.** Définir l'impédance acoustique caractéristique $Z=\rho c$ d'un fluide et
donner son interprétation physique (on pourra s'appuyer sur l'analogie
avec l'impédance électrique). Écrire, en notation complexe, les
expressions de la vitesse particulaire associée à chacune des trois
ondes (incidente, réfléchie, transmise) en fonction de la pression et
des impédances $Z_1$, $Z_2$.

> [!tip]- 💡 Coup de pouce
> Pour une onde plane progressive $\tilde p = A e^{i(\omega t \mp kx)}$, l'équation d'Euler linéarisée $\rho_0\partial_t \tilde v = -\partial_x \tilde p$ donne directement $\tilde v = \pm \tilde p /Z$ selon le sens de propagation (cf. point cours de l'exercice 1 pour l'équation d'Euler linéarisée).


> [!example]- 📝 Solution détaillée
> **Établissement de $\tilde v = \pm\tilde p/Z$**
>
> On repart de l'équation d'Euler linéarisée $\rho_0 \partial_t \tilde v = -\partial_x \tilde p$. Pour une onde progressive vers les $x$ croissants, $\tilde p = A\,e^{i(\omega t-kx)}$, on a $\partial_x\tilde p = -ik\tilde p$ et $\partial_t \tilde v = i\omega \tilde v$, d'où :
> $$\rho_0\,i\omega\,\tilde v = ik\,\tilde p \quad\Longrightarrow\quad \tilde v = \frac{k}{\rho_0\omega}\,\tilde p = \frac{\tilde p}{\rho_0 c} = \frac{\tilde p}{Z},$$
> en utilisant $k/\omega = 1/c$. Pour une onde progressive vers les $x$ décroissants, $\tilde p = A\,e^{i(\omega t+kx)}$, le même calcul donne un signe opposé : $\tilde v = -\tilde p/Z$. On retient donc $Z=\rho c$, homogène à une pression divisée par une vitesse (comme une impédance électrique $U/I$ est une tension divisée par un courant) : $Z$ mesure la « résistance » qu'oppose le fluide à être mis en mouvement par une onde de pression donnée — un fluide de forte impédance (l'eau) nécessite une pression bien plus grande qu'un fluide de faible impédance (l'air) pour atteindre la même vitesse particulaire.
>
> **Application aux trois ondes du problème**
>
> - Onde incidente, dans le fluide (1), se propageant vers $+x$ : $\tilde v_I = \tilde p_I/Z_1$.
> - Onde réfléchie, dans le fluide (1), se propageant vers $-x$ (elle repart vers les $x$ décroissants après réflexion) : $\tilde v_R = -\tilde p_R/Z_1$.
> - Onde transmise, dans le fluide (2), se propageant vers $+x$ : $\tilde v_T = \tilde p_T/Z_2$.


**q2.** En écrivant la continuité de la pression et de la vitesse particulaire
en $x=0$, établir les expressions des coefficients de réflexion $R$ et
de transmission $T$ en amplitude de pression, en fonction de $Z_1$ et $Z_2$.

> [!tip]- 💡 Coup de pouce
> Deux équations, deux inconnues ($R$ et $T$) : substituez l'une dans l'autre (cf. les deux équations déjà posées dans le point cours).


> [!success]- ✅ Correction
> $R = (Z_2-Z_1)/(Z_1+Z_2)$ ; $T = 2Z_2/(Z_1+Z_2)$.


> [!example]- 📝 Solution détaillée
> **Mise en équations en $x=0$**
>
> En $x=0$, les pressions valent $\tilde p_I=A$, $\tilde p_R=RA$, $\tilde p_T=TA$ (on factorise $e^{i\omega t}$, commun à toutes les ondes, et on l'omet par la suite). La continuité de la pression, $\tilde p_I+\tilde p_R=\tilde p_T$, donne directement :
> $$1+R = T. \qquad (\star)$$
> En utilisant les expressions de $\tilde v$ établies en question 1, la continuité de la vitesse, $\tilde v_I+\tilde v_R=\tilde v_T$, s'écrit :
> $$\frac{A}{Z_1} - \frac{RA}{Z_1} = \frac{TA}{Z_2} \quad\Longrightarrow\quad \frac{1-R}{Z_1} = \frac{T}{Z_2}. \qquad (\star\star)$$
>
> **Résolution du système**
>
> On substitue $T=1+R$ (équation $\star$) dans l'équation $\star\star$ :
> $$\frac{1-R}{Z_1} = \frac{1+R}{Z_2} \quad\Longrightarrow\quad Z_2(1-R) = Z_1(1+R) \quad\Longrightarrow\quad Z_2 - Z_1 = R(Z_1+Z_2),$$
> d'où :
> $$\boxed{R = \frac{Z_2-Z_1}{Z_1+Z_2}}.$$
> En reportant dans $T=1+R$ :
> $$T = 1 + \frac{Z_2-Z_1}{Z_1+Z_2} = \frac{Z_1+Z_2+Z_2-Z_1}{Z_1+Z_2} = \boxed{\frac{2Z_2}{Z_1+Z_2}}.$$
> On retrouve exactement les expressions rappelées dans le point cours, ici entièrement redémontrées à partir des deux conditions de continuité.


**q3.** Application numérique : calculer $R$, $T$, et les coefficients
énergétiques $R_I$ et $T_I$ pour une onde issue de l'air
($\rho_1=1{,}2\text{ kg}\cdot\text{m}^{-3}$, $c_1=340\text{ m}\cdot\text{s}^{-1}$)
incidente sur une surface d'eau
($\rho_2=1000\text{ kg}\cdot\text{m}^{-3}$, $c_2=1500\text{ m}\cdot\text{s}^{-1}$).
Commenter en lien avec l'expérience quotidienne.

> [!tip]- 💡 Coup de pouce
> Calculez d'abord $Z_1$ et $Z_2$ séparément, en gardant les unités SI.


> [!success]- ✅ Correction
> $Z_1\approx 408$ ; $Z_2 = 1{,}5\times10^6$ (SI) ; $T_I\approx 1{,}1\times10^{-3}$ : moins de 0,2 % de l'énergie sonore incidente est transmise dans l'eau -- ce qui explique qu'un son émis dans l'air soit très fortement atténué en pénétrant sous la surface.


> [!example]- 📝 Solution détaillée
> **Calcul des impédances**
>
> $$Z_1 = \rho_1 c_1 = 1{,}2\times 340 = 408~\text{kg}\cdot\text{m}^{-2}\cdot\text{s}^{-1},$$
> $$Z_2 = \rho_2 c_2 = 1000\times 1500 = 1{,}5\times10^6~\text{kg}\cdot\text{m}^{-2}\cdot\text{s}^{-1}.$$
> On note immédiatement $Z_2/Z_1 \approx 3676$ : un désaccord d'impédance considérable, de plus de trois ordres de grandeur.
>
> **Coefficients en amplitude**
>
> $$R = \frac{Z_2-Z_1}{Z_1+Z_2} = \frac{1{,}5\times10^6-408}{1{,}5\times10^6+408} \approx \frac{1{,}4996\times10^6}{1{,}5004\times10^6} \approx 0{,}9995,$$
> $$T = \frac{2Z_2}{Z_1+Z_2} = \frac{3{,}0\times10^6}{1{,}5004\times10^6} \approx 1{,}9995 \approx 2{,}0.$$
> On remarque que $T$ est proche de $2$, donc supérieur à $1$ : ceci n'est pas contradictoire, car $T$ est un coefficient de transmission en *amplitude de pression*, pas en énergie — la pression peut tout à fait quasi-doubler à l'interface (comme au voisinage d'une paroi rigide, cas limite $Z_2\to\infty$ pour lequel $T\to 2$ exactement) tout en ne transportant qu'une énergie transmise infime, comme le montre le calcul suivant.
>
> **Coefficients énergétiques et conclusion physique**
>
> $$R_I = R^2 \approx (0{,}9995)^2 \approx 0{,}999,$$
> $$T_I = \frac{4Z_1Z_2}{(Z_1+Z_2)^2} = \frac{4\times408\times1{,}5\times10^6}{(1{,}5004\times10^6)^2} \approx \frac{2{,}448\times10^9}{2{,}251\times10^{12}} \approx 1{,}09\times10^{-3}.$$
> On vérifie $R_I+T_I\approx 0{,}999+0{,}0011\approx 1$ (conservation de l'énergie). Ainsi, environ $99{,}9\%$ de l'énergie acoustique incidente est réfléchie, et seulement environ $0{,}1\%$ est transmise dans l'eau. C'est cette valeur extrêmement faible de $T_I$ qui explique l'expérience quotidienne : un son émis dans l'air est presque totalement réfléchi à la surface de l'eau, ce qui rend très difficile d'entendre, depuis sous l'eau, un son provenant de l'air (et réciproquement).


**q4.** On envoie maintenant l'onde depuis l'eau vers l'air (mêmes fluides
qu'en question 3, ordre inversé). Recalculer $R$ et commenter le signe
obtenu. Ce résultat est-il cohérent avec le principe de retour inverse
de la lumière (ici, du son) ?

> [!tip]- 💡 Coup de pouce
> Échangez les rôles de $Z_1$ et $Z_2$ dans l'expression de $R$ établie en question 2.


> [!success]- ✅ Correction
> $R$ change de signe (devient positif) mais $|R|$ et $T_I$ restent inchangés : la fraction d'énergie réfléchie/transmise ne dépend pas du sens de propagation, seul le signe (la phase) du coefficient de réflexion en amplitude change.


> [!example]- 📝 Solution détaillée
> **Calcul avec les rôles échangés**
>
> L'onde se propage maintenant depuis l'eau (nouveau milieu « 1 », d'impédance $Z_1'=Z_{\text{eau}}=1{,}5\times10^6$) vers l'air (nouveau milieu « 2 », d'impédance $Z_2'=Z_{\text{air}}=408$). D'après la formule générale établie en question 2 :
> $$R' = \frac{Z_2'-Z_1'}{Z_1'+Z_2'} = \frac{408 - 1{,}5\times10^6}{1{,}5\times10^6+408} \approx -0{,}9995 = -R.$$
> Le coefficient de réflexion change bien de signe par rapport à la question 3.
>
> **Interprétation physique du changement de signe**
>
> Ce changement de signe traduit un déphasage de $\pi$ de l'onde réfléchie par rapport à l'onde incidente, qui apparaît précisément lorsque l'onde passe d'un milieu de *plus forte* impédance vers un milieu de *plus faible* impédance ($Z_2'<Z_1'$ ici), exactement comme en optique le déphasage à la réflexion apparaît lorsque la lumière passe d'un milieu de fort indice vers un milieu de faible indice (ou l'inverse, selon la convention choisie) : l'impédance acoustique joue ici un rôle analogue à l'indice optique.
>
> **Compatibilité avec la réciprocité acoustique**
>
> On vérifie que les grandeurs *énergétiques* sont bien invariantes par échange des deux milieux : $R_I' = (R')^2 = R^2 = R_I$ et $T_I' = \dfrac{4Z_1'Z_2'}{(Z_1'+Z_2')^2} = \dfrac{4Z_2Z_1}{(Z_2+Z_1)^2} = T_I$ (l'expression est manifestement symétrique en $Z_1\leftrightarrow Z_2$). Ce résultat est bien cohérent avec un principe de réciprocité : la fraction d'énergie réfléchie ou transmise à une interface ne dépend que du contraste d'impédance $|Z_2-Z_1|/(Z_1+Z_2)$, indépendamment du sens de propagation de l'onde. Seule la phase (le signe) du coefficient de réflexion en amplitude distingue les deux sens de propagation, exactement comme en optique où le module du coefficient de Fresnel est identique dans les deux sens, mais son signe (son déphasage) dépend du sens de traversée de l'interface.


> [!note]- 🔗 Liens avec d'autres disciplines
> **Optique**
>
> Les formules sont celles de Fresnel en incidence normale : la réflexion air-verre en optique est $R_I=\left(\dfrac{n_1-n_2}{n_1+n_2}\right)^2\approx4\ \%$. L'impédance joue le rôle de l'indice, et le déphasage de $\pi$ à la réflexion existe aussi en optique.
>
> **Électricité (lignes et câbles)**
>
> Une onde de tension dans un câble coaxial se réfléchit à une charge d'impédance $Z_L$ avec $R=(Z_L-Z_0)/(Z_L+Z_0)$ : même formule, d'où l'adaptation d'impédance (et la loi d'Ohm $Z=U/I$ évoquée dans l'énoncé).
>
> **Imagerie médicale**
>
> L'échographie exploite les **contrastes d'impédance** entre tissus (muscle, graisse, os) : chaque interface renvoie un écho dont l'amplitude donne $R$ et dont le retard donne la profondeur $d=c\,\Delta t/2$. Le gel supprime l'air entre la sonde et la peau, qui réfléchirait presque tout.
>
> **Géophysique et sismologie**
>
> La prospection sismique repose sur les réflexions aux interfaces entre couches d'impédances différentes ; l'angle critique et la réflexion totale expliquent le guidage des ondes (canal SOFAR sous-marin).
>
> **Architecture et isolation phonique**
>
> Un mur lourd et rigide a une impédance très supérieure à celle de l'air : l'essentiel de l'énergie est réfléchie. Les doubles vitrages exploitent la même idée avec des couches d'air d'impédance très différente.


> [!question]- 🔭 Aller plus loin — Master : Incidence oblique et angle critique
> En incidence oblique (angle $\theta_1$ par rapport à la normale), la continuité de la phase le long de l'interface impose une relation de Snell-Descartes acoustique, $\dfrac{\sin\theta_1}{c_1}=\dfrac{\sin\theta_2}{c_2}$. Lorsque $c_2>c_1$, il existe un angle critique $\theta_c=\arcsin(c_1/c_2)$ au-delà duquel l'onde transmise devient évanescente (réflexion totale) : ce phénomène est à la base de la propagation guidée du son dans certains canaux sous-marins (canal SOFAR) exploités en acoustique sous-marine.


> [!question]- 🔭 Aller plus loin — Doctorat : Interfaces multiples et adaptation d'impédance
> Pour une lame de fluide (ou de solide) d'épaisseur finie insérée entre les deux milieux, on peut chercher à choisir son impédance et son épaisseur (couche « quart d'onde ») de façon à annuler la réflexion à une fréquence donnée : c'est le principe des traitements antireflets acoustiques ou optiques, et plus généralement de l'adaptation d'impédance utilisée en instrumentation ultrasonore médicale (gel de couplage entre la sonde et la peau).


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex5-energie-intensite-acoustique-et-niveau-sonore-de-l-oreille-humaine-a-l-onde-stationnaire|Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex6-tube-d-impedance-mesurer-l-absorption-d-un-materiau-avec-une-onde-stationnaire-partielle|Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex7-resonateur-de-helmholtz-la-bouteille-qui-chante|Exercice 7 — Résonateur de Helmholtz : la bouteille qui chante]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex1-celerite-d-une-onde-acoustique-dans-un-fluide-parfait|Exercice 1 — Célérité d'une onde acoustique dans un fluide parfait]]

