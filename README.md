#To create venv with python3 as default python, add path to command
virtualenv --python=/usr/bin/python3 ENV_NAME

----- sequence of commands i used to install all necessary packages ------

pip -V                                                #check pip version. On my PC it was 10.0.1
virtualenv --version                                  #check virtualenv version. My version is 15.1.0
virtualenv --python=/usr/bin/python3 envDjango        #create new venv with python3 as default
source envDjango2/bin/activate                        #activate our venv
pip install Django==1.11.12                           #install latest LTS version of Django
python -c 'import django;print(django.get_version())  #check Django installation
python -m django --version                            #same 
django-admin startproject projName                    #create project
tree                                                  #check that we have all necessary files and folders
python manage.py runserver                            #start development server to check if everthinh is ok
in browser go to http://127.0.0.1:8000/               #if you see "It worked!"

------ next steps for extra django-registration-redux package installation and configuring -----

http://django-registration-redux.readthedocs.io/en/latest/quickstart.html   #redux documentation
pip install django-registration-redux                                       #install command
pip list                                                                    #check all installed packages

###check INSTALLED_APPS section in settings.py file.
###add three lines if they not exist:

INSTALLED_APPS = (
    'django.contrib.sites',
    'registration',           #should be immediately above 'django.contrib.admin'
    'django.contrib.admin',
    # ...other installed applications...
)

#This settings also required
ACCOUNT_ACTIVATION_DAYS = 7         # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True      # Automatically log the user in.

####Open urls.py file in your project folder and make it look like this
#in short: add accounts line, and add include to first line

        from django.conf.urls import url, include
        from django.contrib import admin

        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^accounts/', include('registration.backends.default.urls')), #add this line
        ]

###Once you’ve done this, run python manage.py migrate to install the model used by the default setup
python manage.py migrate

#Path to django-registration-redux templates
/home/user/work/envs/envDjango2/lib/python3.5/site-packages/registration/templates/registration/registration_base.html

#Create templates folder in your project folder (later we will add path to this folder to settings file)
#copy registration templates folder into templates folder you just created
#registration templates folder located here:
/home/user/work/envs/envDjango2/lib/python3.5/site-packages/registration/templates/

#Find Templates section in settings file, add path to project templates folder:

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/home/user/work/reduxProj/templates/',
            # '',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#Now we need to create superuser account
python manage.py createsuperuser
#and type all necessary data

#now we can test our project settings. To do this, open this page:
http://127.0.0.1:8000/accounts/register/

#if you get an error 'template does not exist'
#it means that path to templates is wrong

#add this to settings after REGISTRATION_AUTO_LOGIN

SITE_ID = 1                         # Without this login and logout mechanism not working

#also SITE_ID is used by redux to send emails with activation links
#we will change default SITE name to our Domain name in future, not now
#you can do it in admin interface in Sites section

#Then we need to check that our registration process is working
#keep in mind that by default our domain name (and site name too) is example.com
#check that you logged out (in case if you already "signed in" in admin interface for example)
#if not, you will be redirecter to '/accounts/profile/' url

#So...
#go to http://127.0.0.1:8000/accounts/register
#fill in all required fields, follow the tips when you create password

#you will get an error 'ConnectionRefusedError at /accounts/register/'  
#or 'smtp bla bla' don't worry, it's ok
#it's because we need to activate our new account

#to do this, login as admin in admin interface
#got to 'registration profiles section'
#click on username you just created and copy given activation key
#add this key to activation url, this url in future will be generated automatically
#by redux application
#see activation url example below paste your activation key instead of ACTIVATION_KEY:
http://127.0.0.1:8000/accounts/activate/ACTIVATION_KEY

#after you will see message 'Your account is now activated.'

#next: try to open page 'http://127.0.0.1:8000/accounts/login'
#you will see 'page not found. error 404' page, it's ok

#next step is to create redirect to 'whatever' page when we succesfully logged in
#go to settings file and add this line
LOGIN_REDIRECT_URL = '/admin/'

#this line will redirect us to admin page when we succesfully logged in
#log out with 'accounts/logout' url and try to log in again 
#you will be redirected to admin page with next message

        # You are authenticated as user, 
        # but are not authorized to access this page. 
        # Would you like to login to a different account? 
        
#django email docs
#https://docs.djangoproject.com/en/dev/topics/email/

#TODO

#create at least one applicateon because we need it in future
#let it be landing page or somthing similar
#change login template and settings to correctly redirect user without errors
#change register/logout templates same way
#configure email sending mecanism, take information from:
#https://www.youtube.com/watch?v=bhzasigpf3Q

#next video mayby will help in future
#https://www.youtube.com/watch?v=A-7vGF_pEss


#to create app with name landing, type this:
python manage.py startapp landing

#then open file landing/views.py and create our first view


from django.http import HttpResponse

def landing_view(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#next we need to create url that will lead user to landing_view
#create landing/views.py file and create url like this:

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.landing_view, name='landing'),
]

#also we need to include our new landing/views.py file in main urls.py file
#open projname/urls.py file
