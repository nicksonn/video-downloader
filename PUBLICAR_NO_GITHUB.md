# 🚀 Como Publicar no GitHub

## 📋 Pré-requisitos

1. **Conta GitHub** - [Criar em github.com](https://github.com/signup)
2. **Git instalado** - [Download aqui](https://git-scm.com/download/win)
3. **Esta pasta** - Todos os arquivos já estão prontos

---

## 🎯 Passo 1: Criar Repositório no GitHub

### Online (Via Website)

1. Acesse **[github.com](https://github.com)**
2. Faça login com sua conta
3. Clique em **"+"** (canto superior direito)
4. Selecione **"New repository"**

### Preencha os Dados:

```
Repository name:     video-downloader
Description:         🎬 Download vídeos de TikTok, Instagram, YouTube
Visibility:          Public (ou Private)
Initialize:          NÃO marque nada
```

5. Clique em **"Create repository"**

---

## 💻 Passo 2: Fazer Upload do Código

### Abra PowerShell ou CMD

Navegue para esta pasta:
```powershell
cd "F:\Usuarios\Nickson\Documents\Claude\Projects\Download  Videos"
```

### Inicialize Git

```bash
git init
```

### Configure seu Usuário (primeira vez)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
```

### Adicione Todos os Arquivos

```bash
git add .
```

### Faça o Commit

```bash
git commit -m "Initial commit: Video Downloader v1.0"
```

### Adicione o Repositório Remoto

Substitua `SEU-USUARIO` pelo seu usuário GitHub:

```bash
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/video-downloader.git
git push -u origin main
```

⚠️ **Será pedido seu GitHub username e password (ou token)**

---

## 🔑 Se Pedir Token

GitHub agora pede um **Personal Access Token** ao invés de senha:

1. Abra https://github.com/settings/tokens
2. Clique em **"Generate new token"**
3. Dê um nome: `git-push`
4. Marque: `repo` (todas as opções)
5. Clique em **"Generate token"**
6. **Copie o token** (aparece uma única vez!)
7. Cole no terminal quando pedir "password"

---

## ✅ Verificar Upload

Acesse **https://github.com/SEU-USUARIO/video-downloader**

Você deve ver:
- ✅ Todos os arquivos
- ✅ README com descrição
- ✅ Histórico de commits

---

## 🏷️ Passo 3: Criar Release (Opcional)

Para que outros possam baixar a ferramenta:

### Via GitHub Website

1. Vá para seu repositório
2. Clique em **"Releases"** (lado direito)
3. Clique em **"Create a new release"**

```
Tag version:     v1.0
Release title:   Video Downloader v1.0
Description:     
  🎬 Ferramenta de download de vídeos
  
  Baixe vídeos de TikTok, Instagram, YouTube
  em melhor qualidade com interface gráfica.
  
  Windows executável incluído!
```

4. **Upload do instalável** (opcional):
   - Clique em "Attach binaries"
   - Selecione `VideoDownloader_Instalavel.zip`

5. Clique **"Publish release"**

---

## 📝 Passo 4: Melhorar Descrição do Repositório

Volte à página principal do repositório:

1. Clique no ⚙️ **Settings**
2. Na seção "About" (lado direito), preencha:

```
Description: 🎬 Download vídeos de TikTok, Instagram, YouTube em melhor qualidade
Website: (deixe em branco ou seu site)
Topics: adicione:
  - video-downloader
  - tiktok
  - instagram
  - youtube
  - python
  - gui
```

---

## 🎨 Bônus: Badge no README

Adicione status badges ao seu `README_GITHUB.md`:

```markdown
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Windows](https://img.shields.io/badge/Platform-Windows-0078D4.svg)]()
[![GitHub release](https://img.shields.io/github/v/release/SEU-USUARIO/video-downloader)](https://github.com/SEU-USUARIO/video-downloader/releases)
```

---

## 🔄 Passo 5: Atualizar Depois

Quando fizer mudanças:

```bash
git add .
git commit -m "Descrevendo a mudança"
git push
```

---

## 📊 Exemplo Completo

Aqui está um exemplo passo a passo:

```powershell
# 1. Entre na pasta
cd "F:\Usuarios\Nickson\Documents\Claude\Projects\Download  Videos"

# 2. Configure git (apenas primeira vez)
git config --global user.name "Nickson"
git config --global user.email "nickson@meiaum.digital"

# 3. Inicialize
git init
git add .
git commit -m "Initial commit: Video Downloader v1.0"

# 4. Adicione repositório remoto
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/video-downloader.git
git push -u origin main
```

---

## ❓ Erros Comuns

### "fatal: not a git repository"
```bash
git init
```

### "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/SEU-USUARIO/video-downloader.git
```

### "authentication failed"
- Use Personal Access Token (veja seção 🔑)
- Verifique username e email no git config

### "fatal: refusing to merge unrelated histories"
```bash
git pull origin main --allow-unrelated-histories
```

---

## 🎉 Próximos Passos

1. ✅ Código no GitHub
2. ✅ Release criado
3. 🚀 Compartilhe o link: `https://github.com/SEU-USUARIO/video-downloader`

**Pronto! Sua ferramenta está publicada!** 🎊

---

## 💡 Dicas

- **Adicione uma imagem** - Print da interface no README
- **Atualize regularmente** - Push de novas features
- **Responda issues** - Comunique com usuários
- **Adicione mais docs** - Wiki, FAQ, examples

---

## 📚 Recursos Úteis

- [GitHub Docs](https://docs.github.com)
- [Git Cheat Sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
- [Markdown Guide](https://www.markdownguide.org/)
- [Shields.io](https://shields.io/) - Para badges

---

**Versão:** 1.0  
**Data:** 2026-04-24  
**Autor:** Seu Nome

Se tiver dúvidas, consulte a [Documentação do GitHub](https://docs.github.com/pt/get-started)
