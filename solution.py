import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 323297403 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    if not 0 <= p <= 1:
        raise ValueError("Confidence level must be between 0 and 1")

    def acceleration_coef(x):
        t = 47
        return 2 * x / (t ** 2)

    n_bootstraps = 10000
    bootstrap_samples = np.random.choice(x, size=(len(x), n_bootstraps), replace=True)

    acceleration_coefs = acceleration_coef(bootstrap_samples)

    alpha = 1 - p
    left_boundary = np.percentile(acceleration_coefs, alpha / 2 * 100)
    right_boundary = np.percentile(acceleration_coefs, (1 - alpha / 2) * 100)

    return left_boundary, right_boundary
