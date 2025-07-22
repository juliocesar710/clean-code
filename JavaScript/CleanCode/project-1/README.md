# Exemplo de código limpo em JavaScript

Este exemplo de código limpo em JavaScript demonstra a importância da limpeza e organização do código. Ele apresenta um exemplo de código limpo que usa a sintaxe moderna do JavaScript e segue os princípios da Clean Code.

# Estrutura de pastas

```
project-1/
├── src/
│   ├── index.js
│   ├── components/
│   │   ├── evalutesStudents.js
|   |── services/
|   |    |──calculatesAverage.js
|   |    |──checkApproval.js
|   tests/
├──   ├── calculatesAverage.js
└── README.md
```

Uma estrutura simples mas segue o principio de Open Close Principle, onde está aberto para novas funcionalidades e fechado para novas alterações.

# Código limpo

Lógica de cálculo de média e aprovação de estudantes: estão nos serviços `calculatesAverage.js` e `checkApproval.js`. Estes serviços são chamados pelo componente `evalutesStudents.js` que é responsável por exibir a média e a aprovação dos estudantes.

`index.js` é o ponto de entrada do projeto e chama os serviços para calcular a média e a aprovação dos estudantes.