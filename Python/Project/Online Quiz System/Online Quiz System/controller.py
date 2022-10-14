from flask import Flask,render_template,request

app = Flask(__name__,template_folder = "templates") 

list_student = []
list_question = []
list_resut = []
dashbord_name = ""
dashbord_score = 0

class student :
    student_name =""
    student_email = ""
    student_pswd = ""
    student_score = 0
    def __init__(self,name,email,password):
        self.student_name= name
        self.student_email =email
        self.student_pswd = password
        
class class_question :
    ID =""
    question =""
    option1 =""
    option2 =""
    option3 =""
    option4 =""
    correct_option = ""
    def __init__(self,ID,question,option1,option2,option3,option4,correct_option):
        self.ID =ID
        self.question =question
        self.option1 = option1
        self.option2 = option2
        self.option3 =option3
        self.option4 = option4
        self.correct_option = correct_option

class class_result:
    r_name = ""
    total_question = 0
    answer = 0
    wrong = 0
    percentage = 0.0
    def __init__(self,sname,stotal_question,sanswer,):
        self.r_name = sname
        self.total_question = stotal_question
        self.answer = sanswer
        self.wrong = stotal_question - sanswer
        self.percentage = (sanswer/stotal_question)*100 
            
    
    
            

def getUser_info (record,x):
    countComma = 0
    store=""
    idx = 0
    while ((countComma<x) and idx<len(record)):
        c = record[idx]
        if( c ==','):
            countComma+=1
        elif (countComma==x-1):
            store=store+c
        idx+=1
    return store   
  
  

def load_data():
    filestudent = open("studentdata.txt","r")
    store_student = filestudent.read().splitlines()  
    for studentinfo in store_student:
        load_name = getUser_info(studentinfo,1)
        load_email =getUser_info(studentinfo,2)
        load_pswd =  getUser_info(studentinfo,3)
        addstudent=student(load_name,load_email,load_pswd)
        list_student.append(addstudent) 
    filestudent.close()     
        
def load_questions():
    filequestion = open("questions.txt","r")
    store_questions = filequestion.read().splitlines()  
    for questioninfo in store_questions:
        load_id = getUser_info(questioninfo,1)
        load_question =getUser_info(questioninfo,2)
        load_option1 =  getUser_info(questioninfo,3)
        load_option2 =  getUser_info(questioninfo,4)
        load_option3 =  getUser_info(questioninfo,5)
        load_option4 = getUser_info(questioninfo,6)
        load_correctoption = getUser_info(questioninfo,7)
        addquestion=class_question(load_id,load_question,load_option1,load_option2,load_option3,load_option4,load_correctoption)
        list_question.append(addquestion)             
    filequestion.close()

def load_result():
    fileresult = open("result.txt","r")
    store_result = fileresult.read().splitlines()
    print(store_result)
    for resultinfo in store_result:
        load_result_name = getUser_info(resultinfo,1)
        load_result_total =int( getUser_info(resultinfo,2))
        load_result_answer = int(getUser_info(resultinfo,3))
        add_result =class_result(load_result_name,load_result_total,load_result_answer )
        list_resut.append(add_result) 
    
load_data()
load_questions()
load_result()

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("registration.html")

@app.route("/login")
def login():
    return render_template("login.html")

def  check_student(login_name,login_pswd):
    for i in  list_student:
        if(login_name==i.student_name and login_pswd== i.student_pswd):
            return True
    return False    
            
    

@app.route("/submitlogin" , methods = ['POST','GET'] )
def submit_login():
    global dashbord_name
    if request.method == 'POST':
        login_name = request.form['name']
        login_pswd = request.form['pswd']
        print(login_name,login_pswd)
        if(login_name == "ADMIN") and (login_pswd=="123"):
            return render_template("indexadmin.html")
        elif(check_student(login_name,login_pswd)):
            
            dashbord_name =login_name
            return render_template("indexstudent.html" , print_name = dashbord_name)
       
    
