build-local:
	python __main__.py


install:
	python -m pip install -r requirements.txt
	python -m pip install pydantic[email]

	