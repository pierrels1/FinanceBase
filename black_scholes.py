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