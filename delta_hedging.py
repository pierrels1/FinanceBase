import numpy as np
import matplotlib.pyplot as plt
from black_scholes import black_scholes_price, compute_greeks

def simulate_delta_hedging(S0, K, T, r, sigma, option_type="call", steps=30):
    """
    Simule une stratégie de delta hedging sur une option européenne.
    
    S0 : prix initial du sous-jacent
    K : strike
    T : maturité en années
    r : taux sans risque
    sigma : volatilité implicite
    option_type : 'call' ou 'put'
    steps : nombre de rebalancements (ex : 30 pour couverture quotidienne sur 1 mois)
    """
    dt = T / steps
    S_path = np.linspace(S0, S0 * 1.1, steps + 1)  # Chemin spot artificiel (hausse linéaire)
    times = np.linspace(0, T, steps + 1)

    # Initialisation
    portfolio_value = []
    cash_account = 0
    delta_prev = 0

    for i, (t, S) in enumerate(zip(times, S_path)):
        T_remaining = T - t
        if T_remaining <= 0:
            break

        option_price, _, _ = black_scholes_price(S, K, T_remaining, r, sigma, option_type)
        delta, _, _ = compute_greeks(S, K, T_remaining, r, sigma, option_type)

        # Ajustement du hedge (achat/vente de sous-jacent)
        d_delta = delta - delta_prev
        cash_account -= d_delta * S  # coût de l'ajustement
        cash_account *= np.exp(r * dt)  # placement au taux sans risque
        portfolio = delta * S + cash_account

        portfolio_value.append(portfolio)
        delta_prev = delta

    # Valeur finale de l'option
    payoff = max(S_path[-1] - K, 0) if option_type == "call" else max(K - S_path[-1], 0)
    pnl = portfolio_value[-1] - payoff

    print(f"\n--- Résultats du Delta Hedging ---")
    print(f"Valeur finale du portefeuille : {portfolio_value[-1]:.2f} €")
    print(f"Payoff de l’option : {payoff:.2f} €")
    print(f"PnL de couverture : {pnl:.2f} €")

    # Graphique
    plt.plot(times[:-1], portfolio_value, label="Valeur du portefeuille")
    plt.axhline(payoff, color='red', linestyle='--', label="Payoff option")
    plt.title("Simulation Delta Hedging")
    plt.xlabel("Temps (années)")
    plt.ylabel("Valeur (€)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Paramètres
    S0 = 100      # Spot initial
    K = 100       # Strike
    T = 30 / 365  # Maturité 30 jours
    r = 0.01      # Taux sans risque
    sigma = 0.2   # Volatilité implicite
    option_type = "call"  # ou 'put'

    simulate_delta_hedging(S0, K, T, r, sigma, option_type)