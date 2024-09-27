from ecommerce.models import Product, Order

def process_response(input_text):
    input_text = input_text.lower()  # Normalize input to lowercase

    # Check for product inquiries
    if "products" in input_text or "what do you have" in input_text:
        products = Product.objects.all()  # Fetch all products
        if products.exists():
            product_list = "\n".join([f"{product.name}: ${product.price}" for product in products])
            return f"Available products:\n{product_list}"
        else:
            return "No products available at the moment."

    # Check for order status inquiries
    elif "order status" in input_text:
        order_id = extract_order_id(input_text)  # Implement a function to extract order ID
        try:
            order = Order.objects.get(id=order_id)  # Fetch order by ID
            return f"Order {order.id} status: {order.order_status}."
        except Order.DoesNotExist:
            return "Sorry, I couldn't find that order."

    # Provide general help
    elif "help" in input_text:
        return "How can I assist you today? You can ask about products or check your order status."

    # Default response for unrecognized input
    return "I'm sorry, I didn't understand that. Please ask about products or your order status."

def extract_order_id(input_text):
    # Placeholder function to extract an order ID from input text
    # For simplicity, returning a static ID; implement extraction logic as needed
    return 1  # Change this to actual extraction logic if needed
