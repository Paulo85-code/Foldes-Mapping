@echo off
cls
net use J: \\brtja20p\acessos
del /f "%~f0"
exit
