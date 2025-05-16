# dag_executor.structure.for.gpt.md

## 🧠 목적

이 문서는 GPT 또는 GPT 기반 에이전트가 `dag_executor` 실행기 구조를 정확히 이해하고,  
자기 개선(self-improvement) 또는 판단 흐름을 조작할 수 있도록 하기 위한 **모듈 구조 안내서**입니다.

---

## 📁 폴더별 구조 및 GPT의 인식 가이드

### 1. `planner/`

- 역할: GPT judgment 흐름 생성
- GPT는 이 폴더 내의 코드를 통해 **DAG를 생성하거나 수정**할 수 있음
- 진입 함수 예시:
  ```python
  planner.plan_from_input(task_description, context)
  ```

### 2. `executor/`

- 역할: 개별 노드를 실행하는 실행기
- GPT는 이 구조를 통해 **작업 요청(task execution)**을 외부 API에 전달하거나, GPT 자신이 실행자 역할을 할 수 있음
- GPT는 `dag_runner.py`에서 `type: work` 노드를 처리함

### 3. `router/`

- 역할: Work 결과를 모아서 판단 후 다음 흐름을 결정 (Plan, Replan, Halt)
- GPT는 이 경로를 통해 **실행 결과를 분석하고 다음 흐름을 판단**해야 함
- GPT는 `route_feedback(results)` 함수를 사용하여 분기 판단을 내릴 수 있음

### 4. `memory/`

- 역할: 판단 결과, 상태, 흐름 메모리 저장
- GPT는 이 저장소를 참조하여 **이전 판단을 복기하거나, 흐름을 컨텍스트로 연결** 가능
- GPT는 `memory.save_result(node_id, result)` 형태로 호출 가능

### 5. `parser/`

- 역할: DSL을 분석하여 실행 흐름(plan/work/feedback)을 모듈로 분기
- GPT는 DSL을 읽을 때, `dag_dsl_parser.py`를 통해 **자신이 어느 역할인지** 파악할 수 있음

### 6. `interface/`

- 역할: Assistant API 또는 외부 도구 호출
- GPT는 여기서 자신의 **실제 호출 방식, 토큰 사용량, 모델 종류** 등을 간접 제어 가능

### 7. `gpt_assist/` (선택)

- 역할: GPT가 자신의 코드/구조를 재귀적으로 분석하고 PR 또는 개선을 제안하는 루프
- GPT는 여기서 자기 자신의 동작을 평가할 수 있음

---

## 🧭 GPT 실행 루프의 흐름 요약

```text
[planner] → generate DAG from spec
 → [parser] → resolve type → [executor/work] or [router/feedback]
 → [router] → decide → call [planner] again (if needed)
```

---

## 📌 구조적 메타 판단 시 유의사항

- GPT는 `type: plan` 노드만 판단자 역할을 수행함
- GPT는 `feedback` 노드를 통해 자기 실행 결과를 검토할 수 있음
- GPT는 memory를 통해 상태 기반 판단을 할 수 있음 (예: retry cutoff, node history)

---

## 🔁 GPT 개선 루프 예시

1. GPT가 실행기를 통해 DAG 실행
2. 결과가 memory에 저장됨
3. GPT는 `gpt_assist/self_review_agent.py`를 호출해 개선사항을 평가
4. `planner.py` 또는 `router.py`를 수정할 PR 제안

---

## ✅ GPT를 위한 Best Practices

- 각 폴더의 역할을 구조적으로 구분하여 판단
- `type:` 기반 DSL을 정확히 분석하고 자기 위치 인식
- planner → executor → feedback → planner의 순환 구조를 유지

---

이 문서는 GPT 기반 judgment 흐름의 외부화 및 구조적 실행을 위한 인식 프레임을 제공합니다.