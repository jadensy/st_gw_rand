ENV := env

clean-env:
	rm -rf $(ENV)

install:
	python3 -m venv $(ENV)

init: install
	$(ENV)/bin/python3 -m pip install --upgrade pip
	$(ENV)/bin/pip install -r requirements.txt

run:
	@if [ -d "$(ENV)" ]; \
		then echo "Running app..." &&  env/bin/streamlit run guesswho_randomiser.py; \
		else echo "Run: make init"; \
	fi
