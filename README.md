# 📘 **Documentação do Alfabeto e Estruturas da Linguagem Lumina**

---
# 🌟 A ideia por Trás da Linguagem

A Lumina é como uma brincadeira séria — uma linguagem construída como se fosse um mapa da mente humana.  
Cada comando carrega um pequeno gesto cognitivo: **reflect** é pensar em voz alta, **choose** é tomar decisões internas,  
**repeat** é revisitar ideias, **whilethink** é aquele estado de processamento mental contínuo,  
e até mesmo **define** representa o momento em que damos nome e forma a um pensamento.

Ela foi criada para soar familiar, quase emocional, como se programar fosse conversar com a própria consciência.  
Por isso os blocos viram “caminhos”, decisões viram “reflexões”, e variáveis são pedaços nomeados do nosso raciocínio.  
A linguagem toda brinca com a metáfora de que escrever código é organizar ideias dentro da cabeça — só que aqui, a cabeça virou gramática.

Lumina é, no fundo, uma linguagem técnica disfarçada de imaginação estruturada.  
É código, mas também é narrativa interna.  
É lógica, mas com um toque de poesia.  
É a mente humana, traduzida em instruções.

# 1️⃣ **Conceito de Alfabeto da Linguagem**

O **alfabeto de uma linguagem formal** é o conjunto de símbolos terminais que podem aparecer em programas escritos nela.

O alfabeto é composto por:

1. **Palavras reservadas**
2. **Símbolos especiais e operadores**
3. **Delimitadores**
4. **Tipos primitivos**
5. **Identificadores**
6. **Literais**
7. **Comentários**
8. **Espaços em branco**

Cada um desses grupos é descrito e exemplificado abaixo.

---

# 2️⃣ **Palavras Reservadas**

As palavras reservadas **não podem ser usadas como nomes de variáveis**, pois possuem significado sintático próprio.

| Palavra         | Função                                             |
| --------------- | -------------------------------------------------- |
| `define`        | Declaração de variável                             |
| `reflect`       | Impressão de valores (equivalente a `print`)       |
| `input`         | Leitura de entrada do usuário                      |
| `choose`        | Início de estrutura condicional                    |
| `path`          | Corpo do caminho principal do choose               |
| `or`            | Operador lógico OR **OU** alternativa do choose    |
| `and`           | Operador lógico AND                                |
| `not`           | Negação lógica                                     |
| `repeat`        | Estrutura semelhante ao `for`                      |
| `whilethink`    | Estrutura semelhante ao `while`                    |
| `return`        | Palavra prevista, mas ainda não usada na gramática, utilizada para retorno de funções e métodos |
| `true`, `false` | Literais booleanos                                 |

### ✔️ Exemplos

```lumina
define idade: int = 20;
reflect "Olá!";
choose (idade > 18) path { ... } or { ... }
repeat (define i: int = 0; i < idade; i = i + 1;) { ... }
whilethink (idade > 0) { ... }
```

---

# 3️⃣ **Tipos Primitivos**

| Tipo Lumina | Significado          |
| ----------- | -------------------- |
| `int`       | Número inteiro       |
| `float`     | Número real (double) |
| `text`      | Cadeia de caracteres |

### ✔️ Exemplo

```lumina
define nome: text = "João";
define idade: int = 25;
define fator: float = 2.5;
```

---

# 4️⃣ **Operadores**

### 🔹 Aritméticos

| Token | Uso           |
| ----- | ------------- |
| `+`   | soma          |
| `-`   | subtração     |
| `*`   | multiplicação |
| `/`   | divisão       |

**Exemplo:**

```lumina
resultado = a + b * 2;
```

---

### 🔹 Relacionais

| Token | Significado    |
| ----- | -------------- |
| `<`   | menor que      |
| `>`   | maior que      |
| `<=`  | menor ou igual |
| `>=`  | maior ou igual |
| `==`  | igual          |
| `!=`  | diferente      |

**Exemplo:**

```lumina
choose (idade >= 18) path { ... }
```

---

### 🔹 Lógicos

| Token | Significado |
| ----- | ----------- |
| `and` | conjunção   |
| `or`  | disjunção   |
| `not` | negação     |

**Exemplo:**

```lumina
if (a > 5 and b < 10 or not c)
```

---

### 🔹 Atribuição

| Token | Significado |
| ----- | ----------- |
| `=`   | atribuição  |

**Exemplo:**

```lumina
x = 3 * 2;
```

---

### 🔹 Declaração tipada

| Token | Significado         |
| ----- | ------------------- |
| `:`   | separa nome do tipo |

**Exemplo:**

```lumina
define nome: text = "Ana";
```

---

# 5️⃣ **Delimitadores**

| Token   | Uso                                                     |
| ------- | ------------------------------------------------------- |
| `(` `)` | Agrupamento e chamadas `choose(...)` `repeat(...)`, etc |
| `{` `}` | Blocos de código                                        |
| `;`     | Final de instrução                                      |
| `,`     | Separador (pouco usado na versão atual)                 |

### ✔️ Exemplos

```lumina
reflect (a + b); # parênteses opcionais
```

---

# 6️⃣ **Identificadores (ID)**

Sintaxe:

```
[a-zA-Z_][a-zA-Z0-9_]*
```

Ou seja:

* começam com **letra ou _**
* continuam com **letras, dígitos ou _**

✔️ Exemplos válidos:

```txt
x
valor1
_nome
idadeUsuario
```

❌ Exemplos inválidos:

```
1abc
@var
```

---

# 7️⃣ **Literais**

### 🔹 Números (`NUMBER`)

```
[0-9]+ ('.' [0-9]+)?
```

Suportam:

* inteiros: `42`
* floats: `3.14`

### 🔹 Strings (`STRING`)

Delimitadas por **aspas duplas** `"..."`
Podem conter escape:

```
"texto"
"linha \"entre aspas\" "
```

---

# 8️⃣ **Comentários**

```
# tudo até o fim da linha
```

Exemplo:

```lumina
# Isto é um comentário
reflect "Olá Lumina!";
```

O compilador **ignora completamente** comentários.

---

# 9️⃣ **Espaços em branco**

São ignorados (exceto em strings):

```
espaco, tab, \r, \n
```

---

# 🔟 **Resumo do Alfabeto (Terminais)**

### ✔️ Palavras Reservadas

```
define reflect input choose path or and not repeat whilethink return
true false
```

### ✔️ Tipos

```
int float text
```

### ✔️ Operadores

```
+ - * / = : < > <= >= == !=
```

### ✔️ Delimitadores

```
( ) { } ; ,
```

### ✔️ Literais

```
NUMBER
STRING
```

### ✔️ Identificadores

```
[a-zA-Z_][a-zA-Z0-9_]*
```

### ✔️ Comentários

```
# comentário até a quebra de linha
```

---