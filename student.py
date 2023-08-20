from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector




class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        ##### Variables  #####
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_searchtxt = StringVar()
        self.var_search = StringVar()



        # first image
        img1 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\student.jpeg")
        img1 = img1.resize((450, 120), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=550, height=120)

        # second image
        img2 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\thaparuniversity.jpg")
        img2 = img2.resize((450, 120), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=450, y=0, width=550, height=120)

        # third image

        img3 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\thapar.jpeg")
        img3 = img3.resize((450, 120), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=900, y=0, width=550, height=120)

        # fourth image

        img4 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\lib.jpeg")
        img4 = img4.resize((450, 120), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        f_lbl = Label(self.root, image=self.photoimg4)
        f_lbl.place(x=1350, y=0, width=550, height=120)

        # Background image
        # img3=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\face.jpg")
        # img3 = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Images\re1.jpg")
        img5 = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\WhiteBackground.jpg")
        img5 = img5.resize((1920, 1080),
                           Image.ANTIALIAS)  # Antialias lea high level image lai low level mah convert garxa
        self.photoimg5 = ImageTk.PhotoImage(img5)

        bg_img = Label(self.root, image=self.photoimg5)
        bg_img.place(x=0, y=130, width=1920, height=1080)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("Algerian", 30, "bold"), bg="white",
                          fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1920, height=30)

        main_frame = Frame(bg_img, bd=2, bg="white", )
        main_frame.place(x=20, y=35, width=1920, height=900)

        # left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("Algerian", 12, "bold"))
        left_frame.place(x=10, y=5, width=900, height=750)

        img_left = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\thapar.jpeg")
        img_left = img_left.resize((450, 120), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=10, y=0, width=876, height=150)

        # current course
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current course information",
                                          font=("Algerian", 12, "bold"))
        current_course_frame.place(x=10, y=155, width=876, height=180)

        # department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=50, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep ,font=("times new roman", 13, "bold"),state="readonly", width=18)
        dep_combo["values"] = ("Select Department", "IT", "Computer", "Civil", "Elx & Comm", "Software")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=15, pady=25, sticky=W)

        # course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=50, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 13, "bold"), state="readonly", width=18)
        course_combo["values"] = ("Select Course", "AI", "IPPR", "CN", "OOSE", "TOC", "CG", "SNM")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=15, pady=25, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=50, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman", 13, "bold"), state="readonly", width=18)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=15, pady=25, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=50, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 13, "bold"), state="readonly", width=18)
        semester_combo["values"] = ("Select Semester", "Semester-I", "Semester-III", "Semester-V", "Semester-VII")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=15, pady=25, sticky=W)

        # class student information
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                         font=("Algerian", 12, "bold"))
        class_student_frame.place(x=10, y=345, width=876, height=375)

        # student ID
        studentId_label = Label(class_student_frame, text="StudentID:", font=("times new roman", 13, "bold"),
                                bg="white")
        studentId_label.grid(row=0, column=0, padx=50, sticky=W)

        studentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=18,font=("times new roman", 13, "bold"))
        studentId_entry.grid(row=0, column=1, padx=15, pady=10, sticky=W)

        # student name
        studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 13, "bold"),
                                  bg="white")
        studentName_label.grid(row=0, column=2, padx=50, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=18,font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=15, pady=10, sticky=W)

        # class division
        class_div_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 13, "bold"),
                                bg="white")
        class_div_label.grid(row=1, column=0, padx=50, sticky=W)

        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,  font=("times new roman", 13, "bold"),state="readonly", width=16)
        div_combo["values"] = ("Select Division", "A", "B")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=15, pady=10, sticky=W)

        # roll_no
        roll_no_label = Label(class_student_frame, text="Roll No:", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=50, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll, width=18,font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=15, pady=10, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=50, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman", 13, "bold"), state="readonly", width=16)
        gender_combo["values"] = ("Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=15, pady=10, sticky=W)

        # DOB
        dob_label = Label(class_student_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=50, sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob, width=18,font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=15, pady=10, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=50, sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email , width=18,font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=15, pady=10, sticky=W)

        # Phone no
        phone_label = Label(class_student_frame, text="Phone No:", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=50, sticky=W)

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,  width=18,font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=15, pady=10, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=50, sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,  width=18,font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=15, pady=10, sticky=W)

        # Teacher Name
        teacher_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"),
                              bg="white")
        teacher_label.grid(row=4, column=2, padx=50, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,  width=18,font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=15, pady=10, sticky=W)

        # radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, text="Take Photo Sample",
                                    value="Yes")
        radiobtn1.grid(row=5, column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame, text="No Photo Sample", value="NO")
        radiobtn2.grid(row=5, column=1)

        # radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5, column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="NO")
        radiobtn2.grid(row=5, column=1)

        # button frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=50, y=273, width=770, height=35)

        save_btn = Button(btn_frame,command=self.add_data, text="Save", width=18, font=("times new roman", 13, "bold"), bg="Green",
                          fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", width=19, font=("times new roman", 13, "bold"), bg="Green",
                            fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", width=18, font=("times new roman", 13, "bold"), bg="Green",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=18, font=("times new roman", 13, "bold"), bg="Green",
                           fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=50, y=308, width=770, height=35)

        take_photo_btn = Button(btn_frame1, text="Take photo sample", width=38, font=("times new roman", 13, "bold"),
                                bg="Green", fg="white")
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame1, text="Take photo sample", width=38, font=("times new roman", 13, "bold"),
                                  bg="Green", fg="white")
        update_photo_btn.grid(row=1, column=1)

        # RIGHT label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student_details",
                                 font=("Algerian", 12, "bold"))
        right_frame.place(x=930, y=5, width=900, height=750)

        img_right = Image.open(r"C:\Users\arshk\OneDrive\Desktop\projectimages\student.jpeg")
        img_right = img_right.resize((450, 120), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=10, y=0, width=876, height=150)

        ########################search system#####################################

        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                  font=("Algerian", 12, "bold"))
        search_frame.place(x=10, y=155, width=876, height=100)

        search_label = Label(search_frame, text="Search by:", font=("times new roman", 15, "bold"), bg="maroon",
                             fg="white")
        search_label.grid(row=0, column=0, padx=40, pady=22, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select ", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=25, sticky=W)

        search_entry = ttk.Entry(search_frame, width=18, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        search_btn = Button(search_frame, text="Search", width=14, font=("times new roman", 13, "bold"), bg="Green",
                            fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_frame, text="Show All", width=14, font=("times new roman", 13, "bold"), bg="Green",
                             fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        # table frame

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=263, width=876, height=400)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=(
            "dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address",
            "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

        ####function decleration ######
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields Are Required", parent=self.root)

        else:
            try:
                # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
                conn = mysql.connector.connect(host="localhost", username="root")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                speak_va('Student Details has been added successfully.')
                messagebox.showinfo("Success", "Student details has been added Sucessfully", parent=self.root)
            except Exception as es:
                speak_va('An Exception Occurred!')
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

                ######======Fetch data ==============#####
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root@khom123",database="khomdb")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student1")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
                conn.commit()
            conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
