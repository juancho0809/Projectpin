test-code:
	poetry run pytest -v

lint-code:
	find . -name "*.py" | xargs pylint

format-code:
	black .

execute-code:
	uvicorn main:app --reload --host 0.0.0.0 -port 8080

generate-requirements:
	poetry export --output requirements.txt --without-hashes
