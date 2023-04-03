# CRUD Python

Este é o repositório da API básica em Python para teste de vaga Fullstack na Globo. O projeto consiste em uma API que permite a criação, leitura, atualização e exclusão de inscrições para o BBB24.

## Iniciar projeto

Para iniciar o projeto, siga as seguintes instruções:

1. Clone o repositório em sua máquina local e entrar no projeto .

```bash
git clone https://github.com/odenirdev/py-crud && cd ./py-crud
```

2. Certifique-se de ter as dependências do projeto instaladas

```bash
poetry install
```

3. Inicie a API com o comando

```bash
uvicorn server:app --reload
```

## Dependências

As dependências do projeto são gerenciadas pelo gerenciador de pacotes **poetry** e podem ser encontradas no arquivo "pyproject.toml". Algumas das dependências incluem:

-   FastAPI: um framework web em Python para construção de APIs de alta performance;
-   uvicorn: um servidor web ASGI de alta performance;
-   Pydantic: uma biblioteca para validação de dados e serialização de modelos em Python;
-   SQLAlchemy: uma biblioteca para interagir com bancos de dados relacionais em Python;
-   pytest: uma biblioteca de testes para escrever e executar testes em Python.

## Arquitetura do projeto

O projeto utiliza a arquitetura limpa (Clean Architecture), que consiste em três camadas: apresentação, domínio e infraestrutura. Na camada de apresentação estão os controllers, na de domínio as entidades e use cases, e na de infraestrutura os adaptadores para comunicação com o banco de dados, validação de dados e interface HTTP. Essa abordagem torna o código mais modular e independente de frameworks externos, facilitando a escrita de testes automatizados.

![The Clean Code Blog](https://blog.cleancoder.com/uncle-bob/images/2012-08-13-the-clean-architecture/CleanArchitecture.jpg)

Foi utilizado o framework FastAPI na camada de infraestrutura para implementar a interface HTTP da API do projeto. O FastAPI é um framework moderno e eficiente para construção de APIs em Python, que oferece uma sintaxe simples e intuitiva para a definição de rotas, validação de dados e documentação automática. Ele é construído sobre o framework Starlette e utiliza a biblioteca Pydantic para validação de dados. O uso do FastAPI facilita o desenvolvimento e a manutenção da API, tornando-a mais rápida e segura.

O uso do FastAPI em conjunto com o Pydantic permite a geração automática de documentação Swagger e Try Out da API, tornando-a mais fácil de ser utilizada e testada. A documentação pode ser acessada por meio de um navegador web, utilizando o endereço http://localhost:8000/docs, após a inicialização do servidor. Com isso, é possível verificar as rotas disponíveis, seus parâmetros e retornos, além de realizar testes diretamente pela documentação gerada. Essa funcionalidade facilita a integração da API com outras aplicações e torna o processo de desenvolvimento mais ágil.

Criado com 💚 por [Odenir Gomes](https://github.com/odenirdev)
