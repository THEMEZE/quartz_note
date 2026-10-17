---
title: "Exercice 2 — Grandeurs Dérivées : Équation au dimensions , dimension et unités dérivées (composées)"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/index|⬅ Retour]] · <a href="/pdfs/td1_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 2. Grandeurs Dérivées : Équation au dimensions , dimension et unités dérivées (composées)

**q1_intro.** **Notions de cours S.I.**\\



(a) Définir la notion de grandeur dérivée (ou composée) et citer quelques exemples.

(b) Qu’appelle t’on équation aux dimensions d’une grandeur dérivée ?

(c) La vitesse est elle une grandeur dérivée ?

(d) A partir d’une relation définissant la vitesse, établir son équation aux dimensions. Conclure sur la dimension de la vitesse.\\

(e) Connaissant l’unité de la vitesse, peut on retrouver sa dimension ?

> [!success]- ✅ Correction
> (a) Une **grandeur dérivée** s'exprime à partir des grandeurs fondamentales.
>       Exemple : le volume $[V] = L^3$ ; la vitesse : $[v] = L * T^{-1}$
>
> (b) L'équation aux dimensions s'écrit $[X] ~ = ~ L^a ~ M^b ~ T^c ~ I^d ~ \Theta^e ~ N^f ~ J^g$
>
> (c) Oui, la vitesse dépend de la longueur et du temps.
>
> (d) ${\displaystyle v = \frac{dx}{dt}}$ donc $[v] = [x]/[t] = L * T^{-1}$.
>
> (e) Oui, $m/s$ correspond bien à $L * T^{-1}$.


> [!example]- 📝 Solution détaillée
> Une **grandeur dérivée** (ou composée) est une grandeur physique définie à partir des grandeurs de base du Système international (SI) — comme la longueur, la masse ou le temps — en utilisant des relations mathématiques (multiplications ou divisions).
> Par opposition aux sept grandeurs de base qui sont indépendantes, les grandeurs dérivées s'expriment à l'aide d'une équation aux dimensions qui combine ces grandeurs fondamentales.
>
> $$\begin{array}{l l l l} \textbf{Grandeur} & \textbf{Formule / Définition} & \textbf{Dimension} & \textbf{Unités S.I. et autres} \\ \hline \textbf{Vitesse} & v = \frac{d}{t} & \mathsf{L}\ast\mathsf{T}^{-1} & \text{m}\cdot\text{s}^{-1} \\ \textbf{Surface (Aire)} & S = L \times l & \mathsf{L}^2 & \text{m}^2 \\ \textbf{Volume} & V = L \times l \times h & \mathsf{L}^3 & \text{m}^3 \\ \textbf{Masse volumique} & \rho = \frac{m}{V} & \mathsf{M}\ast\mathsf{L}^{-3} & \text{kg}\cdot\text{m}^{-3} \\ \hline \textbf{Force} & F = m \times a & \mathsf{M}\ast\mathsf{L}\ast\mathsf{T}^{-2} & \text{N} \quad (\text{kg}\cdot\text{m}\cdot\text{s}^{-2}) \\ \textbf{Pression} & P = \frac{F}{S} & \mathsf{M}\ast\mathsf{L}^{-1}\ast\mathsf{T}^{-2} & \text{Pa} \quad (\text{kg}\cdot\text{m}^{-1}\cdot\text{s}^{-2}) \\ \textbf{Énergie / Travail} & E = F \times d & \mathsf{M}\ast\mathsf{L}^2\ast\mathsf{T}^{-2} & \text{J} \quad (\text{kg}\cdot\text{m}^2\cdot\text{s}^{-2}) \\ \textbf{Puissance} & P = \frac{E}{t} & \mathsf{M}\ast\mathsf{L}^2\ast\mathsf{T}^{-3} & \text{W} \quad (\text{kg}\cdot\text{m}^2\cdot\text{s}^{-3}) \end{array}$$


**q2.** **Équation aux dimensions d’une grandeur à partir de sa relation de définition.**\\

On considère les grandeurs dérivées dans le tableau ci-dessous. Établir leur équation aux dimensions et l’exprimer en unités S.I.

