@echo off
cls
net use J: \\brtja20p\Acessos\Engenharia\GN 2025
del /f "%~f0"
exit
