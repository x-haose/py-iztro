from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, Field, PrivateAttr

TimeIndexType = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
GenderType = Literal["男", "女"]
LanguageType = Literal["en-US", "ja-JP", "ko-KR", "zh-CN", "zh-TW", "vi-VN"]
StarType = Literal["major", "soft", "tough", "adjective", "flower", "helper", "lucun", "tianma"]


class StarModel(BaseModel):
    """
    紫微斗数星耀模型
    """

    name: str = Field(alias="name", title="星耀名字", description="星耀名字")
    type: StarType = Field(
        alias="type",
        title="星耀类型",
        description="星耀类型（主星 | 吉星 | 煞星 | 杂耀 | 桃花星 | 解神 | 禄存 | 天马）",
    )
    scope: str = Field(alias="scope", title="作用范围", description="作用范围（本命盘 | 大限盘 | 流年盘）")
    brightness: str | None = Field(
        alias="brightness",
        default=None,
        title="星耀亮度",
        description="星耀亮度，若没有亮度数据则此字段为`空字符串`或者 `None`",
    )
    mutagen: str | None = Field(
        alias="mutagen", default=None, title="四化", description="四化，若未产生四化则此字段为 `None`"
    )


class DecadalModel(BaseModel):
    """
    大限模型
    """

    range: list[int] = Field(alias="range", title="大限起止年龄 [起始年龄, 截止年龄]")
    heavenly_stem: str = Field(alias="heavenlyStem", title="大限天干")
    earthly_branch: str = Field(alias="earthlyBranch", title="大限地支")


class HoroscopeItemModel(BaseModel):
    """
    运限对象模型
    """

    index: int = Field(alias="index", title="所在宫位的索引")
    name: str = Field(alias="name", title="运限名称")
    heavenly_stem: str = Field(alias="heavenlyStem", title="该运限天干")
    earthly_branch: str = Field(alias="earthlyBranch", title="该运限地支")
    palace_names: list[str] = Field(alias="palaceNames", title="该运限的十二宫")
    mutagen: list[str] = Field(alias="mutagen", title="四化星")
    stars: list[list[StarModel]] | None = Field(alias="stars", default=None, title="流耀")


class SoulAndBodyModel(BaseModel):
    """
    命宫、身宫对象模型
    """

    soul_indx: int = Field(alias="soulIndex", title="命宫索引")
    body_indx: int = Field(alias="bodyIndex", title="身宫索引")
    heavenly_stem_of_soul: str = Field(alias="heavenlyStemOfSoul", title="命宫天干")
    earthly_branch_of_soul: str = Field(alias="earthlyBranchOfBody", title="命宫地支")


class PalaceModel(BaseModel):
    """
    宫位对象模型
    """

    index: int = Field(alias="index", title="宫位索引")
    name: str = Field(alias="name", title="宫位名称")
    is_body_palace: bool = Field(alias="isBodyPalace", title="是否身宫")
    is_original_palace: bool = Field(alias="isOriginalPalace", title="是否来因宫")
    heavenly_stem: str = Field(alias="heavenlyStem", title="宫位天干")
    earthly_branch: str = Field(alias="earthlyBranch", title="宫位地支")
    major_stars: list[StarModel] = Field(alias="majorStars", title="主星")
    minor_stars: list[StarModel] = Field(alias="minorStars", title="辅星")
    adjective_stars: list[StarModel] = Field(alias="adjectiveStars", title="杂耀")
    changsheng12: str = Field(alias="changsheng12", title="长生12神")
    boshi12: str = Field(alias="boshi12", title="博士12神")
    jiangqian12: str = Field(alias="jiangqian12", title="流年将前12神")
    suiqian12: str = Field(alias="suiqian12", title="流年岁前12神")
    decadal: DecadalModel = Field(alias="decadal", title="大限")
    ages: list[int] = Field(alias="ages", title="小限")


