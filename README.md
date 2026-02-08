# Analisa-Textos-arquivo-com-IA-usando-LangChain-e-Groq

- Este projeto demonstra como utilizar Inteligência Artificial generativa para analisar automaticamente conteúdos textuais armazenados em arquivos locais.
- A aplicação lê um arquivo .txt, constrói um prompt estruturado com LangChain PromptTemplate e envia o conteúdo para um LLM da Groq, retornando um resumo e os principais pontos do texto.

- O foco do projeto é aprender a integrar IA em fluxos reais de backend, indo além de simples chamadas de API.

Como a IA responde
- A IA não acessa arquivos diretamente.
- O fluxo funciona assim:
  1. O Python lê o conteúdo do arquivo dados.txt
  2. O texto é inserido dinamicamente em um PromptTemplate
  3. O prompt final é enviado ao modelo de linguagem
  4. A IA retorna:
    * Um resumo do texto
    * Uma lista com os principais pontos abordados
  - Isso demonstra claramente o conceito de arquivo → texto → prompt → resposta da IA.

Tecnologias e conceitos utilizados
- Python
- LangChain
- Groq LLM (LLaMA 3.1)
- Prompt Engineering
- PromptTemplat
- Leitura de arquivos
- Arquitetura de prompts
- Integração com modelos de linguagem
- Uso de variáveis de ambiente (.env)

Estrutura do projeto
projeto/
├── dados.txt
├── analisador_texto_ia.py
├── .env
└── README.md

dados.txt: arquivo de texto analisado pela IA
analisador_texto_ia.py: script principal
.env: contém a chave da API da Groq
README.md: documentação do projeto

Como executar o projeto
  1.) Clone o repositório:

     git clone https://github.com/seu-usuario/Analisa-Textos-arquivo-com-IA-usando-LangChain-e-Groq

  2.) Crie e ative um ambiente virtual (opcional, mas recomendado)
  3.) Instale as dependências:

     pip install langchain langchain-groq python-dotenv

  4.) Crie o arquivo .env e adicione sua chave:

     GROQ_API_KEY=sua_chave_aqui

  5.) Execute o script:

     python analisador_texto_ia.py

Alterando o texto analisado
- Para analisar outro conteúdo, basta editar o arquivo dados.txt com o texto desejado.
- Nenhuma modificação no código é necessária, pois o prompt é dinâmico.

Resumo profissional
  - Projeto educacional focado em análise de textos com IA, utilizando LangChain, PromptTemplate e modelos LLM da Groq, aplicando conceitos de prompt engineering, leitura de arquivos e integração prática com inteligência artificial em Python.

