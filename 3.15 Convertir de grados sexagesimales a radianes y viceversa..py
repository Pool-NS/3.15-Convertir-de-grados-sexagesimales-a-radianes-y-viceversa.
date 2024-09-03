import tkinter as tk
from tkinter import ttk
import math


def convertir():
    try:
        valor = float(entrada_valor.get())
        if combo_desde.get() == "Grados":
            resultado = valor * (math.pi / 180)
            unidad_resultado = "Radianes"
        else:
            resultado = valor * (180 / math.pi)
            unidad_resultado = "Grados"

        etiqueta_resultado.config(text=f"Resultado: {resultado:.4f} {unidad_resultado}")
        actualizar_explicacion(valor, resultado, combo_desde.get(), unidad_resultado)
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingrese un número válido")


def actualizar_explicacion(valor_entrada, valor_salida, desde, hacia):
    if desde == "Grados":
        explicacion = f"Conversión de Grados a Radianes:\n\n"
        explicacion += f"{valor_entrada}° × (π / 180) = {valor_salida:.4f} rad\n\n"
        explicacion += "Explicación:\n"
        explicacion += "1. Multiplicamos el ángulo en grados por π/180\n"
        explicacion += f"2. π/180 ≈ {math.pi / 180:.6f}\n"
        explicacion += f"3. {valor_entrada} × {math.pi / 180:.6f} = {valor_salida:.4f}"
    else:
        explicacion = f"Conversión de Radianes a Grados:\n\n"
        explicacion += f"{valor_entrada} rad × (180 / π) = {valor_salida:.4f}°\n\n"
        explicacion += "Explicación:\n"
        explicacion += "1. Multiplicamos el ángulo en radianes por 180/π\n"
        explicacion += f"2. 180/π ≈ {180 / math.pi:.6f}\n"
        explicacion += f"3. {valor_entrada} × {180 / math.pi:.6f} = {valor_salida:.4f}"

    texto_explicacion.config(state=tk.NORMAL)
    texto_explicacion.delete(1.0, tk.END)
    texto_explicacion.insert(tk.END, explicacion)
    texto_explicacion.config(state=tk.DISABLED)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Ángulos")
ventana.geometry("400x500")

# Crear y colocar widgets
ttk.Label(ventana, text="Conversor de Ángulos", font=("Arial", 16)).pack(pady=10)

frame_entrada = ttk.Frame(ventana)
frame_entrada.pack(pady=10)

ttk.Label(frame_entrada, text="Valor:").grid(row=0, column=0, padx=5)
entrada_valor = ttk.Entry(frame_entrada)
entrada_valor.grid(row=0, column=1, padx=5)

ttk.Label(frame_entrada, text="Desde:").grid(row=0, column=2, padx=5)
combo_desde = ttk.Combobox(frame_entrada, values=["Grados", "Radianes"], state="readonly")
combo_desde.grid(row=0, column=3, padx=5)
combo_desde.set("Grados")

ttk.Button(ventana, text="Convertir", command=convertir).pack(pady=10)

etiqueta_resultado = ttk.Label(ventana, text="Resultado: ", font=("Arial", 12))
etiqueta_resultado.pack(pady=10)

ttk.Label(ventana, text="Explicación:", font=("Arial", 12)).pack(pady=5)
texto_explicacion = tk.Text(ventana, height=10, width=50, state=tk.DISABLED)
texto_explicacion.pack(pady=10)

# Iniciar el loop de la interfaz gráfica
ventana.mainloop()