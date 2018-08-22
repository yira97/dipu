# miles_bbs

##Module Version
flask 1.0.2
python 3.6.6

##Installation Step
0.prepare virtual environment
```
$ mkdir my_work_dir
$ cd my_work_dir
$ python3 -m venv venv
$ source /venv/bin/activate
```
1.create config
```
$ cd app
$ touch config.py
$ vim config.py
```

--config.py--
SECRET_KEY = 'xxxxx'

MONGODB_SETTINGS = {
    'db': 'bbs',
    'host': 'localhost',
    'port': 27017
}

SALT = 'xxx'

2.Start
$ cd ..
$ python3 run.py
