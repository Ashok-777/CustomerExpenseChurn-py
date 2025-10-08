import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from google.colab import files

# Upload CSV
uploaded = files.upload()
for filename in uploaded.keys():
    data = pd.read_csv(filename)
print(data.head())

# Sentiment Analysis
data["sentiment_score"] = data["feedback"].apply(lambda x: TextBlob(str(x)).sentiment.polarity if x else 0)

# Feature Engineering
summary = data.groupby("customer_id").agg({
    "amount": "sum",
    "rating": "mean",
    "sentiment_score": "mean",
    "days_since_last_purchase": "mean"
}).reset_index()
summary.rename(columns={
    "amount": "total_spent",
    "rating": "avg_rating",
    "sentiment_score": "avg_sentiment",
    "days_since_last_purchase": "avg_days_gap"
}, inplace=True)
summary["churn"] = ((summary["avg_days_gap"] > 40) & (summary["avg_sentiment"] < 0)).astype(int)

# ML Model
X = summary[["total_spent", "avg_rating", "avg_sentiment", "avg_days_gap"]]
y = summary["churn"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
summary["churn_prob"] = model.predict_proba(X)[:, 1]

# Visualizations
plt.figure(figsize=(12, 5))
category_expenses = data.groupby("category")["amount"].sum()
plt.bar(category_expenses.index, category_expenses.values, color="skyblue")
plt.title("Total Expenses by Category")
plt.show()

plt.figure(figsize=(12, 5))
plt.hist(summary["avg_sentiment"], bins=10, color="orange", edgecolor="black")
plt.title("Average Sentiment Distribution")
plt.show()

plt.figure(figsize=(8, 5))
plt.barh(X.columns, model.feature_importances_, color="green")
plt.title("Feature Importance for Churn")
plt.show()

# Smart Insights
for _, row in summary.iterrows():
    if row["churn_prob"] > 0.7 and row["total_spent"] > 1000:
        print(f"⚠️ Customer {row['customer_id']} is HIGH spender & HIGH churn risk")
    elif row["churn_prob"] > 0.7:
        print(f"⚠️ Customer {row['customer_id']} is at churn risk")
    elif row["avg_sentiment"] < 0:
        print(f"ℹ️ Customer {row['customer_id']} shows negative feedback")
    else:
        print(f"✅ Customer {row['customer_id']} is healthy")
