# Importing Libraries
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter


class HarryCodeCorner:

    def __init__(self, root):
        self.root = root
        self.root.title("Technology Corner")
        self.root.geometry("1350x720+0+0")


# VARIABLEs FOR DATABASE:
        self.category_var = StringVar()
        self.experience_var = StringVar()
        self.subscription_var = StringVar()
        self.full_name_var = StringVar()
        self.mail_id_var = StringVar()
        self.state_var = StringVar()
        self.qualification_var = StringVar()
        self.passout_year_var = StringVar()
        self.video_type_var = StringVar()
        self.name_var = StringVar()
        self.duration_var = StringVar()
        self.technology_var = StringVar()
        self.start_date_var = StringVar()
        self.end_date_var = StringVar()
        self.rate_var = StringVar()

        lbltitle = Label(self.root, text="Harry's Tech Corner", bg="purple", fg="white",
                         bd=5, relief=SUNKEN, font=("times new roman", 30, "bold"), padx=2, pady=5)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=5, relief=RIDGE, padx=10, bg="gray")
        frame.place(x=0, y=70, width=1345, height=400)

# Created the Left DataFrame
        DataFrameLeft = LabelFrame(frame, text="Techie Details", bg="brown",
                                   fg="white", bd=5, relief=RIDGE, font=("times new roman", 20, "bold"))
        DataFrameLeft.place(x=1, y=5, width=770, height=370)

        lblcategory = Label(DataFrameLeft, text="Category:", bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=2, pady=6)
        lblcategory.grid(row=0, column=0, sticky=W)
        comcategory = ttk.Combobox(DataFrameLeft, font=(
            "times new roman", 11, "bold"), width=22, state="readonly", textvariable=self.category_var)
        comcategory["value"] = ("Working Professional", "Student", "Others")
        comcategory.current(0)
        comcategory.grid(row=0, column=1)

        lblexp = Label(DataFrameLeft, text="Experience:", bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=2, pady=6)
        lblexp.grid(row=1, column=0, sticky=W)
        comexp = ttk.Combobox(DataFrameLeft, font=("times new roman", 11, "bold"),
                              width=22, state="readonly", textvariable=self.experience_var)
        comexp["value"] = ("Fresher", "1-2years",
                           "2-3 years", "3years & above")
        comexp.current(0)
        comexp.grid(row=1, column=1)

        lblsub = Label(DataFrameLeft, text="Subscription:", bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=2, pady=6)
        lblsub.grid(row=2, column=0, sticky=W)
        comsub = ttk.Combobox(DataFrameLeft, font=("times new roman", 11, "bold"),
                              width=22, state="readonly", textvariable=self.subscription_var)
        comsub["value"] = ("Yes", "No")
        comsub.current(0)
        comsub.grid(row=2, column=1)

        lblfname = Label(DataFrameLeft, text="Full_Name:", bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=2, pady=6)
        lblfname.grid(row=3, column=0, sticky=W)
        txtfname = Entry(DataFrameLeft, font=(
            "times new roman", 11, "italic"), width=25, textvariable=self.full_name_var)
        txtfname.grid(row=3, column=1)

        lblmail = Label(DataFrameLeft, text="Mail_Id:",  bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=2, pady=6)
        lblmail.grid(row=4, column=0, sticky=W)
        txtmail = Entry(DataFrameLeft, font=("times new roman",
                        11, "italic"), width=25, textvariable=self.mail_id_var,)
        txtmail.grid(row=4, column=1)

        lblstate = Label(DataFrameLeft, text="State:",  bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=2, pady=6)
        lblstate.grid(row=5, column=0, sticky=W)
        txtstate = Entry(DataFrameLeft, font=(
            "times new roman", 11, "italic"), width=25, textvariable=self.state_var)
        txtstate.grid(row=5, column=1)

        lbldegree = Label(DataFrameLeft, text="Qualification:", bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=2, pady=6)
        lbldegree.grid(row=6, column=0, sticky=W)
        comdegree = ttk.Combobox(DataFrameLeft, font=(
            "times new roman", 11, "bold"), width=22, state="readonly", textvariable=self.qualification_var)
        comdegree["value"] = ("UnderGraduate", "Graduate", "Masters", "Others")
        comdegree.current(0)
        comdegree.grid(row=6, column=1)

        lblyear = Label(DataFrameLeft, text="Passout_Year:", bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=2, pady=6)
        lblyear.grid(row=7, column=0, sticky=W)
        txtyear = Entry(DataFrameLeft, font=(
            "times new roman", 11, "italic"), width=25, textvariable=self.passout_year_var)
        txtyear.grid(row=7, column=1)

        lbltype = Label(DataFrameLeft, text="Video_Type:", bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=25, pady=6)
        lbltype.grid(row=0, column=2, sticky=W)
        comtype = ttk.Combobox(DataFrameLeft, font=(
            "times new roman", 11, "bold"), width=25, state="readonly", textvariable=self.video_type_var)
        comtype["value"] = ("Playlist", "One Shot", "Others")
        comtype.current(0)
        comtype.grid(row=0, column=3)

        lblvname = Label(DataFrameLeft, text="Name:", bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=25, pady=6)
        lblvname.grid(row=1, column=2, sticky=W)
        txtvname = Entry(DataFrameLeft, font=(
            "times new roman", 11, "italic"), width=28, textvariable=self.name_var)
        txtvname.grid(row=1, column=3)

        lbldur = Label(DataFrameLeft, text="Duration:", bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=25, pady=6)
        lbldur.grid(row=2, column=2, sticky=W)
        comdur = ttk.Combobox(DataFrameLeft, font=(
            "times new roman", 11, "italic"), width=25, textvariable=self.duration_var)
        comdur["value"] = ("Hrs", ": : :")
        comdur.current(0)
        comdur.grid(row=2, column=3)

        lbltech = Label(DataFrameLeft, text="Technology:",  bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=25, pady=6)
        lbltech.grid(row=3, column=2, sticky=W)
        txttech = Entry(DataFrameLeft, font=(
            "times new roman", 11, "italic"), width=28, textvariable=self.technology_var)
        txttech.grid(row=3, column=3)

        lblsdate = Label(DataFrameLeft, text="Start_Date:",  bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=25, pady=6)
        lblsdate.grid(row=4, column=2, sticky=W)
        comsdate = ttk.Combobox(DataFrameLeft, font=(
            "times new roman", 11, "bold"), width=25, textvariable=self.start_date_var)
        comsdate["value"] = ("../../....")
        comsdate.current(0)
        comsdate.grid(row=4, column=3)

        lbledate = Label(DataFrameLeft, text="End_Date:",  bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=25, pady=6)
        lbledate.grid(row=5, column=2, sticky=W)
        comedate = ttk.Combobox(DataFrameLeft, font=(
            "times new roman", 11, "bold"), width=25, textvariable=self.end_date_var)
        comedate["value"] = ("../../....")
        comedate.current(0)
        comedate.grid(row=5, column=3)

        lblrate = Label(DataFrameLeft, text="Rate:",  bg="brown", fg="white", font=(
            "times new roman", 15, "underline"), padx=25, pady=6)
        lblrate.grid(row=6, column=2, sticky=W)
        comrate = ttk.Combobox(DataFrameLeft, font=(
            "times new roman", 11, "bold"), width=25, textvariable=self.rate_var)
        comrate["value"] = ("5", "4", "3", "2 & Below")
        comrate.current(0)
        comrate.grid(row=6, column=3)


