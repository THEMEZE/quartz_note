---
title: "Exercice 5 — Complément (niveau 1, CPGE) : pendules couplés par un ressort attaché à mi-hauteur"
tags:
  - td
  - chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/index|⬅ Retour]] · <a href="/pdfs/td4_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 5. Complément (niveau 1, CPGE) : pendules couplés par un ressort attaché à mi-hauteur *(facultatif)*

*Difficulté ●●●○○ · ⏱ 60 min · Type : Complément original, entraînement de type CPGE/concours*

**Exercice complémentaire original (niveau 1).** Deux pendules simples identiques sont formés chacun d'une tige rigide de masse négligeable, de longueur $\ell=1{,}00$ m, suspendue en un point fixe $O_i$ ($i=1,2$) et portant à son extrémité une masse ponctuelle $m=0{,}20$ kg. Les points de suspension sont alignés sur une horizontale, séparés de $d$. Un ressort de raideur $k=0{,}40\ \mathrm{N\cdot m^{-1}}$ et de longueur à vide $d$ est accroché aux deux tiges en des points $P_1$ et $P_2$ situés *à la distance $h=\ell/2$ de leur point de suspension*, et non aux masses. Au repos, les tiges sont verticales et le ressort est horizontal et non déformé. Les angles $\alpha_1$ et $\alpha_2$ des tiges avec la verticale descendante sont comptés positivement vers $+x$. Les masses se déplacent dans le plan vertical $(Oxy)$, sans frottement, $g=9{,}81\ \mathrm{m\cdot s^{-2}}$.

Cet exercice reprend la méthode de l'exercice 1 en déplaçant le point d'attache du ressort : il illustre que le couplage dépend de la géométrie, pas seulement de $k$.


> [!question]- 🪝 Accroche
> **Où accrocher le ressort ?**
>
> *Durée de l'introduction : 3 min*
>
> *Deux pendules identiques sont reliés par un ressort. Peut-on rendre le couplage plus faible sans changer le ressort ? Comment ?*
>
> **Idée clé : le couplage est un moment, donc un produit force $\times$ bras de levier.** Déplacer le point d'attache le long de la tige modifie le bras de levier et l'allongement : le coefficient de couplage est multiplié par $(h/\ell)^2$.




> [!abstract]- 🧠 À savoir avant
> **Exercice 1 du TD4**
>
> Base locale du pendule $(\vec e_r,\vec e_\alpha)$, équations exactes, linéarisation, découplage par $S=\alpha_1+\alpha_2$ et $D=\alpha_1-\alpha_2$.
>
> **Moment d'une force par rapport à un point fixe**
>
> Théorème du moment cinétique en $O_i$ : $J\ddot\alpha_i=\mathcal M_{O_i}$ avec $J=m\ell^2$ ; moment d'une force $\vec F$ appliquée en un point $P$ : $\overrightarrow{O_iP}\wedge\vec F$.
>
> **Battements**
>
> $\sin a+\sin b=2\sin\frac{a+b}2\cos\frac{a-b}2$ ; période de battement $T_b=\dfrac{2\pi}{\omega_2-\omega_1}$.




> [!info]- 🎯 Ce que tu sauras faire
> **Utiliser le théorème du moment cinétique plutôt que la tension**
>
> Quand le ressort n'est pas accroché à la masse, la force de couplage n'est plus colinéaire à la vitesse : c'est le moment par rapport à $O_i$ qui élimine la tension de la tige.
>
> **Comprendre comment la géométrie fixe le couplage**
>
> Montrer que $\omega_c^2=\dfrac km\Big(\dfrac h\ell\Big)^2$ : le même ressort couple d'autant plus faiblement qu'il est accroché près du point de suspension.
>
> **Relier battements et échange d'énergie**
>
> Calculer la fraction d'énergie stockée dans le ressort, et le temps de transfert complet d'un pendule à l'autre.




