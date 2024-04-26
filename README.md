# Aves de Chile

## Descripción
Este proyecto es una aplicación web desarrollada usando Flask que presenta una galería de aves chilenas. Cada ave se muestra con su nombre en español e inglés y está acompañada de una imagen representativa. Esta herramienta está diseñada para educar al público sobre la diversidad aviar de Chile y potenciar el turismo ecológico.

## Características
- **Listado de aves:** Visualiza una lista de aves con su correspondiente nombre en español e inglés.
- **Imágenes:** Cada entrada en la lista incluye una imagen del ave correspondiente.
- **Información detallada:** Acceso a detalles adicionales al seleccionar una ave específica.

## Tecnologías Utilizadas
- **Python 3.7+**
- **Flask**
- **Requests**: Para realizar llamadas a la API externa que provee los datos de las aves.
- **HTML/CSS**: Para la estructuración y diseño de la página web.

## Instalación

Para ejecutar este proyecto localmente, sigue los siguientes pasos:

### Pre-requisitos
Asegúrate de tener Python y pip instalados en tu máquina. También es recomendable usar un entorno virtual:

```bash
pip install virtualenv
virtualenv venv
# Windows
venv\Scripts\activate
# MacOS/Linux
source venv/bin/activate

Dependencias
Instala todas las dependencias necesarias con pip:

bash
Copy code
pip install flask requests
Ejecución
Clona este repositorio y navega al directorio del proyecto:

bash
Copy code
git clone https://github.com/NobelikoCL/ejercicio_api.git
cd ejercicio_api
Ejecuta la aplicación:

bash
Copy code
python app.py
Abre tu navegador y visita http://127.0.0.1:5000/ para ver la aplicación en acción.

Contribuir
Las contribuciones son lo que hacen que la comunidad de código abierto sea un lugar tan increíble para aprender, inspirar y crear. Cualquier contribución que hagas será muy apreciada.

Bifurca el proyecto
Crea tu rama de características (git checkout -b feature/AmazingFeature)
Realiza tus cambios y haz commit (git commit -m 'Add some AmazingFeature')
Empuja a la rama (git push origin feature/AmazingFeature)
Abre una Pull Request
