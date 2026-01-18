# CDU03 – Cadastrar Quarto

**Ator Primário:** Administrador.  
**Descrição:** Permite que o administrador cadastre um novo quarto no sistema.  
**Pré-condições:**  
    - O usuário deve estar logado como Administrador.  
    - Deve existir ao menos um bloco cadastrado.  
    - Deve existir ao menos um tipo de quarto cadastrado.  

**Pós-condições:** O quarto será cadastrado no sistema.

## Fluxo Principal

1. O administrador acessa o sistema com login de administrador.

2. O administrador seleciona o item "Gerenciar Quartos" no menu da barra lateral.

3. O sistema exibe a interface de gerenciamento de quartos.

4. O administrador seleciona a aba "Cadastrar Quarto".

5. O administrador insere as informações do quarto (ex: número, bloco, tipo de quarto, capacidade).

6. O administrador clica no botão "Inserir".

7. O sistema valida os atributos, insere o novo quarto no banco de dados e exibe uma mensagem de confirmação.

## Fluxos De Exceção

- **FE1 – Dados inválidos:**  
  7. Caso o administrador insira dados inválidos (ex: bloco inexistente, tipo de quarto não selecionadosistema exibirá uma mensagem de erro e não realizará o cadastro.

- **FE2 – Dados repetidos:**  
  7. Caso o administrador tenha inserido algum dado repetido (ex: o mesmo número de quarto no mesmo bloco), o sistema exibirá uma mensagem de erro avisando que já existe um quarto com o mesmo número e não realizará o cadastro.
