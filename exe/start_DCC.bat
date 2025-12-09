:: ***************************************************************
::  Content: initialize maya
:: 
::  2025-10-07
:: 
::  Author: Elena Giuliani
::  email: elenagiuliani94@outlook.it
:: ***************************************************************
echo off

:: PATHS
set "PROJECT_ROOT=%~dp0\..\"
::set "\=%PROJECT_ROOT%\lesson01_batch"
set "MAYA_PIPELINE_PATH=%PROJECT_ROOT%\library\software\maya"
set "IMG_PATH=%PROJECT_ROOT%\library\img"

:: PYTHON
set "PYTHONPATH=%MAYA_PIPELINE_PATH%"

:: VERSION
set "MAYA_VERSION=2022"

:: SPLASHSCREEN
set "XBMLANGPATH=%IMG_PATH%;%XBMLANGPATH%"

:: SHELF
set "MAYA_CUSTOM_SHELF=%MAYA_PIPELINE_PATH%\custom_shelf.py"

:: ADD ESCAPE CHARACTERS \\
set "MAYA_CUSTOM_SHELF_ESCAPED=%MAYA_CUSTOM_SHELF:\=\\%"

:: CALL MAYA
set "MAYA_DIR=C:\Program Files\Autodesk\Maya%MAYA_VERSION%"

::set "MAYA_DISABLE_CIP=1"
::set "MAYA_DISABLE_CER=1"



:: START MAYA
start "" "C:\Program Files\Adobe\Adobe Substance 3D Painter\Adobe Substance 3D Painter.exe" 