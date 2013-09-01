@setlocal
@echo off

"%PYTHON%" --version >nul 2>nul
if %ERRORLEVEL% equ 0 goto run

set PYTHON=%~dp0\..\python
"%PYTHON%" --version >nul 2>nul
if %ERRORLEVEL% equ 0 goto run

set PYTHON=python2.7
"%PYTHON%" --version >nul 2>nul
if %ERRORLEVEL% equ 0 goto run

set PYTHON=python2.6
"%PYTHON%" --version >nul 2>nul
if %ERRORLEVEL% equ 0 goto run

set PYTHON=python2.5
"%PYTHON%" --version >nul 2>nul
if %ERRORLEVEL% equ 0 goto run

set PYTHON=python
"%PYTHON%" --version >nul 2>nul
if %ERRORLEVEL% equ 0 goto run

:run
%PYTHON% %~dp0\rfGengouCmd.py %*
@endlocal
