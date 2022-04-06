from bottle import get, default_app, run, view

# https://eu.pythonanywhere.com/
# https://mitid.eu.pythonanywhere.com/
# oracle07.eu.pythonanywhere.com = email address
# password = ?????

#####################################


@get("/")
@view("index")
def _():
    return

################################

try:
    #Server AWS(Production)
    import production
    application= default_app()
except:
    #Local Mechine(development)
        run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")
