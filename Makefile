.PHONY: sb spt sp check check_i

sb:
	rm -rf ./dist
	uv build

publish_testpypi:
	uv run twine upload -r testpypi dist/*

publish_pypi:
	uv run twine upload dist/*

test: sb publish_testpypi

release: sb publish_pypi

check:
	uv run pre-commit run --all-files

check_i:
	uv run pre-commit install
