# model_loader.py
import numpy as np

class LightweightUFOClassifier:
    def __init__(self):
        # Manually set trained coefficients (replace with your actual values)
        self.coef_ = np.array([[0.12, -0.05, 0.08]])  # From original model.coef_
        self.intercept_ = np.array([-0.32])            # From original model.intercept_
        
    def predict(self, X):
        logits = np.dot(X, self.coef_.T) + self.intercept_
        return (logits > 0).astype(int)

# Initialize model with trained parameters
ufo_model = LightweightUFOClassifier()