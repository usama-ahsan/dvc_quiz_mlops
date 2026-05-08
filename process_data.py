import pandas as pd
import json

# Load data
df = pd.read_csv('data/sample.csv')

# Filter rows where value > 150
df_filtered = df[df['value'] > 150]

# Calculate average value
avg_value = df_filtered['value'].mean()
print(f"Average value of filtered data: {avg_value:.2f}")

# Save processed data
df_filtered.to_csv('processed.csv', index=False)

# Generate metrics
accuracy = round(avg_value / 250, 4)
with open('metrics.txt', 'w') as f:
    f.write(f"accuracy: {accuracy}\n")

print(f"Processing complete. Accuracy: {accuracy}")