# Created the Right DataFrame
        DataFrameRight = LabelFrame(frame, text="Details Window", bg="brown",
                                    fg="white", bd=5, relief=SUNKEN, font=("times new roman", 20, "bold"))
        DataFrameRight.place(x=800, y=5, width=515, height=370,)
# Created txtBox, an attribute of the class using self
        self.txtBox = Text(DataFrameRight, font=(
            "Comic Sans MS", 11, "normal"), width=25, height=27, padx=10, pady=5)
        self.txtBox.grid(row=0, column=2)

        listscrollbar = Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0, column=1, sticky="ns")

        listbook = [
            "Python Tutorial for Beginners",
            "JavaScript Full Course",
            "How to Build Your First Web App with Flask",
            "HTML and CSS for Beginners",
            "ReactJS Crash Course",
            "Django Full Stack Web Development Tutorial",
            "Learn Git and GitHub",
            "How to Create a Portfolio Website Using HTML and CSS",
            "Introduction to Machine Learning with Python",
            "Understanding APIs",
            "How to Build a Chatbot with Python",
            "Top 10 Python Libraries You Should Know",
            "SQL Tutorial",
            "How to Get Started with Android Development",
            "Introduction to Data Structures and Algorithms in Python",
            "Building a To-Do List App with React",
            "How to Deploy a Django App to Heroku",
            "Introduction to Web Scraping with Python",
            "How to Build a Blog Using Django and Python",
            "Object-Oriented Programming in Python",
            "Java Programming Tutorial for Beginners",
            "C++ Full Course",
            "Building RESTful APIs with Flask",
            "Pygame Tutorial",
            "How to Use Docker for Python Projects",
            "Learn Firebase - Build Real-Time Apps with Firebase and React"
        ]

        def selectCourse(event=""):

            # For current selection
            selection = lstbox.curselection()

