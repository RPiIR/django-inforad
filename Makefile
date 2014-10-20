
run:
	python ./manage.py runserver 10.0.0.20:8123

db:
	python ./manage.py syncdb

env:
	source env/bin/activate

requirements: requirements.txt
	pip install -r requirements.txt

