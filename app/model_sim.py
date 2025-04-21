def interpretar(prompt):
    prompt = prompt.lower()
    if "transferir" in prompt:
        if "$" in prompt or "pesos" in prompt:
            return "💳 Transferencia realizada con éxito."
        else:
            return "⚠️ Por favor indica un monto válido."
    elif "saldo" in prompt:
        return "💰 Tu saldo es de $9,300.00."
    else:
        return "🤔 Lo siento, no entendí tu solicitud."