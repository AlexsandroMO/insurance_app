from django.test import TestCase

# Create your tests here.

#CPF
#https://pypi.org/project/django-cpf/

#pip install -r requirements.txt, pip install django-filter

#pip install django-cpffield


#<!-- <script src="http://jqueryjs.googlecode.com/files/jquery-1.3.2.js" type="text/javascript"></script> -->
#<script src="http://code.jquery.com/jquery-1.8.2.js"></script>
#<script src="http://code.jquery.com/ui/1.9.0/jquery-ui.js"></script>


'''#==============================================
Heroku Deploy

code:
heroku login

code:
pip install django-heroku

- vai na pasta raiz do danjo em settings e adiciona em cima 
import django_heroku

- Vai no final e coloca:
django_heroku.settings(locals())


code:
pip freeze > requirements.txt

-dentro de requirements.txt adicione gunicorn==20.1.0 e salva

- cria um arquivo chamado Procfile (sem extensão) e escreva gunicorn caminho do wsgi = "insurance_control.wsgi"
web: gunicorn insurance_control.wsgi

code:
git init

code:
git status

code:
heroku git:remote -a insurance-control-app		(nome da branch)

code:
git add .

code:
git commit -m "configuração-heroku"

code:
git push -u heroku main

------------- Agora... --------------------------------

code:
heroku run python manage.py migrate


code:
heroku run python manage.py runserver

code:
heroku logs

code:
heroku restart

web: gunicorn <filename>:<main method name>
					
web: gunicorn insurance.wsgi

heroku ps:scale web=1
'''