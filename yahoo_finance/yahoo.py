import yfinance as yf
import pandas as pd

data = yf.download("TSLA", start="2023-01-01", end="2024-01-01")
print(data.head())

# Crear un objeto para Apple (AAPL)
aapl = yf.Ticker("AAPL")

# Obtener información general
info = aapl.info

# Mostrar algunos datos clave
print(f"Nombre: {info['longName']}")
print(f"Sector: {info['sector']}")
print(f"Industria: {info['industry']}")
print(f"Capitalización de mercado: {info['marketCap']}")
print(f"Precio actual: {info['currentPrice']}")
