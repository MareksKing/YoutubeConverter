import customtkinter


def validate():
    global download_type_label
    value = option.get()
    if value == "Audio":
        download_type_label.configure(text ="Downloading audio only")
    elif value == "Video":
        download_type_label.configure(text ="Downloading video and audio.")
    else:
        download_type_label.configure(text ="A download type must be selected.")
        
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

download_type_label = customtkinter.CTkLabel(master=frame, text="Select download type")
download_type_label.pack(pady=12, padx=10)
option = customtkinter.StringVar()

download_type_audio = customtkinter.CTkRadioButton(master=frame, text="Audio only", value="Audio",variable=option)
download_type_audio.pack(pady=12, padx=10)

download_type_video = customtkinter.CTkRadioButton(master=frame, text="Video & Audio", value="Video", variable=option)
download_type_video.pack(pady=12, padx=10)

download_button = customtkinter.CTkButton(master=frame, text="Download", command=validate)
download_button.pack(pady=12, padx=10)

root.mainloop()