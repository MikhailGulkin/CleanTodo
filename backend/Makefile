CONFIG_DEV_TEST_PATH='./config/dev-test-config.toml'
up-server:
	python3.11 -m src
upd-req:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
up-dev:
	docker-compose -f docker-compose.dev.yaml -p dev up --build --no-attach postgres --no-attach rabbitmq
up-tests:
	docker-compose -f docker-compose.test.yaml -p test up --build --no-attach test-db --no-attach rabbitmq
up-dev-tests:
	docker-compose -f docker-compose.dev.test.yaml -p dev-test up --build

migrate-dev-test:
	CONFIG_PATH=$(CONFIG_DEV_TEST_PATH) alembic upgrade head

run-dev-tests:
	CONFIG_PATH=$(CONFIG_DEV_TEST_PATH) pytest -v -s

# source $(poetry env info --path)/bin/activate
run-lint:
	pre-commit run --all-files
