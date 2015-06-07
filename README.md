# random_app

random code as a service
provide a rest api service.
support versioning.

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

return a json:

   {
  "code": "53", 
  "time_out": 100, 
  "uuid": "23022675170252"
   }


GET:
====

   curl -X GET -H "Content-Type: application/json" 127.0.0.1:5001/random/15

return:
200 ok/404 not found

DELETE
======

   curl -X DELETE -H "Content-Type: application/json" 127.0.0.1:5001/random/15

VERSION SUPPORT
===============

currently random service support versioning, we need to put a version in Header, eg:
"X-Version: 1.011", the service will return error if version request is not supported in error message.

curl -X POST -H "Content-Type: application/json" -H "X-Version: 1.011" http://localhost:5001/random -d '{"length": 2, "time_out": 100}'
{
  "error": "1.011000 is not support! min=1.000000, max=1.010000"
}
