#week-8
from unittest import result
from bottle import error, get,hook, post, put, request, response, run
import json
import uuid

items = [
    {"id":"a95c0155-1268-4d83-bdec-e9f283dea576", "name": "Everest", "last_name": "Nepal"},
    {"id":"d73625d4-ed05-4e75-b91d-0df16d71c9c1", "name": "Everest", "last_name": "Nepal"}
]
#######################      Hook    ###################
@hook("after_request")
def _():
    response.content_type = "application/json"


##################     Home route     ###################
@get("/")
#First entry point for api
def _():
    return "home"

####################    GET   #########################

@get ( "/items")
def _():
    return json.dumps(items)

####################    GET by id   #########################
@get("/items/<item_id>")
def _(item_id):
    # list Comperenhension
    # The structure of code that in the delete function is almost same we can use for loop also
    matches = [ item for item in items if item["id"] == item_id ]
    if not matches:
       response.status = 204
       return

    return matches[0]
       
######################   POST   ######################
@post("/items")
def _():
    item_id = str(uuid.uuid4())
    item_name = request.json.get("name")
    item  = {"id": item_id, "name":item_name}
    items.append(item)
    print( type(item_id) )
    response.status = 201
    return {"id"}


###################################  Put  ###############################
@put("/items/<item_id>")            #patch
def _(item_id):
    try:
        
        # list Comperenhension
        item = [ item for item in items if item ["id"] == item_id][0]

        # for small data well but big data it is not the gppd approach
       # if request.json.get("name"): item["name"] = request.json.get("name")
       # if request.json.get("last_name"): item["last_name"] = request.json.get("last_name")

        for key in item.keys():
            if key in request.json.keys():
                item[key] = request.json.get(key)        

        return item
    except Exception as ex:
        print(ex) 
        response.status = 204
        return





###################################  Delete  ###############################
    @delete("/items/<item_id>")
    def _(item_id):
        for index, item in enumerate(items):
            if item["id"] == item_id:
                items.pop(index)
                return {"info":"item deleted"}
        
        return
        # what ? this is not desplayed in the client because of the response status is 204
        response.status = 204
       # return json.dumps({"info": f"item with id {item_id} not found"})

      


############################# Error   ##################
@error(404)
def _(error):
    response.content_type = "application/json"
    return json.dumps({"info":"Page not found"})

          


#port nubers = 65535
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")