from pymongo import MongoClient
from flask import Flask
    
app = Flask(__name__)      
    
client = MongoClient('mongodb+srv://user:user123@cluster0.rjmqv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client['database']
col = db['transcripts']

# mydb = client["mydatabase"]
# mycol = mydb["customers"]

@app.route('/')
def home():
    mydict = { "name": "John", "address": "Highway 37" }
    db.col.insert_one(mydict)
    return 'Hello, World!'
    

if __name__ == "__main__":    
    app.run(debug=True)   