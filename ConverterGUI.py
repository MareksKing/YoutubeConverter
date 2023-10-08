import customtkinter
from tkinter import messagebox
import subprocess

def select_folder(event):
    selected_folder = customtkinter.filedialog.askdirectory(title="Select download folder")
    if selected_folder:
        download_location_input.insert(0, selected_folder)
    else:
        print("No folder selected")

#Return true if link input is not empty
def validate_link_not_empty():
    youtube_link = link_input.get()
    if youtube_link:
        return bool(youtube_link)
    else:
        messagebox.showerror(title="Error", message="Enter a Youtube link")
        

def validate_download_location_not_empty():
    download_location=download_location_input.get()
    if download_location:
        return bool(download_location) 
    else:
        download_location_input.insert(0, "Downloads")
        messagebox.showinfo(title="Info", message="No location specified, defaults to Downloads")      
    

#Return true after all validations are true and start download
def validate_and_run():
    youtube_file="Youtube_Download.py"
    link_validation = validate_link_not_empty()
    validate_download_location_not_empty()
    if link_validation:
        subprocess.run(["python", youtube_file, "--link", link_input.get(), "--location", download_location_input.get(), "--type", download_type_segmented_button.get()])


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

root =customtkinter.CTk()
root.geometry("600x400")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill="both", expand=True)

link_label = customtkinter.CTkLabel(master=frame, text="Youtube Link")
link_label.pack(pady=12, padx=10)

link_input = customtkinter.CTkEntry(master=frame, placeholder_text="Link here", width=400)
link_input.pack(pady=12, padx=10)

download_location_input = customtkinter.CTkEntry(master=frame, placeholder_text="Select download location", width=200)
download_location_input.pack(pady=12, padx=10)

download_location_input.bind("<1>",command=select_folder)

download_type_segmented_button = customtkinter.CTkSegmentedButton(master=frame, values=["Audio only","Video & Audio"], width=600)
download_type_segmented_button.set("Audio only")
download_type_segmented_button.pack(pady=12, padx=10)


download_button = customtkinter.CTkButton(master=frame, text="Download", command=validate_and_run)
download_button.pack(pady=12, padx=10)



root.mainloop()