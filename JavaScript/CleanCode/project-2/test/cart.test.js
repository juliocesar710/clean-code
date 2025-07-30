import { describe, it, expect, beforeEach } from "vitest";
import Cart from "../src/cart.js";

describe("Cart", () => {
  let cart;

  beforeEach(() => {
    cart = new Cart();
  });

  it("should add a product to the cart", () => {
    cart.addItem("Camisa", 50, 2);
    expect(cart.listItems()).toHaveLength(1);
    expect(cart.listItems()[0]).toEqual({
      name: "Camisa",
      price: 50,
      quantity: 2,
    });
  });

  it("should remove a product from the cart", () => {
    cart.addItem("Camisa", 50, 2);
    cart.addItem("Meia", 10, 3);
    cart.removeItem("Camisa");
    expect(cart.listItems()).toHaveLength(1);
    expect(cart.listItems()[0].name).toBe("Meia");
  });

  it("should calculate the total price of the cart", () => {
    cart.addItem("Camisa", 50, 2); // 100
    cart.addItem("Meia", 10, 3); // 30
    expect(cart.calculateSubtotal()).toBe(130);
  });

  it("should apply a discount to the total price", () => {
    cart.addItem("Camisa", 100, 1);
    const total = cart.applyDiscount("DESC10"); // 10% de desconto
    expect(total).toBe(90);
  });

  it("should return total without discount if coupon is invalid", () => {
    cart.addItem("Calça", 200, 1);
    const total = cart.applyDiscount("INVALIDO");
    expect(total).toBe(200);
  });
});
