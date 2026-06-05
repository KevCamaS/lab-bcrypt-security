#!/usr/bin/env python3
"""
Análisis forense del dataset sintético.
Identifica estructura de hashes, calcula velocidades y genera gráficos.
"""

import json
import matplotlib.pyplot as plt
from collections import Counter

print("\n" + "="*65)
print("  ANÁLISIS FORENSE DE FILTRACIÓN DE DATOS")
print("  Laboratorio Personal — Datos 100% Sintéticos")
print("="*65)

# ─── Cargar datos ─────────────────────────────────────────────
with open("datos/dataset_filtrado.json", "r", encoding="utf-8") as f:
    data = json.load(f)
registros = data["data"]

# ─── 1. Inventario de campos expuestos ────────────────────────
print("\n[1] CAMPOS EXPUESTOS EN LA FILTRACIÓN")
print("-"*50)
campos = ["nombre", "dni", "email", "cargo", "password_hash",
          "entidad", "check_in", "check_out"]
for campo in campos:
    n = sum(1 for r in registros if r.get(campo))
    pct = n / len(registros) * 100
    barra = "█" * int(pct // 10)
    print(f"  {campo:<20} {barra:<10} {n}/{len(registros)} ({pct:.0f}%)")

# ─── 2. Análisis técnico de hashes bcrypt ─────────────────────
print("\n[2] ANÁLISIS TÉCNICO DE HASHES BCRYPT")
print("-"*50)
versiones    = []
cost_factors = []

for r in registros:
    partes = r["password_hash"].split("$")
    if len(partes) >= 3:
        versiones.append(partes[1])
        cost_factors.append(int(partes[2]))

cf_counter = Counter(cost_factors)
print(f"  Versión detectada    : ${Counter(versiones).most_common(1)[0][0]}")
print(f"  Cost factors         : {dict(cf_counter)}")
print(f"  Longitud de hash     : {len(registros[0]['password_hash'])} caracteres")
print(f"\n  Ejemplo de hash:")
h = registros[0]["password_hash"]
print(f"  {h}")
print(f"  $2b → versión  |  $10 → cost  |  [22] salt  |  [31] hash")

# ─── 3. Niveles de seguridad ──────────────────────────────────
print("\n[3] DISTRIBUCIÓN DE NIVELES DE SEGURIDAD")
print("-"*50)
niveles = Counter(r["_nivel_seguridad"] for r in registros)
for nivel, count in sorted(niveles.items()):
    barra = "█" * (count * 4)
    print(f"  {nivel:<12} {barra} ({count} usuarios)")

# ─── 4. Velocidades de cracking ───────────────────────────────
print("\n[4] VELOCIDADES ESTIMADAS DE CRACKING (bcrypt $2b$10)")
print("-"*50)
hardware = [
    ("CPU moderno (sin GPU)",  50),
    ("GPU GTX 1060",           3_000),
    ("GPU RTX 3080",           15_000),
    ("GPU RTX 4090",           35_000),
]
md5_speed = 10_000_000_000
print(f"  {'Hardware':<28} {'H/s bcrypt':>12}  {'vs MD5':>15}")
print(f"  {'-'*58}")
for hw, vel in hardware:
    factor = md5_speed // vel
    print(f"  {hw:<28} {vel:>12,}  {factor:>10,}x más lento")

# ─── 5. Tiempo estimado por tipo de ataque ────────────────────
print("\n[5] TIEMPO ESTIMADO (GPU GTX 1060 → ~3.000 H/s)")
print("-"*50)
vel = 3_000
ataques = [
    ("Dígitos 4 caracteres",       10**4),
    ("Dígitos 6 caracteres",       10**6),
    ("RockYou (14M palabras)",     14_000_000),
    ("Minúsculas 6 caracteres",    26**6),
    ("Alfanuméricas 8 caracteres", 62**8),
    ("Todas ASCII 12 caracteres",  95**12),
]
for desc, espacio in ataques:
    segs = espacio / vel
    if   segs < 60:        t = f"{segs:.1f} segundos"
    elif segs < 3600:      t = f"{segs/60:.1f} minutos"
    elif segs < 86400:     t = f"{segs/3600:.1f} horas"
    elif segs < 86400*365: t = f"{segs/86400:.0f} días"
    else:                  t = f"{segs/86400/365:,.0f} años"
    print(f"  {desc:<35} → {t}")

# ─── 6. Gráficos ──────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("Análisis Forense — Laboratorio Personal (Datos Sintéticos)",
             fontsize=13, fontweight="bold")

# Gráfico 1: Niveles de seguridad
colores_n = {"MUY_DEBIL": "#E24B4A", "MEDIA": "#EF9F27", "FUERTE": "#1D9E75"}
niv_labels = list(niveles.keys())
niv_vals   = list(niveles.values())
axes[0].bar(niv_labels, niv_vals,
            color=[colores_n.get(k, "#888") for k in niv_labels],
            edgecolor="white", linewidth=0.8)
axes[0].set_title("Distribución de fortaleza de contraseñas")
axes[0].set_ylabel("Cantidad de usuarios")
axes[0].set_facecolor("#f9f9f9")
for i, v in enumerate(niv_vals):
    axes[0].text(i, v + 0.05, str(v), ha="center", fontweight="bold")

# Gráfico 2: Velocidad por algoritmo
algos  = ["MD5", "SHA-1", "SHA-256", "bcrypt\ncost=10"]
vels   = [10_000_000_000, 6_000_000_000, 3_000_000_000, 15_000]
cols_v = ["#E24B4A", "#E24B4A", "#EF9F27", "#1D9E75"]
bars   = axes[1].bar(algos, vels, color=cols_v, edgecolor="white")
axes[1].set_title("Velocidad de cracking por algoritmo\n(GPU RTX 3080 — mayor = más vulnerable)")
axes[1].set_ylabel("Hashes por segundo")
axes[1].set_yscale("log")
axes[1].set_facecolor("#f9f9f9")
for bar, v in zip(bars, vels):
    axes[1].text(bar.get_x() + bar.get_width()/2,
                 bar.get_height() * 2,
                 f"{v:,.0f}", ha="center", fontsize=8)

plt.tight_layout()
plt.savefig("resultados/analisis_forense.png", dpi=150, bbox_inches="tight")
print("\n  ✅ Gráfico guardado: resultados/analisis_forense.png")
plt.show()
print()