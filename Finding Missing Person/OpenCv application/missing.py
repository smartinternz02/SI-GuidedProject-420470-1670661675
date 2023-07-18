import cv2
import numpy as np
from keras.preprocessing import image
import tensorflow as tf
from twilio.rest import Client

model=tf.keras.models.load_model("E:\Missing.h5")
video=cv2.VideoCapture(0)
name=["Findingg Missing",'Normal']

account_sid='AC39b7a8fa7a706c18844094a5f230084c'
auth_token='c8fc9274e557ea0be1626f72da172b8b'
client=Client(account_sid,auth_token)
message=client.messages.create(
    to="+919390038771",
    from_="+14175383510",
    body=" Found the Missing at 17.3984° N, 78.5583° E "
)

import cv2
import numpy as np
from keras.preprocessing import image
import tensorflow as tf
from twilio.rest import Client
model=tf.keras.models.load_model("E:\Missing.h5")
video=cv2.VideoCapture(0)
name=['Found Missing','Normal']

from tensorflow.keras.preprocessing import image

while(True):
  success,frame=video.read()
  cv2.imwrite("C:/Users/arake/Downloads/finding-missing-person-using-AI-main-20221204T164027Z-001/finding-missing-person-using-AI-main/Dataset/Dataset/testset/Found Missing/gettyimages-1124266363-612x612.jpg",frame)
  img=image.load_img("C:/Users/arake/Downloads/finding-missing-person-using-AI-main-20221204T164027Z-001/finding-missing-person-using-AI-main/Dataset/Dataset/testset/Found Missing/gettyimages-1124266363-612x612.jpg",target_size=(64,64))
  x=image.img_to_array(img)
  x=np.expand_dims(x,axis=0)
  pred=model.predict(x)
  p=int(pred[0][0])
  print(p)
  cv2.putText(frame,'Predicted Class = '+str(name[p]),(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
  
if pred[0][0]==0:
    account_sid="AC39b7a8fa7a706c18844094a5f230084c"
    auth_token="c8fc9274e557ea0be1626f72da172b8b"
    client=Client(account_sid,auth_token)
    message=client.messages.create(
          to="+919390038771",
          from_='+13868543289',
          body=" white drops "
          )
    print(message.sid)
    print("Found Missing")
    print("SMS Sent")
else:
    print("Normal")
cv2.imshow("frame",frame)
if cv2.waitKey(1) & 0xFF==ord('a'):
    #break
    video.release()
cv2.destroyAllWindows()
    
    
     