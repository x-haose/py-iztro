from importlib import resources

import pythonmonkey as pm

from py_iztro.models import AstrolabeModel, GenderType, LangueType, TimeIndexType


class Astro:
    def __init__(self):
        _js_path = resources.files("py_iztro.res") / "iztro-2.4.9.min.js"
        _js_obj = pm.require(str(_js_path))
        self._astro = _js_obj.get("astro")

    def by_solar(
        self,
        solar_date_str: str,
        time_index: TimeIndexType,
        gender: GenderType,
        fix_leap: bool = True,
        language: LangueType = "zh-CN",
    ) -> AstrolabeModel:
        """
        通过阳历获取星盘信息
        Args:
            solar_date_str: 阳历日期【YYYY-M-D】
            time_index: 出生时辰序号【0~12】0为早子时，1为丑时，2为寅时，3为卯时，4为辰时，5为巳时，6为午时，
            7为未时，8为申时，9为酉时，10为戌时，11为亥时，12为晚子时
            gender: 性别【男|女】
            fix_leap: 是否调整闰月情况【默认 true】，假如调整闰月，则闰月的前半个月算上个月，后半个月算下个月
            language: 输出语言【默认 zh-CN】，支持的语言有：en-US, ja-JP, ko-KR, zh-CN, zh-TW, vi-VN

        Returns:
            星盘信息
        """

        result = self._astro.bySolar(solar_date_str, time_index, gender, fix_leap, language)
        data = AstrolabeModel.from_js_astro_obj(result)
        return data
