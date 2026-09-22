# Vault Quantitative Risk Auditor

> **Institutional Multi-Asset Portfolio Risk Engine & Stress-Testing Oracle**  
> Formally calculating Parametric Value-at-Risk, Downside Volatility, and Macroeconomic Stress Resilience.

---

> [!IMPORTANT]
> **Regulatory Disclosure**: This agent operates as a quantitative risk computation engine. Outputs do not constitute individual investment advice under SEC/FINRA regulations. See [FINANCIAL_DISCLAIMER.md](FINANCIAL_DISCLAIMER.md) for jurisdictional terms.

---

### Risk Assessment Formulations

#### 1. Parametric Value-at-Risk (VaR)
Calculated across 1-year holding periods at both 95% ($z_{0.95} = 1.645$) and 99% ($z_{0.99} = 2.326$) confidence intervals:
$$VaR_{\alpha} = -\left(\mu_p + z_{\alpha} \cdot \sigma_p\right) \cdot W_0$$
Where $\mu_p$ is portfolio expected return, $\sigma_p$ is annualized portfolio standard deviation, and $W_0$ is total asset valuation under audit.

#### 2. Annualized Sharpe Ratio
Benchmarked against the prevailing risk-free treasury yield ($R_f = 4.50\%$):
$$S_p = \frac{R_p - R_f}{\sigma_p}$$

---

### Sample Institutional Risk Memorandum

Below is the verified computation generated from benchmark multi-asset growth funds (`data/sample_portfolio.json`):

```text
======================================================================
VAULT QUANTITATIVE RISK AUDIT MEMORANDUM
Asset Valuation: $10,000,000.00 USD | Benchmark: 60/40 Equity-Fixed Income
======================================================================
* Weighted Expected Return (Annual):  8.25%
* Portfolio Volatility (Annual):     14.10%
* Annualized Sharpe Ratio (Rf=4.5%):  0.27
* 1-Year Parametric VaR (95% CI):    -$1,494,450.00 (-14.94%)
* 1-Year Parametric VaR (99% CI):    -$2,453,160.00 (-24.53%)
* Macroeconomic Shock (-20% Equity): -$1,300,000.00 Loss
======================================================================
Risk Tier Assessment: BALANCED GROWTH (Sufficient Capital Reserve)
```

---

### Portfolio Ingestion & Stress Scenarios

Auditors can configure custom weight vectors and stress parameters directly through `audit.py`:

```bash
# Run quantitative audit on benchmark portfolio
python audit.py --demo

# Execute mathematical validation suite
pytest tests/ -v
```

Complete audit trail methodology, confidence scoring, and source attribution protocols are documented in [EXPLAINABILITY.md](EXPLAINABILITY.md). Framework exports (OpenAI SDK, CrewAI, Claude Code, Lyzr) are available under `exports/`.
