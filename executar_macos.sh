#!/bin/bash

echo ""
echo "╔════════════════════════════════════════════════╗"
echo "║  🎬 Video Downloader - macOS/Linux             ║"
echo "║     TikTok, Instagram, YouTube                 ║"
echo "╚════════════════════════════════════════════════╝"
echo ""

# Detecta o sistema operacional
SISTEMA=$(uname -s)

if [[ "$SISTEMA" == "Darwin" ]]; then
    # macOS
    python3 video_downloader_macos.py
elif [[ "$SISTEMA" == "Linux" ]]; then
    # Linux
    python3 video_downloader_macos.py
else
    echo "❌ Sistema operacional não suportado: $SISTEMA"
    echo "Esta versão é para macOS e Linux apenas."
    exit 1
fi