@app.route("/submitregister" ,methods = ['POST','GET'] )
def sunmit_register():
    
    if request.method == 'POST':
        register_name = request.form['full-name']  
        register_email = request.form['your-email'] 
        register_pass = request.form['password'] 
        register_confirm_pass = request.form['comfirm-password']
        if(register_pass == register_confirm_pass):
            addstudent=student(register_name,register_email,register_pass)
            list_student.append(addstudent)
            print(list_student[0].student_name)
            
            store = register_name +","+register_email+","+register_pass
            print(store)
            filestudent = open("studentdata.txt","a")
            print(store,file=filestudent,sep="\n")
            filestudent.close() 
            return render_template("login.html") 

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", print_name = dashbord_name ,l_question = len(list_question))  

@app.route("/startquiz")
def startquiz():
    return render_template("question.html", print_name = dashbord_name)

@app.route ("/veiwstudent")
def veiw_students():
    global list_student
    list_student = []
    load_data()
    return render_template("veiwstudent.html" , list_student = list_student ,length = len(list_student))         

@app.route("/veiwquestion")
def veiw_questions():
    global list_question
    list_question = []
    load_questions()
    return render_template("question.html" ,list_question = list_question ,length_question = len(list_question)) 

@app.route("/veiwresult")
def veiw_result():
    return render_template("quizresult.html" ,print_name = dashbord_name , quiz_score = dashbord_score , l_question = len(list_question))

@app.route("/quizstart")
def quiz_start():
    global list_question
    list_question = []
    load_questions()
    return render_template("startquiz.html" ,print_name = dashbord_name,list_question = list_question ,l_question = len(list_question))  

def check_name(dashbord_name):
    for nam in list_resut:
        if(dashbord_name==nam.r_name):
            return False            
    return True
    
@app.route("/submitquiz" ,methods = ['POST','GET'] )
def submit_quiz():
    global dashbord_score
    correct_count = 0
    
    for Q in list_question:
        new_id = str(Q.ID)
        selected_option = request.form[new_id]
        correct_option = Q.correct_option
        if(selected_option == correct_option):
            correct_count = correct_count+1    
    dashbord_score = correct_count   
    
    if(check_name(dashbord_name)):
        add_result = class_result(dashbord_name,len(list_question),correct_count)
        list_resut.append(add_result)
        fileresult=open("result.txt","a")
        print(dashbord_name+","+str(len(list_question))+str(correct_count)) 
        fileresult.close()
        
    return render_template("check_result.html" ,print_name = dashbord_name , l_question = len(list_question) )           

@app.route("/addquestion")
def add_question():
    return render_template("addquestion.html",list_question = list_question ,l_question = len(list_question))

@app.route("/submitaddquestion", methods=['POST','GET'] )
def submit_addquestion():
    save_temp =""
    save_correct = 0
    save_questionID = request.form['addquestionID']
    save_question = request.form['addquestion']
    save_option1 = request.form['addoption1']
    save_option2 = request.form['addoption2']
    save_option3 = request.form['addoption3']
    save_option4 = request.form['addoption4']
    if (request.form['123'] == "1"):  
        save_correct = save_option1  
    elif (request.form['123'] == "2"):  
        save_correct = save_option2    
    elif (request.form['123'] == "3"):
        save_correct = save_option3      
    elif (request.form['123'] == "4"): 
        save_correct = save_option4 
    filequestion = open("questions.txt","a")    
    save_temp = str(save_questionID)+","+save_question+","+save_option1 +","+save_option2 +","+save_option3+","+save_option4+","+save_correct
    print(save_temp,file=filequestion,sep='\n')
    filequestion.close()
    return render_template("addquestion.html")
           
@app.route("/veiwallresult")
def veiw_all_result():
    return render_template("veiwallresult.html",list_result = list_resut )    

@app.route("/indexstudent")
def index_student():
    return render_template("indexstudent.html",print_name = dashbord_name ) 
@app.route("/studentanswer")
def student_answer():
    return render_template("studentquestion.html",list_question = list_question ,l_question =int(len(list_question)),print_name = dashbord_name)

@app.route("/indexadmin")
def idex_admin():
    return render_template("indexadmin.html")

if(__name__ =="__main__"):
    app.run(debug=True )