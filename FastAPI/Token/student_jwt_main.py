# ============================================================
# 🎓 FastAPI Student App + MongoDB + JWT Authentication
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from mongoengine import connect, Document, IntField, StringField, BooleanField
from jose import JWTError, jwt
from datetime import datetime, timedelta

app = FastAPI()

# ------------------------------------------------------------
# 🔐 JWT CONFIGURATION
# ------------------------------------------------------------
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = timedelta(minutes=5)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Token expired or invalid")

# ------------------------------------------------------------
# 🌐 MongoDB Atlas Connection
# ------------------------------------------------------------
# Replace with your actual MongoDB connection string
MONGO_URL = "mongodb+srv://chaitanya_db:Joyboy3249@cluster0.ukc42xe.mongodb.net/student_db?appName=Cluster0"
connect(host=MONGO_URL)

# ------------------------------------------------------------
# 🧱 Models & Schemas
# ------------------------------------------------------------
class StudentDB(Document):
    id = IntField(required=True, unique=True)
    name = StringField(required=True)
    age = IntField(required=True)
    grade = StringField(required=True)
    is_enrolled = BooleanField(default=True)
    meta = {"collection": "students"}

class Student(BaseModel):
    id: int
    name: str
    age: int
    grade: str
    is_enrolled: bool = True

class Login(BaseModel):
    username: str
    password: str

# ------------------------------------------------------------
# 🔐 LOGIN API
# ------------------------------------------------------------
@app.post("/login")
def login(user: Login):
    # Dummy Login
    if user.username != "admin" or user.password != "admin123":
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer", "expires_in": "5 minutes"}

# ------------------------------------------------------------
# ✅ PROTECTED CRUD OPERATIONS
# ------------------------------------------------------------
@app.post("/students")
def create_student(student: Student, user: str = Depends(verify_token)):
    existing = StudentDB.objects(id=student.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Student ID already exists")

    new_student = StudentDB(**student.dict())
    new_student.save()
    return {"message": "Student created successfully", "data": student}

@app.get("/students")
def get_all_students(user: str = Depends(verify_token)):
    students = StudentDB.objects()
    data = [{"id": s.id, "name": s.name, "age": s.age, "grade": s.grade, "is_enrolled": s.is_enrolled} for s in students]
    return {"count": len(data), "data": data}

@app.get("/students/{student_id}")
def get_student(student_id: int, user: str = Depends(verify_token)):
    student = StudentDB.objects(id=student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"id": student.id, "name": student.name, "age": student.age, "grade": student.grade, "is_enrolled": student.is_enrolled}

@app.put("/students/{student_id}")
def update_student(student_id: int, updated: Student, user: str = Depends(verify_token)):
    student = StudentDB.objects(id=student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student.update(**updated.dict(exclude={'id'}))
    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int, user: str = Depends(verify_token)):
    student = StudentDB.objects(id=student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student.delete()
    return {"message": "Student deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("student_jwt_main:app", host="127.0.0.1", port=8000, reload=True)
    