> [!note]- 🧮 Outils mathématiques
> **Théorème du moment cinétique**
>
> $J\ddot\alpha_i=\mathcal M_{O_i}(\text{poids})+\mathcal M_{O_i}(\text{ressort})$ ; la tension de la tige n'a pas de moment en $O_i$ (elle est colinéaire à $\overrightarrow{O_iM}$).
>
> **Application numérique**
>
> $\omega_0^2=9{,}81$, $\omega_0=3{,}132\ \mathrm{rad\cdot s^{-1}}$ ; $\omega_c^2=\dfrac{0{,}40}{0{,}20}\times0{,}25=0{,}50$ ; $\omega_2^2=10{,}81$, $\omega_2=3{,}288$ ; $T_b=\dfrac{2\pi}{0{,}1558}=40{,}3$ s.



**q1.** **Question 1.** *Sans approximation.* Exprimer en fonction de $\alpha_1,\alpha_2$ les coordonnées de $P_1$ et $P_2$, la longueur du ressort et la force qu'il exerce sur $P_1$. En déduire, par le théorème du moment cinétique en $O_1$, l'équation exacte vérifiée par $\alpha_1$.


> [!tip]- 💡 Coup de pouce
> **Base locale**
>
> Pour la tige $i$ : $\vec e_{r,i}=(\sin\alpha_i,-\cos\alpha_i)$ ; donc $\overrightarrow{O_iP_i}=h\,\vec e_{r,i}$ et $\overrightarrow{O_iM_i}=\ell\,\vec e_{r,i}$.
>
> **Quelle composante du ressort ?**
>
> $P_1P_2$ n'est pas exactement horizontal : calculez ses composantes $(u,v)$ puis la longueur $\sqrt{u^2+v^2}$.
>
> **Moment**
>
> $\mathcal M_{O_1}(\vec F)=\overrightarrow{O_1P_1}\wedge\vec F$ : seule la composante de $\vec F$ perpendiculaire à la tige compte, soit $\vec F\cdot\vec e_{\alpha,1}$, multipliée par $h$.




> [!success]- ✅ Correction
> **Équation exacte**
>
> $u=d+h(\sin\alpha_2-\sin\alpha_1)$, $v=h(\cos\alpha_1-\cos\alpha_2)$, $\ell_s=\sqrt{u^2+v^2}$ ;
> $$m\ell^2\ddot\alpha_1=-mg\ell\sin\alpha_1+h\,k\,\frac{\ell_s-d}{\ell_s}\,(u\cos\alpha_1+v\sin\alpha_1).$$




> [!example]- 📝 Solution détaillée
> **Coordonnées**
>
> Origine en $O_1$, $\vec e_x$ vers la droite, $\vec e_y$ vers le haut : $P_1=h(\sin\alpha_1,-\cos\alpha_1)$, $P_2=(d,0)+h(\sin\alpha_2,-\cos\alpha_2)$. Donc
> $$\overrightarrow{P_1P_2}=u\,\vec e_x+v\,\vec e_y,\qquad u=d+h(\sin\alpha_2-\sin\alpha_1),\quad v=h(\cos\alpha_1-\cos\alpha_2),\quad\ell_s=\sqrt{u^2+v^2}.$$
> $v$ est la différence de deux termes $1-\alpha^2/2+\dots$ : $v=\tfrac h2(\alpha_2^2-\alpha_1^2)+\dots$ est d'ordre $2$.
>
> **Force sur $P_1$**
>
> Allongement algébrique $\ell_s-d$ ; le ressort tendu tire $P_1$ vers $P_2$ : $\vec F_1=k(\ell_s-d)\,\overrightarrow{P_1P_2}/\ell_s$.
>
> **Théorème du moment cinétique en $O_1$**
>
> Le point fixe $O_1$ est dans un référentiel galiléen ; le moment cinétique de la masse est $J\dot\alpha_1$ avec $J=m\ell^2$ (mouvement plan, rayon constant). Moments : poids $\vec P=-mg\vec e_y$ en $M_1$ : $\overrightarrow{O_1M_1}\wedge\vec P=-mg\ell\sin\alpha_1\,\vec e_z$ (levier horizontal $\ell\sin\alpha_1$) ; tension de la tige : nul (colinéaire à $\overrightarrow{O_1M_1}$) ; ressort : $\overrightarrow{O_1P_1}\wedge\vec F_1=h\,\vec e_{r,1}\wedge\vec F_1$, dont la composante selon $\vec e_z$ est $h\,\vec F_1\cdot\vec e_{\alpha,1}=h\,k\dfrac{\ell_s-d}{\ell_s}(u\cos\alpha_1+v\sin\alpha_1)$ avec $\vec e_{\alpha,1}=(\cos\alpha_1,\sin\alpha_1)$. D'où l'équation exacte ci-dessus. Pour la tige 2, par symétrie, $m\ell^2\ddot\alpha_2=-mg\ell\sin\alpha_2-hk\dfrac{\ell_s-d}{\ell_s}(u\cos\alpha_2+v\sin\alpha_2)$.
>
> **Contrôle**
>
> Si $h=0$ : plus de couplage, deux pendules indépendants. Si $h=\ell$ : on retrouve l'équation de l'exercice 1. Les deux équations sont non linéaires et couplées.



