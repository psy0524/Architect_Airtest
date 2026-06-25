# -*- encoding=utf8 -*-
from airtest.core.api import *
from pages.skill_page import SkillPage

def run_skill_test_suite():
    # 스킬 페이지 객체 인스턴스 생성
    page = SkillPage()

    # -----------------------------------------------------------------
    # TC 1: 스킬 메인 메뉴 진입 및 장착/해제 완결 테스트 (Positive)
    # -----------------------------------------------------------------
    print("[TC_01 START] 모바일 스킬 장착 및 해제 기능 회귀 테스트")
    page.enter_skill_window()
    page.equip_maryuktan()
    
    assert_exists(page.BTN_SKILL_MINUS, "TC_01: 마력탄 스킬 장착 성공 및 마이너스 버튼 UI 갱신 확인")
    
    page.unequip_maryuktan()
    assert_not_exists(page.BTN_SKILL_MINUS, "TC_01_Sub: 스킬 장착 해제 정상 작동 및 슬롯 초기화 확인")
    print("[TC_01 PASS] 스킬 장착/해제 멱등성 검증 완료")

    # -----------------------------------------------------------------
    # 🎯 TC 2 & 3 통합: 가방 상태(재료 유무)에 따른 동적 레벨업 검증 (Dynamic Conditional Test)
    # -----------------------------------------------------------------
    print("\n[TC_02/03 START] 가방 데이터 상태 기반 레벨업 분기 테스트")
    
    # 1) 다시 레벨업 레이어 진입
    page.expand_levelup_layer()
    print("[QA INFO] 레벨업 버튼 클릭 시동")
    
    # 2) [레벨업] 버튼 클릭 트리거
    page.trigger_levelup()
    sleep(1.5)  # 버튼 클릭 후 서버 응답 및 UI 연출 출력을 위한 대기 시간 확보
    
    # =====================================================================
    # 🧭 실시간 화면 상태 인지 및 실무형 예외 처리 흐름 제어 (If-Else Branching)
    # =====================================================================
    
    # 케이스 A: 화면에 "재료 부족 팝업"이 떴을 경우 ➔ [실패 시나리오 검증]
    if exists(page.POPUP_ACQUISITION):
        print("[⚡ BRANCH - FAIL SCENARIO] 재료 부족 상태가 감지되었습니다. 예외 처리 검증을 시작합니다.")
        
        # 실패 팝업이 확실히 존재하는지 단언문 검증
        assert_exists(page.POPUP_ACQUISITION, "TC_02 (FAIL): 재료 부족 시 시스템 획득처 예외 처리 팝업 노출 확인")
        print("[TC_02 PASS] 시스템 재료 조건 부족 예외 차단 및 획득처 안내 검증 성공")
        
        # 상태 복구 (다음 테스트 연계를 위해 팝업 닫기)
        page.close_acquisition_popup()
        print("[QA INFO] 예외 팝업 해제 및 환경 복구 정상 완료")
        
    # 케이스 B: 화면에 "레벨업 성공 이펙트"가 관측되었을 경우 ➔ [성공 시나리오 검증]
    elif exists(page.EFFECT_LEVELUP_SUCCESS):
        print("[⭐ BRANCH - SUCCESS SCENARIO] 재료가 충족되어 레벨업에 성공했습니다. 정상 기능 검증을 시작합니다.")
        
        # 레벨업 성공 이펙트가 확실히 존재하는지 단언문 검증
        assert_exists(page.EFFECT_LEVELUP_SUCCESS, "TC_03 (SUCCESS): 레벨업 성공 이펙트 노출 및 데이터 반영 확인")
        print("[TC_03 PASS] 스킬 레벨업 정상 작동 검증 성공")
        
    # 케이스 C: 둘 다 안 뜨고 화면이 먹통인 경우 ➔ [기능 결함(Bug) 처리]
    else:
        print("[🚨 BRANCH - UNKNOWN STATE] 레벨업 버튼 작동 후 시스템에 아무런 반응이 없습니다!")
        raise Exception("레벨업 기능 응답 부재 결함 발견 (서버 렉 또는 UI 프리징 의심)")