import numpy as np
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

def load_data(file_path):
    """Load data from a CSV file into a numpy array."""
    try:
        data = np.genfromtxt(file_path, delimiter=',', dtype=str, encoding='utf-8', skip_header=1)
        return data
    except Exception as e:
        messagebox.showerror("Error", f"Error loading data: {e}")
        return np.array([])

def search_student(data, student_id):
    """Search for a student's information by ID."""
    if data.size == 0:
        return "Dữ liệu không được tải."

    student_data = data[data[:, 0] == student_id]
    if student_data.size == 0:
        return f"Không tìm thấy thông tin cho sinh viên có ID {student_id}."
    else:
        return "\n".join([", ".join(row) for row in student_data])

def search_subject(data, subject_name):
    """Search for grades of a specific subject."""
    if data.size == 0:
        return "Dữ liệu không được tải."

    subject_data = data[data[:, 2] == subject_name]
    if subject_data.size == 0:
        return f"Không tìm thấy điểm cho môn học {subject_name}."
    else:
        return "\n".join([f"ID: {row[0]}, Tên: {row[1]}, Điểm: {row[3]}" for row in subject_data])

def calculate_average(data, student_id):
    """Calculate the average grade for a specific student using numpy."""
    if data.size == 0:
        return "Dữ liệu không được tải."

    student_data = data[data[:, 0] == student_id]
    if student_data.size == 0:
        return f"Không tìm thấy thông tin cho sinh viên có ID {student_id}."
    else:
        try:
            grades = student_data[:, 3].astype(float)  # Convert grades to float
            average_grade = np.mean(grades)
            return f"Trung bình cộng điểm của sinh viên có ID {student_id} là {average_grade:.2f}."
        except ValueError:
            return "Có lỗi khi chuyển đổi điểm sang số thực. Vui lòng kiểm tra dữ liệu."

def search_action():
    choice = choice_var.get()
    if choice == "student":
        student_id = simpledialog.askstring("Input", "Nhập ID sinh viên:")
        if student_id:
            result = search_student(data, student_id)
            messagebox.showinfo("Kết quả tìm kiếm", result)
    elif choice == "subject":
        subject_name = simpledialog.askstring("Input", "Nhập tên môn học:")
        if subject_name:
            result = search_subject(data, subject_name)
            messagebox.showinfo("Kết quả tìm kiếm", result)
    elif choice == "average":
        student_id = simpledialog.askstring("Input", "Nhập ID sinh viên:")
        if student_id:
            result = calculate_average(data, student_id)
            messagebox.showinfo("Kết quả tính toán", result)

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        global data
        data = load_data(file_path)
        messagebox.showinfo("Thông báo", "Dữ liệu đã được tải thành công.")

# GUI setup
root = tk.Tk()
root.title("Student Information System")

choice_var = tk.StringVar(value="student")

tk.Label(root, text="Chọn hành động:").pack()
tk.Radiobutton(root, text="Tìm kiếm sinh viên", variable=choice_var, value="student").pack()
tk.Radiobutton(root, text="Tìm kiếm môn học", variable=choice_var, value="subject").pack()
tk.Radiobutton(root, text="Tính điểm trung bình", variable=choice_var, value="average").pack()

tk.Button(root, text="Chọn tệp CSV", command=load_file).pack()
tk.Button(root, text="Thực hiện", command=search_action).pack()

root.mainloop()
