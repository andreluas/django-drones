FROM python:3.8
WORKDIR /demanda-project
COPY . /demanda-project/
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
RUN python manage.py migrate
# CMD ["python manage.py runserver 0:8000"]