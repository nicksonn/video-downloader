@echo off
chcp 65001 >nul
cls
color 0A

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║          🎬 GERADOR DE INSTALÁVEL PARA WINDOWS                ║
echo ║                                                                ║
echo ║  Este script vai gerar um .exe instalável da ferramenta       ║
echo ║  que funciona em qualquer Windows SEM precisar de Python!     ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

echo ⚠️  AVISO:
echo  • Este processo pode demorar de 5 a 15 minutos
echo  • A janela não deve ser fechada durante o processo
echo  • Isso é normal - é só compilando o código
echo.

pause

python gerar_instalavel.py

if %errorlevel% equ 0 (
    echo.
    echo ✓ Instalável gerado com sucesso!
    echo.
    echo 📁 Procure pela pasta "VideoDownloader_Instalavel"
    echo    Essa pasta contém tudo que você precisa distribuir!
    echo.
) else (
    echo.
    echo ✗ Erro ao gerar instalável
    echo.
    echo Possíveis soluções:
    echo • Verifique se Python está instalado
    echo • Tente executar como Administrador
    echo • Feche outros programas e tente novamente
    echo.
)

pause
