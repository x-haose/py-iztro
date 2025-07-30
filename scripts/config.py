from py_iztro import Astro
from py_iztro.core.models import ConfigModel


def main():
    astro = Astro()
    config = astro.get_config()
    print(f"默认配置: {config.model_dump_json(indent=4)}")

    config_model = ConfigModel(
        mutagens={"庚": ["太阳", "武曲", "天同", "天相"]},
        brightness={"贪狼": ["旺", "旺", "旺", "旺", "旺", "旺", "旺", "旺", "旺", "旺", "旺", "旺"]},
    )
    astro.config(config_model)
    config = astro.get_config()
    print(f"修改后配置: {config.model_dump_json(indent=4)}")


if __name__ == "__main__":
    main()
