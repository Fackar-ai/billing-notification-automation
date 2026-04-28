import time

clients = [
    {"name": "Juan", "phone": "123456", "amount": 100},
    {"name": "Maria", "phone": "789012", "amount": 150},
]

def generate_invoice(client):
    print(f"Generating invoice for {client['name']}...")
    time.sleep(1)
    return f"Invoice_{client['name']}.pdf"

def send_whatsapp(client, invoice):
    print(f"Sending WhatsApp to {client['name']} ({client['phone']})...")
    time.sleep(1)
    print(f"Message: Hello {client['name']}, your invoice is ready: {invoice}")

def process_clients():
    for client in clients:
        invoice = generate_invoice(client)
        send_whatsapp(client, invoice)
        print("-" * 40)

if __name__ == "__main__":
    process_clients()
