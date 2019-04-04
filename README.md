# dipu bbs
V2EX-like static forum system, integrating register, sign in, post, reply, profile editing, selfie uploading function
![image](https://raw.githubusercontent.com/milespercival/miles_bbs/master/app/static/screen_shot/ss1.png)
![image](https://raw.githubusercontent.com/milespercival/miles_bbs/master/app/static/screen_shot/ss2.png)
![image](https://raw.githubusercontent.com/milespercival/miles_bbs/master/app/static/screen_shot/ss3.png)
![image](https://raw.githubusercontent.com/milespercival/miles_bbs/master/app/static/screen_shot/ss4.png)
![image](https://raw.githubusercontent.com/milespercival/miles_bbs/master/app/static/screen_shot/ss5.png)
## Last Test Version
flask 1.0.2
python 3.6.6

## Install
### 1.prepare runtime environment
```
$ git clone https://github.com/ethanmiles/dipu_bbs && cd dipu_bbs
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt
```
### 2.initial config
```
$ cd app
$ touch config.py
$ vim config.py
```
e.g.
```
SECRET_KEY = 'huaq'

MONGODB_SETTINGS = {
    'db': 'your.db.name', 
    'host': 'your.ip',
    'port': 27017,
}

SALT = キズナアイ'
```
### 3.Start
```
$ python3 run.py
```
