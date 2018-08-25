# miles_bbs
一个使用flask框架的论坛的简单实现
## Module Version
flask 1.0.2
python 3.6.6
mongodb

## Installation Step
### 0.prepare virtual environment
```
$ python3 -m venv venv
$ source /venv/bin/activate
(venv)$ pip install -r requirements.txt
```
### 1.create config
```
$ cd app
$ touch config.py
$ vim config.py
```

#### file:config.py
```
SECRET_KEY = 'xxxxx'  #ramdom string 

MONGODB_SETTINGS = {    # review your mongodb config
    'db': 'bbs', 
    'host': 'localhost',
    'port': 27017
}

SALT = 'xxx'    #ramdom string 
```
### 2.Start
```
$ python3 run.py
```
