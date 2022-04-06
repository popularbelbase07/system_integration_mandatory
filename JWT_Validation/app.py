from bottle import default_app, request, get, post, redirect, response,run, view, template
import json
import jwt
import uuid
from send_sms import send_sms
from secret import secret
from models import User, save, get_u
from get_phone import phone
from get_code import generate_code


@get("/")
@view("index")
def _():
    return



@post("/validate")
@view("code")
def _():
    jwtdata = json.load(request.body)
    try:
        jwt.decode(jwtdata, key=secret, algorithms=['HS256', ])
        code = generate_code()
        res = send_sms(code)
        
        u = User(mobile= phone, code= str(code))
        userId = str(uuid.uuid4())
        save(userId, u.json())
        
        if res == 200:
            response.set_cookie(name='userId', value=userId)
            return redirect("code")          
    except jwt.InvalidSignatureError:
        return redirect('/')

@get("/code")
@view("code")
def _():
    return

@post("/process")
def _():
    userId = request.get_cookie("userId")
    print(userId)
    code = request.forms.get("code")
    print(code)
    user = get_u(userId)
    user = json.loads(user)
    print(user)
    if user['code'] == code:
        print(f'this is the code: {code}')
        return redirect("/welcome")
    else:
        print(f'code not found')
        return redirect('/')

@get("/welcome")
@view("welcome")
def _():
    return

try:
    #Server AWS (Production)
    import production
    application = default_app()
except:
    #local Machine(Development)
    run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")