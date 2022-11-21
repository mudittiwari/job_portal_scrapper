import cv2
# img=cv2.imread('186.jpg')
import numpy as np
# cv2.imshow('image',img)
# cv2.waitKey(0)

# cap=cv2.VideoCapture("test.mp4")
# cap=cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)#brightness
# while True:
#     success,image=cap.read()
#     cv2.imshow('video',image)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break


# kernel=np.ones((5,5),np.uint8)
# imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgblur=cv2.GaussianBlur(imggray,(7,7),0)
# imgcanny=cv2.Canny(img,100,100)
# imgdialation=cv2.dilate(imgcanny,kernel,iterations=1)
# imgeroded=cv2.erode(imgdialation,kernel,iterations=1)
# cv2.imshow('gray',imggray)
# cv2.imshow('blur',imgblur)
# cv2.imshow('canny',imgcanny)
# cv2.imshow('dialation',imgdialation)
# cv2.imshow('eroded',imgeroded)
# cv2.waitKey(0)



# print(img.shape)
# imgResize=cv2.resize(img,(300,200))
# imgCropped=img[0:200,200:500]
# cv2.imshow('image',imgResize)
# cv2.imshow('cropped',imgCropped)
# cv2.waitKey(0)




# img=np.zeros((512,512,3),np.uint8)
# line=cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# rectangle=cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
# circle=cv2.circle(img,(400,50),30,(255,255,0),5)
# text=cv2.putText(img,'OPENCV',(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
# # img[100:300,100:300]=255,0,0
# cv2.imshow('image',img)
# cv2.waitKey(0)




# width,height=250,350
# pts1=np.float32([[111,219],[287,188],[154,482],[352,440]])
# pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix=cv2.getPerspectiveTransform(pts1,pts2)
# imgOutput=cv2.warpPerspective(img,matrix,(width,height))
# cv2.imshow('output',imgOutput)

# horizontal_stack=np.hstack((img,img))
# vertical_stack=np.vstack((img,img))
# cv2.imshow('horizontal',vertical_stack)
# cv2.imshow('stack',horizontal_stack)
# cv2.waitKey(0)

#
# def stackImages(scale,imgArray):
#     rows=len(imgArray)
#     cols=len(imgArray[0])
#     rowsAvailable=isinstance(imgArray[0],list)
#     width=imgArray[0][0].shape[1]
#     height=imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range(0,rows):
#             for y in range(0,cols):
#                 if imgArray[x][y].shape[:2]==imgArray[0][0].shape[:2]:
#                     imgArray[x][y]=cv2.resize(imgArray[x][y],(0,0),None,scale,scale)
#                 else:
#                     imgArray[x][y]=cv2.resize(imgArray[x][y],(imgArray[0][0].shape[1],imgArray[0][0].shape[0]),None,scale,scale)
#                 if len(imgArray[x][y].shape)==2:imgArray[x][y]=cv2.cvtColor(imgArray[x][y],cv2.COLOR_GRAY2BGR)
#         imageBlank=np.zeros((height,width,3),np.uint8)
#         hor=[imageBlank]*rows
#         hor_con=[imageBlank]*rows
#         for x in range(0,rows):
#             hor[x]=np.hstack(imgArray[x])
#         ver=np.vstack(hor)
#     else:
#         for x in range(0,rows):
#             if imgArray[x].shape[:2]==imgArray[0].shape[:2]:
#                 imgArray[x]=cv2.resize(imgArray[x],(0,0),None,scale,scale)
#             else:
#                 imgArray[x]=cv2.resize(imgArray[x],(imgArray[0].shape[1],imgArray[0].shape[0]),None,scale,scale)
#             if len(imgArray[x].shape)==2:imgArray[x]=cv2.cvtColor(imgArray[x],cv2.COLOR_GRAY2BGR)
#         hor=np.hstack(imgArray)
#         ver=hor
#     return ver
#
# imgStack=stackImages(0.5,([img,img,img],[img,img,img]))


# cv2.namedWindow('trackbars')
# cv2.resizeWindow('trackbars',640,240)
# cv2.createTrackbar('hue min','trackbars',0,179,lambda x:x)
# cv2.createTrackbar('hue max','trackbars',19,179,lambda x:x)
# cv2.createTrackbar('sat min','trackbars',110,255,lambda x:x)
# cv2.createTrackbar('sat max','trackbars',240,255,lambda x:x)
# cv2.createTrackbar('val min','trackbars',153,255,lambda x:x)
# cv2.createTrackbar('val max','trackbars',255,255,lambda x:x)
#
# while True:
#     imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     h_min=cv2.getTrackbarPos('hue min','trackbars')
#     h_max=cv2.getTrackbarPos('hue max','trackbars')
#     s_min=cv2.getTrackbarPos('sat min','trackbars')
#     s_max=cv2.getTrackbarPos('sat max','trackbars')
#     v_min=cv2.getTrackbarPos('val min','trackbars')
#     v_max=cv2.getTrackbarPos('val max','trackbars')
#     # print(h_min,h_max,s_min,s_max,v_min,v_max)
#     mask=cv2.inRange(imghsv,(h_min,s_min,v_min),(h_max,s_max,v_max))
#     imgresult=cv2.bitwise_and(img,img,mask=mask)
#     cv2.imshow('original',img)
#     cv2.imshow('hsv',imghsv)
#     cv2.imshow('mask',mask)
#     cv2.imshow('result',imgresult)
#     cv2.waitKey(1)



# img=cv2.imread('shapes-basic-color.jpg')
# imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
# imgCanny=cv2.Canny(imgBlur,100,100)
# imgContour=img.copy()
# cv2.imshow('original',img)
# cv2.imshow('edges',imgCanny)
#
#
#
# def getContours(image):
#     contours,hierarchy=cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area=cv2.contourArea(cnt)
#         # print(area)
#         # cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 1)
#         if area>50:
#             cv2.drawContours(imgContour,cnt,-1,(255,255,255),3)
#             peri=cv2.arcLength(cnt,True)
#             approx=cv2.approxPolyDP(cnt,0.02*peri,True)
#             print(len(approx))
#             objCor=len(approx)
#             x,y,w,h=cv2.boundingRect(approx)
#             if objCor==3:objectType='triangle'
#             elif objCor==4:
#                 aspRatio=w/float(h)
#                 if aspRatio>0.95 and aspRatio<1.05:objectType='square'
#                 else:objectType='rectangle'
#             elif objCor>4:objectType='circle'
#             else:objectType='None'
#             cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
#             cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)
# getContours(imgCanny)
# cv2.imshow('contour',imgContour)
# cv2.waitKey(0)


# img=cv2.imread('Lenna.png')
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces=face_cascade.detectMultiScale(imgGray,1.3,5)
# faces=face_cascade.detectMultiScale(imgGray)
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)



