pip install pipenv

to start virtual env  ->
pipenv shell 


pip install face_recognition

find matches
face_recognition  ./img/known ./img/unknown


lookalike matches -> distance on each match

face_recognition --show-distance true  ./img/known ./img/unknown -> this will show match along with decimal value(less is good)


set tolerance

face_recognition --tolerance 0.50  ./img/known ./img/unknown 


just names->

face_recognition ./img/known ./img/unknown | cut -d ',' -f2

adjust cpu->
face_recognition --cpus 8 ./img/known ./img/unknown
