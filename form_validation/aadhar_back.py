import cv2
import pytesseract
import os

def aadhar_back(img):
    '''
    file = os.listdir('./data/aadhar')
    for i in file:
        x=x.split('.')
        if x[0].endswith('back')
        filename = i
    '''
    img = cv2.imread('./data/aadhar/'+filename)
    #cv2.imshow('Original',img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = gray
    #cv2.imshow("grayscale",img)
    
    (h,w) = img.shape
    st = pytesseract.image_to_string(img[:,w//2:w])
    s = st.split('\n')
    fin = ' '.join(i for i in s)
    #st = pytesseract.image_to_string(img)
    return st
    '''
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''

img = cv2.imread('')
s = aadhar_back()
print(s)