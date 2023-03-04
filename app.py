#IMPORTS & DECLARATIONS
from flask import Flask, jsonify, request
from task import tasks
app = Flask(__name__)
route_base = '/tasks'
#ROUTERS
@app.route('/')
def test():
    return jsonify({"message": "server on work on!"})

@app.route(route_base, methods=['GET'])
def getTasks():
    return jsonify({'LISTA DE TAREAS':tasks})

@app.route(route_base+'/<int:task_id>', methods=['GET'])
def getTask(task_id): 
    taskFound = [task2 for task2 in tasks if task2['activityId'] == task_id]

    if(len (taskFound) > 0):
        return jsonify({'TAREA ENCONTRADA':taskFound[0]})
    return jsonify({"message": "TAREA NO ENCONTRADA"})

@app.route(route_base, methods=['POST'])
def addTask():
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
    return 'recived'
#START SERVER
if __name__  == '__main__':
    app.run(host="0.0.0.0",  debug=True, port=4001)