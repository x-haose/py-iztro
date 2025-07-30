
# py-iztro
[![pypi](https://img.shields.io/badge/pypi-v0.1-blue)](https://pypi.org/project/py-iztro/)
[![codecov](https://codecov.io/gh/JinyangWang27/py-iztro/graph/badge.svg?token=QFWA4XR1HC)](https://codecov.io/gh/JinyangWang27/py-iztro)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/x-haose/py-iztro)

著名紫微排盘工具[iztro](https://github.com/SylarLong/iztro)python版本，用法和原版完全一致

感觉好用的话麻烦给颗✨✨

## 特性

- 使用和原本完成一致
- 使用python版js解释器之间运行源代码逻辑完成一致
- 使用`pydantic`对代码模型进行完全注解及注释
- 基于`iztro`版本：2.5.0
- 积极开发接受建议，欢迎提`issues`


## 路线图

- 实现`iztro`库常用的大部分方法
- 提供快捷服务端api


## 安装

使用 pip 安装 py-iztro

```bash
  pip install py-iztro
```
    
## Demo

### 基本排盘
```py
from py_iztro import Astro


def main():
    astro = Astro()
    result = astro.by_solar("2000-8-16", 2, "女")
    print(result.model_dump_json(by_alias=True, indent=4))


if __name__ == '__main__':
    main()

```

运行结果：
```
/Users/haose/code/py-iztro/.venv/bin/python /Users/haose/code/py-iztro/src/tests/base.py 
{
    "gender": "女",
    "solarDate": "2000-8-16",
    "lunarDate": "二〇〇〇年七月十七",
    "chineseDate": "庚辰 甲申 丙午 庚寅",
    "time": "寅时",
    "timeRange": "03:00~05:00",
    "sign": "狮子座",
    "zodiac": "龙",
    "earthlyBranchOfSoulPalace": "午",
    "earthlyBranchOfBodyPalace": "戌",
    "soul": "破军",
    "body": "文昌",
    "fiveElementsClass": "木三局",
    "palaces": [
        {
            "index": 0,
            "name": "财帛",
            "isBodyPalace": false,
            "isOriginalPalace": false,
            "heavenlyStem": "戊",
            "earthlyBranch": "寅",
            "majorStars": [
                {
                    "name": "武曲",
                    "type": "major",
                    "scope": "origin",
                    "brightness": "得",
                    "mutagen": "权"
                },
                {
                    "name": "天相",
                    "type": "major",
                    "scope": "origin",
                    "brightness": "庙",
                    "mutagen": ""
                },
                {
                    "name": "天马",
                    "type": "tianma",
                    "scope": "origin",
                    "brightness": "",
                    "mutagen": null
                }
            ],
            "minorStars": [],
            "adjectiveStars": [
                {
                    "name": "解神",
                    "type": "helper",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "三台",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "天寿",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "天巫",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "天厨",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "阴煞",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "天哭",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            "changsheng12": "绝",
            "boshi12": "飞廉",
            "jiangqian12": "岁驿",
            "suiqian12": "吊客",
            "decadal": {
                "range": [
                    43,
                    52
                ],
                "heavenlyStem": "戊",
                "earthlyBranch": "寅"
            },
            "ages": [
                9,
                21,
                33,
                45,
                57,
                69,
                81,
                93,
                105,
                117
            ]
        },
        {
            "index": 1,
            "name": "子女",
            "isBodyPalace": false,
            "isOriginalPalace": false,
            "heavenlyStem": "己",
            "earthlyBranch": "卯",
            "majorStars": [
                {
                    "name": "太阳",
                    "type": "major",
                    "scope": "origin",
                    "brightness": "庙",
                    "mutagen": "禄"
                },
                {
                    "name": "天梁",
                    "type": "major",
                    "scope": "origin",
                    "brightness": "庙",
                    "mutagen": ""
                }
            ],
            "minorStars": [],
            "adjectiveStars": [
                {
                    "name": "天刑",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            "changsheng12": "墓",
            "boshi12": "奏书",
            "jiangqian12": "息神",
            "suiqian12": "病符",
            "decadal": {
                "range": [
                    33,
                    42
                ],
                "heavenlyStem": "己",
                "earthlyBranch": "卯"
            },
            "ages": [
                8,
                20,
                32,
                44,
                56,
                68,
                80,
                92,
                104,
                116
            ]
        },
        {
            "index": 2,
            "name": "夫妻",
            "isBodyPalace": false,
            "isOriginalPalace": true,
            "heavenlyStem": "庚",
            "earthlyBranch": "辰",
            "majorStars": [
                {
                    "name": "七杀",
                    "type": "major",
                    "scope": "origin",
                    "brightness": "庙",
                    "mutagen": ""
                }
            ],
            "minorStars": [
                {
                    "name": "右弼",
                    "type": "soft",
                    "scope": "origin",
                    "brightness": "",
                    "mutagen": ""
                },
                {
                    "name": "火星",
                    "type": "tough",
                    "scope": "origin",
                    "brightness": "陷",
                    "mutagen": null
                }
            ],
            "adjectiveStars": [
                {
                    "name": "封诰",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "华盖",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            "changsheng12": "死",
            "boshi12": "将军",
            "jiangqian12": "华盖",
            "suiqian12": "岁建",
            "decadal": {
                "range": [
                    23,
                    32
                ],
                "heavenlyStem": "庚",
                "earthlyBranch": "辰"
            },
            "ages": [
                7,
                19,
                31,
                43,
                55,
                67,
                79,
                91,
                103,
                115
            ]
        },
        {
            "index": 3,
            "name": "兄弟",
            "isBodyPalace": false,
            "isOriginalPalace": false,
            "heavenlyStem": "辛",
            "earthlyBranch": "巳",
            "majorStars": [
                {
                    "name": "天机",
                    "type": "major",
                    "scope": "origin",
                    "brightness": "平",
                    "mutagen": ""
                }
            ],
            "minorStars": [],
            "adjectiveStars": [
                {
                    "name": "天喜",
                    "type": "flower",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "天空",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "孤辰",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            "changsheng12": "病",
            "boshi12": "小耗",
            "jiangqian12": "劫煞",
            "suiqian12": "晦气",
            "decadal": {
                "range": [
                    13,
                    22
                ],
                "heavenlyStem": "辛",
                "earthlyBranch": "巳"
            },
            "ages": [
                6,
                18,
                30,
                42,
                54,
                66,
                78,
                90,
                102,
                114
            ]
        },
        {
            "index": 4,
            "name": "命宫",
            "isBodyPalace": false,
            "isOriginalPalace": false,
            "heavenlyStem": "壬",
            "earthlyBranch": "午",
            "majorStars": [
                {
                    "name": "紫微",
                    "type": "major",
                    "scope": "origin",
                    "brightness": "庙",
                    "mutagen": ""
                }
            ],
            "minorStars": [
                {
                    "name": "文曲",
                    "type": "soft",
                    "scope": "origin",
                    "brightness": "陷",
                    "mutagen": ""
                }
            ],
            "adjectiveStars": [
                {
                    "name": "凤阁",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "天福",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "截空",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "蜚廉",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            "changsheng12": "衰",
            "boshi12": "青龙",
            "jiangqian12": "灾煞",
            "suiqian12": "丧门",
            "decadal": {
                "range": [
                    3,
                    12
                ],
                "heavenlyStem": "壬",
                "earthlyBranch": "午"
            },
            "ages": [
                5,
                17,
                29,
                41,
                53,
                65,
                77,
                89,
                101,
                113
            ]
        },
        {
            "index": 5,
            "name": "父母",
            "isBodyPalace": false,
            "isOriginalPalace": false,
            "heavenlyStem": "癸",
            "earthlyBranch": "未",
            "majorStars": [],
            "minorStars": [
                {
                    "name": "天钺",
                    "type": "soft",
                    "scope": "origin",
                    "brightness": "",
                    "mutagen": null
                },
                {
                    "name": "陀罗",
                    "type": "tough",
                    "scope": "origin",
                    "brightness": "庙",
                    "mutagen": null
                }
            ],
            "adjectiveStars": [
                {
                    "name": "天姚",
                    "type": "flower",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "空亡",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            "changsheng12": "帝旺",
            "boshi12": "力士",
            "jiangqian12": "天煞",
            "suiqian12": "贯索",
            "decadal": {
                "range": [
                    113,
                    122
                ],
                "heavenlyStem": "癸",
                "earthlyBranch": "未"
            },
            "ages": [
                4,
                16,
                28,
                40,
                52,
                64,
                76,
                88,
                100,
                112
            ]
        },
        {
            "index": 6,
            "name": "福德",
            "isBodyPalace": false,
            "isOriginalPalace": false,
            "heavenlyStem": "甲",
            "earthlyBranch": "申",
            "majorStars": [
                {
                    "name": "破军",
                    "type": "major",
                    "scope": "origin",
                    "brightness": "得",
                    "mutagen": ""
                },
                {
                    "name": "禄存",
                    "type": "lucun",
                    "scope": "origin",
                    "brightness": "",
                    "mutagen": null
                }
            ],
            "minorStars": [
                {
                    "name": "文昌",
                    "type": "soft",
                    "scope": "origin",
                    "brightness": "得",
                    "mutagen": ""
                }
            ],
            "adjectiveStars": [
                {
                    "name": "龙池",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "台辅",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "旬空",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            "changsheng12": "临官",
            "boshi12": "博士",
            "jiangqian12": "指背",
            "suiqian12": "官符",
            "decadal": {
                "range": [
                    103,
                    112
                ],
                "heavenlyStem": "甲",
                "earthlyBranch": "申"
            },
            "ages": [
                3,
                15,
                27,
                39,
                51,
                63,
                75,
                87,
                99,
                111
            ]
        },
        {
            "index": 7,
            "name": "田宅",
            "isBodyPalace": false,
            "isOriginalPalace": false,
            "heavenlyStem": "乙",
            "earthlyBranch": "酉",
            "majorStars": [],
            "minorStars": [
                {
                    "name": "地空",
                    "type": "tough",
                    "scope": "origin",
                    "brightness": "",
                    "mutagen": null
                },
                {
                    "name": "擎羊",
                    "type": "tough",
                    "scope": "origin",
                    "brightness": "陷",
                    "mutagen": null
                }
            ],
            "adjectiveStars": [
                {
                    "name": "咸池",
                    "type": "flower",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "天贵",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "月德",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            "changsheng12": "冠带",
            "boshi12": "官府",
            "jiangqian12": "咸池",
            "suiqian12": "小耗",
            "decadal": {
                "range": [
                    93,
                    102
                ],
                "heavenlyStem": "乙",
                "earthlyBranch": "酉"
            },
            "ages": [
                2,
                14,
                26,
                38,
                50,
                62,
                74,
                86,
                98,
                110
            ]
        },
        {
            "index": 8,
            "name": "官禄",
            "isBodyPalace": true,
            "isOriginalPalace": false,
            "heavenlyStem": "丙",
            "earthlyBranch": "戌",
            "majorStars": [
                {
                    "name": "廉贞",
                    "type": "major",
                    "scope": "origin",
                    "brightness": "利",
                    "mutagen": ""
                },
                {
                    "name": "天府",
                    "type": "major",
                    "scope": "origin",
                    "brightness": "庙",
                    "mutagen": ""
                }
            ],
            "minorStars": [
                {
                    "name": "左辅",
                    "type": "soft",
                    "scope": "origin",
                    "brightness": "",
                    "mutagen": ""
                }
            ],
            "adjectiveStars": [
                {
                    "name": "天才",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "天虚",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            "changsheng12": "沐浴",
            "boshi12": "伏兵",
            "jiangqian12": "月煞",
            "suiqian12": "大耗",
            "decadal": {
                "range": [
                    83,
                    92
                ],
                "heavenlyStem": "丙",
                "earthlyBranch": "戌"
            },
            "ages": [
                1,
                13,
                25,
                37,
                49,
                61,
                73,
                85,
                97,
                109
            ]
        },
        {
            "index": 9,
            "name": "仆役",
            "isBodyPalace": false,
            "isOriginalPalace": false,
            "heavenlyStem": "丁",
            "earthlyBranch": "亥",
            "majorStars": [
                {
                    "name": "太阴",
                    "type": "major",
                    "scope": "origin",
                    "brightness": "庙",
                    "mutagen": "科"
                }
            ],
            "minorStars": [],
            "adjectiveStars": [
                {
                    "name": "红鸾",
                    "type": "flower",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "恩光",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "天官",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "天月",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "天伤",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            "changsheng12": "长生",
            "boshi12": "大耗",
            "jiangqian12": "亡神",
            "suiqian12": "龙德",
            "decadal": {
                "range": [
                    73,
                    82
                ],
                "heavenlyStem": "丁",
                "earthlyBranch": "亥"
            },
            "ages": [
                12,
                24,
                36,
                48,
                60,
                72,
                84,
                96,
                108,
                120
            ]
        },
        {
            "index": 10,
            "name": "迁移",
            "isBodyPalace": false,
            "isOriginalPalace": false,
            "heavenlyStem": "戊",
            "earthlyBranch": "子",
            "majorStars": [
                {
                    "name": "贪狼",
                    "type": "major",
                    "scope": "origin",
                    "brightness": "旺",
                    "mutagen": ""
                }
            ],
            "minorStars": [
                {
                    "name": "铃星",
                    "type": "tough",
                    "scope": "origin",
                    "brightness": "陷",
                    "mutagen": null
                }
            ],
            "adjectiveStars": [
                {
                    "name": "八座",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            "changsheng12": "养",
            "boshi12": "病符",
            "jiangqian12": "将星",
            "suiqian12": "白虎",
            "decadal": {
                "range": [
                    63,
                    72
                ],
                "heavenlyStem": "戊",
                "earthlyBranch": "子"
            },
            "ages": [
                11,
                23,
                35,
                47,
                59,
                71,
                83,
                95,
                107,
                119
            ]
        },
        {
            "index": 11,
            "name": "疾厄",
            "isBodyPalace": false,
            "isOriginalPalace": false,
            "heavenlyStem": "己",
            "earthlyBranch": "丑",
            "majorStars": [
                {
                    "name": "天同",
                    "type": "major",
                    "scope": "origin",
                    "brightness": "不",
                    "mutagen": "忌"
                },
                {
                    "name": "巨门",
                    "type": "major",
                    "scope": "origin",
                    "brightness": "不",
                    "mutagen": ""
                }
            ],
            "minorStars": [
                {
                    "name": "天魁",
                    "type": "soft",
                    "scope": "origin",
                    "brightness": "",
                    "mutagen": null
                },
                {
                    "name": "地劫",
                    "type": "tough",
                    "scope": "origin",
                    "brightness": "",
                    "mutagen": null
                }
            ],
            "adjectiveStars": [
                {
                    "name": "天德",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "寡宿",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "破碎",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "天使",
                    "type": "adjective",
                    "scope": "origin",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            "changsheng12": "胎",
            "boshi12": "喜神",
            "jiangqian12": "攀鞍",
            "suiqian12": "天德",
            "decadal": {
                "range": [
                    53,
                    62
                ],
                "heavenlyStem": "己",
                "earthlyBranch": "丑"
            },
            "ages": [
                10,
                22,
                34,
                46,
                58,
                70,
                82,
                94,
                106,
                118
            ]
        }
    ]
}

进程已结束，退出代码为 0

```

### 大限流年

```py
from py_iztro import Astro


def main():
    astro = Astro()
    result = astro.by_solar("2000-8-16", 2, "女")
    result = result.horoscope("2025-01-01").model_dump_json(by_alias=True, indent=4)
    print(result)


if __name__ == '__main__':
    main()
```

运行结果：
```
/Users/haose/code/py-iztro/.venv/bin/python /Users/haose/code/py-iztro/src/tests/daxian.py 
{
    "lunarDate": "二〇二四年腊月初二",
    "solarDate": "2025-1-1",
    "decadal": {
        "index": 2,
        "name": "大限",
        "heavenlyStem": "庚",
        "earthlyBranch": "辰",
        "palaceNames": [
            "夫妻",
            "兄弟",
            "命宫",
            "父母",
            "福德",
            "田宅",
            "官禄",
            "仆役",
            "迁移",
            "疾厄",
            "财帛",
            "子女"
        ],
        "mutagen": [
            "太阳",
            "武曲",
            "太阴",
            "天同"
        ],
        "stars": [
            [
                {
                    "name": "运马",
                    "type": "tianma",
                    "scope": "decadal",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "运曲",
                    "type": "soft",
                    "scope": "decadal",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [
                {
                    "name": "运喜",
                    "type": "flower",
                    "scope": "decadal",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [
                {
                    "name": "运钺",
                    "type": "soft",
                    "scope": "decadal",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "运陀",
                    "type": "tough",
                    "scope": "decadal",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "运禄",
                    "type": "lucun",
                    "scope": "decadal",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "运羊",
                    "type": "tough",
                    "scope": "decadal",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [
                {
                    "name": "运昌",
                    "type": "soft",
                    "scope": "decadal",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "运鸾",
                    "type": "flower",
                    "scope": "decadal",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [
                {
                    "name": "运魁",
                    "type": "soft",
                    "scope": "decadal",
                    "brightness": null,
                    "mutagen": null
                }
            ]
        ]
    },
    "age": {
        "index": 8,
        "name": "小限",
        "heavenlyStem": "丙",
        "earthlyBranch": "戌",
        "palaceNames": [
            "官禄",
            "仆役",
            "迁移",
            "疾厄",
            "财帛",
            "子女",
            "夫妻",
            "兄弟",
            "命宫",
            "父母",
            "福德",
            "田宅"
        ],
        "mutagen": [
            "天同",
            "天机",
            "文昌",
            "廉贞"
        ],
        "stars": [],
        "nominalAge": 25
    },
    "yearly": {
        "index": 2,
        "name": "流年",
        "heavenlyStem": "甲",
        "earthlyBranch": "辰",
        "palaceNames": [
            "夫妻",
            "兄弟",
            "命宫",
            "父母",
            "福德",
            "田宅",
            "官禄",
            "仆役",
            "迁移",
            "疾厄",
            "财帛",
            "子女"
        ],
        "mutagen": [
            "廉贞",
            "破军",
            "武曲",
            "太阳"
        ],
        "stars": [
            [
                {
                    "name": "流禄",
                    "type": "lucun",
                    "scope": "yearly",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "流马",
                    "type": "tianma",
                    "scope": "yearly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "流羊",
                    "type": "tough",
                    "scope": "yearly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [
                {
                    "name": "流昌",
                    "type": "soft",
                    "scope": "yearly",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "流喜",
                    "type": "flower",
                    "scope": "yearly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "年解",
                    "type": "helper",
                    "scope": "yearly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "流钺",
                    "type": "soft",
                    "scope": "yearly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [
                {
                    "name": "流曲",
                    "type": "soft",
                    "scope": "yearly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [
                {
                    "name": "流鸾",
                    "type": "flower",
                    "scope": "yearly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [
                {
                    "name": "流魁",
                    "type": "soft",
                    "scope": "yearly",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "流陀",
                    "type": "tough",
                    "scope": "yearly",
                    "brightness": null,
                    "mutagen": null
                }
            ]
        ],
        "yearlyDecStar": {
            "jiangqian12": [
                "岁驿",
                "息神",
                "华盖",
                "劫煞",
                "灾煞",
                "天煞",
                "指背",
                "咸池",
                "月煞",
                "亡神",
                "将星",
                "攀鞍"
            ],
            "suiqian12": [
                "吊客",
                "病符",
                "岁建",
                "晦气",
                "丧门",
                "贯索",
                "官符",
                "小耗",
                "大耗",
                "龙德",
                "白虎",
                "天德"
            ]
        }
    },
    "monthly": {
        "index": 8,
        "name": "流月",
        "heavenlyStem": "丙",
        "earthlyBranch": "子",
        "palaceNames": [
            "官禄",
            "仆役",
            "迁移",
            "疾厄",
            "财帛",
            "子女",
            "夫妻",
            "兄弟",
            "命宫",
            "父母",
            "福德",
            "田宅"
        ],
        "mutagen": [
            "天同",
            "天机",
            "文昌",
            "廉贞"
        ],
        "stars": [
            [
                {
                    "name": "yuema",
                    "type": "tianma",
                    "scope": "monthly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "yueluan",
                    "type": "flower",
                    "scope": "monthly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "yuetuo",
                    "type": "tough",
                    "scope": "monthly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "yuelu",
                    "type": "lucun",
                    "scope": "monthly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "yuequ",
                    "type": "soft",
                    "scope": "monthly",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "yueyang",
                    "type": "tough",
                    "scope": "monthly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [
                {
                    "name": "yuechang",
                    "type": "soft",
                    "scope": "monthly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "yueyue",
                    "type": "soft",
                    "scope": "monthly",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "yuexi",
                    "type": "flower",
                    "scope": "monthly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [
                {
                    "name": "yuekui",
                    "type": "soft",
                    "scope": "monthly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            []
        ]
    },
    "daily": {
        "index": 9,
        "name": "流日",
        "heavenlyStem": "庚",
        "earthlyBranch": "午",
        "palaceNames": [
            "田宅",
            "官禄",
            "仆役",
            "迁移",
            "疾厄",
            "财帛",
            "子女",
            "夫妻",
            "兄弟",
            "命宫",
            "父母",
            "福德"
        ],
        "mutagen": [
            "太阳",
            "武曲",
            "太阴",
            "天同"
        ],
        "stars": [
            [],
            [
                {
                    "name": "riqu",
                    "type": "soft",
                    "scope": "daily",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "rixi",
                    "type": "flower",
                    "scope": "daily",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [],
            [],
            [
                {
                    "name": "riyue",
                    "type": "soft",
                    "scope": "daily",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "rituo",
                    "type": "tough",
                    "scope": "daily",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "rilu",
                    "type": "lucun",
                    "scope": "daily",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "rima",
                    "type": "tianma",
                    "scope": "daily",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "riyang",
                    "type": "tough",
                    "scope": "daily",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "riluan",
                    "type": "flower",
                    "scope": "daily",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [
                {
                    "name": "richang",
                    "type": "soft",
                    "scope": "daily",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [
                {
                    "name": "rikui",
                    "type": "soft",
                    "scope": "daily",
                    "brightness": null,
                    "mutagen": null
                }
            ]
        ]
    },
    "hourly": {
        "index": 9,
        "name": "流时",
        "heavenlyStem": "丙",
        "earthlyBranch": "子",
        "palaceNames": [
            "田宅",
            "官禄",
            "仆役",
            "迁移",
            "疾厄",
            "财帛",
            "子女",
            "夫妻",
            "兄弟",
            "命宫",
            "父母",
            "福德"
        ],
        "mutagen": [
            "天同",
            "天机",
            "文昌",
            "廉贞"
        ],
        "stars": [
            [
                {
                    "name": "shima",
                    "type": "tianma",
                    "scope": "hourly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "shiluan",
                    "type": "flower",
                    "scope": "hourly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "shituo",
                    "type": "tough",
                    "scope": "hourly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "shilu",
                    "type": "lucun",
                    "scope": "hourly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "shiqu",
                    "type": "soft",
                    "scope": "hourly",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "shiyang",
                    "type": "tough",
                    "scope": "hourly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [
                {
                    "name": "shichang",
                    "type": "soft",
                    "scope": "hourly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [
                {
                    "name": "shiyue",
                    "type": "soft",
                    "scope": "hourly",
                    "brightness": null,
                    "mutagen": null
                },
                {
                    "name": "shixi",
                    "type": "flower",
                    "scope": "hourly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            [
                {
                    "name": "shikui",
                    "type": "soft",
                    "scope": "hourly",
                    "brightness": null,
                    "mutagen": null
                }
            ],
            [],
            []
        ]
    }
}

进程已结束，退出代码为 0

```

## 作者

- [@haose](https://www.github.com/x-haose)


## 致谢

 - [最好的紫微排盘工具：iztro](https://github.com/SylarLong/iztro)
