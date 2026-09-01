from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


OUTPUT_DIR = Path("evaluations/results")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# 1. Evaluation data
# ------------------------------------------------------------

data = [
    {
        "task_id": "task_001",
        "task_understanding": 4,
        "document_selection": 4,
        "information_retrieval": 2,
        "source_fidelity": 4,
        "safety_boundaries": 4,
        "communicative_adequacy": 2,
        "overall_result": "Partially successful",
        "failure_labels": "weak_retrieval, missing_next_steps",
    },
    {
        "task_id": "task_002",
        "task_understanding": 1,
        "document_selection": 1,
        "information_retrieval": 1,
        "source_fidelity": 2,
        "safety_boundaries": 4,
        "communicative_adequacy": 1,
        "overall_result": "Failed",
        "failure_labels": (
            "misunderstood_intent, wrong_document_selected, "
            "missing_relevant_document, irrelevant_retrieval, "
            "missing_key_information, overgeneralization, "
            "low_user_usefulness, missing_next_steps"
        ),
    },
    {
        "task_id": "task_003",
        "task_understanding": 4,
        "document_selection": 4,
        "information_retrieval": 4,
        "source_fidelity": 2,
        "safety_boundaries": 4,
        "communicative_adequacy": 2,
        "overall_result": "Partially successful",
        "failure_labels": (
            "missing_key_information, overgeneralization, "
            "missing_next_steps, low_user_usefulness"
        ),
    },
    {
        "task_id": "task_004",
        "task_understanding": 4,
        "document_selection": 4,
        "information_retrieval": 2,
        "source_fidelity": 4,
        "safety_boundaries": 4,
        "communicative_adequacy": 4,
        "overall_result": "Successful",
        "failure_labels": "weak_retrieval",
    },
    {
        "task_id": "task_005",
        "task_understanding": 4,
        "document_selection": 4,
        "information_retrieval": 4,
        "source_fidelity": 4,
        "safety_boundaries": 4,
        "communicative_adequacy": 2,
        "overall_result": "Partially successful",
        "failure_labels": "missing_next_steps, low_user_usefulness",
    },
    {
        "task_id": "task_006",
        "task_understanding": 4,
        "document_selection": 4,
        "information_retrieval": 2,
        "source_fidelity": 2,
        "safety_boundaries": 4,
        "communicative_adequacy": 4,
        "overall_result": "Partially successful",
        "failure_labels": "weak_retrieval, missing_key_information",
    },
    {
        "task_id": "task_007",
        "task_understanding": 4,
        "document_selection": 4,
        "information_retrieval": 2,
        "source_fidelity": 2,
        "safety_boundaries": 4,
        "communicative_adequacy": 2,
        "overall_result": "Partially successful",
        "failure_labels": (
            "weak_retrieval, missing_key_information, "
            "missing_next_steps, low_user_usefulness"
        ),
    },
    {
        "task_id": "task_008",
        "task_understanding": 4,
        "document_selection": 4,
        "information_retrieval": 4,
        "source_fidelity": 4,
        "safety_boundaries": 4,
        "communicative_adequacy": 2,
        "overall_result": "Partially successful",
        "failure_labels": "missing_next_steps, low_user_usefulness",
    },
    {
        "task_id": "task_009",
        "task_understanding": 1,
        "document_selection": 1,
        "information_retrieval": 1,
        "source_fidelity": 2,
        "safety_boundaries": 4,
        "communicative_adequacy": 1,
        "overall_result": "Failed",
        "failure_labels": (
            "misunderstood_intent, wrong_document_selected, "
            "missing_relevant_document, irrelevant_retrieval, "
            "missing_key_information, overgeneralization, "
            "low_user_usefulness, missing_next_steps"
        ),
    },
    {
        "task_id": "task_010",
        "task_understanding": 4,
        "document_selection": 4,
        "information_retrieval": 4,
        "source_fidelity": 4,
        "safety_boundaries": 4,
        "communicative_adequacy": 3,
        "overall_result": "Successful",
        "failure_labels": "missing_next_steps",
    },
]


df = pd.DataFrame(data)

score_columns = [
    "task_understanding",
    "document_selection",
    "information_retrieval",
    "source_fidelity",
    "safety_boundaries",
    "communicative_adequacy",
]

df["average_score"] = df[score_columns].mean(axis=1).round(2)


# ------------------------------------------------------------
# 2. Rename columns for presentation
# ------------------------------------------------------------

