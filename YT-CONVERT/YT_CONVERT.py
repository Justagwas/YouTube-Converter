#Checkout my other projects! https://github.com/Justagwas
#The OFFICIAL Repo of this is - https://github.com/Justagwas/YT-CONVERT
import tkinter as tk
from tkinter import messagebox
from yt_dlp import YoutubeDL
import threading
import os
import sys

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Converter")
        self.root.geometry("500x220")
        self.root.configure(bg="gray25")
        self.download_thread = None
        self.ydl = None
        self.root.resizable(False, False) 
        self.create_widgets()

    def create_widgets(self):
        self.url_label = tk.Label(self.root, text="YouTube URL:", bg="gray25", fg="gray80")
        self.url_label.pack(pady=5)

        self.url_frame = tk.Frame(self.root, bg="gray25")
        self.url_frame.pack(pady=5)

        self.url_entry = tk.Entry(self.url_frame, width=40)
        self.url_entry.pack(side=tk.LEFT, padx=5)

        self.paste_button = tk.Button(
            self.url_frame, text="PASTE", command=self.paste_url, bg="gray80", fg="gray25"
        )
        self.paste_button.pack(side=tk.LEFT, padx=5)

        self.format_var = tk.StringVar(value="VIDEO+AUDIO")

        self.format_frame = tk.Frame(self.root, bg="gray25")
        self.format_frame.pack(pady=5)

        self.mp3_button = tk.Radiobutton(
            self.format_frame, text="AUDIO", variable=self.format_var, value="AUDIO",
            bg="gray25", fg="gray80", selectcolor="gray15", indicatoron=0, width=8, relief=tk.RAISED
        )
        self.mp3_button.pack(side=tk.LEFT, padx=10)

        self.mp4_button = tk.Radiobutton(
            self.format_frame, text="VIDEO", variable=self.format_var, value="VIDEO",
            bg="gray25", fg="gray80", selectcolor="gray15", indicatoron=0, width=10, relief=tk.RAISED
        )
        self.mp4_button.pack(side=tk.LEFT, padx=10)

        self.video_audio_button = tk.Radiobutton(
            self.format_frame, text="VIDEO+AUDIO", variable=self.format_var, value="VIDEO+AUDIO",
            bg="gray25", fg="gray80", selectcolor="gray15", indicatoron=0, width=14, relief=tk.RAISED
        )
        self.video_audio_button.pack(side=tk.LEFT, padx=10)

        self.best_mp4_button = tk.Radiobutton(
            self.format_frame, text="MP4", variable=self.format_var, value="MP4",
            bg="gray25", fg="gray80", selectcolor="gray15", indicatoron=0, width=10, relief=tk.RAISED
        )
        self.best_mp4_button.pack(side=tk.LEFT, padx=10)

        self.best_mp3_button = tk.Radiobutton(
            self.format_frame, text="MP3", variable=self.format_var, value="MP3",
            bg="gray25", fg="gray80", selectcolor="gray15", indicatoron=0, width=8, relief=tk.RAISED
        )
        self.best_mp3_button.pack(side=tk.LEFT, padx=10)

        self.download_button = tk.Button(self.root, text="DOWNLOAD", command=self.start_download, bg="gray80", fg="gray25")
        self.download_button.pack(pady=10)

        self.abort_button = tk.Button(self.root, text="TERMINATE", command=self.abort_download, bg="gray80", fg="gray25")
        self.abort_button.pack(pady=5)

        self.status_label = tk.Label(self.root, text="", bg="gray25", fg="gray80")
        self.status_label.pack(pady=5)

    def paste_url(self):
        try:
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, self.root.clipboard_get())
        except tk.TclError:
            messagebox.showerror("Error", "No URL found in clipboard")

    def start_download(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return

        format_choice = self.format_var.get()
        self.download_thread = threading.Thread(target=self.download_video, args=(url, format_choice))
        self.download_thread.start()

    def abort_download(self):
        if self.ydl:
            self.ydl.download = False
            self.status_label.config(text="Download aborted!")
        self.terminate_program()

    def terminate_program(self):
        self.root.destroy()
        sys.exit()

    def download_video(self, url, format_choice):
        self.status_label.config(text="Starting download...")

        suffix = f"_{format_choice}" if format_choice in ['AUDIO', 'VIDEO'] else ""
        ydl_opts = {
            'format': 'bestaudio' if format_choice == 'AUDIO' else
                      'bestvideo' if format_choice == 'VIDEO' else
                      'bestvideo+bestaudio' if format_choice == 'VIDEO+AUDIO' else
                      'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' if format_choice == 'MP4' else
                      'bestaudio/best',
            'outtmpl': os.path.expanduser(f'~/Downloads/%(title)s{suffix}.%(ext)s'),
            'progress_hooks': [self.ydl_hook],
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }] if format_choice == 'MP3' else [],
            'noplaylist': True,
            'abort_on_unavailable_fragments': True
        }

        with YoutubeDL(ydl_opts) as ydl:
            self.ydl = ydl
            try:
                ydl.download([url])
                self.status_label.config(text="Download completed successfully!")
            except Exception as e:
                if 'abort' in str(e).lower():
                    self.status_label.config(text="Download aborted!")
                else:
                    self.status_label.config(text="Download failed!")
                    messagebox.showerror("Error", str(e))

    def ydl_hook(self, d):
        if d['status'] == 'downloading':
            try:
                percent_str = d.get('_percent_str', '').strip()
                percent = percent_str.split('%')[0].strip()[-4:]
                self.status_label.config(text=f"{percent}% Downloaded")
            except KeyError:
                self.status_label.config(text="Downloading...")

        elif d['status'] == 'finished':
            self.status_label.config(text="Download finished! Converting...")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()