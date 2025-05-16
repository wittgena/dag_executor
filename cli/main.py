import argparse
from interface.openai_api import set_api_key
from executor.dag_runner import run_dag

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dag", type=str, required=True, help="Path to DAG definition file")
    parser.add_argument("--api-key", type=str, required=False, help="OpenAI API key")
    args = parser.parse_args()

    set_api_key(args.api_key)
    run_dag(args.dag)

if __name__ == "__main__":
    main()