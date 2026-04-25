#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar instalável (.exe) da ferramenta de download de vídeos
Usa PyInstaller para criar um executável standalone
"""

import subprocess
import sys
import os
from pathlib import Path
import shutil

def print_section(title):
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")

def install_pyinstaller():
    """Instala PyInstaller"""
    print_section("1️⃣  INSTALANDO PYINSTALLER")
    try:
        print("Instalando PyInstaller (pode demorar alguns minutos)...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "pyinstaller", "-U"],
            check=True
        )
        print("✓ PyInstaller instalado com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Erro ao instalar PyInstaller: {e}")
        return False

def create_spec_file():
    """Cria arquivo spec customizado para PyInstaller"""
    print_section("2️⃣  CRIANDO ARQUIVO DE CONFIGURAÇÃO")

    spec_content = """# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

a = Analysis(
    ['video_downloader.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['yt_dlp'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=[],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='VideoDownloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='NONE',
)
"""

    spec_file = Path("video_downloader.spec")
    with open(spec_file, 'w') as f:
        f.write(spec_content)

    print(f"✓ Arquivo spec criado: {spec_file}")
    return spec_file

def build_executable(spec_file):
    """Constrói o executável usando PyInstaller"""
    print_section("3️⃣  GERANDO EXECUTÁVEL")

    try:
        print("Gerando executável (pode demorar alguns minutos)...")
        print("Aguarde... isso é normal!\n")

        cmd = [
            sys.executable,
            "-m", "PyInstaller",
            str(spec_file),
            "--distpath=dist",
            "--workpath=build",
            "--clean",
        ]

        result = subprocess.run(cmd, capture_output=False)

        if result.returncode == 0:
            print("\n✓ Executável gerado com sucesso!")
            return True
        else:
            print("\n✗ Erro ao gerar executável")
            return False

    except Exception as e:
        print(f"✗ Erro: {e}")
        return False

def create_installer_package():
    """Cria pasta com instalável e todos os arquivos necessários"""
    print_section("4️⃣  PREPARANDO PACOTE DE INSTALAÇÃO")

    dist_folder = Path("dist")
    exe_file = dist_folder / "VideoDownloader" / "VideoDownloader.exe"

    if not exe_file.exists():
        # Tenta caminho alternativo
        exe_file = dist_folder / "VideoDownloader.exe"

    if not exe_file.exists():
        print(f"✗ Arquivo .exe não encontrado em {dist_folder}")
        return False

    # Cria pasta de pacote
    package_folder = Path("VideoDownloader_Instalavel")
    if package_folder.exists():
        shutil.rmtree(package_folder)

    package_folder.mkdir()

    try:
        # Copia o executável
        if (dist_folder / "VideoDownloader" / "VideoDownloader.exe").exists():
            shutil.copytree(
                dist_folder / "VideoDownloader",
                package_folder / "VideoDownloader"
            )
            exe_path = package_folder / "VideoDownloader" / "VideoDownloader.exe"
        else:
            shutil.copy(exe_file, package_folder / "VideoDownloader.exe")
            exe_path = package_folder / "VideoDownloader.exe"

        # Copia arquivos de documentação
        for file in ["README.md", "INSTRUÇÕES.txt", "exemplo_links.txt"]:
            if Path(file).exists():
                shutil.copy(file, package_folder / file)

        # Cria script batch para facilitar execução
        batch_content = """@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo ╔════════════════════════════════════════════════╗
echo ║  🎬 Downloader de Vídeos                       ║
echo ║     TikTok, Instagram, YouTube                ║
echo ╚════════════════════════════════════════════════╝
echo.

if exist VideoDownloader\\VideoDownloader.exe (
    start VideoDownloader\\VideoDownloader.exe
) else (
    start VideoDownloader.exe
)

echo Iniciando aplicação...
timeout /t 2 /nobreak
"""

        with open(package_folder / "EXECUTAR.bat", 'w', encoding='utf-8') as f:
            f.write(batch_content)

        # Cria arquivo README de instalação
        install_readme = """╔═══════════════════════════════════════════════════════════════════════╗
║                  🎬 DOWNLOADER DE VÍDEOS - INSTALAÇÃO                     ║
╚═══════════════════════════════════════════════════════════════════════╝

📦 CONTEÚDO DA PASTA:
───────────────────

  • VideoDownloader.exe ou VideoDownloader/VideoDownloader.exe
    → Executável da ferramenta (não precisa de Python!)

  • EXECUTAR.bat
    → Clique aqui para rodar a ferramenta facilmente

  • README.md
    → Documentação completa

  • INSTRUÇÕES.txt
    → Guia passo a passo

  • exemplo_links.txt
    → Exemplo com links para testar


🚀 COMO USAR:
────────────

OPÇÃO 1 (Recomendada):
  → Duplo clique em: EXECUTAR.bat
  → A ferramenta abre automaticamente

OPÇÃO 2:
  → Duplo clique em: VideoDownloader.exe
  → Se estiver em pasta VideoDownloader/


⚡ PRINCIPAIS VANTAGENS:
──────────────────────

  ✓ Funciona em qualquer Windows
  ✓ NÃO precisa instalar Python
  ✓ NÃO precisa de arquivo .txt
  ✓ Pode colar links direto na interface
  ✓ Salva vídeos em melhor qualidade
  ✓ Salva nome, descrição e informações


📋 PRIMEIRO USO:
────────────────

  1. Duplo clique em EXECUTAR.bat
  2. Na interface, escolha:
     - 📋 "Colar links aqui" (mais fácil)
     - 📄 "Usar arquivo .txt" (se preferir)
  3. Cole seus links ou selecione arquivo
  4. Clique em "▶ INICIAR DOWNLOADS"
  5. Aguarde os vídeos serem baixados


⚠️  AVISO:
─────────

  • Na primeira execução, pode demorar um pouco
  • Alguns antivírus podem avisar (é falso positivo)
  • Se receber aviso, clique "Executar mesmo assim"
  • A ferramenta baixa de forma 100% segura


❓ PROBLEMAS?
──────────

  1. Se nada acontecer ao clicar em EXECUTAR.bat:
     → Tente duplo clique em VideoDownloader.exe diretamente

  2. Se antivírus bloqueia:
     → Clique "Permitir" ou "Adicionar exceção"

  3. Se tiver erro de permissão:
     → Execute como Administrador
     → Clique direito → Executar como administrador


🔒 SEGURANÇA:
──────────

  • Não contém vírus ou malware
  • Gerado de código open-source
  • yt-dlp é biblioteca confiável e amplamente usada
  • Você pode examinar o código-fonte em video_downloader.py


📞 DÚVIDAS:
──────────

  Veja os arquivos:
  • README.md - documentação completa
  • INSTRUÇÕES.txt - guia passo a passo


═══════════════════════════════════════════════════════════════════════
Versão: 1.0 | Executável gerado com PyInstaller
═══════════════════════════════════════════════════════════════════════
"""

        with open(package_folder / "LEIA-ME.txt", 'w', encoding='utf-8') as f:
            f.write(install_readme)

        print(f"✓ Pacote criado em: {package_folder}")
        print(f"✓ Arquivos inclusos:")
        print(f"  • Executável")
        print(f"  • EXECUTAR.bat")
        print(f"  • INSTRUÇÕES.txt")
        print(f"  • README.md")
        print(f"  • LEIA-ME.txt")

        return package_folder

    except Exception as e:
        print(f"✗ Erro ao preparar pacote: {e}")
        return None

def main():
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*15 + "🎬 GERADOR DE INSTALÁVEL WINDOWS" + " "*21 + "║")
    print("╚" + "="*68 + "╝")

    # Verifica se arquivo principal existe
    if not Path("video_downloader.py").exists():
        print("\n✗ Erro: arquivo 'video_downloader.py' não encontrado!")
        print("Execute este script na pasta raiz do projeto.")
        input("Pressione ENTER para sair...")
        return False

    # Instala PyInstaller
    if not install_pyinstaller():
        print("\n✗ Falha ao instalar PyInstaller")
        input("Pressione ENTER para sair...")
        return False

    # Cria arquivo spec
    spec_file = create_spec_file()

    # Gera executável
    if not build_executable(spec_file):
        print("\n✗ Falha ao gerar executável")
        input("Pressione ENTER para sair...")
        return False

    # Cria pacote de instalação
    package_folder = create_installer_package()

    if not package_folder:
        print("\n✗ Falha ao criar pacote")
        input("Pressione ENTER para sair...")
        return False

    print_section("✅ INSTALÁVEL CRIADO COM SUCESSO!")
    print(f"📁 Pasta: {package_folder}")
    print(f"\n✓ Você pode distribuir a pasta '{package_folder}' em outros PCs Windows!")
    print(f"✓ Não precisa instalar nada, é totalmente standalone!")
    print(f"\n🚀 Próximas etapas:")
    print(f"  1. Copie a pasta '{package_folder}' para pendrive ou envie por email")
    print(f"  2. No outro PC, clique duplo em 'EXECUTAR.bat'")
    print(f"  3. Pronto! A ferramenta abre e funciona normalmente")

    print("\n")
    input("Pressione ENTER para sair...")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
