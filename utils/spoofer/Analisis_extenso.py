from scapy.all import sniff, IP, TCP, UDP, ICMP

# Contador para limitar la cantidad de paquetes procesados
packet_count = 0

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
            #Protocolo UDP, puerto origen, puerto destino
            print(f"|  UDP: {packet[UDP].sport} -> {packet[UDP].dport}", end=" ")

        elif packet.haslayer(ICMP):
            #çProtocolo ICMP, tipo, código
            print(f"| ICMP: {packet[ICMP].type}/{packet[ICMP].code}", end=" ")

        print(f" |PAYLOAD  -> {packet.payload} LEN -> {len(packet)} TIME -> {packet.time} ID -> {packet.id}", end = " ")
        
        print(f" | {packet.src} {packet.dst}", end = " ")

        # Otros campos adicionales
        print(f" | Duration: {packet.time} | Bytes from Source: {len(packet.payload)} | Bytes to Destination: {len(packet.payload)}", end=" ")
        print(f" | TTL Source: {packet.ttl} | TTL Destination: {packet[IP].ttl} | Retransmitted Source: {packet.len} | Retransmitted Destination: {packet.len}", end=" ")
        print(f" | Source BPS: {len(packet.payload)*8/packet.time} | Destination BPS: {len(packet.payload)*8/packet.time}", end=" ")
        print(f" | Source Packet Count: {packet.len} | Destination Packet Count: {packet.len}", end=" ")
        print(f" | Source TCP Window: {packet.len} | Destination TCP Window: {packet.len}", end=" ")
        print(f" | Source TCP Base Seq: {packet.len} | Destination TCP Base Seq: {packet.len}", end=" ")
        print(f" | Source Flow Packet Size Mean: {packet.len} | Destination Flow Packet Size Mean: {packet.len}", end=" ")
        print(f" | Pipelined Depth: {packet.len} | Uncompressed Content Size: {packet.len}", end=" ")
        print(f" | Source Jitter: {packet.len} | Destination Jitter: {packet.len}", end=" ")
        print(f" | Record Start Time: {packet.len} | Record Last Time: {packet.len}", end=" ")
        print(f" | Source Interpacket Arrival Time: {packet.len} | Destination Interpacket Arrival Time: {packet.len}", end=" ")
        print(f" | TCP Setup RTT: {packet.len} | TCP Setup Time SYN-ACK: {packet.len} | TCP Setup Time SYN-ACK: {packet.len}", end=" ")
        print(f" | IP and Port Equality: {packet.len} | State No.: {packet.len}", end=" ")
        print(f" | HTTP Method Flows: {packet.len} | FTP Login: {packet.len}", end=" ")
        print(f" | FTP Command Flows: {packet.len} | Service and Source Address Connections: {packet.len}", end=" ")
        print(f" | Service and Destination Address Connections: {packet.len} | Destination Address Connections: {packet.len}", end=" ")
        print(f" | Source Address Connections: {packet.len} | Source Address and Destination Port Connections: {packet.len}", end=" ")
        print(f" | Destination Address and Source Port Connections: {packet.len} | Source and Destination Address Connections: {packet.len}", end=" ")

        print()
        print()

# Capturar paquetes en la red
print("Iniciando captura de paquetes...")
sniff(prn=process_packet)
