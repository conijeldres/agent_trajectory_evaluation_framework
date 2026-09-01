# Marco de Evaluación de Trayectorias de Agentes

Un marco ligero para evaluar agentes de IA más allá de la corrección de la respuesta final.

Este proyecto se centra en la trayectoria completa de un agente de IA: cómo entiende una tarea, planifica sus acciones, selecciona y usa herramientas, recupera información, se mantiene fiel a las fuentes, respeta límites de seguridad, se comunica con el usuario y produce una respuesta final útil.

## Implementación actual

La versión actual implementa un agente base simple en Python.

No utiliza LangChain, LlamaIndex, APIs externas de LLMs, embeddings ni sistemas reales de salud. Esto es intencional: el primer objetivo es crear trayectorias transparentes y auditables que puedan evaluarse antes de incorporar arquitecturas de agentes más complejas.

## Caso de uso inicial

El primer caso de uso es un agente de apoyo administrativo en salud en español.

El agente maneja tareas no clínicas, como reagendamiento de horas, políticas de cancelación, requisitos de documentación y derivación a soporte humano cuando corresponde.

Este dominio fue seleccionado porque combina ambigüedad real, ansiedad del usuario, información procedimental, privacidad y la necesidad de una comunicación clara, segura y sensible al contexto.

## Idea central

Evaluar solo la respuesta final no es suficiente para los agentes de IA.

Una respuesta final puede parecer correcta aunque el agente haya elegido mal una herramienta, recuperado evidencia débil, ignorado una ambigüedad, vulnerado un límite de seguridad o seguido una trayectoria ineficiente.

Este proyecto propone evaluar la trayectoria completa del agente, no solo su respuesta final.

## Dimensiones de evaluación

1. Comprensión de la tarea
2. Calidad de la planificación
3. Selección de herramientas
4. Ejecución de herramientas
5. Calidad de la recuperación de información
6. Fidelidad a las fuentes
7. Seguridad y límites
8. Adecuación comunicativa
9. Eficiencia
10. Utilidad para el usuario

# Resultados de evaluación

Esta carpeta contiene los resultados generados a partir de la evaluación por rúbrica de las trayectorias del agente.

Los archivos incluyen:

- `evaluation_results.md`: tabla de evaluación por tarea en inglés.
- `evaluation_results.es.md`: tabla de evaluación por tarea en español.
- `dimension_averages.md`: promedio por dimensión en inglés.
- `dimension_averages.es.md`: promedio por dimensión en español.
- `summary.md`: resumen general en inglés.
- `summary.es.md`: resumen general en español.
- `chart_dimension_averages.png`: gráfico de promedios por dimensión en inglés.
- `chart_dimension_averages.es.png`: gráfico de promedios por dimensión en español.
- `chart_overall_results.png`: gráfico de resultados globales en inglés.
- `chart_overall_results.es.png`: gráfico de resultados globales en español.

Estos archivos se generan con:

```bash
python scripts/create_evaluation_tables.py
```


## Idioma

Este repositorio está documentado en inglés y español.

- [English README](README.md)
- [Project Scope](docs/project_scope.md)
- [Alcance del proyecto](docs/project_scope.es.md)

## Estado

Proyecto en desarrollo.
