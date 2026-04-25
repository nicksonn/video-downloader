# 🎬 Downloader de Vídeos - TikTok, Instagram, YouTube

Ferramenta para baixar vídeos de múltiplas plataformas com **melhor qualidade disponível**.

## 📋 Funcionalidades

- ✅ Suporte para **YouTube, TikTok e Instagram**
- ✅ **Melhor qualidade disponível** (vídeo + áudio)
- ✅ Interface gráfica amigável
- ✅ Download em lote (múltiplos vídeos)
- ✅ Log em tempo real
- ✅ Tratamento de erros

## 🚀 Como Usar

### 1. Preparação Inicial

Certifique-se de ter Python 3.7+ instalado. Ao executar pela primeira vez, o programa pedirá para instalar `yt-dlp` (biblioteca necessária).

### 2. Criar arquivo com links

Crie um arquivo `links.txt` (ou qualquer nome) com os links dos vídeos, **um por linha**:

```
https://www.youtube.com/watch?v=...
https://www.tiktok.com/@usuario/video/...
https://www.instagram.com/reel/...
```

### 3. Executar a ferramenta

**Opção 1: Duplo clique**
```
Clique duas vezes em: video_downloader.py
```

**Opção 2: Pelo terminal/CMD**
```bash
python video_downloader.py
```

### 4. Usar a interface

1. **Selecione o arquivo de links** (.txt com os URLs)
2. **Escolha a pasta de destino** (onde salvar os vídeos)
3. **Clique em "Iniciar Downloads"**
4. Acompanhe o progresso no log

## 📁 Estrutura de Arquivos

```
Download Videos/
├── video_downloader.py    ← Ferramenta principal
├── exemplo_links.txt      ← Exemplo de arquivo com links
└── README.md             ← Este arquivo
```

## ⚙️ Configurações

A ferramenta está configurada para:
- **Melhor qualidade de vídeo disponível** (até 4K se disponível)
- **Melhor áudio disponível** (até 320kbps)
- **Merge automático** de vídeo + áudio
- **Nome dos arquivos**: Título do vídeo original

## 🔧 Requisitos

- Python 3.7+
- Internet
- `yt-dlp` (instalado automaticamente)

## ❓ Perguntas Frequentes

**P: Posso misturar links de diferentes plataformas?**
R: Sim! A ferramenta detecta automaticamente a plataforma de cada link.

**P: Por que alguns vídeos demoram mais?**
R: Vídeos em maior qualidade (4K, 60fps) demandam mais tempo de download.

**P: E se um vídeo falhar?**
R: A ferramenta pula para o próximo. Você pode tentar novamente depois.

**P: Os vídeos incluem áudio?**
R: Sim, todos os vídeos baixados incluem melhor qualidade de áudio disponível.

**P: Posso usar um arquivo .csv ou .xlsx?**
R: Por enquanto, apenas .txt é suportado. Você pode converter facilmente.

## 📝 Exemplo de Arquivo links.txt

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.tiktok.com/@usuario/video/1234567890123456789
https://www.instagram.com/reel/ABC123XYZ/
https://www.youtube.com/watch?v=jNQXAC9IVRw
```

## ⚠️ Avisos Importantes

- **Respeite os direitos autorais**: Não baixe vídeos protegidos sem permissão
- **Privacidade**: Não republique vídeos alheios sem autorização
- **Conexão**: Mantenha internet estável durante downloads
- **Espaço em disco**: Vídeos em alta qualidade ocupam bastante espaço

## 🐛 Problemas Comuns

**Erro: "yt-dlp não encontrado"**
- Instale manualmente: `pip install yt-dlp -U`

**Download não inicia**
- Verifique se o arquivo .txt existe e tem links válidos
- Verifique a pasta de destino tem permissão de escrita

**Vídeo não baixa**
- O link pode estar inválido ou privado
- A plataforma pode ter bloqueado acesso
- Tente copiar o link novamente e certifique-se da URL

---

**Versão**: 1.0
**Última atualização**: 2026-04-24
