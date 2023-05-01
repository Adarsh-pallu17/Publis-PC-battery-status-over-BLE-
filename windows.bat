@echo off

:: Check if Python 3 is installed
where python >nul 2>&1
if %errorlevel% equ 0 (
    echo Python 3 is already installed.
) else (
    echo Python 3 is not installed. Installing...
    choco install python --version=3.9.4 -y
)

:: Install bluepy library
echo Installing bluepy library...
pip install bluepy

:: Install psutil library
echo Installing psutil library...
pip install psutil

echo All libraries installed successfully!
