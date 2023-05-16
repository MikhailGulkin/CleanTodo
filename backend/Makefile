up-server:
	python3.11 -m src.__main__
upd-req:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
up-tests:
	docker-compose -f docker-compose.test.yaml -p test up --build --no-attach test-db --no-attach rabbitmq
