# ⚙️ Fase 0 — Preparación del Entorno

> Documentación de todo lo que realicé para preparar el entorno de trabajo antes de comenzar con las actividades prácticas del laboratorio.

**Fecha de realización:** Junio 2026
**Estado:** ✅ Completada

---

## 🖥️ Entorno utilizado

| Componente | Detalle |
|---|---|
| Sistema anfitrión | Windows (PC principal) |
| Máquina virtual | Kali Linux 2024 (VM) |
| Editor de código | Cursor |
| Conexión remota | Tailscale + SSH |

---

## Paso 1 — Verificar herramientas preinstaladas en Kali

```bash
python3 --version
hashcat --version
john
```

**Resultados:**

```
Python 3.13.12
v7.1.2
John the Ripper 1.9.0-jumbo-1+bleeding-aec1328d6c 2021-11-02
[linux-gnu 64-bit x86_64 AVX2 AC]
```

✅ Python, Hashcat y John the Ripper disponibles sin instalarlos.

> **Nota:** `john --version` no funciona — hay que ejecutar solo `john` para ver la versión.

📸 Captura: `capturas/00a_versiones.png`

---

## Paso 2 — Crear la carpeta del proyecto en Kali

```bash
cd ~/Desktop
mkdir lab-bcrypt-security
cd lab-bcrypt-security
```

Ruta del proyecto: `/home/thony/Desktop/lab-bcrypt-security`

---

## Paso 3 — Crear el entorno virtual Python (venv)

Kali Linux 2024 bloquea la instalación directa de paquetes Python con el error `externally-managed-environment`. La solución es un entorno virtual aislado.

```bash
python3 -m venv venv
source venv/bin/activate
```

Cuando está activo el prompt muestra:

```
(venv)(thony@kali)-[~/Desktop/lab-bcrypt-security]$
```

> ⚠️ Cada vez que abra una nueva terminal debo ejecutar `source venv/bin/activate` antes de correr cualquier script Python.

---

## Paso 4 — Instalar librerías Python

```bash
pip install bcrypt pandas matplotlib
```

Versiones instaladas:

```
bcrypt 5.0.0
pandas 3.0.3
matplotlib 3.10.9
numpy 2.4.6
```

**Verificación:**

```bash
python3 -c "import bcrypt, pandas, matplotlib; print('✅ Todo listo')"
```

```
✅ Todo listo
```

📸 Captura: `capturas/00b_pip_install.png`

---

## Paso 5 — Verificar y descomprimir RockYou.txt

RockYou.txt es el diccionario estándar de pentesting con 14.3 millones de contraseñas reales. Viene en Kali pero comprimido.

```bash
ls -lh /usr/share/wordlists/
# Aparece: rockyou.txt.gz (51 MB)

sudo gunzip /usr/share/wordlists/rockyou.txt.gz

ls -lh /usr/share/wordlists/rockyou.txt
# -rw-r--r-- 1 root root 134M Feb 3 02:57
```

✅ RockYou descomprimido — **134 MB** listos para usar.

📸 Captura: `capturas/00c_rockyou.png`

---

## Paso 6 — Configurar flujo profesional: Cursor + Kali via SSH

Decidí trabajar de forma profesional conectando Cursor directamente a Kali via SSH, para editar archivos en Kali desde Windows con toda la comodidad del editor.

### 6.1 — Instalar Tailscale en Kali

Tailscale asigna una IP fija que no cambia sin importar en qué red esté. Clave porque me muevo entre redes distintas constantemente.

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
tailscale ip -4
# 100.83.186.5  ← IP fija permanente de Kali
```

### 6.2 — Habilitar SSH en Kali

```bash
sudo apt install openssh-server -y
sudo systemctl enable ssh
sudo systemctl start ssh
sudo systemctl status ssh
# Active: active (running)
```

### 6.3 — Generar llave SSH en Windows

Para evitar problemas con contraseñas con caracteres especiales (`#`, `$`), usé autenticación por llave SSH — más segura y sin problemas de codificación.

Desde PowerShell en Windows:

```powershell
ssh-keygen -t ed25519 -C "cursor-kali-lab"
# Llave guardada en: C:\Users\KEVIN007\.ssh\id_ed25519
```

### 6.4 — Registrar la llave pública en Kali

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIARn5mjs9B2jO6r5nlCG/pXYsSV0Oy/QKNrjmutK22Vc cursor-kali-lab" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

### 6.5 — Configurar Cursor

Instalé la extensión **Remote - SSH** en Cursor.
Archivo `C:\Users\KEVIN007\.ssh\config`:

```
Host kali-lab
    HostName 100.83.186.5
    User thony
    Port 22
    IdentityFile ~/.ssh/id_ed25519
```

### 6.6 — Conectar Cursor a Kali

- `Ctrl+Shift+P` → `Remote-SSH: Connect to Host` → `kali-lab`
- Plataforma del servidor: **Linux**
- Cursor instaló su servidor en Kali (solo primera vez)

**Resultado:**

```
Indicador abajo izquierda: >< SSH: kali-lab   ✅
Terminal integrada muestra: (thony@kali)-[~]  ✅
```

---

## Paso 7 — Crear estructura de carpetas del proyecto

```bash
cd ~/Desktop/lab-bcrypt-security
mkdir -p datos analisis resultados capturas docs
```

```
lab-bcrypt-security/
├── venv/          ← NO se sube a GitHub
├── datos/
├── analisis/
├── resultados/
├── capturas/
└── docs/
```

---

## ✅ Estado final de la Fase 0

```
✅ Python 3.13.12          verificado
✅ Hashcat 7.1.2           verificado
✅ John 1.9.0-jumbo        verificado
✅ venv                    creado y activo
✅ bcrypt 5.0.0            instalado
✅ pandas 3.0.3            instalado
✅ matplotlib 3.10.9       instalado
✅ rockyou.txt             descomprimido (134 MB)
✅ Tailscale               activo en Kali (100.83.186.5)
✅ SSH                     activo y habilitado
✅ Llave SSH               configurada (ed25519)
✅ Cursor Remote SSH       conectado y funcionando
✅ Estructura de carpetas  creada
```

---

## 💡 Problemas encontrados y soluciones

| Problema | Causa | Solución |
|---|---|---|
| `externally-managed-environment` | Kali 2024 protege el Python del sistema | Usar `python3 -m venv venv` |
| `Failed password` en Cursor SSH | Contraseña con `#` y `$` interpretados mal | Configurar llave SSH ed25519 |
| IP de Kali cambia según la red | IP local depende del router | Instalar Tailscale (IP fija permanente) |

---

## ➡️ Siguiente fase

**[Fase 1 — Generación del dataset sintético](fase_01_dataset.md)**
