#the calculating part of the skills test
from pyscript import display, document

def createorder(e):
    document.getElementById("output").innerHTML = ""

    c1 = document.getElementById("pizza1")
    c2 = document.getElementById("pizza2")
    c3 = document.getElementById("pizza3")
    c4 = document.getElementById("pizza4")
 

    p1 = float(c1.value) * int(c1.checked)
    p2 = float(c2.value) * int(c2.checked)
    p3 = float(c3.value) * int(c3.checked)
    p4 = float(c4.value) * int(c4.checked)
    
    subtotal = round(p1 + p2 + p3 + p4)
    vat = round(subtotal * 0.12)
    total = round(subtotal + vat)

    display(f'Subtotal: PHP {subtotal}', target="output", append=False) 
    display(f'VAT: PHP {vat}', target="output", append=True)
    display(f'Total: PHP {total}', target="output", append=True)
