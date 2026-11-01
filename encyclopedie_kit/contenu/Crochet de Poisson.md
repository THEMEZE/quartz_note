## 1. Définition

Sur $\Gamma=T^\ast Q$ :
$$
\{f,g\}=\frac{\partial f}{\partial q^\alpha}\frac{\partial g}{\partial p_\alpha}-\frac{\partial f}{\partial p_\alpha}\frac{\partial g}{\partial q^\alpha}=\omega^{-1}(df,dg),\qquad\{q^\alpha,p_\beta\}=\delta^\alpha{}_\beta .
$$

>[!tip]+ **Structure.** Le crochet est
>1. bilinéaire et **antisymétrique** : $\{f,g\}=-\{g,f\}$ ;
>2. une **dérivation** : $\{f,gh\}=\{f,g\}h+g\{f,h\}$ (Leibniz) ;
>3. de **Jacobi** : $\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=0$.
>
>Ainsi $(C^\infty(\Gamma),\{,\})$ est une [[Algèbre de Lie]] (de dimension infinie) et $f\mapsto\{\,\cdot\,,f\}$ en est une représentation par dérivations.
>
>*Démonstration de (3).* Le terme en dérivées d'ordre 2 d'un seul facteur s'annule par symétrie de Schwarz ; les termes restants se regroupent deux à deux avec signes opposés. De façon structurale : $X_{\{f,g\}}=\pm[X_f,X_g]$ au signe près selon la convention, et le crochet de Lie des champs de vecteurs satisfait Jacobi. $\square$

## 2. Dynamique

$\dfrac{df}{dt}=\{f,H\}+\partial_tf$.

>[!tip]+ **Théorème de Poisson.** Si $f$ et $g$ sont des intégrales premières, $\{f,g\}$ aussi.
>
>*Démonstration.* Pour $\partial_t=0$ : $\{\{f,g\},H\}=-\{\{g,H\},f\}-\{\{H,f\},g\}=0$ par Jacobi. $\square$

## 3. Exemple : algèbre du moment cinétique

Pour $\mathsf L^{ij}=x^ip^j-x^jp^i$ (cartésien orthonormé),
$$
\{\mathsf L^{ij},\mathsf L^{kl}\}=g^{ik}\mathsf L^{jl}-g^{il}\mathsf L^{jk}-g^{jk}\mathsf L^{il}+g^{jl}\mathsf L^{ik}\quad(\mathfrak{so}(n)),
$$
qui redonne $\{L_x,L_y\}=L_z$ en dimension 3.

## 4. Fil de Noether

$Q$ **génère** la transformation $\delta f=\sigma\{f,Q\}$ : translation ($Q=p$), rotation ($Q=\vec L$), évolution temporelle ($Q=H$). L'invariance de $H$ sous ce flot équivaut à $\{H,Q\}=0$.