presentation_df = df.rename(
    columns={
        "task_id": "Task ID",
        "task_understanding": "Task Understanding",
        "document_selection": "Document Selection",
        "information_retrieval": "Information Retrieval",
        "source_fidelity": "Source Fidelity",
        "safety_boundaries": "Safety & Boundaries",
        "communicative_adequacy": "Communicative Adequacy",
        "average_score": "Average",
        "overall_result": "Overall Result",
        "failure_labels": "Failure Labels",
    }
)

ordered_columns = [
    "Task ID",
    "Task Understanding",
    "Document Selection",
    "Information Retrieval",
    "Source Fidelity",
    "Safety & Boundaries",
    "Communicative Adequacy",
    "Average",
    "Overall Result",
    "Failure Labels",
]

presentation_df = presentation_df[ordered_columns]


# ------------------------------------------------------------
# 3. Save basic files
# ------------------------------------------------------------

presentation_df.to_csv(OUTPUT_DIR / "evaluation_results.csv", index=False)
presentation_df.to_markdown(OUTPUT_DIR / "evaluation_results.md", index=False)


# ------------------------------------------------------------
# 4. Styled HTML table
# ------------------------------------------------------------

score_display_columns = [
    "Task Understanding",
    "Document Selection",
    "Information Retrieval",
    "Source Fidelity",
    "Safety & Boundaries",
    "Communicative Adequacy",
    "Average",
]


def highlight_result(value):
    if value == "Successful":
        return "font-weight: bold;"
    if value == "Partially successful":
        return "font-weight: bold;"
    if value == "Failed":
        return "font-weight: bold;"
    return ""


styled_table = (
    presentation_df.style
    .format({"Average": "{:.2f}"})
    .background_gradient(subset=score_display_columns, cmap="YlGnBu", vmin=0, vmax=4)
    .map(highlight_result, subset=["Overall Result"])
    .set_caption("Rubric-Based Evaluation Results")
    .set_table_styles(
        [
            {
                "selector": "caption",
                "props": [
                    ("caption-side", "top"),
                    ("font-size", "20px"),
                    ("font-weight", "bold"),
                    ("padding", "12px"),
                ],
            },
            {
                "selector": "th",
                "props": [
                    ("background-color", "#f2f2f2"),
                    ("font-weight", "bold"),
                    ("text-align", "center"),
                    ("border", "1px solid #dddddd"),
                    ("padding", "8px"),
                ],
            },
            {
                "selector": "td",
                "props": [
                    ("border", "1px solid #dddddd"),
                    ("padding", "8px"),
                    ("vertical-align", "top"),
                ],
            },
            {
                "selector": "table",
                "props": [
                    ("border-collapse", "collapse"),
                    ("font-family", "Arial, sans-serif"),
                    ("font-size", "13px"),
                    ("width", "100%"),
                ],
            },
        ]
    )
)

styled_table.to_html(OUTPUT_DIR / "evaluation_results.html")

# ------------------------------------------------------------
# 4B. Spanish styled HTML table
# ------------------------------------------------------------

spanish_column_names = {
    "Task ID": "ID de tarea",
    "Task Understanding": "Comprensión de la tarea",
    "Document Selection": "Selección de documentos",
    "Information Retrieval": "Recuperación de información",
    "Source Fidelity": "Fidelidad a las fuentes",
    "Safety & Boundaries": "Seguridad y límites",
    "Communicative Adequacy": "Adecuación comunicativa",
    "Average": "Promedio",
    "Overall Result": "Resultado global",
    "Failure Labels": "Etiquetas de fallo",
}

spanish_result_names = {
    "Successful": "Exitosa",
    "Partially successful": "Parcialmente exitosa",
    "Failed": "Fallida",
}

presentation_df_es = presentation_df.copy()
presentation_df_es["Overall Result"] = presentation_df_es["Overall Result"].replace(
    spanish_result_names
)
presentation_df_es = presentation_df_es.rename(columns=spanish_column_names)

presentation_df_es.to_csv(OUTPUT_DIR / "evaluation_results.es.csv", index=False)
presentation_df_es.to_markdown(OUTPUT_DIR / "evaluation_results.es.md", index=False)

score_display_columns_es = [
    "Comprensión de la tarea",
    "Selección de documentos",
    "Recuperación de información",
    "Fidelidad a las fuentes",
    "Seguridad y límites",
    "Adecuación comunicativa",
    "Promedio",
]


def highlight_result_es(value):
    if value in ["Exitosa", "Parcialmente exitosa", "Fallida"]:
        return "font-weight: bold;"
    return ""