**q2.** **Question 2.** *Petits angles.* Linéariser les deux équations à l'ordre $1$ en $\alpha_1,\alpha_2$. Justifier que l'inclinaison du ressort est négligeable. Définir $\omega_0$ et $\omega_c$.


> [!tip]- 💡 Coup de pouce
> **Ordres**
>
> $v=O(\alpha^2)$, donc $\ell_s=u+O(\alpha^4)$ ; $u\cos\alpha_1+v\sin\alpha_1=u+O(\alpha^2)\cdot O(\alpha)$ quel est le terme d'ordre le plus bas qui change ?




> [!success]- ✅ Correction
> **Système linéarisé**
>
> $$\ddot\alpha_1+(\omega_0^2+\omega_c^2)\alpha_1-\omega_c^2\alpha_2=0,\qquad\ddot\alpha_2+(\omega_0^2+\omega_c^2)\alpha_2-\omega_c^2\alpha_1=0,$$
> $\omega_0^2=g/\ell$, $\omega_c^2=\dfrac km\dfrac{h^2}{\ell^2}$.




> [!example]- 📝 Solution détaillée
> **Bookkeeping des ordres**
>
> $u-d=h(\sin\alpha_2-\sin\alpha_1)$ est d'ordre $1$ ; $v=O(\alpha^2)$ donc $\ell_s=u+\dfrac{v^2}{2u}+\dots=u+O(\alpha^4)$ et $\ell_s-d=h(\sin\alpha_2-\sin\alpha_1)+O(\alpha^4)$. De plus $u/\ell_s=1+O(\alpha^4)$ et $v\sin\alpha_1/\ell_s=O(\alpha^3)$. Donc le facteur de la force vaut
> $$k\frac{\ell_s-d}{\ell_s}(u\cos\alpha_1+v\sin\alpha_1)=k\,h(\sin\alpha_2-\sin\alpha_1)\cos\alpha_1+O(\alpha^4)=k\,h(\alpha_2-\alpha_1)+O(\alpha^3).$$
> L'inclinaison du ressort (terme $v$) n'intervient qu'à l'ordre $3$ : à l'ordre $1$ on peut le considérer horizontal. (Vérifié numériquement : l'écart entre la force exacte et $h(\sin\alpha_2-\sin\alpha_1)\cos\alpha_1$ est divisé par $16$ quand les angles sont divisés par $2$, signe d'un terme d'ordre $4$.)
>
> **Résultat**
>
> $$m\ell^2\ddot\alpha_1=-mg\ell\,\alpha_1+kh^2(\alpha_2-\alpha_1),\qquad m\ell^2\ddot\alpha_2=-mg\ell\,\alpha_2-kh^2(\alpha_2-\alpha_1).$$
> En divisant par $m\ell^2$ : $\omega_0^2=\dfrac g\ell$ et $\omega_c^2=\dfrac{kh^2}{m\ell^2}$, soit les équations de la correction. Application numérique : $\omega_0^2=9{,}81\ \mathrm{s^{-2}}$ ; $\omega_c^2=\dfrac{0{,}40}{0{,}20}\times\dfrac14=0{,}50\ \mathrm{s^{-2}}$ ; $\omega_c^2/\omega_0^2=5\,\%$ : couplage faible.
>
> **Comparaison avec l'exercice 1**
>
> Dans l'exercice 1, $h=\ell$ et $\omega_c^2=k/m$. Ici le même ressort est accroché à mi-hauteur : $\omega_c^2$ est divisé par $4$ (l'allongement du ressort est divisé par $2$ et le bras de levier aussi).



