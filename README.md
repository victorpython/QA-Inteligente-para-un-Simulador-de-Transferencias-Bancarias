# 🏦 Simulación de Transferencias Bancarias con QA Automatizado

## Proyecto de automatización de pruebas en entorno bancario simulado
Este repositorio contiene una mini aplicación Flask que simula una interfaz bancaria, junto con pruebas automatizadas usando pytest, organizadas bajo el patrón Page Object Model y documentadas con reportes HTML.

## 🚀 Instrucciones para ejecutar

1. Asegúrate de tener instalado Python 3.9+ y Chrome con chromedriver agregado al PATH.

2. Instala las dependencias necesarias:
   
   ```bash
   pip install flask selenium pytest pytest-html
   ```
   
3. Inicia el stub del servidor Flask (debe estar activo antes de lanzar los tests):

   ```bash
   cd app
   python app.py
   ```

4. En otra terminal, ejecuta las pruebas:

   ```bash
   cd ..
   pytest tests/test_transferencias.py --html=reports/test_report.html
   ```

## ✅ Funcionalidad cubierta

- Envío de instrucciones de transferencia bancaria simuladas.

- Validación de respuestas generadas por un "modelo IA" ficticio.

- Reporte detallado de resultados con ```pytest-html```.

## 🧠 Tecnologías utilizadas

- **Flask** – Para construir el stub de la app bancaria.

- **Selenium** – Para automatizar la interacción con la interfaz web.

- **Pytest** – Framework principal de pruebas.

- **Pytest-HTML** – Generación de reportes legibles.

## 📁 Estructura del proyecto

```bash
qa-banking-simulation/
├── app/                     # Mini servidor Flask (banca simulada)
│   ├── __init__.py
│   ├── app.py               # Servidor web
│   ├── model_sim.py         # "Modelo IA" que interpreta instrucciones
│   └── templates/
│       └── index.html       # Interfaz del usuario
├── tests/                   # Tests automatizados
│   ├── __init__.py
│   └── test_transferencias.py # Validaciones de texto con IA
├── reports/                 # Reportes de pruebas
│   ├── test_report.html     # Reporte generado por pytest-html
```
