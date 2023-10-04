import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

root =customtkinter.CTk()
root.geometry("600x400")

frame = customtkinter.CTkFrame(master=root)
frame.place()

link_label = customtkinter.CTkLabel(master=frame, text="Youtube Link")
link_label.place()

link_input = customtkinter.CTkEntry(master=frame, placeholder_text="Link here", width=400)
link_input.place()

download_type_label = customtkinter.CTkLabel(master=frame, text="Select download type")
download_type_label.place()

download_type_audio = customtkinter.CTkRadioButton(master=frame, text="Audio only", value=1)
download_type_audio.place()

download_type_video = customtkinter.CTkRadioButton(master=frame, text="Video & Audio", value=2)
download_type_video.place()

download_button = customtkinter.CTkButton(master=frame, text="Download")
download_button.place()
root.mainloop()