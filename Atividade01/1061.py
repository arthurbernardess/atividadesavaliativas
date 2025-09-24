dia1 = int(input().split()[1])
h1, m1, s1 = map(int, input().split(" : "))

dia2 = int(input().split()[1])
h2, m2, s2 = map(int, input().split(" : "))

t1 = dia1 * 86400 + h1 * 3600 + m1 * 60 + s1
t2 = dia2 * 86400 + h2 * 3600 + m2 * 60 + s2

tempo = t2 - t1

dias = tempo // 86400
tempo %= 86400
horas = tempo // 3600
tempo %= 3600
minutos = tempo // 60
segundos = tempo % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")