%\begingroup
    % Sauvegarde de la taille actuelle
    %\makeatletter
    %\let\oldfontsize\@currsize
    %\makeatother
    $$
    {%
    %\fontsize{5pt}{10pt}\selectfont
    \begin{array}{l l l l}
    \textbf{Grandeur} & \textbf{Formule / Définition} & \textbf{Dimension} & \textbf{Unités S.I. et autres} \\
    \hline
    \textbf{Longueur} & L & \mathsf{L} & \text{m} \\
    \textbf{Surface} & S = H \times L & \mathsf{L}^2 & \text{m}^2 \\
    \textbf{Volume} &  & &  \\
    \hline
    \textbf{Temps} &  &  &  \\
    \textbf{Fréquence} &  &  \\
    \textbf{Vitesse} &  &  &  \\
    \textbf{Accélération} &  &  & \\
    \hline
    \textbf{Masse} &  & &  \\
    \textbf{Force} &  \\
    \textbf{Énergie / Travail} &  \\
    \textbf{Pression} & 
    \end{array}
    }
    $$
    % Retour à la taille précédente
    %\oldfontsize
    %\endgroup
    
    \begin{center}
      \text{**Table 3 :** Savoir retrouver rapidement la dimension et l’unité SI d’une grandeur dérivée}
    \end{center}

> [!tip]- 💡 Coup de pouce
> Méthode pour établir l’équation aux dimensions d’une grandeur :
>
>
> - exprimer la grandeur à l’aide d’une formule simple ou une relation de définition
> - exprimer les dimensions des grandeurs intervenant dans la formule précédente
> - conclure sur la dimension de la grandeur recherchée


> [!example]- 📝 Solution détaillée
> %\begingroup
> % Sauvegarde de la taille actuelle
> %\makeatletter
> %\let\oldfontsize\@currsize
> %\makeatother
> $$
> {%
> %\fontsize{5pt}{10pt}\selectfont
> \begin{array}{l l l l}
> \textbf{Grandeur} & \textbf{Formule / Définition} & \textbf{Dimension} & \textbf{Unités S.I. et autres} \\
> \hline
> \textbf{Longueur} & L & \mathsf{L} & \text{m} \\
> \textbf{Surface} & S = H \times L & \mathsf{L}^2 & \text{m}^2 \\
> \textbf{Volume} & V = S \times H & \mathsf{L}^3 & \text{m}^3 \\
> \hline
> \textbf{Temps} & t & \mathsf{T} & \text{s} \\
> \textbf{Fréquence} & f = \frac{1}{T} & \mathsf{T}^{-1} & \text{Hz} \quad (\text{s}^{-1}) \\
> \textbf{Vitesse} & { v = \frac{\text{d}x}{\text{d}t}} & \mathsf{L}\ast\mathsf{T}^{-1} & \text{m}\cdot\text{s}^{-1} \\
> \textbf{Accélération} & a = \frac{\text{d}v}{\text{d}t} & \mathsf{L}\ast\mathsf{T}^{-2} & \text{m}\cdot\text{s}^{-2} \\
> \hline
> \textbf{Masse} & m & \mathsf{M} & \text{kg} \\
> \textbf{Force} & F = m \times a & \mathsf{M}\ast\mathsf{L}\ast\mathsf{T}^{-2} & \text{N} \quad (\text{kg}\cdot\text{m}\cdot\text{s}^{-2}) \\
> \textbf{Énergie / Travail} & E = F \times d & \mathsf{M}\ast\mathsf{L}^2\ast\mathsf{T}^{-2} & \text{J} \quad (\text{kg}\cdot\text{m}^2\cdot\text{s}^{-2}) \\
> \textbf{Pression} & P = \frac{F}{S} & \mathsf{M}\ast\mathsf{L}^{-1}\ast\mathsf{T}^{-2} & \text{Pa} \quad (\text{kg}\cdot\text{m}^{-1}\cdot\text{s}^{-2})
> \end{array}
> }
> $$
> % Retour à la taille précédente
> %\oldfontsize
> %\endgroup
>
> \begin{center}
>   \text{**Table 3 :** Savoir retrouver rapidement la dimension et l’unité SI d’une grandeur dérivée}
> \end{center}


**q3.** **Équation aux dimensions d’une grandeur à partir de son unité.**\\

Trouver l’équation aux dimensions d’une grandeur peut se faire simplement en analysant son unité si on la connaît.
À partir des unités S.I. fournies ($m\cdot s^{-1}$, $m^3$, $kg\cdot m^{-3}$, $kg\cdot mol^{-1}$, $m^3\cdot kg^{-1}$), identifier la grandeur physique correspondante et son équation aux dimensions.

  {
    %\fontsize{20pt}{10pt}\selectfont
    $$
    \begin{array}{lll}
    \textbf{Grandeur} & \textbf{Dimension} & \textbf{Unité} \\
    \hline
    \textbf{Vitesse} & \mathsf{L}\ast\mathsf{T}^{-1} & \text{m} \cdot \text{s}^{-1}  \\
    \textbf{Volume} &  \\
    \textbf{Masse volumique} &   \\
    \textbf{Masse molaire} & \\
    \textbf{Volume massique} & 
    \end{array}
    $$
    }

