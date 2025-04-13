#Checkout my other projects! https://github.com/Justagwas
#The OFFICIAL Repo of this is - https://github.com/Justagwas/YouTube-Converter
import tkinter as tk
from tkinter import messagebox
from yt_dlp import YoutubeDL
import threading
import os
import sys
from urllib.parse import urlparse, parse_qs, urlunparse
import ctypes as ct
import requests
from packaging.version import Version, InvalidVersion
import logging
import time
from pathvalidate import sanitize_filename
import shutil
import zipfile

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Converter v4.1.0")
        self.root.geometry("500x260")
        self.root.configure(bg="gray25")
        self.set_icon()
        self.download_thread = None
        self.ydl = None
        self.root.resizable(False, False) 
        self.check_ffmpeg()
        self.set()
        self.check_for_updates()
        self.create_widgets()

    def set_icon(self):
        script_dir = os.path.dirname(os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__))
        icon_path = os.path.join(script_dir, "icon.ico")

        if os.path.exists(icon_path):
            try:
                self.root.iconbitmap(icon_path)
                return
            except Exception as e:
                logging.error(f"Failed to set application icon: {e}")

        def is_admin():
            try:
                return ct.windll.shell32.IsUserAnAdmin()
            except:
                return False

        def run_as_admin():
            try:
                script = os.path.abspath(sys.argv[0])
                params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
                ct.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)
                sys.exit(0)
            except Exception as e:
                logging.error(f"Failed to relaunch as admin: {e}")
                messagebox.showerror("Error", "Failed to request administrator privileges.")
                return False

        if messagebox.askyesno("Download Icon", "The application's icon is missing. Would you like to download and install it?"):
            if not is_admin():
                if not run_as_admin():
                    return

            try:
                icon_url = "https://github.com/Justagwas/YouTube-Converter/raw/master/YouTube-Converter/icon.ico"
                logging.info(f"Downloading icon from {icon_url} to {icon_path}")
                response = requests.get(icon_url, stream=True)
                with open(icon_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                self.root.iconbitmap(icon_path)
            except Exception as e:
                logging.error(f"Failed to download or set application icon: {e}")
                messagebox.showerror("Error", "Failed to download or set the application's icon.")

    def check_ffmpeg(self):
        ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")
        ffmpeg_installed = self.is_ffmpeg_installed()

        if not ffmpeg_installed and not os.path.exists(ffmpeg_path):
            self.prompt_ffmpeg_download()

    def is_ffmpeg_installed(self):
        try:
            result = os.system("ffmpeg -version >nul 2>&1")
            return result == 0
        except Exception:
            return False

    def prompt_ffmpeg_download(self):
        def on_confirm():
            if checkbox_var.get():
                self.clear_ffmpeg_prompt()
            else:
                messagebox.showerror("Error", "You must check the box to proceed.")

        def on_download_choice():
            for widget in self.root.winfo_children():
                widget.destroy()

            tk.Label(
                self.root,
                text="Choose how to download FFmpeg:",
                bg="gray25",
                fg="gray80",
                wraplength=420,
                font=("Arial", 12, "bold"),
                justify="center"
            ).pack(pady=10)

            tk.Label(
                self.root,
                text="Automatic (Recommended): The application will download and install FFmpeg after you are introduced to the legal disclaimer.\n\n"
                     "Manual: Follow the steps to download and install FFmpeg yourself.",
                bg="gray25",
                fg="gray80",
                wraplength=420,
                justify="left"
            ).pack(pady=10)

            button_frame = tk.Frame(self.root, bg="gray25")
            button_frame.pack(pady=10)

            auto_button = tk.Button(
                button_frame, text="Automatic", command=show_legal_disclaimer, bg="gray80", fg="gray25"
            )
            auto_button.pack(side=tk.LEFT, padx=5)

            manual_button = tk.Button(
                button_frame, text="Manual", command=show_manual_steps, bg="gray80", fg="gray25"
            )
            manual_button.pack(side=tk.LEFT, padx=5)

            self.status_label = tk.Label(self.root, text="", bg="gray25", fg="gray80")
            self.status_label.pack(pady=5)

        def show_legal_disclaimer():
            def is_admin():
                try:
                    return ct.windll.shell32.IsUserAnAdmin()
                except:
                    return False

            def run_as_admin():
                try:
                    script = os.path.abspath(sys.argv[0])
                    params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
                    ct.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)
                    sys.exit(0)
                except Exception as e:
                    logging.error(f"Failed to relaunch as admin: {e}")
                    messagebox.showerror("Error", "Failed to request administrator privileges.")
                    return False

            if not is_admin():
                if messagebox.askyesno(
                    "Admin Permission Required",
                    "This action requires administrator privileges. Would you like to restart the application as an administrator?"
                ):
                    if not run_as_admin():
                        return
                else:
                    return

            for widget in self.root.winfo_children():
                widget.destroy()

            tk.Label(
                self.root,
                text="Legal Disclaimer:",
                bg="gray25",
                fg="gray80",
                font=("Arial", 12, "bold"),
                justify="center"
            ).pack(pady=10)

            tk.Label(
                self.root,
                text="By proceeding, you acknowledge that FFmpeg is a third-party software.\n\n"
                     "The application will download FFmpeg from an official Windows build.\n\n"
                     "FFmpeg is licensed under the GNU Lesser General Public License (LGPL) version 2.1 or later.\n"
                     "For more details, visit:",
                bg="gray25",
                fg="gray80",
                wraplength=420,
                justify="left"
            ).pack(pady=0)
            link = tk.Label(
                self.root,
                text="https://ffmpeg.org/legal.html",
                bg="gray25",
                fg="blue",
                cursor="hand2",
                wraplength=220,
                justify="left",
                anchor="w"
            )
            link.pack(pady=5, padx=38, anchor="w")
            link.bind("<Button-1>", lambda e: os.startfile("https://ffmpeg.org/legal.html"))

            button_frame = tk.Frame(self.root, bg="gray25")
            button_frame.pack(pady=10)

            proceed_button = tk.Button(
                button_frame, text="Proceed", command=on_download, bg="gray80", fg="gray25"
            )
            proceed_button.pack(side=tk.LEFT, padx=5)

            cancel_button = tk.Button(
                button_frame, text="Cancel", command=self.terminate_program, bg="gray80", fg="gray25"
            )
            cancel_button.pack(side=tk.LEFT, padx=5)

            self.status_label = tk.Label(self.root, text="\n\n", bg="gray25", fg="gray80")
            self.status_label.pack(pady=5)

        def show_manual_steps():
            for widget in self.root.winfo_children():
                widget.destroy()

            tk.Label(
                self.root,
                text="Manual Download Steps:",
                bg="gray25",
                fg="gray80",
                font=("Arial", 12, "bold"),
                justify="center"
            ).pack(pady=10)

            tk.Label(
                self.root,
                text="1. Visit the official FFmpeg build page:",
                bg="gray25",
                fg="gray80",
                wraplength=420,
                justify="left"
            ).pack(pady=0, padx=50, anchor="w")

            link = tk.Label(
                self.root,
                text="https://github.com/GyanD/codexffmpeg/releases/latest",
                bg="gray25",
                fg="blue",
                cursor="hand2",
                wraplength=420,
                justify="left",
                anchor="w"
            )
            link.pack(pady=0, padx=50, anchor="w")
            link.bind("<Button-1>", lambda e: os.startfile("https://github.com/GyanD/codexffmpeg/releases/latest"))

            tk.Label(
                self.root,
                text="2. Download the file named 'ffmpeg-x.x.x-essentials_build.zip'.\n"
                     "3. Extract the downloaded ZIP file.\n"
                     "4. Locate the 'ffmpeg.exe' file within the extracted folder and its subfolders.\n"
                     "5. Move the 'ffmpeg.exe' file to the same directory as this application.",
                bg="gray25",
                fg="gray80",
                wraplength=420,
                justify="left"
            ).pack(pady=5)

            tk.Label(
                self.root,
                text="Once you have completed these steps, restart the application.",
                bg="gray25",
                fg="gray80",
                wraplength=420,
                justify="left"
            ).pack(pady=10)

            ok_button = tk.Button(
                self.root, text="OK", command=self.terminate_program, bg="gray80", fg="gray25"
            )
            ok_button.pack(pady=10)

        def on_download():
            def rotate_spinner():
                while self.spinner_running:
                    for frame in ["|", "/", "-", "\\"]:
                        self.status_label.config(text=f"Downloading FFmpeg... {frame}")
                        time.sleep(0.1)

            try:
                self.spinner_running = True
                spinner_thread = threading.Thread(target=rotate_spinner, daemon=True)
                spinner_thread.start()

                download_url = "https://github.com/GyanD/codexffmpeg/releases/download/2025-03-31-git-35c091f4b7/ffmpeg-2025-03-31-git-35c091f4b7-essentials_build.zip"
                script_dir = os.path.dirname(os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__))
                download_path = os.path.join(script_dir, "ffmpeg-git-essentials.zip")
                extract_path = os.path.join(script_dir, "ffmpeg_temp")

                logging.info(f"Downloading FFmpeg from {download_url} to {download_path}")
                response = requests.get(download_url, stream=True)
                with open(download_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)

                self.spinner_running = False
                self.status_label.config(text="Extracting FFmpeg...")
                logging.info(f"Extracting FFmpeg to {extract_path}")
                os.makedirs(extract_path, exist_ok=True)
                with zipfile.ZipFile(download_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)

                bin_folder = next(
                    (os.path.join(root, "ffmpeg.exe") for root, _, files in os.walk(extract_path) if "ffmpeg.exe" in files),
                    None
                )
                if bin_folder:
                    shutil.copy(bin_folder, script_dir)
                    logging.info(f"Copied ffmpeg.exe to {script_dir}")

                os.remove(download_path)
                shutil.rmtree(extract_path)

                self.status_label.config(text="FFmpeg installed successfully!")
                messagebox.showinfo("Success", "FFmpeg has been installed successfully.")
                self.clear_ffmpeg_prompt()
            except Exception as e:
                self.spinner_running = False
                logging.error(f"Error during FFmpeg installation: {e}")
                messagebox.showerror("Error", f"Failed to download and install FFmpeg: {e}")
                self.status_label.config(text="FFmpeg installation failed.")

        for widget in self.root.winfo_children():
            widget.destroy()
        message = (
            "The FFmpeg framework, which is essential for this application to function, is missing from your system.\n\n"
            "Without this dependency, the application will not work.\n\n"
            "Would you like to download and install FFmpeg now?"
        )
        tk.Label(self.root, text=message, bg="gray25", fg="gray80", wraplength=420, justify="left").pack(pady=10)

        button_frame = tk.Frame(self.root, bg="gray25")
        button_frame.pack(pady=10)

        proceed_button = tk.Button(button_frame, text="Yes", command=on_download_choice, bg="gray80", fg="gray25")
        proceed_button.pack(side=tk.LEFT, padx=5)

        confirm_button = tk.Button(button_frame, text="Cancel", command=on_confirm, bg="gray80", fg="gray25")
        confirm_button.pack(side=tk.LEFT, padx=5)

        checkbox_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(
            self.root,
            text="I understand that this application might not work without it and don't want to proceed.",
            variable=checkbox_var,
            bg="gray25",
            fg="gray80",
            wraplength=420,
            justify="left",
        )
        checkbox.pack(pady=5)
        self.status_label = tk.Label(self.root, text="\n\n\n", bg="gray25", fg="gray80")
        self.status_label.pack(pady=5)

    def clear_ffmpeg_prompt(self):
        for widget in self.root.winfo_children():
            widget.destroy()
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
        sanitized_name = sanitize_filename(name)
        return sanitized_name.strip()

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

        quality_choice = self.quality_var.get()
        if quality_choice == "Select Quality":
            messagebox.showerror("Error", "Please select a quality")
            return

        self.download_button.config(state=tk.DISABLED)

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

        info_dict = YoutubeDL().extract_info(url, download=False)
        sanitized_title = self.sanitize_filename(info_dict['title'])
        temp_filename = f"{sanitized_title}_YTC.{format_choice}"
        final_filename = temp_filename.replace("_YTC", "")
        output_path = os.path.join(os.path.expanduser('~/Downloads'), final_filename)

        if os.path.exists(output_path):
            self.status_label.config(text="File is already downloaded!")
            messagebox.showinfo("Info", "File is already downloaded!")
            self.download_button.config(state=tk.NORMAL)
            return

        output_template = os.path.expanduser(f'~/Downloads/{temp_filename}')
        
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
        tempf = f"{sanitized_title}_YTC"
        if format_choice in ['mp3', 'wav']:
            output_template = os.path.expanduser(f'~/Downloads/{tempf}')
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': output_template,
                'progress_hooks': [self.ydl_hook],
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': format_choice,
                    'preferredquality': '192',
                }],
                'noplaylist': True,
                'abort_on_unavailable_fragments': True,
                'force_overwrites': True
            }
        else:
            if format_choice == 'mov':
                output_template = os.path.expanduser(f'~/Downloads/{tempf}')
            else: output_template = os.path.expanduser(f'~/Downloads/{temp_filename}')
            ydl_opts = {
                'format': quality_format.get(quality_choice, 'bestvideo+bestaudio/best'),
                'outtmpl': output_template,
                'progress_hooks': [self.ydl_hook],
                'postprocessors': [{
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
                ydl.download([url])
                self.status_label.config(text="Download completed successfully!")
            except Exception as e:
                if 'abort' in str(e).lower():
                    self.status_label.config(text="Download aborted!")
                else:
                    self.status_label.config(text="Download failed!")
                    messagebox.showerror("Error", str(e))
            finally:
                time.sleep(0.5)
                if os.path.exists(os.path.join(os.path.expanduser('~/Downloads'), temp_filename)):
                    os.rename(
                        os.path.join(os.path.expanduser('~/Downloads'), temp_filename),
                        output_path
                    )
                self.download_button.config(state=tk.NORMAL)

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
                current_version = "v4.1.0"
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