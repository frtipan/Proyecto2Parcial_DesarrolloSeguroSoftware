# Proyecto Segundo Parcial - Desarrollo Seguro de Software

## Integrantes

* Fernando Tipán
* Kevin Asmal

---

## NRC

30735-DESARROLLO SOFTWARE SEGURO

---

# Detector Inteligente de Vulnerabilidades en Código Fuente

Sistema desarrollado para la asignatura de Desarrollo Seguro de Software.

El proyecto implementa un modelo de Inteligencia Artificial capaz de detectar vulnerabilidades en código fuente y además integra un ciclo de vida de software seguro mediante automatización CI/CD, análisis de seguridad, pruebas automáticas y despliegue continuo.

---

# Objetivo

Diseñar e implementar un pipeline CI/CD seguro que permita detectar automáticamente vulnerabilidades mediante un modelo de Machine Learning basado en minería de datos, garantizando que únicamente el código seguro llegue a producción.

---

# Etapas del Pipeline CI/CD Seguro

## Etapa 1: Revisión de Seguridad con Inteligencia Artificial

El pipeline se activa automáticamente cuando se crea un Pull Request desde la rama `dev` hacia la rama `test`.

Durante esta etapa se realiza:

* Obtención de los archivos modificados.
* Extracción de características del código fuente.
* Clasificación del código mediante un modelo de Machine Learning basado en Logistic Regression.

Si el modelo clasifica el código como **VULNERABLE**:

* Se bloquea el Pull Request.
* Se crea una Issue automáticamente.
* Se agrega un comentario en el Pull Request.
* Se envía una notificación mediante Telegram.
* Se solicita la corrección del código.

Si el modelo clasifica el código como **SAFE**, el pipeline continúa con la siguiente etapa.

---

## Etapa 2: Ejecución de Pruebas Automáticas

Una vez aprobada la revisión de seguridad, se ejecutan las pruebas automáticas mediante Pytest.

Las pruebas verifican:

* Correcta clasificación de código seguro.
* Correcta clasificación de código vulnerable.
* Funcionamiento del modelo de Inteligencia Artificial.
* Funcionamiento de la API REST.

Si alguna prueba falla:

* Se detiene el pipeline.
* Se bloquea el merge.
* Se envía una notificación mediante Telegram.

Si todas las pruebas son exitosas, se continúa con la siguiente etapa.

---

## Etapa 3: Integración hacia la rama Test

Después de superar la revisión de seguridad y las pruebas automáticas, el código es integrado en la rama `test`.

La rama `test` funciona como entorno de validación antes de pasar a producción.

Durante esta etapa se generan notificaciones automáticas indicando que:

* El código es seguro.
* Las pruebas fueron ejecutadas correctamente.

---

## Etapa 4: Integración hacia Producción

Una vez validado el funcionamiento en la rama `test`, se crea un Pull Request desde:

test → main

La rama `main` representa el entorno de producción.

Solo el código que haya superado todas las verificaciones anteriores puede llegar a producción.

---

## Etapa 5: Despliegue Continuo

Después del merge hacia la rama `main`, se realiza el despliegue automático de la aplicación.

El despliegue se efectúa en Render, permitiendo que la API se encuentre disponible en línea.

URL de producción:

https://proyecto2parcial-desarrollosegurosoftware.onrender.com/

---

## Etapa 6: Sistema de Notificaciones

Durante todo el ciclo de vida del pipeline se envían notificaciones automáticas mediante Telegram.

Eventos notificados:

* Inicio de revisión de seguridad.
* Resultado de la clasificación del modelo.
* Resultado de las pruebas automáticas.
* Código seguro.
* Vulnerabilidades detectadas.
* Bloqueo del Pull Request.
* Despliegue exitoso en producción.

---

## Flujo General del Pipeline

Desarrollador

↓

Push en rama dev

↓

Pull Request dev → test

↓

Etapa 1: Revisión de Seguridad con IA

↓

Etapa 2: Ejecución de Pruebas Automáticas

↓

Etapa 3: Integración en rama test

↓

Pull Request test → main

↓

Etapa 4: Integración hacia producción

↓

Etapa 5: Despliegue en Render

↓

Etapa 6: Notificaciones Telegram

↓

Aplicación disponible en producción


