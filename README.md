# 📈 FinanceBase

**FinanceBase** est un projet Python pédagogique conçu pour explorer les fondamentaux du **pricing d’options** et de la **gestion dynamique de portefeuille en produits dérivés**.  
Il intègre trois outils-clés utilisés quotidiennement sur les desks de trading :

- 📊 Le modèle de **Black-Scholes** pour le pricing analytique
- 🔄 Le **simulateur de couverture Delta**
- 🔍 Le **calcul de volatilité implicite**

---

## 🧠 Objectifs pédagogiques

- Comprendre les principes du **Delta Hedging** appliqué à un portefeuille contenant des options.
- Visualiser l’effet du **Gamma** sur la qualité de la couverture.
- Extraire la **volatilité implicite** à partir d’un prix d’option observé sur le marché.
- Calculer les **Greeks** (Delta, Gamma, Vega) pour analyser les sensibilités.
- Suivre l’évolution du **PnL dans le temps**, pas uniquement à l’échéance.

---

## 📂 Structure du projet

### `black_scholes.py`

➡️ Fonctionnalités :

- `black_scholes_price(S, K, T, r, sigma, option_type)`  
  → Calcule le prix d’un call/put via la formule de Black-Scholes.

- `compute_greeks(S, K, T, r, sigma, option_type)`  
  → Calcule les **Greeks** : Delta, Gamma, Vega.

📌 **Utilité** : Ce module est la base analytique utilisée pour la couverture, le pricing et le calcul de volatilité.

---

### `delta_hedging.py`

➡️ Fonctionnalités :

- Simule une stratégie de **couverture Delta** dynamique.
- Met à jour la position chaque jour selon le Delta de l’option.
- Suit l'évolution du **PnL cumulé** jour après jour.
- Affiche l’effet du **Gamma** sur l’imperfection de couverture.

📌 **Pourquoi c’est utile ?**  
Cela permet de comprendre **comment un trader ajuste sa couverture quotidiennement** pour se protéger contre les variations du sous-jacent.

---

### `delta_hedging_interactive.ipynb`

➡️ Interface interactive avec `ipywidgets` et `plotly` :

- Contrôle en temps réel :
  - du spot initial, de la volatilité, de la maturité, etc.
- Affiche :
  - 📉 la **distribution du PnL final**
  - 📊 les **statistiques du PnL**
  - 📈 le **PnL en temps réel**

📌 **Pourquoi c’est utile ?**  
Idéal pour explorer l’impact de différents scénarios de marché et visualiser les performances de la stratégie.

---

### `implied_volatility.py`

➡️ Fonctionnalité :

- Calcule la **volatilité implicite** à partir du prix d’une option.
- Inversion numérique du modèle Black-Scholes via `scipy.optimize.brentq`.

💡 Exemple d’utilisation :
```python
price = 5.0
iv = implied_volatility(price, S=100, K=100, T=0.5, r=0.01, option_type="call")
print(f"Volatilité implicite : {iv:.2%}")```


📌 Pourquoi c’est utile ?
Les traders vol utilisent la volatilité implicite pour détecter des anomalies de marché et concevoir des stratégies directionnelles ou neutres.

⸻

🚀 Fonctionnalités clés

1. 📐 Pricing Black-Scholes & Greeks
	•	Calcule le prix théorique d’un call ou put européen.
	•	Affiche les Greeks (Delta, Gamma, Vega).
	•	Génère une visualisation du payoff.

2. 📉 Simulateur de Delta Hedging
	•	Crée un portefeuille avec position en option + couverture.
	•	Rebalance le portefeuille quotidiennement selon le Delta.
	•	Suit le PnL total (cash + position delta) dans le temps.
	•	Affiche l’imperfection de couverture liée au Gamma.

3. 🔍 Calcul de Volatilité Implicite
	•	Calcule la volatilité implicite à partir d’un prix de marché.
	•	Utilise des méthodes numériques robustes (e.g. Brent, Newton-Raphson).
	•	Peut être intégré dans une chaîne de pricing d’options réelles.

⸻

💾 Installation

1. Cloner le dépôt
git clone https://github.com/ton_utilisateur/FinanceBase.git
cd FinanceBase

2. Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

3. Installer les dépendances
pip install -r requirements.txt

▶️ Lancer le simulateur interactif
jupyter notebook delta_hedging_interactive.ipynb


⸻

📌 Ressources complémentaires
	•	📘 Options, Futures, and Other Derivatives — John C. Hull
	•	🧮 The Concepts and Practice of Mathematical Finance — Mark Joshi
	•	📊 Volatility Trading — Euan Sinclair

⸻

👨‍💻 Auteur

Pierre Louis
Master Finance & Ingénierie Quantitative – ECE
www.linkedin.com/in/pierre-louis75 • pierre.louis@edu.ece.fr
