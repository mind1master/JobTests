MANAGE=django-admin.py

test:
	PYTHONPATH=../uwsgi DJANGO_SETTINGS_MODULE=settings_deploy $(MANAGE) test main

run:
	PYTHONPATH=../uwsgi DJANGO_SETTINGS_MODULE=settings_deploy $(MANAGE) runserver

syncdb:
	PYTHONPATH=../uwsgi DJANGO_SETTINGS_MODULE=settings_deploy $(MANAGE) syncdb --noinput
	
migrate:
	PYTHONPATH=../uwsgi DJANGO_SETTINGS_MODULE=settings_deploy $(MANAGE) convert_to_south main && PYTHONPATH=../uwsgi DJANGO_SETTINGS_MODULE=settings_deploy $(MANAGE) migrate main
