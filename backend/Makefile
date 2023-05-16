up-server:
	python3.11 -m src.__main__
upd-req:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
up-tests:
	docker-compose -f docker-compose.test.yaml -p test up --build --no-attach test-db --no-attach rabbitmq
up-dev-tests:
	docker-compose -f docker-compose.dev.test.yaml -p dev-test up --build
migrate-dev-test:
	export CONFIG_PATH='./config/dev-test-config.toml' && alembic upgrade head
run-dev-tests:
	CONFIG_PATH='./config/dev-test-config.toml' pytest -v -s

# source $(poetry env info --path)/bin/activate
