# random_app

random code as a service
provide a rest api service.

HOW TO RUN
==========
python /run.py

HOW TO ACCESS
=============
POST
====
genreate a random code:
length is the random code length;
time_out is how long it will be invalid;

example:

   curl -X POST -H "Content-Type: application/json" 127.0.0.1:5001/random -d '{"length": 2, "time_out": 100}'

return:

    "code": "15" ,201


GET:
====

   curl -X GET -H "Content-Type: application/json" 127.0.0.1:5001/random/15

return:
200 ok/404 not found

DELETE
======

   curl -X DELETE -H "Content-Type: application/json" 127.0.0.1:5001/random/15

.
├── app
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── manager.py
│   ├── manager.pyc
│   ├── memorycache.py
│   ├── memorycache.pyc
│   ├── random_code.py
│   ├── random_code.pyc
│   ├── views.py
│   └── views.pyc
├── daocloud.yml
├── Dockerfile
├── README.md
├── run.py
└── tests
    ├── functional
    │   ├── functions.sh
    │   ├── pre-test.sh
    │   └── test.sh
    └── unit

