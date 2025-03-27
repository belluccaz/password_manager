from tkinter import messagebox

class DataManager:
    @staticmethod
    def save(website, email, password):
        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
            return False  # Indica que o salvamento falhou

        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?"
        )

        if is_ok:
            try:
                with open("data.txt", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password}\n")
                
                return True  # Indica que o salvamento foi bem-sucedido
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving the data:\n{e}")
                return False  # Indica que o salvamento falhou
        
        return False  # Caso o usuário cancele a ação
