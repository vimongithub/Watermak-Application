from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageGrab
from tkinter.filedialog import askopenfile


def image_upload():
    global image_on_canvas

    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png'),('JPEG Files', '*.jpeg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    selected_img = Image.open(filename)
    selected_img_size = selected_img.size
    x, y = selected_img_size
    canvas.config(width=x, height=y)
    image_resized = selected_img.resize((500, 600))
    image_on_canvas = ImageTk.PhotoImage(image_resized)
    canvas.create_image(250, 300, image=image_on_canvas)

def save_image():
    x= window.winfo_rootx() + canvas.winfo_x()
    y =window.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    image_new_name = "abc_watermark.jpg"
    file_location = filedialog.askdirectory(title="Save new images to...")

    grab_image = ImageGrab.grab(bbox=(x, y, x1, y1))
    grab_image.save(f"{file_location}/{image_new_name}")



window = Tk()
window.title("Watermark Application")
window.config(bg="grey")

win_width = 500
win_height = 700

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width / 2 - win_width / 2)
center_y = int(screen_height/2 - win_height / 2)

window.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')
window.resizable(False, False)



canvas = Canvas(window, height=600, width=500, background="blanched almond", highlightthickness=0)
canvas.grid(row=0, column=0)

select_img = Button(window, text="📂",command=image_upload,bg='yellow green', font=('Arial',15))
select_img.place(x=200, y=610)

save_img = Button(window, text="💾",command=save_image,bg='light green', font=('Arial',15))
save_img.place(x=250, y=610)
#
# watermark_text = Label(text='Watermark Text', font=('Arial',10,'bold'))
# watermark_text.place(x=65, y=470)
#
# watermark_entry = Entry(width=35)
# watermark_entry.place(x=200, y=470)




window.mainloop()