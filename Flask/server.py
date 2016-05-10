
from flask import Flask,request, render_template, g, session,redirect, Response,send_file
from mongokit import Connection, Document
import os,sys
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
from Crypto.Cipher import AES

UPLOAD_FOLDER = '/Users/Siri/Documents/cn'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
ecb_key = "1234567891234567"
imagepath = '/Users/Siri/Documents/ms/ColumbiaSpring/TopicsSE/project/test/mkdir.png'
videopath = '/Users/Siri/Documents/ms/ColumbiaSpring/TopicsSE/project/test/sample.mp4'

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

def max_length(length):
    def validate(value):
        if len(value) <= length:
            return True
        raise Exception('%s must be at most %s characters long' % length)
    return validate
    

class Person(Document):
    structure = {
        'name': basestring,
        'email': basestring,
        'location':basestring,
    }
    use_dot_notation = True
    def __repr__(self):
        return '<User %r>' % (self.Name)

#Schema for security form
class UserDetails(Document):
    structure = {
        'name': basestring,
        'email': basestring,
        'location':basestring,
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

@app.route("/dataView")
def view():
    connection.register([Person])
    collection = connection['test1'].person 
    return str(list(collection.find()))
 
@app.route("/dataAdd")
def displayPersons():
    # Add some rows
    connection.register([Person])
    collection = connection['test1'].person    
    for i in range(1001):
        pers = collection.Person()
        pers['name'] = 'Nirma'
        pers['email'] = 'admin@localhost'
        pers['location'] = 'nyc'
        pers.save()
    #print list(collection.Ad.find())      
    return "Added"

@app.route("/login")
def loginPage(): #login page rendered
    return render_template("login.html")

@app.route("/signup")
def signup(): #sign up page rendered
    return render_template("signup.html")

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
    #print "session",session
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
    d={}
    try:
        connection.register([UserDetails])	
        collection = connection['test1'].userdetails
        user1 = collection.UserDetails()
        record=collection.find_one({'email':session['username']}) #some email value)
        print "session",session
    except:
        print "hee:",sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]
    if record :
        try:
            record['name'] = request.form['name']
            record['ssn'] = request.form['ssn']
            record['location'] = request.form['location']
            d.update({"name":record['name'],"email":str(session['username']),"ssn":record['ssn'],"location":record['location']})
        except:
            print "2:",sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]
    else:
        try:
            user1['name'] = ""
            user1['email'] = str(session['username'])
            user1['location'] = ""
            user1['ssn'] = ""
            user1.save()
            print "added! to UserDetails"
            d.update({"name":"","email":session['username'],"ssn":"","location":""})
        except:
            print "3:",sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]   
    context=d
    print context
    return render_template("display.html",**context)


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

@app.route("/imgRetrieve")
def renderImage():
    try:
        return send_file(imagepath)
    except:
        print "img",sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]   
        
@app.route("/videoRetrieve")
def renderVideo():
    try:
        return send_file(videopath)
    except:
        print "video",sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]      

@app.route("/encrypt") 
def encryptImage():
    try:
        image = open(imagepath,"rb")
        plaintext = image.read()
        print "encrypting.." 
        cipher = enc_input(plaintext)
        dec = dec_input(cipher)
        print dec
        f= open('dec', 'w')
        f.write(dec)
        f.close()    
    except: 
        print sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]            
    return "success"    

def enc_input(data):

    plaintext = data
    cbc_key = ecb_key
    iv = "A" * 16
    try:
        encryptor = AES.new(cbc_key, AES.MODE_CBC, iv)
        #print "yo, " + plaintext
        padded_plaintext = pkcs7_pad(plaintext)
        return encryptor.encrypt(padded_plaintext)
    except:
        print sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]


def dec_input(data):
    iv = "A" * 16
    cbc_key = ecb_key
    decryptor = AES.new(cbc_key, AES.MODE_CBC, iv)
    padded_plaintext = decryptor.decrypt(data)
    plaintext = pkcs7_unpad(padded_plaintext)
    return plaintext

def pkcs7_pad(text, block_size=16):
    """
    performs a pkcs#7 padding and returns the modified text with
    appropriate padding bytes added
    """
    size = len(text)
    padding_len = (block_size - (size % block_size))  
    return text + chr(padding_len) * padding_len


def pkcs7_unpad(text):
    """
        This function assumes that a PKCS#7 padding was already used on text
        and strips the padding bytes in order to return the original data
    """
    return text[0: -ord(text[-1])]


if __name__ == "__main__":
    app.run()