> [!example]- 📝 Solution détaillée
> {
> %\fontsize{20pt}{10pt}\selectfont
> $$
> \begin{array}{lll}
> \textbf{Grandeur} & \textbf{Dimension} & \textbf{Unité} \\
> \hline
> \textbf{Vitesse} & \mathsf{L}\ast\mathsf{T}^{-1} & \text{m} \cdot \text{s}^{-1}  \\
> \textbf{Volume} & \mathsf{L}^3 & \text{m}^3 \\
> \textbf{Masse volumique} & \mathsf{M} \ast \mathsf{L}^{-3} & \text{kg} \cdot \text{m}^{-3}  \\
> \textbf{Masse molaire} & \mathsf{M} \ast \mathsf{N}^{-1} & \text{kg} \cdot \text{mol}^{-1}\\
> \textbf{Volume massique} & \mathsf{L}^3 \ast \mathsf{M}^{-1} & \text{m}^3 \cdot \text{kg}^{-1}
> \end{array}
> $$
> }
> \begin{center}
>   \text{**Table 4 :** Savoir retrouver rapidement la dimension d’une grandeur connaissant son unité !!}
> \end{center}


**q4.** **Unités dérivées et conversion.**\\

Convertir les grandeurs suivantes dans l'unité demandée : (a) $8*10^{-6} ~ m^2$ en $\mu m^2$ ; (b) $0,0087 ~ m^3$ en $cm^3$ ; (c) $540 ~ mm^3$ en $m^3$ ; (d) $1 ~ L$ en $m^3$ ; (e) $380 ~ km/h$ en $m/s$ ; (f) $340 ~ m/s$ en $km/h$ ; (g) $3*10^8 ~ m/s$ en $km/h$ ; (h) $940*10^6 ~ km/an$ en $km/h$

{
    %\fontsize{10pt}{10pt}\selectfont

    \tikzset{
        pointillesPerso/.style={
        % dotted,
        % line width=2pt,
        % line cap=round,
        % dash pattern=on 1pt off 1pt on 1pt off 1pt
        line width=1.5pt,
        line cap=round,
        dash pattern=on 0pt off 3.5pt
      }
    }
    \[
    \begin{array}{rrclcrrcl}
    \textbf{(a)} & 8 \times 10^{-6}\,\mathrm{m}^2
    & = &  \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (2,0); \,\,\mu\mathrm{m}^2
    && \textbf{(e)} & 380\,\mathrm{km}\cdot\mathrm{h}^{-1}
    & = & \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (2,0); \,\,\mathrm{m}\cdot\mathrm{s}^{-1}
    \\[2mm]

    \textbf{(b)} & 0{,}0087\,\mathrm{m}^3
    & = & \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (2,0);\,\, \mathrm{cm}^3
    && \textbf{(f)} & 340\,\mathrm{m}\cdot\mathrm{s}^{-1}
    & = & \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (2,0);\,\, \mathrm{km}\cdot\mathrm{h}^{-1}
    \\[2mm]

    \textbf{(c)} & 540\,\mathrm{mm}^3
    & = & \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (2,0);\,\, \mathrm{m}^3
    && \textbf{(g)} & 3 \times 10^{8}\,\mathrm{m}\cdot\mathrm{s}^{-1}
    & = & \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (2,0);\,\, \mathrm{km}\cdot\mathrm{h}^{-1}
    \\[2mm]

    \textbf{(d)} & 1\,\mathrm{L}
    & = & \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (2,0);\,\, \mathrm{m}^3
    && \textbf{(h)} & 940 \times 10^{6}\,\mathrm{km}\cdot\mathrm{an}^{-1}
    & = & \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (2,0);\,\, \mathrm{km}\cdot\mathrm{h}^{-1}
    \end{array}
    \]

  

}