---
# Tecnologías Utilizadas

## Backend

* Python 3.11
* Flask
* Flask-Talisman
* Flask-Limiter

## Inteligencia Artificial

* Scikit-Learn
* Logistic Regression
* TF-IDF Vectorizer
* Pandas
* NumPy
* Joblib

## DevSecOps

* GitHub Actions
* Pull Requests
* GitHub Issues
* Branch Protection Rules

## Notificaciones

* Telegram Bot API

## Despliegue

* Render

---

# Arquitectura General

```text
Usuario
   │
   ▼
Flask API
   │
   ▼
Preprocesamiento TF-IDF
   │
   ▼
Modelo Logistic Regression
   │
   ▼
Predicción
SAFE / VULNERABLE
```

---

# Estructura del Proyecto

```text
Proyecto2Parcial_DesarrolloSeguroSoftware
│
├── app.py
├── requirements.txt
│
├── models
│     └── model.joblib
│
├── data
│     └── juliet_balanced.csv
│
├── src
│     ├── api
│     ├── controllers
│     ├── ml
│     │      ├── train.py
│     │      └── predict.py
│     │
│     ├── ci_cd
│     │      ├── security_check.py
│     │      └── deploy.py
│     │
│     └── ndt
│            └── diff_analyzer.py
│
├── test
│     ├── test_api.py
│     └── test_model.py
│
└── .github
      └── workflows
             secure_pipeline.yml
```

---

# Metodología SSDLC

El proyecto fue desarrollado siguiendo el enfoque Secure Software Development Life Cycle.

## Fase de Análisis

Se identificaron amenazas y vulnerabilidades comunes:

* Buffer Overflow
* Command Injection
* Code Injection
* Uso inseguro de funciones del sistema
* Manejo inseguro de memoria

---

## Fase de Diseño Seguro

La arquitectura fue dividida en:

* API REST
* Módulo de IA
* Pipeline CI/CD
* Sistema de notificaciones
* Despliegue continuo

---

## Fase de Implementación Segura

### Flask-Talisman

Permite agregar:

* Strict-Transport-Security
* X-Frame-Options
* Content-Security-Policy

Configuración:

```python
Talisman(app)
```

### Flask-Limiter

Protección contra abuso del API.

```python
Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["50 per minute"]
)
```

---

## Fase de Verificación

Se desarrollaron pruebas automáticas con Pytest.

Casos evaluados:

* Código seguro en C
* Código vulnerable en C
* Código seguro en Python
* Código vulnerable en Python

---

## Fase de Despliegue

La aplicación fue desplegada en Render mediante integración continua.

---

# Dataset Utilizado

Dataset balanceado:

```text
Juliet Test Suite
```

Clases:

* SAFE
* VULNERABLE

Cantidad de muestras:

```text
1564 registros

782 SAFE
782 VULNERABLE
```

---

# Entrenamiento del Modelo

Flujo utilizado:

```text
Dataset
     │
     ▼
Extracción de Features
     │
     ▼
TF-IDF
     │
     ▼
Logistic Regression
     │
     ▼
model.joblib
```

---

# Features Utilizadas

## TF-IDF

Representación vectorial del código fuente.

```python
TfidfVectorizer()
```

## Features Manuales

### Funciones peligrosas

* gets()
* strcpy()
* strcat()
* sprintf()
* scanf()
* system()
* eval()
* exec()
* os.system()

### Sanitizadores

* fgets()
* strncpy()
* snprintf()
* sanitize()
* escape()

### Otras características

* Número de funciones peligrosas
* Número de sanitizadores
* Longitud del código
* Número de líneas

---

# Modelo Utilizado

Modelo supervisado:

```python
LogisticRegression()
```

Clasifica:

* SAFE
* VULNERABLE

---

# Flujo de Predicción

```text
Código Fuente
      │
      ▼
TF-IDF
      │
      ▼
Logistic Regression
      │
      ▼
SAFE / VULNERABLE
```

---

# Accuracy del Modelo

Resultado obtenido:

```text
95.41%
```

Cumpliendo el requisito mínimo:

```text
≥ 82%
```

---

# Pipeline DevSecOps

## Ramas Implementadas

```text
dev
 ↓
test
 ↓
main
```

---

# Flujo CI/CD

