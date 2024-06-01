# Problem 1: Find Total Time Spent By Each Employee 


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['diff'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(['emp_id','event_day'])['diff'].sum().reset_index()
    return employees[['event_day','emp_id','diff']].rename(columns = {'event_day':'day', 'diff': 'total_time'})



#  Problem 2 : Number of Unique Subjects Taught By Each Teacher

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher[['teacher_id','subject_id']].drop_duplicates()
    df1=df.groupby('teacher_id')['subject_id'].count().reset_index()
    return df1.rename(columns={'subject_id' : 'cnt'})


 
#  Problem 3 : Classes more than 5 Students

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['student'].count().reset_index()
    return df[df.student>=5]['class'].to_frame()