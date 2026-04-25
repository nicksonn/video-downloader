#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video Downloader - Versão macOS/Linux
Baixe vídeos de TikTok, Instagram, YouTube com interface gráfica
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime
import platform

class VideoDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Downloader - TikTok, Instagram, YouTube")
        self.root.geometry("800x700")
        self.root.resizable(True, True)

        # Variáveis
        self.links_file = tk.StringVar()
        self.output_folder = tk.StringVar(value=str(Path.home() / "Downloads" / "Videos"))
        self.is_downloading = False
        self.input_mode = tk.StringVar(value="file")

        # Cores
        self.root.configure(bg="#f0f0f0")

        self.setup_ui()
        self.check_yt_dlp()

    def check_yt_dlp(self):
        """Verifica se yt-dlp está instalado e funcional"""
        self.log("Verificando yt-dlp...", is_startup=True)

        try:
            result = subprocess.run([sys.executable, "-m", "yt_dlp", "--version"],
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                version = result.stdout.strip()
                self.log(f"✓ yt-dlp encontrado: {version}", is_startup=True)
                return True
        except Exception as e:
            self.log(f"✗ Erro ao verificar yt-dlp: {e}", is_startup=True)

        self.log("yt-dlp não está instalado. Tentando instalar...", is_startup=True)

        try:
            self.log("Aguarde... isso pode demorar alguns minutos...", is_startup=True)
            subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp", "-U"],
                         check=True, capture_output=True, timeout=120)

            self.log("✓ yt-dlp instalado com sucesso!", is_startup=True)
            messagebox.showinfo("Sucesso", "yt-dlp instalado! Você pode começar a usar a ferramenta.")
            return True

        except subprocess.TimeoutExpired:
            self.log("✗ Timeout na instalação", is_startup=True)
            messagebox.showerror("Erro", "Instalação de yt-dlp expirou. Tente novamente.")
            return False
        except Exception as e:
            msg = f"Erro ao instalar yt-dlp: {e}\n\nTente instalar manualmente:\npip install yt-dlp -U"
            self.log(f"✗ {msg}", is_startup=True)
            messagebox.showerror("Erro de Instalação", msg)
            return False

    def setup_ui(self):
        """Configura a interface gráfica"""
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Seção de entrada de links
        links_frame = tk.LabelFrame(main_frame, text="🔗 Links para Baixar",
                                     bg="#f0f0f0", font=("Arial", 10, "bold"))
        links_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # Opções de entrada
        option_frame = tk.Frame(links_frame, bg="#f0f0f0")
        option_frame.pack(fill=tk.X, padx=5, pady=5)

        tk.Radiobutton(option_frame, text="📄 Usar arquivo .txt",
                      variable=self.input_mode, value="file",
                      command=self.toggle_input_mode,
                      bg="#f0f0f0", font=("Arial", 9)).pack(side=tk.LEFT, padx=5)

        tk.Radiobutton(option_frame, text="📋 Colar links aqui",
                      variable=self.input_mode, value="paste",
                      command=self.toggle_input_mode,
                      bg="#f0f0f0", font=("Arial", 9)).pack(side=tk.LEFT, padx=5)

        # Frame para arquivo
        self.file_frame = tk.Frame(links_frame, bg="#f0f0f0")
        self.file_frame.pack(fill=tk.X, padx=5, pady=(0, 5))

        tk.Label(self.file_frame, text="Arquivo .txt com os links (um por linha):",
                bg="#f0f0f0", font=("Arial", 9)).pack(anchor=tk.W)

        file_input_frame = tk.Frame(self.file_frame, bg="#f0f0f0")
        file_input_frame.pack(fill=tk.X, pady=5)

        tk.Entry(file_input_frame, textvariable=self.links_file, state="readonly",
                width=50, font=("Arial", 9)).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Button(file_input_frame, text="Selecionar", command=self.select_file,
                 bg="#4CAF50", fg="white", padx=10).pack(side=tk.LEFT)

        # Frame para colar links
        self.paste_frame = tk.Frame(links_frame, bg="#f0f0f0")
        self.paste_frame.pack_forget()

        tk.Label(self.paste_frame, text="Cole seus links abaixo (um por linha):",
                bg="#f0f0f0", font=("Arial", 9)).pack(anchor=tk.W, padx=5)

        self.links_text = scrolledtext.ScrolledText(self.paste_frame, height=6, width=70,
                                                     bg="white", fg="#333", font=("Courier", 9))
        self.links_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        button_paste_frame = tk.Frame(self.paste_frame, bg="#f0f0f0")
        button_paste_frame.pack(fill=tk.X, padx=5, pady=5)

        tk.Button(button_paste_frame, text="Limpar", command=self.clear_links_text,
                 bg="#FF9800", fg="white", padx=10).pack(side=tk.LEFT, padx=5)

        # Seção de pasta de destino
        output_frame = tk.LabelFrame(main_frame, text="📁 Pasta de Destino",
                                     bg="#f0f0f0", font=("Arial", 10, "bold"))
        output_frame.pack(fill=tk.X, pady=(0, 10))

        folder_input_frame = tk.Frame(output_frame, bg="#f0f0f0")
        folder_input_frame.pack(fill=tk.X, padx=5, pady=5)

        tk.Entry(folder_input_frame, textvariable=self.output_folder,
                width=50, font=("Arial", 9)).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Button(folder_input_frame, text="Procurar", command=self.select_folder,
                 bg="#2196F3", fg="white", padx=10).pack(side=tk.LEFT)

        tk.Button(output_frame, text="🔍 Abrir pasta de destino",
                 command=self.open_output_folder,
                 bg="#FF9800", fg="white", width=30).pack(pady=5)

        # Seção de log
        log_frame = tk.LabelFrame(main_frame, text="📋 Log (Mensagens de Status)",
                                  bg="#f0f0f0", font=("Arial", 10, "bold"))
        log_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        self.log_text = scrolledtext.ScrolledText(log_frame, height=15, width=80,
                                                   bg="white", fg="#333", font=("Courier", 9))
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Botões de controle
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(fill=tk.X)

        self.download_btn = tk.Button(button_frame, text="▶ INICIAR DOWNLOADS",
                                       command=self.start_download,
                                       bg="#4CAF50", fg="white", font=("Arial", 11, "bold"),
                                       padx=20, pady=12)
        self.download_btn.pack(side=tk.LEFT, padx=(0, 5))

        tk.Button(button_frame, text="Limpar Log", command=self.clear_log,
                 bg="#9C27B0", fg="white", padx=15, pady=10).pack(side=tk.LEFT, padx=5)

        tk.Button(button_frame, text="❌ Sair", command=self.root.quit,
                 bg="#f44336", fg="white", padx=15, pady=10).pack(side=tk.RIGHT)

    def toggle_input_mode(self):
        """Alterna entre modo arquivo e modo colar"""
        if self.input_mode.get() == "file":
            self.file_frame.pack(fill=tk.X, padx=5, pady=(0, 5))
            self.paste_frame.pack_forget()
            self.log("📄 Modo: Usar arquivo .txt")
        else:
            self.file_frame.pack_forget()
            self.paste_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))
            self.log("📋 Modo: Colar links diretamente")

    def select_file(self):
        """Seleciona arquivo de links"""
        file = filedialog.askopenfilename(
            title="Selecione arquivo com links",
            filetypes=[("Arquivo texto", "*.txt"), ("Todos", "*.*")]
        )
        if file:
            self.links_file.set(file)
            self.log(f"✓ Arquivo selecionado: {file}")

    def select_folder(self):
        """Seleciona pasta de destino"""
        folder = filedialog.askdirectory(title="Selecione pasta para salvar vídeos")
        if folder:
            self.output_folder.set(folder)
            self.log(f"✓ Pasta selecionada: {folder}")

    def open_output_folder(self):
        """Abre a pasta de destino"""
        folder = self.output_folder.get()
        if os.path.exists(folder):
            if platform.system() == 'Darwin':  # macOS
                os.system(f'open "{folder}"')
            else:  # Linux
                os.system(f'xdg-open "{folder}"')
            self.log(f"✓ Abrindo pasta: {folder}")
        else:
            self.log(f"✗ Pasta não existe: {folder}")
            messagebox.showwarning("Aviso", f"Pasta não existe:\n{folder}")

    def log(self, message, is_startup=False):
        """Adiciona mensagem ao log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"

        self.log_text.insert(tk.END, full_message)
        self.log_text.see(tk.END)
        self.root.update()

        if is_startup:
            print(message)

    def clear_log(self):
        """Limpa o log"""
        self.log_text.delete(1.0, tk.END)

    def clear_links_text(self):
        """Limpa o texto de links colados"""
        self.links_text.delete(1.0, tk.END)

    def validate_inputs(self):
        """Valida entradas"""
        if self.input_mode.get() == "file":
            if not self.links_file.get():
                messagebox.showerror("Erro", "❌ Selecione um arquivo de links")
                self.log("✗ Nenhum arquivo de links selecionado")
                return False

            if not os.path.exists(self.links_file.get()):
                messagebox.showerror("Erro", f"❌ Arquivo não encontrado:\n{self.links_file.get()}")
                self.log(f"✗ Arquivo não existe: {self.links_file.get()}")
                return False
        else:
            links_text = self.links_text.get(1.0, tk.END).strip()
            if not links_text:
                messagebox.showerror("Erro", "❌ Cole os links na caixa de texto")
                self.log("✗ Nenhum link colado")
                return False

        output_folder = self.output_folder.get()
        if not output_folder:
            messagebox.showerror("Erro", "❌ Selecione pasta de destino")
            self.log("✗ Nenhuma pasta de destino selecionada")
            return False

        return True

    def start_download(self):
        """Inicia os downloads"""
        if not self.validate_inputs():
            return

        if self.is_downloading:
            messagebox.showwarning("Aviso", "⚠️ Já há um download em progresso")
            return

        thread = threading.Thread(target=self.download_videos)
        thread.daemon = True
        thread.start()

    def download_videos(self):
        """Processa downloads dos vídeos"""
        self.is_downloading = True
        self.download_btn.config(state=tk.DISABLED, bg="#999")

        try:
            output_folder = self.output_folder.get()
            Path(output_folder).mkdir(parents=True, exist_ok=True)
            self.log(f"✓ Pasta de destino: {output_folder}")

            if self.input_mode.get() == "file":
                with open(self.links_file.get(), 'r', encoding='utf-8') as f:
                    links = [line.strip() for line in f if line.strip()]
                self.log(f"✓ Links lidos do arquivo: {self.links_file.get()}")
            else:
                links_text = self.links_text.get(1.0, tk.END)
                links = [line.strip() for line in links_text.split('\n') if line.strip()]
                self.log(f"✓ Links lidos do texto colado")

            if not links:
                messagebox.showwarning("Aviso", "⚠️ Nenhum link encontrado")
                self.log("✗ Lista de links vazia")
                return

            self.log(f"\n{'='*70}")
            self.log(f"🎬 INICIANDO DOWNLOADS DE {len(links)} VÍDEO(S)")
            self.log(f"{'='*70}\n")

            success_count = 0
            error_count = 0

            for idx, link in enumerate(links, 1):
                if not link:
                    continue

                self.log(f"\n[{idx}/{len(links)}] Processando: {link}")

                try:
                    video_output = os.path.join(output_folder, "%(title)s.%(ext)s")

                    cmd = [
                        sys.executable,
                        "-m", "yt_dlp",
                        "-f", "bestvideo+bestaudio/best",
                        "-o", video_output,
                        "--no-warnings",
                        "--progress",
                        link
                    ]

                    self.log(f"  → Executando download...")

                    result = subprocess.run(
                        cmd,
                        capture_output=True,
                        text=True,
                        timeout=600
                    )

                    if result.returncode == 0:
                        self.log(f"  ✓ Download concluído com sucesso!")
                        self.download_metadata(link, output_folder)
                        success_count += 1
                    else:
                        error_msg = result.stderr.strip() if result.stderr else "Erro desconhecido"
                        self.log(f"  ✗ Erro: {error_msg}")
                        error_count += 1

                except subprocess.TimeoutExpired:
                    self.log(f"  ✗ Timeout - download demorou muito (>10min)")
                    error_count += 1
                except Exception as e:
                    self.log(f"  ✗ Erro ao processar: {str(e)}")
                    error_count += 1

            self.log(f"\n{'='*70}")
            self.log(f"✅ PROCESSO FINALIZADO!")
            self.log(f"   Sucesso: {success_count} | Erros: {error_count}")
            self.log(f"   Pasta: {output_folder}")
            self.log(f"   Arquivos .txt com informações também criados!")
            self.log(f"{'='*70}\n")

            msg = f"Downloads concluídos!\n\n✓ Sucesso: {success_count}\n✗ Erros: {error_count}\n\nVídeos e informações salvos em:\n{output_folder}"
            messagebox.showinfo("Concluído", msg)

        except Exception as e:
            error_msg = f"Erro geral durante downloads:\n{str(e)}"
            self.log(f"✗ {error_msg}")
            messagebox.showerror("Erro", error_msg)

        finally:
            self.is_downloading = False
            self.download_btn.config(state=tk.NORMAL, bg="#4CAF50")

    def download_metadata(self, link, output_folder):
        """Baixa e salva metadados do vídeo"""
        try:
            self.log(f"  → Baixando informações...")

            cmd = [
                sys.executable,
                "-m", "yt_dlp",
                "--dump-json",
                "--no-warnings",
                "-q",
                link
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode == 0:
                import json
                data = json.loads(result.stdout)

                title = data.get('title', 'Vídeo sem título')
                description = data.get('description', 'Sem descrição')
                uploader = data.get('uploader', 'Autor desconhecido')
                upload_date = data.get('upload_date', 'Data desconhecida')
                duration = data.get('duration', 0)
                url = data.get('webpage_url', link)

                if duration:
                    minutes = duration // 60
                    seconds = duration % 60
                    duration_str = f"{minutes}:{seconds:02d}"
                else:
                    duration_str = "Duração desconhecida"

                safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
                info_file = os.path.join(output_folder, f"INFO_{safe_title}.txt")

                counter = 1
                while os.path.exists(info_file):
                    info_file = os.path.join(output_folder, f"INFO_{safe_title}_{counter}.txt")
                    counter += 1

                with open(info_file, 'w', encoding='utf-8') as f:
                    f.write("="*70 + "\n")
                    f.write("INFORMAÇÕES DO VÍDEO\n")
                    f.write("="*70 + "\n\n")
                    f.write(f"TÍTULO:\n{title}\n\n")
                    f.write(f"AUTOR:\n{uploader}\n\n")
                    f.write(f"DATA DE UPLOAD:\n{upload_date}\n\n")
                    f.write(f"DURAÇÃO:\n{duration_str}\n\n")
                    f.write(f"LINK ORIGINAL:\n{url}\n\n")
                    f.write(f"DESCRIÇÃO:\n{'-'*70}\n{description}\n")
                    f.write(f"{'-'*70}\n")

                self.log(f"  ✓ Informações salvas em: INFO_{safe_title}.txt")

            else:
                self.log(f"  ⚠️  Não foi possível extrair informações (vídeo pode ser privado)")

        except Exception as e:
            self.log(f"  ⚠️  Erro ao extrair metadados: {str(e)}")


def main():
    root = tk.Tk()
    app = VideoDownloaderGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
