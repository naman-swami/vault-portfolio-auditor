# Explainability — vault-portfolio-auditor

## Decision Reasoning
Vault determines portfolio health by computing covariance matrices, historical and parametric Value at Risk (VaR 95%/99%), and comparing active asset weights against mandated investment policy statement (IPS) drift thresholds.

## Data Sources and Inputs Used
Curated historical asset pricing series, macroeconomic benchmark indices, SEC/FINRA regulatory filings, and user-provided portfolio holding weights and transaction logs.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, vault-portfolio-auditor assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, vault-portfolio-auditor will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, vault-portfolio-auditor explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
vault-portfolio-auditor actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Black Swan Events: Parametric VaR assumes normal or student-t distributions and may underestimate tail-risk catastrophes.
- Liquidity Constraints: Cannot guarantee order execution at modelled mark-to-market prices during market illiquidity.
- Tax Advice: Does not provide certified individual tax or legal estate planning advice.
- Market Timing: Models do not speculate on short-term market momentum or intraday fluctuations.

## Uncertainty Quantification Approach
During regime shifts (e.g., sudden interest rate pivots, geopolitical crises), historical correlation matrices break down. Vault explicitly expands its confidence intervals, highlights correlation breakdown risks, and recommends conservative hedging buffers.
