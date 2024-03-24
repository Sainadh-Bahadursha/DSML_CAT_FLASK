# following comment used to download python 3.9.13 version along with slim-buster OS
# Actually this docker file goes to another docker file regarding slim-buster to do many operations
# windows based os are heavy
FROM python:3.9.13-slim-buster

# Working directory
WORKDIR /Users/saina/Desktop/DS_ML_AI/Scaler/Module_17_MLOPS/Lecture_4_Containerization_- _Docker_&_DockerHub/Docker_Working_directory

# Copy the requirements to working directory
COPY requirements.txt ./

# to avoid upgrade pip error
RUN python -m pip install --upgrade pip

# to install all the libraries which are in the requirements.txt without cache(optional)
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files in current directory to working directory by using two dots
COPY . .

# to create the command to run the flask app predictios.py which was done in last class by command prompt command
# local host used is 0.0.0.0 it is like public access host. It is Optional 
CMD ["python","-m","flask","--app","predictions.py","run","--host=0.0.0.0"]
