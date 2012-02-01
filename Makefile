MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=TestTask1.settings $(MANAGE) test main

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=TestTask1.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=TestTask1.settings $(MANAGE) syncdb --noinput
	
migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=TestTask1.settings $(MANAGE) convert_to_south main && PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=TestTask1.settings $(MANAGE) migrate main
