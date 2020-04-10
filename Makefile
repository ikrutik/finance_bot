REMOTE=origin
BRANCH=master

default:
	@cat README.md

# Развернуть свежую версию
deploy: pull clean install_production restart_app

# Установка Production
install: ENVIRONMENT=production
install: install_production

# Установка Testing
install_test: ENVIRONMENT=testing
install_test: install_testing


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

restart_bot:
	@echo "Restarting finance-bot:"
	sudo /bin/systemctl restart finance-bot
	sudo /bin/systemctl --no-pager status finance-bot

stop_bot:
	@echo "Stopping web app:"
	sudo /bin/systemctl stop finance-bot
