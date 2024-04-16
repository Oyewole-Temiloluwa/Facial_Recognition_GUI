
import cv2 as cv
import tkinter as tk
import util
from PIL import Image, ImageTk
import os
import face_recognition
import datetime
import pickle

class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry('1200x620+350+100')

        self.login_button_main_window = util.get_button(self.main_window, 'Login', color='green', command=self.login, )
        self.login_button_main_window.place(x=750, y=300)

        self.register_new_user_button_main_window = util.get_button(self.main_window, 'Register New User', color='grey', command=self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=750, y=400)

        self.text_viewer_window = util.get_button(self.main_window, 'Attendance Display', color='blue', command=self.attendance_display,)
        self.text_viewer_window.place(x=750, y=500)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)

        self.db_dir = '.\db' 

        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)
        
        self.log_path = './log.txt'

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv.VideoCapture(0)
        
        self._label = label

        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        self.most_recent_capture_arr = frame

        img_ = cv.cvtColor(self.most_recent_capture_arr, cv.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)
    
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)

        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)
    
    def login(self):
        name = util.recognize(self.most_recent_capture_arr, self.db_dir)
        if name in ['unknown_person', 'no_persons_found']:
            util.msg_box('Ooopssssss.....', 'Unknown user, Please register or try again')
        else:
            util.msg_box('Welcome', 'Welcome, {}'.format(name))
            with open(self.log_path, 'a') as f:
                f.write('{}, {}\n'.format(name, datetime.datetime.now()))
                f.close()

    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry('1200x520+370+120')
        
        self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Accept', color='green',command=self.accept_register_new_user)
        self.accept_button_register_new_user_window.place(x=750, y=300)

        self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Try Again', color='red',command=self.try_again_register_new_user)
        self.try_again_button_register_new_user_window.place(x=750, y=400)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750, y= 150)

        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window, 'Please, \n input username:')
        self.text_label_register_new_user.place(x=750, y=70)
    
    def attendance_display(self):
        text_widget = tk.Text(self.main_window, wrap=tk.WORD)
        text_widget.pack(fill=tk.BOTH, expand=True)
        #file_path = filedialog.askopenfilename(filetypes=[("Attendance List", "C:\\Users\\hp\\FaceRecognition\\Scripts\\Prohect\log.txt")])
        with open(".\log.txt", "r") as file:
            text = file.read()
            text_widget.delete(1.0, tk.END)  # Clear existing text
            text_widget.insert(tk.END, text)  # Insert file content into text widget
    
    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()


    def start(self):
        self.main_window.mainloop()

    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0, 'end-1c')

        embeddings = face_recognition.face_encodings(self.register_new_user_capture)[0]

        file = open(os.path.join(self.db_dir, '{}.pickle'.format(name)), 'wb')
        pickle.dump(embeddings, file)

        util.msg_box('Success', 'User was registered successfully')

        self.register_new_user_window.destroy()

if __name__ == '__main__':
    app = App()
    app.start()
