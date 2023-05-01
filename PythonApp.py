# python-mobile-app
""" Creating basic layout using Gridlayout , label , coloumn , app, widget and Library in KIVY with the help of pycharm editor devlope a simple input-output ,details,button."""
import kivy #Framework (Library)
from kivy.app import App
#To Arrange Widgets Properly
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import  TextInput
#To Use Buttons To Interaction
from kivy.uix.button import Button

#making class - OOP (Layout)
class PrashantGrid(GridLayout):
    def __init__(self,**kwargs): #many arguments 
        super(PrashantGrid,self).__init__()

        self.cols=2
        #Student Name widget
        self.add_widget(Label(text="Student Name :"))
        self.s_name=TextInput()
        self.add_widget(self.s_name)

        #student Marks Widget
        self.add_widget(Label(text="Student's Marks :"))
        self.s_marks= TextInput()
        self.add_widget(self.s_marks)

        #student Gender
        self.add_widget(Label(text="Student's Gender :"))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        #Button
        self.press= Button(text="Click Me")
        # to add Interactivity
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)



    def click_me(self,instance):

        print("You Have Entered Details Succesfully.")
        #to Return Details on Console
        print("Name of Student   -> ",self.s_name.text)
        print("Marks of Student  -> ", self.s_marks.text)
        print("Gender of Student -> ", self.s_gender.text)




class PrashantApp(App):

    def build(self):
        return PrashantGrid()

if __name__=="__main__" :
    PrashantApp().run()
