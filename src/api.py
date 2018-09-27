from flask import Flask, jsonify
from flask_restplus import (Resource,
                            Api,
                            cors,
                            inputs,
                            fields)
from flask_mail import Mail, Message

app = Flask(__name__)
api = Api(app, title='SMail Api', description='An Api for send secure mail')
mail = Mail(app)

message_model = api.model("message", {
    "_id": fields.String(description='ID'),
    "from": fields.String(description='Name'),
    "message": fields.String(description='Content message')
})

@api.route('/send/<login>/')
class SendMessage(Resource):
    @cors.crossdomain(origin='*')
    @api.expect(message_model, validate=True)
    @api.doc(body=message_model)
    def post(self, login):
        data = api.payload
        msg = Message('Secure message', sender=data["from"], recipients=["{}@px.io".format(login)])
        msg.body = data["message"]
        with app.app_context():
            mail.send(msg)
        return jsonify({'msg': 'send to {}'.format(login)})

if __name__ == '__main__':
    app.run(debug=True)
