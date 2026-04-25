#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste para diagnosticar problemas com yt-dlp
"""

import subprocess
import sys
import os
from pathlib import Path

def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def test_python():
    print_section("1️⃣  TESTANDO PYTHON")
    print(f"Versão Python: {sys.version}")
    print(f"Executável: {sys.executable}")

    if sys.version_info >= (3, 7):
        print("✓ Python versão OK (3.7+)")
        return True
    else:
        print("✗ Python versão baixa! (Requer 3.7+)")
        return False

def test_pip():
    print_section("2️⃣  TESTANDO PIP")
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"],
                              capture_output=True, text=True, timeout=10)
        print(f"✓ {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"✗ Erro: {e}")
        return False

def test_yt_dlp_installed():
    print_section("3️⃣  VERIFICANDO YT-DLP INSTALADO")
    try:
        result = subprocess.run([sys.executable, "-m", "yt_dlp", "--version"],
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✓ {result.stdout.strip()}")
            return True
        else:
            print(f"✗ yt-dlp retornou erro: {result.stderr}")
            return False
    except FileNotFoundError:
        print("✗ yt-dlp não encontrado no PATH")
        return False
    except Exception as e:
        print(f"✗ Erro: {e}")
        return False

def test_yt_dlp_help():
    print_section("4️⃣  TESTANDO COMANDO YT-DLP")
    try:
        result = subprocess.run([sys.executable, "-m", "yt_dlp", "--help"],
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✓ yt-dlp respondeu ao help")
            return True
        else:
            print(f"✗ yt-dlp help falhou")
            return False
    except Exception as e:
        print(f"✗ Erro: {e}")
        return False

def test_example_link():
    print_section("5️⃣  TESTANDO DOWNLOAD COM LINK DE EXEMPLO")
    test_link = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
    test_folder = Path.home() / "Downloads" / "VideoTest"

    try:
        test_folder.mkdir(parents=True, exist_ok=True)
        print(f"Link de teste: {test_link}")
        print(f"Pasta de teste: {test_folder}")
        print("Iniciando download (pode demorar)...")

        cmd = [
            sys.executable,
            "-m", "yt_dlp",
            "-f", "best",
            "-o", str(test_folder / "%(title)s.%(ext)s"),
            "--quiet",
            test_link
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        if result.returncode == 0:
            files = list(test_folder.glob("*"))
            if files:
                print(f"✓ Download bem-sucedido!")
                print(f"  Arquivo: {files[0].name}")
                print(f"  Tamanho: {files[0].stat().st_size / (1024*1024):.2f} MB")
                return True
            else:
                print("✗ Download executado mas arquivo não encontrado")
                return False
        else:
            print(f"✗ Erro no download:")
            print(f"  stdout: {result.stdout}")
            print(f"  stderr: {result.stderr}")
            return False

    except subprocess.TimeoutExpired:
        print("✗ Timeout (download demorou mais de 60s)")
        return False
    except Exception as e:
        print(f"✗ Erro: {e}")
        return False

def test_arquivo_exemplo():
    print_section("6️⃣  VERIFICANDO ARQUIVO EXEMPLO")
    exemplo = Path(__file__).parent / "exemplo_links.txt"

    if exemplo.exists():
        with open(exemplo, 'r', encoding='utf-8') as f:
            links = [l.strip() for l in f if l.strip()]
        print(f"✓ Arquivo encontrado: {exemplo}")
        print(f"  Links encontrados: {len(links)}")
        for i, link in enumerate(links[:3], 1):
            print(f"    {i}. {link}")
        if len(links) > 3:
            print(f"    ... e mais {len(links) - 3}")
        return True
    else:
        print(f"✗ Arquivo não encontrado: {exemplo}")
        return False

def main():
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*10 + "🎬 TESTE DE DIAGNÓSTICO DE DOWNLOADS" + " "*11 + "║")
    print("╚" + "="*58 + "╝")

    results = {
        "Python": test_python(),
        "Pip": test_pip(),
        "yt-dlp instalado": test_yt_dlp_installed(),
        "yt-dlp help": test_yt_dlp_help(),
        "Arquivo exemplo": test_arquivo_exemplo(),
    }

    print_section("📊 RESUMO DOS TESTES")
    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for test, result in results.items():
        symbol = "✓" if result else "✗"
        print(f"{symbol} {test}")

    print(f"\nTotal: {passed}/{total} testes passaram")

    if passed == total:
        print("\n✅ Tudo OK! A ferramenta deveria funcionar.")
        print("\nPróximas tentativas:")
        print("1. Execute: python video_downloader.py")
        print("2. Selecione arquivo de links (exemplo_links.txt)")
        print("3. Clique em 'INICIAR DOWNLOADS'")
    else:
        print("\n⚠️  Alguns testes falharam. Tente:")
        if not results.get("yt-dlp instalado"):
            print("→ Instalar yt-dlp: pip install yt-dlp -U")
        print("→ Reiniciar o computador")
        print("→ Tentar como Administrador")

    print("\n")
    input("Pressione ENTER para sair...")

if __name__ == "__main__":
    main()
