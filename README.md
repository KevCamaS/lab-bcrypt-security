# 🔐 Lab: Análisis Forense de Filtración de Datos y Cracking de Hashes Bcrypt

> Laboratorio personal autodidacta de ciberseguridad ofensiva y análisis forense.
> Desarrollado paso a paso como parte de mi proceso de aprendizaje en ciberseguridad.
> ⚠️ Todos los datos utilizados son **100% sintéticos y generados por scripts propios**.

---

## 👤 Sobre este laboratorio

Este repositorio documenta mi proceso de aprendizaje personal en ciberseguridad. No es un trabajo académico ni tiene fecha límite — cada actividad se realiza cuando tengo tiempo, con el objetivo de entender profundamente cómo funcionan los ataques reales y cómo defenderse de ellos.

El laboratorio simula el análisis forense de una filtración de datos de un sistema institucional ficticio. Estudio cómo un atacante podría explotar contraseñas débiles en hashes bcrypt usando herramientas reales de pentesting, y qué medidas de seguridad hubieran prevenido el ataque.

---

## 🎯 Qué aprendo con este laboratorio

- Cómo identificar y analizar hashes bcrypt en un dataset filtrado
- Por qué bcrypt es más seguro que MD5/SHA1 pero no invulnerable
- Cómo funcionan los ataques de diccionario y fuerza bruta controlada
- Por qué las contraseñas débiles se rompen en minutos aunque estén hasheadas
- Cómo usar Hashcat y John the Ripper de forma profesional
- Cómo documentar un proceso de análisis forense correctamente
- Flujo de trabajo profesional: Kali Linux + Cursor + Git + GitHub

---

## 🛡️ Aviso legal y ético

```
Este laboratorio:
  ✅ Usa únicamente datos ficticios generados por scripts propios
  ✅ Se ejecuta en entorno aislado (VM Kali Linux)
  ✅ Tiene fines exclusivamente personales y educativos
  ✅ No involucra sistemas, personas ni credenciales reales
  ✅ Sigue los principios éticos del pentesting responsable

No está permitido:
  ❌ Usar estas técnicas contra sistemas reales sin autorización escrita
  ❌ Aplicar estos scripts sobre datos de personas reales
  ❌ Distribuir contraseñas o hashes obtenidos fuera del entorno de lab
```

---

## 🛠️ Entorno de trabajo

| Componente | Detalle |
|---|---|
| **Sistema operativo** | Kali Linux 2024 (VM) |
| **Editor de código** | Cursor (conectado a Kali via Remote SSH) |
| **Conexión remota** | Tailscale + SSH (IP fija sin importar la red) |
| **Control de versiones** | Git + GitHub |
| **Python** | 3.13.12 con entorno virtual (venv) |
| **Cracking** | Hashcat 7.1.2 + John the Ripper 1.9.0-jumbo |
| **Diccionario** | RockYou.txt (134 MB, 14M contraseñas) |

---

## 🗂️ Estructura del proyecto

```
lab-bcrypt-security/
│
├── README.md                      ← descripción general del lab
├── .gitignore                     ← archivos excluidos de GitHub
│
├── datos/
│   ├── generar_dataset.py         ← genera el dataset sintético
│   ├── dataset_filtrado.json      ← dataset ficticio completo
│   └── hashes.txt                 ← hashes bcrypt para atacar
│
├── analisis/
│   ├── analisis_forense.py        ← análisis técnico + gráficos
│   ├── verificar_resultados.py    ← validación criptográfica
│   └── reporte_final.py           ← métricas e impacto
│
├── resultados/
│   ├── analisis_forense.png       ← gráficos comparativos
│   ├── reporte_final.png          ← gráfico de impacto
│   └── resultados_crack.txt       ← contraseñas encontradas
│
├── capturas/
│   ├── 00a_versiones.png
│   ├── 00b_pip_install.png
│   ├── 00c_rockyou.png
│   ├── 01_generacion_dataset.png
│   ├── 02_analisis_forense.png
│   ├── 03_john_running.png
│   ├── 04_hashcat_status.png
│   ├── 05_resultados.png
│   └── 06_reporte_final.png
│
└── docs/
    ├── fase_00_entorno.md         ← preparación del entorno ✅
    ├── fase_01_dataset.md         ← generación de datos (pendiente)
    ├── fase_02_analisis.md        ← análisis forense (pendiente)
    ├── fase_03_john.md            ← cracking con John (pendiente)
    ├── fase_04_hashcat.md         ← cracking con Hashcat (pendiente)
    ├── fase_05_verificacion.md    ← verificación (pendiente)
    └── fase_06_reporte.md         ← reporte final (pendiente)
```

---

## 📅 Progreso del laboratorio

| Fase | Descripción | Estado |
|---|---|---|
| Fase 0 | Preparación del entorno | ✅ Completada |
| Fase 1 | Generación del dataset sintético | 🔄 Pendiente |
| Fase 2 | Análisis forense con Python | 🔄 Pendiente |
| Fase 3 | Cracking con John the Ripper | 🔄 Pendiente |
| Fase 4 | Cracking con Hashcat | 🔄 Pendiente |
| Fase 5 | Verificación de resultados | 🔄 Pendiente |
| Fase 6 | Reporte final | 🔄 Pendiente |

---

## ⚙️ Cómo reproducir este laboratorio

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/lab-bcrypt-security.git
cd lab-bcrypt-security

# 2. Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install bcrypt pandas matplotlib

# 4. Descomprimir RockYou (Kali Linux)
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# 5. Seguir las fases en orden desde docs/
```

---

## 🔗 Documentación por fases

Cada fase tiene su propio documento detallado en la carpeta `docs/` con:
- Qué se hizo exactamente
- Comandos ejecutados y sus salidas
- Capturas de pantalla
- Problemas encontrados y cómo se resolvieron
- Aprendizajes obtenidos

---

*Laboratorio en progreso — actualizado continuamente*
