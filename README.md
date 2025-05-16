# DAG Executor

A GPT-compatible DAG runtime for orchestrating judgment-based workflows.  
This project is designed not only as an execution engine, but as a **structural reflection layer** that allows GPT to operate as a planner, executor, and feedback agent across recursive judgment loops.

---

## 🔁 What Makes This Project Unique?

Unlike typical GPT integrations or auto-code generation tools, this project:

- **Begins with GPT documentation**, not code. A `docs-for-gpt/` folder is maintained to guide GPT through structural self-awareness.
- **Separates plan/work/feedback threads** following a DSL judgment specification.
- **Enables recursive improvement**, allowing GPT to act as a planner, analyze its own outputs, and modify its DAG structure over time.

---

## 📁 Project Structure

```
dag_executor/
├── planner/        # Plan thread: GPT-based DAG judgment logic
├── executor/       # Work thread: task execution engine
├── router/         # Feedback thread: result routing and recursion
├── memory/         # Storage for results, context, retry states
├── parser/         # DSL interpreter (type-based routing)
├── gpt_assist/     # Self-review and code improvement agent (optional)
├── interface/      # Assistant API integration
├── examples/       # Example DAGs
├── tests/          # Basic unit tests
├── docs-for-gpt/   # 📄 Documents to help GPT understand structure
└── README.md
```

---

## 🧠 docs-for-gpt/

This directory is a core innovation in the development method:

> It lets GPT understand its **own runtime position and role** inside a multi-threaded judgment DAG system.

Included documents:
- `dag_executor.structure.for.gpt.md`
- `dag_executor.dsl_mapping_matrix.md`

GPT agents reading from this folder will understand how to:
- Differentiate plan/work/feedback roles
- Route themselves through recursive flows
- Contribute to system improvement as judgmental agents

---

## 🚀 Example Usage

```bash
dag-exec run --dag examples/hello_world.json --api-key $OPENAI_API_KEY
```

---

## 🧭 Roadmap

- [ ] Memory routing system
- [ ] DSL type validation and dynamic planner feedback
- [ ] GPT-assisted pull requests from judgment feedback

---

## License

MIT