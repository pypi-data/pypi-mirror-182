import sys
sys.path.append("..")


from src.pkg.pkg1 import information_input as ii
from src.pkg.pkg1 import information_output as io
from src.pkg.pkg1 import information_check as ic
from src.pkg.pkg2 import Checking as ch
from src.pkg.pkg2 import Course as co
from src.pkg.pkg2 import Question as qu

def addition(num1, num2):
    return num1 + num2

# Checking.py
import unittest

class Test_output(unittest.TestCase):
    
    def setUp(self): 
        print('Set Up')
        self.student_name= 'lily'
        self.student_ID= 9130
        self.student_major='MDS'
        self.student_degree='Post'
        self.teacher_name= 'John'
        self.teacher_ID= 7788
        self.teachr_research='maching learning'
        self.teacher_length=5
        
    def tearDown(self):
        print('Tear Down')
        
    def test_student(self):
        p1= io.Student(self.student_name,self.student_ID,self.student_major,self.student_degree)
        p2 = io.Group(self.student_name,self.student_ID)
    
        self.assertEqual(p1.major,self.student_major)
        self.assertEqual(p1.degree,self.student_degree)
        self.assertEqual(p2.name,self.student_name)
        self.assertEqual(p2.ID,self.student_ID)
    
    def test_teacher(self):
        p3= io.Teacher(self.teacher_name,self.teacher_ID,self.teachr_research,self.teacher_length)
        p4 = io.Group(self.teacher_name,self.teacher_ID)
    
        self.assertEqual(p3.research,self.teachr_research)
        self.assertEqual(p3.length,self.teacher_length)
        self.assertEqual(p4.name,self.teacher_name)
        self.assertEqual(p4.ID,self.teacher_ID)
            
        
unittest.main(argv=[''], verbosity=2, exit=False)

class Test_check(unittest.TestCase):
    
    def setUp(self): 
        print('Set Up')
        self.right_name = 'lily'
        self.right1_name = 'Justin'
        self.right2_name = 'Travis'
        self.wrong_name = ''
        self.right_id = "12345"
        self.right2_id = "54321"
        self.wrong_id = "36345"
        self.wrong2_id = ""
                
    def tearDown(self):
        print('Tear Down')
        
    def test_check_inlist(self): #function
        right = ic.Info_Check(self.right_name,self.right_id)
        wrong = ic.Info_Check(self.wrong_name,self.wrong_id)
        right2 = ic.Info_Check(self.right2_id,self.right_id)
        wrong2 = ic.Info_Check(self.wrong_name,self.wrong_id)
        
        self.assertTrue(right.check_inlist())
        self.assertFalse(wrong.check_inlist())
        self.assertTrue(right2.check_inlist())
        self.assertFalse(wrong2.check_inlist())
              
        
    def test_check_IsNull(self):
        right = ic.Info_Check(self.right_name,self.right_id)
        wrong = ic.Info_Check(self.wrong_name,self.right_id)
        right1 = ic.Info_Check(self.right1_name,self.right_id)
        right2 = ic.Info_Check(self.right2_name,self.right_id)
        
        self.assertFalse(right.check_IsNull())
        self.assertTrue(wrong.check_IsNull())
        self.assertFalse(right1.check_IsNull())
        self.assertFalse(right2.check_IsNull())
        
        
class TestCheck(unittest.TestCase):
    def setUp(self): # Setting up for the test 
        print('Set Up')
        self.teacher_have_data = co.Course([{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "3","difficulty": "easy"}]," ", "teacher")
        self.teacher_have_no_data = co.Course([]," ", "teacher")
        self.student_have_data = co.Course([{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "3","difficulty": "easy"}]," ", "student")
        self.student_have_no_data = co.Course([]," ", "student")
        
    def tearDown(self):
        print('Tear Down')
    
    def test_isEmpty(self):
        self.assertTrue(self.teacher_have_data.isEmpty())
        self.assertFalse(self.teacher_have_no_data.isEmpty())
        self.assertTrue(self.student_have_data.isEmpty())
        self.assertFalse(self.student_have_no_data.isEmpty())
        
    def test_check_answer(self):
        self.assertTrue(self.teacher_have_no_data.check_answer("3","3"))
        self.assertFalse(self.teacher_have_no_data.check_answer("3","0"))
        self.assertTrue(self.student_have_data.check_answer("3","3"))
        self.assertFalse(self.student_have_data.check_answer("3","0"))

        
# Course.py
class TestCourse(unittest.TestCase):
    def setUp(self): # Setting up for the test 
        print('Set Up')
        self.correct_question = "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n"
        self.data1 = [{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "3","difficulty": "easy"}]
        self.data2 = [{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "4","difficulty": "normal"}]
        self.data3 = [{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "5","difficulty": "hard"}]
        self.data4 = [{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "6","difficulty": ""}]
        self.teacher_have_data1 = co.Course([{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "3","difficulty": "easy"}]," ", "teacher")
        self.teacher_have_data2 = co.Course([{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "4","difficulty": "normal"}]," ", "teacher")
        self.teacher_have_data3 = co.Course([{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "5","difficulty": "hard"}]," ", "teacher")
        self.teacher_have_data4 = co.Course([{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "6","difficulty": ""}]," ", "teacher")
    
    def tearDown(self):
        print('Tear Down')
        
    def test_append_text(self):
        for question in self.data1:
            self.assertEqual(self.teacher_have_data1.append_text(question), self.correct_question)
            
    def test_append_answer(self):
        for question in self.data1:
            self.assertEqual(self.teacher_have_data1.append_answer(question), "3")
        for question in self.data2:
            self.assertEqual(self.teacher_have_data2.append_answer(question), "4")
        for question in self.data3:
            self.assertEqual(self.teacher_have_data3.append_answer(question), "5")
        for question in self.data4:
            self.assertEqual(self.teacher_have_data4.append_answer(question), "6")

    def test_append_difficulty(self):
        for question in self.data1:
            self.assertEqual(self.teacher_have_data1.append_difficulty(question), "easy")
        for question in self.data2:
            self.assertEqual(self.teacher_have_data2.append_difficulty(question), "normal")
        for question in self.data3:
            self.assertEqual(self.teacher_have_data3.append_difficulty(question), "hard")
        for question in self.data4:
            self.assertEqual(self.teacher_have_data4.append_difficulty(question), "")

    
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestCheck))
    suite.addTest(unittest.makeSuite(TestCourse))
    suite.addTest(unittest.makeSuite(Test_output))
    suite.addTest(unittest.makeSuite(Test_check))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
    
my_suite()

                 
    
    
    
    
    
  