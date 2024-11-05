from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
#Creo un Endpoint de tipo GET que retorna en formato json todas las todos 
# que tenemos almacenadas en la variable todos que es un arreglo de objetos 
@app.route('/todos', methods=['GET']) 
def hello_world():
    return jsonify(todos)

#Creo otro Endpoint con la misma url que tiene el metodo POST 


@app.route('/todos', methods=['POST'])
def add_new_todo(): #agreganmos una nueva tarea
    request_body = request.json #Extraemos el body de nuestra request 
    print("Incoming request with the following body", request_body) #imprimimos el body en la consola para ver que recibimos
    todos.append(dict(request_body)) # le agregamos a la variable todos un nuevo diccionario con la variable request_body que es lo que estamos recibiendo  
    return jsonify(todos) #devuelvo la lista actualizada de todos 



@app.route('/todos/<int:position>', methods=['DELETE']) #recibimos una posicion (Int position), se parsea de forma automatica como un entero 
def delete_todo(position): #recibo la position en la funcion 
    print("This is the position to delete:", position)
    del todos[position] #uso la palabra reservada DEL (eliminar), coloco la lista de la que quiero eliminar informacion y la posicion de la cual quiero eliminar la informacion
    return jsonify(todos) #retorno todas las tareas actualizadas 






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)