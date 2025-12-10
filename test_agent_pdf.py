import sys
import os

# 1. Force Python to load modules from THIS folder first
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# 2. Now import the module
import pdf_single_agent
print("📌 IMPORTED FROM:", pdf_single_agent.__file__)

# 3. Import the function
from pdf_single_agent import generate_pdf

# --- Mock property + metrics (safe test values)
property_data = {
    "street_address": "123 Main St",
    "zip_code": "94566"
}

metrics = {
    "First Year Cash Flow ($)": -2000,
    "Cash-on-Cash Return (%)": 3,
    "Expected Annual Return": 7,
    "Grade": "B",
    "Annual Rents $ (by year)": [2200, 2400, 2600, 2800, 3000]
}

summary_text = "This property presents a moderate-risk income investment with stable long-term appreciation."

# --- Generate PDF buffer
buffer = generate_pdf(
    property_data=property_data,
    metrics=metrics,
    summary_text=summary_text,
    agent_name="Agent X",
    brokerage_name="Intero Real Estate",
    client_name="John & Mary Smith",
    agent_notes="This deal works well for a long-term hold given current rental demand.",
    improvement_name="Kitchen Remodel",
    improvement_cost=24000,
    improvement_rent_impact=350
)

# --- Write to file so you can open it
with open("TEST_AGENT_REPORT.pdf", "wb") as f:
    f.write(buffer.getvalue())

print("✅ Agent PDF created: TEST_AGENT_REPORT.pdf")
