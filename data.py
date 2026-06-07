import pandas as pd

data = {
    'Arac_Sinifi': ['Hobi']*10 + ['Pro']*10 + ['Canavar']*10,
    'Zemin_Durumu': (['Kuru']*5 + ['Islak']*5) * 3,
    'Tur_Suresi': [
        61, 63, 60, 62, 64, 67, 69, 66, 68, 70,  # Hobi
        53, 55, 52, 54, 56, 60, 62, 59, 61, 63,  # Pro
        46, 48, 45, 47, 49, 75, 78, 74, 77, 76   # Canavar
    ]
}

df = pd.DataFrame(data)
