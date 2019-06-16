import cv2
import pytesseract
import re
import string
def pan_f(img):
    #img = cv2.imread('./data/pan.jpeg')
    #cv2.imshow('Original',img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = gray
    #cv2.imshow("grayscale",img)
    st={' '}
    (h,w) = img.shape
    #st = pytesseract.image_to_string(img[:,w//2:w])
    st = pytesseract.image_to_string(img)
    dob=re.findall(r'(((?:0[0-9])|(?:[1-2][0-9])|(?:3[0-1]))\/((?:0[1-9])|(?:1[0-2]))\/(\d{4}))',st)
    pan=re.findall(r'[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}',st)
    #s=s.replace(' ', '')
    punct=set(string.punctuation)
    snpunc=''.join(x for x in st if x not in punct)
    namepos=re.split("Name",snpunc)
    Name=namepos[1]
    FName=namepos[2]
    return {'name':Name,'f_name':FName,'dob':dob,'pan_no':pan}
    
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# img = cv2.imread('WhatsApp Image 2019-06-15 at 6.40.48 PM.jpeg')
# s = pan_final(img)
#trys="02/16/9999"
#st=s.split()
#str="The rain in Spain"
#new (((?:0[0-9])|(?:[1-2][0-9])|(?:3[0-1]))\/((?:0[1-9])|(?:1[0-2]))\/(\d{4}))
#(((?:0[0-9])|(?:[1-2][0-9])|(?:3[0-1]))\/((?:0[1-9])|(?:1[0-2]))\/(\d{4})
# dob=re.findall(r'(((?:0[0-9])|(?:[1-2][0-9])|(?:3[0-1]))\/((?:0[1-9])|(?:1[0-2]))\/(\d{4}))',s)
# pan=re.findall(r'[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}',s)
# #s=s.replace(' ', '')
# punct=set(string.punctuation)
# snpunc=''.join(x for x in s if x not in punct)
# namepos=re.split("Name",snpunc)
# Name=namepos[1]
# FName=namepos[2]
#x=re.findall("Name", snpunc)
#namepos=re.split("Name",snpunc)
#pancnpos=re.split("Number",s)
#print(s)