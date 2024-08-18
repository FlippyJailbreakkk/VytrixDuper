@echo off
echo Installing packages...

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python first.
    exit /b 1
)

:: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: List of packages to install
set packages=customtkinter numpy pandas requests matplotlib

:: Install each package
for %%p in (%packages%) do (
    echo Installing %%p...
    python -m pip install %%p
)

echo Installation complete!
echo You can successfully run the duper.
pause
