import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

cred = credentials.Certificate("E:\Codes\E.D.I.T.H\serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognitionbu-default-rtdb.firebaseio.com/"
})

ref = db.reference("students")

info = {
    "E23CSEU0301":
    {"Name":"Pranav Gupta",
     "Enrollment_No" : "E23CSEU0301", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0302":
    {"Name":"Harshit Dhar",
     "Enrollment_No" : "E23CSEU0302", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0303":
    {"Name":"Harsh Sinha",
     "Enrollment_No" : "E23CSEU0303", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0304":
    {"Name":"Aryan Tyagi",
     "Enrollment_No" : "E23CSEU0304", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0305":
    {"Name":"Aarav Sareen",
     "Enrollment_No" : "E23CSEU0305", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0306":
    {"Name":"Sarthak Arora",
     "Enrollment_No" : "E23CSEU0306", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0307":
    {"Name":"Divyansh Chouhan",
     "Enrollment_No" : "E23CSEU0307", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0308":
    {"Name":" Harpreet Singh Gandh",
     "Enrollment_No" : "E23CSEU0308", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0309":
    {"Name":" Prince pokharna",
     "Enrollment_No" : "E23CSEU0309", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0310":
    {"Name":"Saksham Pandit",
     "Enrollment_No" : "E23CSEU0310", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0311":
    {"Name":"Mehar Singh",
     "Enrollment_No" : "E23CSEU0311", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0312":
    {"Name":"Jayesh Anand",
     "Enrollment_No" : "E23CSEU0312", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0313":
    {"Name":"Aditi Singh",
     "Enrollment_No" : "E23CSEU0313", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0314":
    {"Name":"Abhinav Vainkatesh",
     "Enrollment_No" : "E23CSEU0314", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0315":
    {"Name":"Harshit Dwivedi",
     "Enrollment_No" : "E23CSEU0315", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0316":
    {"Name":"Arsh Srivastava",
     "Enrollment_No" : "E23CSEU0316", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },
    
    "E23CSEU0317":
    {"Name":" Nitya Goel",
     "Enrollment_No" : "E23CSEU0317", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0318":
    {"Name":"Jashanpreet Singh",
     "Enrollment_No" : "E23CSEU0318", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0319":
    {"Name":"Bakul Mehta",
     "Enrollment_No" : "E23CSEU0319", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0320":
    {"Name":"Krrish Chhabra",
     "Enrollment_No" : "E23CSEU0320", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0321":
    {"Name":"Anousha Singh",
     "Enrollment_No" : "E23CSEU0321", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0322":
    {"Name":"Krish bagga",
     "Enrollment_No" : "E23CSEU0322", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0323":
    {"Name":" Kairav Dixit",
     "Enrollment_No" : "E23CSEU0323", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0324":
    {"Name":"Anant Mishra",
     "Enrollment_No" : "E23CSEU0324", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0325":
    {"Name":"Navya Purohit",
     "Enrollment_No" : "E23CSEU0325", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0326":
    {"Name":"Kshitij Sahdev",
     "Enrollment_No" : "E23CSEU0326", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0327":
    {"Name":"Mrigashi",
     "Enrollment_No" : "E23CSEU0327", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0328":
    {"Name":"Ashvin sharma",
     "Enrollment_No" : "E23CSEU0328", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0329":
    {"Name":"Samya Gupta",
     "Enrollment_No" : "E23CSEU0329", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU0330":
    {"Name":"Jay Wardhan Suri",
     "Enrollment_No" : "E23CSEU0330", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU2421":
    {"Name":"Chirag Sethi",
     "Enrollment_No" : "E23CSEU2421", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    },

    "E23CSEU2422":
    {"Name":"Ayushman Sirohi",
     "Enrollment_No" : "E23CSEU2422", 
     "Batch" : "11",
     "Last_Attendance" : "2023-10-25 10-40-33"
    }

    
}

for key, value in info.items() : 
    ref.child(key).set(value)
