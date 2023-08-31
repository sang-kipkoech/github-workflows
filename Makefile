
.PHONY: lint
lint:
	pre-commit run --all-files

.PHONY: install
install:
	python -m pip install --upgrade pip
	if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
