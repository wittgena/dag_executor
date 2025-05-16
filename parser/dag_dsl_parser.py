# dag_dsl_parser.py
# DSL 파서 – type: plan/work/feedback에 따라 실행 모듈 분기

import json

def parse_dsl(path: str) -> list:
    with open(path) as f:
        dag = json.load(f)
    execution_plan = []
    for node in dag.get("nodes", []):
        node_type = node.get("type")
        if node_type == "plan":
            execution_plan.append(("plan", node))
        elif node_type == "work":
            execution_plan.append(("work", node))
        elif node_type == "feedback":
            execution_plan.append(("feedback", node))
    return execution_plan