pip install pytube
pip install youtube_dl


from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox, filedialog
from pytube import YouTube
import youtube_dl

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progressbar['value'] = + percentage_of_completion
    media_tab.update()
    print(progressbar['value'])

def Browse():
    download_Directory = filedialog.askdirectory(
        initialdir="~/", title="Save as")
    download_Path.set(download_Directory)

def fetchSample():
    url = YouTube(str(get_url_to_video.get()))
    resvar = str(var.get())
    strresvar = resvar+"p"
    video = url.streams.filter(res=strresvar).first()
    sizeres = url.streams.get_highest_resolution()
    print(f"เรียก \"{video.title}\"..")
    messagebox.showinfo("ตัวอย่าง",
                        "วิดีโอของที่อยู่ที่คุณป้อนคือ\n"
                        + video.title + "\nโดย" +url.author)

def Downloader():
    url = YouTube(str(get_url_to_video.get()))
    resvar = str(var.get())
    strresvar = resvar+"p"
    video = url.streams.filter(res=strresvar).first()
    download_Folder = download_Path.get()
    url.register_on_progress_callback(on_progress)
    print(f"Fetching \"{video.title}\"..")
    print(f"Fetching successful\n")
    print(f"กำลังดาวน์โหลด \"{video.title}\"..")
    video.download(download_Folder)
    messagebox.showinfo("สถานะ",
                    "ดาวน์โหลดวิด๊โอสำเร็จและเก็บไว้ที่\n"
                    + download_Folder)
def mp3Sample():
    video_url = (str(get_url_to_mp3.get()))
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    messagebox.showinfo("ตัวอย่าง",
                        "ไฟล์เสียงของที่อยู่ที่คุณป้อนคือ\n"
                        + filename)

def mp3Dowloader():
    video_url = (str(get_url_to_mp3.get()))
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    messagebox.showinfo("success",
                        "ดาวน์โหลดเสียงให้คุณแล้ว\n"
                        + filename)

    print("Download complete... {}".format(filename))

  
window = Tk()
window.title("YouLoad : YouTube videos dowloader")
window.geometry('400x250')

tabs_control = Notebook(window)
media_tab = Frame(tabs_control)
music_tab = Frame(tabs_control)
seter_tab = Frame(tabs_control)
tabs_control.add(media_tab, text="MP4")
tabs_control.add(music_tab, text="MP3")
tabs_control.add(seter_tab, text='Setting')
tabs_control.pack(expand=1, fill="both")

#MP4 TAB  ----------------------------- MP4 TAB#
app_name_label = Label(media_tab, font='calibri 30 bold',
                       text='MP4 : with URL')
app_name_label.pack(anchor='center')
pls_link_label = Label(media_tab, background='#ff0000', font='calibri 15 bold',
                       text='Pease URL from YouTube.com in this input')
pls_link_label.pack(anchor='center')
get_url_to_video = Entry(media_tab, font='calibri 15 bold', width=30)
get_url_to_video.pack(anchor='center')
put_url_label = Label(media_tab, font='calibri 10 bold',
                      text="After put URL,You can check detail of url with Check button")
put_url_label.pack(anchor='s')
progressbar = Progressbar(media_tab, mode="determinate", length=200)
progressbar.pack(anchor='center')
check_url_button = Button(media_tab, text="Check",command=fetchSample)
check_url_button.pack(anchor='s')
set_url_button = Button(media_tab, text="Download",command=Downloader)
set_url_button.pack(anchor='s')
#MP4 TAB  ----------------------------- MP4 TAB#

#MP3 TAB  ----------------------------- MP3 TAB#
app_name_label_mp3 = Label(music_tab, font='calibri 30 bold',
                           text='MP3 : with URL')
app_name_label_mp3.pack(anchor='center')
pls_link_label_mp3 = Label(music_tab, background='#ff0000', font='calibri 15 bold',
                           text='Pease URL from YouTube.com in this input')
pls_link_label_mp3.pack(anchor='center')
get_url_to_mp3 = Entry(music_tab, font='calibri 15 bold', width=30)
get_url_to_mp3.pack(anchor='center')
put_url_label_mp3 = Label(music_tab, font='calibri 10 bold',
                          text="After put URL,You can check detail of url with Check button")
put_url_label_mp3.pack(anchor='s')
progressbar_mp3 = Progressbar(music_tab, mode="determinate", length=200)
progressbar_mp3.pack(anchor='center')
check_url_button_mp3 = Button(music_tab, text="Check",command=mp3Sample)
check_url_button_mp3.pack(anchor='s')
set_url_button_mp3 = Button(music_tab, text="Download",command=mp3Dowloader)
set_url_button_mp3.pack(anchor='s')
#MP3 TAB  ----------------------------- MP3 TAB#

#SET TAB  ----------------------------- SET TAB#
setting_label = Label(seter_tab, font='calibri 30 bold',
                      text='SETTINGS')
setting_label.pack(anchor='center')
separator = Separator(seter_tab, orient='horizontal')
separator.pack(fill='x')
download_Path = StringVar()
download_Path.set("~/")
path_label = Label(seter_tab, font='calibri 10 bold',
                          text="Location for save file")
path_label.pack(anchor='s')
pathbrow = Entry(seter_tab, textvariable=download_Path, font=(
    'courier', 15, 'bold')).pack(anchor='center')
pathbrow_btn = Button(seter_tab, text="path",command=Browse)
pathbrow_btn.pack(anchor='s',pady=5)

separator_two = Separator(seter_tab, orient='horizontal')
separator_two.pack(fill='x')

reso_label = Label(seter_tab, font='calibri 10 bold',
                          text="Select resolutions of videos")
reso_label.pack(anchor='s')
var = IntVar()
var.set(720)
R1 = Radiobutton(seter_tab, text="144p", variable=var, value=144)
R1.pack(side=LEFT)
R2 = Radiobutton(seter_tab, text="480p", variable=var, value=480)
R2.pack(side=LEFT)
R3 = Radiobutton(seter_tab, text="720p", variable=var, value=720)
R3.pack(side=LEFT)
R4 = Radiobutton(seter_tab, text="1080p", variable=var, value=1080)
R4.pack(side=LEFT)

#SET TAB  ----------------------------- SET TAB#

window.mainloop()
