# 🎬 Video Downloader - macOS & Linux

Versão para **macOS** (Intel e M1/M2/M3) e **Linux** da ferramenta de download de vídeos com interface gráfica.

## ✨ Características

- ✅ **Interface Gráfica** - Fácil de usar
- ✅ **Melhor Qualidade** - 4K, 60fps se disponível
- ✅ **Multiplataformas** - macOS (Intel & Apple Silicon) + Linux
- ✅ **Metadados** - Salva título, descrição, autor
- ✅ **Duas Formas de Entrada** - Arquivo .txt ou colar links
- ✅ **Log em Tempo Real** - Acompanhe cada download
- ✅ **100% Seguro** - Código aberto, sem malware

## 🚀 Instalação Rápida

### macOS (Intel & Apple Silicon)

#### 1️⃣ Instale Homebrew (se não tiver)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 2️⃣ Instale Python
```bash
brew install python3
```

#### 3️⃣ Clone o Repositório
```bash
git clone https://github.com/nicksonn/video-downloader.git
cd video-downloader
```

#### 4️⃣ Instale Dependências
```bash
pip3 install yt-dlp
```

#### 5️⃣ Dê Permissão de Execução
```bash
chmod +x executar_macos.sh
```

#### 6️⃣ Execute
```bash
./executar_macos.sh
```

---

### Linux (Ubuntu/Debian/Fedora)

#### 1️⃣ Instale Python
**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-tk
```

**Fedora:**
```bash
sudo dnf install python3 python3-pip python3-tkinter
```

#### 2️⃣ Clone o Repositório
```bash
git clone https://github.com/nicksonn/video-downloader.git
cd video-downloader
```

#### 3️⃣ Instale Dependências
```bash
pip3 install yt-dlp
```

#### 4️⃣ Dê Permissão de Execução
```bash
chmod +x executar_macos.sh
```

#### 5️⃣ Execute
```bash
./executar_macos.sh
```

---

## 📖 Como Usar

1. **Execute** o script:
   ```bash
   ./executar_macos.sh
   ```

2. **Escolha um método:**
   - 📄 **Arquivo .txt** - Lista de links
   - 📋 **Colar Direto** - Cole na interface

3. **Selecione a pasta** onde salvar

4. **Clique** em "▶ INICIAR DOWNLOADS"

5. **Aguarde** - Veja progresso no log

---

## 📦 O Que é Baixado

Para cada vídeo:
```
Video_Title.mp4              ← Vídeo em alta qualidade
INFO_Video_Title.txt         ← Metadados
```

---

## 🔧 Requisitos

- **macOS:** 10.13+ (Intel ou Apple Silicon)
- **Linux:** Ubuntu 18.04+ / Debian 10+ / Fedora 30+
- **Python:** 3.7+
- **Internet:** Conexão estável

---

## ⚙️ Solução de Problemas

### "command not found: python3"
```bash
brew install python3  # macOS
sudo apt install python3  # Linux
```

### "ModuleNotFoundError: No module named 'tkinter'"
**macOS:** Já incluído com Python via Homebrew

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-tk
```

**Linux (Fedora):**
```bash
sudo dnf install python3-tkinter
```

### "yt-dlp command not found"
```bash
pip3 install yt-dlp -U
```

### Permissão negada ao executar
```bash
chmod +x executar_macos.sh
./executar_macos.sh
```

---

## 📁 Estrutura do Projeto

```
video-downloader/
├── video_downloader_macos.py    ← Programa principal
├── executar_macos.sh             ← Script para rodar
├── exemplo_links.txt             ← Exemplo
├── README.md                      ← Documentação Windows
├── README_MACOS.md              ← Este arquivo
└── LICENSE                       ← Licença MIT
```

---

## 🎯 Comparação: Windows vs macOS/Linux

| Feature | Windows | macOS/Linux |
|---------|---------|-------------|
| **Interface Gráfica** | Sim (GUI) | Sim (GUI) |
| **Executável** | .exe (VideoDownloader_Instalavel) | Script shell (.sh) |
| **Python Required** | Não (exe) | Sim (3.7+) |
| **Suporte** | Completo | Completo |
| **Metadados** | Sim | Sim |
| **Melhor Qualidade** | Sim | Sim |

---

## 💡 Dicas

- **Alias para facilitar:**
  ```bash
  echo "alias video-downloader='~/path/to/executar_macos.sh'" >> ~/.zshrc
  source ~/.zshrc
  video-downloader
  ```

- **Usar em background:**
  ```bash
  nohup ./executar_macos.sh &
  ```

- **Executar com arquivo direto:**
  ```bash
  python3 video_downloader_macos.py
  ```

---

## 🐛 Reportar Bugs

Se encontrar problemas:
1. Abra uma [Issue](https://github.com/nicksonn/video-downloader/issues)
2. Inclua: Sistema operacional, versão Python, mensagem de erro

---

## 📝 Licença

MIT License - veja [LICENSE](LICENSE)

---

## ⚖️ Aviso Legal

- Use apenas para conteúdo que você tem permissão
- Respeite direitos autorais
- Não republique sem autorização

---

**Versão:** 1.0 (macOS/Linux)  
**Python:** 3.7+  
**Suporte:** macOS 10.13+ | Linux (Ubuntu, Debian, Fedora)
