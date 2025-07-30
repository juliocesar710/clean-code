import Cart from './src/cart.js';

const cart = new Cart();

cart.addItem("Camisa", 50, 2);
cart.addItem("Calça", 120, 1);
cart.addItem("Meia", 10, 5);

console.log("🛒 Carrinho atual:");
console.table(cart.listItems());

const subtotal = cart.calculateSubtotal();
console.log("Subtotal: R$", subtotal.toFixed(2));

const totalComDesconto = cart.applyDiscount("DESC10");
console.log("Total com desconto (DESC10): R$", totalComDesconto.toFixed(2));

cart.removeItem("Meia");

console.log("\nApós remover 'Meia':");
console.table(cart.listItems());
console.log("Novo subtotal: R$", cart.calculateSubtotal().toFixed(2));
