from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageGrab, ImageFont, ImageDraw


def image_upload():
    global image_on_canvas, image_path, image_name

    file_types = [('Select Image File', '*.*'),('PNG Files', '*.png'),('JPG Files', '*.jpg'),('JPEG Files', '*.jpeg')]
    image_path = filedialog.askopenfilename(filetypes=file_types)

    image_name = image_path.split('/')[-1]
    image_name = image_name[0:-4]
    selected_img = Image.open(image_path)
    try:
        if selected_img:
            width, height = selected_img.size
            canvas.config(width=width,height=height)
            canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
            image_on_canvas = ImageTk.PhotoImage(selected_img)
            canvas.create_image(0,0, image=image_on_canvas, anchor="nw")
    except FileNotFoundError:
        print("Please select the file")


def add_watermark():
    global watermarked_image
    image = Image.open(image_path).convert("RGBA")
    text_image = Image.new('RGBA', image.size, (255,255,255,0))

    watermark_text = watermark_entry.get()
    font = ImageFont.truetype("arial.ttf", 45)

    draw_obj = ImageDraw.Draw(text_image)

    width, height = image.size
    text_width, text_height = draw_obj.textsize(watermark_text,font)

    if menu.get() =="Top Left":
        x = 20
        y= 20
    elif menu.get() =='Top Right':
        x= width-300
        y= 20
    elif menu.get()=='Center':
        x = width / 2 - text_width / 2
        y= height / 2 - text_height / 2

    elif menu.get() =='Bottom Left':
        x = 50
        y = height - 50

    elif menu.get() == 'Bottom Right':
        x= width - 300
        y= height -50
    else:
        x= width /2 - text_width / 2
        y= height-text_height -300

    draw_obj.text((x,y), watermark_text,fill=(255,255,255, 120), font=font)
    watermarked = Image.alpha_composite(image, text_image)

    watermarked_image = ImageTk.PhotoImage(watermarked)
    canvas.create_image(0, 0, image=watermarked_image, anchor="nw")



def save_image():
    x= window.winfo_rootx() + canvas.winfo_x()
    y =window.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    image_new_name = f"{image_name}+watermarked.jpg"
    file_location = filedialog.askdirectory(title="Save new images to...")

    grab_image = ImageGrab.grab(bbox=(x, y, x1, y1))
    grab_image.save(f"{file_location}/{image_new_name}")

window = Tk()
window.title("Watermark Application")
window.config(bg="grey")

screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

window.geometry(f'{screen_width}x{screen_height}')
window.resizable(False, False)



canvas = Canvas(window, height=screen_height - 100, width=screen_width, background="blanched almond", highlightthickness=0)
canvas.grid(row=0, column=0)

select_img = Button(window, text="📂",command=image_upload,bg='yellow green', font=('Arial',15))
select_img.place(x=1100, y=680)

save_img = Button(window, text="💾",command=save_image,bg='light green', font=('Arial',15))
save_img.place(x=1150, y=680)

position = ["Top Left", "Top Right","Center","Bottom Left","Bottom Right"]
menu= StringVar(window)
menu.set("Select Text Position")


#Create a dropdown Menu

text_position = OptionMenu(window, menu, *position)
text_position.place(x=550,y=683)
text_position.config(font=('Arial',14), bg='tomato')



watermark_text = Button(window, text='Add', font=('Arial',15,'bold'), bg='SlateBlue4', command=add_watermark, width=10)
watermark_text.place(x=395, y=680)

watermark_entry = Entry(width=20, font=('Arial',15), border=2, borderwidth=2)
watermark_entry.place(x=150, y=688)




window.mainloop()