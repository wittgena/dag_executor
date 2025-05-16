# dag.dsl ↔ dag_executor.runtime 매핑 테이블 (v0.2 기준)

이 문서는 `dag.dsl.threadSpec.v1`을 기준으로, DSL 내 주요 type 요소와  
`dag_executor` 내 실행기 구조 간의 정합성과 매핑 관계를 설명합니다.

---

## 📊 DSL ↔ Runtime Module Mapping

| `dag.dsl` 요소 | 의미 | 매핑되는 `dag_executor` 모듈 | 정합성 평가 | 개선 필요 사항 |
|----------------|------|-------------------------------|----------------|-------------------|
| `type: plan` | GPT judgment를 호출하여 DAG 계획을 구성 | ❌ 없음 (`planner.py` 필요) | ⚠️ 없음 | GPT 호출 기반 plan 모듈 필요 |
| `type: work` | node 실행, GPT 또는 tool-call 수행 | ✅ `executor/dag_runner.py` + `interface/openai_api.py` | ✅ 정합 | DSL 파싱에 `type` 기준 분기 필요 |
| `type: feedback` | 여러 work 결과 종합, 다음 판단 결정 | ❌ 없음 (`result_router.py`) | ⚠️ 없음 | 결과 수집 및 plan 트리거 기능 필요 |
| `on_fail`, `retry`, `recurse_if` | 흐름 조건 분기 및 재귀 판단자 트리거 | ⚠️ `dag_runner.py` 부분 구현 | ⚠️ 부분 정합 | 상태 추적 + 조건 분기 처리 강화 필요 |
| `memory.*` | 실행결과 및 판단 맥락 저장/재사용 | ❌ 없음 (`memory.py`) | ❌ 없음 | 최소 judgment memory 구조 필요 |
| `action: assistant(...)` | GPT API 호출 실행 노드 | ✅ `interface/openai_api.py` | ✅ 정합 | 파라미터 커스터마이징 추가 필요 |
| `merge: [...]`, `to: node(...)` | feedback 결과 병합 후 흐름 제어 | ⚠️ 구조 없음 | ⚠️ 미정 | feedback → plan 루트 전환기 필요 |
| `dag {...}` | 전체 DAG 정의 | ✅ DSL 파싱 구조 대응 | ✅ 정합 | validator 강화 필요 (구조 논리성 포함) |

---

## 🔧 개선 우선순위

| 순위 | 필요 모듈 | 설명 |
|------|------------|------|
| ① | `planner.py` | GPT 기반 judgment → DAG plan |
| ② | `result_router.py` | Work 결과를 평가하고 Plan thread로 전달 |
| ③ | `memory.py` | 결과 및 판단 context 저장소 |
| ④ | `dag_dsl_parser.py` 확장 | DSL `type:` 구문 기반 실행 모듈 연결 |
| ⑤ | `examples/plan_work_feedback.json` | 최소 구조 예제 DAG 파일 작성 필요 |

---

## ✅ 구조 정합성 평가 요약

| 항목 | 점수 (100점 기준) |
|------|-------------------|
| Plan Thread 대응 | 18 / 30 |
| Work Thread 대응 | 28 / 30 |
| Feedback 구조 대응 | 14 / 20 |
| DSL → 모듈 매핑 구조 | 15 / 20 |
| **총점** | **75 / 100** |

---

이 매핑 표는 `dag.dsl`의 판단 흐름을 외부 실행기에서 구현하는 데 있어  
`dag_executor`가 어떤 구성 요소를 이미 갖추고 있으며,  
어디를 확장해야 judgment runtime으로 완성되는지를 보여줍니다.