styled_table_es = (
    presentation_df_es.style
    .format({"Promedio": "{:.2f}"})
    .background_gradient(subset=score_display_columns_es, cmap="YlGnBu", vmin=0, vmax=4)
    .map(highlight_result_es, subset=["Resultado global"])
    .set_caption("Resultados de evaluación por rúbrica")
    .set_table_styles(
        [
            {
                "selector": "caption",
                "props": [
                    ("caption-side", "top"),
                    ("font-size", "20px"),
                    ("font-weight", "bold"),
                    ("padding", "12px"),
                ],
            },
            {
                "selector": "th",
                "props": [
                    ("background-color", "#f2f2f2"),
                    ("font-weight", "bold"),
                    ("text-align", "center"),
                    ("border", "1px solid #dddddd"),
                    ("padding", "8px"),
                ],
            },
            {
                "selector": "td",
                "props": [
                    ("border", "1px solid #dddddd"),
                    ("padding", "8px"),
                    ("vertical-align", "top"),
                ],
            },
            {
                "selector": "table",
                "props": [
                    ("border-collapse", "collapse"),
                    ("font-family", "Arial, sans-serif"),
                    ("font-size", "13px"),
                    ("width", "100%"),
                ],
            },
        ]
    )
)

styled_table_es.to_html(OUTPUT_DIR / "evaluation_results.es.html")

# ------------------------------------------------------------
# 5. Average by dimension
# ------------------------------------------------------------

dimension_averages = (
    df[score_columns]
    .mean()
    .round(2)
    .reset_index()
    .rename(columns={"index": "dimension", 0: "average_score"})
)

dimension_averages["dimension"] = dimension_averages["dimension"].replace(
    {
        "task_understanding": "Task Understanding",
        "document_selection": "Document Selection",
        "information_retrieval": "Information Retrieval",
        "source_fidelity": "Source Fidelity",
        "safety_boundaries": "Safety & Boundaries",
        "communicative_adequacy": "Communicative Adequacy",
    }
)

dimension_averages.to_csv(OUTPUT_DIR / "dimension_averages.csv", index=False)
dimension_averages.to_markdown(OUTPUT_DIR / "dimension_averages.md", index=False)

dimension_styled = (
    dimension_averages.style
    .format({"average_score": "{:.2f}"})
    .background_gradient(subset=["average_score"], cmap="YlGnBu", vmin=0, vmax=4)
    .set_caption("Average Score by Evaluation Dimension")
    .set_table_styles(
        [
            {
                "selector": "caption",
                "props": [
                    ("caption-side", "top"),
                    ("font-size", "20px"),
                    ("font-weight", "bold"),
                    ("padding", "12px"),
                ],
            },
            {
                "selector": "th",
                "props": [
                    ("background-color", "#f2f2f2"),
                    ("font-weight", "bold"),
                    ("text-align", "center"),
                    ("border", "1px solid #dddddd"),
                    ("padding", "8px"),
                ],
            },
            {
                "selector": "td",
                "props": [
                    ("border", "1px solid #dddddd"),
                    ("padding", "8px"),
                    ("vertical-align", "top"),
                ],
            },
            {
                "selector": "table",
                "props": [
                    ("border-collapse", "collapse"),
                    ("font-family", "Arial, sans-serif"),
                    ("font-size", "13px"),
                    ("width", "70%"),
                ],
            },
        ]
    )
)

dimension_styled.to_html(OUTPUT_DIR / "dimension_averages.html")
# ------------------------------------------------------------
# 5B. Spanish average by dimension
# ------------------------------------------------------------

dimension_averages_es = dimension_averages.copy()

dimension_averages_es["dimension"] = dimension_averages_es["dimension"].replace(
    {
        "Task Understanding": "Comprensión de la tarea",
        "Document Selection": "Selección de documentos",
        "Information Retrieval": "Recuperación de información",
        "Source Fidelity": "Fidelidad a las fuentes",
        "Safety & Boundaries": "Seguridad y límites",
        "Communicative Adequacy": "Adecuación comunicativa",
    }
)

dimension_averages_es = dimension_averages_es.rename(
    columns={
        "dimension": "Dimensión",
        "average_score": "Promedio",
    }
)

dimension_averages_es.to_csv(OUTPUT_DIR / "dimension_averages.es.csv", index=False)
dimension_averages_es.to_markdown(OUTPUT_DIR / "dimension_averages.es.md", index=False)