**q3.** **Question 3.** *Découplage.* Déterminer les modes propres (a) à la manière du physicien (somme et différence), (b) à la manière du mathématicien (matrice $K$, déterminant, vecteurs propres). Donner $\omega_1$ et $\omega_2$.


> [!tip]- 💡 Coup de pouce
> **Physicien**
>
> Ajoutez puis soustrayez les deux équations : quelles équations obtenez-vous pour $S=\alpha_1+\alpha_2$ et $D=\alpha_1-\alpha_2$ ?
>
> **Mathématicien**
>
> Écrivez $\ddot{\vec\alpha}+\mathcal K\vec\alpha=\vec0$ avec $\mathcal K=\begin{pmatrix}\omega_0^2+\omega_c^2&-\omega_c^2\\-\omega_c^2&\omega_0^2+\omega_c^2\end{pmatrix}$ et cherchez ses valeurs propres.




> [!success]- ✅ Correction
> **Modes**
>
> $\ddot S+\omega_0^2S=0$ et $\ddot D+(\omega_0^2+2\omega_c^2)D=0$ ; $\omega_1=\omega_0=3{,}132$ rad/s (en phase, $\vec u_1=(1,1)$) ; $\omega_2=\sqrt{\omega_0^2+2\omega_c^2}=3{,}288$ rad/s (opposition, $\vec u_2=(1,-1)$).




> [!example]- 📝 Solution détaillée
> **Méthode du physicien**
>
> Somme : $\ddot S+(\omega_0^2+\omega_c^2)S-\omega_c^2S=\ddot S+\omega_0^2S=0$. Différence : $\ddot D+(\omega_0^2+\omega_c^2)D+\omega_c^2D=\ddot D+(\omega_0^2+2\omega_c^2)D=0$. Le découplage marche parce que les deux pendules sont identiques (diagonale égale) et que le couplage est réciproque : l'échange $1\leftrightarrow2$ est une symétrie.
>
> **Méthode du mathématicien**
>
> $\det(\mathcal K-\omega^2I)=(\omega_0^2+\omega_c^2-\omega^2)^2-\omega_c^4=0\Rightarrow\omega^2=\omega_0^2+\omega_c^2\pm\omega_c^2$. Vecteurs propres : $\omega^2=\omega_0^2$ donne $\omega_c^2(A_1-A_2)=0$, $\vec u_1=(1,1)$ ; $\omega^2=\omega_0^2+2\omega_c^2$ donne $A_1+A_2=0$, $\vec u_2=(1,-1)$. Ils sont orthogonaux (matrice symétrique, $M=m\ell^2I$) et la matrice de passage $P=\tfrac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ diagonalise $\mathcal K$ : les coordonnées normales sont $S/\sqrt2$ et $D/\sqrt2$.
>
> **Comparaison**
>
> Les deux méthodes sont identiques ici : $S$ et $D$ sont les coordonnées dans la base des vecteurs propres. Seule la seconde se généralise à des pendules non identiques (exercice 2).
>
> **Solution générale**
>
> $\alpha_1=\tfrac12\big[S_0\cos(\omega_1t+\varphi_1)+D_0\cos(\omega_2t+\varphi_2)\big]$, $\alpha_2=\tfrac12\big[S_0\cos(\omega_1t+\varphi_1)-D_0\cos(\omega_2t+\varphi_2)\big]$.



**q4.** **Question 4.** *Battements.* À $t=0$, on écarte la tige 1 de l'angle $A=0{,}10$ rad, la tige 2 restant verticale, et on lâche sans vitesse. Calculer $\alpha_1(t)$ et $\alpha_2(t)$ sous forme d'un produit, la période de battement $T_b$ et le temps nécessaire pour que le pendule 2 atteigne l'amplitude maximale.


