
from flask import Flask
from mongokit import Connection, Document

# configuration
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

# create the little application object
app = Flask(__name__)
app.config.from_object(__name__)

# connect to the database
connection = Connection(app.config['MONGODB_HOST'],
                        app.config['MONGODB_PORT'])


def max_length(length):
    def validate(value):
        if len(value) <= length:
            return True
        raise Exception('%s must be at most %s characters long' % length)
    return validate

class Ad(Document):
    structure = {
        'AdName': unicode,
        'tagline': unicode,
        'product':unicode,
        'email': unicode,
    }
    validators = {
        'AdName': max_length(50),
        'email': max_length(120)
    }
    use_dot_notation = True
    def __repr__(self):
        return '<User %r>' % (self.AdName)

# register the User document with our current connection
connection.register([Ad])
collection = connection['test1'].ads
ad1 = collection.Ad()
ad1['AdName'] = u'Nirma'
ad1['email'] = u'admin@localhost'
ad1.save()
print ad1
print list(collection.Ad.find())

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
