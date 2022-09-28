from django.shortcuts import render
import psycopg2
from django.http import HttpResponse

#Access AWWS DB code
conn  = psycopg2.connect(database="postgres",
                        host="db-hw3.cintcumqd4if.us-east-1.rds.amazonaws.com",
                        user="postgres",
                        password="hw3password",
                        port="5432")
cursor = conn.cursor()
cursor.execute('SELECT VERSION()')

vers = cursor.fetchone()

cursor.close()

words = "<H1>Alexis Sanchez's HW3</H1>"
final  = f"{words}{vers}"

# Create your views here.
def home(request):
    return HttpResponse(final)