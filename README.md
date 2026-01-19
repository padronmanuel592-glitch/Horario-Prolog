# Horario-Prolog

# Generador de Horarios con Prolog y Python

## 📌 Descripción
Este proyecto implementa un **generador automático de horarios académicos** utilizando la integración entre **Python** y **Prolog** (a través de la librería `pyswip`).  
El sistema permite asignar clases a franjas horarias y aulas disponibles, respetando restricciones como:
- Disponibilidad de profesores.
- Evitar solapamiento de clases en la misma franja y aula.
- Garantizar que todas las clases definidas sean asignadas.

En esencia, el programa construye un **horario válido** que cumple las reglas locales y globales definidas en la base de conocimiento Prolog.

![streamlit-image](docs/streamlit-image.png)



---

## ⚙️ Funcionalidades
- Definición de **clases, profesores, duración**.
- Definición de **franjas horarias** y **aulas**.
- Restricciones de **no disponibilidad** de profesores.
- Generación de horarios válidos mediante reglas en Prolog.
- Procesamiento en Python para devolver el horario en formato estructurado (diccionario con clase, profesor, franja, aula, día y horas).

Ejemplo de salida:
```json
[
  {
    "clase": "ai_fundamentos",
    "profesor": "juan",
    "duracion": 2,
    "franja": "lunes_8_10",
    "aula": "a101",
    "dia": "lunes",
    "hora_inicio": "8",
    "hora_fin": "10"
  },
  ...
]
```

---

## 🛠️ Instalación

### 1. Requisitos previos
- **Python 3.8+**
- **SWI-Prolog** instalado en tu sistema (descargar aquí [(swi-prolog.org in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.swi-prolog.org%2FDownload.html"))
- Librería `pyswip` para conectar Python con Prolog.

### 2. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/generador-horarios.git
cd generador-horarios
```

### 3. Crear entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
```

### 4. Instalar dependencias
```bash
pip install -r install.txt
```

---

## ▶️ Uso
Ejecuta el script principal en Python:

```bash
python main.py
```

Esto generará un horario válido según las restricciones definidas en la base de conocimiento Prolog.

---

## 📚 Estructura del proyecto
```
├── main.py                
├── README.md              # Documentación del proyecto
├──Generador.py            # Script principal con la clase GeneradorHorarios
├──install.txt
├── .gitignore
```

---
## 🎥 Video Demo

Puedes ver la demostración completa en el siguiente enlace:  
[Ver video en Google Drive](https://share.google/gUXVmJ3OylqhdO59q)

---

## 👨‍💻 Autores
- Alejandro Colón Alvarez
- Manuel René de Moya
- Lázaro Cardero Calá
