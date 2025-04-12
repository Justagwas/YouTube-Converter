#Checkout my other projects! https://github.com/Justagwas
#The OFFICIAL Repo of this is - https://github.com/Justagwas/YouTube-Converter
import tkinter as tk
from tkinter import messagebox
from yt_dlp import YoutubeDL
import threading
import os
import sys
import re
from urllib.parse import urlparse, parse_qs, urlunparse
import ctypes as ct
import requests
from packaging.version import Version, InvalidVersion
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Converter v4.0.0")
        self.root.geometry("500x260")
        self.root.configure(bg="gray25")
        self.download_thread = None
        self.ydl = None
        self.root.resizable(False, False) 
        self.set()
        self.check_for_updates()
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

        self.format_var = tk.StringVar(value="Select Format")
        self.quality_var = tk.StringVar(value="Select Quality")

        self.format_frame = tk.Frame(self.root, bg="gray25")
        self.format_frame.pack(pady=5)

        self.format_options = [
            "mp4 (Video&Audio)", "mov (Video&Audio)",
            "mp3 (Audio)", "wav (Audio)"
        ]
        self.quality_options = [
            "Select Quality", "144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p (4k)", "MAX"
        ]

        self.format_dropdown = tk.OptionMenu(self.format_frame, self.format_var, *self.format_options)
        self.format_dropdown.config(bg="gray25", fg="gray80", width=20)
        self.format_dropdown.pack(side=tk.LEFT, padx=10)

        self.quality_dropdown = tk.OptionMenu(self.format_frame, self.quality_var, *self.quality_options)
        self.quality_dropdown.config(bg="gray25", fg="gray80", width=20)
        self.quality_dropdown.pack(side=tk.LEFT, padx=10)

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

    def sanitize_filename(self, name):
        return re.sub(r'[<>:"/\\|?*]', '', name)

    def sanitize_url(self, url):
        parsed_url = urlparse(url)
        if parsed_url.netloc not in ["www.youtube.com", "youtube.com", "youtu.be"]:
            return None
        query = parse_qs(parsed_url.query)
        clean_query = {k: query[k] for k in query if k in ["v", "list"]}
        sanitized_url = urlunparse(parsed_url._replace(query="&".join(f"{k}={v[0]}" for k, v in clean_query.items())))
        return sanitized_url

    def start_download(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return

        sanitized_url = self.sanitize_url(url)
        if not sanitized_url:
            messagebox.showerror("Error", "Please enter a valid YouTube URL")
            return

        format_choice = self.format_var.get().split()[0]
        if format_choice == "Select":
            messagebox.showerror("Error", "Please select a format")
            return

        if format_choice == "mov":
            response = messagebox.askyesno("MOV Format Selected", "MOV format converts MP4 files. The MP4 file (IF EXISTS) will be deleted after conversion. Do you want to continue?")
            if not response:
                return

        quality_choice = self.quality_var.get()
        if quality_choice == "Select Quality":
            messagebox.showerror("Error", "Please select a quality")
            return

        self.download_thread = threading.Thread(target=self.download_video, args=(sanitized_url, format_choice, quality_choice))
        self.download_thread.start()

    def abort_download(self):
        if self.ydl:
            self.ydl.download = False
            self.status_label.config(text="Download aborted!")
        self.terminate_program()

    def terminate_program(self):
        self.root.destroy()
        sys.exit()

    def download_video(self, url, format_choice, quality_choice):
        self.status_label.config(text="Starting download...")
        output_template = os.path.expanduser(f'~/Downloads/%(title)s.%(ext)s')
        existing_files = [f for f in os.listdir(os.path.expanduser('~/Downloads')) if os.path.isfile(os.path.join(os.path.expanduser('~/Downloads'), f))]

        quality_format = {
            "144p": "worstvideo[height<=144]+bestaudio/best[height<=144]",
            "240p": "worstvideo[height<=240]+bestaudio/best[height<=240]",
            "360p": "worstvideo[height<=360]+bestaudio/best[height<=360]",
            "480p": "worstvideo[height<=480]+bestaudio/best[height<=480]",
            "720p": "bestvideo[height<=720]+bestaudio/best[height<=720]",
            "1080p": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
            "1440p": "bestvideo[height<=1440]+bestaudio/best[height<=1440]",
            "2160p (4k)": "bestvideo[height<=2160]+bestaudio/best[height<=2160]",
            "MAX": "bestvideo+bestaudio/best"
        }

        ydl_opts = {
            'format': quality_format.get(quality_choice, 'bestvideo+bestaudio/best'),
            'outtmpl': output_template,
            'progress_hooks': [self.ydl_hook],
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': format_choice,
                'preferredquality': '192',
            }] if format_choice in ['mp3', 'wav'] else [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mov'
            }] if format_choice == 'mov' else [],
            'noplaylist': True,
            'abort_on_unavailable_fragments': True,
            'force_overwrites': True
        }
        with YoutubeDL(ydl_opts) as ydl:
            self.ydl = ydl
            try:
                info_dict = ydl.extract_info(url, download=False)
                sanitized_title = self.sanitize_filename(info_dict['title'])
                if any(f.startswith(sanitized_title) and f.endswith(format_choice) for f in existing_files):
                    self.status_label.config(text="File already exists, using existing file...")
                else:
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

    def set(self):
        self.root.update()
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ct.windll.user32.GetParent
        hwnd = get_parent(self.root.winfo_id())
        rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
        value = 2
        value = ct.c_int(value)
        set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))

    def check_for_updates(self):
        def update_check():
            try:
                current_version = "v4.0.0"
                releases_url = "https://api.github.com/repos/Justagwas/YouTube-Converter/releases/latest"
                response = requests.get(releases_url, timeout=10)
                if response.status_code == 200:
                    latest_release = response.json()
                    latest_version = latest_release.get("tag_name", "")
                    try:
                        if Version(latest_version) > Version(current_version):
                            download_url = "https://github.com/Justagwas/YouTube-Converter/releases/latest/download/YouTube_Converter_Setup.exe"
                            prompt_message = (
                                f"A newer version - {latest_version} is available!\n"
                                f"Would you like to download it now?"
                            )
                            if messagebox.askyesno("Update Available", prompt_message):
                                os.startfile(download_url)
                    except InvalidVersion:
                        logging.error(f"Invalid version format: {latest_version}")
                else:
                    logging.error(f"Failed to fetch release info: HTTP {response.status_code}")
            except requests.RequestException as e:
                logging.error(f"Network error during update check: {e}")
                messagebox.showerror("Update Check Failed", "Unable to check for updates. Please try again later.")

        threading.Thread(target=update_check, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()