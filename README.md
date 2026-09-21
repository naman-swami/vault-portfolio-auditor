# Vault Portfolio Quantitative Risk Auditor

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![Finance](https://img.shields.io/badge/Domain-Quantitative_Portfolio_Risk-gold.svg)](docs/risk_methodology.md)
[![Standard](https://img.shields.io/badge/Model-Parametric_VaR-blue.svg)](docs/risk_methodology.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

An institutional quantitative portfolio risk auditing engine calculating Parametric Value-at-Risk (VaR 95%/99%), annualized Sharpe ratios, asset-class exposure allocations, and macro stress scenario simulations.

```
                    ┌─────────────────────────┐
                    │ Multi-Asset Portfolio   │
                    │   (Weights & Values)    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ models/risk_metrics.py  │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │  Parametric VaR     │         │ Sharpe & Volatility │
      │  (95% / 99% USD)    │         │  (Risk Rating Tier) │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Risk & Capital Advisory │
                    │ (Stress Shock Exposure) │
                    └─────────────────────────┘
```

## Features

- **Parametric VaR Modeling**: Evaluates 1-year 95% and 99% maximum expected loss in USD.
- **Sharpe Ratio Calibration**: Incorporates configurable risk-free rate benchmarks ($R_f = 4.5\%$).
- **Macroeconomic Stress Shock**: Simulates downside impact of a 20% equity drawdown on capital reserves.
- **Fixture Grounding**: Includes benchmark $10M diversified growth portfolio fixture.

## Directory Structure

```
vault-portfolio-auditor/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint financial risk provenance
├── models/
│   └── risk_metrics.py              # Quantitative VaR & Sharpe engine
├── data/
│   └── sample_portfolio.json        # Benchmark multi-asset portfolio
├── docs/
│   └── risk_methodology.md          # Mathematical formulations
├── tests/
│   └── test_agent.py                # Quantitative validation tests
├── main.py                          # Portfolio risk CLI
└── requirements.txt
```

## Quick Start

```bash
# Run risk calculation test suite
pytest tests/ -v

# Audit sample $10M portfolio
python main.py --demo
```
