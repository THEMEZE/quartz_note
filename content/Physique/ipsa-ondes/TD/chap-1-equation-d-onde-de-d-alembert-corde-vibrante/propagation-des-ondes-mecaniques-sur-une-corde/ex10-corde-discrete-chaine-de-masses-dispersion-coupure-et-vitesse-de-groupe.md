---
title: "Exercice 10 — Corde discrète (chaîne de masses) : dispersion, coupure et vitesse de groupe"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a>

### Exercice 10. Corde discrète (chaîne de masses) : dispersion, coupure et vitesse de groupe *(facultatif)*

Une corde n'est pas un milieu continu : on modélise ici une corde « discrète » par $N$ masses ponctuelles identiques $m$, régulièrement espacées de la distance $a$ au repos, reliées par des fils sans masse tendus avec la tension $F$ (constante, considérée comme identique pour tous les fils). La masse $n$ a pour position au repos $x_n=na$ et se déplace transversalement de $y_n(t)$. On suppose les déplacements petits devant $a$.

**q1.** Écrire le PFD sur la masse $n$ (projection transversale, petits angles) et établir
$$m\,\ddot y_n=\frac{F}{a}\left(y_{n+1}-2y_n+y_{n-1}\right).$$

> [!tip]- 💡 Coup de pouce
> **Pente des fils**
>
> Le fil entre $n$ et $n+1$ a pour pente $\dfrac{y_{n+1}-y_n}{a}$. Sa tension a pour composante transversale $F\times\text{pente}$.


**q2.** Limite continue. On pose $\mu=m/a$ et $y_n(t)=y(na,t)$. Développer $y_{n\pm1}$ en série de Taylor en $x=na$ jusqu'à l'ordre 4 et montrer que l'équation devient
$$\frac{\partial^2y}{\partial t^2}=c_0^2\left(\frac{\partial^2y}{\partial x^2}+\frac{a^2}{12}\frac{\partial^4y}{\partial x^4}+\dots\right)$$
avec $c_0=\sqrt{F/\mu}$. Commenter : à quelle condition retrouve-t-on l'équation de d'Alembert ?

> [!tip]- 💡 Coup de pouce
> **Développement**
>
> $y(x\pm a)=y\pm a\,y'+\dfrac{a^2}{2}y''\pm\dfrac{a^3}{6}y'''+\dfrac{a^4}{24}y''''+\dots$ La somme $y(x+a)+y(x-a)$ élimine les termes impairs.


**q3.** On cherche $y_n=\text{Re}\left[A\,e^{\,j(\omega t-kna)}\right]$. Établir la relation de dispersion
$$\omega=\omega_{\max}\left|\sin\frac{ka}{2}\right|,\qquad\omega_{\max}=2\sqrt{\frac{F}{ma}}.$$
Montrer qu'on retrouve $\omega\simeq c_0k$ pour $ka\ll1$. Pourquoi peut-on se limiter à $|k|\le\pi/a$ ?

> [!tip]- 💡 Coup de pouce
> **Injection**
>
> $y_{n\pm1}=y_n\,e^{\mp jka}$ en complexes. Utiliser $2\cos\theta-2=-4\sin^2(\theta/2)$.


**q4.** Calculer la vitesse de phase $v_\varphi=\omega/k$ et la vitesse de groupe $v_g=\dfrac{\mathrm{d}\omega}{\mathrm{d}k}$ en fonction de $c_0$ et de $ka$. Que valent-elles pour $ka\to0$ et pour $k=\pi/a$ ? Interpréter. Application numérique : $F=10\ \text{N}$, $m=10\ \text{g}$, $a=10\ \text{cm}$, calculer $c_0$, $\omega_{\max}$, $f_{\max}$, puis $k$, $\lambda$, $v_\varphi$ et $v_g$ pour $\omega=0{,}9\,\omega_{\max}$.

> [!tip]- 💡 Coup de pouce
> **Dérivée**
>
> $\dfrac{\mathrm{d}}{\mathrm{d}k}\sin\dfrac{ka}{2}=\dfrac{a}{2}\cos\dfrac{ka}{2}$.


**q5.** (*) Fréquence supérieure à la coupure. On excite la chaîne à $\omega>\omega_{\max}$. On cherche $y_n=A\,(-1)^n e^{-qn}\cos\omega t$ avec $q>0$. Montrer que cela est possible et exprimer $q$ en fonction de $\omega/\omega_{\max}$. Application : $\omega=1{,}25\,\omega_{\max}$. Que devient l'onde ?

> [!tip]- 💡 Coup de pouce
> **Nombre d'onde complexe**
>
> Poser $ka=\pi+jq$ dans la relation de la question 3 et utiliser $\sin\left(\dfrac{\pi}{2}+j\dfrac{q}{2}\right)=\cosh\dfrac{q}{2}$.


**q6.** (*) Chaîne finie. La chaîne comporte $N$ masses et les deux extrémités sont fixes ($y_0=y_{N+1}=0$). Montrer que les modes propres sont $y_n\propto\sin\dfrac{np\pi}{N+1}$ avec $p=1,\dots,N$ et exprimer $\omega_p$. Pour $N=3$, $F=10\ \text{N}$, $m=10\ \text{g}$, $a=10\ \text{cm}$, comparer les pulsations aux modes de la corde continue de même longueur $L=(N+1)a$ et de même masse linéique. Conclure.

> [!tip]- 💡 Coup de pouce
> **Ondes stationnaires**
>
> Chercher $y_n=A\sin(kna+\varphi)\cos\omega t$. Les conditions aux limites fixent $\varphi$ et $k$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex4-equation-des-cordes-vibrantes-et-onde-progressive|Exercice 4 — Équation des cordes vibrantes et onde progressive]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex8-energie-et-puissance-d-une-onde-sur-une-corde-impedance-caracteristique|Exercice 8 — Énergie et puissance d'une onde sur une corde : impédance caractéristique]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]]

