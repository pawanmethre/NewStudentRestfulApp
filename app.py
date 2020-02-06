from flask import Flask
from flask_restful import Api
import sys
sys.path.append('/home/pawan/PycharmProjects/StudentApp')
from entities.student_entity import Student, Students
from  entities.user_entity import SignIn, UserRegister
api = Api(app)
api.add_resource(Student, '/student')
api.add_resource(UserRegister, '/auth/register')
api.add_resource(SignIn, '/auth/signIn')
api.add_resource(Students, '/student/students')

if __name__ == '__main__':
    PORT = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=PORT)
