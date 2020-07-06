# Pandas for processing data
from pandas import read_csv, read_parquet

# sys to access command line arguments
import sys

# To use standard json format
import json

# To access ".parquet" file
import pyarrow


# Function responsible for processing data and converting to json report
# Arguments -> students : dataframe containing students data; teachers : dataframe containing teachers data
def process_data(students, teachers):

    # data : json data
    data = []

    for indx, row in teachers.iterrows():
        tmp = {'teacher_id': row['id'],
               'teacher_name': row['fname'] + ' ' + row['lname'],
               'class_id': row['cid']}

        tmp_obj = []
        for ind, _row in students[students['cid'] == row['cid']].iterrows():
            st_obj = {'student_id': _row['id'],
                 'student_name': _row['fname'] + ' ' + _row['lname']}
            tmp_obj.append(st_obj)
        
        tmp['students'] = tmp_obj    
        data.append(tmp)

    # Writing json data to a file
    with open('data.json', 'w') as student_object:
        json.dump(data, student_object,indent=4)


    # print the json data
    print(data)


if __name__ == "__main__":

    # If no command line arguments are passed
    if len(sys.argv)==1:
        try:
            teachers = read_parquet('teachers.parquet', engine='pyarrow')
            students = read_csv('students.csv', delimiter='_')
            process_data(students, teachers)

        except FileNotFoundError as e:
            print(e)


    # Case in which links to files saved in S3 are passed
    else:
        if len(sys.argv)>1 and  sys.argv[1] == 's3':

            # smart_open to access files stored in S3, uses 'boto3' in backend.
            from smart_open import smart_open

            try:
                aws_id = sys.argv[2]
                aws_secret = sys.argv[3]
                bucket_name = sys.argv[4]
                object_key_teacher='teachers.parquet' if (len(sys.argv)==5) else sys.argv[5]
                object_key_student = 'students.csv'if (len(sys.argv)==5) else sys.argv[6]

                path = 's3://{}:{}@{}/{}'.format(aws_id, aws_secret, bucket_name, object_key_teacher)
                teachers = read_parquet(smart_open(path),engine='pyarrow')

                path = 's3://{}:{}@{}/{}'.format(aws_id, aws_secret, bucket_name, object_key_student)
                students = read_csv(smart_open(path), delimiter='_')

                process_data(students, teachers)

            except Exception as e:
                print(e)


        # Case in which paths to files saved in local device are passed
        elif sys.argv[1]!= 's3':
            try:
                teachers = read_parquet(sys.argv[1], engine='pyarrow')
                students = read_csv(sys.argv[2], delimiter='_')
                process_data(students, teachers)

            except Exception as e:
                print(e)