> [!tip]- 💡 Coup de pouce
> **Conditions initiales**
>
> Calculez $S_0=\alpha_1(0)+\alpha_2(0)$ et $D_0=\alpha_1(0)-\alpha_2(0)$ avec les vitesses nulles.
>
> **Produit**
>
> $\cos a+\cos b=2\cos\frac{a+b}2\cos\frac{a-b}2$ et $\cos a-\cos b=-2\sin\frac{a+b}2\sin\frac{a-b}2$.




> [!success]- ✅ Correction
> **Battements**
>
> $\alpha_1=A\cos\Omega_mt\cos\Omega_0t$, $\alpha_2=A\sin\Omega_mt\sin\Omega_0t$, $\Omega_0=\dfrac{\omega_1+\omega_2}2=3{,}210$ rad/s, $\Omega_m=\dfrac{\omega_2-\omega_1}2=0{,}0779$ rad/s ; $T_b=\dfrac{2\pi}{\omega_2-\omega_1}=40$ s ; le transfert complet prend $T_b/2=20$ s.




> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $S_0=D_0=A$, vitesses nulles donc $\varphi_1=\varphi_2=0$ : $\alpha_1=\tfrac A2(\cos\omega_1t+\cos\omega_2t)=A\cos\Omega_mt\cos\Omega_0t$ et $\alpha_2=\tfrac A2(\cos\omega_1t-\cos\omega_2t)=A\sin\Omega_mt\sin\Omega_0t$ avec $\Omega_0=\tfrac{\omega_1+\omega_2}2$, $\Omega_m=\tfrac{\omega_2-\omega_1}2$.
>
> **Application numérique**
>
> $\omega_1=3{,}132$, $\omega_2=3{,}288$ rad/s ; $\omega_2-\omega_1=0{,}1558$ ; $T_b=\dfrac{2\pi}{0{,}1558}=40{,}3$ s. Approximation : $\omega_2-\omega_1\simeq\dfrac{\omega_c^2}{\omega_0}=0{,}160$, soit $T_b\simeq39{,}4$ s (écart $2\,\%$ car $\omega_c^2/\omega_0^2=5\,\%$).
>
> **Transfert d'énergie**
>
> L'amplitude de $\alpha_2$ est maximale quand $\sin\Omega_mt=1$, soit $t=\dfrac{\pi}{2\Omega_m}=\dfrac{T_b}2=20$ s : à cet instant le pendule 1 est quasiment immobile. La pseudo-période des oscillations rapides est $T_0=2\pi/\Omega_0=1{,}96$ s ; il y en a $\simeq20$ par demi-battement.
>
> **Validité**
>
> Les enveloppes lentes $\cos\Omega_mt$, $\sin\Omega_mt$ ont un sens parce que $\Omega_m/\Omega_0=2{,}4\%\ll1$ : séparation d'échelles de temps. Les petits angles sont valables si $A=0{,}1$ rad : la correction relative à la fréquence est $\sim A^2/16=6\times10^{-4}$.



**q5.** **Question 5.** *Énergie.* Écrire l'énergie mécanique totale à l'ordre quadratique. Quelle fraction $\kappa$ de l'énergie initiale est au maximum stockée dans le ressort ? Pourquoi est-ce petit ?


