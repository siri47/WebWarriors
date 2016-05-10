
from flask import Flask,request, render_template, g, session,redirect, Response
from mongokit import Connection, Document
import os
from flask import Flask, request, redirect, url_for
#from werkzeug import secure_filename

UPLOAD_FOLDER = '/Users/Siri/Documents/cn'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# configuration
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

# create the little application object
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
    

class Person(Document):
    structure = {
        'Name': unicode,
        'email': unicode,
        'location':unicode,
    }
    use_dot_notation = True
    def __repr__(self):
        return '<User %r>' % (self.Name)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/login")
def loginPage():
    return render_template("login.html")
    #return "Hello World!"

@app.route("/signup")
def signup():
    return render_template("signup.html")
    #return "Hello World!"
    
@app.route('/userinfo',methods=['GET','POST'])
def userinfo():
    return render_template("details.html")
    
@app.route("/data/read")
def displayPersons():
    # register the User document with our current connection
    connection.register([Ad])
    collection = connection['test1'].ads
    ad1 = collection.Ad()
    ad1['AdName'] = u'Nirma'
    ad1['email'] = u'admin@localhost'
    ad1.save()
    print ad1
    #print list(collection.Ad.find())      
    return "added"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
if __name__ == "__main__":
    app.run()
