# django-router-tutorial

Tutorial for use [Django Router](https://pypi.org/project/django-router/).

## This project was done with:

* [Python 3.12](https://www.python.org/)
* [Django 5.1.3](https://www.djangoproject.com/)
* [Django Router 1.0.8](https://pypi.org/project/django-router/)

## How to run project?

* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Run the migrations.

```
git clone https://github.com/rg3915/django-router-tutorial.git
cd django-router-tutorial

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python contrib/env_gen.py

python manage.py migrate
python manage.py runserver
```

## Este projeto foi feito com:

* [Python 3.12](https://www.python.org/)
* [Django 5.1.3](https://www.djangoproject.com/)
* [Django Router 1.0.8](https://pypi.org/project/django-router/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django-router-tutorial.git
cd django-router-tutorial

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python contrib/env_gen.py

python manage.py migrate
python manage.py runserver
```

## show urls

Digite

```
python manage.py show_urls
```

```python
/   apps.core.views.index   core:index
/accounts/login/    django.contrib.auth.views.LoginView login
/accounts/logout/   django.contrib.auth.views.LogoutView    logout
/accounts/signup/   apps.accounts.views.SignUpView  accounts:signup
/admin/ django.contrib.admin.sites.index    admin:index
...
/crm/person-export-csv/ apps.crm.views.person_export_csv    crm:person_export_csv
/crm/person/    apps.crm.views.PersonListView   crm:person_list
/crm/person/    apps.crm.views.person_list  crm:person_list
/crm/person/<int:pk>/   apps.crm.views.PersonDetailView crm:person_detail
/crm/person/<int:pk>/   apps.crm.views.person_detail    crm:person_detail
/crm/person/<int:pk>/delete/    apps.crm.views.PersonDeleteView crm:person_delete
/crm/person/<int:pk>/delete/    apps.crm.views.person_delete    crm:person_delete
/crm/person/<int:pk>/update/    apps.crm.views.PersonUpdateView crm:person_update
/crm/person/<int:pk>/update/    apps.crm.views.person_update    crm:person_update
/crm/person/add/    apps.crm.views.person_create    crm:person_create
/crm/person/create/ apps.crm.views.PersonCreateView crm:person_create
/crm/person/export/csv/ apps.crm.views.person_export_csv2   crm:person_export_csv2
/crm/person/export/excel/   apps.crm.views.person_export_excel  crm:person_export_excel
```
