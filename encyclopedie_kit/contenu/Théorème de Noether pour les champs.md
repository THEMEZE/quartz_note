## 1. Cadre

Des champs $\phi_A(x^\mu)$, $\mu=0,\dots,n$, de **densité lagrangienne** $\mathscr L(\phi,\partial_\mu\phi,x)$ et d'action $S=\int\mathscr L\,\sqrt{|g|}\,d^{n+1}x$. Les équations d'Euler–Lagrange de champ sont
$$
\partial_\mu\Big(\frac{\partial\mathscr L}{\partial(\partial_\mu\phi_A)}\Big)=\frac{\partial\mathscr L}{\partial\phi_A}.
$$

>[!tip]+ **Théorème de Noether (champs).** Si $\phi_A\to\phi_A+\sigma\,\delta\phi_A$ laisse $\mathscr L$ invariant à une divergence près, $\delta\mathscr L=\partial_\mu K^\mu$, alors le **courant de Noether**
>$$
>J^\mu=\frac{\partial\mathscr L}{\partial(\partial_\mu\phi_A)}\,\delta\phi_A-K^\mu\qquad\text{vérifie}\qquad\partial_\mu J^\mu=0\quad(\text{sur les solutions}).
>$$
>Si les champs décroissent assez vite à l'infini, la **charge** $\mathscr Q=\int J^0\,d^nx$ est conservée.
>
>*Démonstration.* $\delta\mathscr L=\frac{\partial\mathscr L}{\partial\phi_A}\delta\phi_A+\frac{\partial\mathscr L}{\partial(\partial_\mu\phi_A)}\partial_\mu\delta\phi_A=\partial_\mu\Big(\frac{\partial\mathscr L}{\partial(\partial_\mu\phi_A)}\delta\phi_A\Big)$ en utilisant EL ; on égale à $\partial_\mu K^\mu$. Pour la charge : $\frac{d}{dt}\int J^0\,d^nx=-\oint J^i\,dS_i=0$. $\square$

## 2. Exemples

>[!example]+ Champ scalaire complexe, symétrie $U(1)$
>$\mathscr L=\partial_\mu\psi^\ast\partial^\mu\psi-m^2\psi^\ast\psi$ est invariant par $\delta\psi=i\psi$, $\delta\psi^\ast=-i\psi^\ast$. Alors
>$$
>J^\mu=i\big(\psi\,\partial^\mu\psi^\ast-\psi^\ast\partial^\mu\psi\big),\qquad\partial_\mu J^\mu=0 ,
>$$
>charge = nombre de particules moins antiparticules. Pour Schrödinger, la même symétrie donne la conservation de $\int|\psi|^2$ (probabilité) ; voir [[Dynamique quantique]].

>[!example]+ Translations : énergie-impulsion
>$x^\nu\to x^\nu+\sigma a^\nu$ donne $\delta\phi=-a^\nu\partial_\nu\phi$, $K^\mu=-a^\mu\mathscr L$, donc le [[Tenseur énergie-impulsion]]
>$$
>T^\mu{}_\nu=\frac{\partial\mathscr L}{\partial(\partial_\mu\phi_A)}\partial_\nu\phi_A-\delta^\mu_\nu\mathscr L,\qquad\partial_\mu T^\mu{}_\nu=0 .
>$$

## 3. Remarques

- $J^\mu$ n'est défini qu'à $\partial_\nu B^{[\mu\nu]}$ près (antisymétrique) : la charge est inchangée.
- Le théorème fournit des courants **conservés mais non géométriques** : la source d'un champ de jauge est justement un tel courant (voir [[Théories de jauge]]).
- Version mécanique : [[Théorème de Noether]] (le cas $\dim=0$).
