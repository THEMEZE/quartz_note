---
title: "TP Ondes stationnaires : modes propres d'un ressort hélicoïdal et d'une corde vibrante"
tags:
  - tp
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6
---

[[physique/IPSA/ipsa-physique-ondes/index|⬅ Physique des ondes]]

<p><span style="color:#1565C0">(Standing Waves: normal modes of a helical spring and a vibrating string)</span></p>

> [!info] ℹ️ Chap. 1 — Équation d'onde de d'Alembert : corde vibrante (voir TD1, ex. 4, 5 et 6)
> Séance 1


<a href="/pdfs/tp1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/tp1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

> [!abstract]+ 📚 Prérequis
> **Ondes stationnaires et modes propres <span style="color:#1565C0">(Standing waves and normal modes)</span>**
>
> Corde fixée aux deux bouts : $f_n=nc/(2L)$, $\lambda_n=2L/n$, $c=\lambda f$, $c=\sqrt{F/\mu}$ (TD1 ex. 4). Nœuds et ventres séparés de $\lambda/2$.
>
> <span style="color:#1565C0">String fixed at both ends: $f_n=nc/(2L)$, $\lambda_n=2L/n$, $c=\lambda f$, $c=\sqrt{F/\mu}$ (TD1 ex. 4). Nodes and antinodes are separated by $\lambda/2$.</span>
>
> **Régime forcé et résonance (Melde) <span style="color:#1565C0">(Forced regime and resonance, Melde)</span>**
>
> Un vibreur impose $y(0,t)=a\,e^{j\omega t}$ ; résonance quand $\sin(k\ell)=0$, soit $f=Nc/(2\ell)$ (TD1 ex. 5). Le vibreur est un nœud approché, pas un nœud parfait.
>
> <span style="color:#1565C0">A vibrator imposes $y(0,t)=a\,e^{j\omega t}$; resonance when $\sin(k\ell)=0$, i.e. $f=Nc/(2\ell)$ (TD1 ex. 5). The vibrator is an approximate node, not a perfect one.</span>
>
> **Régression linéaire et incertitudes <span style="color:#1565C0">(Linear regression and uncertainties)</span>**
>
> Ajustement affine dans Excel (pente, équation affichée), différentielle logarithmique : si $Q=A^aB^bC^c$, $\dfrac{\Delta Q}{Q}=|a|\dfrac{\Delta A}{A}+|b|\dfrac{\Delta B}{B}+|c|\dfrac{\Delta C}{C}$.
>
> <span style="color:#1565C0">Linear fit in Excel (slope, displayed equation), logarithmic differential: if $Q=A^aB^bC^c$, $\dfrac{\Delta Q}{Q}=|a|\dfrac{\Delta A}{A}+|b|\dfrac{\Delta B}{B}+|c|\dfrac{\Delta C}{C}$.</span>

> [!info]+ 🎯 Objectifs
> **Ce que l'étudiant doit savoir faire <span style="color:#1565C0">(What students must be able to do)</span>**
>
> Repérer un mode propre (motif stable, nœuds bien localisés, amplitude nettement accrue), mesurer $f_n$ pour $n=1,\dots,6$, tracer $f_n=f(n)$ et en tirer $c=2L\times\text{pente}$, montrer que $c$ dépend de la tension, obtenir $\mu$ par deux méthodes, comparer deux déterminations de $\lambda_n$, discuter l'écart au modèle.
>
> <span style="color:#1565C0">Identify a normal mode (stable pattern, well-localized nodes, clearly larger amplitude), measure $f_n$ for $n=1,\dots,6$, plot $f_n$ versus $n$ and get $c=2L\times\text{slope}$, show that $c$ depends on tension, obtain $\mu$ by two methods, compare two determinations of $\lambda_n$, discuss the deviation from the model.</span>

> [!note]+ 🧰 Matériel
> **Matériel par binôme <span style="color:#1565C0">(Equipment per pair)</span>**
>
> - Générateur de fonctions FG100 et vibreur (3B Scientific) ;
> - ressort hélicoïdal et tige support (ondes longitudinales) ;
> - corde, potence, poulie, dynamomètre, tige support avec broche de connexion (ondes transversales) ;
> - règle ou mètre ruban, balance (sinon utiliser $m=(3{,}0\pm0{,}1)$ g) ;
> - ordinateur avec Excel pour les graphiques.
>
>
>
> <span style="color:#1565C0">FG100 function generator and vibration generator (3B Scientific); helical spring and support rod (longitudinal waves); string, stand, pulley, dynamometer, support rod with connector pin (transverse waves); ruler or tape measure, balance (otherwise use $m=(3.0\pm0.1)$ g); computer with Excel for the graphs.</span>

