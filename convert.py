import pdfplumber
import re
import pandas as pd

file = 'BE COMP (2019 COURSE).pdf'

# Define regex patterns
student_re = re.compile(r'SEAT NO\.: (\S+)')
name_re = re.compile(r'NAME : ([A-Z\s]+?)(?= MOTHER|$)')
course_re = re.compile(r'^(\d{6}[A-Z]?) (.*?) \*')
credits_re = re.compile(r'TOTAL CREDITS EARNED : (\d+)')
points_re = re.compile(r'TOTAL GRADE POINTS / TOTAL CREDITS : (\d+)/(\d+)')
sgpi_re = re.compile(r'FOURTH YEAR SGPA : (\d+\.\d+)')
cgpi_re = re.compile(r'CGPA : (\d+\.\d+)')
DAA_re = re.compile(r'DESIGN & ANALYSIS OF ALGO. (\S+)/(\S+)\s*(\S+)/(\S+?)\s*(\S+)/(\S+)')
ML_re = re.compile(r' MACHINE LEARNING (\S+)/(\S+)\s*(\S+)/(\S+?)\s*(\S+)/(\S+)')
BT_re = re.compile(r' BLOCKCHAIN TECHNOLOGY (\S+)/(\S+)\s*(\S+)/(\S+?)\s*(\S+)/(\S+)')
CSDF_re = re.compile(r' CYBER SEC. & DIG. FORENSICS. (\S+)/(\S+)\s*(\S+)/(\S+?)\s*(\S+)/(\S+)')
STQA_re = re.compile(r' SOFT. TEST. & QLTY ASSURANCE (\S+)/(\S+)\s*(\S+)/(\S+?)\s*(\S+)/(\S+)')
MC_re = re.compile(r'MOBILE COMPUTING (\S+)/(\S+)\s*(\S+)/(\S+?)\s*(\S+)/(\S+)')
LP3_re = re.compile(r' LABORATORY PRACTICE - III * (---)\s*(---)\s*(---)\s*(\S+)/(\S+)\s*(\S+)/(\S+)')
LP4_re = re.compile(r'LABORATORY PRACTICE - IV (---)\s*(---)\s*(---)\s*(\S+)/(\S+)')
Project1_re = re.compile(r' PROJECT STAGE - I (---)\s*(---)\s*(---)\s*(\S+)/(\S+)')

class Line:
    def __init__(self, student, name, course, credits, points, sgpi, cgpi, DAA, ML, BT, CSDF, STQA, MC, LP3, LP4, Project1): 
        
        self.student = student
        self.name = name
        self.course = course
        self.credits = credits
        self.points = points
        self.sgpi = sgpi
        self.cgpi = cgpi
        self.DAA = DAA
        self.ML = ML
        self.BT = BT
        self.CSDF = CSDF
        self.STQA = STQA
        self.MC = MC
        self.LP3 = LP3
        self.LP4 = LP4
        self.Project1 = Project1

    def __repr__(self):
        return (f"Line(student={self.student}, name={self.name}, course={self.course}, "
                f"credits={self.credits}, points={self.points}, sgpi={self.sgpi}, cgpi={self.cgpi}, DAA={self.DAA}, ML={self.ML}, BT={self.BT}, CSDF={self.CSDF}, STQA={self.STQA}, MC={self.MC}, LP3={self.LP3}, LP4={self.LP4}, Project1={self.Project1})")
    

lines = []

# Open the PDF and extract text
with pdfplumber.open(file) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            # Initialize variables for storing data
            student = None
            name = None
            course = None
            credits = None
            points = None
            sgpi = None
            cgpi = None
            DAA = None
            ML = None
            BT = None
            CSDF = None
            STQA = None
            MC = None
            LP3 = None
            LP4 = None
            Project1 = None

            # Iterate through each line in the page
            for line in text.split('\n'):
                print(f"Processing line: {line}")  # Print each line for inspection

                # Perform regex searches
                student_match = student_re.search(line)
                name_match = name_re.search(line)
                course_match = course_re.search(line)
                credits_match = credits_re.search(line)
                points_match = points_re.search(line)
                sgpi_match = sgpi_re.search(line)
                cgpi_match = cgpi_re.search(line)
                DAA_match = DAA_re.search(line)
                ML_match = ML_re.search(line)
                BT_match = BT_re.search(line)
                CSDF_match = CSDF_re.search(line)
                STQA_match = STQA_re.search(line)
                MC_match = MC_re.search(line)
                LP3_match = LP3_re.search(line)
                LP4_match = LP4_re.search(line)
                Project1_match = Project1_re.search(line)
                
                if student_match:
                    student = student_match.group(1)
                if name_match:
                    name = name_match.group(1).strip()
                if course_match:
                    course = course_match.group(2)
                if credits_match:
                    credits = credits_match.group(1)
                if points_match:
                    points = (points_match.group(1), points_match.group(2))
                if sgpi_match:
                    sgpi = sgpi_match.group(1)
                if cgpi_match:
                    cgpi = cgpi_match.group(1)
                if DAA_match:
                    DAA = (DAA_match.group(1),'/', DAA_match.group(2),'/', DAA_match.group(3),'/', DAA_match.group(4), '/', DAA_match.group(5),'/', DAA_match.group(6))
                if ML_match:
                    ML = (ML_match.group(1),'/', ML_match.group(2),'/', ML_match.group(3),'/', ML_match.group(4), '/', ML_match.group(5),'/', ML_match.group(6))
                if BT_match:
                    BT = (BT_match.group(1),'/', BT_match.group(2),'/', BT_match.group(3),'/', BT_match.group(4), '/', BT_match.group(5),'/', BT_match.group(6))
                if CSDF_match:
                    CSDF = (CSDF_match.group(1),'/', CSDF_match.group(2),'/', CSDF_match.group(3),'/', CSDF_match.group(4), '/', CSDF_match.group(5),'/', CSDF_match.group(6))
                if STQA_match:
                    STQA = (STQA_match.group(1),'/', STQA_match.group(2),'/', STQA_match.group(3),'/', STQA_match.group(4), '/', STQA_match.group(5),'/', STQA_match.group(6))
                if MC_match:
                    MC = (MC_match.group(1),'/', MC_match.group(2),'/', MC_match.group(3),'/', MC_match.group(4), '/', MC_match.group(5),'/', MC_match.group(6))
                if LP3_match:
                   LP3 = (LP3_match.group(4), LP3_match.group(5), LP3_match.group(6), LP3_match.group(7))
                if LP4_match:
                   LP4 = (LP4_match.group(4), LP4_match.group(5))
                if Project1_match:
                   Project1 = (Project1_match.group(4), Project1_match.group(5))
                
                

                # If all required information is collected, create a Line object
                if student and name and credits and points and sgpi and cgpi and ML and CSDF and (STQA or MC) and LP3 and LP4 and Project1:
                    line_obj = Line(student, name, course, credits, points, sgpi, cgpi, DAA, ML, BT, CSDF, STQA, MC, LP3, LP4, Project1)
                    lines.append(line_obj)
                    
                    # Reset variables for the next entry
                    student = name = course = credits = points = sgpi = cgpi = DAA = ML = BT = CSDF = STQA = MC = LP3 = LP4 = Project1 = None

# Convert to DataFrame and save to CSV
df = pd.DataFrame([vars(line) for line in lines])
df.to_csv('extracted_data.csv', index=False)

print("Data extraction complete and saved to 'extracted_data.csv'.")
