import pandas as pd
import numpy as np
import joblib

model = joblib.load("models/xgboost.pkl")

def predict_enrollment(input_data):
    df = pd.DataFrame([input_data])

    df["demand_ratio"] = df["waitlist"] / df["capacity"]
    df["quality_index"] = df["feedback_score"] * df["faculty_rating"]
    df["revenue_potential"] = df["tuition_fee"] * df["capacity"]
    df["pressure"] = df["waitlist"] + df["capacity"]
    df["tuition_fee_log"] = np.log1p(df["tuition_fee"])

    if "course_id" in df.columns:
        df = df.drop(columns=["course_id"])

    model_features = [
        'tuition_fee',
        'waitlist',
        'retention_rate',
        'feedback_score',
        'faculty_rating',
        'capacity',
        'demand_ratio',
        'quality_index',
        'revenue_potential',
        'pressure',
        'tuition_fee_log'
    ]

    df = df[model_features]

    # Fix: model was trained without column names, so pass a plain numpy array
    prediction = model.predict(df.values)[0]
    return int(prediction)


if __name__ == "__main__":
    sample_input = {
        "course_id": 101,
        "tuition_fee": 50000,
        "waitlist": 25,
        "retention_rate": 0.8,
        "feedback_score": 4.2,
        "faculty_rating": 4.5,
        "capacity": 80
    }

    result = predict_enrollment(sample_input)
    print("Predicted Enrollment:", result)