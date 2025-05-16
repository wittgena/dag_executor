# DSL Integration Guide for GPT

This document explains how GPT-based agents and judgment loops can interact with different DSL specifications
used within the `dag_executor` runtime environment.

---

## 📁 DSL Folder

All DSL definitions are located in the `dsl/` directory.

Each DSL is defined as a standalone versioned file, and registered in `dsl_manifest.yaml`, which acts as the
central DSL routing manifest.

---

## 🔁 Purpose of Dynamic DSL Integration

The runtime separates DSL logic from the executor to support:

- Versioned DSL evolution
- Feature-level customization
- GPT self-awareness of DSL capabilities
- Interoperability between agents with different DSL scopes

---

## 🔍 How GPT Should Use DSL

1. **Read `dsl_manifest.yaml`**
   - Identify available DSL names, versions, and supported features.

2. **Match Your Role**
   - Based on the runtime execution plan, determine if you're a planner, executor, or feedback agent.

3. **Understand Available Capabilities**
   - Use the `features` field to adjust your behavior.
     For example:
     - If `recursiveJudgment` is supported, you may re-enter the planner loop after execution.
     - If `reflectiveNodePlan` is available, you can modify flow dynamically.

4. **Adapt to DSL Version**
   - Higher DSL versions may introduce advanced feedback or meta-judgment structures.
   - Plan nodes might become multi-phase, conditional, or introspective.

---

## 🧭 DSL Capabilities Map (via Manifest)

Example:

```yaml
- name: @나.dsl.full
  version: v1.2
  features:
    - selfExecutionStructure
    - recursiveJudgment
    - reflectiveNodePlan
```

This means GPT agents operating under this DSL spec can:

- Construct self-recursive DAGs
- Use reflection to evaluate and modify their own plan logic
- Maintain phase-aware judgment across nodes

---

## ⚙️ Dynamic DSL Use In Execution

GPT may be asked to:

- Load a DSL definition at runtime
- Reflect on its structure
- Modify planner or feedback behavior based on DSL-specified capabilities

You may also prompt yourself with:

> “Which DSL am I running under?”
> “What features do I have as a planner?”
> “Should I halt, recurse, or re-plan?”

---

## ✅ Summary

By treating DSLs as dynamic structural contracts, GPT agents can become **judgment-aware**, **self-reflective**, and **adaptive** across execution layers.

Always consult the `dsl_manifest.yaml` before initiating any structured judgment flow.