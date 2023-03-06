#IMPORTS & DECLARATIONS
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from task import tasks
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'
route_base = '/tasks'

#ROUTERS
@app.route('/')
def test():
    return jsonify({"message": "server on work on!"})

@app.route(route_base, methods=['GET'])
@cross_origin()
def getActivities():
    return jsonify({'activities':tasks})

@app.route(route_base+'/<int:task_id>', methods=['GET'])
def getActivity(task_id): 
    taskFound = [task2 for task2 in tasks if task2['activityId'] == task_id]

    if(len (taskFound) > 0):
        return jsonify({'ACTIVIDAD ENCONTRADA':taskFound[0]})
    return jsonify({"message": "ACTIVIDAD NO ENCONTRADA"})

@app.route(route_base, methods=['POST'])
def addActivity():
    json = request.get_json(force=True)
    new_task  =  {
        "activityId" : json['activityId'],
        "title" : json['title'],
        "type" : json['type'],
        "startDate" : json['startDate'],
        "endDate" : json['endDate'],
        "status" : json['status']
    }
    tasks.append(new_task)
    print(new_task)
    return jsonify({"message": "ACTIVIDAD CREADA"})
#START SERVER
if __name__  == '__main__':
    app.run(host="0.0.0.0",  debug=True, port=4001)