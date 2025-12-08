:: ***************************************************************
::  Content: start desktop app
:: 
::  2025-12-01
:: 
::  Author: Elena Giuliani
::  email: elenagiuliani94@outlook.it
:: ***************************************************************
echo off

:: PATHS
set "PROJECT_ROOT=%~dp0"
set "PIPELINE_PATH=%PROJECT_ROOT%\library\apps\arAsset.py"

:: PYTHON
set "PYTHONPATH=%PIPELINE_PATH%"

python "%PIPELINE_PATH%"



