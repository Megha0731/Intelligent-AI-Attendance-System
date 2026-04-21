from src.database.config import supabase

import bcrypt

def hash_pass(pwd):#passward keo asa kr dega koi smajh n paye
    return bcrypt.hashpw(pwd.encode(),bcrypt.gensalt()).decode()

def check_pass(pwd,hashed):
    return bcrypt.checkpw(pwd.encode(),hashed.encode())




def check_teacher_exits(username):
    response=supabase.table("teachers").select("username").eq("username",username).execute()
    return len(response.data)>0



def create_teacher(username,password,name):
    data={"username":username,"password":hash_pass(password),"name":name}#passward ko hash me chnage kr diya (no on eunderstand)
    response=supabase.table("teachers").insert(data).execute()
    return response.data



def teacher_login(username,password):
    response=supabase.table("teachers").select("*").eq("username",username).execute()
    if response.data:
        teacher=response.data[0]
        if check_pass(password,teacher['password']):#apin same passward pr hash use kr rye and check krenge
            return teacher
        
    return None
def get_all_students():
    response=supabase.table('student').select('*').execute()
    return response.data