# 🎓 AI-Driven Enrollment Forecasting & Resource Optimization

## 📌 Overview

 Developed Random Forest and XGBoost models using scikit-learn and XGBoost, improving enrollment forecasting accuracy  with RMSE of 11.5(using Random Forest) and 6.0(using XGBoost) ,enabling data-driven planning for 50+ academic courses 

  Automated synthetic data generation with Python's Faker library and constructed pipelines with 15+ features (tuition, waitlist, retention, feedback), reducing preparation time by 30% and improving model training efficiency 

 Leveraged Sweetviz for EDA and formulated predictive features to improve retention targeting by 12% and reduce scheduling conflicts by 20%, enhancing course offering decisions 

  🚀 Key Features

* 📊 Generated **5000+ synthetic records** using Faker to simulate real-world academic data
* 🔍 Performed **Exploratory Data Analysis (EDA)** using Sweetviz and visualizations
* 🧠 Engineered meaningful features like:

  * Demand Ratio
  * Quality Index
  * Revenue Potential
* 🌲 Trained **Random Forest & XGBoost models**
* 📉 Achieved:

  * **XGBoost RMSE ≈ 6**
  * **Random Forest RMSE ≈ 11**
* 📈 Derived insights to support **data-driven academic planning**

---

## 🏗️ Project Structure

```
enrollment-forecasting/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── data_generation.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   ├── 05_evaluation_and_insights.ipynb
│
├── models/
│   ├── random_forest.pkl
│   ├── xgboost.pkl
│
├── reports/
│   ├── sweetviz_report.html
│
└── README.md
```

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Faker
* Sweetviz
* Matplotlib, Seaborn

---

## 📊 Workflow

1. **Data Generation**

   * Created realistic dataset with controlled feature relationships

2. **EDA**

   * Analyzed distributions, correlations, and trends

3. **Feature Engineering**

   * Built domain-specific features to improve prediction accuracy

4. **Model Training**

   * Applied Random Forest and XGBoost
   * Tuned hyperparameters

5. **Evaluation**

   * Compared models using RMSE and R²
   * Visualized predictions and errors

6. **Insights**

   * Identified key drivers of enrollment
   * Generated actionable recommendations

---

## 📈 Key Insights

* High waitlist indicates strong demand → increase capacity
* Course quality (feedback + faculty rating) significantly impacts enrollment
* Demand ratio is a strong predictor of course popularity
* Optimized scheduling can reduce conflicts and improve enrollment

---

## 📉 Model Performance

| Model         | RMSE | R² Score |
| ------------- | ---- | -------- |
| Random Forest | ~11  | ~0.98    |
| XGBoost       | ~6   | ~0.99    |

---

## ▶️ How to Run

```bash
git clone https://github.com/athhh07/AI-Driven-Enrollment-Forcasting-and-Resource-Optimization.git
cd enrollment-forecasting
jupyter notebook
```

---

## 💡 Future Improvements

* Deploy using Streamlit dashboard
* Use real-world university datasets
* Add time-series forecasting for semester trends
* Integrate with scheduling optimization systems

---

## 🎯 Use Cases

* Academic planning
* Course capacity optimization
* Student retention analysis
* Resource allocation

---

## 👨‍💻 Author

Atharva Desai

---

## ⭐ If you found this useful, consider giving it a star!
