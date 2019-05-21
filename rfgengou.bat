@setlocal enabledelayedexpansion
@echo off

set PYTHON_CHECK="import sys;exit(not((sys.version_info[0]==3 and sys.version_info[1]>=3) or (sys.version_info[0]==2 and sys.version_info[1]>=3)))"

if defined PYTHON (
    %PYTHON% -c %PYTHON_CHECK% >nul 2>nul
    if %ERRORLEVEL% equ 0 goto run
)

for %%V in ("" 3 3.8 3.7 3.6 3.5 3.4 3.3 2 2.7 2.6 2.5 2.4 2.3) do (
    set "PYTHON=python%%V"
    !PYTHON! -c %PYTHON_CHECK% >nul 2>nul
    if !ERRORLEVEL! equ 0 goto run
)

for %%V in (38 38-32 37 37-32 36 36-32 35 35-32 34 33 27 26 25 24 23) do (
for %%P in ("%USERPROFILE%\AppData\Local\Programs\Python" "%ProgramFiles%" "%ProgramFiles(x86)%" "%SystemDrive%") do (
    set "PYTHON=%%P\Python%%V\python"
    !PYTHON! -c %PYTHON_CHECK% >nul 2>nul
    if !ERRORLEVEL! equ 0 goto run
)
)

echo python not found
echo please install python 3.3 (or later) or 2.3 (or later)
exit /b 9009

:run
%PYTHON% %~dp0\rfGengouCmd.py %*
@endlocal