1. Pull Request dev → test
2. Revisión de seguridad mediante IA
3. Bloqueo automático si existe vulnerabilidad
4. Ejecución de pruebas
5. Creación automática de Issues
6. Comentarios automáticos
7. Notificaciones Telegram
8. Merge hacia test
9. Merge hacia main
10. Despliegue automático

---

# Automatizaciones Implementadas

## Security Check

Analiza automáticamente los cambios enviados.

Si detecta una vulnerabilidad:

* Bloquea el merge
* Crea una Issue
* Agrega comentarios
* Envía mensajes Telegram

---

## Tests Automatizados

Pruebas unitarias con:

```bash
pytest
```

---

## Comentarios Automáticos

```text
❌ Vulnerabilidad detectada por IA

Resultado: VULNERABLE

El merge fue bloqueado automáticamente.
```

---

## Issues Automáticas

Ejemplo:

```text
Vulnerabilidad detectada por IA
```

---

## Etiquetas Automáticas

### fixing-required

Aplicada cuando existe una vulnerabilidad.

### tests-failed

Aplicada cuando fallan las pruebas.

---

# Notificaciones Telegram

### Inicio de revisión

```text
🔍 Inicio revisión de seguridad
```

### Código seguro

```text
✅ Código seguro
```

### Pruebas exitosas

```text
🧪 Tests exitosos
```

### Merge exitoso

```text
🚀 Merge a test realizado correctamente
```

### Pipeline fallido

```text
❌ Pipeline fallido
```

### Vulnerabilidad detectada

```text
🚨 Vulnerabilidad detectada
```

---

# Branch Protection Rules

## Rama test

* Pull Request obligatorio
* Checks obligatorios
* Sin push directo

## Rama main

* Pull Request obligatorio
* Checks obligatorios
* Sin push directo

---

# API REST

## GET /

Respuesta:

```json
{
  "message": "Secure Code Detector API",
  "status": "running"
}
```

---

## GET /health

Respuesta:

```json
{
  "status": "ok"
}
```

---

# Ejemplo de Vulnerabilidad Detectada

Código vulnerable:

```c
char buffer[10];

gets(buffer);
```

Resultado:

```json
{
  "result":"VULNERABLE",
  "confidence":99.0,
  "vulnerability":"Buffer Overflow"
}
```

---

# Ejemplo de Código Seguro

```c
char buffer[50];

fgets(buffer,sizeof(buffer),stdin);
```

Resultado:

```json
{
  "result":"SAFE",
  "confidence":95.0
}
```

---

# Despliegue

Aplicación desplegada en Render.

URL:

```text
https://proyecto2parcial-desarrollosegurosoftware.onrender.com/
```

---

# Ejecución Local

Clonar repositorio:

```bash
git clone https://github.com/frtipan/Proyecto2Parcial_DesarrolloSeguroSoftware.git
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar aplicación:

```bash
python app.py
```

---

# Ejecución de Pruebas

```bash
pytest
```

---

# Cumplimiento del Proyecto

| Requisito                  | Estado |
| -------------------------- | ------ |
| Modelo de IA propio        | ✅      |
| Logistic Regression        | ✅      |
| Dataset público            | ✅      |
| Accuracy superior al 82%   | ✅      |
| Pull Requests obligatorios | ✅      |
| Branch Protection Rules    | ✅      |
| GitHub Actions             | ✅      |
| Tests automáticos          | ✅      |
| Telegram Bot               | ✅      |
| Comentarios automáticos    | ✅      |
| Issues automáticas         | ✅      |
| SSDLC                      | ✅      |
| DevSecOps                  | ✅      |
| Shift Left Security        | ✅      |
| Despliegue en Render       | ✅      |

---

# Resultados Alcanzados

✅ Inteligencia Artificial

✅ TF-IDF

✅ Logistic Regression

✅ Backend Seguro

✅ SSDLC

✅ DevSecOps

✅ Shift Left Security

✅ GitHub Actions

✅ Pull Requests obligatorios

✅ Branch Protection Rules

✅ Issues automáticas

✅ Comentarios automáticos

✅ Telegram Bot

✅ Integración Continua

✅ Entrega Continua Segura

✅ Despliegue Automático

✅ Accuracy superior al 82%
