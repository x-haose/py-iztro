from py_iztro import Astro


def main():
    astro = Astro()

    # 通过阳历调用紫薇斗数排盘
    result_solar = astro.by_solar("2000-8-16", 2, "女")
    result_solar_data = result_solar.model_dump_json(by_alias=True, indent=4)
    print(result_solar_data)

    # 通过农历调用紫薇斗数排盘
    result_lunar = astro.by_lunar("2000-7-17", 2, "女")
    result_lunar_data = result_lunar.model_dump_json(by_alias=True, indent=4)
    print(result_lunar_data)

    # 比较阳历和农历的结果是否相同
    print(result_solar_data == result_lunar_data)


if __name__ == "__main__":
    main()
