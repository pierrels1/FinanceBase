# black_scholes.py

import numpy as np
from scipy.stats import norm
import plotly.graph_objects as go

def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    """
    Calcule le prix d'une option européenne (call ou put) avec Black-Scholes.
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
    """
    Calcule les principaux Greeks : delta, gamma, vega.
    """
    _, d1, _ = black_scholes_price(S, K, T, r, sigma, option_type)
    delta = norm.cdf(d1) if option_type == "call" else norm.cdf(d1) - 1
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T)
    return delta, gamma, vega

def plot_payoff(S_range, K, option_type="call"):
    """
    Affiche le payoff à maturité d'une option.
    """
    if option_type == "call":
        payoffs = np.maximum(S_range - K, 0)
    else:
        payoffs = np.maximum(K - S_range, 0)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S_range, y=payoffs, mode='lines', name='Payoff'))
    fig.update_layout(title=f"{option_type.capitalize()} Payoff à Maturité",
                      xaxis_title="Prix du sous-jacent",
                      yaxis_title="Profit",
                      template="plotly_white")
    fig.show()

def plot_greeks_vs_S(S_range, K, T, r, sigma, option_type="call"):
    """
    Trace les Greeks en fonction du prix du sous-jacent.
    """
    deltas, gammas, vegas = [], [], []

    for S in S_range:
        delta, gamma, vega = compute_greeks(S, K, T, r, sigma, option_type)
        deltas.append(delta)
        gammas.append(gamma)
        vegas.append(vega)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S_range, y=deltas, mode='lines', name='Delta'))
    fig.add_trace(go.Scatter(x=S_range, y=gammas, mode='lines', name='Gamma'))
    fig.add_trace(go.Scatter(x=S_range, y=vegas, mode='lines', name='Vega'))

    fig.update_layout(title=f"Greeks vs Prix Spot ({option_type.upper()})",
                      xaxis_title="Prix du sous-jacent (S)",
                      yaxis_title="Valeur du Greek",
                      template="plotly_white")
    fig.show()

if __name__ == "__main__":
    # Paramètres de l'option
    S = 100      # Prix spot
    K = 100      # Strike
    T = 30 / 365 # 30 jours
    r = 0.01     # Taux sans risque
    sigma = 0.2  # Volatilité implicite
    option_type = "call"  # ou "put"

    # Calculs
    price, _, _ = black_scholes_price(S, K, T, r, sigma, option_type)
    delta, gamma, vega = compute_greeks(S, K, T, r, sigma, option_type)

    print(f"\n--- Résultats pour un {option_type.upper()} ---")
    print(f"Prix Black-Scholes : {price:.2f} €")
    print(f"Delta : {delta:.4f}")
    print(f"Gamma : {gamma:.4f}")
    print(f"Vega  : {vega:.4f}")

    # Affichages interactifs
    S_range = np.linspace(50, 150, 100)
    plot_payoff(S_range, K, option_type)
    plot_greeks_vs_S(S_range, K, T, r, sigma, option_type)