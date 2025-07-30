from functools import cached_property

from py_iztro import Astro
from py_iztro.core.models import AstrolabeModel


class TestAstroGeneration:
    GEORGIAN_DATE = "2000-8-16"
    LUNISOLAR_DATE = "2000-7-17"
    GENDER = "女"
    TIME_IDX = 2
    astro = Astro()

    @cached_property
    def expected_result(self) -> AstrolabeModel:
        # just do not want to load the expected result twice
        with open("tests/data/astro.json", encoding="utf-8") as f:
            return AstrolabeModel.model_validate_json(f.read())

    def test_astrolabe_from_georgian_calendar(self):
        astrolabe = self.astro.by_solar(self.GEORGIAN_DATE, self.TIME_IDX, self.GENDER)
        assert astrolabe.model_dump_json(by_alias=True) == self.expected_result.model_dump_json(by_alias=True)

    def test_astrolabe_from_lunisolar_calendar(self):
        astrolabe = self.astro.by_lunar(self.LUNISOLAR_DATE, self.TIME_IDX, self.GENDER)
        assert astrolabe.model_dump_json(by_alias=True) == self.expected_result.model_dump_json(by_alias=True)
