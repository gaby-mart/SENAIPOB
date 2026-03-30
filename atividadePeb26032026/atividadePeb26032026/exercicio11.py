xa = float(input("xA superior esquerdo:"))
ya = float(input("yA superior esquerdo:"))
xa2 = float(input("xA inferior direito:"))
ya2 = float(input("yA inferior direito:"))

xb = float(input("xB superior esquerdo:"))
yb = float(input("yB superior esquerdo:"))
xb2 = float(input("xB: inferior direito:"))
yb2 = float(input("yB inferior direito:"))

if xa2 < xb or xa > xb2 or ya2 > yb or ya < ya2:
    print("Os triângulos não se sobrepõem.")
else:
    print("Os triângulos se sobrepõem.")