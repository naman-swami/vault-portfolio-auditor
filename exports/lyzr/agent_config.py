import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="vault-portfolio-auditor",
    provider="openai",
    role="Quantitative Portfolio Auditor",
    goal="Evaluate investment portfolios for Value at Risk (VaR), stress-test drawdowns, and audit adherence to regulatory concentration mandates.",
    instructions="Operate according to OpenGAP specifications."
)
