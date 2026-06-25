# -*- encoding=utf8 -*-
import os
from airtest.core.api import *

class SkillPage:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ASSETS_DIR = os.path.join(self.BASE_DIR, "assets")

        # -----------------------------------------------------------------
        # 📁 UI 이미지 템플릿 정의
        # -----------------------------------------------------------------
        # [menu] 태그
        self.BTN_MAIN_MENU       = Template(self.get_path("menu", "tpl1782358382254.png"), record_pos=(-0.443, -0.21), resolution=(2340, 1080))
        self.BTN_SKILL_TAB       = Template(self.get_path("menu", "tpl1782358407878.png"), record_pos=(-0.335, 0.114), resolution=(2340, 1080))
        self.TITLE_SKILL_WINDOW  = Template(self.get_path("menu", "tpl1782358444368.png"), record_pos=(0.0, -0.001), resolution=(2340, 1080))

        # [skill] 태그
        self.TAB_MARYUKTAN       = Template(self.get_path("skill", "tpl1782358515661.png"), record_pos=(-0.316, -0.019), resolution=(2340, 1080))
        self.SLOT_TARGET_EMPTY   = Template(self.get_path("skill", "tpl1782358537971.png"), record_pos=(-0.045, 0.006), resolution=(2340, 1080))
        self.BTN_SKILL_MINUS     = Template(self.get_path("skill", "tpl1782358585872.png"), threshold=0.90, record_pos=(0.009, -0.015), resolution=(2340, 1080))
        self.BTN_EXPAND_LAYER    = Template(self.get_path("skill", "tpl1782358599912.png"), record_pos=(0.435, -0.032), resolution=(2340, 1080))
        self.BTN_LAYER_LEVELUP   = Template(self.get_path("skill", "tpl1782358614729.png"), record_pos=(0.344, 0.193), resolution=(2340, 1080))
        
        # [★성공 시나리오 완벽 보정] Template으로 감싸고 인자 구분을 명확히 정렬했습니다.
        self.EFFECT_LEVELUP_SUCCESS = Template(self.get_path("skill", "tpl1782361887110.png"), record_pos=(0.0, 0.0), resolution=(2340, 1080))

        # [popup] 태그
        self.POPUP_ACQUISITION   = Template(self.get_path("popup", "tpl1782358632680.png"), record_pos=(-0.0, -0.158), resolution=(2340, 1080))
        self.BTN_CLOSE_POPUP     = Template(self.get_path("popup", "tpl1782358648521.png"), record_pos=(0.158, -0.158), resolution=(2340, 1080))

    def get_path(self, tag, filename):
        return os.path.join(self.ASSETS_DIR, tag, filename)

    # -----------------------------------------------------------------
    # 🛠️ 게임 조작 비즈니스 로직 정의 (Page Actions)
    # -----------------------------------------------------------------
    def enter_skill_window(self):
        touch(self.BTN_MAIN_MENU)
        sleep(1.0)
        touch(self.BTN_SKILL_TAB)
        wait(self.TITLE_SKILL_WINDOW, timeout=10)

    def equip_maryuktan(self):
        touch(self.TAB_MARYUKTAN)
        sleep(0.5)
        touch(self.SLOT_TARGET_EMPTY)
        sleep(1.5)

    def unequip_maryuktan(self):
        touch(self.BTN_SKILL_MINUS)
        sleep(1.0)

    def expand_levelup_layer(self):
        touch(self.TAB_MARYUKTAN)
        sleep(0.5)
        touch(self.BTN_EXPAND_LAYER)
        sleep(1.5)

    def trigger_levelup(self):
        touch(self.BTN_LAYER_LEVELUP)

    def close_acquisition_popup(self):
        touch(self.BTN_CLOSE_POPUP)
        sleep(1.0)