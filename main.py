import os

def vel_localidade(vel:float):
    pass

def vel_fora_localidade(vel:float):
    pass

def vel_autoestrada(vel:float):
    pass

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
    
    velocidade = float(input("\nIntroduza a velocidade a que circulava o veículo").strip())
    
    match loc:
        case 1: vel_localidade()
        case 2: vel_fora_localidade()
        case 3: vel_autoestrada()