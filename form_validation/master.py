import requests
from flask import Flask, render_template, request, redirect, url_for
import os
from aadhar_front import aadhar_f
from aadhar_back import aadhar_b
from pan_final import pan_f
import cv2
import Levenshtein as lev
import re

app = Flask(__name__,static_url_path="",static_folder="static/")
app.config['DEBUG'] = True

info = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handleUploads',methods = ['GET','POST'])
def handleUpload():
    if request.method == 'POST':
        name = request.form.get('name')
        fname = request.form.get('fname')
        add = request.form.get('message')
        dob = request.form.get('dob')
        a_no = request.form.get('aadhar_number')
        pan_no = request.form.get('pan_number')
        info = {'name':name,'fname':fname,'address':add,'dob':dob,'aadhar_no':a_no,'pan_no':pan_no}
        print(info)
    if 'aadhar_f' in request.files:
        photo = request.files['aadhar_f']
        if photo.filename != '':            
            photo.save(os.path.join('./form_validation/data/aadhar_f/', photo.filename))
    if 'aadhar_b' in request.files:
        photo = request.files['aadhar_b']
        if photo.filename != '':            
            photo.save(os.path.join('./form_validation/data/aadhar_b/', photo.filename))
    if 'pan' in request.files:
        photo = request.files['pan']
        if photo.filename != '':            
            photo.save(os.path.join('./form_validation/data/pan/', photo.filename))
    return redirect(url_for('xyz'))

@app.route('/xyz',methods = ['POST','GET'])
def xyz():
    af = cv2.imread('./form_validation/data/aadhar_f/'+str(os.listdir('./form_validation/data/aadhar_f/')[0]))
    af_d = aadhar_f(af)
    ab = cv2.imread('./form_validation/data/aadhar_b/'+str(os.listdir('./form_validation/data/aadhar_b/')[0]))
    ab_d = aadhar_b(ab)
    pan_img = cv2.imread('./form_validation/data/pan/'+str(os.listdir('./form_validation/data/pan/')[0]))
    pan_info = pan_f(pan_img)

    nameform = info['name']
    namepan= pan_info['name']
    fnameform=info['fname']
    fnamepan=pan_info['f_name']
    dobaad=af_d['dob']
    dobpan=pan_info['dob']
    dobform=info['dob']
    pannum=pan_info['pan_no']
    pannumform=info['pan_no']
    aadnum=info['aadhar_no']
    addnumform=info['aadhar_no']
    addform=info['address']
    addaad=ab_d['address']
    Fratio=1
    Error=0
    #name
    Distance = lev.distance(nameform,namepan)
    ratio = lev.ratio(nameform,namepan)
    Error=Error+Distance
    Fratio=Fratio*ratio
    #fname
    Distance = lev.distance(fnameform,fnamepan)
    ratio = lev.ratio(fnameform,fnamepan)
    Error=Error+Distance
    Fratio=Fratio*ratio
    #dob
    Distance = lev.distance(dobpan,dobform)
    ratio = lev.ratio(dobpan,dobform)
    Error=Error+Distance
    Fratio=Fratio*ratio
    #pannumber
    Distance = lev.distance(pannum,pannumform)
    ratio = lev.ratio(pannum,pannumform)
    Error=Error+Distance
    Fratio=Fratio*ratio
    #aadhaar num
    Distance = lev.distance(aadnum,addnumform)
    ratio = lev.ratio(aadnum,addnumform)
    Error=Error+Distance
    Fratio=Fratio*ratio
    #address
    Distance = lev.distance(addform,addaad)
    ratio = lev.ratio(addform,addaad)
    Error=Error+Distance
    Fratio=Fratio*ratio
    # print(Error)
    # print(Fratio)
    if Fratio>80:
        return render_template('regg.html')
    elif Fratio<80:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()