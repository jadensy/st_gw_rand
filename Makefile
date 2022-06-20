ENV := env

clean-env:
	rm -rf $(ENV)

clean-all-repos:
	rm -rf repos/*

clean-dst-repos:
	rm -rf repos/[0-9]*

clean: clean-env clean-all-repos

install:
	python3 -m venv $(ENV)

init: install
	$(ENV)/bin/python3 -m pip install --upgrade pip
	$(ENV)/bin/pip install -r requirements.txt

run:
	@if [ -d "$(ENV)" ]; \
		then echo "Running app..." &&  env/bin/streamlit run self_service_dashboard_migration.py; \
		else echo "Run: make init"; \
	fi

run-debug:
	@if [ -d "$(ENV)" ]; \
		then echo "Running app in DEBUG mode..." &&  env/bin/streamlit run self_service_dashboard_migration.py --logger.level=DEBUG; \
		else echo "Run: make init"; \
	fi
