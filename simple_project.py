# python-mobile-app
""" Creating basic layout using Gredlayout , label , coloumn , app, widget and Library in KIVY with the help of pycharm editor devlope a simple input-output ,details,button."""
import kivy 
from kivy.app import App
from kivy.uix.gridlayout import Gridlayout
from kivy.uix.label import Label
from kivy.uix.textinput import Textinput 
from kivy.uix.button import Button

class PrashantGrid(Gridlayout):
   def __init__(self,**kwargs):
     super(Prashant,self).__init__()
     self.cols=2
     self.add_widget(Label(text="Students Name: "))
     self.s_name=Textinput()
     self.add_widget(self.s_name)
     self.add_widget(Label(text="Students Marks: "))
     self.s_marks=Textinput()
     self.add_widget(self.s_marks)
     self.add_widget(Label(text="Student Gender: "))
     self.s_gender=Textinput()
     self.add_widget(self.s_gender)
     self.press=Button(text="Click Me ")
     self.press.bind(on_press=self.click_me)
     self.add_widget(self.press)
  
   
   def click_me(self,instance):
        print("You have enter Details Succesfully !! ")
        print("Name of student is  : ",self.s_name.text)
        print("marks of student are  : ",self.s_marks.text)
        print("Gender of student is  : ",self.s_gender.text)
   
class PrashantApp(App):
   def build(self):
     return PrashantGrid()

if __name__== "__main__":
  PrashantApp().run()
