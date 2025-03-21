# Hotel Dashboard con Video de Fondo

Una aplicación web profesional que muestra un dashboard de hotel con video de fondo a pantalla completa y efectos visuales.

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Navegador web moderno (Chrome, Firefox, Safari)

## Instalación

1. Clona o descarga este repositorio
2. Abre una terminal en la carpeta del proyecto
3. Instala las dependencias:
```bash
pip install flask
```

## Estructura del Proyecto

```
hotel-dashboard/
├── assets/
│   └── style.css
├── index.html
├── main.py
└── README.md
```

## Cómo Ejecutar

1. Abre una terminal en la carpeta del proyecto
2. Ejecuta el servidor:
```bash
python main.py
```
3. Abre tu navegador y visita:
```
http://localhost:5000
```

## Características

- Video de fondo a pantalla completa con control de volumen
- Diseño responsivo
- Interfaz moderna con efectos visuales
- Menú interactivo con iconos
- Reloj en tiempo real
- Información del clima
- Carousel de servicios del hotel

## Personalización

Para cambiar el video de fondo, modifica la URL del video en el archivo `index.html`:

```html
<video id="background-video" autoplay loop muted playsinline>
    <source src="TU_URL_DE_VIDEO" type="video/mp4">
</video>
```

## Notas

- El video de fondo se reproduce automáticamente y en bucle
- Los controles de volumen están ubicados en la esquina inferior izquierda
- La interfaz es completamente responsiva y se adapta a diferentes tamaños de pantalla
# demo_clientes
