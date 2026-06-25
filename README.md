# 🎯 Architect Mobile UI Automation Test Suite & Framework

> **게임 품질 확보 및 회귀 테스트 효율화를 위한 모바일 UI 자동화 테스트 프레임워크**
> 
> 본 프로젝트는 라이브 서비스 환경에서 발생할 수 있는 스킬 장착 및 강화 시스템의 결함을 사전 차단하기 위해 구축된 **테스트 자동화 스위트(Test Automation Suite)**입니다. **POM(Page Object Model)** 패턴을 기반으로 설계되었으며, 유동적인 게임 데이터 환경에 대응하는 **실시간 UI 인지형 동적 분기 기술**을 도입하여 테스트의 강건성(Robustness)을 극대화했습니다.

---

## 🛠️ Tech Stack & Environment

* **Language:** Python 3.x
* **Framework:** Airtest Framework (Aircv 이미지 매칭 구조)
* **Protocol:** ADB (Android Debug Bridge)

### 📱 Test Device Specifications
모바일 UI 및 이미지 매칭 자동화의 정확성을 보장하기 위해 아래의 단일 기준 디바이스 환경에서 테스트가 설계 및 검증되었습니다.

| 항목 (Component) | 스펙 상세 (Specifications) | 비고 (Note) |
| :--- | :--- | :--- |
| **Device Model** | Samsung Galaxy Series (스마트폰 실기기) | ADB USB Debugging 연동 |
| **OS Version** | Android 10 이상 (최신 One UI 환경) | 개발자 옵션 및 자동 보안 차단 해제 |
| **Screen Resolution**| **2340 x 1080 (FHD+)** | 스크립트 내 기준 해상도 |
| **Aspect Ratio** | 19.5 : 9 | 인게임 UI 레이아웃 정합성 기준 |
| **Capture Method** | Javacap / ADBCAP Mode | 미러링 및 스냅샷 인젝션 엔진 |
| **Touch Method** | MAXTOUCH | 디바이스 터치 컨트롤 드라이버 |

---

## 🚀 Key Features (QA Engineering Highlights)

* **POM (Page Object Model) 디자인 패턴 적용**
  * UI 요소(템플릿 이미지 객체) 및 캐릭터 조작 액션(`pages/`)과 실제 단언문 중심의 테스트 시나리오 레이어(`tests/`)를 완벽히 분리하여 유지보수 비용을 최소화했습니다.
* **실시간 UI 인지형 동적 분기 테스트 (Dynamic Conditional Testing)**
  * 유저 가방 내부의 재료 보유량(유동 데이터)에 따른 의존성 문제를 해결하기 위해 `exists()` 함수 기반의 실시간 판단 로직을 구현했습니다. 단일 스크립트로 정상 성공 구간과 시스템 예외 차단 구간을 완벽하게 교차 검증합니다.
* **Flakiness (테스트 불안정성) 제어 및 오탐 차단**
  * 스킬 해제 후 불투명한 인게임 UI 배경으로 인한 가짜 배경 오탐(False-Positive) 결함을 해결하기 위해, 특정 이미지 객체의 매칭 합격 기준선(`threshold`)을 **0.90으로 상향 보정**하여 테스트의 신뢰도를 100%로 확보했습니다.
* **도메인 격리형 자산 관리 시스템 (Domain Asset Separation)**
  * 프로젝트 규모 확장에 대비해 이미지 자산(`tpl*.png`)을 `menu/`, `skill/`, `popup/` 등 기능적 도메인 단위로 정렬하고 파이썬 `os.path` 라이브러리로 안전하게 절대 경로 바인딩을 자동 수행합니다.
* **디바이스 애그노스틱 및 안전한 상태 복구 (State Recovery)**
  * 소스코드 내 기기 고유 시리얼 번호 하드코딩을 전면 배제하고 자동 디바이스 탐색 메커니즘(`android:///`)을 채택했습니다. 또한 예외 처리 검증 직후 시스템 닫기 액션을 수행하여, 다음 테스트 시나리오 진입 전 기기 화면을 항상 **멱등성(Idempotency)**이 보장된 초기 상태로 원상 복구합니다.

---

## 📂 Directory Structure

```text
Architect_Test.air/
│
├── Architect_Test.py      # [Runner] 프레임워크 초기화, 디바이스 연결 및 전체 테스트 통합 구동
│
├── pages/                 # [Page Objects] UI 템플릿 정의 및 인게임 비즈니스 로직 클래스
│   └── skill_page.py
│
├── tests/                 # [Test Cases] 기능 정상 작동/예외 처리 검증 시나리오 스위트
│   └── test_skill.py
│
└── assets/                # [Assets] 기능 도메인별로 완벽히 격리된 이미지 자산 보관소
    ├── menu/              # 메인 메뉴, 내비게이션 관련 UI 이미지
    ├── skill/             # 스킬 슬롯, 마이너스 버튼, 레벨업 성공 이펙트 이미지
    └── popup/             # 시스템 획득처 및 재료 부족 경고 팝업 이미지
