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
set "PIPELINE_PATH=%PROJECT_ROOT%\..\library\apps\arScene.py"

:: PYTHON
set "PYTHONPATH=%PROJECT_ROOT%"

python "%PIPELINE_PATH%"




