# virtualenv and run application
dev_run:
	. venv/bin/activate && gunicorn -c gunicorn.conf --chdir app/ main:app

venv:
	virtualenv -p /usr/bin/python3 venv/ && make venv_install_reqs && make venv_install_reqs_dev

venv_install_reqs:
	. venv/bin/activate && pip install -r requirements.txt

venv_install_reqs_dev:
	. venv/bin/activate && pip install -r requirements_dev.txt

# tests and maintaining code
black_all:
	. venv/bin/activate && black -l 119 -S app/ unittests/

test-unittests:
	. venv/bin/activate && \
	export PYTHONPATH=$PYTHONPATH:app/ && \
	python -m pytest app/ unittests/ -vv -s -ra --cov --cov-report term-missing:skip-covered --cov-fail-under=75 --pylama && \
	rm -r ".coverage" ".pytest_cache" && find app unittests -name "__pycache__" -exec rm -rf {} +
