# dag.dsl.threadSpec.v1

## 🎯 목적
이 문서는 `dag.dsl`이 GPT judgment 기반 실행 구조를 갖추기 위해,  
Plan / Work / Feedback 흐름을 구조적으로 분리하고 DSL 상에서 명확히 표현할 수 있는 기준을 정의한다.

---

## 🧩 전체 개요

dag.dsl은 단순한 순차 실행이 아니라 다음 3종류의 judgment thread를 분화하여 관리함으로써  
GPT를 판단자(planner)로, 외부 실행기를 실행자(worker)로 구성한다.

```
[plan] → [work1, work2, ..., workN] → [feedback] → (plan 재귀 or 종료)
```

---

## 🧠 Thread 분화 정의

### 1. Plan Thread

- 역할: GPT judgment를 호출하여 DAG를 설계하거나 흐름을 재조정
- 실행자: GPT (Assistant API, role: planner)
- DSL 명시:
```dsl
node(plan_phase) {
  type: plan
  model: gpt-4o
  prompt: "Given the task spec and prior results, plan the next step."
  input: memory.task_context
  output: dag
}
```

### 2. Work Thread

- 역할: GPT 또는 외부 tool로 node별 작업 수행
- 실행자: API/tool-caller 또는 GPT (role: executor)
- DSL 명시:
```dsl
node(work_A) {
  type: work
  action: assistant("complete task A")
  retry: 2
  on_fail: node(fallback)
}
```

### 3. Feedback Thread

- 역할: 여러 work 결과를 통합하고 다음 판단 흐름(plan)을 호출할지 판단
- 실행자: 구조 집계기 또는 GPT (judgment router)
- DSL 명시:
```dsl
node(feedback) {
  type: feedback
  merge: [work_A.result, work_B.result]
  to: node(plan_phase)
  if: "work_A.result.status == success"
}
```

---

## 🔁 재귀 판단 흐름

```dsl
node(plan_phase) {
  type: plan
  recurse_if: node(feedback).signal == "retry"
}
```

---

## ✅ 흐름 예시: DSL 구조

```dsl
dag {
  node(init_plan) {
    type: plan
    model: gpt-4o
    output: dag
  }

  node(work_1) {
    type: work
    action: assistant("step 1")
  }

  node(work_2) {
    type: work
    action: assistant("step 2")
  }

  node(feedback) {
    type: feedback
    merge: [work_1.result, work_2.result]
    to: node(init_plan)
  }
}
```

---

## 📌 설계 원칙

- 흐름은 항상 [plan → work → feedback → (plan)] 순환을 기준으로 구성
- work은 병렬 가능, plan/feedback은 단일 판단 루프 유지
- feedback은 상태 기반 판단(merge, conditional branch, halt 등)을 명시해야 함
- 모든 judgment 흐름은 GPT에 의해 수행되며, 외부 실행기는 DSL을 정확히 분해하고 호출 가능해야 함

---

## 🧭 향후 확장 예정

- `type: loop`, `type: observer`, `type: fallback_group` 등 메타노드 유형
- node 간 signal 기반 judgment routing 확장
- memory / result context 자동 전달 스펙