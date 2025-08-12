import pandas as pd
import numpy as np
import os

# Parameters
n_users = 10000
n_videos = 2000
n_rows = 50000
np.random.seed(42)

users = np.arange(1, n_users+1)
videos = np.arange(1, n_videos+1)
categories = ['dance', 'comedy', 'music', 'sports', 'gaming', 'food', 'fashion']

# Randomly sample interactions
user_ids = np.random.choice(users, size=n_rows)
video_ids = np.random.choice(videos, size=n_rows)
video_categories = np.random.choice(categories, size=n_rows)
video_lengths = np.random.randint(5, 61, size=n_rows)

watch_times = np.minimum(video_lengths, np.random.normal(loc=video_lengths*0.7, scale=3).astype(int))
watch_times = np.clip(watch_times, 1, None)

like_probs = watch_times / video_lengths
like_probs = np.nan_to_num(like_probs, nan=0.0)  # Replace NaNs with 0

groups = np.random.choice(['control', 'variant'], size=n_rows)

# Boost probabilities for variant group only
boosted_like_probs = like_probs + 0.02
boosted_like_probs = np.clip(boosted_like_probs, 0, 1)

# Create liked array with boosted probabilities for variant group
liked = np.zeros(n_rows, dtype=int)
liked[groups == 'control'] = np.random.binomial(1, like_probs[groups == 'control'])
liked[groups == 'variant'] = np.random.binomial(1, boosted_like_probs[groups == 'variant'])

share_probs = like_probs * 0.2
shared = np.random.binomial(1, share_probs)

comment_probs = like_probs * 0.1
commented = np.random.binomial(1, comment_probs)

follow_probs = like_probs * 0.05
follow_creator = np.random.binomial(1, follow_probs)

dates = pd.date_range(end=pd.Timestamp.today(), periods=30).to_pydatetime().tolist()
dates_sample = np.random.choice(dates, size=n_rows)

df = pd.DataFrame({
    'user_id': user_ids,
    'video_id': video_ids,
    'category': video_categories,
    'length_sec': video_lengths,
    'watch_time_sec': watch_times,
    'liked': liked,
    'shared': shared,
    'commented': commented,
    'follow_creator': follow_creator,
    'group': groups,
    'date': dates_sample
})

# Create 'engaged' column to indicate any engagement
df['engagement'] = df[['liked', 'shared', 'commented']].sum(axis=1)
df['engaged'] = (df['engagement'] > 0).astype(int)

# Save dataset
os.makedirs("data", exist_ok=True)
df.to_csv("data/tiktok_synthetic_data.csv", index=False)
print(f"Dataset generated with shape {df.shape} and saved to data/tiktok_synthetic_data.csv")
