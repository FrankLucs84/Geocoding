# dal file excel ad una rappresentazione html -> (non solo in locale sul pc, ma anche online)
✅ SCRIPT folium PER MAPPA INTERATTIVA – COMPATIBILE CON IL TUO FILE
Questo script legge il tuo file e crea una mappa interattiva HTML con:

🧭 Un marker rosso per il punto fisso (es. Roma)

🔵 Marker blu per ogni officina

📋 Popup con: nome + distanza + durata

💾 Salvataggio mappa in .html

🔧 Codice completo:
python
Copia
Modifica
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
📦 Installazione (se non l’hai già fatto)
bash
Copia
Modifica
pip install folium
🗺️ Output: mappa_officine.html
Puoi aprirla in qualsiasi browser

Include tutti i marker

Puoi zoomare, spostarti e cliccare ogni punto

➕ Estensioni possibili
Vuoi che disegni anche le linee del percorso dalla sede a ogni officina (con tracciato stradale)?
Posso integrarlo con le polylines dell’API ORS.


---
✅ METODO 1 – Netlify Drop (consigliato ⚡)
✅ Punti di forza:
Gratuito, immediato, senza login

Nessuna configurazione

Ottimo per file singoli HTML

🔧 Come fare:
Vai su 👉 https://app.netlify.com/drop

Trascina il file mappa_officine.html nella finestra

Attendi pochi secondi ⏳

Ti verrà fornito un link pubblico, es.:

arduino
Copia
Modifica
https://charming-sunflower-42d1a2.netlify.app
✅ Apribile da chiunque, su qualunque dispositivo.

---


