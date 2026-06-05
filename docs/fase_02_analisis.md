# 🔍 Fase 2 — Análisis Forense con Python

> Documentación del análisis técnico del dataset sintético: identificación de campos expuestos, estructura de hashes bcrypt, velocidades de cracking y visualizaciones comparativas.

**Fecha de realización:** Junio 2026
**Estado:** ✅ Completada

---

## 🎯 Objetivo de esta fase

Analizar técnicamente el dataset filtrado para:
- Identificar qué campos quedaron expuestos y en qué porcentaje
- Diseccionar la estructura interna de los hashes bcrypt
- Calcular velocidades reales de cracking según el hardware
- Estimar el tiempo que tomaría romper cada tipo de contraseña
- Generar gráficos visuales que demuestren el impacto

---

## 📂 Archivos creados

| Archivo | Ubicación | Descripción |
|---|---|---|
| `analisis_forense.py` | `analisis/` | Script de análisis completo |
| `analisis_forense.png` | `resultados/` | Gráficos comparativos generados |

---

## ▶️ Ejecución

```bash
cd ~/Desktop/lab-bcrypt-security
source venv/bin/activate
python3 analisis/analisis_forense.py
```

---

## 📊 Resultados obtenidos

### [1] Campos expuestos en la filtración

```
nombre               ██████████  10/10 (100%)
dni                  ██████████  10/10 (100%)
email                ██████████  10/10 (100%)
cargo                ██████████  10/10 (100%)
password_hash        ██████████  10/10 (100%)
entidad              ██████████  10/10 (100%)
check_in             ██████████  10/10 (100%)
check_out            ██████████  10/10 (100%)
```

**Conclusión:** El 100% de los campos sensibles quedó expuesto en la filtración. Ningún campo fue filtrado o protegido por la API.

---

### [2] Análisis técnico de hashes bcrypt

```
Versión detectada    : $2b
Cost factors         : {10: 10}
Longitud de hash     : 60 caracteres

Ejemplo de hash:
$2b$10$6Qcmr.XwVYkhAgSrQbTOL.ML0FdlG8uj.N5CLirVq5mahCq53C5ia
$2b → versión  |  $10 → cost  |  [22] salt  |  [31] hash
```

**Hallazgos:**
- Todos los hashes usan versión `$2b` — la versión actual y correcta de bcrypt
- Todos usan cost factor `10` — 2^10 = 1.024 iteraciones por intento
- La longitud fija de 60 caracteres es característica de bcrypt

---

### [3] Distribución de niveles de seguridad

```
FUERTE       ████████  (2 usuarios)
MEDIA        ████████  (2 usuarios)
MUY_DEBIL    ████████████████████████  (6 usuarios)
```

**Conclusión:** El 60% de los usuarios tiene contraseñas débiles que serán vulnerables al ataque de diccionario.

---

### [4] Velocidades estimadas de cracking

```
Hardware                      H/s bcrypt          vs MD5
──────────────────────────────────────────────────────────
CPU moderno (sin GPU)                 50   200,000,000x más lento
GPU GTX 1060                      3,000     3,333,333x más lento
GPU RTX 3080                     15,000       666,666x más lento
GPU RTX 4090                     35,000       285,714x más lento
```

**Conclusión clave:** Incluso la GPU más potente del mercado es **285,714 veces más lenta** crackeando bcrypt que MD5. Este es el poder del cost factor.

---

### [5] Tiempo estimado de cracking (GPU GTX 1060 → 3.000 H/s)

```
Dígitos 4 caracteres          →  3.3 segundos     ← trivial
Dígitos 6 caracteres          →  5.6 minutos      ← muy rápido
RockYou (14M palabras)        →  1.3 horas        ← viable
Minúsculas 6 caracteres       →  1 días           ← posible
Alfanuméricas 8 caracteres    →  2,308 años       ← inviable
Todas ASCII 12 caracteres     →  5,711,568,658,704 años ← imposible
```

**Conclusión:** Las contraseñas que están en el diccionario RockYou se rompen en aproximadamente 1 hora. Las contraseñas cortas de solo dígitos, en segundos. Las contraseñas largas y mixtas son prácticamente invulnerables.

---

## 📈 Gráficos generados

### Gráfico 1: Distribución de fortaleza de contraseñas
Muestra visualmente que el 60% del dataset tiene contraseñas MUY_DEBIL (rojo), el 20% MEDIA (amarillo) y el 20% FUERTE (verde).

### Gráfico 2: Velocidad de cracking por algoritmo
Escala logarítmica que demuestra la diferencia abismal entre MD5 (10 billones H/s) y bcrypt cost=10 (15,000 H/s). La diferencia visual es impactante porque la escala es logarítmica.

📸 Captura guardada en: `resultados/analisis_forense.png`

---

## 💡 Aprendizajes de esta fase

- **bcrypt no es invulnerable** — las contraseñas débiles siguen siendo el eslabón más débil
- **El cost factor es fundamental** — aumentar de 10 a 12 hace el cracking 4x más lento sin impacto perceptible para el usuario
- **RockYou como referencia** — si una contraseña existe en ese diccionario, será crackeada independientemente del algoritmo de hash
- **La escala logarítmica** en el gráfico de velocidades es necesaria porque la diferencia entre MD5 y bcrypt es de 6 órdenes de magnitud
- **Exponer `password_hash` en una API** convierte un sistema con bcrypt (seguro) en uno vulnerable, porque permite el ataque offline sin límite de intentos

---

## 📸 Capturas de esta fase

| Captura | Descripción |
|---|---|
| `capturas/02_analisis_terminal.png` | Salida completa en terminal |
| `resultados/analisis_forense.png` | Gráficos generados por matplotlib |

---

## ➡️ Siguiente fase

**[Fase 3 — Cracking con John the Ripper](fase_03_john.md)**
