# Institutional Quantitative Risk & Regulatory Disclaimer

## 1. SEC & FINRA Regulatory Disclosures
This software system, **Vault Portfolio Quantitative Risk Auditor**, is provided solely as a quantitative risk analytics and computational research platform. 

> [!IMPORTANT]
> **No Investment Advice or Fiduciary Relationship**:
> - Neither this repository, nor the software code, nor any generated risk reports, memorandums, or metric computations constitute financial, legal, tax, or investment advice under the **Investment Advisers Act of 1940 (15 U.S.C. § 80b-1 et seq.)** or the **Securities Exchange Act of 1934**.
> - The software does not provide personalized recommendations to buy, sell, hold, or rebalance any security, equity, bond, derivative, commodity, or crypto-asset.
> - Use of this software does not establish an advisory, broker-dealer, or fiduciary relationship between the user and `@naman-swami` or any contributing entity.
> - Institutional and retail users must perform independent due diligence and consult certified financial planners, chartered financial analysts (CFA), and legal counsel before executing capital allocation decisions.

---

## 2. Mathematical Modeling Assumptions & Inherent Limitations

### A. Parametric Value-at-Risk (VaR)
Vault calculates 1-year Parametric Value-at-Risk using the delta-normal formulation:
$$VaR_{\alpha} = -\left(\mu_p + z_{\alpha} \cdot \sigma_p\right) \cdot W_0$$

Users must account for the following structural assumptions and edge cases:
1. **Normality Assumption**: The model assumes that portfolio asset returns follow a multivariate Gaussian distribution. Real-world financial asset returns exhibit significant **leptokurtosis (fat tails)** and negative skewness during liquidity crises. Consequently, parametric VaR may substantially underestimate actual tail losses during black swan events.
2. **Stationarity of Volatility**: The annualized volatility ($\sigma_p$) and asset covariance matrices are estimated from historical lookback periods. In high-volatility regimes or structural market breaks (e.g., sudden interest rate shocks, geopolitical conflict), historical correlations often break down toward $+1.0$.
3. **Liquidity Horizon**: The standard model assumes all portfolio positions can be liquidated within the holding period without generating market price impact or slippage. Illiquid private assets, real estate, and micro-cap equities violate this assumption.

### B. Sharpe Ratio Benchmarks
Annualized Sharpe calculations utilize a risk-free rate benchmark ($R_f = 4.50\%$), calibrated to short-term U.S. Treasury Bill yields:
$$S_p = \frac{R_p - R_f}{\sigma_p}$$
The Sharpe ratio penalizes upside volatility identically to downside volatility. For asymmetric return distributions, users should reference the Sortino ratio or Omega ratio.

---

## 3. Macroeconomic Stress Testing Framework
Stress testing simulations (such as the $-20\%$ equity crash shock in `models/risk_metrics.py`) apply deterministic factor shocks across defined asset classes:
- Large-Cap / Growth Equities: $\beta = 1.00$ to $1.25$ factor sensitivity.
- Fixed Income / Sovereign Bonds: Duration-adjusted convexity shifts.
- Cash & Equivalents: Zero market loss, subject to inflation drag.

These scenarios do not forecast actual market outcomes and should be treated as synthetic resilience boundaries for capital preservation planning.