> [!tip]- 💡 Coup de pouce
> **Énergie potentielle**
>
> $E_p=\tfrac12mg\ell(\alpha_1^2+\alpha_2^2)+\tfrac12kh^2(\alpha_1-\alpha_2)^2$ (à l'ordre $2$). Quelle est la valeur maximale de $\alpha_1-\alpha_2=D$ ?




> [!success]- ✅ Correction
> **Fraction**
>
> $E=\tfrac12m\ell^2A^2(\omega_0^2+\omega_c^2)$ ; $E_{\rm ressort,max}=\tfrac12kh^2A^2$ ; $\kappa=\dfrac{\omega_c^2}{\omega_0^2+\omega_c^2}=\dfrac{0{,}5}{10{,}31}=4{,}9\,\%$.




> [!example]- 📝 Solution détaillée
> **Énergie à l'ordre quadratique**
>
> $E=\tfrac12m\ell^2(\dot\alpha_1^2+\dot\alpha_2^2)+\tfrac12mg\ell(\alpha_1^2+\alpha_2^2)+\tfrac12kh^2(\alpha_1-\alpha_2)^2$ : on a utilisé $mg\ell(1-\cos\alpha)\simeq\tfrac12mg\ell\alpha^2$ et l'énergie élastique $\tfrac12k(\ell_s-d)^2\simeq\tfrac12kh^2(\alpha_1-\alpha_2)^2$ (pour l'énergie on garde l'ordre $2$ : $1-\cos\alpha\simeq\alpha^2/2$, alors que pour les forces l'ordre $1$ suffit, $\cos\alpha\simeq1$).
>
> **Valeur à $t=0$ et valeur maximale**
>
> À $t=0$ : $\alpha_1=A$, $\alpha_2=0$, vitesses nulles : $E=\tfrac12mg\ell A^2+\tfrac12kh^2A^2=\tfrac12m\ell^2A^2(\omega_0^2+\omega_c^2)$. L'énergie du ressort vaut $\tfrac12kh^2D^2$ avec $D=A\cos\omega_2t$ : maximale $\tfrac12kh^2A^2$, donc $\kappa=\dfrac{kh^2}{m\ell^2(\omega_0^2+\omega_c^2)}=\dfrac{\omega_c^2}{\omega_0^2+\omega_c^2}=4{,}9\,\%$ (confirmé par intégration numérique).
>
> **Interprétation**
>
> Le couplage est faible parce que l'énergie du ressort est petite devant l'énergie de gravité à ces angles : le ressort ne sert qu'à *transférer* lentement l'énergie. À $t=T_b/2$, quasiment toute l'énergie est dans le pendule 2 : le transfert est complet bien que le ressort n'en stocke que $5\,\%$ à chaque instant. Ce n'est pas contradictoire : le ressort sert de canal, pas de réservoir.




> [!note]- 🔗 Liens avec d'autres disciplines
> **Mécanique des structures**
>
> Un raidisseur placé près de l'encastrement d'une poutre couple moins qu'un raidisseur placé en bout : même idée de bras de levier.




> [!question]- 🔭 Aller plus loin — Licence : Ressort pas horizontal
> Montrer que si les points de fixation sont à des hauteurs différentes, il apparaît des termes en $\alpha_i$ au premier ordre dans la force de rappel (l'équilibre est modifié).




> [!question]- 🔭 Aller plus loin — Master : Corrections d'ordre $4$
> Vérifier numériquement que la force du ressort est $h(\sin\alpha_2-\sin\alpha_1)\cos\alpha_1+O(\varepsilon^4)$, ce qui justifie le modèle linéaire jusqu'à $\varepsilon\sim0{,}3$.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex2-couplage-de-deux-oscillateurs-harmoniques-dissymetriques|Exercice 2 — Couplage de deux oscillateurs harmoniques dissymétriques]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex3-oscillations-libres-et-forcees-d-un-couplage-pendule-chariot|Exercice 3 — Oscillations libres et forcées d'un couplage pendule-chariot]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex4-frequence-propre-d-une-molecule-diatomique|Exercice 4 — Fréquence propre d'une molécule diatomique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex6-complement-niveau-2-ambitieux-trois-masses-quatre-ressorts-diagonalisation-et-perturbation|Exercice 6 — Complément (niveau 2, ambitieux) : trois masses, quatre ressorts, diagonalisation et perturbation]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex7-complement-niveau-2-ambitieux-oscillateurs-desaccordes-anticroisement-et-transfert-d-energie|Exercice 7 — Complément (niveau 2, ambitieux) : oscillateurs désaccordés, anticroisement et transfert d'énergie]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex8-complement-niveau-3-ens-modes-non-lineaires-de-deux-pendules-couples-stabilite-et-instabilite-parametrique|Exercice 8 — Complément (niveau 3, ENS) : modes non linéaires de deux pendules couplés, stabilité et instabilité paramétrique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex9-complement-niveau-3-ens-anneau-de-n-oscillateurs-modes-de-fourier-et-propagation-du-signal|Exercice 9 — Complément (niveau 3, ENS) : anneau de N oscillateurs, modes de Fourier et propagation du signal]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex1-pendules-couples-et-battements|Exercice 1 — Pendules couplés et battements]]


