import tkinter as tk
from organizer import get_files
import customtkinter as ctk
ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("green")    
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("File organizer")
        
        # Name Label
        self.nameLabel = ctk.CTkLabel(self,
                                      text="Source Folder")
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
        self.src_entry= ctk.CTkEntry(self)
        self.src_entry.grid(row=0, column=2,
                            padx=20, pady=20,
                            sticky="ew")
        self.browse_btn=ctk.CTkButton(self,text='Browse',command=self.browse_src_folder)
        self.browse_btn.grid(row=0, column=3,
                            padx=20, pady=20,
                            sticky="ew")
        self.dest_lbl=ctk.CTkLabel(self,text='Destination')
        self.dest_lbl.grid(row=2, column=0,
                            padx=20, pady=20,
                            sticky="ew")
        self.dest_entry=ctk.CTkEntry(self)
        self.dest_entry.grid(row=2,column=2,padx=20, pady=20,
                            sticky="ew")
        self.browse_btn=ctk.CTkButton(self,text='Browse',command=self.browse_destination_folder)
        self.browse_btn.grid(row=2, column=3,
                            padx=20, pady=20,
                            sticky="ew")
        self.file_type_lbl=ctk.CTkLabel(self,text='File Type')
        self.file_type_lbl.grid(row=3,column=0)
        self.file_type_entry=ctk.CTkEntry(self)
        self.file_type_entry.grid(row=3,column=2)
        self.search_term_lbl=ctk.CTkLabel(self,text='Search Term')
        self.search_term_lbl.grid(row=4,column=0,padx=20, pady=20,
                            sticky="ew")
        self.search_term_entry=ctk.CTkEntry(self)
        self.search_term_entry.grid(row=4,column=2)
        self.status_label=ctk.CTkLabel(self,text='',fg_color='black')
        self.organize_lbl=ctk.CTkButton(self,text='Organize Files',command=self.organize)
        self.organize_lbl.grid(row=5,column=2,padx=20, pady=20,
                            sticky="ew")
    def organize(self):
          source_entry=self.src_entry.get()+'/'
          destination_folder=self.dest_entry.get()+'/'
          extension=self.file_type_entry.get()
          search_term=self.search_term_entry.get()
          try:
               if search_term:
                   get_files(extension,source_entry,destination_folder,search_term)
               else:
                   get_files(extension,source_entry,destination_folder)
               self.status_label.config(text="Files organized successfully", fg="green")
          except Exception as e:
                   self.status_label.config(text="Error: " + str(e), fg="red")
    def browse_src_folder(self):
           source_folder=tk.filedialog.askdirectory()
           self.src_entry.delete(0,ctk.END)
           self.src_entry.insert(0,source_folder)
    def browse_destination_folder(self):
            destination_folder=tk.filedialog.askdirectory()
            self.dest_entry.delete(0,ctk.END)
            self.dest_entry.insert(0,destination_folder)

if __name__=='__main__':
	app=App()
	app.mainloop()