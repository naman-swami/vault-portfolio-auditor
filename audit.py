import argparse
import json
import os
from models.risk_metrics import PortfolioRiskModel

def main():
    parser = argparse.ArgumentParser(description="Vault Portfolio Quantitative Risk CLI")
    parser.add_argument("--demo", action="store_true", help="Audit sample $10M portfolio")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "data", "sample_portfolio.json")

    if args.demo:
        with open(data_file, "r") as f:
            portfolio = json.load(f)
        
        metrics = PortfolioRiskModel.calculate_metrics(
            positions=portfolio["positions"],
            total_value=portfolio["total_value_usd"]
        )

        print("=== VAULT QUANTITATIVE PORTFOLIO AUDIT REPORT ===\n")
        print(f"Portfolio ID: {portfolio['portfolio_id']}")
        print(f"Total Market Value: ${portfolio['total_value_usd']:,.2f}")
        print(f"Annual Expected Return: {metrics['portfolio_return_annual']*100:.2f}%")
        print(f"Annual Volatility: {metrics['portfolio_volatility_annual']*100:.2f}% | Rating: {metrics['risk_rating']}")
        print(f"Sharpe Ratio (Rf=4.5%): {metrics['sharpe_ratio']}\n")
        print("--- Value-at-Risk (VaR) ---")
        print(f"  95% 1-Year VaR: {metrics['var_95_annual_pct']*100:.2f}% (${metrics['var_95_annual_usd']:,.2f})")
        print(f"  99% 1-Year VaR: {metrics['var_99_annual_pct']*100:.2f}% (${metrics['var_99_annual_usd']:,.2f})")
        print(f"  Simulated -20% Equity Crash Exposure: ${metrics['stress_scenario_market_crash_usd']:,.2f}\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
