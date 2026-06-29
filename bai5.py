# chủ đề : QUẢN LÝ SINH VIÊN
from fastapi import FastAPI , HTTPException

app = FastAPI()

# 6 api dựa trên chủ đề đã chọn + 2 api tự nghĩ

# xem danh sách toàn bộ sinh viên
@app.get("/students")
def get_student():
    pass

# xem chi tiết từng sinh viên
@app.get("/students/detail")
def get_detail_student():
    pass

# thêm mới sinh viên
@app.post("/students")
def add_student():
    pass

# cập nhật thông tin của sinh viên
@app.put("/students/update")
def update_student():
    pass

# xóa sinh viên 
@app.delete("/students/delete")
def delete_student():
    pass

# xem danh sách sinh viên qua môn 
@app.get("/students/pass")
def get_pass_student():
    pass

# xem top các sinh viên có điểm cao nhất
@app.get("/students/highest_point")
def get_highest_point_student():
    pass

# xem sinh viên theo từng lớp
@app.get("/students/class")
def get_students_by_class():
    pass