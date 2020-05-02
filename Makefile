.PHONY: help
help:
	@echo "Usage:"
	@echo "    help:    Prints this screen"
	@echo "    build:   Build superset"
	@echo "    run:     Run superset"
	@echo "    init-db: Initalize the database"
	@echo ""

.PHONY: build
build:
	docker build -t coa-superset .

.PHONY: run
run:
	docker run --rm \
		-e DB_USERNAME \
		-e DB_PASSWORD \
		-e DB_SERVER \
		-e DB_PORT \
		-e DB_DATABASE \
		-e SECRET_KEY \
		-e MAPBOX_API_KEY \
		-p 8088:8088 \
		--name coa-superset \
		coa-superset

.PHONY: init-db
init-db:
	docker exec -it coa-superset superset-init
