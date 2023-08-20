from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk
from student import student


class Face_Recognition_System:
    def __init__(self, root= None):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # first image
        img1 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\Background.jfif")
        img1 = img1.resize((1920, 120), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1920, height=120)

        # backgroundimage
        img2 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\WhiteBackground.jpg")
        img2 = img2.resize((1920, 960), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=120, width=1920, height=960)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("Algerian", 35, "bold"),
                          bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        # studentbutton1

        img3 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\Student.jpg")
        img3 = img3.resize((250, 220), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        btn1 = Button(bg_img, image=self.photoimg3, command=self.student_details, cursor="hand2")
        btn1.place(x=225, y=150, width=250, height=220)

        btn1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("Algerian", 15, "bold"), bg="darkblue", fg="white")
        btn1_1.place(x=225, y=350, width=250, height=40)

        # detect face button

        img4 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\Facedetect.jpg")
        img4 = img4.resize((250, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        btn1 = Button(bg_img, image=self.photoimg4, cursor="hand2")
        btn1.place(x=625, y=150, width=250, height=220)

        btn1_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("Algerian", 15, "bold"), bg="darkblue",
                        fg="white")
        btn1_1.place(x=625, y=350, width=250, height=40)

        # attendance button
        img5 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\attendance.jpeg")
        img5 = img5.resize((250, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        btn1.place(x=1025, y=150, width=250, height=220)

        btn1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("Algerian", 15, "bold"), bg="darkblue",
                        fg="white")
        btn1_1.place(x=1025, y=350, width=250, height=40)

        # help
        img6 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\helpdesk.png")
        img6 = img6.resize((250, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        btn1.place(x=1425, y=150, width=250, height=220)

        btn1_1 = Button(bg_img, text="Help", cursor="hand2", font=("Algerian", 15, "bold"), bg="darkblue", fg="white")
        btn1_1.place(x=1425, y=350, width=250, height=40)

        # train face button
        img7 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\traindata.jpeg")
        img7 = img7.resize((250, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btn1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        btn1.place(x=225, y=500, width=250, height=220)

        btn1_1 = Button(bg_img, text="Train Faces", cursor="hand2", font=("Algerian", 15, "bold"), bg="darkblue",
                        fg="white")
        btn1_1.place(x=225, y=700, width=250, height=40)

        # photos
        img8 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\photos.jpg")
        img8 = img8.resize((250, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        btn1 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        btn1.place(x=625, y=500, width=250, height=220)

        btn1_1 = Button(bg_img, text="Photos", cursor="hand2", font=("Algerian", 15, "bold"), bg="darkblue", fg="white")
        btn1_1.place(x=625, y=700, width=250, height=40)

        # developer
        img9 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\developer.png")
        img9 = img9.resize((250, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        btn1 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        btn1.place(x=1025, y=500, width=250, height=220)

        btn1_1 = Button(bg_img, text="Developer", cursor="hand2", font=("Algerian", 15, "bold"), bg="darkblue",
                        fg="white")
        btn1_1.place(x=1025, y=700, width=250, height=40)

        # exit button
        img10 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\exit.jpeg")
        img10 = img10.resize((250, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        btn1 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        btn1.place(x=1425, y=500, width=250, height=220)

        btn1_1 = Button(bg_img, text="Exit", cursor="hand2", font=("Algerian", 15, "bold"), bg="darkblue", fg="white")
        btn1_1.place(x=1425, y=700, width=250, height=40)

        # =================================== Functions button =========================================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
