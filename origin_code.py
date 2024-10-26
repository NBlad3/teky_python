def check_barcode(barcode):
    a = 0
    for i in range(0, 11, 2):
        a += int(barcode[i])

    b = 0
    for i in range(1, 12, 2):
        b += int(barcode[i])

    d = a + 3 * b

    if d % 10 != 0:
        f = 10 - d % 10
    else:
        f = 0

    return f == int(barcode[12])  

def get_origin(barcode, origin_codes):
    prefix = barcode[:3]
    for country, codes in origin_codes.items():
        if prefix in codes:
            return country
    return 'Unknown'

def load_origin_codes(filename):
    origin_codes = {}
    with open(filename, 'r') as f:
        for line in f:
            country, codes = line.strip().split(':')
            codes_list = [code.strip() for code in codes.split(',')]
            origin_codes[country] = codes_list
    return origin_codes

def rw_barcode():
    results = {}
    
    origin_codes = load_origin_codes("origin_code.txt")
    
    with open("barcode.txt", "r") as rfile:
        for line in rfile:
            barcode = line.strip()  
            if len(barcode) == 13 and barcode.isdigit():  
                is_valid = check_barcode(barcode)
                if is_valid:    
                    origin = get_origin(barcode, origin_codes)
                    results[barcode] = f'yes {origin}'
                else:
                    results[barcode] = 'no'
            else:
                results[barcode] = 'no'  

    with open("barcode_validation.txt", "w") as wfile:
        for barcode, result in results.items():
            wfile.write(f"{barcode} - {result}\n")

rw_barcode()

