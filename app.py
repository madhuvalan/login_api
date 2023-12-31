from flask import Flask, request
import validations

app = Flask(__name__)

@app.route('/')
def read():
    return {"status":200,"message":"helloworld"}

@app.route('/signup', methods=['POST'])
def credentials_signup():
    request_data = request.get_json()
    username = request_data.get("username")
    password = request_data.get("password")   
    if username is None or password is None:
        return  {"message":"Missing username, password fields in the request"}
    username_validation = validations.checks(username)
    password_validation = validations.checks(password)
    status = all([username_validation.get("status"),
                    password_validation.get("status") ])
    if status:
        return {"status": "status from db update", "msg": "msg from db_update"}
    else:
        return {"status": status, "username": username_validation.get("msg"),
                "password":password_validation.get("msg")}



if __name__ == '__main__':
    app.run()