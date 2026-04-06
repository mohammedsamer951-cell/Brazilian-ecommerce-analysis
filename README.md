# Brazilian E-Commerce Analysis

## Business Question
Does delivery speed explain revenue differences across Brazilian states?

## Data
- 112,650 order items across 27 Brazilian states (Olist dataset)
- Variables: state, price, revenue, delivery days, total orders

## Key Findings
- Revenue and total orders: r = 0.999 (revenue is driven by volume, not price)
- Delivery speed and revenue: r = -0.596 (faster delivery = higher revenue)
- São Paulo is a major outlier — removing it drops mean revenue by 36%
- Remote states have higher average prices because customers only order high-value items worth the long wait

## Recommendation
Invest in logistics in North and Northeast states — 10 states earn under R$100K despite significant populations

## Tools Used
- Python, pandas, matplotlib
- Google Sheets for initial exploration

## Files
- script.py — full analysis
- revenue_by_state.png — bar chart
- delivery_vs_revenue..png.png — scatter plot
