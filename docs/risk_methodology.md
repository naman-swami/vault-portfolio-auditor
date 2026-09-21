# Quantitative Risk Methodology

## Parametric Value-at-Risk (VaR)
Parametric VaR evaluates the maximum expected loss over horizon $T$ at confidence level $1 - \alpha$:

$$\text{VaR}_{\alpha} = z_{\alpha} \cdot \sigma_p \cdot V$$

Where:
- $z_{0.95} = 1.645$ (95% single-tailed Gaussian normal)
- $z_{0.99} = 2.326$ (99% single-tailed Gaussian normal)
- $\sigma_p$ is annualized portfolio volatility
- $V$ is total portfolio market value

## Sharpe Ratio
$$\text{Sharpe} = \frac{\mathbb{E}[R_p] - R_f}{\sigma_p}$$
