
from flask import Flask,request, render_template, g, session,redirect, Response
from mongokit import Connection, Document
import os,sys
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = '/Users/Siri/Documents/cn'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.urandom(24)

# configuration
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

# create the little application object
app.config.from_object(__name__)

# connect to the database
connection = Connection(app.config['MONGODB_HOST'],
                        app.config['MONGODB_PORT'])

"""@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()"""

def max_length(length):
    def validate(value):
        if len(value) <= length:
            return True
        raise Exception('%s must be at most %s characters long' % length)
    return validate
    

class Person(Document):
    structure = {
        'Name': unicode,
        'email': unicode,
        'location':unicode,
    }
    use_dot_notation = True
    def __repr__(self):
        return '<User %r>' % (self.Name)

#Schema for security form
class UserDetails(Document):
    structure = {
        'name': unicode,
        'email': basestring,
        'location':unicode,
        'ssn' : basestring,
    }
    use_dot_notation = True
    def __repr__(self):
        return '<User %r>' % (self.Name)

class webUser(Document):
    structure = {
        'Name': unicode,
        'email': unicode,
        'password': unicode,
    }
    use_dot_notation = True
    def __repr__(self):
        return '<User %r>' % (self.Name)
    
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/login")
def loginPage(): #login page rendered
    return render_template("login.html")
    #return "Hello World!"

@app.route("/signup")
def signup(): #sign up page rendered
    return render_template("signup.html")
    #return "Hello World!"

@app.route('/log', methods=['POST'])
def newUser(): #make a session for the user who logs in
    #print "please"
    email = request.form['email']
    password = request.form['password'] 
    connection.register([webUser])
    collection = connection['test1'].webusers
    curUser=collection.find_one({'email': email,'password':password})
    try:
        session['username']=email
    except:
        print sys.exc_info()[0]
    if curUser:
        print "found",curUser['email'],curUser['password']
        return redirect('/userinfo')
    else:
        #context=dict(error1="User not Found!")
        return render_template("signup.html",error="User not found, please sign up!")
    
@app.route('/new', methods=['POST'])
def add(): #add a new user redirected from sign up
    print "please"
    name = request.form['name']
    email = request.form['email']
    password = request.form['password'] 
    connection.register([webUser])
    collection = connection['test1'].webusers
    user = collection.webUser()
    user['Name'] = name
    user['email'] = email
    user['password'] = password
    print "added!",name,email
    user.save()
    #session['username']=email
    return redirect('/login')
    
@app.route('/userinfo',methods=['GET','POST'])
def userinfo(): 
    print "hello! in userinfo"

    d={}
    try:
        connection.register([UserDetails])	
        collection = connection['test1'].userdetails
        user1 = collection.UserDetails()
        record=collection.find_one({'email':session['username']}) #some email value)
        print "bitch",record
    except:
        print sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]
    if record :
        try:
            record.name = request.form['name']
            #record.email = request.form.get['email']
            record.ssn = request.form['ssn']
            record.location = request.form['location']
            d.update({"name":record.name},{"mail":session['username']},{"ssn":record.ssn},{"location":record.location})
        except:
            print sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]
    else:
        try:
            print "hiiiiiiii"
            user1['name'] = u''
            user1['email'] = str(session['username'])
            user1['location'] = u''
            user1['ssn'] = ""
            user1.save()
            print "added! to UserDetails"
            d.update({"name":""},{"mail":session['username']},{"ssn":""},{"location":""})
        except:
            print sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]
            #pass
        #d.update({name"})    
    context=d
    print context
    return render_template("display.html",**context)

    
@app.route("/read")
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
