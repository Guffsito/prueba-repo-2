from datetime import date


def mensaje() -> str:
    return f"Prueba 2 funcionando. Hoy es {date.today():%d/%m/%Y}."


if __name__ == "__main__":
    print(mensaje())