class SurroundedPalacesModel(BaseModel):
    """
    三方四正宫位模型
    """

    target: PalaceModel = Field(alias="target", title="目标宫位, 本宫")
    opposite: PalaceModel = Field(alias="opposite", title="对宫")
    wealth: PalaceModel = Field(alias="wealth", title="三方位（财帛位）")
    career: PalaceModel = Field(alias="career", title="三方位（官禄位）")


class HoroscopeItemAgeModel(HoroscopeItemModel):
    """
    运限小限模型
    """

    nominal_age: int = Field(alias="nominalAge", title="虚岁")


class HoroscopeItemYearlyModel(HoroscopeItemModel):
    """
    运限流年模型
    """

    class YearlyDecStarModel(BaseModel):
        jiangqian12: list[str] = Field(alias="jiangqian12", title="流年将前12神")
        suiqian12: list[str] = Field(alias="suiqian12", title="流年岁前12神")

    yearly_dec_star: YearlyDecStarModel = Field(alias="yearlyDecStar", title="流年12神")


class HoroscopeModel(BaseModel):
    """
    运限模型
    """

    lunar_date: str = Field(alias="lunarDate", title="农历日期")
    solar_date: str = Field(alias="solarDate", title="阳历日期")
    decadal: HoroscopeItemModel = Field(alias="decadal", title="大限")
    age: HoroscopeItemAgeModel = Field(alias="age", title="小限")
    yearly: HoroscopeItemYearlyModel = Field(alias="yearly", title="流年")
    monthly: HoroscopeItemModel = Field(alias="monthly", title="流月")
    daily: HoroscopeItemModel = Field(alias="daily", title="流日")
    hourly: HoroscopeItemModel = Field(alias="hourly", title="流时")


class AstrolabeModel(BaseModel):
    """
    星盘模型
    """

    gender: str = Field(alias="gender", title="性别")
    solar_date: str = Field(alias="solarDate", title="阳历日期")
    lunar_date: str = Field(alias="lunarDate", title="农历日期")
    chinese_date: str = Field(alias="chineseDate", title="干支纪年日期")
    time: str = Field(alias="time", title="时辰")
    time_range: str = Field(alias="timeRange", title="时辰对应的时间段")
    sign: str = Field(alias="sign", title="星座")
    zodiac: str = Field(alias="zodiac", title="生肖")
    earthly_branch_of_soul_palace: str = Field(alias="earthlyBranchOfSoulPalace", title="命宫地支")
    earthly_branch_of_body_palace: str = Field(alias="earthlyBranchOfBodyPalace", title="身宫地支")
    soul: str = Field(alias="soul", title="命主")
    body: str = Field(alias="body", title="身主")
    five_elements_class: str = Field(alias="fiveElementsClass", title="五行局")
    palaces: list[PalaceModel] = Field(alias="palaces", title="十二宫数据")

    _js_astro_obj: Any = PrivateAttr()

    def horoscope(self, date: str | None = None, time_index: TimeIndexType | None = None) -> HoroscopeModel:
        """
        获取运限数据

        Args:
            date: 阳历日期【可选】，默认为调用时的日期
            time_index: 时辰索引【可选】，默认会自动读取当前时间的时辰 0-12

        Returns:

        """
        result = self._js_astro_obj.horoscope(date, time_index)

        def _get_horoscope_item_dict(
            _data: dict[str, str | list[str]],
        ) -> dict[str, str | float | list[str] | list[list[StarModel]]]:
            _new_data: dict[str, Any] = dict(
                **_data,
                palaceNames=list(_data["palaceNames"]),
                mutagen=list(_data["mutagen"]),
                stars=[[StarModel(**star) for star in stars] for stars in _data.stars or []],  # type: ignore
            )
            if _data["yearlyDecStar"]:
                _new_data["yearlyDecStar"] = HoroscopeItemYearlyModel.YearlyDecStarModel(
                    jiangqian12=list(_data["yearlyDecStar"]["jiangqian12"]),  # type: ignore
                    suiqian12=list(_data["yearlyDecStar"]["suiqian12"]),  # type: ignore
                )
            return _new_data

        return HoroscopeModel(
            lunarDate=result.lunarDate,
            solarDate=result.solarDate,
            decadal=HoroscopeItemModel.model_validate(_get_horoscope_item_dict(result.decadal)),
            age=HoroscopeItemAgeModel.model_validate(_get_horoscope_item_dict(result.age)),
            yearly=HoroscopeItemYearlyModel.model_validate(_get_horoscope_item_dict(result.yearly)),
            monthly=HoroscopeItemModel.model_validate(_get_horoscope_item_dict(result.monthly)),
            daily=HoroscopeItemModel.model_validate(_get_horoscope_item_dict(result.daily)),
            hourly=HoroscopeItemModel.model_validate(_get_horoscope_item_dict(result.hourly)),
        )

    @classmethod
    def from_js_astro_obj(cls, js_astro_obj: Any) -> "AstrolabeModel":
        astro = cls(**js_astro_obj)
        for palace in js_astro_obj.palaces:
            p = PalaceModel(**dict(palace, decadal=DecadalModel(**palace.decadal)))
            p.decadal.range = list(map(int, palace.decadal.range))
            p.major_stars = [StarModel(**major_star) for major_star in palace.majorStars]
            p.minor_stars = [StarModel(**minor_star) for minor_star in palace.minorStars]
            p.adjective_stars = [StarModel(**adjective_star) for adjective_star in palace.adjectiveStars]
            p.ages = list(map(int, palace.ages))
            astro.palaces.append(p)
        astro._js_astro_obj = js_astro_obj
        return astro


