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



out_resultado = widgets.Output()

# Widgets para el RF1: Inicio de turno
txt_cajero = widgets.Text(description='Cajero:', placeholder='Nombre o código')
int_tope = widgets.IntText(value=0, description='Tope Max:')
btn_iniciar = widgets.Button(description="Iniciar Turno", button_style='success')

# Widgets para el RF2, RF3, RF4: Atención de clientes
# Se usa Text en lugar de Int para permitir la palabra "FIN" o el "0"
txt_monto = widgets.Text(description='Monto Recibido:', placeholder='Monto, 0 o FIN', style={'description_width': 'initial'})
btn_cobrar = widgets.Button(description="Registrar Pago", button_style='primary')
btn_fin_cola = widgets.Button(description="Fin de Cola (Cerrar)", button_style='danger')

# Deshabilitar controles de pago hasta que inicie el turno
txt_monto.disabled = True
btn_cobrar.disabled = True
btn_fin_cola.disabled = True



def iniciar_turno(b):
    with out_resultado:
        clear_output()
        cajero = txt_cajero.value.strip()
        tope = int_tope.value
        
        if not cajero:
            print("Error: Debe ingresar el nombre del cajero.")
            return
            
        if tope <= 0:
            print(" Error: El tope debe ser un número mayor que cero.")
            return

        # Inicializar estado
        estado_caja["cajero"] = cajero
        estado_caja["tope"] = tope
        estado_caja["recaudo_total"] = 0
        estado_caja["transacciones"] = 0
        estado_caja["activa"] = True
        estado_caja["motivo_cierre"] = ""

        # Habilitar/Deshabilitar interfaz
        txt_cajero.disabled = True
        int_tope.disabled = True
        btn_iniciar.disabled = True
        
        txt_monto.disabled = False
        btn_cobrar.disabled = False
        btn_fin_cola.disabled = False
        
        print(f"Turno iniciado para el cajero {cajero}. Tope: {formatear_moneda(tope)}")
        print("Esperando clientes...")

btn_iniciar.on_click(iniciar_turno)