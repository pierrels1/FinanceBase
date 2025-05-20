# FinanceBase

[Version française →](README.md)

---

📈 FinanceBase

FinanceBase is a Python project designed to explore the fundamentals of option pricing and portfolio management in derivatives. It covers three essential tools used daily on trading desks: the Black-Scholes model, delta hedging, and implied volatility calculation.

# 🧠 Delta Hedging Simulator & Option Analysis

This educational Python project models a **Delta Hedging strategy**, calculates **option prices** via the **Black-Scholes model**, extracts **implied volatility** from market prices, and analyzes the **Greeks** (Delta, Gamma, Vega).

---

## 🎯 Objectives

- Understand **dynamic hedging (delta hedging)** of an option portfolio.
- Visualize the imperfection of linear hedging caused by **Gamma**.
- Extract **implied volatility** from an observed option price.
- Calculate **Greeks** to quantify portfolio sensitivities.
- Study the **PnL formation over time** (not only at maturity).

---

## 📂 Project Structure

### `black_scholes.py`

Functions:

- `black_scholes_price(S, K, T, r, sigma, option_type)`  
  ➤ Computes the price of a call/put option using the Black-Scholes model.

- `compute_greeks(S, K, T, r, sigma, option_type)`  
  ➤ Returns **Delta**, **Gamma**, and **Vega**.

📌 Usage: the analytical basis for the entire simulator.

---

### `delta_hedging.py`

Simulates a Delta hedging strategy:

- Daily rebalancing according to the computed **Delta**.
- Tracking daily **PnL** (cash + position).
- Impact of **Gamma** on hedging errors.
- Display of final **PnL** and its evolution over time.

---

### `delta_hedging_interactive.ipynb`

Interactive notebook:

- Sliders to adjust all parameters (spot, vol, maturity, etc.).
- Real-time display of:
  - **Final PnL distribution**
  - **PnL statistics** (mean, standard deviation)
- Built with `ipywidgets` and `plotly`.

---

### `implied_volatility.py`

Calculates **implied volatility**:

- From an **observed option market price**.
- Via numerical inversion of Black-Scholes using `scipy.optimize.brentq`.

📈 Example:
```python
price = 5.0  # market option price
iv = implied_volatility(price, S=100, K=100, T=0.5, r=0.01, option_type="call")
print(f"Implied Volatility: {iv:.2%}")
```


## 🚀 Features
### 1.	Black-Scholes Pricing + Greeks

	•	Compute the price of a European call or put.
	•	Display Greeks: Delta, Gamma, Vega.
	•	Generate an interactive payoff graph.

📌 Why is this useful?
It is the foundation of option pricing on all Equity Derivatives desks. Understanding this model is essential for any quantitative finance analyst or trader.

⸻

### 2.	Delta Hedging Simulator

	•	Create a portfolio with an option position.
	•	Simulate daily rebalancing to dynamically hedge risk via Delta.
	•	Visualize the performance of the hedged portfolio.

📌 Why is this useful?
It helps understand how traders dynamically manage exposure to market moves — a key risk management skill.

⸻

### 3.	Implied Volatility Calculation

	•	Compute implied volatility from observed option prices by inverting Black-Scholes.
	•	Supports different numerical solvers (e.g., Newton-Raphson).

📌 Why is this useful?
Traders use implied volatility to detect market anomalies and construct trading strategies.

⸻
## 💾 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your_username/FinanceBase.git
cd FinanceBase
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate # macOS/Linux
.venv\Scripts\activate # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
---

## ▶️ Launch the interactive simulator
```bash
jupyter notebook delta_hedging_interactive.ipynb
```

---

## 📌 Additional Resources
- 📘 *Options, Futures, and Other Derivatives* — John C. Hull
- 🧮 *The Concepts and Practice of Mathematical Finance* — Mark Joshi
- 📊 *Volatility Trading* — Euan Sinclair

---

## 👨‍💻 Author

**Pierre Louis**
Master's in Finance & Quantitative Engineering – ECE
[LinkedIn](https://www.linkedin.com/in/pierre-louis75) • [Email](mailto:pierre.louis@edu.ece.fr)

---