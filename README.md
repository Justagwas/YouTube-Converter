# YouTube Downloader/Converter

A user-friendly Python application to convert and download YouTube videos or audio directly from their URL.

Purpose is to allow users to download video/audio off of YouTube with ease.

## Table of Contents

- 📋 [Features](#-features)
- ❓ [How to Use (Installation)](#-how-to-use)
- 📦 [Packaging Instructions](#-packaging-instructions)
- ⚠️ [Warnings](#%EF%B8%8F-warnings)
- 📷 [Preview](#-preview)
- 🔗 [Links & Statistics](#-links--statistics)
- 🛑 [Downloaded My Software and Got a Warning?](#-downloaded-my-software-and-got-a-warning) 🛑
- 🚧 [TODO List](#-todo-list)
- 📜 [License](#-license)
---

## 📋 Features

1. **Video Conversion**  
   Convert YouTube videos to various video formats with ease.
   
2. **Audio Extraction**  
   Extract audio from YouTube videos and download in popular audio formats.  

3. **Simple Interface**  
   Enter the URL, choose the format, and download!  

4. **Fast and Reliable**  
   Quick conversions with the best possible results.  

__DOWNLOAD__ - The download button downloads whatever it is you wanted the program to download.

__TERMINATE__ - The terminate button kills the program, stopping the download if there was one.

📷 [Check out the preview](#-preview)

---

## ❓ How to Use

### Method 1: Downloading the Precompiled Executable (Application) via Installer
1. **Download via the Installer (RECOMMENDED)**  
   Visit the [Latest Release](https://github.com/Justagwas/YouTube-Converter/releases/latest) and download `YouTube_Converter_Setup.exe`,  
    or click the button below ↓.
   
   [![Download YT_CONVERT_Setup.exe](https://img.shields.io/badge/▼%20Download▼-YouTube_Converter_Setup.exe-blue?style=for-the-badge)](https://github.com/Justagwas/YouTube-Converter/releases/latest/download/YouTube_Converter_Setup.exe)

3. **Run the Installer**  
   Simply double-click the downloaded file to install the app.  

4. **Usage**  
  3.1 **Launch the APP**  
     Launch the newly downloaded application.
   
    3.2 **Enter the URL**  
       Paste the YouTube video URL into the input box.  
    
    3.3 **Choose Format**  
       Select your desired format.  
    
    3.4 **Download**  
       Click on the **Download** button to start the process.

Using the installer is essential as it automatically adds the application to the start menu, ensuring convenient access at any time.

---

### Method 2: Run the Python Script
1. **Download**  
   Clone or download the repository as a ZIP file from the latest release:
   
   [![Download Latest Release YouTube_Converter.zip](https://img.shields.io/badge/▼%20Download_Latest_Release%20▼-Source_Code.zip%20-blue?style=for-the-badge)](https://github.com/Justagwas/YouTube-Converter/archive/refs/tags/v1.1.0.zip)

3. **Install Dependencies**  
   Ensure Python is installed on your system. Then, install the required libraries using the following command:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**  
   Execute the Python script using:
   ```bash
   python YouTube_Converter.py
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
   pyinstaller YouTube_Converter.spec
   ```
   
   This will generate the executable in the `dist/` folder, using the configurations from the `.spec` file.

4. **Build Without the `.spec` File** (If you prefer to compile manually), run:  
   ```bash
   pyinstaller --onefile YouTube_Converter.py
   ```
   - `--onefile`: Combines all dependencies into a single executable.  

6. **Locate the Executable**  
   After packaging, the executable (`YouTube_Converter.exe`) will be located in the `dist/` directory.


- **Why** should I build it by using the provided `.spec` file?

- `.spec` is a file that stores all the settings used during development packaging, meaning this is how the executable in releases was built, however, as the user, you are free to do whatever.
   
---

## ⚠️ Warnings

NOTE that all downloaded files from the application (YouTube Video/Audio files) are downloaded to the Downloads folder.

RELEVANT IF YOU USED THE `YouTube_Converter_Setup.exe` TO INSTALL THE PROGRAM.

- **Uninstalling**

You can uninstall the program by navigating to your Windows Settings.
  1. Press Win + I.  
  2. In the Settings search bar, type Programs.  
  3. Within the suggested selections in the search bar, select "Add or remove programs".  
  4. In the new window search YouTube Converter.  
  5. Click the 3-Dots Icon next to the application and uninstall.  
  6. Follow the on-screen pop-up to uninstall the application completely.

If you are unable to find the program within Windows Settings, follow this guide below.
  
  1. Press Win + R.  
  2. In the pop-up type `C:\Program Files` and press enter (DEFAULT INSTALLATION IS `C:\Program Files` UNLESS YOU'VE CHANGED THIS).  
  3. Locate the folder named "YouTube Converter".  
  4. Open the folder.
  5. Within the folder find a file named `unins000.exe`.
  6. Double click that file and follow on screen instructions to uninstall the application.

NOTE (2) that this application stores NO DATA, upon deletion it is completely removed from your system, it is safe to use and downloads ONLY whatever you want it to.

---

## 📷 Preview



---

## 🔗 Links & Statistics

[![Latest Release](https://img.shields.io/badge/🔖%20Latest%20Release-blue?style=for-the-badge)](https://github.com/Justagwas/YouTube-Converter/releases/latest)  
[![Issues](https://img.shields.io/badge/🐛%20Issues-orange?style=for-the-badge)](https://github.com/Justagwas/YouTube-Converter/issues)  
[![Contributors](https://img.shields.io/github/contributors/Justagwas/YouTube-Converter?label=👥%20Contributors&style=for-the-badge)](https://github.com/Justagwas/YouTube-Converter/graphs/contributors)  
[![Download Count](https://img.shields.io/github/downloads/Justagwas/YouTube-Converter/total?label=⬇️%20Total%20Downloads&style=for-the-badge&color=blue)](https://github.com/Justagwas/YouTube-Converter/releases)  
[![Open Issues](https://img.shields.io/github/issues/Justagwas/YouTube-Converter?label=🐛%20Open%20Issues&style=for-the-badge)](https://github.com/Justagwas/YouTube-Converter/issues)  
[![Last Commit](https://img.shields.io/github/last-commit/Justagwas/YouTube-Converter?label=🕒%20Last%20Commit&style=for-the-badge)](https://github.com/Justagwas/YouTube-Converter/commits)  

---

## 🛑 **Downloaded My Software and Got a Warning?**  

Don’t worry! Windows and other operating systems sometimes flag my software simply because it’s not yet widely recognized. Rest assured, **all my software is open source** and completely transparent. You can review the code yourself and decide if you trust it, although it is safe. 

### 🛠 **What You Can Do:**  
1. Double-check if your download is from the (official repository)[https://github.com/Justagwas/YouTube-Converter].
2. If Windows shows a warning, click **More Info** > **Run Anyway** to bypass it.  
3. Refer to the ⚠️ [Warnings](#%EF%B8%8F-warnings) section in this repository for any potential risks. If none are listed, there’s nothing to worry about.  

---

## ❓ **Got Any Other Questions?**  
Check out my [FAQ Page](https://www.justagwas.com/faqs) for more answers and details about my projects, safety, and usage guidelines.  

--- 

## 🚧 TODO List

### Version 2.0.0

- [x] Dropdown Selection for VIDEO/AUDIO Formats.
- [x] UI Spacing Improvement.
- [x] Check for YouTube URL.
- [x] Sanitize YouTube URLs.
- [x] Sanitize File Names.
- [x] Packaged for PR.
- [x] Name Change.
- [x] 1.1.0 -> 2.0.0
- [x] Released.
 
### Version 2.1.0

- [ ] Video Resolution Selection.

---

## 📜 License

[![License](https://img.shields.io/github/license/Justagwas/YouTube-Converter?label=📝%20License&style=for-the-badge)](LICENSE.txt)
