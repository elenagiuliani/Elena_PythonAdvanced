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
set "PROJECT_ROOT=%~dp0"
set "PIPELINE_PATH=%PROJECT_ROOT%\..\lib\apps\arAsset.py"

:: VERSION
::set "MAYA_VERSION=2022"

:: PYTHON
set "PYTHONPATH=%PIPELINE_PATH%"

:: ICONS PATH
::set "ICONS_PATH=%PIPELINE_PATH%\icons"


:: SPLASHSCREEN
::set "XBMLANGPATH=%ICONS_PATH%;%XBMLANGPATH%"


:: SHELF
::set "CUSTOM_SHELF=%PIPELINE_PATH%\shelf\create_shelf.py"

:: ADD ESCAPE CHARACTERS \\
::set "CUSTOM_SHELF_ESCAPED=%CUSTOM_SHELF:\=\\%"

:: CALL MAYA
::set "MAYA_DIR=C:\Program Files\Autodesk\Maya%MAYA_VERSION%"
::set "PATH=%MAYA_DIR%\bin;%PATH%"

:: START MAYA
::start "" "%MAYA_DIR%\bin\maya.exe" -command "python(\"exec(open(r'%CUSTOM_SHELF_ESCAPED%').read())\")"

python "%PIPELINE_PATH%"



::echo Check custom shelf path:  %CUSTOM_SHELF_ESCAPED%




