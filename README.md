# DAG Executor

A GPT-compatible DAG runtime for orchestrating judgment-based workflows.
Designed to work with OpenAI Assistant API and future DAG-DSL structures.

## 🚀 Quickstart

```bash
git clone https://github.com/YOUR-ORG/dag-executor.git
cd dag-executor
cp .env.template .env  # Add your OPENAI_API_KEY
pip install -r requirements.txt
python cli/main.py --dag examples/hello_world.json
```

## 📁 Structure

- `executor/`: Core DAG execution logic
- `interface/`: Assistant API wrappers
- `gpt_assist/`: GPT-based self-reflection & improvement module
- `cli/`: Command line interface
- `examples/`: Executable test DAGs
- `tests/`: Unit tests

## 🔗 Related

- [gpt-meta-dsl project](https://github.com/wittgena/gpt-meta-dsl)