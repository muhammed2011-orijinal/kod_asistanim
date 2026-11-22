tl_miktari=float(input("Kumbaraya eklenen TL miktarını girin:"))

doviz_kuru=float(input("Güncel döviz kurunu giriniz:"))

doviz_karsiligi=tl_miktari/doviz_kuru

print(f"Kumbaraya eklenen{tl_miktari}TL miktarının döviz karşılığı:{doviz_karsiligi:.2f}")