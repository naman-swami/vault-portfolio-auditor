import json
import argparse
from src.risk_engine import PortfolioRiskAuditor

def main():
    parser = argparse.ArgumentParser(description="Vault Portfolio Risk Auditor CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated portfolio risk audit")
    args = parser.parse_args()

    auditor = PortfolioRiskAuditor()
    sample_portfolio = {
        "portfolio_id": "HEDGE-EQUITY-007",
        "total_value_usd": 5000000,
        "annualized_return": 0.165,
        "annualized_volatility": 0.142,
        "historical_equity_curve": [5000000, 5200000, 5150000, 5400000, 4900000, 5300000, 5650000]
    }

    report = auditor.audit_portfolio(sample_portfolio)
    print("="*60)
    print(" VAULT PORTFOLIO RISK & COMPLIANCE AUDIT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
