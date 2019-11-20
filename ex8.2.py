def calc_hypo(a, b):
    if type(a) in (int, float) and type(b) in (int, float): 
        hypo = (a**2 + b**2)**0.5
        return hypo
    else:
        return "Not a number"

print(calc_hypo(3, 4))



