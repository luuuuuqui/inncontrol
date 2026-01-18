# CDU21 – Histórico de Estadias

**Descrição:** Permite visualizar o histórico de estadias de um hóspede no sistema.

**Ator Primário:** Administrador ou Recepcionista.

**Pré-condições:**  
- O usuário deve estar logado no sistema.
- O hóspede deve estar cadastrado no sistema.

**Pós-condições:**  
- O histórico de estadias do hóspede é exibido.

## Fluxo Principal

1. O usuário acessa a opção Histórico de Estadias no sistema.
2. O sistema exibe o campo de pesquisa de hóspede.
3. O usuário seleciona ou informa o hóspede desejado.
4. O sistema busca o histórico de estadias do hóspede.
5. O sistema exibe a lista de estadias realizadas.

## Fluxos de Exceção

- **FE1 – Hóspede inexistente:**  
  Se o hóspede informado não existir no sistema, o sistema exibirá uma mensagem de erro.

- **FE2 – Nenhum histórico encontrado:**  
  Se o hóspede não possuir estadias registradas, o sistema exibirá uma mensagem informando que não há histórico disponível.
