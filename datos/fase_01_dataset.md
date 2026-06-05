# 📁 Fase 1 — Generación del Dataset Sintético

> Documentación del proceso de creación del dataset ficticio que simula una filtración de datos de un sistema institucional de registro de visitas.

**Fecha de realización:** Junio 2026
**Estado:** ✅ Completada

---

## 🎯 Objetivo de esta fase

Crear un dataset 100% sintético que replique la estructura real de una filtración de datos de una API municipal, incluyendo nombres, DNIs, emails, cargos y — lo más importante — **hashes bcrypt de contraseñas reales**. Este dataset será el input para todas las fases siguientes de análisis y cracking.

---

## 📂 Archivos creados

| Archivo | Ubicación | Descripción |
|---|---|---|
| `generar_dataset.py` | `datos/` | Script generador del dataset |
| `dataset_filtrado.json` | `datos/` | 10 registros ficticios completos |
| `hashes.txt` | `datos/` | 10 hashes bcrypt listos para atacar |
| `respuestas_reales.txt` | raíz | Referencia local — NO subido a GitHub |

---

## 🔑 Diseño de contraseñas del dataset

El dataset incluye contraseñas de tres niveles de seguridad deliberadamente, para demostrar el impacto real de cada tipo:

| Nivel | Contraseñas incluidas | Resultado esperado |
|---|---|---|
| MUY_DEBIL | `123456`, `password`, `admin123`, `qwerty`, `12345678`, `municipio1`, `peru2024`, `letmein` | Se rompen en segundos con RockYou |
| MEDIA | `Municipio#24`, `Secretaria!2024` | Pueden romperse con reglas |
| FUERTE | `xK9$mP2@vL7#nQ3`, `G!7hR#2kXp@9mN3z` | Prácticamente invulnerables |

---

## ⚙️ Cómo funciona el script

El script `generar_dataset.py` hace lo siguiente en orden:

**1. Define el pool de contraseñas** con sus niveles de seguridad.

**2. Define 10 personas ficticias** con nombre, DNI y cargo inventados.

**3. Para cada persona:**
- Elige una contraseña aleatoria del pool
- Genera un hash bcrypt real con `cost factor = 10`
- Construye un email ficticio a partir del nombre
- Genera fechas de visita aleatorias dentro de un rango

**4. Guarda tres archivos:**
- `dataset_filtrado.json` — todos los campos (simula la filtración completa)
- `hashes.txt` — solo los hashes (input para Hashcat y John)
- `respuestas_reales.txt` — referencia local para verificar resultados

---

## ▶️ Ejecución

```bash
cd ~/Desktop/lab-bcrypt-security
source venv/bin/activate
python3 datos/generar_dataset.py
```

---

## 📊 Resultado obtenido

```
=================================================================
  GENERADOR DE DATASET SINTÉTICO - LABORATORIO PERSONAL
=================================================================
  Generando 10 registros con hashes bcrypt...
  Puede tardar ~30 segundos (bcrypt es lento por diseño)

  [█░░░░░░░░░] LOPEZ GARCIA JUAN CARLOS     | MUY_DEBIL  | $2b$10$6Qcmr.XwVYkhAgSrQb...
  [██░░░░░░░░] RAMIREZ TORRES MARIA ELENA   | MUY_DEBIL  | $2b$10$RbVn8C32KDUohG4JP3...
  [███░░░░░░░] QUISPE MAMANI PEDRO PABLO    | FUERTE     | $2b$10$hB0W1RaOLc4Wvuqx21...
  [████░░░░░░] FLORES HUANCA ROSA AMELIA    | MUY_DEBIL  | $2b$10$Z4z5MsJn70P6Ao9gaP...
  [█████░░░░░] CONDORI APAZA FELIX HUGO     | MUY_DEBIL  | $2b$10$gpWdtPWA5J2EAqJ7Nk...
  [██████░░░░] VARGAS CANO LUCIA ESPERANZA  | MUY_DEBIL  | $2b$10$I9rcG0O5KH/SIVL6mS...
  [███████░░░] MENDOZA RIOS EDGAR IVAN      | MEDIA      | $2b$10$cPIC8RrW5wf5kNTHsT...
  [████████░░] HUANCA TICONA ELSA MILAGROS  | MUY_DEBIL  | $2b$10$Woi6pQhCimSN3ydlLo...
  [█████████░] CCOPA MAMANI ROBERTO DANTE   | FUERTE     | $2b$10$KryuLtyuV.96.H0CDw...
  [██████████] PINTO SALAS CARMEN ROSA      | MEDIA      | $2b$10$8plI3wzy880tLnZ0Rl...

=================================================================
  ✅ datos/dataset_filtrado.json  → 10 registros
  ✅ datos/hashes.txt             → 10 hashes bcrypt
  ✅ respuestas_reales.txt        → referencia local (NO subir)
=================================================================

  Ejemplo de hash generado:
  $2b$10$6Qcmr.XwVYkhAgSrQbTOL.ML0FdlG8uj.N5CLirVq5mahCq53C5ia

  $2b  = versión bcrypt
  $10  = cost factor (2^10 = 1.024 iteraciones por intento)
  [22 chars salt] + [31 chars hash]
```

---

## 📊 Distribución de niveles generados

| Nivel | Cantidad | % del total |
|---|---|---|
| MUY_DEBIL | 6 | 60% |
| MEDIA | 2 | 20% |
| FUERTE | 2 | 20% |

---

## 🔬 Anatomía de un hash bcrypt generado

```
$2b$10$6Qcmr.XwVYkhAgSrQbTOL.ML0FdlG8uj.N5CLirVq5mahCq53C5ia
│  │  │◄──── 22 chars ────►│◄────────── 31 chars ──────────►│
│  │  └─ Salt aleatorio único por cada hash
│  └─ Cost factor: 2^10 = 1.024 iteraciones
└─ Versión bcrypt ($2b = versión actual)
```

**¿Por qué cada hash es diferente aunque la contraseña sea la misma?**
Porque bcrypt genera un salt aleatorio nuevo cada vez. Dos personas con la misma contraseña tendrán hashes completamente distintos. Esto impide los ataques de tabla arcoíris (rainbow tables).

---

## 💡 Aprendizajes de esta fase

- `bcrypt.gensalt(rounds=10)` genera un salt único aleatorio en cada llamada
- `bcrypt.hashpw()` combina la contraseña + salt y aplica 2^10 iteraciones
- El cost factor 10 hace que cada hash tarde ~100ms en generarse — por eso los 10 registros tardaron ~30 segundos
- El archivo `respuestas_reales.txt` está en `.gitignore` y nunca se subirá a GitHub — en una filtración real el atacante no tendría este archivo, lo que hace que el cracking sea el único camino

---

## 📸 Capturas de esta fase

| Captura | Descripción |
|---|---|
| `capturas/01_generacion_dataset.png` | Terminal mostrando la barra de progreso y los hashes generados |

---

## ➡️ Siguiente fase

**[Fase 2 — Análisis forense con Python](fase_02_analisis.md)**
