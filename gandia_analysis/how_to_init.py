import os
import requests
import zipfile

# Create data folder
os.makedirs("gandia_data/INE", exist_ok=True)
os.makedirs("gandia_data/Catastro", exist_ok=True)
os.makedirs("gandia_data/Municipal", exist_ok=True)

# ---------- INE ----------
ine_urls = {
    "padron_municipios": "https://www.ine.es/jaxiT3/files/t/csv_bd/37810.csv",
}
for name, url in ine_urls.items():
    r = requests.get(url)
    with open(f"gandia_data/INE/{name}.csv", "wb") as f:
        f.write(r.content)

# ---------- CATASTRO ----------
# Download the provincial shapefile package (Valencia)
catastro_url = "https://www.catastro.hacienda.gob.es/INSPIRE/Buildings/46/ES.SDGC.BU.46220.GANDIA.zip"
r = requests.get(catastro_url)
if r.status_code == 200:
    with open("gandia_data/Catastro/catastro_gandia.zip", "wb") as f:
        f.write(r.content)
else:
    print("Catastro file not directly accessible; check sedecatastro.gob.es manually.")

# ---------- MUNICIPAL ----------
# Example municipal open-data CSVs (replace/add more if needed)
municipal_urls = {
    "presupuestos": "https://datos.gob.es/sites/default/files/dataset/presupuestos_gandia.csv",
    "infraestructuras": "https://datos.gob.es/sites/default/files/dataset/infraestructuras_gandia.csv",
}
for name, url in municipal_urls.items():
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            with open(f"gandia_data/Municipal/{name}.csv", "wb") as f:
                f.write(r.content)
    except Exception as e:
        print(f"Could not download {name}: {e}")

# ---------- ZIP EVERYTHING ----------
with zipfile.ZipFile("gandia_data.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk("gandia_data"):
        for file in files:
            path = os.path.join(root, file)
            zipf.write(path, arcname=os.path.relpath(path, "gandia_data"))

print("All done! → gandia_data.zip")