# Checked for selected item
            if not selection:
                print("No item selected")
                return  # Exit the function if no item is selected

# Extracted the first index from the selection
            index = selection[0]

# Checked for the selected value
            x = lstbox.get(index)

            if (x == "Python Tutorial for Beginners"):
                self.name_var.set("Python Tutorial for Beginners")
                self.duration_var.set("30 Hours")
                self.technology_var.set("Python")
                self.rate_var.set("5")

            elif x == "JavaScript Full Course":
                self.name_var.set("JavaScript Full Course")
                self.duration_var.set("40 Hours")
                self.technology_var.set("JavaScript")
                self.rate_var.set("4")

            elif x == "How to Build Your First Web App with Flask":
                self.name_var.set("How to Build Your First Web App with Flask")
                self.duration_var.set("20 Hours")
                self.technology_var.set("Python, Flask")
                self.rate_var.set("4.5")

            elif x == "HTML and CSS for Beginners":
                self.name_var.set("HTML and CSS for Beginners")
                self.duration_var.set("15 Hours")
                self.technology_var.set("HTML, CSS")
                self.rate_var.set("3.5")

            elif x == "ReactJS Crash Course":
                self.name_var.set("ReactJS Crash Course")
                self.duration_var.set("25 Hours")
                self.technology_var.set("JavaScript, ReactJS")
                self.rate_var.set("4.5")

            elif x == "Django Full Stack Web Development Tutorial":
                self.name_var.set("Django Full Stack Web Development Tutorial")
                self.duration_var.set("50 Hours")
                self.technology_var.set("Python, Django")
                self.rate_var.set("5")

            elif x == "Learn Git and GitHub":
                self.name_var.set("Learn Git and GitHub")
                self.duration_var.set("10 Hours")
                self.technology_var.set("Git, GitHub")
                self.rate_var.set("4")

            elif x == "How to Create a Portfolio Website Using HTML and CSS":
                self.name_var.set(
                    "How to Create a Portfolio Website Using HTML and CSS")
                self.duration_var.set("12 Hours")
                self.technology_var.set("HTML, CSS")
                self.rate_var.set("3.5")

            elif x == "Introduction to Machine Learning with Python":
                self.name_var.set(
                    "Introduction to Machine Learning with Python")
                self.duration_var.set("35 Hours")
                self.technology_var.set("Python, Machine Learning")
                self.rate_var.set("5")

            elif x == "Understanding APIs":
                self.name_var.set("Understanding APIs")
                self.duration_var.set("8 Hours")
                self.technology_var.set("REST, APIs")
                self.rate_var.set("3.5")

            elif x == "How to Build a Chatbot with Python":
                self.name_var.set("How to Build a Chatbot with Python")
                self.duration_var.set("18 Hours")
                self.technology_var.set("Python, NLP")
                self.rate_var.set("4.5")

            elif x == "Top 10 Python Libraries You Should Know":
                self.name_var.set("Top 10 Python Libraries You Should Know")
                self.duration_var.set("10 Hours")
                self.technology_var.set("Python")
                self.rate_var.set("4")

            elif x == "SQL Tutorial":
                self.name_var.set("SQL Tutorial")
                self.duration_var.set("20 Hours")
                self.technology_var.set("SQL")
                self.rate_var.set("4.5")

            elif x == "How to Get Started with Android Development":
                self.name_var.set(
                    "How to Get Started with Android Development")
                self.duration_var.set("30 Hours")
                self.technology_var.set("Java, Android")
                self.rate_var.set("4.5")

            elif x == "Introduction to Data Structures and Algorithms in Python":
                self.name_var.set(
                    "Introduction to Data Structures and Algorithms in Python")
                self.duration_var.set("40 Hours")
                self.technology_var.set("Python, Data Structures")
                self.rate_var.set("5")

            elif x == "Building a To-Do List App with React":
                self.name_var.set("Building a To-Do List App with React")
                self.duration_var.set("15 Hours")
                self.technology_var.set("JavaScript, React")
                self.rate_var.set("4")

            elif x == "How to Deploy a Django App to Heroku":
                self.name_var.set("How to Deploy a Django App to Heroku")
                self.duration_var.set("12 Hours")
                self.technology_var.set("Python, Django, Heroku")
                self.rate_var.set("4.5")

            elif x == "Introduction to Web Scraping with Python":
                self.name_var.set("Introduction to Web Scraping with Python")
                self.duration_var.set("20 Hours")
                self.technology_var.set("Python, Web Scraping")
                self.rate_var.set("4")

            elif x == "How to Build a Blog Using Django and Python":
                self.name_var.set(
                    "How to Build a Blog Using Django and Python")
                self.duration_var.set("25 Hours")
                self.technology_var.set("Python, Django")
                self.rate_var.set("5")

            elif x == "Object-Oriented Programming in Python":
                self.name_var.set("Object-Oriented Programming in Python")
                self.duration_var.set("30 Hours")
                self.technology_var.set("Python, OOP")
                self.rate_var.set("5")

            elif x == "Java Programming Tutorial for Beginners":
                self.name_var.set("Java Programming Tutorial for Beginners")
                self.duration_var.set("35 Hours")
                self.technology_var.set("Java")
                self.rate_var.set("4")

            elif x == "C++ Full Course":
                self.name_var.set("C++ Full Course")
                self.duration_var.set("45 Hours")
                self.technology_var.set("C++")
                self.rate_var.set("4.5")

        lstbox = Listbox(DataFrameRight, font=(
            "Comic Sans MS", 12, "normal"), width=25, height=23)
        lstbox.bind("<<ListboxSelect>>", selectCourse)
        lstbox.grid(row=0, column=0, padx=5, pady=5)
        listscrollbar.config(command=lstbox.yview)

        for item in listbook:
            lstbox.insert(END, item)


