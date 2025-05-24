# Load the dataset
import pickle

import pandas as pd
import numpy as np
from charset_normalizer import models
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
from typing import List
import joblib

def train_model() -> None:
    """Trains an XGBClassifier to predict diabetes.
    """
    data = pd.read_csv("/opt/airflow/dags/scripts/diabetes.csv")  # Spécifiez le chemin local de votre fichier CSV
    y = data['Outcome']
    x = data.drop(['Outcome'], axis=1)
    x_train, x_val, y_train, y_val = train_test_split(
        x, y, test_size=0.2, random_state=101
    )

    model = XGBClassifier(
        n_estimators=100, max_depth=11, learning_rate=0.1,
        use_label_encoder=False, verbosity=0,
        scale_pos_weight=1.8
    )
    model.fit(
        x_train, y_train,
        eval_set=[(x_train, y_train), (x_val, y_val)],
        eval_metric='auc',
        early_stopping_rounds=8,
        verbose=True
    )
    print('XGB classifier saved')
    # Enregistrez le modèle avec joblib
    joblib.dump(model, '/opt/airflow/dags/scripts/xgb_model.pkl')
    print('XGB classifier saved as xgb_model.pkl')
    y_val_pred = model.predict_proba(x_val)[:, 1]

    print('XGB classifier saved')


def predict_diabetes_probability(data: List[float], verbose=True) -> float:
    """Returns the model's predicted probability of diabetes from the given
    physiological data.

    Args:
        data (List[float]): A list of the physiological data.

    Returns:
        float: Predicted probability of diabetes,
    """
    print('Predicting...\n' if verbose else "", end="")
    xgb_model = XGBClassifier()
    print('Loading model...\n' if verbose else "", end="")
    xgb_model.load_model('xgb_model.pkl')
    print('Making Prediction...\n' if verbose else "", end="")
    prediction = xgb_model.predict_proba(np.array(data).reshape(1, -1))[0][1]
    print(f'Predicted probability {round(prediction*100)} %\n' if verbose else "", end="")
    return prediction



if __name__ == "__main__":
    train_model()

