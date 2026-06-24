from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3
import os

DB = "school.db"


class LoginScreen(Screen):
    def login(self):
        email = self.ids.email.text
        pwd = self.ids.pwd.text

        conn = sqlite3.connect(DB)
        user = conn.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, pwd)
        ).fetchone()
        conn.close()

        if user:
            self.ids.msg.text = ""
            self.manager.current = "classes"
        else:
            self.ids.msg.text = "Invalid login details"


class ClassesScreen(Screen):

    def on_enter(self):
        self.ids.class_box.clear_widgets()

        classes = [
            "Baby Class", "Middle Class", "Top Class",
            "P1", "P2", "P3", "P4", "P5", "P6", "P7"
        ]

        from kivy.uix.button import Button

        for c in classes:
            btn = Button(text=c, size_hint_y=None, height=60)
            btn.bind(on_press=lambda x, cls=c: self.open_class(cls))
            self.ids.class_box.add_widget(btn)

    def open_class(self, cls):
        screen = self.manager.get_screen("student")
        screen.class_name = cls
        self.manager.current = "student"


class StudentScreen(Screen):

    class_name = ""

    def on_enter(self):
        self.ids.title.text = f"{self.class_name} Students"
        self.load_students()

    def add_student(self):

        name = self.ids.name.text
        gender = self.ids.gender.text
        dob = self.ids.dob.text
        phone = self.ids.phone.text
        emis = self.ids.emis.text

        if name == "":
            self.ids.msg.text = "Enter student name"
            return

        conn = sqlite3.connect(DB)

        try:
            conn.execute("""
                INSERT INTO students
                (name, class_name, gender, dob, phone, emis)
                VALUES(?,?,?,?,?,?)
            """, (
                name,
                self.class_name,
                gender,
                dob,
                phone,
                emis
            ))

            conn.commit()
            self.ids.msg.text = "Student saved"

        except:
            self.ids.msg.text = "Student already exists"

        conn.close()

        self.ids.name.text = ""
        self.ids.gender.text = ""
        self.ids.dob.text = ""
        self.ids.phone.text = ""
        self.ids.emis.text = ""

        self.load_students()

    def load_students(self):

        conn = sqlite3.connect(DB)

        students = conn.execute("""
            SELECT name, emis
            FROM students
            WHERE class_name=?
        """, (self.class_name,)).fetchall()

        conn.close()

        txt = ""

        for s in students:
            txt += f"{s[0]}   ({s[1]})\n"

        self.ids.students.text = txt


class WindowManager(ScreenManager):
    pass


class NymalaApp(App):

    def build(self):

        conn = sqlite3.connect(DB)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            password TEXT
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            class_name TEXT,
            gender TEXT,
            dob TEXT,
            phone TEXT,
            emis TEXT,
            UNIQUE(name, class_name)
            )
        """)

        conn.execute("""
            INSERT OR IGNORE INTO users
            (id,email,password)
            VALUES(1,'admin@school.com','admin123')
        """)

        conn.commit()
        conn.close()

        return Builder.load_file("nymala.kv")


if __name__ == "__main__":
    NymalaApp().run()
