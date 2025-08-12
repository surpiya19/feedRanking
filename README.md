## Overview

**feedRanking** is an analytical project simulating a TikTok-style dataset to evaluate the impact of different feed-ranking algorithms on user engagement. This project compares a control algorithm with a variant that prioritizes short comedy videos, aiming to determine whether the new algorithm significantly increases user interactions.

## Project Structure
feedRanking/
├── data/ # Synthetic dataset (CSV)
├── notebooks/ # Jupyter notebooks for analysis
├── scripts/ # Python scripts for data processing and analysis
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## Analysis Workflow

1. **Data Preprocessing**  
   Load and clean the synthetic dataset.
2. **Feature Engineering**  
   Define engagement metrics based on user interactions (likes, shares, comments).
3. **Statistical Testing**  
   Perform a two-proportion z-test to compare engagement rates between control and variant groups.
4. **Visualization**  
   Generate plots to visualize engagement trends over time.
5. **Business Recommendation**  
   Provide actionable insights based on statistical results.

## Key Findings
- Calculated average engagement rates for control and variant groups.
- Conducted a two-proportion z-test to assess statistical significance.
- Analyzed daily engagement trends via time series visualization.

## Business Recommendation

Based on the p-value from the statistical test:

```python
if p_val < 0.05:
    print("Statistically significant increase in engagement for variant group → Recommend rollout!")
else:
    print("No statistically significant difference → Further testing needed.")