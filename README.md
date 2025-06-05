# 👤 Backend de Registro y Autenticación Facial con Flask

Este proyecto es un backend desarrollado en **Python con Flask**, que proporciona una API REST para **registro de usuarios**, **autenticación**, y **verificación facial** usando modelos de reconocimiento.

---

## 📌 Descripción

El sistema permite registrar usuarios, gestionar autenticaciones seguras y utilizar reconocimiento facial para validar la identidad. Utiliza `Flask`, `Flask-Ninja` para manejo de vistas HTML si se desea, y librerías de visión computacional para procesar imágenes faciales. Es ideal para sistemas de control de acceso, asistencia o validación biométrica.

---

## 🚀 Características

- Registro de usuarios con datos personales y facial encoding
- Autenticación mediante usuario/contraseña
- Validación de identidad con reconocimiento facial (`.h5` o `face_recognition`)
- Endpoints RESTful usando Flask
- Almacenamiento de datos en base de datos (SQLAlchemy/MySQL/SQLite)
- Integración con HTML frontend usando Flask Ninja (opcional)

---

## 🛠️ Tecnologías

- Python 3.11
- Flask
- Flask-Ninja
- SQLAlchemy
- OpenCV / face_recognition
- h5py (si usas un modelo `.h5`)
- Flask-CORS (para acceso desde frontend React/Ionic/etc.)

---

## 📦 Instalación

### 1. Clonar el repositorio

git clone https://github.com/ClownLuck444/facetime.git
cd facetime
### 2. Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
### 3. Configurar base de datos
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db" 
### 4. Ejecutar
flask run


