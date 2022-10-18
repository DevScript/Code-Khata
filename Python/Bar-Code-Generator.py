# Generating Barcodes in Python
# you need to install a specific package to generate barcode
# following command can be used to install barcode package (Note PIP must be installed)
# pip install python-barcode

import barcode                          # here we are importing barcode library 
z=barcode.get_barcode_class('ean13')    # here we are calling barcode class and we want a bar code of ean13 so we called its functionality or siply its inner class 
x=z('1112345678910')                    # here we have declared a variable x for storing our barcode value it can be any numeric value (EAN13 must have 12 figures atleast )
BR=x.save('MY_Bar_Code')                # here we are saving our generated barcode in a default SVG formate 
