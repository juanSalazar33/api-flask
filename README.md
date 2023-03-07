# simple api-flask 

# 1. install and run Docker on your computer:
     https://www.docker.com/

# 2. in cmd terminal run:
    docker build -t flaskapp .

# 3. in cmd terminal run: 
    docker run -p 7000:4001 -d flaskapp

# if you want developer i recomend use virtual environment:
    python3 -m venv env

# if you add new dependencies run:
    pip freeze > requirments.txt

