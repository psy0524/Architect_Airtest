# -*- encoding=utf8 -*-
import sys
import os
from airtest.core.api import *

# =====================================================================
# 🧭 프레임워크 패키지 경로 동적 바인딩
# =====================================================================
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

# 모듈화된 테스트 시나리오 가져오기
from tests.test_skill import run_skill_test_suite

if __name__ == "__main__":
    # 디바이스 자동 안전 연결
    auto_setup(__file__, devices=["android:///"])
    
    try:
        print("\n========================================")
        print("[START] 아키텍트 모바일 UI 자동화 테스트 프레임워크 구동")
        print("========================================")
        
        # 통합 모듈 시나리오 구동
        run_skill_test_suite()
        
        print("\n========================================")
        print("[SUCCESS] 모든 시나리오 및 예외 처리 검증 완료 (ALL PASS)")
        print("========================================")
        
    except Exception as e:
        print(f"\n[FAIL] 프레임워크 구동 중 결함 및 예외 발견: {e}")
        snapshot(filename="mobile_error.png", msg="자동화 테스트 실패 순간 폰 화면 증적 확보")