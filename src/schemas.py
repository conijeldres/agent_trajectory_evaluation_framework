from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional


@dataclass
class AgentStep:
    step_id: int
    action: str
    reasoning: str
    tool_name: Optional[str] = None
    tool_input: Optional[str] = None
    tool_output: Optional[Any] = None


@dataclass
class AgentTrace:
    task_id: str
    user_query: str
    detected_intent: str
    selected_documents: List[str]
    steps: List[AgentStep]
    final_response: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "user_query": self.user_query,
            "detected_intent": self.detected_intent,
            "selected_documents": self.selected_documents,
            "steps": [asdict(step) for step in self.steps],
            "final_response": self.final_response,
        }
