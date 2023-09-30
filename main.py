from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import re
class RegistrationApp(App):
    def build(self):
        self.title='REGISTRATION APP'
        layout=BoxLayout(orientation='vertical',padding=30,spacing=10)
        label=Label(text='PYTHON REGISTRATION FORM',font_size=26,bold=True,height=40)
        #adding_name_label
        name_label=Label(text='NAME',font_size=18)
        self.name_input=TextInput(multiline=False,font_size=25)
        email_label = Label(text='EMAIL', font_size=18)
        self.email_input = TextInput(multiline=False, font_size=25)
        password_label = Label(text='PASSWORD', font_size=18)
        self.password_input = TextInput(multiline=False, font_size=25)
        confirm_label = Label(text='CONFIRM PASSWORD', font_size=18)
        self.confirm_input = TextInput(multiline=False, font_size=25)
        button=Button(text='SUBMIT',font_size=18,on_press=self.register)
        layout.add_widget(label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(confirm_label)
        layout.add_widget(self.confirm_input )
        layout.add_widget(button)
        return layout
    def register(self,instance):
        name=self.name_input.text
        email=self.email_input.text
        password=self.password_input.text
        confirm=self.confirm_input.text
        pass_patt = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()-]).{8,}'
        email_pattr = r'[\w\.-]+@[\w\.-]+\.\w+'
        is_valid_pass=re.match(pass_patt,password)
        is_valid_email=re.match(email_pattr,email)
        if name=='' or email=='' or password=='' or confirm=='':
            message='PLEASE FILL IN ALL FIELDS'
        elif password != confirm:
            message = 'THE PASSWORDS DO NOT MATCH'
        elif not is_valid_pass:
            message='PASSWORD DO NOT MATCH THE REQUIREMENTS' \
                        'THERE SHOULD BE ATLEAST 1 UPPERCASE LETTER ,1 LOWER CASE LETTER,1 SPECIAL CHARACTER AND ATLEAST 1 DIGIT!'
        elif not is_valid_email:
            message='INVALID EMAIL'
        else:

                filename = name + '.txt'
                with open(filename, 'w') as f:
                    f.write(f'Name: {name} \n')
                    f.write(f'Email: {email} \n')
                    f.write(f'Password: {password} \n')
                message = 'REGISTRATION SUCCESSFUL!\nName: {}\nEmail: {}'.format(name, email)




        pop=Popup(title='REGISTRATION STATUS',content=Label(text=message),size_hint=(None,None),size=(800,400))
        message_label=Label(text=message,font_size=10)
        pop.content=message_label
        pop.open()






if __name__=='__main__':
    RegistrationApp().run()


