# Proyecto Segundo Parcial - Desarrollo Seguro de Software

## Integrante

- Fernando Tipán

---

# Detector Inteligente de Vulnerabilidades en Código Fuente

Sistema desarrollado para la asignatura de Desarrollo Seguro de Software.

El proyecto implementa un modelo de Inteligencia Artificial capaz de detectar vulnerabilidades en código fuente escrito en C/C++ y además integra un ciclo de vida de software seguro mediante automatización CI/CD, análisis de seguridad, pruebas automáticas y despliegue continuo.

---

# Objetivo

Detectar automáticamente vulnerabilidades comunes en código fuente utilizando Machine Learning y aplicar prácticas de Desarrollo Seguro de Software durante todo el ciclo de vida del proyecto.

---

# Tecnologías Utilizadas

## Backend

- Python 3.11
- Flask
- Flask-Talisman
- Flask-Limiter

## Inteligencia Artificial

- Scikit-Learn
- Logistic Regression
- TF-IDF Vectorizer
- Pandas
- NumPy
- Joblib

## DevSecOps

- GitHub Actions
- GitHub Issues
- Pull Requests
- Branch Protection Rules

## Notificaciones

- Telegram Bot API

## Despliegue

- Render

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

# Metodología de Desarrollo Seguro

El proyecto fue desarrollado siguiendo principios de Secure Software Development Lifecycle (SSDLC).

## Fase de Análisis

Se identificaron amenazas y vulnerabilidades comunes presentes en aplicaciones desarrolladas en lenguaje C.

Vulnerabilidades consideradas:

- Buffer Overflow
- Uso de gets()
- strcpy()
- strcat()
- Manejo inseguro de memoria

---

## Fase de Diseño Seguro

Se diseñó una arquitectura separando:

- API REST
- Modelo de Inteligencia Artificial
- Pipeline CI/CD
- Sistema de notificaciones

Además se definieron controles de seguridad para proteger la aplicación.

---

## Fase de Implementación Segura

Se implementaron mecanismos de protección:

### Security Headers

Mediante Flask-Talisman.

### Rate Limiting

Mediante Flask-Limiter.

Configuración:

```python
Talisman(app)

Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["50 per minute"]
)
```

---

## Fase de Verificación

Se desarrollaron pruebas automáticas utilizando Pytest.

Casos evaluados:

- Código seguro
- Código vulnerable

Además se ejecutan automáticamente en cada Pull Request.

---

## Fase de Despliegue

Se realizó despliegue continuo utilizando Render.

La aplicación se encuentra disponible públicamente mediante una URL segura.

---

# Ciclo de Vida Seguro Implementado

```text
Desarrollo
    │
    ▼
Pull Request
    │
    ▼
Análisis IA
    │
    ▼
Tests Automatizados
    │
    ▼
Validación de Seguridad
    │
    ▼
Merge
    │
    ▼
Deploy Render
```

---

# Dataset

Se utilizó un conjunto de ejemplos de código clasificados como:

- SAFE
- VULNERABLE

Ejemplo vulnerable:

```c
gets(buffer);
```

Ejemplo seguro:

```c
fgets(buffer,sizeof(buffer),stdin);
```

---

# Inteligencia Artificial

## Preprocesamiento

Antes del entrenamiento se realizó extracción de características utilizando:

### TF-IDF (Term Frequency - Inverse Document Frequency)

TF-IDF permite transformar fragmentos de código fuente en vectores numéricos para que puedan ser procesados por algoritmos de Machine Learning.

Implementación:

```python
vectorizer = TfidfVectorizer()
```

---

## Modelo Utilizado

Se utilizó un modelo supervisado de clasificación:

```python
LogisticRegression()
```

El modelo fue entrenado para clasificar fragmentos de código en dos categorías:

- SAFE
- VULNERABLE

---

## Flujo de Predicción

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

Accuracy obtenida:

```text
95.41%
```

Cumpliendo el requisito mínimo solicitado:

```text
≥ 82%
```

---

# Pipeline DevSecOps

## Estructura de Ramas

```text
dev
 ↓
test
 ↓
main
```

---

# Flujo CI/CD

1. Desarrollo en rama dev
2. Pull Request hacia test
3. Security Check
4. Ejecución de Tests
5. Comentario automático
6. Creación automática de Issue
7. Notificación Telegram
8. Merge hacia test
9. Pull Request hacia main
10. Despliegue automático en Render

---

# Automatizaciones Implementadas

## Detección Automática de Vulnerabilidades

El pipeline analiza automáticamente el código enviado mediante Pull Request.

Cuando detecta vulnerabilidades:

- Bloquea el merge
- Crea una Issue
- Agrega comentarios automáticos
- Envía notificaciones Telegram

---

## Comentario Automático

```text
❌ Vulnerabilidad detectada por IA

Resultado: VULNERABLE

El merge fue bloqueado.
```

---

## Creación Automática de Issues

Ejemplo:

```text
Vulnerabilidad detectada por IA
```

---

## Etiquetas Automáticas

### fixing-required

Aplicada cuando se detecta una vulnerabilidad.

### tests-failed

Aplicada cuando las pruebas fallan.

---

# Notificaciones Telegram

## Inicio de Validación

```text
🔍 Inicio revisión de seguridad
```

## Código Seguro

```text
✅ Código seguro
```

## Tests Exitosos

```text
🧪 Tests exitosos
```

## Merge Exitoso

```text
🚀 Merge a test realizado correctamente
```

## Pipeline Fallido

```text
❌ Pipeline fallido
```

---

# Protección de Ramas

Configurada para:

## Rama test

- Pull Request obligatorio
- Checks obligatorios
- Sin push directo

## Rama main

- Pull Request obligatorio
- Checks obligatorios
- Sin push directo

---

# API REST

## Endpoint Principal

```http
GET /
```

Respuesta:

```json
{
  "message": "Secure Code Detector API",
  "status": "running"
}
```

---

## Endpoint Health Check

```http
GET /health
```

Respuesta:

```json
{
  "status": "ok"
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

# Resultados Alcanzados

✅ Inteligencia Artificial para detección de vulnerabilidades

✅ TF-IDF para extracción de características

✅ Logistic Regression para clasificación

✅ Backend Seguro

✅ SSDLC

✅ GitHub Actions

✅ DevSecOps

✅ Pull Requests obligatorios

✅ Branch Protection Rules

✅ Issues automáticas

✅ Comentarios automáticos

✅ Notificaciones Telegram

✅ Despliegue en Render

✅ Integración Continua

✅ Entrega Continua Segura

✅ Accuracy superior al 82%