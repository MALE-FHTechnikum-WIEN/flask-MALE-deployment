@echo off

echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

set pfad=%CD%\flask-app\
echo +Path to catkin_ws=%pfad%

echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

docker run -it --rm -p 5000:5000 --mount type=bind,source="%pfad%\",target=/home/flask_user/flask-app/ --name "1.0"  "flask-male-deployment:latest" "bash"

cmd /k
