server:
	python manage.py runserver

make_migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate --run-syncdb