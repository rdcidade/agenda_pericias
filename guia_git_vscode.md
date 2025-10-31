# 📝 Guia rápido Git/GitHub – VSCode

## 1️⃣ Inicialização e verificação do repositório

```bash
# Verificar repositório remoto
git remote -v

# Verificar status dos arquivos
git status
```

> Confirme que o VSCode mostra o repositório e branch ativos.

---

## 2️⃣ Branches

| Ação | Comando VSCode / Terminal |
|------|---------------------------|
| Criar branch nova | `git checkout -b feature/nova_funcionalidade` ou pelo VSCode (canto inferior esquerdo → Create Branch) |
| Trocar de branch | `git checkout nome-da-branch` ou clicar no nome da branch |
| Listar branches | `git branch` |

💡 **Dica:** Sempre crie uma branch para cada funcionalidade ou correção.

---

## 3️⃣ Fluxo diário de commits

1. Editar arquivos no VSCode.
2. Abrir **Source Control** (`Ctrl + Shift + G`) → adicionar arquivos (`+`) ao commit.
3. Escrever mensagem clara no campo de commit.
4. Clicar em **✔ Commit**.

**Terminal equivalente:**

```bash
git add .
git commit -m "Mensagem clara do commit"
```

---

## 4️⃣ Push para GitHub

- Botão **Sincronizar Mudanças (↕)** no VSCode  
- Ou no terminal:

```bash
git push -u origin nome-da-branch
```

> O `-u` cria o rastreamento da branch remota na primeira vez.

---

## 5️⃣ Pull / Atualizar a branch local

Sempre antes de iniciar uma nova tarefa:

```bash
git pull origin main
```

> Mantém seu código atualizado e evita conflitos.

---

## 6️⃣ Pull Request e integração

1. No GitHub, vá à branch da feature.  
2. Clique em **Pull Request → Compare & Create PR**.  
3. Revise alterações e integre à branch `main`.  

---

## 7️⃣ Dicas finais

- Commit frequente e mensagens curtas ajudam no histórico.  
- Nunca commite arquivos do `venv`, `.env` ou `__pycache__` (o `.gitignore` cuida disso).  
- Sempre atualize `main` antes de criar novas branches.  
- Use a aba **Graph** ou `git log --oneline --graph` para visualizar histórico.
