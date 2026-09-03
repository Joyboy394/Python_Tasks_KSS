# ============================================================
# 🎓 FastAPI Student Management System - MySQL Version
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, ConfigDict, EmailStr
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
import uvicorn

# ------------------------------------------------------------
# 🚀 Initialize App
# ------------------------------------------------------------
app = FastAPI(title="Student Management API")

# ------------------------------------------------------------
# 🗄️ MySQL Database Configuration
# ------------------------------------------------------------
# Using the credentials you provided earlier. 
# Make sure the 'student_db' database exists in MySQL!
DATABASE_URL = "mysql+pymysql://root:Joyboy%403249@localhost:3306/student_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ------------------------------------------------------------
# 🧱 Database Model (SQLAlchemy)
# ------------------------------------------------------------
class StudentDB(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    grade = Column(String(10), nullable=False)

# Auto-create the table if it doesn't exist
Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------
# 🧾 Pydantic Schemas (Data Validation - V2 Syntax)
# ------------------------------------------------------------
class StudentCreate(BaseModel):
    name: str
    age: int
    email: str
    grade: str

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str
    grade: str

    model_config = ConfigDict(from_attributes=True)

# ------------------------------------------------------------
# 🔌 Database Dependency
# ------------------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------------------------------------------
# 🏠 Root Endpoint
# ------------------------------------------------------------
@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Management API 🎓"}

# ------------------------------------------------------------
# ✅ 1. CREATE Student
# ------------------------------------------------------------
@app.post("/students/", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = db.query(StudentDB).filter(StudentDB.email == student.email).first()
    if db_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_student = StudentDB(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# ------------------------------------------------------------
# ✅ 2. READ ALL Students
# ------------------------------------------------------------
@app.get("/students/", response_model=list[StudentResponse])
def get_all_students(db: Session = Depends(get_db)):
    return db.query(StudentDB).all()

# ------------------------------------------------------------
# ✅ 3. READ SINGLE Student
# ------------------------------------------------------------
@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# ------------------------------------------------------------
# ✅ 4. UPDATE Student
# ------------------------------------------------------------
@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, updated_data: StudentCreate, db: Session = Depends(get_db)):
    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    student.name = updated_data.name
    student.age = updated_data.age
    student.email = updated_data.email
    student.grade = updated_data.grade

    db.commit()
    db.refresh(student)
    return student

# ------------------------------------------------------------
# ✅ 5. DELETE Student
# ------------------------------------------------------------
@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()
    return None

# ------------------------------------------------------------
# ▶️ Run Server
# ------------------------------------------------------------
if __name__ == "__main__":
    # Ensure this file is saved as main.py for this command to work
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    