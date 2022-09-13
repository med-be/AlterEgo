## import libraries
from tkinter import *
from gtts import gTTS
from playsound import playsound
from pytesseract import *
from PIL import Image
import argparse
pytesseract.tesseract_cmd = r'C:\Users\hs\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


################### taking inputs from cmd ####################

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
img  = Image.open(img_path)

################### convert img to text ##############################

Message = pytesseract.image_to_string(img)

################### Initialized window ####################

root = Tk()
root.geometry('600x400')
root.resizable(0,0)
root.title('AlterEgo')


##heading
Label(root, text = 'AlterEgo' , font='Roboto 25' ).pack()
Label(root, text ='Smart Assistant for Blind and Visually Impaired People', font ='Roboto 15 italic').pack()
Label(root, text ='AlterEgo@2021' , font ='Roboto 10').pack(side = BOTTOM)



#label
hello='HelloWorld'
Label(root, text =hello, font ='arial 15 bold').pack()
Label(root, text =" ", font ='arial 15 bold').pack()
Label(root, text = Message, font ='arial 10', bg ='white smoke').pack()

###################define function##############################

def Text_to_speech():
    speech = gTTS(text = Message)
    speech.save('d1.mp3')
    playsound('d1.mp3')

def Exit():
    root.destroy()

#Button
Button(root, text = "PLAY" , font = 'Roboto 15', command = Text_to_speech, width =4).place(x=230, y=300)
Button(root,text = 'EXIT',font = 'Roboto 15' , command = Exit, bg = 'OrangeRed1').place(x=315,y=300)

#infinite loop to run program
root.mainloop()
