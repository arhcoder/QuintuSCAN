from scapy.all import *

# Función de callback para procesar cada paquete capturado
def process_packet(packet):
    if IP in packet:
        proto = packet[IP].proto
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Asignar valor 1 si el protocolo es TCP, 3 si es UDP, 0 si no lo es
        if proto == 6:  # TCP
            protocol_label = "1"
            state = packet[TCP].sprintf('%TCP.flags%')
            sttl = packet[IP].ttl
        elif proto == 17:  # UDP
            protocol_label = "2"
            state = '-'
            sttl = packet[IP].ttl
        else:
            protocol_label = "0"
            state = '-'
            sttl = packet[IP].ttl

        if proto == 6:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            
            print(f"PROTO: {protocol_label}, IPSRC: {src_ip}:{src_port}, IPDST: {dst_ip}:{dst_port}, STATE: {state}, STTL: {sttl} ")
            print()
            print()

        elif proto == 17:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            
            print(f"PROTO: {protocol_label}, IPSRC: {src_ip}:{src_port}, IPDST: {dst_ip}:{dst_port}, STATE: {state}, STTL: {sttl} ")
            print()
            print()


# Capturar paquetes en la red
print("Iniciando captura de paquetes...")
sniff(prn=process_packet, store=0)
