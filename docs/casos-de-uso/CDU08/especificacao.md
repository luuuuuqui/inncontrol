# CDU08 – Cadastrar Serviços Adicionais

**Descrição:** Permite que o administrador cadastre novos serviços ou produtos adicionais (como itens de frigobar ou lavanderia) que serão oferecidos aos hóspedes.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O administrador deve estar logado no sistema.

**Pós-condições:** 
- O novo serviço adicional fica disponível para ser lançado em consumos de reservas.

## Fluxo Principal

1. O administrador acessa a opção "Adicionais" no menu lateral.
2. O sistema exibe a interface de gerenciamento e o administrador seleciona a aba "Inserir".
3. O administrador informa a descrição do serviço e o valor unitário.
4. O administrador confirma o cadastro clicando no botão "Inserir".
5. O sistema valida se a descrição foi preenchida, se o valor é válido e se o item já não existe.
6. O sistema salva o novo serviço adicional.
7. O sistema exibe uma mensagem de sucesso e limpa os campos para um novo cadastro.

## Fluxos de Exceção

- **FE1 – Dados inválidos:** Se o administrador deixar a descrição em branco ou informar um valor negativo, o sistema exibirá uma mensagem de erro solicitando a correção.

- **FE2 – Serviço já existente:** Se o administrador tentar cadastrar um serviço com uma descrição que já exista (mesmo com letras maiúsculas ou minúsculas diferentes), o sistema informará que o item já está cadastrado.