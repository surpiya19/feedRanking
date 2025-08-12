## Overview 

**feedRanking** is an analytical project simulating a TikTok-style dataset to evaluate the impact of different feed-ranking algorithms on user engagement. This project compares a control algorithm with a variant that prioritizes short comedy videos, aiming to determine whether the new algorithm significantly increases user interactions.

## Project Workflow 

1. **Data Preprocessing**  
2. **Feature Engineering**  
3. **Statistical Testing**  
4. **Visualization**  
5. **Business Recommendation**  

## Analysis Workflow
- Calculated average engagement rates for control and variant groups.
- Conducted a two-proportion z-test to assess statistical significance.
- Analyzed daily engagement trends via time series visualization.

## Synthetic Data Generation

The dataset used in this project was synthetically generated to simulate user interactions on a TikTok-style video platform. This approach enables controlled experimentation without relying on real user data.

Key points about the data generation process:

- Created 10,000 users and 2,000 videos spanning 7 categories such as dance, comedy, music, sports, gaming, food, and fashion.
- Simulated 50,000 user-video interaction records by randomly sampling user and video pairs.
- Assigned video lengths randomly between 5 and 60 seconds.
- Generated watch times based on a normal distribution centered around 70% of the video length, clipped to valid ranges.
- Modeled engagement behaviors (likes, shares, comments, follows) with probabilities proportional to watch time.
- Randomly split interactions into control and variant groups, with a slight boost in like probability for the variant group to mimic a new recommendation algorithm.
- Generated timestamps for interactions over the past 30 days to enable time series analyses.
- Created an `engaged` flag that aggregates likes, shares, and comments as an indicator of overall engagement.

This synthetic dataset provides a realistic and flexible foundation for analyzing and testing the effects of different feed-ranking algorithms on user engagement.

## Business Recommendation

Based on the p-value from the statistical test:

```python
if p_val < 0.05:
    print("Statistically significant increase in engagement for variant group → Recommend rollout!")
else:
    print("No statistically significant difference → Further testing needed.")