# Buttons to update the textbox content
        buttonframe = Frame(self.root, bd=5, relief=RIDGE,
                            padx=20, bg="lightgreen")
        buttonframe.place(x=0, y=475, width=1345, height=70)

        btninsert = Button(buttonframe, text="Insert", command=self.addData, font=(
            "times new roman", 15, "bold"), width=20, bg="purple", fg="white", padx=33, bd=5, pady=8)
        btninsert.grid(row=0, column=0)

        btnreset = Button(buttonframe, text="Read", command=self.showData, font=(
            "times new roman", 15, "bold"), width=20, bg="purple", fg="white", padx=33, bd=5, pady=8)
        btnreset.grid(row=0, column=2)

        btndelete = Button(buttonframe, text="Reset", command=self.reset, font=(
            "times new roman", 15, "bold"), width=20, bg="purple", fg="white", padx=33, bd=5, pady=8)
        btndelete.grid(row=0, column=3)

        btnexit = Button(buttonframe, text="Exit", command=self.iexit, font=(
            "times new roman", 15, "bold"), width=20, bg="purple", fg="white", padx=33, bd=5, pady=8)
        btnexit.grid(row=0, column=4)


# INFORMATION Frame
        infoframe = Frame(self.root, bd=5, relief=RIDGE,
                          padx=5, bg="lightgreen")
        infoframe.place(x=0, y=549, width=1345, height=143)

        Tableframe = Frame(infoframe, bd=4, relief=RIDGE, bg="powder blue")
        Tableframe.place(x=15, y=2, width=1275, height=130)

