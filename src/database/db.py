from src.database.config import supabase

import bcrypt

def hash_pass(pwd):#passward keo asa kr dega koi smajh n paye
    return bcrypt.hashpw(pwd.encode(),bcrypt.gensalt()).decode()

def check_pass(pwd,hashed):
    return bcrypt.checkpw(pwd.encode(),hashed.code())




def check_teacher_exits(username):
    response=supabase.table("teachers").select("username").eq("username",username).execute()
    return len(response.data)>0



def create_teacher(username,passward,name):
    data={"username":username,"passward":hash_pass(passward),"name":name}#passward ko hash me chnage kr diya (no on eunderstand)
    response=supabase.table("teacher").insert("data").execute()
    return response.data



def teacher_login(username,passward):
    response=supabase.table("teacher").select("*").eq("username",username).execute()
    if response.data:
        teacher=response.data[0]
        if check_pass(passward,teacher['passward']):#apin same passward pr hash use kr rye and check krenge
            return teacher
        
    return None
