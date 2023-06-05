ximport mysql.connector as mycon
import speech_recognition as sr
import pyttsx3
import pandas as pd

db = mycon.connect(host="localhost", user="root", passwd="mysql", database="startle")
cursor = db.cursor()
db.autocommit = True
text = 0
login = 0
ID = 0
passwd = 0
choice = 0

# TEXT TO VOICE
def text_to_speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    rate = engine.getProperty("rate")
    engine.setProperty("rate", rate - 55)
    engine.setProperty("voice", voices[1].id)

    # say method on the engine that passes input text to be spoken
    engine.say(x)

    # run and wait method, it processes the voice commands.
    engine.runAndWait()
    return


# SPEECH RECOGNITION
def speech_recog(query):
    text_to_speech(query)
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=16000, chunk_size=2048) as source:

        r.adjust_for_ambient_noise(source)
        print(query)
        print("Listening....")

        audio = r.listen(source)
        print("audio recorded")

    try:
        text = r.recognize_google(audio)
        if text.lower() == "tu":
            text = str(2)
        print("you said: " + text)
        return text

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speech_recog(query)
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speech_recog(query)


# Display
def display():

    sql = "select * from employees;"
    cursor.execute(sql)
    data = cursor.fetchall()

    for i in data:
        print(i)


# Add more employees
def insert():
    input("press enter to command")
    ID = int(speech_recog("Enter ID of the employee: "))
    cursor.execute(f"select * from employees where ID='{ID}';")
    data = cursor.fetchone()
    print(data)
    if data is None:

        input("press enter to command")
        name = speech_recog("Enter name of the employee:")

        input("press enter to command")
        dsg = speech_recog("Enter designation of the employee:")

        input("press enter to command")
        sal = int(speech_recog("Enter salary of the employee:"))

        input("press enter to command")
        pfm = int(speech_recog("Enter performance rate out of 10 of the employee:"))

        input("press enter to command")
        phone = int(speech_recog("Enter mobile no of the employee:"))

        input("press enter to command")
        text_to_speech("Enter the joining date of the employee")
        year = input("Enter the joining date of the employee:")

        input("press enter to command")
        spouse = speech_recog("Enter name of spouse of the employee:")

        input("press enter to command")
        ads = speech_recog("Enter the address of the employee:")

        cursor.execute(
            f"insert into employees(ID, Name, Designation, Salary, Performance, Phone, Year_Joined, Spouse_Name, Address) values({ID},'{name}','{dsg}',{sal},{pfm},{phone},'{year}','{spouse}','{ads}');"
        )

        print("Record inserted Voila")

        text_to_speech("Please enter the new password for future login with this id")
        pswd = input("Please enter the new password for future login with this id")
        cursor.execute(f'insert into login_ids(ID, Password) values({ID},"{pswd}");')
        text_to_speech("Login details saved")

    else:
        print("Oops! Record already exists")


# Fire an employee
def delete():
    input("press enter to command")
    ID = int(speech_recog("Enter ID of the employee:"))
    sql = "select * from employees where ID=%s" % (ID)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data == None:
        text_to_speech("No such record exists sir")
        print("Non such record exists sir")
    else:
        sql1 = "delete from employees where ID=%s" % (ID)
        cursor.execute(sql1)
        sql2 = "delete from login_ids where ID=%s" % (ID)
        cursor.execute(sql2)
        text_to_speech("Record deleted successfully")
        print("Record deleted successfully")


# Update
def update():
    ID = int(speech_recog("Enter ID of the employee"))
    sql = "select * from employees where ID=%s" % (ID)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data == None:
        text_to_speech("No such record exists boss")
        print("No such record exists boss")
    else:
        text_to_speech("You have plenty of options boss")
        print("You have plenty of options boss")
        text_to_speech("Name")
        print("1)  NAME")
        text_to_speech("Designation")
        print("2)  DESIGNATION")
        text_to_speech("Salary")
        print("3)  SALARY")
        text_to_speech("Performance")
        print("4)  PERFORMANCe")
        text_to_speech("Phone number")
        print("5)  PHONE NUMBER")
        text_to_speech("Date Joined")
        print("6)  Date JOINED")
        text_to_speech("Spouse name")
        print("7)  SPOUSE NAME")
        text_to_speech("Address")
        print("8)  ADDRESS")

        input("press enter to command")
        x = input(speech_recog("What would you like to update"))
        if x == 1:
            input("press enter to command")
            m = speech_recog("Enter updated name of the employee")
            cursor.execute(f"update employees set Name='{m}' where ID={ID} ;")
            text_to_speech("Record updated")
            print("RECORD UPDATED")

        elif x == 2:
            input("press enter to command")
            m = speech_recog("Enter updated designation of the employee")
            cursor.execute(f"update employees set Designation='{m}' where ID={ID};")
            text_to_speech("Record updated")
            print("RECORD UPDATED")

        elif x == 3:
            input("press enter to command")
            m = speech_recog("Enter updated salary of the employee")
            cursor.execute(f"update employees set Salary={m} where ID={ID};")
            text_to_speech("Record updated")
            print("RECORD UPDATED")

        elif x == 4:
            input("press enter to command")
            m = speech_recog("Enter updated performance of the employee")
            cursor.execute(f"update employees set Performance={m} where ID={ID};")
            text_to_speech("Record updated")
            print("RECORD UPDATED")

        elif x == 5:
            input("press enter to command")
            m = speech_recog("Enter updated phone no of the employee")
            cursor.execute(f"update employees set Phone={m} where ID={ID};")
            text_to_speech("Record updated")
            print("RECORD UPDATED")

        elif x == 6:
            input("press enter to command")
            m = input("Enter updated year joined of the employee")
            cursor.execute(f"update employees set Year_Joined='{m}' where ID={ID};")
            text_to_speech("Record Updated")
            print("RECORD UPDATED")

        elif x == 7:
            input("press enter to command")
            m = speech_recog("Enter updated spouse name of the employee")
            cursor.execute(f"update employees set Spouse_Name='{m}' where ID={ID};")
            text_to_speech("Record updated")
            print("RECORD UPDATED")

        elif x == 8:
            input("press enter to command")
            m = input("Enter updated address of the employee")
            cursor.execute(f"update employees set Address='{m}' where ID={ID};")
            text_to_speech("Record updated")
            print("RECORD UPDATED")
        else:
            text_to_speech("No such updation is possible Boss")
            print("No such updation is possible Boss")