# # I will get the joining letter from Ericsson India Global Service within November. God will help me.

        xscroll = ttk.Scrollbar(Tableframe, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Tableframe, orient=VERTICAL)
# Created a Treeview widget to display the data from MySQL

        self.libraryTable = ttk.Treeview(Tableframe, columns=("Category:", "Experience:", "Subscription:", "Full_Name:", "Mail_Id:", "State:", "Qualification:", "Passout_Year:",
                                         "Video_Type:", "Name:", "Duration:", "Technology:", "Start_Date:", "End_Date:", "Rate:"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
# ScrollBar added to the Treeview
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.libraryTable.xview)
        yscroll.config(command=self.libraryTable.yview)
# The column headings defined

        self.libraryTable.heading("Category:", text="Category")
        self.libraryTable["show"] = "headings"
        self.libraryTable.pack(fill=BOTH, expand=1)

        self.libraryTable.heading("Experience:", text="Experience")
        self.libraryTable.heading("Subscription:", text="Subscription")
        self.libraryTable.heading("Full_Name:", text="Full Name")
        self.libraryTable.heading("Mail_Id:", text="Mail Id")
        self.libraryTable.heading("State:", text="State")
        self.libraryTable.heading("Qualification:", text="Qualification")
        self.libraryTable.heading("Passout_Year:", text="Passout Year")
        self.libraryTable.heading("Video_Type:", text="Video Type")
        self.libraryTable.heading("Name:", text="Name")
        self.libraryTable.heading("Duration:", text="Duration")
        self.libraryTable.heading("Technology:", text="Technology")
        self.libraryTable.heading("Start_Date:", text="Start Date")
        self.libraryTable.heading("End_Date:", text="End Date")
        self.libraryTable.heading("Rate:", text="Rate")
        self.libraryTable["show"] = "headings"
        self.libraryTable.pack(fill=BOTH, expand=1)

# THE WIDTH OF COLUMNS IN TABLE checked
        self.libraryTable.column("Category:", width=100)
        self.libraryTable.column("Experience:", width=100)
        self.libraryTable.column("Subscription:", width=100)
        self.libraryTable.column("Full_Name:", width=100)
        self.libraryTable.column("Mail_Id:", width=100)
        self.libraryTable.column("State:", width=100)
        self.libraryTable.column("Qualification:", width=100)
        self.libraryTable.column("Passout_Year:", width=100)
        self.libraryTable.column("Video_Type:", width=100)
        self.libraryTable.column("Name:", width=100)
        self.libraryTable.column("Duration:", width=100)
        self.libraryTable.column("Technology:", width=100)
        self.libraryTable.column("Start_Date:", width=100)
        self.libraryTable.column("End_Date:", width=100)
        self.libraryTable.column("Rate:", width=100)
        # self.libraryTable.column(":", width= 100)

        self.connect_to_database()
# Fetched the data from MySQL database
        self.fetch_data_from_mysql()
        self.libraryTable.bind("<ButtonRelease-1>",
                               self.get_cursor)  # Event Binding

    def connect_to_database(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="library_database")
        self.my_cursor = self.my_db.cursor()
        print("Connected First Time")

    def addData(self):
        if self.my_db is not None:

            query = """
                INSERT INTO library (Category, Experience, Subscription, Full_Name, Mail_Id, State, Qualification,
                                    Passout_Year, Video_Type, Name, Duration, Technology, Start_Date, End_Date, Rate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

# Created a tuple of data to insert
            data = (
                self.category_var.get(),
                self.experience_var.get(),
                self.subscription_var.get(),
                self.full_name_var.get(),
                self.mail_id_var.get(),
                self.state_var.get(),
                self.qualification_var.get(),
                self.passout_year_var.get(),
                self.video_type_var.get(),
                self.name_var.get(),
                self.duration_var.get(),
                self.technology_var.get(),
                self.start_date_var.get(),
                self.end_date_var.get(),
                self.rate_var.get()
            )

# Executed the SQL command
            self.my_cursor.execute(query, data)
            self.my_db.commit()  # Commit the transaction
            self.fetch_data_from_mysql()

            messagebox.showinfo("Success", "Data inserted successfully!")
            print("Data inserted successfully.")

    def fetch_data_from_mysql(self):
        """Fetched data from MySQL database and display it in the Treeview"""
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="library_database")

        if conn.is_connected():
            print("Connected Second Time")

# Created a cursor object to interact with the database
            cursor = conn.cursor()

# Executed the SELECT query
            query = "SELECT * FROM library"
            cursor.execute(query)

# Fetched all the rows
            rows = cursor.fetchall()

# Inserted rows into the Treeview widget
            if len(rows) != 0:

                self.libraryTable.delete(*self.libraryTable.get_children())
                for row in rows:
                    self.libraryTable.insert("", END, values=row)

# Closed the cursor and connection
            conn.commit()
            cursor.close()
            conn.close()
# Inserted the data into the text box in the desired format

    def showData(self):
        self.txtBox.insert(END, "Category:\t" + self.category_var.get() + "\n")
        self.txtBox.insert(END, "Experience:\t" +
                           self.experience_var.get() + "\n")
        self.txtBox.insert(END, "Subscription:\t" +
                           self.subscription_var.get() + "\n")
        self.txtBox.insert(END, "Full_Name:\t" +
                           self.full_name_var.get() + "\n")
        self.txtBox.insert(END, "Mail ID:\t" + self.mail_id_var.get() + "\n")
        self.txtBox.insert(END, "State:\t" + self.state_var.get() + "\n")
        self.txtBox.insert(END, "Qualification:\t" +
                           self.qualification_var.get() + "\n")
        self.txtBox.insert(END, "Passout Year:\t" +
                           self.passout_year_var.get() + "\n")
        self.txtBox.insert(END, "Video Type:\t" +
                           self.video_type_var.get() + "\n")
        self.txtBox.insert(END, "Name:\t" + self.name_var.get() + "\n")
        self.txtBox.insert(END, "Duration:\t" + self.duration_var.get() + "\n")
        self.txtBox.insert(END, "Technology:\t" +
                           self.technology_var.get() + "\n")
        self.txtBox.insert(END, "Start Date:\t" +
                           self.start_date_var.get() + "\n")
        self.txtBox.insert(END, "End Date:\t" + self.end_date_var.get() + "\n")
        self.txtBox.insert(END, "Rate:\t" + self.rate_var.get() + "\n")

    def get_cursor(self, event=""):
        # To get the currently focused row
        cursor_row = self.libraryTable.focus()
        content = self.libraryTable.item(cursor_row)
        rows = content.get("values")
# Checked if the row is valid
        if cursor_row == '':

            print("Selected row is empty")
            return  # Exit the function if the row has no values
# Checked if 'rows' is None or an empty list
        if rows is None or len(rows) == 0:
            print("There is no value")
            return

# Assigned values from the database or other data source to StringVars
        self.category_var.set(rows[0])
        self.experience_var.set(rows[1])
        self.subscription_var.set(rows[2])
        self.full_name_var.set(rows[3])
        self.mail_id_var.set(rows[4])
        self.state_var.set(rows[5])
        self.qualification_var.set(rows[6])
        self.passout_year_var.set(rows[7])
        self.video_type_var.set(rows[8])
        self.name_var.set(rows[9])
        self.duration_var.set(rows[10])
        self.technology_var.set(rows[11])
        self.start_date_var.set(rows[12])
        self.end_date_var.set(rows[13])
        self.rate_var.set(rows[14])

    def reset(self):

        self.category_var.set("")
        self.experience_var.set("")
        self.subscription_var.set("")
        self.full_name_var.set("")
        self.mail_id_var.set("")
        self.state_var.set("")
        self.qualification_var.set("")
        self.passout_year_var.set("")
        self.video_type_var.set("")
        self.name_var.set("")
        self.duration_var.set("")
        self.technology_var.set("")
        self.start_date_var.set("")
        self.end_date_var.set("")
        self.rate_var.set("")

    def iexit(self):
        iexit = tkinter.messagebox.askyesno(
            "Harry's Code Corner", "Are you sure?")
        if iexit > 0:
            self.root.destroy()
            return


# Created the Tkinter root window
if __name__ == "__main__":
    root = Tk()
    app = HarryCodeCorner(root)

# Started the Tkinter event loop
    root.mainloop()
