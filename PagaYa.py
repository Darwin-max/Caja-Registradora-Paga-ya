#Nombre: Darwin Samuel Machuca Gonzalez Codigo:01251152024
#Nombre: Bladimir Ferney Bermúdez Toloza Codigo:01251152013

import ipywidgets as widgets
from IPython.display import display, clear_output

estado_caja = {
    "cajero": "",
    "tope": 0,
    "recaudo_total": 0,
    "transacciones": 0,
    "activa": False,
    "motivo_cierre": ""
}



def formatear_moneda(valor):
    return f"${valor:,.0f}".replace(",", ".")

def formatear_promedio(valor):
    texto = f"${valor:,.2f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")

def generar_reporte():
    cajero = estado_caja["cajero"]
    tope = estado_caja["tope"]
    transacciones = estado_caja["transacciones"]
    recaudo = estado_caja["recaudo_total"]
    motivo = estado_caja["motivo_cierre"]
    
    promedio = (recaudo / transacciones) if transacciones > 0 else 0.0

    print("\n===== REPORTE DE TURNO =====")
    print(f"Cajero:               {cajero}")
    print(f"Tope asignado:        {formatear_moneda(tope)}")
    print(f"Transacciones:        {transacciones}")
    print(f"Recaudo total:        {formatear_moneda(recaudo)}")
    print(f"Promedio/transacción: {formatear_promedio(promedio)}")
    print(f"Motivo de cierre:     {motivo}")