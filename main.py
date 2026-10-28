
CATEGORIES = {
    "Delivery",
    "Shipping",
    "Refund",
    "Payment",
    "Cancellation",
    "Defect",
    "Return",
    "Account",
    "Unknown",
}

CLASSIFICATION_PROMPT = """
You are a customer query classification system for an e-commerce company.

Classify the customer's query into exactly ONE category:

Delivery: Order has not arrived or delivery is delayed.
Shipping: Package is in transit or has shipping/tracking issues.
Refund: Customer wants money back or asks about refund status.
Payment: Payment failure, duplicate charge, or billing issue.
Cancellation: Customer wants to cancel an order.
Defect: Product is broken, damaged, faulty, or not working.
Return: Customer wants to send back a product.
Account: Login, password, or account access issue.
Unknown: Query does not fit any category or cannot be classified.

Rules:
1. Identify the customer's main intention.
2. Choose only one category from the list.
3. Do not guess missing information.
4. If no category clearly applies, choose Unknown.
5. Output exactly one category word.
6. Do not include explanations or punctuation.

Customer query: {query}

Output:
"""


def classify_query(query):
    """Classify a customer query using keyword-based rules."""

    text = query.lower()

    # Account issues
    if any(word in text for word in [
        "login", "log in", "password", "account"
    ]):
        return "Account"

    # Cancellation
    if any(word in text for word in [
        "cancel", "cancellation"
    ]):
        return "Cancellation"

    # Refund
    if any(word in text for word in [
        "refund", "money back", "reimburse"
    ]):
        return "Refund"

    # Payment
    if any(word in text for word in [
        "payment", "paid twice", "double charge",
        "charged twice", "deducted twice", "billing"
    ]):
        return "Payment"

    # Defective products
    if any(word in text for word in [
        "broken", "defective", "damaged", "faulty",
        "not working"
    ]):
        return "Defect"

    # Returns
    if any(word in text for word in [
        "return", "send back", "exchange"
    ]):
        return "Return"

    # Shipping and tracking
    if any(word in text for word in [
        "in transit", "tracking", "shipped",
        "shipping", "stuck in transit"
    ]):
        return "Shipping"

    # Delivery
    if any(word in text for word in [
        "not arrived", "hasn't arrived",
        "has not arrived", "late delivery",
        "delivery", "where is my order"
    ]):
        return "Delivery"

    return "Unknown"


if __name__ == "__main__":
    print("Customer Query Classification")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Enter customer query: ").strip()

        if query.lower() == "exit":
            break

        if not query:
            print("Unknown")
            continue

        result = classify_query(query)
        print(result)
