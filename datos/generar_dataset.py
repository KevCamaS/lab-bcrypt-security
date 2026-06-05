#!/usr/bin/env python3
"""
Generador de dataset sintético para laboratorio personal.
Todos los datos son ficticios. No usar con datos reales.
"""

import bcrypt
import json
import uuid
import random
from datetime import datetime, timedelta

passwords_pool = [
    ("123456",           "MUY_DEBIL"),
    ("password",         "MUY_DEBIL"),
    ("admin123",         "MUY_DEBIL"),
    ("qwerty",           "MUY_DEBIL"),
    ("12345678",         "MUY_DEBIL"),
    ("municipio1",       "MUY_DEBIL"),
    ("peru2024",         "MUY_DEBIL"),
    ("letmein",          "MUY_DEBIL"),
    ("Municipio#24",     "MEDIA"),
    ("Secretaria!2024",  "MEDIA"),
    ("xK9$mP2@vL7#nQ3",  "FUERTE"),
    ("G!7hR#2kXp@9mN3z", "FUERTE"),
]

personas = [
    {"nombre": "LOPEZ GARCIA JUAN CARLOS",    "dni": "12345001", "cargo": "Secretaria"},
    {"nombre": "RAMIREZ TORRES MARIA ELENA",  "dni": "12345002", "cargo": "Secretaria"},
    {"nombre": "QUISPE MAMANI PEDRO PABLO",   "dni": "12345003", "cargo": "Alcalde"},
    {"nombre": "FLORES HUANCA ROSA AMELIA",   "dni": "12345004", "cargo": "Regidor"},
    {"nombre": "CONDORI APAZA FELIX HUGO",    "dni": "12345005", "cargo": "Secretaria"},
    {"nombre": "VARGAS CANO LUCIA ESPERANZA", "dni": "12345006", "cargo": "Secretaria"},
    {"nombre": "MENDOZA RIOS EDGAR IVAN",     "dni": "12345007", "cargo": "Funcionario"},
    {"nombre": "HUANCA TICONA ELSA MILAGROS", "dni": "12345008", "cargo": "Secretaria"},
    {"nombre": "CCOPA MAMANI ROBERTO DANTE",  "dni": "12345009", "cargo": "Funcionario"},
    {"nombre": "PINTO SALAS CARMEN ROSA",     "dni": "12345010", "cargo": "Secretaria"},
]

entidades_ficticias = [
    "PRESIDENTE DE UPIS DEMO",
    "MERCADO CENTRAL FICTICIO",
    "ASOCIACION VECINAL DEMO",
    "VASO DE LECHE DEMO",
    "FENAMAD DEMO",
    "CORREDOR DEMO",
]

print("\n" + "="*65)
print("  GENERADOR DE DATASET SINTÉTICO - LABORATORIO PERSONAL")
print("="*65)
print(f"\n  Generando {len(personas)} registros con hashes bcrypt...")
print(f"  Puede tardar ~30 segundos (bcrypt es lento por diseño)\n")

usuarios  = []
hashes    = []
base_date = datetime(2025, 8, 11, 14, 0, 0)

for i, persona in enumerate(personas):
    pwd_texto, nivel = random.choice(passwords_pool)

    password_hash = bcrypt.hashpw(
        pwd_texto.encode("utf-8"),
        bcrypt.gensalt(rounds=10)
    ).decode("utf-8")

    partes    = persona["nombre"].lower().split()
    email     = f"{partes[0]}.{partes[1]}@municipio-demo.gob.pe"
    fecha_in  = base_date + timedelta(days=random.randint(0, 90))
    fecha_out = fecha_in + timedelta(hours=random.randint(1, 3))

    registro = {
        "id":               str(uuid.uuid4()),
        "nombre":           persona["nombre"],
        "dni":              persona["dni"],
        "email":            email,
        "cargo":            persona["cargo"],
        "lugar":            "Despacho de Alcaldía",
        "entidad":          random.choice(entidades_ficticias),
        "motivo":           "Reunión de Trabajo",
        "check_in":         fecha_in.isoformat(),
        "check_out":        fecha_out.isoformat(),
        "password_hash":    password_hash,
        "_nivel_seguridad": nivel,
        "_password_real":   pwd_texto,
    }

    usuarios.append(registro)
    hashes.append(password_hash)

    barra = "█" * (i + 1) + "░" * (len(personas) - i - 1)
    print(f"  [{barra}] {persona['nombre'][:28]:<28} | {nivel:<10} | {password_hash[:25]}...")

with open("datos/dataset_filtrado.json", "w", encoding="utf-8") as f:
    json.dump({"success": True, "total": len(usuarios), "data": usuarios},
              f, ensure_ascii=False, indent=2)

with open("datos/hashes.txt", "w") as f:
    f.write("\n".join(hashes) + "\n")

with open("respuestas_reales.txt", "w", encoding="utf-8") as f:
    f.write("# SOLO PARA VERIFICACIÓN LOCAL - NO SUBIR A GITHUB\n\n")
    for u in usuarios:
        f.write(f"{u['nombre']:<35} | {u['_password_real']:<20} | {u['_nivel_seguridad']}\n")

print("\n" + "="*65)
print(f"  ✅ datos/dataset_filtrado.json  → {len(usuarios)} registros")
print(f"  ✅ datos/hashes.txt             → {len(hashes)} hashes bcrypt")
print(f"  ✅ respuestas_reales.txt        → referencia local (NO subir)")
print("="*65)
print(f"\n  Ejemplo de hash generado:")
print(f"  {hashes[0]}")
print(f"\n  $2b  = versión bcrypt")
print(f"  $10  = cost factor (2^10 = 1.024 iteraciones por intento)")
print(f"  [22 chars salt] + [31 chars hash]\n")