> [!warning] ⚠️ Attention
> **TP de physique des ondes – Informations pratiques <span style="color:#1565C0">Wave Physics Lab – Practical Information</span>**
>
> Bonjour à toutes et à tous,
>
> <span style="color:#1565C0">Hello everyone,</span> 
>
>
>
> Voici quelques informations importantes pour le bon déroulement des TP de physique des ondes.
>
> <span style="color:#1565C0">Here is some important information to help ensure that your wave physics lab sessions run smoothly.</span>
>
> **1. Documents**<span style="color:#1565C0">Documents</span>
>
> Les polys de TP sont disponibles dans la salle. Le **carnet expérimental à compléter pendant la séance** est disponible sur Moodle. Vous devrez le déposer sur Moodle à la fin de la séance.
> <span style="color:#1565C0">The lab handouts are available in the lab. The **experimental lab notebook, which you must complete during the session**, is available on Moodle. You must upload it to Moodle at the end of the session.</span>
>
> **2. Supports expérimentaux****Experimental equipment stands**
>
> Les supports sont rangés sur la table à l’arrière de la salle. Ils sont lourds et les barres ne se fixent pas toujours facilement dessus. **Manipulez-les avec précaution** lors de vos déplacements et de leur installation.<span style="color:#1565C0">The stands are stored on the table at the back of the room. They are heavy, and the rods do not always screw into them easily. **Handle them carefully** when moving and setting them up.</span>
>
> **3. Matériel**<span style="color:#1565C0">Equipment</span>
>
> Le matériel est rangé dans les armoires du fond :
>
>
> - une boîte pour les générateurs ;
> - boîte pour les alimentations ;
> - une boîte pour les accessoires (câbles, cordes, ressorts, supports de maintien du vibreur, etc.).
>
>
>
> <span style="color:#1565C0">The equipment is stored in the cabinets at the back of the room :
>
>
> - one box for the signal generators;
> - one box for the power supplies;
> - one box for accessories (cables, strings, springs, supports designed to relieve lateral tension on the vibrator, etc.).
>
>
> </span>
>
> Veillez à utiliser le matériel avec soin et à ne pas égarer les accessoires.
>
> <span style="color:#1565C0">Handle all equipment carefully and make sure no accessories are misplaced.
> </span>
>
> **4. Utilisation du vibreur**<span style="color:#1565C0">Using the vibrator</span>
>
> Le vibreur est conçu pour effectuer un mouvement uniquement vertical. Une traction latérale risque de l’endommager rapidement.
> <span style="color:#1565C0">The vibrator is designed to move vertically only. Any lateral pull may damage it quickly.</span>
>
> **Utilisez systématiquement les supports prévus pour soulager le vibreur de la tension latérale**, et assurez-vous qu’ils sont correctement installés avant de commencer l’expérience.<span style="color:#1565C0">**Always use the supports provided to relieve lateral tension on the vibrator**, and make sure they are correctly installed before starting the experiment.</span>
>
> **5. Rangement en fin de séance****Tidying up at the end of the session**
>
> À la fin du TP, vous devrez remettre tout le matériel à sa place. Veillez notamment à **ne pas mélanger les câbles accrochés aux murs avec ceux utilisés pour l’expérience**.
> <span style="color:#1565C0">At the end of the lab session, you must return all equipment to its proper place. In particular, **do not mix up the cables hanging on the walls with those used for the experiment**.</span>
>
> Merci à toutes et à tous pour votre attention et votre soin dans la manipulation du matériel.<span style="color:#1565C0">Thank you for your attention and for taking good care of the equipment.</span>
>
> **Règles impératives <span style="color:#1565C0">(Mandatory rules)</span>**
>
> - **Amplitude du générateur $\le 5$ V** : bouton Amplitude jamais au-delà de la position « midi » ; démarrer avec une valeur basse.
> - **Ne jamais tendre la corde contre le vibreur** : la tension statique est reprise par la tige arrière à broche ; le vibreur ne transmet que la petite oscillation.
> - N'exercer aucune force latérale sur la tige mobile du vibreur.
> - Ne pas sur-étirer le ressort (déformation permanente, mesures faussées).
> - Si la tige du vibreur est visiblement déviée ou inclinée corde au repos : **montage incorrect**, ne pas allumer, desserrer la fixation au vibreur et recommencer.
>
>
>
> <span style="color:#1565C0">**Generator amplitude $\le 5$ V**: Amplitude knob never beyond the 12 o'clock position; start low. **Never tension the string against the vibrator**: the static tension is carried by the rear rod with connector pin; the vibrator only transmits the small oscillation. Apply no lateral force on the moving rod. Do not over-stretch the spring. If the rod is visibly pulled sideways or tilted with the string at rest: **incorrect setup**, do not switch on, loosen the attachment at the vibrator and start again.</span>


## Exercices

- [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales)]] <span style="color:#1565C0">(Part A — Normal modes of a helical spring, longitudinal waves)</span>
- [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde]] <span style="color:#1565C0">(Part B — Effect of tension on the normal modes of a string)</span>
- [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex3-partie-c-masse-lineique-de-la-corde-par-deux-methodes|Exercice 3 — Partie C — Masse linéique de la corde par deux méthodes]] <span style="color:#1565C0">(Part C — Linear mass density of the string by two methods)</span>
- [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres]] <span style="color:#1565C0">(Part D — Compatibility of wavelengths with the normal-mode model)</span>
- [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex5-synthese-scientifique-du-tp|Exercice 5 — Synthèse scientifique du TP]] <span style="color:#1565C0">(Scientific summary of the lab)</span>
