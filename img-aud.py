import mysql.connector
import sys
from gtts import gTTS
from PIL import Image
from pytesseract import image_to_string
#======================================

db= mysql.connector.connect(user="root",password="your_password",host="localhost",database="dsaa")

mycursor = db.cursor()

print """ 
	+=========================================+
	|    Please select  page no. of Book	  |
	+=========================================+
	  """
mycursor.execute("select id,address from test")

data = mycursor.fetchall()
a=[]
for i in data:
	a.append(i[1].encode('ascii','replace'))
	#print i

for i in range(len(a)):
	print i," - ",a[i]

mycursor.close()
#=====================================

while 1:
	
	page_no=int(input("Enter a page number which you want to read and listen:\n\n"))
	path="empty"
	for i in range(0,7):
		if page_no==i:
			path=a[i]
			print path
			break
	if path=="empty":
		print "Please choose a correct page no."
		continue
	else:
		break		
	"""	
	if page_no==0 :
		path=a[0]
		break
	elif page_no == 1:
		path=a[1] 
		break
	elif(page_no==2):
		path=a[2]
		break
	elif(page_no==3):
		path=a[3]
		break
	elif(page_no==4):
		path=a[4]
		break
	elif(page_no==5):
		path=a[5]
		break
	elif(page_no==5):
		path=a[5]
		break
	elif(page_no==7):
		path=a[7]
		break
	else:
		print "Please choose a correct page no."
		continue
	"""
print ("\t\t\t<<<========================Book Page=======================================>>>\n\n")

#============Image to text=============

img=Image.open(path)
text=image_to_string(img)
print text
txt=text.encode('ascii','replace')

fle = open("output-text/text"+str(page_no)+".txt",'w')
fle.write(txt)
fle.close() 
#img.show()

#==========Text to Speech===============

blabla = (text)
tts = gTTS(text=blabla, lang='en')
tts.save("/home/username/dsaa-project/audio/audio"+str(page_no)+".mp3")

#==========Playing sound==================
from playsound import playsound
playsound("/home/username/dsaa-project/audio/audio"+str(page_no)+"mp3")


db.close()
sys.exit()
