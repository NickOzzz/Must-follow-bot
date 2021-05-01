from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.core.window import Window
import os
import sys
from selenium.webdriver.common.keys import Keys
from kivy.uix.spinner import Spinner

class mn(Screen):
    def __init__(self, **kwargs):
        super(mn, self).__init__(**kwargs)
        layout = FloatLayout(size=(350,600), )
        button1 = Button(text="START", pos_hint={"x": 0.365, "y": 0.05}, size_hint=(0.25, 0.08))
        self.txt1 = TextInput(multiline=False, pos_hint={"x": 0.365, "y": 0.55}, size_hint=(0.25, 0.08), hint_text="PASSWORD")
        self.txt2 = TextInput(multiline=False, pos_hint={"x": 0.365, "y": 0.65}, size_hint=(0.25, 0.08),
                         hint_text="LOGIN")
        self.txt3 = TextInput(multiline=False, pos_hint={"x": 0.365, "y": 0.75}, size_hint=(0.25, 0.08),
                         hint_text="USERNAME")
        self.txt4 = TextInput(multiline=False, pos_hint={"x": 0.365, "y": 0.45}, size_hint=(0.25, 0.08),
                              hint_text="AMOUNT OF FOLLOWS")
        self.txt5 = TextInput(multiline=False, pos_hint={"x": 0.365, "y": 0.35}, size_hint=(0.25, 0.08),
                              hint_text="TIME BETWEEN FOLLOWS")
        self.spinner = Spinner(text="CHOOSE", values=("Visualize", "Hidden interface"), size_hint=(0.25, 0.08),
                                    pos_hint={"x": 0.365, "y": 0.25})
        label = Label(text="INSTABOT", size_hint=(0.62, .07), pos_hint={"x": 0.175, "y": 0.85})
        self.label1 = Label(text="", size_hint=(0.62, .07), pos_hint={"x": 0.176, "y": 0.15}, color=(1, 0, 0, 1))
        button1.bind(on_press=self.launch_page)
        layout.add_widget(button1)
        layout.add_widget(self.txt1)
        layout.add_widget(self.txt2)
        layout.add_widget(self.txt3)
        layout.add_widget(self.txt4)
        layout.add_widget(self.txt5)
        layout.add_widget(self.spinner)
        layout.add_widget(label)
        layout.add_widget(self.label1)
        self.add_widget(layout)

    def launch_page(self, *args):
        m = True
        txt4 = ""
        txt5 = ""
        try:
            txt4 = int(self.txt4.text)
            m = False
        except Exception as e:
            self.label1.text = "please provide number in amount of follows"
        m = True
        try:
            txt5 = int(self.txt5.text)
            m = False
        except Exception as e:
            self.label1.text = "please provide number in time between follows"
        if not m:
            if self.txt1.text == "" or self.txt2.text == "" or self.txt3.text == "" or self.spinner.text == "CHOOSE" or self.txt4.text == "" or self.txt5.text == "":
                if self.txt1.text == "":
                    self.label1.text = "please provide password"
                elif self.txt2.text == "":
                    self.label1.text = "please provide login"
                elif self.txt3.text == "":
                    self.label1.text = "please provide username"
                elif self.txt4.text == "":
                    self.label1.text = "please provide amount of follows"
                elif self.txt5.text == "":
                    self.label1.text = "please provide time between follows"
                elif self.spinner.text == "CHOOSE":
                    self.label1.text = "please choose an option"
            else:
                key = True
                self.label1.text = ""
                if self.spinner.text == "Hidden interface":
                    hide = webdriver.ChromeOptions()
                    hide.add_argument('headless')
                    page = webdriver.Chrome(os.path.dirname(__file__) + "/bin/chromedriver", options=hide)
                elif self.spinner.text == "Visualize":
                    page = webdriver.Chrome(os.path.dirname(__file__) + "/bin/chromedriver")
                page.get("https://www.instagram.com/accounts/login/")
                try:
                    page.find_element_by_class_name("bIiDR").click()
                except Exception as e:
                    pass
                try:
                    time.sleep(1)
                    login = page.find_element_by_name("username")
                    password = page.find_element_by_name("password")
                    login.send_keys(str(self.txt2.text))
                    password.send_keys(str(self.txt1.text))
                    time.sleep(1)
                    page.find_element_by_class_name("y3zKF").click()
                except Exception as e:
                    time.sleep(1)
                    login = page.find_element_by_name("username")
                    password = page.find_element_by_name("password")
                    login.send_keys(str(self.txt2.text))
                    password.send_keys(str(self.txt1.text))
                    time.sleep(2)
                    page.find_element_by_class_name("y3zKF").click()
                time.sleep(3)
                if self.spinner.text == "Visualize":
                    try:
                        page.find_element_by_class_name("HoLwm").click()
                    except Exception as e:
                        self.label1.text = "please provide correct password, login and username"
                        key = False
                page.get(f"https://www.instagram.com/{self.txt3.text}/")
                try:
                    page.find_element_by_class_name("_bz0w").click()
                except Exception as e:
                    self.label1.text = "please provide correct password, login and username"
                    key = False
                counter = 1
                if key:
                    time.sleep(1)
                    switcher = True
                    while switcher:
                        if counter <= txt4:
                            try:
                                page.find_element_by_class_name("zV_Nj").click()
                                time.sleep(1)
                                for item in page.find_elements_by_class_name("L3NKy"):
                                    if counter <= txt4:
                                        try:
                                            if item.text == "Follow":
                                                item.click()
                                                counter += 1
                                                if txt5 > 0:
                                                    time.sleep(txt5)
                                        except Exception as e:
                                            pass
                                time.sleep(1)
                                page.find_element_by_class_name("Yx5HN").click()
                                time.sleep(1)
                                page.find_element_by_class_name("coreSpriteRightPaginationArrow").send_keys(Keys.RIGHT)
                                time.sleep(1)
                            except Exception as e:
                                self.label1.color = (0, 1, 0, 1)
                                self.label1.text = "Success"
                                switcher = False
                        else:
                            self.label1.color = (0, 1, 0, 1)
                            self.label1.text = "Success"
                            switcher = False
        self.follow()

    def follow(self):
        print("end")


scr = ScreenManager()
scr.add_widget(mn(name="mn"))


class InstaBot(App):
    def build(self):
        return scr


if __name__ == "__main__":
    Config.set('graphics', 'fullscreen', '0')
    Config.set('graphics', 'resizable', False)
    Config.set("graphics", "width", "750")
    Config.set("graphics", "height", "500")
    Config.write()
    Window.clearcolor = (1, 0.7, 0.8, 1)
    InstaBot().run()
