import os
import json
import pytest
from models.risk_metrics import PortfolioRiskModel

def test_risk_metrics_calculation():
    positions = [
        {"symbol": "SPY", "weight": 0.60, "asset_class": "US_EQUITY", "expected_annual_return": 0.10, "annual_volatility": 0.16},
        {"symbol": "BND", "weight": 0.40, "asset_class": "FIXED_INCOME", "expected_annual_return": 0.04, "annual_volatility": 0.06}
    ]
    res = PortfolioRiskModel.calculate_metrics(positions, total_value=1000000.0)
    
    expected_return = 0.60 * 0.10 + 0.40 * 0.04 # 0.076
    assert abs(res["portfolio_return_annual"] - 0.076) < 1e-4
    assert res["sharpe_ratio"] > 0
    assert res["var_95_annual_usd"] > 0
    assert res["var_99_annual_usd"] > res["var_95_annual_usd"]

def test_benchmark_portfolio_fixture():
    data_file = os.path.join(os.path.dirname(__file__), "..", "data", "sample_portfolio.json")
    with open(data_file, "r") as f:
        port = json.load(f)
    res = PortfolioRiskModel.calculate_metrics(port["positions"], port["total_value_usd"])
    assert res["risk_rating"] in ["CONSERVATIVE", "MODERATE", "AGGRESSIVE"]
    assert res["stress_scenario_market_crash_usd"] > 0
