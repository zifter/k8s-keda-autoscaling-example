docker-compose-up:
	docker-compose up -d

docker-compose-down:
	docker-compose down

docker-publish:
	docker build -t zifter/k8s-keda-autoscaling-example:latest .
	docker push zifter/k8s-keda-autoscaling-example:latest

run-flask:
	export FLASK_APP=src && export FLASK_ENV=development && pipenv run flask run

run-workers:
	pipenv run rq worker slow queue
