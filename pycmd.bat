@echo off

SET app=%0
SET lib=%~dp0

python "%lib%pycmd" %*

echo.

exit /B %ERRORLEVEL%