# 프로젝트 개요
- Python Django로 To-do List를 만들어본다. 

# 파이썬 설치
- 파이썬 설치는 Anaconda 또는 Python 홈페이지에서 직접 설치한다.
    + Anaconda : https://www.anaconda.com/
    + Python : https://www.python.org/

# 가상환경 설치
- 파이썬 설치가 끝났다면, 해당 깃허브를 다운로드 받는다.  
```bash 
$ git clone https://github.com/dschloe/django_to_do.git
```

- django_to_do 폴더에 진입 후 아래와 같이 실행한다. 
```bash
$ cd django_to_do
$ virtualenv venv
created virtual environment CPython3.9.7.final.0-64 in 7884ms     
  creator CPython3Windows(dest=C:\Users\human\Desktop\django_to_do\venv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\human\AppData\Local\pypa\virtualenv)
    added seed packages: pip==22.0.4, setuptools==62.1.0, wheel==0.37.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
```

- 실제 실행 후 venv 폴더가 나타나는지 확인한다. 
```bash
$ ls
README.md  venv/
```

- 가상환경에 접속한다. 
```bash
$ source venv/Scripts/activate
(venv)
```

# 환경 설정 Django

## Installing Django
- Django : https://www.djangoproject.com/
- 가상환경이 접속된 상태에서 django를 설치한다. 
```bash
$ pip install django
```

## my_app 폴더 생성
- 새로운 폴더 `my_app` 하나 생성한다. 
``