# Search a record
def search():
    input("press enter to command")
    ID = int(speech_recog("Enter ID of the employee"))
    cursor.execute(f"select * from employees where ID={ID};")
    data = cursor.fetchone()
    if data == None:
        text_to_speech("No such record exists")
        print("NO SUCH RECORD EXISTS")
    else:
        print(
            "ID",
            "\t",
            "Name",
            "\t",
            "Designation",
            "\t",
            "Salary",
            "\t",
            "Performance",
            "\t",
            "Phone",
            "\t",
            "Year_Joined",
            "\t",
            "Spouse_Name",
            "\t",
            "Address",
        )
        print(
            data[0],
            "\t",
            data[1],
            "\t",
            data[2],
            "\t",
            data[3],
            "\t",
            data[4],
            "\t",
            data[5],
            "\t",
            data[7],
            "\t",
            data[8],
        )
        text_to_speech(data)


#  MAIN PROGRAM

print("-------------------------------------------------------------------------------")
print("WELCOME TO STARTLE")
text_to_speech("Welcome To STARTLE")
print("INNOVATE . BELIEVE . CREATE")
text_to_speech("INNOVATE . BELIEVE . CREATE")
print(
    "--------------------------------------------------------------------------------"
)
print("EMPLOYEE MANAGEMENT SYSTEM")
text_to_speech("Presenting the Employee Management System")
text_to_speech("Login and you can access the customised Program")
login = int(input("Enter 1 for ADMIN and 2 for EMPLOYEES: "))
if login == 1:
    ID = int(input("Enter your ID:"))
    passwd = input("Enter your password: ")
    if ID == 100 and passwd == "iambest":
        print("GLAD TO HAVE YOU BACK BOSS")
        text_to_speech("Glad to have you Back Boss!")
        print("WHAT ARE YOU LOOKING FOR? ")
        text_to_speech("What are you looking for?")
        while True:
            print("1)  DISPLAY ALL RECORDS")
            text_to_speech("Display all records")
            print("2)  ADD MORE EMPLOYEES")
            text_to_speech("Add more employees to the database")
            print("3)  UPDATE A RECORD ")
            text_to_speech("Update a record")
            print("4)  SEARCH FOR A RECORD")
            text_to_speech("Search for a record")
            print("5)  FIRE AN EMPLOYEE")
            text_to_speech("Fire an employee")
            print("6)  LOG OUT")
            text_to_speech("Log Out")

            input("Press enter to command")
            try:

                choice = int(speech_recog("What do you choose: "))
            except:
                pass
            print(choice)

            if choice == 1:
                display()
            elif choice == 2:
                insert()
            elif choice == 3:
                update()
            elif choice == 4:
                search()
            elif choice == 5:
                delete()
            elif choice == 6:
                print("HAVE A GOOD DAY BOSS")
                text_to_speech("Have a good day Boss")
                break

            else:
                print("SORRY WRONG INPUT")
                text_to_speech("Sorry wrong input")

    else:
        print("ACCESS DENIED!")
        text_to_speech("Access Denied")

elif login == 2:
    ID = int(input("Enter your ID:"))
    passwd = input("Enter your password: ")
    cursor.execute(f"select * from login_ids where ID={ID};")
    data = cursor.fetchone()

    if data == None:
        print("Sorry. Wrong ID or Password. Please refresh the program to try again")
        text_to_speech(
            "Sorry. Wrong ID or Password. Please refresh the program to try again"
        )

    else:

        while True:
            print("WELCOME SIR")
            text_to_speech("Welcome Sir!")
            print("WHAT ARE YOU LOOKING FOR...?")
            text_to_speech("What are you looking for?")
            print("1)  DISPLAY ALL RECORDS")
            text_to_speech("Display all records")
            print("2)  SEARCH FOR A RECORD")
            text_to_speech("Search for a record")
            print("3)  LOG OUT")
            text_to_speech("Log Out")
            input("press enter to command")
            choice = int(speech_recog("What do you choose: "))
            if choice == 1:
                display()
            elif choice == 2:
                search()
            elif choice == 3:
                print("Logging Out...")
                text_to_speech("Logging out")
                break
            else:
                print("SORRY WRONG INPUT")
                text_to_speech("Sorry. Wrong input")