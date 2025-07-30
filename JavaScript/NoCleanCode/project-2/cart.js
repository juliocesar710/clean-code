let carrinho = [];

function adicionar(nome, preco, quantidade){
    carrinho.push({ nome, preco, quantidade });
}

function remover(nome){
    for (let i = 0; i < carrinho.length; i++) {
        if (carrinho[i].nome === nome) {
            carrinho.splice(i, 1);
            break;
        }
    }
}

function calcula(){
    let subtotal = 0;
    for (let item of carrinho) {
        subtotal += item.preco * item.quantidade;
    }
    return subtotal;
}

function aplicaDesconto(cupom){
    let desconto = 0;

    if( cupom === 'PROMO10') {
        desconto = 0.10; // 10% de desconto
    } else if( cupom === 'PROMO20') {
        desconto = 0.20; // 20% de desconto
    }
    let subtotal = calcula();
    let total = subtotal - (subtotal * desconto);
    return total;
}

adicionar('Camisa', 50, 2);
adicionar('Calça', 100, 1);
adicionar('Tênis', 200, 3);
console.log("Subtotal: R$ " + calcula());
console.log("Total: R$ " + aplicaDesconto("PROMO10"));
remover('Camisa');
console.log("Subtotal: R$ " + calcula());
console.log("Total: R$ " + aplicaDesconto("PROMO20"));
console.log("Carrinho:", carrinho); 