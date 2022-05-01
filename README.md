
# 🤖 Bot de comentários no Instagram 

Um bot com funcionalidade de logar e comentar automaticamente em uma lista de posts retirados de uma tag do Instagram.


## 🛠 Funcionalidades

- Curtir em posts.
- Comentar em posts.
- Pegar links de posts de uma tag especifica.
- Login automático.
- Digitação semelhante a humana.
- Tempo aleatório entre comentários enviados.
- Possível lista com comentários ilimitados.


## ⚙️ Configuração

Passo 1° - Tenha instalado o navegador firefox, para uso do [geckodriver](https://github.com/mozilla/geckodriver).

Passo 2° - Instale a biblioteca [selenium](https://www.selenium.dev/selenium/docs/api/py/).

```bash
$ pip install selenium
```

Passo 3° - Mude as informações de login no codigo.
```py
/* 
Coloque seu usuario e senha, e qual a tag que o bot ira pegar os posts 
- Colocar usuario sem @
- Colocar hashtag sem #
*/
bot = InstagramBot("user", "senha", "tag")
```

Passo 4° - Altere a lista de comentarios de acordo com seu gosto.
```py
comments = [

"que post bacana",
"amei o seu post",
"veja meu instagram"
           ] 
```

## 🖊 Exemplo de uso

```py
bot = InstagramBot("DARKnx", "012345678", "trend")
```
 

## 🚀 Tecnologias usadas
- python
- selenium
- firefox geckodriver
