usage:
	@echo "Available commands: "
	@echo
	@echo "\t start - run all application services"
	@echo "\t stop - stop application services"
	@echo "\t build_frontend - build frontend"
	@echo "\t load_data - load markets data from API"
	@echo "\t test - run tests"
	@echo "\t lint - run pylint for python code"
	@echo "\t migrate - run django migrations"
	@echo "\t shell - enter to django shell"
	@echo

start:
	@docker-compose up -d

stop:
	@docker-compose down

build_frontend:
	@cd frontend; npm run-script build

load_data:
	@docker-compose run web python manage.py load_data

test:
	@docker-compose run web python manage.py test

lint :
	@docker-compose run web pylint --load-plugins pylint_django core btccharts

migrate:
	@docker-compose run web python manage.py migrate

shell:
	@docker-compose run web python manage.py shell
