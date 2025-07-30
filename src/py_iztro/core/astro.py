from importlib import resources

import pythonmonkey as pm  # type: ignore

from py_iztro.core.models import AstrolabeModel, ConfigModel, GenderType, LanguageType, TimeIndexType


class Astro:
    def __init__(self):
        _js_path = resources.files("py_iztro.res") / "iztro-2.5.0.min.js"
        _js_obj = pm.require(str(_js_path))
        self._astro = _js_obj.get("astro")

    def by_solar(
        self,
        solar_date_str: str,
        time_index: TimeIndexType,
        gender: GenderType,
        fix_leap: bool = True,
        language: LanguageType = "zh-CN",
    ) -> AstrolabeModel:
        """
        通过阳历获取星盘信息
        Args:
            solar_date_str: 阳历日期【YYYY-M-D】
            time_index: 出生时辰序号【0~12】
                - 0: 早子时
                - 1: 丑时
                - 2: 寅时
                - 3: 卯时
                - 4: 辰时
                - 5: 巳时
                - 6: 午时
                - 7: 未时
                - 8: 申时
                - 9: 酉时
                - 10: 戌时
                - 11: 亥时
                - 12: 晚子时
            gender: 性别【男|女】
            fix_leap: 是否调整闰月情况【默认 true】，假如调整闰月，则闰月的前半个月算上个月，后半个月算下个月
            language: 输出语言【默认 zh-CN】，支持的语言有：en-US, ja-JP, ko-KR, zh-CN, zh-TW, vi-VN

        Returns:
            星盘信息
        """

        result = self._astro.bySolar(solar_date_str, time_index, gender, fix_leap, language)
        data = AstrolabeModel.from_js_astro_obj(result)
        return data

    def by_lunar(
        self,
        lunar_date_str: str,
        time_index: TimeIndexType,
        gender: GenderType,
        fix_leap: bool = True,
        language: LanguageType = "zh-CN",
    ) -> AstrolabeModel:
        """
        通过农历获取星盘信息
        Args:
            lunar_date_str: 农历日期【YYYY-M-D】，例如2000年七月十七则传入 2000-7-17
            time_index: 出生时辰序号【0~12】
                - 0: 早子时
                - 1: 丑时
                - 2: 寅时
                - 3: 卯时
                - 4: 辰时
                - 5: 巳时
                - 6: 午时
                - 7: 未时
                - 8: 申时
                - 9: 酉时
                - 10: 戌时
                - 11: 亥时
                - 12: 晚子时
            gender: 性别【男|女】
            fix_leap: 是否调整闰月情况【默认 true】，假如调整闰月，则闰月的前半个月算上个月，后半个月算下个月
            language: 输出语言【默认 zh-CN】，支持的语言有：en-US, ja-JP, ko-KR, zh-CN, zh-TW, vi-VN

        Returns:
            星盘信息
        """
        result = self._astro.byLunar(lunar_date_str, time_index, gender, fix_leap, language)
        data = AstrolabeModel.from_js_astro_obj(result)
        return data

    def config(self, config: ConfigModel):
        """
        全局配置四化和亮度
        Args:
            config: 配置数据

        Returns:

        """
        data = config.model_dump(by_alias=True, mode="json")
        self._astro.config(data)

    def get_config(self) -> ConfigModel:
        """
        获取当前配置
        Returns:
            配置数据
        """
        result = self._astro.getConfig()
        data = ConfigModel(**result)
        data.mutagens = {k: list(v) for k, v in result["mutagens"].items()}
        data.brightness = {k: list(v) for k, v in result["brightness"].items()}
        return data
