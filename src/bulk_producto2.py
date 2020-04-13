import pandas as pd
import glob
import re

df = []
for file in glob.glob("../output/producto2/*.csv"):
    date = re.search("\d{4}-\d{2}-\d{2}", file).group(0).replace("-", "/")
    fragment = pd.read_csv(file)
    fragment["Fecha"] = date
    df.append(fragment)

df = pd.concat(df)

# Reemplaza nombres de comuna, para coincidir con los publicados por SUBDERE
df["Comuna"] = df["Comuna"].replace({"Coyhaique": "Coihaique", "OHiggins": "O'Higgins"})

# Lee IDs de comunas desde página web oficial de SUBDERE
df_dim_comunas = pd.read_excel("http://www.subdere.gov.cl/sites/default/files/documentos/cut_2018_v03.xls", encoding="utf-8")

# Crea columna sin tildes, para hacer merge con datos publicados
df_dim_comunas["Comuna"] = df_dim_comunas["Nombre Comuna"].str.normalize("NFKD").str.encode("ascii", errors="ignore").str.decode("utf-8")

df = df.merge(df_dim_comunas, on="Comuna", how="outer")

df = df.drop(columns=["Comuna", "Region", "Codigo region", "Codigo comuna"])
df = df.rename(columns={
    "Nombre Región": "Region",
    "Nombre Provincia": "Provincia", 
    "Nombre Comuna": "Comuna",
    "Código Región": "Region ID",
    "Código Provincia": "Provincia ID",
    "Código Comuna 2017": "Comuna ID"
})

df["Casos Confirmados"] = df["Casos Confirmados"].fillna("-")

df["Tasa"] = df.apply(lambda x: (100000 * int(x["Casos Confirmados"]) / x["Poblacion"]) if x["Casos Confirmados"] != "-" else "-", axis=1) 

# Crea output de datos en CSV / JSON
df.to_csv("../output/producto6/bulk/producto2.csv", index=False)
df.to_json("../output/producto6/bulk/producto2.json", orient="records")