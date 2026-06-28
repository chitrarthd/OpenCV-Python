# you have to create a user driven file where you kae input of a image location than ask him he wants to drow a line rectangle circle or text
#take the required inputs also from the user like radius and centre of the circle etc
#then ask him to eirhter save it or see it saving name also

import cv2 as cv


location=input("Enter the path of image: ")


img = cv.imread(location)

if img is not None:
    print("image loaded sucessfully!!!")
    
     
    h,w,c=img.shape
    print(f"image loaded:\n Heights: {h}\n Width: {w}\n Channels: {c} " )
    
    
    

    option= int(input("1: to make a line\n2: to make rectange\n3: to make circle\n4: To write text on image\nwrite your choice: ",))






    if option==1:
        x1,y1=map(int,input("Enter point 1 (x1,y1): ").split())
        x2,y2=map(int,input("Enter point 2 (x2,y2): ").split())

        cv.line(img,(x1,y1),(x2,y2),(255,0,0),3)

    elif option==2:
        x3,y3=map(int,input("Enter point 1 (x1,y1): ").split())
        x4,y4=map(int,input("Enter point 2 (x2,y2): ").split())

        cv.rectangle(img,(x3,y3),(x4,y4),(255,0,0),3)
    
    elif option==3:
        rad=int(input("Enter the radius of circle: "))
        x5,y5=map(int,input("Enter centre of circle (x,y): ").split())
        cv.circle(img,(x5,y5),rad,(255,0,0),4)
    
    elif option==4:
        text=input("Enter the text: ")
        x6,y6=map(int,input("Enter bottem left corner point of text (x,y): ").split())

        cv.putText(img,text,(x6,y6),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),4)




    do=int(input("Enter 1 to see or 2 to save : "))
    if do == 1:
        cv.imshow("Edited Image", img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif do == 2:
        name = input("Enter filename (example: output.jpg): ")

        cv.imwrite(name, img)
        print("Image saved successfully!") 
    
else:
    print("image not leaoded!!!")



