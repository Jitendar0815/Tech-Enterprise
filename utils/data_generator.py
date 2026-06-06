import numpy as np
import pandas as pd

def generate_attention(media='video', seed=42):
    np.random.seed(seed)
    progress = np.linspace(0, 100, 100)
    if media == 'video':
        retention = 100 * np.exp(-0.03 * progress) + np.random.normal(0, 2, 100)
    elif media == 'music':
        retention = 100 * np.exp(-0.02 * progress) + 5 * np.sin(progress/10) + np.random.normal(0, 1.5, 100)
    else:
        retention = 100 * np.exp(-0.04 * progress) + np.random.normal(0, 3, 100)
    retention = np.clip(retention, 0, 100)
    
    total_duration = np.random.choice([60, 120, 300, 600])
    timestamps = np.linspace(0, total_duration, 100)
    interactions = np.random.poisson(0.5, 100)
    interactions = np.clip(interactions, 0, 5)
    
    df = pd.DataFrame({
        'timestamp_sec': timestamps,
        'progress_pct': progress,
        'retention_pct': retention,
        'interactions': interactions
    })
    
    avg_ret = np.mean(retention)
    completion = retention.iloc[-1]
    score = 0.6 * avg_ret + 0.4 * completion
    
    # Find sharp drops (>10% drop)
    diffs = df['retention_pct'].diff()
    drop_idx = diffs < -10
    drop_points = df.loc[drop_idx, 'timestamp_sec'].tolist()
    
    meta = {
        'title': f"Sample {media.capitalize()} Content",
        'media_type': media,
        'total_duration_sec': total_duration,
        'avg_retention': round(avg_ret, 1),
        'completion_rate': round(completion, 1),
        'attention_score': round(score, 1),
        'dropoff_points': drop_points
    }
    return df, meta
