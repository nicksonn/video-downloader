# 📦 Como Gerar Instalável para Windows

## 🎯 Objetivo

Converter a ferramenta Python em um **executável Windows (.exe)** que funciona em qualquer PC **sem precisar instalar Python**.

---

## 📋 Pré-requisitos

✓ Python 3.7+ instalado  
✓ Internet (para baixar dependências)  
✓ Espaço em disco (~ 500 MB durante geração)  

---

## 🚀 Passo 1: Gerar o Instalável

### Opção A: Clique Duplo (Mais Fácil)
```
Duplo clique em: GERAR_INSTALAVEL.bat
```

### Opção B: Pelo Terminal
```bash
python gerar_instalavel.py
```

**Aguarde de 5 a 15 minutos** - é normal demorar!

---

## ⏱️ O Que Acontece

1. **Instala PyInstaller** (se necessário)
2. **Compila o código Python** em executável
3. **Empacota tudo** junto
4. **Cria pasta pronta para distribuir**

---

## 📁 Resultado

Será criada uma pasta chamada:
```
VideoDownloader_Instalavel/
├── VideoDownloader.exe (ou VideoDownloader/)
├── EXECUTAR.bat
├── README.md
├── INSTRUÇÕES.txt
├── exemplo_links.txt
└── LEIA-ME.txt
```

---

## 💾 Como Distribuir

### Para Outro PC:

1. **Copie a pasta inteira** `VideoDownloader_Instalavel/`
   - Para pendrive
   - Para email
   - Para OneDrive/Google Drive
   - Para Dropbox

2. **No outro PC:**
   - Extraia a pasta (se enviou em .zip)
   - Duplo clique em `EXECUTAR.bat`
   - A ferramenta abre e funciona normalmente!

### ✨ Não Precisa:
- ❌ Instalar Python
- ❌ Instalar yt-dlp
- ❌ Configurar nada
- ✅ Apenas duplo clique e usar!

---

## 🔍 Se Der Erro

### Erro: "PyInstaller não encontrado"
```bash
pip install pyinstaller -U
```
Depois execute novamente.

### Erro: "Acesso negado"
→ Execute como Administrador:
  - Clique direito no .bat
  - Selecione "Executar como administrador"

### Processo muito lento
→ É normal! Tomar 15+ minutos é comum
→ Deixe processando, não feche a janela

### Antivírus bloqueia
→ Adicione exceção para a pasta
→ O executável é 100% seguro (gerado de código aberto)

---

## 📊 Tamanho do Arquivo

- **Pasta resultante:** ~300-500 MB
- **Para distribuição:** Comprimir com 7-Zip reduz para ~100 MB

### Como Comprimir:
```
Clique direito na pasta VideoDownloader_Instalavel/
→ 7-Zip (ou WinRAR)
→ "Adicionar ao arquivo"
→ Formato: .7z (melhor compressão)
```

---

## 🧪 Testar o Instalável

Antes de distribuir:

1. **Na mesma máquina:**
   - Abra a pasta `VideoDownloader_Instalavel/`
   - Duplo clique em `EXECUTAR.bat`
   - Teste fazer um download

2. **Em outro PC:**
   - Copie a pasta para um pendrive
   - Teste no outro computador
   - Confirme que funciona

---

## ⚙️ Customizações Avançadas

### Alterar Nome/Ícone do Executável:

Edite o arquivo `video_downloader.spec`:
```python
exe = EXE(
    ...
    name='MeuNome',  # ← Mude aqui
    icon='caminho/para/icone.ico',  # ← Adicione ícone
    ...
)
```

Depois regenere o instalável.

---

## 📝 Arquivos Criados

| Arquivo | Função |
|---------|--------|
| `VideoDownloader_Instalavel/` | Pasta com tudo pronto para distribuir |
| `build/` | Arquivos temporários (pode deletar) |
| `dist/` | Executável compilado (pode deletar) |
| `video_downloader.spec` | Configuração PyInstaller (pode deletar) |

---

## 🔒 Segurança

✓ **Sem vírus ou malware**  
✓ **Código totalmente aberto** - você pode verificar `video_downloader.py`  
✓ **Usa yt-dlp** - biblioteca confiável e open-source  
✓ **Não coleta dados** - opera 100% localmente  

---

## 🎉 Próximos Passos

1. **Gere o instalável** rodando este script
2. **Distribua a pasta** `VideoDownloader_Instalavel/` 
3. **Qualquer pessoa** pode usar em qualquer Windows!

---

## 💡 Dicas

- **Comprima em .7z** para reduzir tamanho na distribuição
- **Teste em outro PC** antes de enviar para outros usuários
- **Mantenha pasta original** em caso de precisar regenerar
- **Atualize regularmente** quando adicionar novos recursos

---

## ❓ Dúvidas?

Veja arquivos incluídos:
- `README.md` - Documentação geral
- `INSTRUÇÕES.txt` - Guia de uso
- `LEIA-ME.txt` - Informações do instalável

---

**Versão:** 1.0  
**Última Atualização:** 2026-04-24  
**Python:** 3.7+  
**PyInstaller:** Versão mais recente
