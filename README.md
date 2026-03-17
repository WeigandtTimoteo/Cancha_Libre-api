# ⚽ Cancha Libre - API Engine

**Cancha Libre** es el motor lógico y estadístico de una plataforma integral para la gestión de fútbol. Esta API no solo centraliza datos de partidos profesionales, sino que implementa un algoritmo de **matchmaking** basado en el nivel de habilidad (*skill*) para equilibrar encuentros recreativos.

## 🚀 Características Principales

* **Algoritmo de Nivelación:** Lógica personalizada para la generación de equipos equilibrados basada en atributos de jugador.
* **Gestión de Estadísticas:** Almacenamiento y procesamiento de métricas de rendimiento (goles, asistencias, consistencia).
* **Matchmaking Engine:** Sistema de creación de partidos automáticos minimizando la brecha de nivel entre equipos.
* **Arquitectura RESTful:** Endpoints optimizados y documentados para el consumo desde clientes web y móviles.

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.x
* **Framework:** Django & Django REST Framework (DRF)
* **Base de Datos:** PostgreSQL / SQLite (Desarrollo)
* **Autenticación:** JWT (JSON Web Tokens)

## 🏗️ Lógica de Matchmaking

El sistema busca optimizar la paridad de los encuentros mediante la siguiente premisa:
$$\min \sum |Skill_{Equipo A} - Skill_{Equipo B}|$$

---
*Desarrollado por Timoteo Weigandt*