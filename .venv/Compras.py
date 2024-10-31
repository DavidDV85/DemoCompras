import tkinter as tk
import locale

locale.setlocale( locale.LC_ALL, '' )
# Create the main window
root = tk.Tk()
root.geometry("600x350")  # Set window size
root.title("Compras en línea")  # Set window title

text_pUnitario = tk.StringVar() # Create a StringVar to associate with the label
text_pUnitario.set("Precio Unitario")
# Create the label widget with all options
label_pUnitario = tk.Label(root, textvariable=text_pUnitario, bg="white", height=1, width=15,
  font=("Arial", 10, "bold"), cursor="hand2", fg="black", padx=2, pady=2, underline=0, wraplength=150
)
# Pack the label into the window
label_pUnitario.pack(pady=10)  # Add some padding to the top
label_pUnitario.place(x=50,y=40)

text_total = tk.StringVar() # Create a StringVar to associate with the label
text_total.set("Total a pagar: $000.0")
# Create the label widget with all options
label_total = tk.Label(root,
 textvariable=text_total, bg="white", height=1, width=25,
  font=("Arial", 10, "bold"), cursor="hand2", fg="black", padx=2, pady=2,
 underline=0, wraplength=250
)
# Pack the label into the window
label_total.pack(pady=5)  # Add some padding to the top
label_total.place(x=300,y=80)

text_leyenda_punitario = tk.StringVar() # Create a StringVar to associate with the label
text_leyenda_punitario.set("$000.0")
entry_pUnitario = tk.Entry(textvariable=text_leyenda_punitario,justify=tk.RIGHT,state="readonly")
entry_pUnitario.place(x=300, y=40) # Posicionarla en la ventana.

def get_total(info):
 print("Edittext ",info)
 print("info ", text_leyenda_cantidadProd.get())
 if (text_leyenda_cantidadProd.get().replace('.','',1).isdigit() ):
  unitario = float(entry_pUnitario.get().replace("$",""))
  cantidad = float(entry_cantidadProd.get())
  total = unitario * cantidad
  #cadena = f"Total a pagar: ${total:.2f}"
  cadena = f"Total a pagar: {locale.currency(total, grouping=True)}"

  text_total.set(cadena.format(total))
 else:
  text_total.set("Solo se permiten numeros")

text_leyenda_cantidadProd = tk.StringVar() # Create a StringVar to associate with the label
entry_cantidadProd = tk.Entry(justify=tk.RIGHT, textvariable=text_leyenda_cantidadProd)
entry_cantidadProd.bind("<KeyRelease>", get_total)
entry_cantidadProd.place(x=50, y=80) # Posicionarla en la ventana.

# Create the list of options
producto_lista = ["Seleccionar un Producto","Jicama", "Naranja", "Manzana", "Pera", "Calabaza"]
producto_precio_lista = [0,10.5, 15.6, 20.4, 7.6, 96.36]

def get_valor(selection):
 for index, valor in enumerate(producto_lista):
  if (selection == valor):
   precio=producto_precio_lista[index]
   text_leyenda_punitario.set(f"${precio}")
 return None

valor_interno = tk.StringVar(root) # selected in OptionMenu
valor_interno.set("Seleccionar un Producto") # Set the default value of the variable
# Create the optionmenu widget and passing the options_list and value_inside to it.
comboBox = tk.OptionMenu(root, valor_interno, *producto_lista, command=get_valor)
comboBox.pack(pady=10)  # Add some padding to the top
comboBox.place(x=170,y=5)

# Run the main event loop
root.mainloop()