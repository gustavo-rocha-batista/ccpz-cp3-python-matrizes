temperaturas = [[28, 31, 34, 33],
                [25, 27, 29, 28],
                [32, 35, 36, 34],
                [24, 26, 25, 27]]
sala_maior_regs = 0
maior_regs = -1
for index, sala in enumerate(temperaturas):
    media = 0
    reg_criticos = 0

    for temperatura in sala:
        media += temperatura
        if temperatura >= 33:
            reg_criticos+=1

    if reg_criticos > maior_regs:
        maior_regs = reg_criticos
        sala_maior_regs = index + 1

    media /= len(sala)

    print(f"Sala {index + 1}")
    print(f"Média: {media}")
    print(f"Registros críticos: {reg_criticos}")
    print()

print(f"Sala com maior risco: {sala_maior_regs}")