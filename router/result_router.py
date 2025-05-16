# result_router.py
# Feedback Thread 실행기 – 여러 work 결과를 통합하고 plan 재실행 여부 판단

def route_feedback(results: dict) -> str:
    """
    Evaluates node results and returns next step signal:
    - "continue": proceed to next work
    - "replan": return to planner
    - "halt": end execution
    """
    if any(r.get("status") == "failed" for r in results.values()):
        return "replan"
    if all(r.get("status") == "success" for r in results.values()):
        return "continue"
    return "halt"