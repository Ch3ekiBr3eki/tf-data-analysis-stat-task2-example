import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    loc = x.mean()
    scale = np.sqrt(np.var(x))
    
    alpha = 1 - p
    z = norm.ppf(1 - alpha / 2)
    left = loc - z * scale / np.sqrt(len(x))
    right = loc + z * scale / np.sqrt(len(x))
    
    return (left, right)
