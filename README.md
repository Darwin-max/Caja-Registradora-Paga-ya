# 📦 Sistema de Caja - PagaYa S.A.S.

# Integrantes
Darwin samuel Machuca Gonzalez   01251152024
Bladimir Ferney Bermudez Toloza  01251152013

Este repositorio contiene el módulo de control de caja desarrollado en **Python** (utilizando `ipywidgets` para la interfaz gráfica interactiva) para la empresa recaudadora de pagos PagaYa S.A.S. El sistema gestiona el ingreso de dinero durante el turno de un cajero y cuenta con un mecanismo de suspensión automática por seguridad al alcanzar un tope de efectivo.

## 🎓 Información Académica

| | |
|---|---|
| **Asignatura** | Programación 1 |
| **Docente** | Ing. Carlos Carrascal |


## 📚 Material de Referencia
* **Preparcial:** [Ver documento original](https://drive.google.com/file/d/1H77uJ2qrU2XkWag7ZYZHTHwSWYPgf_jl/view?usp=sharing)


## Diagrama de flujo
![Diagrama de Flujo de Datos](DFD%20PREPARCIAL.png)


## 📝 Descripción del Problema y Reglas de Negocio

El sistema de caja funciona bajo los siguientes requerimientos funcionales:

1. **Inicio de turno:** El cajero inicia turno ingresando su nombre y un **tope máximo de dinero** (mayor que 0).
2. **Atención:** Se atiende a los clientes ingresando el monto de cada transacción en la interfaz.
3. **Validación:** Los montos menores o iguales a `0` se rechazan y no afectan los saldos.
4. **Suspensión por tope:** Si el recaudo total alcanza o supera el tope, la caja se bloquea automáticamente con el motivo **"Tope alcanzado"**.
5. **Cierre manual:** Si se ingresa el monto `0`, la palabra `FIN`, o se presiona el botón "Fin de Cola", el turno termina con el motivo **"Fin de cola"**.
6. **Reporte:** Al finalizar, la pantalla imprime un reporte completo con el resumen de transacciones, promedios y el motivo del cierre.

---

## 📂 Contenido del Repositorio

```text
.
├── README.md           # Documentación del proyecto (Este archivo)
├── DFD Preparcial 
├── pagaYa.ipynb        # Cuaderno de Jupyter con la interfaz gráfica completa
└── PagaYa.py           # Script original de respaldo