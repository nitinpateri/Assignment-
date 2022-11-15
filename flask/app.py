#importing modules
from flask import Flask, render_template, request, redirect
import csv



app = Flask(__name__)



#Index Page
@app.route('/')
def index():
    return render_template('index.html')

#importing user details
@app.route("/details")
def details():

   
    #Adding the details into files

    file = open("users.csv","r+",newline='')       
    data = csv.reader(file)
    writer = csv.writer(file)            
    Id = request.args.get('id')
    first_name =request.args.get('first_name')
    last_name =request.args.get('last_name')
    username =request.args.get('username')
    email =request.args.get('email')
    gender =request.args.get('gender')
    dob = request.args.get('dob')
    address = request.args.get('address')
    for i in data:
        if i[0]==Id or i[3]==username:
            return render_template("invalid.html")
    user_details = [Id,first_name,last_name,username,email,dob,gender,address]
    writer.writerow(user_details)
    file.close()

     #Sorting the details 

    file = open("users.csv",'r') 
    data = []
    for i in file:
        data.append(i.split(','))
    file.close()
    length = len(data)
    for i in range(1,length):
        for j in range(1,length):
            if int(data[j-1][0]) > int(data[j][0]):
                data[j-1],data[j] = data[j],data[j-1]
    file = open(" users-sorted.csv","w",newline='')
    writer = csv.writer(file)
    for i in data:
        writer.writerow(i)

        
    return render_template("success.html")

    

@app.route("/search")
def search():
    if request.method == 'GET':
        id = request.args.get("search")
        file = open("users.csv","r")
        for i in file:
            print(i.split(',')[0],id)
            if i.split(',')[0]==str(id):
                return render_template("User-details.html",data=i)
        return render_template("user-not-found.html")
if __name__=="__main__":

    app.run(host='0.0.0.0', port='8000', debug='True')