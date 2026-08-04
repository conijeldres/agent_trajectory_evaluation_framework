import json
from pathlib import Path

from src.agent import run_agent


TASKS_PATH = Path("data/tasks_spanish_healthcare_admin.jsonl")
TRACES_PATH = Path("traces")


def load_tasks():
    tasks = []

    with TASKS_PATH.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                tasks.append(json.loads(line))

    return tasks


def save_trace(trace):
    TRACES_PATH.mkdir(exist_ok=True)

    output_path = TRACES_PATH / f"{trace.task_id}_trace.json"

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(trace.to_dict(), file, ensure_ascii=False, indent=2)

    return output_path


def main():
    tasks = load_tasks()

    for task in tasks:
        trace = run_agent(
            task_id=task["task_id"],
            user_query=task["user_query"]
        )

        output_path = save_trace(trace)
        print(f"Saved trace: {output_path}")


if __name__ == "__main__":
    main()
