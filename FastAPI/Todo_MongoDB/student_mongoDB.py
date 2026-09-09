# ============================================================
# 🎓 FastAPI Student App - MongoDB Atlas + MongoEngine
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import connect, Document, IntField, StringField, BooleanField

# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🌐 MongoDB Atlas Connection
# ------------------------------------------------------------
# Replace with your actual MongoDB connection string
MONGO_URL = "mongodb+srv://chaitanya_db:Joyboy3249@cluster0.ukc42xe.mongodb.net/student_db?appName=Cluster0"
connect(host=MONGO_URL)

# ------------------------------------------------------------
# 🧱 MongoDB Model 
# ------------------------------------------------------------
class StudentDB(Document):
    id = IntField(required=True, unique=True)
    name = StringField(required=True)
    age = IntField(required=True)
    grade = StringField(required=True)
    is_enrolled = BooleanField(default=True)

    meta = {
        "collection": "students"
    }

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class Student(BaseModel):
    id: int
    name: str
    age: int
    grade: str
    is_enrolled: bool = True

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "Student Management System API 🚀"}

# ------------------------------------------------------------
# ✅ 1. CREATE STUDENT
# ------------------------------------------------------------
@app.post("/students")
def create_student(student: Student):
    existing = StudentDB.objects(id=student.id).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    new_student = StudentDB(
        id=student.id,
        name=student.name,
        age=student.age,
        grade=student.grade,
        is_enrolled=student.is_enrolled
    )
    new_student.save()

    return {
        "message": "Student created successfully",
        "data": student
    }

# ------------------------------------------------------------
# ✅ 2. READ ALL STUDENTS
# ------------------------------------------------------------
@app.get("/students")
def get_all_students():
    students = StudentDB.objects()
    data = []

    for student in students:
        data.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "grade": student.grade,
            "is_enrolled": student.is_enrolled
        })

    return {
        "count": len(data),
        "data": data
    }

# ------------------------------------------------------------
# ✅ 3. READ SINGLE STUDENT
# ------------------------------------------------------------
@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = StudentDB.objects(id=student_id).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "grade": student.grade,
        "is_enrolled": student.is_enrolled
    }

# ------------------------------------------------------------
# ✅ 4. UPDATE STUDENT
# ------------------------------------------------------------
@app.put("/students/{student_id}")
def update_student(student_id: int, updated: Student):
    student = StudentDB.objects(id=student_id).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = updated.name
    student.age = updated.age
    student.grade = updated.grade
    student.is_enrolled = updated.is_enrolled
    student.save()

    return {
        "message": "Student updated successfully"
    }

# ------------------------------------------------------------
# ✅ 5. DELETE STUDENT
# ------------------------------------------------------------
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    student = StudentDB.objects(id=student_id).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.delete()

    return {
        "message": "Student deleted successfully"
    }

# ------------------------------------------------------------
# ▶️ Run Server
# ------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    # Make sure this matches your filename (e.g., student_mongoDB)
    uvicorn.run("student_mongoDB:app", host="127.0.0.1", port=8000, reload=True)
    