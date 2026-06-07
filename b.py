import statsmodels.api as sm
from statsmodels.formula.api import ols
from data import df

# 2. Modelin Kurulması (B Şıkkı - Etkileşimli Model)
# '*' işareti hem ana etkileri hem de 'Arac_Sinifi * Zemin_Durumu' etkileşimini modele otomatik ekler.
model_b = ols('Tur_Suresi ~ C(Arac_Sinifi) * C(Zemin_Durumu)', data=df).fit()

# 3. F Testi (ANOVA Tablosu) Çıktısının Alınması
anova_b = sm.stats.anova_lm(model_b, typ=2)

print("--- B ŞIKKI: ETKİLEŞİMLİ MODEL ANOVA TABLOSU ---")
print(anova_b)