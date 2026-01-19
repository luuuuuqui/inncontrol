# CDU04 – Listar Quartos

**Descrição:** Permite visualizar todos os quartos cadastrados no sistema.

**Ator Primário:** Administrador ou Recepcionista.

**Pré-condições:**  

- O usuário deve estar logado no sistema.

**Pós-condições:**  

- A lista de quartos é exibida.

## Fluxo Principal

1. O usuário acessa a opção "Quarto" no menu lateral e seleciona a aba "Listar".
2. O sistema exibe uma tabela com todos os quartos cadastrados, mostrando ID, Tipo, Bloco e Número.
3. Se não houver quartos, exibe mensagem informativa.

## Fluxos de Exceção

- **FE1 – Nenhum quarto encontrado:**  
  Se não existir nenhum quarto cadastrado, o sistema exibirá uma mensagem informando que não há quartos.

(Notas: Filtros por tipo e disponibilidade não estão implementados no código atual.)
