:: ***************************************************************
::  Content: initialize DCC
:: 
::  2025-10-07
:: 
:: license  : MIT
::  Author: Elena Giuliani
::  email: elenagiuliani94@outlook.it
:: ***************************************************************
echo off

:: PATHS
set "PROJECT_ROOT=%~dp0\..\"

:: MAYA *********************************************************
set "MAYA_PIPELINE_PATH=%PROJECT_ROOT%\library\software\maya"
set "IMG_PATH=%PROJECT_ROOT%\library\img"

:: PYTHON
set "PYTHONPATH=%MAYA_PIPELINE_PATH%;%PYTHONPATH%"

:: VERSION
set "MAYA_VERSION=2022"

:: SPLASHSCREEN
set "XBMLANGPATH=%IMG_PATH%;%XBMLANGPATH%"

:: SHELF
set "LOAD_CUSTOM_SHELF=1"
echo "load custom shelf:  %LOAD_CUSTOM_SHELF%"

:: CALL MAYA
set "MAYA_DIR=C:\Program Files\Autodesk\Maya%MAYA_VERSION%"
:: ***************************************************************

start "" "%MAYA_DIR%\bin\maya.exe" -file "F:\3D_Projects\5_PixelsAndCrafts\Environment\E_25_001__Brandon_room\files\Architectural\modeling\Brandon_architectural_model_project\scenes\Brandon_architectural_model_v001.ma"
