from scapy.all import sniff, IP, TCP, UDP, ICMP

# Contador para limitar la cantidad de paquetes procesados
packet_count = 0

# Número de paquete: IP origen -> IP destino Protocolo: Puerto origen -> Puerto destino Tipo de tráfico

# Donde:
# - "Número de paquete" es un contador que indica el orden del paquete capturado.
# - "IP origen" es la dirección IP de origen del paquete.
# - "IP destino" es la dirección IP de destino del paquete.
# - "Protocolo" indica el protocolo utilizado (TCP, UDP, ICMP, etc.).
# - "Puerto origen" es el puerto de origen del paquete.
# - "Puerto destino" es el puerto de destino del paquete.
# - "Tipo de tráfico" indica el tipo de tráfico capturado (TCP, UDP, ICMP).

# Función de callback para procesar cada paquete capturado
def process_packet(packet):
    global packet_count
    if packet.haslayer(IP):
        packet_count += 1
        # Número de paquete, IP fuente, IP destino
        print(f"{packet_count}  | {packet[IP].src} -> {packet[IP].dst}", end=" ")

        if packet.haslayer(TCP):
            # Protocolo TCP, puerto origen, puerto destino
            print(f"|  TCP: {packet[TCP].sport} -> {packet[TCP].dport}", end=" ")

        elif packet.haslayer(UDP):
            # Protocolo UDP, puerto origen, puerto destino
            print(f"|  UDP: {packet[UDP].sport} -> {packet[UDP].dport}", end=" ")

        elif packet.haslayer(ICMP):
            # Protocolo ICMP, tipo, código
            print(f"| ICMP: {packet[ICMP].type}/{packet[ICMP].code}", end=" ")

        print(f" | {packet.payload} {len(packet)} {packet.time} {packet.id}", end = " ")

        # Dirección MAC de origen y destino
        print(f" | {packet.src} {packet.dst}", end = " ")

        # Información sobre la interfaz de red
        print(f" | {packet.sniffed_on}")

        # # Tipo de tráfico
        # if packet.haslayer(TCP):
        #     print(" |  TCP | ")
        # elif packet.haslayer(UDP):
        #     print(" |  UDP | ")
        # elif packet.haslayer(ICMP):
        #     print(" | ICMP | ")
        # else:
        #     print("Otro")

# Capturar paquetes en la red
print("Iniciando captura de paquetes...")
sniff(prn=process_packet)
