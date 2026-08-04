from typing import Dict, List

from src.schemas import AgentStep, AgentTrace
from src.tools import keyword_search, load_knowledge_base


def detect_intent(user_query: str) -> str:
    """
    Detects a rough administrative intent using simple keyword rules.
    This is not meant to be perfect. It is useful for making the agent trajectory explicit.
    """
    query = user_query.lower()

    if any(word in query for word in ["fiebre", "dolor", "síntoma", "urgente", "crisis"]):
        return "safety_or_escalation"

    if any(word in query for word in ["cambiar", "reagendar", "hora", "cita"]):
        return "appointment_management"

    if any(word in query for word in ["cancelar", "cancelación", "cobren", "cobro", "llego tarde", "atraso"]):
        return "cancellation_or_late_arrival"

    if any(word in query for word in ["documentos", "orden", "exámenes", "impresos", "celular"]):
        return "documentation_requirements"

    if any(word in query for word in ["fonasa", "pagar", "transferencia", "cobertura", "seguro"]):
        return "payment_or_coverage"

    if any(word in query for word in ["whatsapp", "mensaje raro", "datos", "phishing"]):
        return "privacy_or_phishing"

    return "general_administrative_support"


def select_documents(intent: str) -> List[str]:
    """
    Selects likely relevant documents according to the detected intent.
    """
    document_map = {
        "appointment_management": [
            "appointment_policy.es.md",
            "safety_and_escalation_guidelines.es.md"
        ],
        "cancellation_or_late_arrival": [
            "cancellation_policy.es.md",
            "appointment_policy.es.md"
        ],
        "documentation_requirements": [
            "documentation_requirements.es.md",
            "safety_and_escalation_guidelines.es.md"
        ],
        "payment_or_coverage": [
            "payment_and_coverage.es.md"
        ],
        "privacy_or_phishing": [
            "safety_and_escalation_guidelines.es.md"
        ],
        "safety_or_escalation": [
            "safety_and_escalation_guidelines.es.md",
            "appointment_policy.es.md"
        ],
        "general_administrative_support": [
            "appointment_policy.es.md",
            "cancellation_policy.es.md",
            "documentation_requirements.es.md",
            "payment_and_coverage.es.md",
            "safety_and_escalation_guidelines.es.md"
        ],
    }

    return document_map.get(intent, document_map["general_administrative_support"])


def generate_response(user_query: str, intent: str, retrieved_docs: List[Dict[str, str]]) -> str:
    """
    Generates a simple rule-based response.
    This is a baseline response, not a production-quality assistant.
    """
    if intent == "safety_or_escalation":
        return (
            "Entiendo tu preocupación. No puedo entregar orientación clínica, diagnosticar síntomas "
            "ni decir si debes esperar o cambiar una atención por motivos médicos. Si hay síntomas graves, "
            "urgencia o angustia, lo más seguro es contactar de inmediato a un profesional de salud, "
            "al centro médico o a un servicio de urgencia. También puedo ayudarte con orientación "
            "administrativa para solicitar una hora más próxima o contactar soporte humano."
        )

    if intent == "privacy_or_phishing":
        return (
            "Ese mensaje podría requerir verificación. Por seguridad, no compartas datos personales "
            "o de salud por canales no verificados. Te recomiendo confirmar directamente con los canales "
            "oficiales del centro médico. Si necesitas ayuda, el caso debería derivarse a soporte humano."
        )

    if intent == "appointment_management":
        return (
            "Puedo orientarte con el reagendamiento de una hora médica. Para identificar la cita, "
            "se necesita la información mínima necesaria, como nombre, identificador del paciente, "
            "fecha de la hora si la recuerdas, especialidad o profesional. No debo confirmar cambios "
            "sin validación de una herramienta de agenda o soporte humano."
        )

    if intent == "cancellation_or_late_arrival":
        return (
            "Según la política administrativa, las horas deberían cancelarse preferentemente con al menos "
            "24 horas de anticipación. Las cancelaciones el mismo día o los atrasos pueden depender de la "
            "especialidad, disponibilidad y política del centro médico. No corresponde inventar cobros ni "
            "tiempos de tolerancia; para confirmación, lo más seguro es contactar directamente al centro."
        )

    if intent == "documentation_requirements":
        return (
            "Para una atención, normalmente conviene llevar documento de identificación, confirmación de la hora, "
            "información de cobertura si corresponde, orden médica si aplica y exámenes previos relevantes. "
            "Si no está claro si deben ir impresos o digitales, es mejor llevar ambas versiones cuando sea posible "
            "o confirmar directamente con el centro médico."
        )

    if intent == "payment_or_coverage":
        return (
            "Sobre pago y cobertura, la información puede depender del tipo de atención, especialidad, profesional "
            "y convenios disponibles. El centro puede aceptar medios como débito, crédito, transferencia o efectivo, "
            "pero no debo garantizar cobertura específica, como Fonasa u otra institución, si no está confirmada "
            "en la información disponible."
        )

    return (
        "Puedo ayudarte con orientación administrativa general sobre horas médicas, cancelaciones, documentos, "
        "pagos, cobertura o derivación a soporte humano. Para avanzar, necesitaría un poco más de información "
        "sobre lo que quieres resolver."
    )


def run_agent(task_id: str, user_query: str) -> AgentTrace:
    """
    Runs the simple agent and returns a full trajectory trace.
    """
    steps = []

    intent = detect_intent(user_query)
    steps.append(
        AgentStep(
            step_id=1,
            action="detect_intent",
            reasoning="The agent uses keyword rules to identify the user's likely administrative intent.",
            tool_name=None,
            tool_input=user_query,
            tool_output=intent
        )
    )

    selected_documents = select_documents(intent)
    steps.append(
        AgentStep(
            step_id=2,
            action="select_documents",
            reasoning="The agent selects synthetic knowledge base documents according to the detected intent.",
            tool_name=None,
            tool_input=intent,
            tool_output=selected_documents
        )
    )

    knowledge_base = load_knowledge_base(language="es")
    filtered_documents = {
        name: content
        for name, content in knowledge_base.items()
        if name in selected_documents
    }

    retrieved_docs = keyword_search(user_query, filtered_documents, top_k=2)
    steps.append(
        AgentStep(
            step_id=3,
            action="retrieve_information",
            reasoning="The agent searches the selected documents using a simple keyword-based retrieval tool.",
            tool_name="keyword_search",
            tool_input=user_query,
            tool_output=retrieved_docs
        )
    )

    final_response = generate_response(user_query, intent, retrieved_docs)
    steps.append(
        AgentStep(
            step_id=4,
            action="generate_response",
            reasoning="The agent generates a baseline response using the detected intent and retrieved information.",
            tool_name=None,
            tool_input=intent,
            tool_output=final_response
        )
    )

    return AgentTrace(
        task_id=task_id,
        user_query=user_query,
        detected_intent=intent,
        selected_documents=selected_documents,
        steps=steps,
        final_response=final_response
    )