class YearDivideEnum(str, Enum):
    """
    年分割点枚举
    """

    # 正月初一分界
    NORMAL = "normal"
    # 立春分界
    EXACT = "exact"


class AgeDivideEnum(str, Enum):
    """
    小限分割点枚举
    """

    # 只考虑年份，不考虑生日
    NORMAL = "normal"
    # 以生日为分界点
    BIRTHDAY = "birthday"


class AlgorithmEnum(str, Enum):
    """
    紫薇派别
    """

    # 以《紫微斗数全书》为基础安星
    DEFAULT = "default"
    # 以中州派安星法为基础安星
    ZHONGZHOU = "zhongzhou"


class ConfigModel(BaseModel):
    """
    配置模型
    """

    # 四化表配置。如：
    #   { 庚: ['太阳', '武曲', '天同', '天相'] }
    mutagens: dict[str, list[str]] | None = Field(default_factory=dict, title="四化表的配置")
    # 星耀在十二宫的亮度配置 如
    #   { 贪狼: ['旺', '旺', '旺', '旺', '旺', '旺', '旺', '旺', '旺', '旺', '旺', '旺'] }
    brightness: dict[str, list[str]] | None = Field(default_factory=dict, title="星耀在十二宫的亮度")
    # 年分割点配置
    #   - YearDivideEnum.NORMA: 正月初一分界
    #   - YearDivideEnum.EXACT: 立春分界
    year_divide: YearDivideEnum | None = Field(default=YearDivideEnum.NORMAL, title="年分割点", alias="yearDivide")
    # 小限分割点
    #   - AgeDivideEnum.NORMA: 只考虑年份，不考虑生日
    #   - AgeDivideEnum.BIRTHDAY: 以生日为分界点
    age_divide: AgeDivideEnum | None = Field(default=AgeDivideEnum.NORMAL, title="小限分割点", alias="ageDivide")
    # 运限分割点配置
    #   - YearDivideEnum.NORMA: 正月初一分界
    #   - YearDivideEnum.EXACT: 立春分界
    horoscope_divide: YearDivideEnum | None = Field(
        default=YearDivideEnum.NORMAL, title="xx分割点", alias="horoscopeDivide"
    )
    # 安星方法
    #   - AlgorithmEnum.DEFAULT: 以《紫微斗数全书》为基础安星
    #   - AlgorithmEnum.ZHONGZHOU: 以中州派安星法为基础安星
    algorithm: AlgorithmEnum | None = Field(default=AlgorithmEnum.DEFAULT, title="紫微派别")
