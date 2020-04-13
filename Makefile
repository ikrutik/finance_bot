REMOTE=origin
BRANCH=master

default:
	@cat README.md

# Развернуть свежую версию
deploy: pull clean install_production restart_service

install_and_run: pull clean install_production start_app_pooling

install_production:
	@echo "Install requirements"
	pipenv install --deploy

install_testing:
	@echo "Install requirements"
	pipenv install --dev

pull:
	@echo "Git checkout pull ${REMOTE} ${BRANCH}"
	git fetch ${REMOTE}
	git pull ${REMOTE} ${BRANCH}

checkout:
	@echo "Git checkout to $(COMMIT)"
	git checkout $(COMMIT)

clean:
	@echo "Cleaning Python compiled files:"
	find . -name __pycache__ -exec rm -fr {} +
	find . -name '*.pyc' -delete

# Run as app pooling via pipenv
start_app_pooling:
	@echo "Restarting app as pooling:"
	pipenv run python src/rest/applications/aiogram/application.py

start_app_webhook:
	@echo "Restarting app as webhook:"
	pipenv run python src/rest/applications/aiogram/application.py --mode=webhook

stop_app_webhook:
	@echo "Stopping app:"
	sudo kill $(sudo lsof -t -i:${RUN_PORT})

# Run as app via systemd
start_service: restart_service
restart_service:
	@echo "Restarting service:"
	sudo /bin/systemctl restart finance.service
	sudo /bin/systemctl --no-pager status finance.service

stop_service:
	@echo "Stopping service:"
	sudo /bin/systemctl stop finance.service
