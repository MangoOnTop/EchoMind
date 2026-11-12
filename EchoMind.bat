@echo off
title EchoMind Desktop Assistant
if exist "%~dp0dist\EchoMind.exe" (
    start "" "%~dp0dist\EchoMind.exe"
) else (
    python "%~dp0gui.py"
)
