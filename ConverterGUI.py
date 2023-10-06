import customtkinter


#Return true if link input is not empty
def validate_link_not_empty():
    youtube_link = link_input.get()
    return bool(youtube_link)

#Return true if download type is selected
def validate_download_type():
    print(download_type_segmented_button.get())

def validate_and_run():
    validate_download_type()
    validate_link_not_empty()
    

def select_folder():
    selected_folder = customtkinter.filedialog.askdirectory(title="Select download folder")
    if selected_folder:
        download_location_input.configure(placeholder_text=selected_folder)
    else:
        print("No folder selected")

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

download_location_button = customtkinter.CTkButton(master=frame, text="Download location", command=select_folder)
download_location_button.pack(pady=12, padx=10)

download_type_segmented_button = customtkinter.CTkSegmentedButton(master=frame, values=["Audio only","Video & Audio"], width=600)
download_type_segmented_button.set("Audio only")
download_type_segmented_button.pack(pady=12, padx=10)


download_button = customtkinter.CTkButton(master=frame, text="Download", command=validate_and_run)
download_button.pack(pady=12, padx=10)



root.mainloop()