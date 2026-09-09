
from pyscript import display, document

def createorder(e):
    document.getElementById("output").innerHTML = ""

    a1 = document.getElementById("pizza1")
    a2 = document.getElementById("pizza2")
    a3 = document.getElementById("pizza3")
    a4 = document.getElementById("pizza4")
 

    p1 = float(a1.value) * int(a1.checked)
    p2 = float(a2.value) * int(a2.checked)
    p3 = float(a3.value) * int(a3.checked)
    p4 = float(a4.value) * int(a4.checked)
    
    subtotal = round(p1 + p2 + p3 + p4)
    vat = round(subtotal * 0.12)
    total = round(subtotal + vat)

    display(f'Subtotal: PHP {subtotal}', target="output", append=False) 
    display(f'VAT: PHP {vat}', target="output", append=True)
    display(f'Total: PHP {total}', target="output", append=True)
