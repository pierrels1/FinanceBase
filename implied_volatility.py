from scipy.optimize import brentq
from black_scholes import black_scholes_price

def implied_volatility(price_market, S, K, T, r, option_type, tol=1e-6):
    """
    Calcule la volatilité implicite à partir du prix marché d'une option.
    
    price_market : Prix de l'option observé sur le marché
    S            : Prix spot de l’actif sous-jacent
    K            : Strike de l’option
    T            : Temps jusqu’à maturité (en années)
    r            : Taux sans risque
    option_type  : 'call' ou 'put'
    tol          : Tolérance numérique pour la précision de la solution
    """
    def objective_function(sigma):
        price = black_scholes_price(S, K, T, r, sigma, option_type)
        return price - price_market

    try:
        # Recherche d'une racine entre des bornes réalistes
        implied_vol = brentq(objective_function, 1e-6, 3.0, xtol=tol)
        return implied_vol
    except ValueError:
        return None  # Si pas de solution dans l'intervalle
    
if __name__ == "__main__":
    price_market = 6.5  # prix observé sur le marché
    S = 100             # spot
    K = 100             # strike
    T = 30 / 365        # 30 jours
    r = 0.01
    option_type = "call"

    vol_imp = implied_volatility(price_market, S, K, T, r, option_type)

    if vol_imp:
        print(f"Volatilité implicite extraite : {vol_imp:.2%}")
    else:
        print("Volatilité implicite non trouvée dans l'intervalle.")