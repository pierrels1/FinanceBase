# black_scholes.py

import numpy as np
from scipy.stats import norm
import plotly.graph_objects as go

def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    """
    Calcule le prix d'une option européenne (call ou put) avec Black-Scholes.

    S : prix spot de l’actif sous-jacent
    K : strike de l’option
    T : maturité (en années)
    r : taux sans risque
    sigma : volatilité implicite (annualisée)
    option_type : 'call' ou 'put'
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return price, d1, d2

def compute_greeks(S, K, T, r, sigma, option_type="call"):
    _, d1, d2 = black_scholes_price(S, K, T, r, sigma, option_type)

    delta = norm.cdf(d1) if option_type == "call" else norm.cdf(d1) - 1
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T)

    return delta, gamma, vega

def plot_payoff(S_range, K, option_type="call"):
    """
    Affiche le payoff à maturité d'une option.
    """
    payoffs = []
    for S in S_range:
        if option_type == "call":
            payoffs.append(max(S - K, 0))
        else:
            payoffs.append(max(K - S, 0))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S_range, y=payoffs, mode='lines', name='Payoff'))
    fig.update_layout(title=f"{option_type.capitalize()} Payoff à Maturité",
                      xaxis_title="Prix du sous-jacent",
                      yaxis_title="Profit",
                      template="plotly_white")
    fig.show()

if __name__ == "__main__":
    # Paramètres
    S = 100      # Prix spot
    K = 100      # Strike
    T = 30 / 365 # 30 jours
    r = 0.01     # Taux sans risque
    sigma = 0.2  # Volatilité
    option_type = "call"  # ou "put"

    price, _, _ = black_scholes_price(S, K, T, r, sigma, option_type)
    delta, gamma, vega = compute_greeks(S, K, T, r, sigma, option_type)

    print(f"\n--- Résultats pour un {option_type.upper()} ---")
    print(f"Prix Black-Scholes : {price:.2f} €")
    print(f"Delta : {delta:.4f}")
    print(f"Gamma : {gamma:.4f}")
    print(f"Vega  : {vega:.4f}")

    # Graphique payoff
    S_range = np.linspace(50, 150, 100)
    plot_payoff(S_range, K, option_type)

    # Graphique des greeks
    greeks = []
    for S in S_range:
        delta, gamma, vega = compute_greeks(S, K, T, r, sigma, option_type)
        greeks.append((S, delta, gamma, vega))
    greeks = np.array(greeks)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=greeks[:, 0], y=greeks[:, 1], mode='lines', name='Delta'))
    fig.add_trace(go.Scatter(x=greeks[:, 0], y=greeks[:, 2], mode='lines', name='Gamma'))
    fig.add_trace(go.Scatter(x=greeks[:, 0], y=greeks[:, 3], mode='lines', name='Vega'))
    fig.update_layout(title="Greeks en fonction du prix du sous-jacent",
                      xaxis_title="Prix du sous-jacent",
                      yaxis_title="Valeur des Greeks",
                      template="plotly_white")
    fig.show()
    # Graphique de la volatilité implicite
    # (Non implémenté ici, mais pourrait être ajouté en fonction des besoins)
    # Graphique de la surface de volatilité implicite
    # (Non implémenté ici, mais pourrait être ajouté en fonction des besoins)
    