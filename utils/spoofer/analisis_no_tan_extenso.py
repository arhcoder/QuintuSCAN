from scapy.all import *
import time

# Función para calcular la tasa de bits de destino
def calculate_dload(packet):
    global last_time, last_size
    current_time = time.time()
    size = len(packet)
    if last_time is None:
        last_time = current_time
        last_size = size
        return 0.0
    else:
        # Calcular la tasa de bits de destino en bits por segundo
        dload = abs((size - last_size) / (current_time - last_time))
        last_time = current_time
        last_size = size
        return dload

# Función de callback para procesar cada paquete capturado
def process_packet(packet):
    global last_time, last_size
    if IP in packet:
        proto = packet[IP].proto
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Asignar valor 1 si el protocolo es TCP, 2 si es UDP, 3 si es ICMP, 0 si no lo es
        if proto == 6:  # TCP
            protocol_label = "1"
            state = packet[TCP].sprintf('%TCP.flags%')
            sttl = packet[IP].ttl
            swin = packet[TCP].window
            dwin = packet[TCP].options[3][1] if packet[TCP].options and len(packet[TCP].options) > 3 else 0  # Extraer dwin si existe
        elif proto == 17:  # UDP
            protocol_label = "2"
            state = '-'
            sttl = packet[IP].ttl
            swin = 0  # No hay campo de ventana en UDP
            dwin = 0
        elif proto == 1:  # ICMP
            protocol_label = "3"
            state = '-'
            sttl = packet[IP].ttl
            swin = 0  # No hay campo de ventana en ICMP
            dwin = 0
        else:
            protocol_label = "0"
            state = '-'
            sttl = packet[IP].ttl
            swin = 0
            dwin = 0

        if proto == 6:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            # Calcular la tasa de bits de destino
            dload = calculate_dload(packet)
            
            print(f"PROTO: {protocol_label}, IPSRC: {src_ip} : SPORT: {src_port}, IPDST: {dst_ip} : DPORT: {dst_port}, STATE: {state}, STTL: {sttl}, DLOAD: {dload}, SWIN: {swin}, DWIN: {dwin}")
            print()
            print()

        elif proto == 17:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            # Calcular la tasa de bits de destino
            dload = calculate_dload(packet)
            
            print(f"PROTO: {protocol_label}, IPSRC: {src_ip} : SPORT: {src_port}, IPDST: {dst_ip} : DPORT: {dst_port}, STATE: {state}, STTL: {sttl}, DLOAD: {dload}, SWIN: {swin}, DWIN: {dwin}")
            print()
            print()
        
        elif proto == 1:
            src_port = packet[ICMP].sport
            dst_port = packet[ICMP].dport
            # Calcular la tasa de bits de destino
            dload = calculate_dload(packet)

            
            print(f"PROTO: {protocol_label}, IPSRC: {src_ip} : SPORT: {src_port}, IPDST: {dst_ip} : DPORT: {dst_port}, STATE: {state}, STTL: {sttl}, DLOAD: {dload}, SWIN: {swin}, DWIN: {dwin}")
            print()
            print()



# Variable global para el tiempo y tamaño del último paquete
last_time = None
last_size = None

# Capturar paquetes en la red
print("Iniciando captura de paquetes...")
sniff(prn=process_packet, store=0)
