import statsmodels.api as sm
from statsmodels.formula.api import ols
from data import df

# 2. Modelin Kurulması (A Şıkkı - Ana Etki Modeli)
# C() fonksiyonu değişkenlerin kategorik (nitel) olduğunu belirtir ve arkada kukla değişkenleri kendi atar.
# '+' işareti etkileşim OLMADIĞINI, sadece ana etkilerin test edildiğini gösterir.
model_a = ols('Tur_Suresi ~ C(Arac_Sinifi) + C(Zemin_Durumu)', data=df).fit()

# 3. F Testi (ANOVA Tablosu) Çıktısının Alınması
anova_a = sm.stats.anova_lm(model_a, typ=2)

print("--- A ŞIKKI: ETKİLEŞİMSİZ MODEL ANOVA TABLOSU ---")
print(anova_a)