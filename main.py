import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("350x300")
        self.title("Aplication")
        customtkinter.set_appearance_mode("dark")

        self.label_name = customtkinter.CTkLabel(self, text="Name")
        self.label_name.place(relx=0.5, rely=0.2, anchor="center")

        self.input_name = customtkinter.CTkEntry(self, placeholder_text="Input your name: ", width=300, height=35)
        self.input_name.place(relx=0.5, rely=0.3, anchor="center")

        self.label_password = customtkinter.CTkLabel(self, text="Password")
        self.label_password.place(relx=0.5, rely=0.5, anchor="center")

        self.input_name = customtkinter.CTkEntry(self, placeholder_text="Input your password: ", width=300, height=35)
        self.input_name.place(relx=0.5, rely=0.6, anchor="center")


        self.button = customtkinter.CTkButton(self, width=300, text="Logar")
        self.button.place(relx="0.5", rely="0.8", anchor="center")



app = App()
app.mainloop()
