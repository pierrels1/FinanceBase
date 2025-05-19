
⸻

📈 FinanceBase

FinanceBase est un projet Python conçu pour explorer les fondations du pricing d’options et de la gestion de portefeuille en produits dérivés. Il couvre trois outils essentiels utilisés quotidiennement sur les desks de trading : le modèle de Black-Scholes, la couverture delta, et le calcul de volatilité implicite.

⸻

🚀 Fonctionnalités

1. Pricing Black-Scholes + Greeks
	•	Calcule le prix d’un call ou d’un put européen.
	•	Affiche les Greeks : Delta, Gamma, Vega.
	•	Génère un graphique interactif du payoff.

📌 Pourquoi c’est utile ?
C’est la base du pricing des options sur tous les desks Equity Derivatives. Comprendre ce modèle est indispensable pour tout analyste ou trader en finance quantitative.

⸻

2. Simulateur de Delta Hedging
	•	Crée un portefeuille avec une position en option.
	•	Simule des rebalancements quotidiens pour couvrir dynamiquement le risque via le delta.
	•	Visualisation de la performance du portefeuille couvert.

📌 Pourquoi c’est utile ?
Permet de comprendre comment un trader gère son exposition aux mouvements de marché de façon dynamique, une compétence clé en gestion de risque.

⸻

3. Calcul de Volatilité Implicite
	•	À partir du prix observé d’une option, calcule la volatilité implicite en inversant le modèle de Black-Scholes.
	•	Supporte les appels à différents solveurs numériques (e.g., Newton-Raphson).

📌 Pourquoi c’est utile ?
Les traders utilisent la volatilité implicite pour détecter des anomalies sur le marché et construire des stratégies de trading.