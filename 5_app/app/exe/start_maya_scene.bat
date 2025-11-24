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
set "PROJECT_ROOT=C:\Users\utente\Desktop\Python Advanced - AlexanderRichterCourse\Elena_assignments"
set "PIPELINE_PATH=%PROJECT_ROOT%\lesson01_batch"

:: VERSION
set "MAYA_VERSION=2022"

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
set "MAYA_DIR=C:\Program Files\Autodesk\Maya%MAYA_VERSION%"
set "PATH=%MAYA_DIR%\bin;%PATH%"

:: START MAYA
::start "" "%MAYA_DIR%\bin\maya.exe" -command "python(\"exec(open(r'%CUSTOM_SHELF_ESCAPED%').read())\")"

start "" "C:\Users\utente\Desktop\Python Advanced - AlexanderRichterCourse\Elena_assignments\git_elena_assignments\5_app\app\testing_area/Props/P_25_001__1970_ceramic_set/files//maya/modeling/1970Ceramic_model_project/scenes/1970Ceramic_model_v002.ma"