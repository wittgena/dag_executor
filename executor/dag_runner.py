import json

def run_dag(path):
    with open(path) as f:
        dag = json.load(f)
    print("[DAG Executor] Running DAG with nodes:")
    for node in dag.get("nodes", []):
        print(" -", node["id"])