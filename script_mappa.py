import folium
import pandas as pd

# === CONFIGURAZIONI ===
input_path = r"C:\Users\f.lucignano\Desktop\Nuova cartella\officina_con_distanze.xlsx"
output_map = r"C:\Users\f.lucignano\Desktop\Nuova cartella\mappa_officine.html"

# Punto fisso (es. sede Roma)
lat_punto_fisso = 41.9028
lon_punto_fisso = 12.4964

# === LETTURA FILE ===
df = pd.read_excel(input_path)
df.columns = df.columns.str.strip().str.upper()

# === CREAZIONE MAPPA ===
m = folium.Map(location=[lat_punto_fisso, lon_punto_fisso], zoom_start=6)

# Marker per sede centrale
folium.Marker(
    location=[lat_punto_fisso, lon_punto_fisso],
    popup="Punto Fisso (Roma)",
    icon=folium.Icon(color='red', icon='home')
).add_to(m)

# Marker per ogni officina
for _, row in df.iterrows():
    lat = row['LAT']
    lon = row['LONG']
    nome = row['NOME']
    distanza = row['DISTANZA_STRADALE_KM']
    durata = row['DURATA_TRASFERIMENTO_MIN']

    popup_html = f"""
    <b>{nome}</b><br>
    Distanza: {distanza} km<br>
    Durata: {durata} min
    """
    folium.Marker(
        location=[lat, lon],
        popup=popup_html,
        icon=folium.Icon(color='blue', icon='wrench')
    ).add_to(m)

# === SALVATAGGIO ===
m.save(output_map)
print(f"✅ Mappa salvata: {output_map}")
