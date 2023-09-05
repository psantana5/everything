@echo off

setlocal

set "temp_folder=%TEMP%"

if exist "%temp_folder%" (
  powershell.exe -Command "Get-ChildItem -Path '%temp_folder%' -Recurse | Remove-Item -Force -Recurse"
  set /a "size_freed_up=0"
  for /f "tokens=2" %%a in ('dir /s "%temp_folder%" ^| findstr /i "bytes"') do set /a "size_freed_up+=%%a"
  echo The following folders were deleted: %temp_folder%
  echo The total space freed up is: %size_freed_up% bytes
) else (
  echo No temporary folders found.
)

pause