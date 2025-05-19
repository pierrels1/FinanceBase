import numpy as np
import matplotlib.pyplot as plt
from black_scholes import black_scholes_price, compute_greeks

def simulate_delta_hedging_gbm(S0, K, T, r, sigma_imp, sigma_mkt, option_type="call", steps=30, n_sim=1000):
    """
    Simule une stratégie de delta hedging sur plusieurs chemins GBM.

    S0 : prix initial du sous-jacent
    K : strike
    T : maturité en années
    r : taux sans risque
    sigma_imp : volatilité implicite (utilisée pour pricing & delta)
    sigma_mkt : volatilité réelle du marché (simule le chemin du spot)
    option_type : 'call' ou 'put'
    steps : nombre de rebalancements (ex : 30 pour couverture quotidienne sur 1 mois)
    n_sim : nombre de simulations Monte Carlo
    """
    dt = T / steps
    pnl_list = []

    for sim in range(n_sim):
        # Simuler chemin GBM du spot sous sigma_mkt
        S_path = [S0]
        for _ in range(steps):
            z = np.random.normal()
            S_next = S_path[-1] * np.exp((r - 0.5 * sigma_mkt**2) * dt + sigma_mkt * np.sqrt(dt) * z)
            S_path.append(S_next)
        S_path = np.array(S_path)
        times = np.linspace(0, T, steps + 1)

        # Initialisation
        cash_account = 0
        delta_prev = 0

        for i, (t, S) in enumerate(zip(times[:-1], S_path[:-1])):
            T_remaining = T - t
            option_price, _, _ = black_scholes_price(S, K, T_remaining, r, sigma_imp, option_type)
            delta, _, _ = compute_greeks(S, K, T_remaining, r, sigma_imp, option_type)

            # Ajustement du hedge
            d_delta = delta - delta_prev
            cash_account -= d_delta * S
            cash_account *= np.exp(r * dt)  # placement au taux sans risque
            delta_prev = delta

        # Valeur finale du portefeuille
        portfolio_value = delta_prev * S_path[-1] + cash_account
        payoff = max(S_path[-1] - K, 0) if option_type == "call" else max(K - S_path[-1], 0)
        pnl = portfolio_value - payoff
        pnl_list.append(pnl)

    pnl_array = np.array(pnl_list)

    print(f"\n--- Simulation Monte Carlo Delta Hedging ({n_sim} chemins) ---")
    print(f"PnL moyen : {np.mean(pnl_array):.4f} €")
    print(f"PnL std : {np.std(pnl_array):.4f} €")
    print(f"Min PnL : {np.min(pnl_array):.4f} €, Max PnL : {np.max(pnl_array):.4f} €")

    # Histogramme du PnL
    plt.hist(pnl_array, bins=50, alpha=0.7)
    plt.title("Distribution du PnL de la stratégie Delta Hedging")
    plt.xlabel("PnL (€)")
    plt.ylabel("Fréquence")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Paramètres
    S0 = 100       # Spot initial
    K = 100        # Strike
    T = 30 / 365   # Maturité 30 jours
    r = 0.01       # Taux sans risque
    sigma_imp = 0.2  # Volatilité implicite (pricing)
    sigma_mkt = 0.25 # Volatilité réelle du marché (simule le spot)
    option_type = "call"  # ou 'put'

    simulate_delta_hedging_gbm(S0, K, T, r, sigma_imp, sigma_mkt, option_type, steps=30, n_sim=1000)