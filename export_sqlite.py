import sqlite3
import json
import sys

conn = sqlite3.connect('db.sqlite3')
conn.row_factory = sqlite3.Row

cur = conn.cursor()

data = []

# Export web_trabajo
cur.execute("SELECT * FROM web_trabajo")
for row in cur.fetchall():
    data.append({
        "model": "web.trabajo",
        "pk": row["id"],
        "fields": {
            "titulo": row["titulo"],
            "descripcion": row["descripcion"],
            "fecha_creacion": row["fecha_creacion"],
            "imagen": row["imagen"] if row["imagen"] else ""
        }
    })

# Export web_mensajecontacto
cur.execute("SELECT * FROM web_mensajecontacto")
for row in cur.fetchall():
    data.append({
        "model": "web.mensajecontacto",
        "pk": row["id"],
        "fields": {
            "nombre": row["nombre"],
            "email": row["email"],
            "telefono": row["telefono"] if row["telefono"] else "",
            "mensaje": row["mensaje"],
            "fecha_envio": row["fecha_envio"]
        }
    })

conn.close()

with open('shodo_backup_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Exportados: {len([d for d in data if d['model']=='web.trabajo'])} trabajos, {len([d for d in data if d['model']=='web.mensajecontacto'])} mensajes")
