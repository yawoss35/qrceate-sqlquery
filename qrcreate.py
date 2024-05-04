import qrcode
import sys

if len(sys.argv) < 2:
    print("Kullanım: python script.py 'SQL_SORGUSU'")
    sys.exit(1)

sql_query = sys.argv[1]

qr = qrcode.QRCode()
qr.add_data(sql_query)
qr.print_ascii()