> [!tip]- 💡 Coup de pouce
> Exemple, pour convertir : $3\,\mathrm{cm}^2$ en  $m^2$  sachant que $1\,\mathrm{cm}=10^{-2}\,\mathrm{m}$ :
>
> \[
> 3\,\mathrm{cm}^2 \underset{3 \times \,10^{-4} ~ m^2 }{\xrightarrow{ \mathrm{cm}^2 ~ = ~  ( 10^{-2} ~ m  )^2 ~ = ~ 10^{-4} ~ m^2 }}
> 3\, 10^{-4}\,\mathrm{m}^2
> \]
>
> Une brique de lait de $1\, \mathrm{L}$ fait à peu près $1\, \mathrm{dm} \times 1,\mathrm{dm} \times 1\, \mathrm{dm} = 1,\mathrm{dm}^3$.
>
> Or,
>
> $$
> 1\,\mathrm{m}^3
> = (10\,\mathrm{dm}) \times (10\,\mathrm{dm}) \times (10\,\mathrm{dm})
> = (10\,\mathrm{dm})^3
> = 10^3\,\mathrm{dm}^3.
> $$
>
> Donc, dans un mètre cube, il y a $1000\, \mathrm{L}$.
>
> Dans une pipette, on voit que les graduations sont généralement de l'ordre de $1\,\mathrm{cm}^3$, ce qui correspond à $1\,\mathrm{mL}$.
>
> <p style="text-align:center"><a href="/figures/brique_lait.svg" target="_blank" rel="noopener"><img src="/figures/brique_lait.svg" alt="" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>
>
> **Conversion des vitesses ($\mathrm{km/h}$ en $\mathrm{m/s}$)
> **
>
> Pour comprendre la conversion entre $\mathrm{km/h}$ et $\mathrm{m/s}$ :
>
> Il y a $60\,\mathrm{min}$ dans $1\,\mathrm{h}$ et $60\,\mathrm{s}$ dans $1\,\mathrm{min}$, donc $3600\,\mathrm{s}$ dans $1\,\mathrm{h}$.
>
> $$
> 1\,\mathrm{km/h} = \frac{1}{60}\,\mathrm{km/min} = \frac{1}{60 \times 60}\,\mathrm{km/s} = \frac{1}{3600}\,\mathrm{km/s}
> $$
>
> De plus, sachant qu'il y a $1000\,\mathrm{m}$ dans $1\,\mathrm{km}$ :
>
> $$
> 1\,\mathrm{km/h} = \frac{1000\,\mathrm{m}}{3600\,\mathrm{s}} = \frac{1}{3{,}6}\,\mathrm{m/s}
> $$
>
> En résumé :
>
>
> - Pour passer de **$\mathrm{km/h}$ à $\mathrm{m/s}$**, on divise par $3{,}6$.
> - Pour passer de **$\mathrm{m/s}$ à $\mathrm{km/h}$**, on multiplie par $3{,}6$.


> [!example]- 📝 Solution détaillée
> {
> %\fontsize{10pt}{10pt}\selectfont
> \[
> \begin{array}{rrclcrrcl}
> \textbf{(a)} & 8 \times 10^{-6}\,\mathrm{m}^2
> & = & 8 \times 10^{6}\,\mu\mathrm{m}^2
> && \textbf{(e)} & 380\,\mathrm{km}\cdot\mathrm{h}^{-1}
> & = & 1{,}06 \times 10^{2}\,\mathrm{m}\cdot\mathrm{s}^{-1}
> \\[2mm]
>
> \textbf{(b)} & 0{,}0087\,\mathrm{m}^3
> & = & 8{,}7 \times 10^{3}\,\mathrm{cm}^3
> && \textbf{(f)} & 340\,\mathrm{m}\cdot\mathrm{s}^{-1}
> & = & 1{,}22 \times 10^{3}\,\mathrm{km}\cdot\mathrm{h}^{-1}
> \\[2mm]
>
> \textbf{(c)} & 540\,\mathrm{mm}^3
> & = & 5{,}4 \times 10^{-7}\,\mathrm{m}^3
> && \textbf{(g)} & 3 \times 10^{8}\,\mathrm{m}\cdot\mathrm{s}^{-1}
> & = & 1{,}08 \times 10^{9}\,\mathrm{km}\cdot\mathrm{h}^{-1}
> \\[2mm]
>
> \textbf{(d)} & 1\,\mathrm{L}
> & = & 1 \times 10^{-3}\,\mathrm{m}^3
> && \textbf{(h)} & 940 \times 10^{6}\,\mathrm{km}\cdot\mathrm{an}^{-1}
> & = & 1{,}07 \times 10^{5}\,\mathrm{km}\cdot\mathrm{h}^{-1}
> \end{array}
> \]
> }
>
> \begin{center}
> **Table 4 :** Savoir retrouver rapidement la dimension d’une grandeur connaissant son unité !!
> \end{center}


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex1-grandeurs-physiques-fondamentales-dimensions-et-unites-de-base|Exercice 1 — Grandeurs physiques fondamentales : dimensions et unités de base]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex3-homogeneite-et-analyse-dimensinnelle|Exercice 3 — Homogénéité et Analyse Dimensinnelle]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex4-lois-et-constantes-fondamentales-en-physiques|Exercice 4 — Lois et Constantes Fondamentales en physiques]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex5-l-analyse-dimensionnelle-comme-outil-de-prediction|Exercice 5 — L'analyse dimensionnelle comme outil de prédiction]]