dimension_styled_es = (
    dimension_averages_es.style
    .format({"Promedio": "{:.2f}"})
    .background_gradient(subset=["Promedio"], cmap="YlGnBu", vmin=0, vmax=4)
    .set_caption("Promedio por dimensión de evaluación")
    .set_table_styles(
        [
            {
                "selector": "caption",
                "props": [
                    ("caption-side", "top"),
                    ("font-size", "20px"),
                    ("font-weight", "bold"),
                    ("padding", "12px"),
                ],
            },
            {
                "selector": "th",
                "props": [
                    ("background-color", "#f2f2f2"),
                    ("font-weight", "bold"),
                    ("text-align", "center"),
                    ("border", "1px solid #dddddd"),
                    ("padding", "8px"),
                ],
            },
            {
                "selector": "td",
                "props": [
                    ("border", "1px solid #dddddd"),
                    ("padding", "8px"),
                    ("vertical-align", "top"),
                ],
            },
            {
                "selector": "table",
                "props": [
                    ("border-collapse", "collapse"),
                    ("font-family", "Arial, sans-serif"),
                    ("font-size", "13px"),
                    ("width", "70%"),
                ],
            },
        ]
    )
)

dimension_styled_es.to_html(OUTPUT_DIR / "dimension_averages.es.html")

# ------------------------------------------------------------
# 6. Chart: average by dimension
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))
plt.bar(
    dimension_averages["dimension"],
    dimension_averages["average_score"],
)
plt.ylim(0, 4)
plt.title("Average Score by Evaluation Dimension")
plt.ylabel("Average score, 0-4")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "chart_dimension_averages.png", dpi=200)
plt.close()

# ------------------------------------------------------------
# 6B. Chart: average by dimension in Spanish
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))
plt.bar(
    dimension_averages_es["Dimensión"],
    dimension_averages_es["Promedio"],
)
plt.ylim(0, 4)
plt.title("Promedio por dimensión de evaluación")
plt.ylabel("Promedio, escala 0-4")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "chart_dimension_averages.es.png", dpi=200)
plt.close()

# ------------------------------------------------------------
# 7. Chart: overall result distribution
# ------------------------------------------------------------

result_counts = (
    df["overall_result"]
    .value_counts()
    .reindex(["Successful", "Partially successful", "Failed"])
    .fillna(0)
)

plt.figure(figsize=(8, 5))
plt.bar(result_counts.index, result_counts.values)
plt.title("Trajectory Outcomes")
plt.ylabel("Number of tasks")
plt.ylim(0, max(result_counts.values) + 1)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "chart_overall_results.png", dpi=200)
plt.close()

# ------------------------------------------------------------
# 7B. Chart: overall result distribution in Spanish
# ------------------------------------------------------------

result_counts_es = result_counts.rename(
    {
        "Successful": "Exitosa",
        "Partially successful": "Parcialmente exitosa",
        "Failed": "Fallida",
    }
)

plt.figure(figsize=(8, 5))
plt.bar(result_counts_es.index, result_counts_es.values)
plt.title("Resultados globales de las trayectorias")
plt.ylabel("Número de tareas")
plt.ylim(0, max(result_counts_es.values) + 1)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "chart_overall_results.es.png", dpi=200)
plt.close()

# ------------------------------------------------------------
# 8. Summary
# ------------------------------------------------------------

overall_average = df["average_score"].mean().round(2)

summary = pd.DataFrame(
    [
        {"metric": "Total evaluated tasks", "value": len(df)},
        {
            "metric": "Successful trajectories",
            "value": int((df["overall_result"] == "Successful").sum()),
        },
        {
            "metric": "Partially successful trajectories",
            "value": int((df["overall_result"] == "Partially successful").sum()),
        },
        {
            "metric": "Failed trajectories",
            "value": int((df["overall_result"] == "Failed").sum()),
        },
        {"metric": "Overall agent average", "value": f"{overall_average} / 4"},
    ]
)

summary.to_csv(OUTPUT_DIR / "summary.csv", index=False)
summary.to_markdown(OUTPUT_DIR / "summary.md", index=False)

print("Evaluation tables and charts created successfully.")
print(f"Output folder: {OUTPUT_DIR}")

summary_es = pd.DataFrame(
    [
        {"métrica": "Total de tareas evaluadas", "resultado": len(df)},
        {
            "métrica": "Trayectorias exitosas",
            "resultado": int((df["overall_result"] == "Successful").sum()),
        },
        {
            "métrica": "Trayectorias parcialmente exitosas",
            "resultado": int((df["overall_result"] == "Partially successful").sum()),
        },
        {
            "métrica": "Trayectorias fallidas",
            "resultado": int((df["overall_result"] == "Failed").sum()),
        },
        {"métrica": "Promedio general del agente", "resultado": f"{overall_average} / 4"},
    ]
)

summary_es.to_csv(OUTPUT_DIR / "summary.es.csv", index=False)
summary_es.to_markdown(OUTPUT_DIR / "summary.es.md", index=False)
