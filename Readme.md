## **Task :**
This python application processes the two data files [students.csv , teachers.parquet], which can be provided as an absolute path and also as S3 bucket files.
Then the application outputs a report in json, listing each student and the teacher which the student has and the class ID the student is scheduled for.

## **System requirements :**
- OpenSSL 1.1.1
- python 3.6

## **Modules used :**
- pandas (for processing csv and parquet files)
- os (to access files from local directory)
- json (to output a proper json formatted data)
- pyarrow (to access parquet files)
- smart_open (to access files from S3)

## **Set up environment :**
- **Create an environment :**
```python
python -m virtualenv env
```

- **Activate environment :**
```python
source env/bin/activate
```

- **Install requirements**
```python
pip install requirements.txt
```

## **Commands to run :**
- **Git clone command :**
```python
git clone <url>
```

- **Command to run :**
```python
python app.py
python app,py [path1 (.parquet)] [path2 (.csv)]
python app.py s3 [access_key] [secret_access_key] [bucket_name] [object_key_1 (.parquet)] [object_key_2 (.csv)]
```

- **Docker commands :**
```dockerfile
docker build app . 
docker run app
```