# RED

This project is to put learning into practice
- Class-based views: 
    - TemplateView
    - ListView
    - DetailView
    - CreateView
    - DeleteView
- Authentication
- Registers
- Profiles
- Pages

Basic commands
```
$ docker-compose -f local.yml build
$ docker-compose -f local.yml up -d
$ docker-compose -f local.yml down -v
$ docker-compose -f local.yml down -v --remove-orphans 
$ docker-compose -f local.yml run --rm django python manage.py createsuperuser
$ docker-compose -f local.yml run --rm django python manage.py makemigrations
$ docker-compose -f local.yml run --rm django python manage.py migrate
$ docker-compose -f local.yml run --rm django python manage.py start app <nameApp>
```


**Ever Ruiz Diaz**, *Software Developer* - [Portfolio](http://everdev.pythonanywhere.com/)