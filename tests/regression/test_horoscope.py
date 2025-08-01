import json
from pathlib import Path

from py_iztro.core.astro import Astro
from py_iztro.core.models import HoroscopeModel


def test_horoscope(test_data_dir: Path):
    json_path = test_data_dir / "horoscope.json"
    with open(json_path, encoding="utf-8") as f:
        expected = HoroscopeModel.model_validate(json.load(f))

    astro = Astro()
    astrolabe = astro.by_solar("2000-8-16", 2, "女")
    result = astrolabe.horoscope("2025-01-01").model_dump_json(by_alias=True)
    assert result == expected.model_dump_json(by_alias=True)
