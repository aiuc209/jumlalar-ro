def katta_harflar(jumlalar):
    yangi_jumlalar = []
    for jumla in jumlalar:
        sozlar = jumla.split()
        yangi_jumla = sozlar[0].capitalize() + ' ' + ' '.join(sozlar[1:-1]) + ' ' + sozlar[-1].capitalize()
        yangi_jumlalar.append(yangi_jumla)
    return yangi_jumlalar

jumlalar = ["men yaxshi oqiyman", "siz yomon oqiyssiz", "biz yaxshi oqiygapmiz"]
print(katta_harflar(jumlalar))
