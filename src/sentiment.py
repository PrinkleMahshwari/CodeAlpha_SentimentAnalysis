# import the libraries
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure directories exist
os.makedirs('data', exist_ok=True)
os.makedirs('screenshots', exist_ok=True)

# create a sample dataset of amazon laptop review
# we generate in this code so we don't get error 404
print("Generating sample dataset...")
data = {
    'Review': [
        "I absolutely love this laptop! It's incredibly fast and the screen is gorgeous.",
        "Worst purchase ever. It crashed on day one and customer service was unhelpful.",
        "The battery life is decent, but the keyboard feels a bit cheap.",
        "Fantastic performance for gaming! Highly recommend it.",
        "Do not buy this. It overheats constantly and the fan is so loud.",
        "It's an okay laptop for the price. Nothing special, but it gets the job done.",
        "Best laptop I've ever owned. The build quality is premium! 😍",
        "I'm very disappointed. The screen arrived with a dead pixel.",
        "Average product. Good for browsing, but struggles with heavy software.",
        "Super satisfied with my purchase! Delivery was fast too. 🚀",
        "Terrible experience. The trackpad stopped working after a week.",
        "The display is bright and crisp, but the speakers are quite tinny.",
        "Not worth the money. You can get better specs for the same price elsewhere.",
        "Solid machine. I use it for coding and it handles everything perfectly.",
        "It's fine. I have no strong complaints, but I'm not amazed either."
    ]
}
df = pd.DataFrame(data)

# save to data folder
df.to_csv('data/reviews.csv', index=False)
print("✅ Dataset saved to 'data/reviews.csv'\n")

# initialize vader sentiment analyzer
print("Running Sentiment Analysis...")
analyzer = SentimentIntensityAnalyzer()

# create empty lists to store our results
compound_scores = []
sentiments = []

# loop through each review and analyze it
for review in df['Review']:
    # get the sentiment dictionary for review
    scores = analyzer.polarity_scores(review)

    # extract the compound score (ranges from -1 to +1)
    compound = scores['compound']
    compound_scores.append(compound)
    
    # classify the sentiment based on the compound score
    if compound >= 0.05:
        sentiments.append('Positive')
    elif compound <= -0.05:
        sentiments.append('Negative')
    else:
        sentiments.append('Neutral')

# add new data to our DataFrame
df['compound_scores'] = compound_scores
df['sentiments'] = sentiments  # Keeps column consistent

# display a neat table in the terminal
print(df.to_markdown(index=False))
print("\n" + "="*40 + "\n")

# visualizing the results
print("Creating Visualizations...")
sns.set_theme(style="whitegrid")

# plot: count of sentiments
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='sentiments', hue='sentiments', palette={'Positive': 'green', 'Negative': 'red', 'Neutral': 'gray'}, legend=False)
plt.title('Sentiment Distribution of Laptop Reviews', fontsize=16)
plt.xlabel('Sentiment', fontsize=12)
plt.ylabel('Number of Reviews', fontsize=12)
plt.savefig('screenshots/sentiment_distribution.png')
plt.close()
print("✅ Plot saved: screenshots/sentiment_distribution.png")

# save the analyzed data to a new CSV
df.to_csv('data/analyzed_reviews.csv', index=False)
print("\n🎉 Sentiment Analysis Complete!")
