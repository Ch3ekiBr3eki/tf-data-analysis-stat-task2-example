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
    sample_mean = np.mean(x)
    sample_std = np.std(x, ddof=1)

    alpha = 1 - p
    dof = len(x) - 1
    critical_value = norm.ppf(1 - alpha / 2)
    margin_of_error = critical_value * sample_std / np.sqrt(len(x))

    left_boundary = sample_mean - margin_of_error
    right_boundary = sample_mean + margin_of_error

    return left_boundary, right_boundary 
