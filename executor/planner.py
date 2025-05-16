# planner.py
# Plan Thread 실행기 – GPT judgment를 기반으로 DAG 흐름 설계

from interface.openai_api import call_gpt

def plan_from_input(task_description: str, context: dict = None) -> dict:
    prompt = f"""You are a planner. Given the following task, create a DAG plan.
Task: {task_description}
Context: {context if context else "None"}
Please respond in JSON format with nodes and edges.
"""
    return call_gpt(prompt, model="gpt-4o")  # Expects JSON-formatted DAG