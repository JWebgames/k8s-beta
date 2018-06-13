VERSION ?= v1

.PHONY: \
	messager-build messager-apply messager-delete \
	webapi-build webapi-apply webapi-delete

build: messager-build webapi-build

apply: messager-apply webapi-apply

delete: messager-delete webapi-delete

messager-build:
	docker build -t gcr.io/$(PROJECT_ID)/jwebgames-messager:$(VERSION) ../messager
	docker push gcr.io/$(PROJECT_ID)/jwebgames-messager:$(VERSION)

messager-apply:
	kubectl apply -f messager-deployment.yaml
	kubectl apply -f messager-service.yaml

messager-delete:
	kubectl delete -f messager-service.yaml
	kubectl delete -f messager-deployment.yaml

webapi-build:
	docker build -t gcr.io/$(PROJECT_ID)/jwebgames-webapi:$(VERSION) ../webapi
	docker push gcr.io/$(PROJECT_ID)/jwebgames-webapi:$(VERSION)

webapi-apply:
	kubectl apply -f webapi-deployment.yaml
	kubectl apply -f webapi-service.yaml

webapi-delete:
	kubectl delete -f webapi-service.yaml
	kubectl delete -f webapi-deployment.yaml
