"""
Machine Learning Training Pipeline for Career Guidance System.
Trains, evaluates, benchmarks, and exports a Random Forest Classifier
along with feature metadata for production deployment.
"""

import os
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

DATASET_PATH = "data/career_dataset.csv"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "career_model.pkl")
META_PATH = os.path.join(MODEL_DIR, "feature_meta.pkl")


def train_and_evaluate():
    print("=" * 70)
    print("  AI-BASED SMART CAREER GUIDANCE SYSTEM: MODEL TRAINING PIPELINE")
    print("=" * 70)

    # 1. Load Dataset
    if not os.path.exists(DATASET_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATASET_PATH}. Run data/generate_dataset.py first.")

    df = pd.read_csv(DATASET_PATH)
    print(f"\n[1] Dataset Loaded Successfully:")
    print(f"    - Total records: {len(df)}")
    print(f"    - Total features: {len(df.columns) - 1}")
    print(f"    - Target classes: {df['career'].unique().tolist()}")

    X = df.drop(columns=["career"])
    y = df["career"]
    feature_names = list(X.columns)

    # 2. Stratified Train-Test Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"\n[2] Data Split:")
    print(f"    - Training samples: {len(X_train)} (80%)")
    print(f"    - Testing samples:  {len(X_test)} (20%)")

    # 3. Model Comparison Benchmark
    print(f"\n[3] Model Benchmarking (5-Fold Cross Validation):")
    models = {
        "Decision Tree": DecisionTreeClassifier(max_depth=10, random_state=42),
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Random Forest (Ensemble)": RandomForestClassifier(
            n_estimators=150,
            max_depth=12,
            min_samples_split=4,
            random_state=42
        )
    }

    benchmark_results = {}
    for name, model in models.items():
        cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring="accuracy")
        benchmark_results[name] = cv_scores.mean()
        print(f"    - {name:<26}: Mean CV Accuracy = {cv_scores.mean() * 100:.2f}% (Std: +/- {cv_scores.std() * 100:.2f}%)")

    # 4. Train Selected Champion Model (Random Forest)
    champion = models["Random Forest (Ensemble)"]
    champion.fit(X_train, y_train)

    # 5. Evaluate Champion on Unseen Test Set
    y_pred = champion.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)
    print(f"\n[4] Champion Model Evaluation on Test Set:")
    print(f"    ==================================================")
    print(f"    TEST ACCURACY: {test_accuracy * 100:.2f}%")
    print(f"    ==================================================")

    print("\n[5] Classification Report:")
    report = classification_report(y_test, y_pred)
    print(report)

    print("[6] Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred, labels=champion.classes_)
    cm_df = pd.DataFrame(cm, index=champion.classes_, columns=champion.classes_)
    print(cm_df)

    # 6. Feature Importance Analysis
    importances = champion.feature_importances_
    sorted_idx = np.argsort(importances)[::-1]
    print("\n[7] Top 10 Most Influential Features:")
    top_features = []
    for i in range(min(10, len(sorted_idx))):
        idx = sorted_idx[i]
        top_features.append({"feature": feature_names[idx], "importance": round(float(importances[idx]), 4)})
        print(f"    {i+1:2d}. {feature_names[idx]:<28}: {importances[idx] * 100:.2f}%")

    # 7. Export Model and Metadata
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(champion, MODEL_PATH)

    meta = {
        "feature_names": feature_names,
        "classes": champion.classes_.tolist(),
        "test_accuracy": round(float(test_accuracy) * 100, 2),
        "top_features": top_features,
        "benchmark": {k: round(v * 100, 2) for k, v in benchmark_results.items()}
    }
    joblib.dump(meta, META_PATH)

    print(f"\n[8] Model Exported:")
    print(f"    - Model file:    {MODEL_PATH}")
    print(f"    - Metadata file: {META_PATH}")

    # 8. Sanity Inference Test
    print("\n[9] Running Sanity Prediction on Sample Input...")
    sample_input = X_test.iloc[0:1]
    pred_career = champion.predict(sample_input)[0]
    pred_probs = champion.predict_proba(sample_input)[0]
    print(f"    - True Class:       {y_test.iloc[0]}")
    print(f"    - Predicted Career: {pred_career}")
    print("    - Class Probabilities:")
    for cls, prob in zip(champion.classes_, pred_probs):
        print(f"      * {cls:<24}: {prob * 100:5.1f}%")

    print("\n" + "=" * 70)
    print("  MODEL TRAINING PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 70)


if __name__ == "__main__":
    train_and_evaluate()
