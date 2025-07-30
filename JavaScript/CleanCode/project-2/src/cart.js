class Cart {
  constructor() {
    this.items = [];
  }

  addItem(name, price, quantity) {
    this.items.push({ name, price, quantity });
  }

  removeItem(name) {
    this.items = this.items.filter((item) => item.name !== name);
  }

  calculateSubtotal() {
    return this.items.reduce((total, item) => total + item.price * item.quantity, 0);
  }

  getDiscountRate(coupon) {
    const coupons = {
      DESC10: 0.1,
      DESC20: 0.2,
    };
    return coupons[coupon] || 0;
  }

  applyDiscount(coupon) {
    const rate = this.getDiscountRate(coupon);
    const subtotal = this.calculateSubtotal();
    return subtotal - subtotal * rate;
  }

  listItems() {
    return this.items;
  }
}

export default Cart;
