@echo off

rem This file is UTF-8 encoded, so we need to update the current code page while executing it
for /f "tokens=2 delims=:." %%a in ('"%SystemRoot%\System32\chcp.com"') do (
    set _OLD_CODEPAGE=%%a
)
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" 65001 > nul
)

<<<<<<< HEAD
set VIRTUAL_ENV=C:\Users\trand\coding_temple\cohorts\2021\december\week_01\01\fakebook-october\marvel-env
=======
set VIRTUAL_ENV=C:\Users\trand\coding_temple\cohorts\2021\december\week_01\01\marvel\marvel-env
>>>>>>> eef9db4ed2bf415e0ca66ce16e365942756f774f

if not defined PROMPT set PROMPT=$P$G

if defined _OLD_VIRTUAL_PROMPT set PROMPT=%_OLD_VIRTUAL_PROMPT%
if defined _OLD_VIRTUAL_PYTHONHOME set PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%

set _OLD_VIRTUAL_PROMPT=%PROMPT%
set PROMPT=(marvel-env) %PROMPT%

if defined PYTHONHOME set _OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%
set PYTHONHOME=

if defined _OLD_VIRTUAL_PATH set PATH=%_OLD_VIRTUAL_PATH%
if not defined _OLD_VIRTUAL_PATH set _OLD_VIRTUAL_PATH=%PATH%

set PATH=%VIRTUAL_ENV%\Scripts;%PATH%
<<<<<<< HEAD
set VIRTUAL_ENV_PROMPT=(marvel-env) 
=======
>>>>>>> eef9db4ed2bf415e0ca66ce16e365942756f774f

:END
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" %_OLD_CODEPAGE% > nul
    set _OLD_CODEPAGE=
)
