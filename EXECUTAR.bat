@echo off
chcp 65001 >nul
cls
echo.
echo ═══════════════════════════════════════════════════════
echo      🎬 Downloader de Vídeos - TikTok, Instagram, YouTube
echo ═══════════════════════════════════════════════════════
echo.

python video_downloader.py

if errorlevel 1 (
    echo.
    echo ❌ Erro ao executar!
    echo.
    echo Possíveis soluções:
    echo 1. Verifique se Python 3.7+ está instalado
    echo 2. Tente executar como Administrador
    echo 3. Verifique arquivo video_downloader.py existe
    echo.
    pause
)
