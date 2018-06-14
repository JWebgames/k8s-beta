VERSION ?= v1

.PHONY: \
	messager-build messager-apply messager-delete \
	webapi-build webapi-apply webapi-delete \
	redis-apply redis-delete \
	postgres-apply postgres-delete

build: messager-build webapi-build

apply: messager-apply redis-apply postgres-apply webapi-apply

delete: webapi-delete postgres-delete messager-delete redis-delete

messager-build:
	docker build -t gcr.io/$(PROJECT_ID)/jwebgames-messager:$(VERSION) ../messager
	docker push gcr.io/$(PROJECT_ID)/jwebgames-messager:$(VERSION)

messager-apply:
	kubectl apply -f messager-deployment.yaml
	kubectl apply -f messager-service.yaml

messager-delete:
	kubectl delete -f messager-service.yaml
	kubectl delete -f messager-deployment.yaml

redis-apply:
	kubectl apply -f redis-deployment.yaml
	kubectl apply -f redis-service.yaml

redis-delete:
	kubectl delete -f redis-service.yaml
	kubectl delete -f redis-deployment.yaml

postgres-apply:
	kubectl apply -f postgres-deployment.yaml
	kubectl apply -f postgres-service.yaml

postgres-delete:
	kubectl delete -f postgres-service.yaml
	kubectl delete -f postgres-deployment.yaml

webapi-build:
	docker build -t gcr.io/$(PROJECT_ID)/jwebgames-webapi:$(VERSION) ../webapi
	docker push gcr.io/$(PROJECT_ID)/jwebgames-webapi:$(VERSION)

webapi-apply:
	kubectl apply -f webapi-deployment.yaml
	kubectl apply -f webapi-service.yaml

webapi-delete:
	kubectl delete -f webapi-service.yaml
	kubectl delete -f webapi-deployment.yaml
