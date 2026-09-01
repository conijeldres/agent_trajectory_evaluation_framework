# Informe final: Agent Trajectory Evaluation Framework

## 1. Resumen ejecutivo

Este proyecto presenta un marco ligero para evaluar agentes de inteligencia artificial más allá de la corrección de la respuesta final. En lugar de analizar únicamente si la respuesta final parece adecuada, el framework observa la trayectoria completa del agente: cómo interpreta la consulta del usuario, qué documentos selecciona, qué información recupera, cómo respeta los límites del dominio y qué tan útil resulta su respuesta final.

El caso de uso inicial corresponde a un agente de apoyo administrativo en salud en español. Este dominio fue elegido porque combina tareas aparentemente simples, como reagendar una hora médica o consultar requisitos de documentación, con situaciones de ambigüedad, sensibilidad, privacidad y potencial riesgo clínico.

El proyecto incluye un dataset sintético de 10 tareas, una base de conocimiento sintética, un agente baseline basado en reglas, trazas generadas en formato JSON, revisiones cualitativas por tarea y resultados cuantitativos generados con Python. La evaluación muestra que el agente tiene un buen desempeño en seguridad y límites, pero presenta debilidades en detección de intención, recuperación de información específica y adecuación comunicativa.

## 2. Objetivo del proyecto

El objetivo principal del proyecto es diseñar y aplicar un framework de evaluación de trayectorias para agentes de IA, con énfasis en tareas administrativas de salud en español.

El proyecto busca demostrar que evaluar únicamente la respuesta final no basta. Una respuesta puede parecer correcta a simple vista, pero la trayectoria del agente puede revelar fallos importantes, como una mala selección de documentos, recuperación de evidencia débil, clasificación incorrecta de la intención, falta de próximos pasos o el uso de una plantilla demasiado general.

## 3. Motivación

Los agentes de IA no solo generan texto. También interpretan instrucciones, planifican acciones, seleccionan herramientas, consultan fuentes, recuperan información y deciden qué límites deben respetarse. Por eso, su evaluación requiere observar el proceso completo.

En dominios sensibles, como la salud, esta necesidad es todavía más importante. Un agente administrativo no debería ofrecer consejo médico, interpretar síntomas ni confirmar acciones como cambios de hora sin validación. Evaluar la trayectoria permite identificar si el agente actuó de forma segura incluso antes de leer la respuesta final.

Este proyecto surge de la idea de crear un método claro y detallado para analizar el comportamiento de un agente, asegurando que sea auditable y reproducible.

## 4. Caso de uso inicial

El caso de uso inicial es un agente de apoyo administrativo en salud en español.

El agente debe responder consultas no clínicas relacionadas con:

- búsqueda y reagendamiento de horas médicas;
- políticas de cancelación;
- atrasos y asistencia;
- requisitos de documentación;
- medios de pago y cobertura;
- dudas sobre privacidad o mensajes sospechosos;
- derivación a soporte humano cuando corresponde.

El agente no debe entregar:

- diagnóstico clínico;
- recomendaciones de tratamiento;
- triaje de urgencia;
- interpretación de síntomas;
- interpretación de exámenes;
- instrucciones sobre medicamentos;
- consejo médico personalizado.

## 5. Componentes del proyecto

El repositorio contiene los siguientes componentes principales:

```text
data/
  tasks_spanish_healthcare_admin.jsonl
  knowledge_base/

docs/
  project_scope.md
  project_scope.es.md
  final_report.es.md

src/
  agent.py
  tools.py
  schemas.py
  run_agent.py

traces/
  task_*_trace.json

evaluations/
  trace_review_template.md
  trace_review_template.es.md
  trace_review_task_*.md
  trace_review_task_*.es.md
  results/

scripts/
  create_evaluation_tables.py
