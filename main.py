import os

def vel_localidade(vel:float):
    if vel >= 120: return 320
    elif vel >= 90: return 120
    elif vel > 50: return 60

def vel_fora_localidade(vel:float):
    if vel >= 120: return 120
    elif vel > 90: return 60

def vel_autoestrada(vel:float):
    if vel > 175: return 360
    elif vel > 150: return 120
    elif vel > 120: return 60

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Onde circulava o veículo?"
          "\n[1] - Localidade"
          "\n[2] - Fora de localidade"
          "\n[3] - Autoestrada")
    try:
        loc = int(input("\nIntroduza o local: ").strip())
    except ValueError:
        print("\nErro! Input deve ser numérico!")
        continue
    except Exception as e:
        print(f"\nErro: {e}")
        continue
    if loc not in range(1,4):
        print("\nErro! Seleção fora das opções apresentadas!")
        continue
    
    velocidade = float(input("\nIntroduza a velocidade a que circulava o veículo: ").strip())
    
    if velocidade < 50: print("\nNão há multa a pagar.")
    else:
        match loc:
            case 1: multa = vel_localidade(velocidade)
            case 2: multa = vel_fora_localidade(velocidade)
            case 3: multa = vel_autoestrada(velocidade)
        print(f"\nA multa a pagar é de {multa}€")
    
    while True:
        continuar = input("\nDeseja continuar? [S/N]\n> ").strip().capitalize()
        match continuar:
            case "S":break
            case "N":break
            case _: print("\nErro! Input inválido!")
    if continuar == "N": break