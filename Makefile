requirements:
	poetry export -f requirements.txt --output req-dev.txt --dev
	poetry export -f requirements.txt --output req-prod.txt

.PHONY: requirements

