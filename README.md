**What is Mandelbrot Set Viewer?**
This Python viewer is designed for a highly customizable open-source experience of fractals. It allows for custom fractals, Julia sets, large zooming, burning ships, and near-infinite resolution!
**How can I set it up?**
First, make sure you have Python 3.12 installed. You can check which version of Python you have using this command:

    python -version
   or if you know you have Python 3 you can also use:
   

    python3 -version
   If you don't have Python 3.12 installed, you can either download it from [python.org downloads](https://www.python.org/downloads/) or you can use the command line:
   **Windows**
   1. **Download the Python Installer**  
Download the installer using a tool like **`curl`** or **`wget`**. Open **Command Prompt** or **PowerShell**:

    curl -O https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe
2. **Install Python Silently**  
Run the installer with the **silent installation** flag:

		python-3.12.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
-   `InstallAllUsers=1`: Installs Python system-wide.
-   `PrependPath=1`: Adds Python to the system PATH automatically.
3. **Verify Installation**  
After installation, check if Python 3.12 is installed correctly:
`python --version`
or
`python3 --version`
If Python isn't recognized, restart your terminal.
    

----------

## **On macOS**

1.  **Install Homebrew (if not already installed)**  
    Open Terminal and run:
    `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    
2.   **Install Python 3.12**  
    Use Homebrew to install Python 3.12:
    `brew install python@3.12
`
3. **Verify Installation**  
Check the Python version:
`python3.12 --version
`
## **On Linux (Ubuntu/Debian)**

1.  **Update Package Lists**  
    Update your system's package manager:
    
    `sudo apt update && sudo apt upgrade` 
    
2.  **Install Dependencies**  
    Install tools required to build Python:
    
    `sudo apt install -y wget build-essential libssl-dev zlib1g-dev \
    libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev \
    libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev` 
    
3.  **Download Python Source Code**  
    Use `wget` to download Python 3.12:
    
    `wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tgz` 
    
4.  **Extract and Install**  
    Extract the source code and compile it:
    
    `tar -xf Python-3.12.0.tgz
    cd Python-3.12.0
    ./configure --enable-optimizations
    make -j $(nproc)
    sudo make altinstall` 
    
    -   `make -j $(nproc)` builds faster by using all CPU cores.
    -   `make altinstall` prevents overwriting the default `python3` command.
5.  **Verify Installation**  
    Check the version:
    
    `python3.12 --version` 
    

----------

### Notes:

-   **Windows**: You need to use the installer from the Python website.
-   **macOS/Linux**: Homebrew or source compilation are reliable methods.

**You will have to do this even if you installed Python 3.12 from the website**

 After installing Python, create a Python virtual environment by running this command in the directory you want to create the environment in:
 `python3 -m venv myenv`
 Replace `myenv` with your desired environment name.


 Next, you need to activate the environment.
 #### On Windows:

`myenv\Scripts\activate` 

#### On macOS/Linux:

`source myenv/bin/activate` 

Once activated, your command prompt will show the environment name:

`(myenv) C:\path\to\local\repo>`

**Installing Dependencies**

After all of this, you will need to cd into where the requirements.txt is, for example: `C:\repos\Mandelbrot Set\Mandelbrot Set`

To install the dependencies, run this command:
`pip install -r requirements.txt`

To confirm that the required packages were installed, you can list the installed packages:
`pip freeze`

**Running the viewer**

To run the viewer, use this command:
`python Mandelbrot_set.py
`

Or if you have access to a GUI-based file explorer you can just double-click on the file.

**Extra Information Outside of Installation**
1. Custom formulas do not currently work. They do something, just not what they are supposed to do. Please fix it if you can. It currently is not at the top of my priorities.

2. This was made almost entirely using matplotlib

3. Julia Sets also are a little broken. Same as the custom formulas, I do not currently have the time to fix it. Please do if you can.
