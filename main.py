import sys
import cv2
import sqlite3
import os
from PySide6 import QtCore
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QWidget, QMessageBox)
from PySide6.QtSql import QSqlTableModel, QSqlDatabase
from ui import Ui_Form
from deepface import DeepFace
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import datetime

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

        self.ui.maintab.setTabVisible(1, False)
        self.ui.maintab.setTabVisible(2, False)
        self.ui.maintab.setTabVisible(3, False)
        self.ui.maintab.setTabVisible(4, False)

        self.cap_video = cv2.VideoCapture(0)
        if not self.cap_video.isOpened():
            show_error_message(self, "错误", "无法打开摄像头")
            sys.exit(1)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(50)

        try:
            os.makedirs("face_list", exist_ok=True)
        except OSError as e:
            show_error_message(self, "错误", f"无法创建 face_list 目录: {e}")
            sys.exit(1)

        self.con = sqlite3.connect("face_info.db")
        create_database_tables(self.con)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('face_info.db')
        if not self.db.open():
            show_error_message(self, "错误", "无法打开数据库")
            sys.exit(1)

        self.ui.add.clicked.connect(self.add_photo)
        self.ui.check.clicked.connect(self.checkface)
        self.ui.admin_login.clicked.connect(self.admin_login)
        self.ui.exit.clicked.connect(self.exit)
        self.ui.update_name.clicked.connect(self.update_user_name)
        self.ui.update_id.clicked.connect(self.update_user_id)
        self.ui.update_ph.clicked.connect(self.update_photo)
        self.ui.del_user.clicked.connect(self.delete_user)
        self.ui.find.clicked.connect(self.find_user_by_id)

        self.display_face_list()
        self.display_check_list()

    def update_frame(self):
        ret, img = self.cap_video.read()
        if ret:
            frame = self.process_frame(img)
            self.show_frame(frame)
        self.plot_check_list_last_three_days()

    def update_user_name(self):
        new_name = self.ui.u_name.text().strip()
        user_id = self.ui.u_id.text().strip()

        if not new_name or not user_id:
            show_warning_message(self, "提示", "新姓名和 ID 不能为空")
            return

        try:
            cursor = self.con.cursor()
            cursor.execute("UPDATE face_list SET name =? WHERE user_id =?", (new_name, user_id))
            self.con.commit()

            if cursor.rowcount > 0:
                show_info_message(self, "更新成功", "用户姓名更新成功！")
            else:
                show_warning_message(self, "更新失败", "未找到对应的用户 ID，请检查输入。")
        except Exception as e:
            show_error_message(self, "错误", f"更新用户姓名时出现错误: {e}")
        self.display_face_list()

    def update_user_id(self):
        new_id = self.ui.u_id.text().strip()
        name = self.ui.u_name.text().strip()

        if not new_id or not name:
            show_warning_message(self, "提示", "新 ID 和姓名不能为空")
            return

        try:
            cursor = self.con.cursor()
            cursor.execute("UPDATE face_list SET user_id =? WHERE name =?", (new_id, name))
            self.con.commit()
            if cursor.rowcount > 0:
                show_info_message(self, "更新成功", "用户 ID 更新成功！")
            else:
                show_warning_message(self, "更新失败", "未找到对应的用户姓名，请检查输入。")
        except Exception as e:
            show_error_message(self, "错误", f"更新用户 ID 时出现错误: {e}")

        self.display_face_list()

    def update_photo(self):
        name = self.ui.u_name.text().strip()
        user_id = self.ui.u_id.text().strip()

        if not name or not user_id:
            show_warning_message(self, "提示", "姓名和 ID 不能为空")
            return

        # 查询用户是否存在
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM face_list WHERE name =? AND user_id =?", (name, user_id))
        result = cursor.fetchone()
        if not result:
            show_warning_message(self, "更新失败", "未找到对应的用户信息，请检查输入。")
            return

        ret, frame = self.cap_video.read()
        if ret:
            photo_filename = f"face_list/{name}_{user_id}.jpg"
            if os.path.exists(photo_filename):
                os.remove(photo_filename)
            cv2.imwrite(photo_filename, frame)
            show_info_message(self, "更新成功", "照片更新成功！")

            cursor.execute("UPDATE face_list SET photo_file =? WHERE name =? AND user_id =?",
                           (photo_filename, name, user_id))
            self.con.commit()

        self.display_face_list()

    def delete_user(self):
        name = self.ui.u_name.text().strip()
        user_id = self.ui.u_id.text().strip()

        if not name or not user_id:
            show_warning_message(self, "提示", "姓名和 ID 不能为空")
            return

        try:
            cursor = self.con.cursor()
            cursor.execute("SELECT photo_file FROM face_list WHERE name =? AND user_id =?", (name, user_id))
            result = cursor.fetchone()
            if result:
                photo_filename = result[0]
                if os.path.exists(photo_filename):
                    os.remove(photo_filename)
                cursor.execute("DELETE FROM face_list WHERE name =? AND user_id =?", (name, user_id))
                cursor.execute("DELETE FROM check_list WHERE name =? AND user_id =?", (name, user_id))
                self.con.commit()
                show_info_message(self, "删除成功", "用户信息删除成功！")
            else:
                show_warning_message(self, "删除失败", "未找到对应的用户信息，请检查输入。")
        except Exception as e:
            show_error_message(self, "错误", f"删除用户信息时出现错误: {e}")

        self.display_face_list()

    def find_user_by_id(self):
        user_id = self.ui.find_id.text().strip()

        if not user_id:
            show_warning_message(self, "提示", "ID 不能为空")
            return

        try:
            cursor = self.con.cursor()
            cursor.execute("SELECT * FROM face_list WHERE user_id =?", (user_id,))
            result = cursor.fetchone()

            if result:
                self.face_list_model.setFilter(f"user_id = {user_id}")
                self.face_list_model.select()
                show_info_message(self, "查找成功", "已在列表中显示匹配用户信息。")
            else:
                self.face_list_model.setFilter("")
                self.face_list_model.select()
                show_warning_message(self, "查找失败", "未找到对应的用户信息，请检查输入。")
        except Exception as e:
            show_error_message(self, "错误", f"查找用户信息时出现错误: {e}")

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

    def checkface(self):
        self.plot_check_list_last_three_days()
        ret, frame = self.cap_video.read()
        if ret:
            face_list_dir = "face_list"

            try:
                results = DeepFace.find(
                    img_path=frame, db_path=face_list_dir, model_name="VGG-Face", enforce_detection=True
                )

                if len(results) > 0 and not results[0].empty:
                    file_path = results[0].iloc[0]['identity']
                    file_name = os.path.basename(file_path)
                    name = file_name.split("_")[0]
                    user_id = file_name.split("_")[1].split(".")[0]
                    show_info_message(self, "找到匹配人脸",
                                      f"找到匹配的人脸！姓名: {name}")
                    self.add_check_info_to_database(name, user_id)
                    self.display_check_list()
                    return True
                else:
                    show_warning_message(self, "未找到匹配人脸", "未找到匹配的人脸。")
                    return False

            except ValueError as e:
                if "Face could not be detected" in str(e):
                    show_error_message(self, "检测错误", "错误：输入图像中未检测到人脸！")
                    return False
                else:
                    raise e

    def add_check_info_to_database(self, name, user_id):
        cursor = self.con.cursor()
        cursor.execute("INSERT INTO check_list (name, user_id, time) VALUES (?,?,DATETIME('now'))",
                       (name, user_id))
        self.con.commit()

    def display_check_list(self):
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('check_list')
        self.model.select()

        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "姓名")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "时间")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "时间")

        self.ui.check_list.setModel(self.model)

    def exit(self):
        self.ui.maintab.setTabVisible(1, False)
        self.ui.maintab.setTabVisible(2, False)
        self.ui.maintab.setTabVisible(3, False)
        self.ui.maintab.setTabVisible(4, False)

    def admin_login(self):
        admin_password = "admin"
        password = self.ui.admin_pass.text()
        if password == admin_password:
            show_info_message(self, "登录成功", "管理员登录成功！")
            self.ui.maintab.setTabVisible(1, True)
            self.ui.maintab.setTabVisible(2, True)
            self.ui.maintab.setTabVisible(3, True)
            self.ui.maintab.setTabVisible(4, True)

    def closeEvent(self, event):
        self.timer.stop()
        self.cap_video.release()
        self.con.close()
        self.db.close()
        event.accept()

    def display_face_list(self):
        self.face_list_model = QSqlTableModel(self, self.db)
        self.face_list_model.setTable('face_list')
        self.face_list_model.select()

        self.face_list_model.setHeaderData(0, QtCore.Qt.Horizontal, "姓名")
        self.face_list_model.setHeaderData(1, QtCore.Qt.Horizontal, "ID")
        self.face_list_model.setHeaderData(2, QtCore.Qt.Horizontal, "照片文件")

        self.ui.user_list.setModel(self.face_list_model)

    def plot_check_list_last_three_days(self):
        cursor = None
        try:
            cursor = self.con.cursor()
            cursor.execute("SELECT DATE(time), COUNT(*) FROM check_list WHERE DATE(time) >= DATE('now', '-3 days') GROUP BY DATE(time)")
            results = cursor.fetchall()

            today = datetime.date.today()
            three_days_ago = today - datetime.timedelta(days=2)
            all_dates = [str(three_days_ago + datetime.timedelta(days=i)) for i in range(3)]

            data_dict = {date: 0 for date in all_dates}
            for date, count in results:
                data_dict[date] = count

            dates = list(data_dict.keys())
            counts = list(data_dict.values())

            plt.rcParams['font.sans-serif'] = ['SimHei']
            plt.rcParams['axes.unicode_minus'] = False

            fig, ax = plt.subplots()
            plt.rcParams['figure.dpi'] = 100
            plt.rcParams['savefig.dpi'] = 100
            plt.rcParams['figure.autolayout'] = True

            ax.plot(dates, counts, marker='o', color='skyblue', antialiased=True)
            ax.set_xlabel('日期')
            ax.set_ylabel('识别量')
            ax.set_title('最近三天识别量统计')

            ax.set_ylim(bottom=0)

            for x, y in zip(dates, counts):
                ax.annotate(f'{y}',
                            xy=(x, y),
                            xytext=(0, 3),
                            textcoords="offset points",
                            ha='center', va='bottom')

            canvas = FigureCanvas(fig)

            label_size = self.ui.draw.size()
            canvas.resize(label_size.width(), label_size.height())

            pixmap = QPixmap(canvas.grab().toImage())
            self.ui.draw.setPixmap(pixmap.scaled(label_size))

            plt.close(fig)
        except sqlite3.Error as e:
            show_error_message(self, "数据库错误", f"数据库查询失败：{str(e)}")
        except Exception as e:
            show_error_message(self, "图表生成错误", f"生成图表时发生错误：{str(e)}")
        finally:
            if cursor:
                cursor.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())