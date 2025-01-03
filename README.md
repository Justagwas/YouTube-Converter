# YouTube Convert (YT CONVERT)

A user-friendly Python application to convert and download YouTube videos or audio directly from their URL.

Purpose is to allow users to download video/audio off of YouTube with ease.

---

## 📋 Features

1. **Video Conversion**  
   Convert YouTube videos to various video formats with ease.
   
2. **Audio Extraction**  
   Extract audio from YouTube videos and download in popular audio formats.  

3. **Simple Interface**  
   Enter the URL, choose the format, and download!  

4. **Fast and Reliable**  
   Quick conversions with high-quality results.  

__DOWNLOAD__ - The download button downloads whatever it is you wanted the program to download.

__TERMINATE__ - The terminate button kills the program, stopping the download if there was one.

### Formats: 

**AUDIO** - Will download the best Audio-ONLY format.  

**VIDEO** - Will download the best Video-ONLY format.  

**VIDE+AUDIO** - Will download the best VIDEO+AUDIO format, **MERGING THEM**.  

**MP4** - Will download the best Video-ONLY format AND Audio-ONLY format and merge them into MP4, **MP4 includes both VIDEO AND AUDIO**.  

**MP3** - Will download the best Audio-ONLY format and convert it to MP3.  

---

## ❓ How to Use

### Method 1: Downloading the Precompiled Executable via Installer
1. **Download via the Installer (RECOMMENDED)**  
   Visit the [Latest Release](https://github.com/Justagwas/YT-CONVERT/releases/latest) and download `YT_CONVERT_Setup.exe`

   [![Download YT_CONVERT_Setup.exe](https://img.shields.io/badge/▼%20Download▼-YT_CONVERT_Setup.exe-blue?style=for-the-badge)](https://github.com/Justagwas/YT-CONVERT/releases/latest/download/YT_CONVERT_Setup.exe)

2. **Run the Installer**  
   Simply double-click the downloaded file to install the app.  

3. **Usage**  
  3.1 **Launch the APP**  
     Launch the newly downloaded application.
   
    3.2 **Enter the URL**  
       Paste the YouTube video URL into the input box.  
    
    3.3 **Choose Format**  
       Select whether to download as video or audio and pick the desired format.  
    
    3.4 **Download**  
       Click on the **Download** button to start the process.

Using the installer is essential as it automatically adds the application to the start menu, ensuring convenient access at any time.

---

### Method 2: Run the Python Script
1. **Download**  
   Clone or download the repository as a ZIP file from the latest release:
   
   [![Download Latest Release YT_CONVERT.zip](https://img.shields.io/badge/▼%20Download_Latest_Release%20▼-Source_Code.zip%20-blue?style=for-the-badge)](https://github.com/Justagwas/YT-CONVERT/archive/refs/tags/v1.0.0.zip)

3. **Install Dependencies**  
   Ensure Python is installed on your system. Then, install the required libraries using the following command:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**  
   Execute the Python script using:
   ```bash
   python YT_CONVERT.py
   ```

---
## 📦 Packaging Instructions

Follow these steps to package/build the Python script into an executable using **PyInstaller**:

1. **Extract ZIP**  
   Extract the downloaded ZIP file into a directory of your choice.

2. **Install PyInstaller**  
   Open a terminal/command prompt and install PyInstaller (if not already installed):
   ```bash
   pip install pyinstaller
   ```

3. **Build Using the `.spec` File**
   (skip this if you want to do it manually)
   
   Use the provided `.spec` file to replicate the exact settings used during development, run:
   ```bash
   pyinstaller YT_CONVERT.spec
   ```
   
   This will generate the executable in the `dist/` folder, using the configurations from the `.spec` file.

4. **Build Without the `.spec` File** (If you prefer to compile manually), run:  
   ```bash
   pyinstaller --onefile YT_CONVERT.py
   ```
   - `--onefile`: Combines all dependencies into a single executable.  

6. **Locate the Executable**  
   After packaging, the executable (`YT_CONVERT.exe`) will be located in the `dist/` directory.


- **Why** should I build it by using the provided `.spec` file?

- `.spec` is a file that stores all the settings used during development packaging, meaning this is how the executable in releases was built, however, as the user, you are free to do whatever.
   
---

## ⚠️ Warnings

RELEVANT IF YOU USED THE `YT_CONVERT_Setup.exe` TO INSTALL THE PROGRAM.

- **Uninstalling**

You can uninstall the program by navigating to your Windows Settings.
  1. Press Win + I.  
  2. In the Settings search bar, type Programs.  
  3. Within the suggested selections in the search bar, select "Add or remove programs".  
  4. In the new window search YT CONVERT.  
  5. Click the 3-Dots Icon next to the application and uninstall.  
  6. Follow the on-screen pop-up to uninstall the application completely.

If you are unable to find the program within Windows Settings, follow this guide below.
  
  1. Press Win + R.  
  2. In the pop-up type `C:\Program Files` and press enter (DEFAULT INSTALLATION IS `C:\Program Files` UNLESS YOU'VE CHANGED THIS).  
  3. Locate the folder named "YT CONVERT".  
  4. Open the folder.
  5. Within the folder find a file named `unins000.exe`.
  6. Double click that file and follow on screen instructions to uninstall the application.

NOTE that all downloaded files from the application (YouTube Video/Audio files) are downloaded to the Downloads folder.

NOTE (2) that this application stores NO DATA, upon deletion it is completely removed from your system, it is safe to use and downloads ONLY whatever you want it to.

---

## 📷 Preview

![image](https://github.com/user-attachments/assets/a20285a7-aff8-433b-a8bb-133d268a6d4b)

---

## 🔗 Links & Statistics

[![Latest Release](https://img.shields.io/badge/🔖%20Latest%20Release-blue?style=for-the-badge)](https://github.com/Justagwas/YT-CONVERT/releases/latest)  
[![Issues](https://img.shields.io/badge/🐛%20Issues-orange?style=for-the-badge)](https://github.com/Justagwas/YT-CONVERT/issues)  
[![Contributors](https://img.shields.io/github/contributors/Justagwas/YT-CONVERT?label=👥%20Contributors&style=for-the-badge)](https://github.com/Justagwas/YT-CONVERT/graphs/contributors)  
[![Download Count](https://img.shields.io/github/downloads/Justagwas/YT-CONVERT/total?label=⬇️%20Total%20Downloads&style=for-the-badge&color=blue)](https://github.com/Justagwas/YT-CONVERT/releases)  
[![Open Issues](https://img.shields.io/github/issues/Justagwas/YT-CONVERT?label=🐛%20Open%20Issues&style=for-the-badge)](https://github.com/Justagwas/YT-CONVERT/issues)  
[![Last Commit](https://img.shields.io/github/last-commit/Justagwas/YT-CONVERT?label=🕒%20Last%20Commit&style=for-the-badge)](https://github.com/Justagwas/YT-CONVERT/commits)  

---

## 📜 License

[![License](https://img.shields.io/github/license/Justagwas/YT-CONVERT?label=📝%20License&style=for-the-badge)](LICENSE.txt)
