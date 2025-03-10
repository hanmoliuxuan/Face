import sys
import cv2
import numpy as np
import sqlite3
import os
from PySide6 import QtCore
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QWidget, QMessageBox)
from PySide6.QtSql import QSqlTableModel, QSqlDatabase
from ui import Ui_Form
from deepface import DeepFace

def create_database_tables(con):
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS face_list (
            name TEXT,
            user_id INTEGER Primary Key,
            photo_file TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS check_list (
            name TEXT,
            user_id INTEGER,
            time DATETIME
        )
    ''')
    con.commit()

def show_error_message(parent, title, message):
    QMessageBox.critical(parent, title, message)

def show_warning_message(parent, title, message):
    QMessageBox.warning(parent, title, message)

def show_info_message(parent, title, message):
    QMessageBox.information(parent, title, message)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 初始化摄像头
        self.cap_video = cv2.VideoCapture(0)
        if not self.cap_video.isOpened():
            show_error_message(self, "错误", "无法打开摄像头")
            sys.exit(1)

        # 初始化定时器
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(50)

        # 创建存储目录
        try:
            os.makedirs("face_list", exist_ok=True)
        except OSError as e:
            show_error_message(self, "错误", f"无法创建 face_list 目录: {e}")
            sys.exit(1)

        self.con = sqlite3.connect("face_info.db")
        create_database_tables(self.con)

        # 连接到数据库
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('face_info.db')
        if not self.db.open():
            show_error_message(self, "错误", "无法打开数据库")
            sys.exit(1)

        # 连接信号
        self.ui.add.clicked.connect(self.add_photo)
        self.ui.check.clicked.connect(self.checkface)

        # 显示 check_list 数据
        self.display_check_list()

    def update_frame(self):
        ret, img = self.cap_video.read()
        if ret:
            frame = self.process_frame(img)
            self.show_frame(frame)

    def process_frame(self, img):
        shrink = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        shrink = cv2.flip(shrink, 1)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(shrink, cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(shrink, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return shrink

    def show_frame(self, frame):
        QtImg = QImage(frame.data,
                       frame.shape[1],
                       frame.shape[0],
                       frame.shape[1] * 3,
                       QImage.Format_RGB888)
        jpg_out = QPixmap(QtImg).scaled(
            self.ui.label.width(), self.ui.label.height())
        self.ui.label.setPixmap(jpg_out)

    def add_photo(self):
        name = self.ui.name.text().strip()
        user_id = self.ui.id.text().strip()

        if not name or not user_id:
            show_warning_message(self, "提示", "姓名和 ID 不能为空")
            return

        if self.is_duplicate_info(name, user_id):
            show_warning_message(self, "提示", "该用户信息已存在，请勿重复添加！")
            return

        ret, frame = self.cap_video.read()
        if ret:
            photo_filename = f"face_list/{name}_{user_id}.jpg"
            cv2.imwrite(photo_filename, frame)
            show_info_message(self, "添加成功", "照片添加成功！")

            self.add_info_to_database(name, user_id, photo_filename)

    def is_duplicate_info(self, name, user_id):
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM face_list WHERE name =? AND user_id =?", (name, user_id))
        return cursor.fetchone() is not None

    def add_info_to_database(self, name, user_id, photo_filename):
        cursor = self.con.cursor()
        cursor.execute("INSERT INTO face_list (name, user_id, photo_file) VALUES (?,?,?)",
                       (name, user_id, photo_filename))
        self.con.commit()

    def checkface(self):
        ret, frame = self.cap_video.read()
        if ret:
            face_list_dir = "face_list"
            for filename in os.listdir(face_list_dir):
                if filename.endswith(('.jpg', '.jpeg', '.png')):
                    img2_path = os.path.join(face_list_dir, filename)
                    try:
                        ver = DeepFace.verify(img1_path=frame, img2_path=img2_path, model_name="VGG-Face")
                        name,userid=os.path.splitext(filename)[0].split("_")
                        if ver.get("verified"):
                            show_info_message(self, "验证成功", f"验证成功！ID: {userid}")
                            self.add_check_info_to_database(name, userid)
                            # 更新 check_list 显示
                            self.display_check_list()
                            return
                    except Exception as e:
                        print(f"比对 {img2_path} 时出现错误: {e}")
            show_warning_message(self, "验证失败", "未找到匹配的人脸！")

    def add_check_info_to_database(self, name, user_id):
        cursor = self.con.cursor()
        cursor.execute("INSERT INTO check_list (name, user_id, time) VALUES (?,?,DATETIME('now'))",
                       (name, user_id))
        self.con.commit()

    def display_check_list(self):
        # 创建 QSqlTableModel
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('check_list')
        self.model.select()

        # 设置表头
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "姓名")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "时间")

        # 将模型设置到 QTableView
        self.ui.check_list.setModel(self.model)

    def closeEvent(self, event):
        """窗口关闭时释放资源"""
        self.cap_video.release()
        self.con.close()
        self.db.close()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())