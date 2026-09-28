# 📦 Control de Caja - PagaYa S.A.S.

# Integrantes
Darwin samuel Machuca Gonzalez   01251152024
Bladimir Ferney Bermudez Toloza  01251152013


# Material dado por el Profesor 

Preparcial:[https://drive.google.com/file/d/1H77uJ2qrU2XkWag7ZYZHTHwSWYPgf_jl/view?usp=sharing]

Este repositorio contiene el módulo de control de caja desarrollado en Python para la empresa recaudadora de pagos PagaYa S.A.S. El sistema gestiona el ingreso de dinero durante el turno de un cajero y cuenta con un mecanismo de suspensión por seguridad al alcanzar un tope de efectivo máximo.


## 🚀 Características Principales (Requerimientos Funcionales)

- **RF1 - Inicio de turno:** Configuración del identificador del cajero y validación estricta del tope máximo de recaudo (> 0).
- **RF2 - Atención de clientes:** Bucle continuo de recaudo y conteo de transacciones exitosas.
- **RF3 - Validación de montos:** Rechazo automático de montos negativos, ceros o valores no numéricos sin interrumpir la ejecución.
- **RF4 - Suspensión por seguridad:** Bloqueo automático de la caja al alcanzar o superar el tope de recaudo establecido.
- **RF5 - Cierre manual por fin de cola:** Opción de finalizar el turno ingresando `0` o la palabra `FIN`.
- **RF6 - Reporte final detallado:** Resumen del turno que incluye total recaudado, promedio por transacción, motivo de cierre y formateo de moneda colombiana (COP).

## 🛠️ Tecnologías y Ejecución

- **Lenguaje:** Python 3.x
- **Entorno recomendado:** Google Colab o cualquier terminal local.

**Para ejecutar localmente:**
1. Clona este repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/nombre-del-repositorio.git](https://github.com/tu-usuario/nombre-del-repositorio.git)