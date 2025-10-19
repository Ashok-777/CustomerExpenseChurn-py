# CustomerExpenseChurn-py


# Smart Expenses + Feedback + Churn Prediction  Analyze customer spending, feedback sentiment, and churn risk with a Python-based interactive tool. Upload CSV data, run sentiment analysis, predict churn with ML, and generate smart insights &amp; visualizations.  Technologies: Python, Pandas, Matplotlib, Scikit-learn, TextBlob
# Smart Expenses + Feedback + Churn Prediction Dashboard

## Overview
The **Smart Expenses + Feedback + Churn Prediction Dashboard** is a Python-based project that helps businesses analyze customer transactions, evaluate customer feedback sentiment, and predict churn risk. This tool allows users to upload customer data in CSV format and instantly generate actionable insights, visualizations, and predictions for better decision-making.

This project is ideal for:
- **Students** learning data analysis and machine learning
- **Portfolio projects** demonstrating Python and data visualization skills
- **Small business owners** looking for insights on customer retention
- 
## Features

### 1. CSV File Upload
- Upload any CSV file containing customer data.
- Columns required: `customer_id`, `amount`, `category`, `feedback`, `rating`, `days_since_last_purchase`.
- Works seamlessly with **Google Colab** for quick experimentation.

### 2. Sentiment Analysis
- Extracts polarity scores from customer feedback using **TextBlob**.
- Scores range from -1 (negative) to 1 (positive).
- Helps identify customer satisfaction levels automatically.

### 3. Feature Engineering for Churn
Aggregates customer-level metrics:
- `total_spent`: Total money spent by the customer
- `avg_rating`: Average rating given by the customer
- `avg_sentiment`: Average sentiment score
- `avg_days_gap`: Average days since last purchase

Generates **churn labels** using business rules:
- Example: Customers with low sentiment and long inactivity are labeled as high churn risk.

### 4. Machine Learning Churn Prediction
- Uses a **Random Forest Classifier** for churn prediction.
- Outputs both predicted labels and churn probabilities for each customer.
- Feature importance visualization helps understand drivers of churn.

### 5. Visualizations
- **Bar Chart:** Total expenses per category
- **Histogram:** Distribution of sentiment scores
- **Horizontal Bar Chart:** Feature importance for churn prediction
- Helps stakeholders understand key business metrics quickly.

### 6. Smart Insights & Recommendations
- Automatically generates recommendations based on:
  - High spending customers at high risk → offer loyalty programs
  - Negative sentiment customers → improve service quality
  - General low-risk customers → maintain engagement

## Technologies Used

- **Python 3.x** – Core programming language
- **Pandas** – Data manipulation
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **TextBlob** – Sentiment analysis
- **Scikit-learn** – Machine learning
- **Google Colab** – File upload and interactive execution

## CSV Format Example

```csv
customer_id,amount,category,feedback,rating,days_since_last_purchase
1,250,Electronics,"Great product!",5,30
2,120,Groceries,"Not satisfied",2,50
3,300,Clothing,"Loved it",4,20
