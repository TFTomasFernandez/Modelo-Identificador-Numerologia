# 🧮 AI - Reconocimiento de Símbolos Matemáticos

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![License](https://img.shields.io/badge/License-MIT-green)

Este proyecto de inteligencia artificial tiene como objetivo reconocer y predecir símbolos matemáticos a partir de imágenes mediante redes neuronales convolucionales (CNN). Está diseñado para procesar imágenes de números y símbolos matemáticos escritos a mano, con la finalidad de resolver operaciones matemáticas básicas.

## 🚀 Descripción del Proyecto

El modelo se entrena con imágenes de 64x64 píxeles en escala de grises que representan números y símbolos matemáticos. Utiliza una arquitectura CNN con varias capas de convolución y agrupación máxima (MaxPooling), optimizada para la clasificación de símbolos. Se emplea `LabelEncoder` para convertir las etiquetas de los símbolos en valores numéricos.

### ✨ Características Principales

- 🧠 **Modelo CNN**: Varias capas de convolución y agrupación que optimizan el reconocimiento de patrones en las imágenes.
- 🏷️ **Codificación de Etiquetas**: Uso de `LabelEncoder` para transformar las etiquetas de texto en números.
- 🔮 **Predicción en Tiempo Real**: Predice el símbolo en la imagen ingresada utilizando un modelo preentrenado.
- 🏋️ **Entrenamiento Personalizado**: Entrena el modelo con un conjunto de datos propio, organizado por clases de símbolos.

## 📂 Estructura del Proyecto

1. **📥 Carga de Imágenes**: Las imágenes se cargan desde una carpeta local, organizada en subcarpetas para cada clase.
2. **🔧 Preprocesamiento**: Las imágenes se convierten a escala de grises, se redimensionan a 64x64 píxeles y se normalizan para ajustarse al rango [0, 1].
3. **🏗️ Arquitectura del Modelo**:
   - Capas de convolución (`Conv2D`) seguidas de capas de agrupación máxima (`MaxPooling2D`).
   - Capa densa con activación `softmax` para la predicción de la clase.
4. **⚙️ Entrenamiento y Evaluación**: El modelo se entrena con 5 épocas sobre las imágenes preprocesadas.
5. **🔮 Predicción**: Carga una imagen de prueba y el modelo predice el símbolo.

## 🛠️ Requisitos

- ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
- ![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24%2B-lightblue)
- ![Pillow](https://img.shields.io/badge/Pillow-8.x-yellow)
- ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.3%2B-purple)
- ![NumPy](https://img.shields.io/badge/NumPy-1.19%2B-blue)

## 🛤️ Futuras Mejoras

🎯 Mejorar la precisión del modelo mediante el ajuste de hiperparámetros y técnicas de aumento de datos.

➕ Ampliar el conjunto de datos con más símbolos matemáticos y operadores complejos.

🧠 Implementar capacidades de interpretación para secuencias matemáticas completas.

## 👨‍💻 Autor:
### Tomas Fernandez

GitHub : TFTomasFernandez

LinkedIn: (https://www.linkedin.com/in/tomas-fernandez-7a7957257/)
