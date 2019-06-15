import requests
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        uname = request.form.get('usrnm')
        #psw = request.form.get('psw')
        print(uname)
    if 'aadhar_f' in request.files:
        photo = request.files['aadhar_f']
        if photo.filename != '':            
            photo.save(os.path.join('./data/aadhar/', photo.filename))
    if 'aadhar_b' in request.files:
        photo = request.files['aadhar_b']
        if photo.filename != '':            
            photo.save(os.path.join('./data/aadhar/', photo.filename))
    if 'pan' in request.files:
        photo = request.files['pan']
        if photo.filename != '':            
            photo.save(os.path.join('./data/pan/', photo.filename))
    
    return render_template('loginform.html')

# @app.route('/handleUploads',methods = ['POST','GET'])
# def handleFileUpload():
#     if 'pi' in request.files:
#         photo = request.files['pi']
#         if photo.filename != '':            
#             photo.save(os.path.join('/home/saujanya/code_asylums', photo.filename))
#     return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()