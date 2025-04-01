@echo off
cls
net use J: \\brtja20p\Areas\Recursos Humanos\Adm RH
del /f "%~f0"
exit
