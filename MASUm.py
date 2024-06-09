def gtokg(g):
    return g / 1000

def kgtog(kg):
    return kg * 1000

def kgtot(kg):
    return kg / 1000

def ttokg(t):
    return t * 1000

def gtot(g):
    kg = gtokg(g)
    t = kgtot(kg)
    return t

def ttog(t):
    kg = ttokg(t)
    g = kgtog(kg)
    return g

def mmtog(mg):
    return mg / 1000

def gtomm(g):
    return g * 1000

def ttodt(t):
    return t * 10

def dttot(dt):
    return dt / 10

def main():
    weight = float(input("Gib das Gewicht ein: "))
    unit = input("Gib die Einheit ein (mg, g, kg, t, dz): ")

    if unit == "mg":
        result_g = mmtog(weight)
        result_kg = gtokg(result_g)
        result_t = kgtot(result_kg)
        result_dz = ttodt(result_t)
        print(weight, "mg entsprechen", result_g, "g,", result_kg, "kg,", result_t, "t und", result_dz, "dz")
    elif unit == "g":
        result_mg = gtomm(weight)
        result_kg = gtokg(weight)
        result_t = kgtot(result_kg)
        result_dz = ttodt(result_t)
        print(weight, "g entsprechen", result_mg, "mg,", result_kg, "kg,", result_t, "t und", result_dz, "dz")
    elif unit == "kg":
        result_g = kgtog(weight)
        result_mg = gtomm(result_g)
        result_t = kgtot(weight)
        result_dz = ttodt(result_t)
        print(weight, "kg entsprechen", result_mg, "mg,", result_g, "g,", result_t, "t und", result_dz, "dz")
    elif unit == "t":
        result_kg = ttokg(weight)
        result_g = kgtog(result_kg)
        result_mg = gtomm(result_g)
        result_dz = ttodt(weight)
        print(weight, "t entsprechen", result_mg, "mg,", result_g, "g,", result_kg, "kg und", result_dz, "dz")
    elif unit == "dz":
        result_t = dttot(weight)
        result_kg = ttokg(result_t)
        result_g = kgtog(result_kg)
        result_mg = gtomm(result_g)
        print(weight, "dz entsprechen", result_mg, "mg,", result_g, "g,", result_kg, "kg und", result_t, "t")
    else:
        print("Ungültige Einheit.")

if __name__ == "__main__":
    main()