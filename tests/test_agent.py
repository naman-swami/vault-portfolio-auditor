import pytest
from src.risk_engine import PortfolioRiskAuditor

def test_sharpe_ratio_computation():
    auditor = PortfolioRiskAuditor(risk_free_rate=0.04)
    # (0.12 - 0.04) / 0.16 = 0.50
    assert auditor.calculate_sharpe_ratio(0.12, 0.16) == 0.50

def test_drawdown_computation():
    auditor = PortfolioRiskAuditor()
    curve = [100, 120, 90, 110, 130]
    # peak 120 dropped to 90 -> (120-90)/120 = 0.25 (25%)
    assert auditor.calculate_max_drawdown(curve) == 0.25

def test_full_portfolio_audit():
    auditor = PortfolioRiskAuditor()
    portfolio = {
        "portfolio_id": "TEST-PORT",
        "total_value_usd": 1000000,
        "annualized_return": 0.15,
        "annualized_volatility": 0.10,
        "historical_equity_curve": [100, 105, 110, 108, 115]
    }
    report = auditor.audit_portfolio(portfolio)
    assert report["risk_profile"] == "MODERATE"
    assert report["audit_verdict"] == "HEALTHY"
    assert report["metrics"]["var_95_daily_usd"] > 0
