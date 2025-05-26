import os

def rename_files(folder_path):
    # Cria um dicionário para rastrear os nomes já encontrados
    name_count = {}
    file_count = 0
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Ignora os dois primeiros arquivos
            if file_count < 2:
                file_count += 1
                continue
            
            # Pega os 10 primeiros caracteres do nome do arquivo
            first_10_chars = file[:10]
            
            # Verifica se esse nome já foi encontrado antes
            if first_10_chars in name_count:
                # Se sim, incrementa o contador
                name_count[first_10_chars] += 1
                new_name = f"{first_10_chars} ({name_count[first_10_chars]}).txt"
            else:
                # Se não, cria um novo contador
                name_count[first_10_chars] = 1
                new_name = f"{first_10_chars}.txt"
            
            # Renomeia o arquivo
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)
            print(f"Arquivo renomeado: {old_path} -> {new_path}")

# Caminho da pasta "2003"
folder_path = r"C:\Users\carla\OneDrive\Área de Trabalho\06 Temer\2018"
rename_files(folder_path)