@echo off

SET app=%0
SET lib=%~dp0

python "%lib%install.py" %*

echo.

exit /B %ERRORLEVEL%