# 🎬 Video Downloader - TikTok, Instagram, YouTube

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Windows](https://img.shields.io/badge/Platform-Windows-0078D4.svg)]()
[![Releases](https://img.shields.io/github/v/release/nickson/video-downloader)]()

Ferramenta de download de vídeos com **interface gráfica** para Windows. Baixe vídeos de **TikTok, Instagram, YouTube** e 500+ outros sites em **melhor qualidade disponível**.

## 🌟 Características

- ✅ **Interface Gráfica (GUI)** - Fácil de usar, sem linha de comando
- ✅ **Melhor Qualidade** - 4K, 60fps se disponível
- ✅ **Múltiplas Plataformas** - TikTok, Instagram, YouTube, etc
- ✅ **Metadados** - Salva título, descrição, autor de cada vídeo
- ✅ **Duas Formas de Entrada** - Arquivo .txt ou colar links direto
- ✅ **Executável Standalone** - Funciona sem Python instalado
- ✅ **Log em Tempo Real** - Acompanhe cada download
- ✅ **100% Seguro** - Código aberto, sem malware

## 🚀 Quick Start

### Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/video-downloader.git
cd video-downloader

# Instale dependências
pip install -r requirements.txt

# Execute
python video_downloader.py
```

### Usar Executável (Sem Python)

Baixe o instalável em [Releases](https://github.com/seu-usuario/video-downloader/releases):
1. Extraia `VideoDownloader_Instalavel.zip`
2. Duplo clique em `EXECUTAR.bat`
3. Pronto! Funciona sem Python

## 📖 Como Usar

### Interface Gráfica

1. **Execute** a ferramenta
2. **Escolha um método:**
   - 📄 **Arquivo .txt** - Uma lista de links
   - 📋 **Colar Direto** - Cole links na interface
3. **Escolha a pasta** onde salvar
4. **Clique** em "▶ INICIAR DOWNLOADS"
5. **Aguarde** - Veja o progresso no log

### Exemplo de Arquivo de Links

```txt
https://www.tiktok.com/@usuario/video/123456
https://www.youtube.com/watch?v=ABC123
https://www.instagram.com/reel/XYZ789/
```

## 📦 O Que é Baixado

Para cada vídeo, você recebe:

```
Video_Title.mp4                  ← Vídeo em alta qualidade
INFO_Video_Title.txt             ← Metadados
```

O arquivo `.txt` contém:
- Título
- Autor/Canal
- Data de upload
- Duração
- Link original
- Descrição completa

## 🔧 Requisitos

### Para Desenvolvedores

- Python 3.7+
- yt-dlp (instalado automaticamente)
- tkinter (incluído no Python)

### Para Usuários

- Windows 7+
- Internet
- ~300 MB de espaço (para o executável)

## 📚 Documentação

- **[INSTRUÇÕES.txt](INSTRUÇÕES.txt)** - Guia passo a passo em português
- **[README.md](README.md)** - Documentação completa
- **[COMO_GERAR_INSTALAVEL.md](COMO_GERAR_INSTALAVEL.md)** - Como criar .exe

## 🛠️ Gerar Executável

```bash
# Instale dependências
pip install -r requirements-build.txt

# Gere o instalável
python gerar_instalavel.py

# Resultado em: VideoDownloader_Instalavel/
```

## 📁 Estrutura do Projeto

```
video-downloader/
├── video_downloader.py           # Ferramenta principal
├── gerar_instalavel.py           # Gerador de .exe
├── TESTAR.py                     # Script de diagnóstico
├── exemplo_links.txt             # Exemplo com links
├── requirements.txt              # Dependências
├── requirements-build.txt        # Para gerar .exe
├── README.md                     # Documentação
├── INSTRUÇÕES.txt                # Guia em português
├── COMO_GERAR_INSTALAVEL.md     # Como compilar
└── .gitignore
```

## 🤝 Contribuindo

Contributions são bem-vindas! Para mudanças importantes:

1. Faça um Fork do repositório
2. Crie uma branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

MIT License - veja [LICENSE](LICENSE) para detalhes

## ⚖️ Aviso Legal

- Use apenas para conteúdo que você tem permissão de baixar
- Respeite direitos autorais
- Não republique conteúdo de terceiros sem permissão
- A ferramenta é para uso pessoal

## 🐛 Reportar Bugs

Encontrou um bug? Abra uma [Issue](https://github.com/seu-usuario/video-downloader/issues):

```
Título: [BUG] Descrição breve
Descrição: 
- O que tentou fazer
- O que esperava
- O que aconteceu
- Seu sistema (Windows 10, Python 3.10, etc)
```

## 💡 Sugestões e Ideias

Tem uma ideia? Abra uma [Discussion](https://github.com/seu-usuario/video-downloader/discussions)!

## 📞 Suporte

- 📖 Veja a [Documentação](README.md)
- 🐛 Reporte bugs em [Issues](https://github.com/seu-usuario/video-downloader/issues)
- 💬 Tire dúvidas em [Discussions](https://github.com/seu-usuario/video-downloader/discussions)

## 🙏 Agradecimentos

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Mecanismo de download
- [PyInstaller](https://pyinstaller.org/) - Criação de executáveis
- Python Community - Ferramentas incríveis

## 📊 Status

- ✅ v1.0 - Release inicial
- 🚀 Interface GUI funcional
- ✅ Download em melhor qualidade
- ✅ Extração de metadados
- ✅ Executável Windows
- 🔄 Em desenvolvimento...

## 🗺️ Roadmap

- [ ] Suporte para Linux/macOS
- [ ] Interface em múltiplos idiomas
- [ ] Histórico de downloads
- [ ] Filtros por qualidade
- [ ] Playlist support
- [ ] Configurações customizáveis

---

<div align="center">

**[Baixar Executável](https://github.com/seu-usuario/video-downloader/releases)** • **[Documentação](README.md)** • **[Issues](https://github.com/seu-usuario/video-downloader/issues)**

Feito com ❤️ em Python

</div>
