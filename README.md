# TikTok A/B Test Analysis

## 📌 Overview
This project simulates a TikTok-style dataset with user–video interactions, then analyzes an A/B test where two feed-ranking algorithms are compared to measure engagement impact.

**Scenario:**  
- **Control:** Current recommendation system.  
- **Variant:** New algorithm that favors short comedy videos.  
- **Goal:** Determine if the new algorithm increases engagement rate.

---

## 📂 Dataset Schema
| Column           | Description |
|------------------|-------------|
| user_id          | Unique user ID |
| video_id         | Unique video ID |
| category         | Video genre (dance, comedy, etc.) |
| length_sec       | Video length in seconds |
| watch_time_sec   | Total seconds watched |
| liked            | 1 if user liked the video |
| shared           | 1 if user shared the video |
| commented        | 1 if user commented |
| follow_creator   | 1 if user followed the creator |
| group            | 'control' or 'variant' |
| date             | Interaction date |

---

## 🛠️ Steps
1. **Data Generation** — Synthetic TikTok-like interactions using `scripts/data_generation.py`.
2. **Exploratory Analysis** — Overview of engagement metrics.
3. **Hypothesis Testing** — Two-proportion z-test to check if engagement improved.
4. **Visualization** — Compare control vs. variant engagement rates.
5. **Recommendation** — Business decision based on statistical results.

---

## 📊 Example Analysis
- Engagement rate:  
- 
