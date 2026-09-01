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
```
## 6. Metodología

La metodología del proyecto se desarrolló en seis etapas.

### 6.1 Diseño del dataset

Se creó un dataset sintético de 10 tareas en español, centrado en consultas administrativas de salud. Cada tarea incluye:

- identificador de tarea;
- dominio;
- idioma;
- consulta del usuario;
- comportamiento esperado;
- nivel de riesgo;
- herramientas requeridas;
- dimensiones de evaluación;
- posibles modos de fallo.

Las tareas fueron diseñadas para cubrir casos simples, ambiguos y sensibles. Algunas consultas son puramente administrativas, mientras que otras incluyen elementos de seguridad, privacidad o posible escalamiento humano.

### 6.2 Creación de la base de conocimiento

Se creó una base de conocimiento sintética con documentos en inglés y español. Los documentos cubren políticas administrativas sobre:

- horas médicas;
- cancelación y atrasos;
- requisitos de documentación;
- pago y cobertura;
- seguridad y derivación.

Estos documentos funcionan como fuente de referencia para evaluar si el agente selecciona y recupera información pertinente.

### 6.3 Implementación del agente baseline

Se implementó un agente baseline simple en Python. Esta primera versión no utiliza LLMs, embeddings, APIs externas, LangChain ni LlamaIndex. Su objetivo es producir trayectorias transparentes y fáciles de auditar.

El agente realiza cuatro pasos principales:

1. detecta la intención del usuario mediante reglas por palabras clave;
2. selecciona documentos de la base de conocimiento según la intención detectada;
3. recupera información usando búsqueda simple por palabras clave;
4. genera una respuesta final a partir de una plantilla asociada a la intención.

### 6.4 Generación de trazas

Para cada tarea del dataset, el agente genera una traza en formato JSON. Cada traza contiene:

- consulta del usuario;
- intención detectada;
- documentos seleccionados;
- pasos ejecutados;
- herramienta utilizada;
- entrada y salida de cada paso;
- respuesta final.

Estas trazas permiten evaluar no solo el resultado final, sino también el camino que siguió el agente.

### 6.5 Evaluación cualitativa por tarea

Cada traza fue revisada manualmente usando una plantilla de evaluación. La revisión considera seis dimensiones principales:

1. comprensión de la tarea;
2. selección de documentos;
3. recuperación de información;
4. fidelidad a las fuentes;
5. seguridad y límites;
6. adecuación comunicativa.

Para cada dimensión se asignó una evaluación cualitativa:

- correcta;
- parcialmente correcta;
- incorrecta.

También se identificaron etiquetas de fallo cuando correspondía.

### 6.6 Evaluación cuantitativa con rúbrica

Luego se transformaron las evaluaciones cualitativas en puntajes de 0 a 4. Esta rúbrica permite obtener:

- puntaje por dimensión;
- promedio por tarea;
- promedio por dimensión;
- resultado global de cada trayectoria;
- distribución de trayectorias exitosas, parcialmente exitosas y fallidas.

Los resultados fueron procesados con un script en Python que genera tablas y gráficos en inglés y español.

## 7. Dimensiones de evaluación

Las dimensiones utilizadas permiten revisar distintos niveles del comportamiento del agente.

### 7.1 Comprensión de la tarea

Evalúa si el agente identificó correctamente la intención principal del usuario.

### 7.2 Selección de documentos

Evalúa si el agente seleccionó las fuentes adecuadas de la base de conocimiento.

### 7.3 Recuperación de información

Evalúa si el agente recuperó fragmentos relevantes y suficientemente específicos.

### 7.4 Fidelidad a las fuentes

Evalúa si la respuesta final está respaldada por la información recuperada.

### 7.5 Seguridad y límites

Evalúa si el agente respetó el alcance administrativo y evitó entregar orientación clínica insegura.

### 7.6 Adecuación comunicativa

Evalúa si la respuesta fue clara, útil, contextualizada y accionable para el usuario.

## 8. Resultados generales

Se evaluaron 10 trayectorias en total.

```text
Total de tareas evaluadas: 10
Trayectorias exitosas: 2
Trayectorias parcialmente exitosas: 6
Trayectorias fallidas: 2
Promedio general del agente: 3.12 / 4
```

El promedio por dimensión fue el siguiente:

```text
Comprensión de la tarea: 3.40
Selección de documentos: 3.40
Recuperación de información: 2.60
Fidelidad a las fuentes: 3.20
Seguridad y límites: 4.00
Adecuación comunicativa: 2.30
```

La dimensión con mejor desempeño fue **seguridad y límites**. La dimensión más débil fue **adecuación comunicativa**, seguida por **recuperación de información**.

## 9. Hallazgos principales

### 9.1 Buen desempeño en seguridad

El agente obtuvo un desempeño sólido en seguridad y límites. En las tareas evaluadas, no entregó diagnóstico clínico, no interpretó síntomas, no recomendó tratamientos y no solicitó datos clínicos innecesarios.

Esto es especialmente relevante en tareas como `task_004`, donde el usuario menciona fiebre alta en una niña, y `task_007`, donde se solicita una hora urgente con psiquiatría infantil. En ambos casos, el agente evitó tomar decisiones clínicas y recomendó contacto con profesionales de salud o servicios de urgencia cuando correspondía.

### 9.2 Problemas de detección de intención

El principal problema de clasificación apareció en tareas donde la palabra `hora` activó incorrectamente la intención `appointment_management`.

Esto ocurrió en:

- `task_002`: el usuario preguntaba por cancelación el mismo día y posible cobro, pero el agente respondió sobre reagendamiento.
- `task_009`: el usuario preguntaba por horario de atención y atraso, pero el agente respondió sobre cambio de hora.

Este patrón muestra que la detección por palabras clave necesita priorizar señales específicas antes que términos generales.

### 9.3 Recuperación poco granular

En varias tareas el agente seleccionó documentos adecuados, pero recuperó fragmentos demasiado generales. Esto ocurrió especialmente en:

- `task_004`;
- `task_006`;
- `task_007`.

En estos casos, la respuesta final podía ser segura, pero la evidencia visible en la traza no siempre mostraba el fragmento más específico que justificaba la respuesta.

### 9.4 Respuestas demasiado generales

El agente suele responder con plantillas seguras, pero no siempre suficientemente adaptadas al contexto del usuario.

Esto se observó en:

- `task_003`, donde el usuario preguntaba por pediatría y el agente respondió con una lista general de documentos;
- `task_005`, donde el usuario hizo dos preguntas, Fonasa y transferencia, pero el agente no las separó claramente;
- `task_008`, donde el usuario indicó preferencia de horario en la tarde, pero el agente no la reconoció explícitamente;
- `task_010`, donde el usuario preguntaba específicamente por formato impreso o digital, pero la respuesta comenzó con un checklist general.

## 10. Patrones de fallo observados

Los principales patrones de fallo fueron:

```text
1. Clasificación excesiva como appointment_management.
2. Recuperación de información poco específica.
3. Respuestas finales demasiado generales.
4. Falta de próximos pasos concretos.
5. Baja adaptación a consultas con más de una pregunta.
```

Las etiquetas de fallo más frecuentes incluyeron:

```text
missing_next_steps
low_user_usefulness
weak_retrieval
missing_key_information
misunderstood_intent
wrong_document_selected
irrelevant_retrieval
overgeneralization
```

## 11. Interpretación

El agente baseline cumple su propósito como primera versión auditable. Su diseño simple permite observar con claridad dónde se producen los errores: en la detección de intención, en la selección de documentos, en la recuperación de información o en la generación de la respuesta final.

La evaluación demuestra que una trayectoria puede ser segura pero todavía insuficiente desde el punto de vista comunicativo. También muestra que una respuesta final aparentemente razonable puede ocultar una recuperación débil o poco específica.

El valor del framework está precisamente en hacer visibles esas capas intermedias.

## 12. Recomendaciones para la siguiente iteración

A partir de los resultados, se proponen las siguientes mejoras:

1. Ajustar el orden de detección de intención para priorizar términos específicos antes que términos generales como `hora`.
2. Crear una intención específica para horarios y atrasos, por ejemplo `opening_hours_or_late_arrival`.
3. Mejorar la recuperación para priorizar secciones específicas dentro de los documentos.
4. Incorporar plantillas de respuesta más contextuales según el tipo de consulta.
5. Separar respuestas cuando el usuario realiza más de una pregunta.
6. Agregar próximos pasos concretos en tareas administrativas.
7. Mantener las reglas de seguridad actuales, ya que funcionaron bien en consultas sensibles.
8. Añadir pruebas comparativas entre la versión baseline y una futura versión mejorada.
9. Considerar una futura implementación con recuperación semántica usando embeddings o LlamaIndex.
10. Considerar una futura versión con un agente con herramientas usando LangChain.

## 13. Limitaciones

Este proyecto es una primera versión experimental y tiene varias limitaciones.

El dataset es sintético y pequeño, con solo 10 tareas. La base de conocimiento también es sintética y no representa políticas reales de un centro médico. El agente baseline usa reglas simples por palabras clave y búsqueda básica, por lo que no debe interpretarse como un sistema listo para producción.

Además, las evaluaciones fueron realizadas manualmente, lo que permite análisis cualitativo detallado, pero también introduce subjetividad. Una etapa futura podría incluir múltiples evaluadores, acuerdo interanotador y comparación entre modelos o arquitecturas.

## 14. Conclusión

El proyecto demuestra que la evaluación de agentes de IA requiere mirar más allá de la respuesta final. Al analizar la trayectoria completa, es posible identificar fallos que permanecerían ocultos en una evaluación tradicional basada solo en output.

El agente baseline evaluado muestra un buen comportamiento en seguridad y límites, pero necesita mejoras en detección de intención, recuperación de información y adecuación comunicativa. Estos hallazgos son precisamente el tipo de evidencia que una evaluación por trayectorias permite obtener.

En conjunto, este framework ofrece una base inicial para evaluar agentes de IA de forma más transparente, auditable y sensible al contexto, especialmente en dominios donde el lenguaje, la seguridad y la utilidad práctica son inseparables.
