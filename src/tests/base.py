from py_iztro import Astro


def main():
    astro = Astro()
    result = astro.by_solar("2000-8-16", 2, "女")
    print(result.model_dump_json(by_alias=True, indent=4))


if __name__ == "__main__":
    main()
