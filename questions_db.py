import sqlite3

def create_question_db():
    """
    Creates the 'questions.db' database and the 'questions' table if they don't exist.
    """
    conn = sqlite3.connect('questions.db')
    c = conn.cursor()

    # Create 'questions' table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS questions (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    options TEXT,
                    answer TEXT)''')

    conn.commit()
    conn.close()

def insert_questions():
    """
    Insert sample questions into the 'questions.db' database.
    This function should be called only once to populate the questions table.
    """
    questions = [
        ("What is the output of print(2 ** 3)?", "8,6,7,9", "8"),
        ("Which of the following is the correct syntax for defining a function in Python?", "def func():,function func():,def: func(),func(): def", "def func():"),
        ("Which data type is used to store a sequence of characters in Python?", "string,list,tuple,int", "string"),
        ("What is the keyword used to create a class in Python?", "create,define,class,object", "class"),
        ("Which operator is used to check equality in Python?", "==,=,===,!=", "=="),
        ("What is the correct syntax to import a module in Python?", "import module,module import,import('module'),from module import", "import module"),
        ("Which method is used to find the length of a list in Python?", "length(),len(),size(),count()", "len()"),
        ("What is the purpose of the break statement in Python?", "Stop the program,Exit the current loop,Skip the loop iteration,Return a value", "Exit the current loop"),
        ("What is the result of 5 / 2 in Python 3?", "2,2.5,2.0,3", "2.5"),
        ("What does the 'self' keyword represent in Python?", "A reference to the current object,A built-in function,A module,A global variable", "A reference to the current object"),
        ("Which Python data type is immutable?", "List,Set,Dictionary,Tuple", "Tuple"),
        ("What is the output of print('hello'.upper())?", "hello,HELLO,error,None", "HELLO"),
        ("Which of the following is used to define a comment in Python?", "//,#,/* */,%%", "#"),
        ("What is the correct way to declare a variable in Python?", "var x = 10,x: int = 10,x = 10,int x = 10", "x = 10"),
        ("What will be the output of the following Python code: print('1' + 1)?", "Error,11,TypeError,None", "TypeError"),
        ("Which function is used to get user input in Python?", "input(),get(),scan(),inputData()", "input()"),
        ("How do you create a dictionary in Python?", "dict = {},dict = [],dict = (),dict = ''", "dict = {}"),
        ("Which Python library is used for numerical calculations?", "math,numpy,pandas,numpy & pandas", "numpy"),
        ("What is the correct syntax to check if a variable x is greater than 5 in Python?", "if x > 5:,if x > 5 then:,if x > 5 do:,if 5 < x:", "if x > 5:"),
        ("How can you catch an exception in Python?", "try-except,catch-except,catch-finally,try-finally", "try-except"),
        ("What is the return type of the len() function?", "int,str,list,float", "int")
    ]
    
    conn = sqlite3.connect('questions.db')
    c = conn.cursor()
    
    # Insert each question into the database
    c.executemany('''INSERT INTO questions (question, options, answer) VALUES (?, ?, ?)''', questions)
    
    conn.commit()
    conn.close()

# Call the function to set up the questions database (run this once)
create_question_db()
insert_questions()
