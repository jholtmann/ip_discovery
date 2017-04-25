@echo off

net session >nul 2>&1
if %errorLevel% == 0 (
    python %0\..\ip_disc_client.py
) else (
    echo Administrator priviliges required.
)

pause