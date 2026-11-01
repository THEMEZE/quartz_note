## 1. Du lagrangien au hamiltonien

Si $\mathrm{Hess}_{\dot q}L=m_{\alpha\beta}$ est inversible, la [[Transformée de Legendre]] définit
$$
\boxed{H(q,p,t)=p_\alpha\dot q^\alpha-L=\tfrac12\,m^{\alpha\beta}(q)\,p_\alpha p_\beta+V(q,t).}
$$
Cas électromagnétique : $H=\dfrac1{2m}g^{ij}(p_i-qA_i)(p_j-qA_j)+q\varphi$.

>[!tip]+ **Équations de Hamilton.** Sur les solutions d'Euler–Lagrange :
>$$
>\boxed{\dot q^\alpha=\frac{\partial H}{\partial p_\alpha},\qquad\dot p_\alpha=-\frac{\partial H}{\partial q^\alpha},\qquad\frac{\partial H}{\partial t}=-\frac{\partial L}{\partial t}.}
>$$
>*Démonstration.* $dH=\dot q^\alpha dp_\alpha+p_\alpha d\dot q^\alpha-\frac{\partial L}{\partial q^\alpha}dq^\alpha-p_\alpha d\dot q^\alpha-\frac{\partial L}{\partial t}dt$, et $\partial L/\partial q^\alpha=\dot p_\alpha$ (EL). On identifie les coefficients de $dp,dq,dt$. $\square$

## 2. Espace des phases

L'**espace des phases** est $\Gamma=T^\ast Q$ (dimension $2\ell$), muni de $\omega=dq^\alpha\wedge dp_\alpha$. Avec $z=(q,p)$ et $J=\begin{pmatrix}0&\mathbb 1\\-\mathbb 1&0\end{pmatrix}$ :
$$
\dot z=J\,\nabla_zH .
$$
Le champ $X_H$ est le **champ hamiltonien** ; son flot est symplectique (voir [[Théorème de Liouville]], [[Géométrie symplectique]]).

>[!tip]+ **Principe variationnel de phase.** Les équations de Hamilton sont les équations stationnaires de $\displaystyle S[q,p]=\int\big(p_\alpha\dot q^\alpha-H\big)dt$, avec $q$ et $p$ variés **indépendamment** ($q$ fixé aux bornes).
>
>*Preuve.* $\delta S=\int(\dot q^\alpha-\partial_{p_\alpha}H)\delta p_\alpha-(\dot p_\alpha+\partial_{q^\alpha}H)\delta q^\alpha\,dt$ après intégration par parties. $\square$

## 3. Observables et évolution

Pour une fonction $f(q,p,t)$ : $\ \dfrac{df}{dt}=\{f,H\}+\dfrac{\partial f}{\partial t}$ (voir [[Crochet de Poisson]]). $f$ est une **intégrale première** si $\{f,H\}=-\partial_tf$.

## 4. Fil de Noether

En version hamiltonienne, la réciproque devient vraie : $Q$ est conservée ssi son flot $\{\,\cdot\,,Q\}$ est une **symétrie** de $H$ (car $\{Q,H\}=0$ s'écrit aussi $\{H,Q\}=0$). **Symétries et intégrales premières sont en bijection** (à constante additive près).

## 5. Pont vers le quantique

$\{\cdot,\cdot\}\;\leadsto\;\tfrac1{i\hbar}[\cdot,\cdot]$ : voir [[Quantification]].
