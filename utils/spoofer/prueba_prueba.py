# from scapy.all import sniff, IP, TCP

# # Contador para limitar la cantidad de paquetes procesados
# packet_count = 0

# # Función de callback para procesar cada paquete capturado
# def process_packet(packet):
#     global packet_count
#     if packet.haslayer(IP):
#         packet_count += 1
#         # Obtener los campos necesarios
#         sttl = packet[IP].ttl
#         dttl = packet.ttl
#         start_time = packet.time
#         last_time = packet.time
#         # Calcular tiempos de conexión TCP
#         syn_time = None
#         syn_ack_time = None
#         ack_time = None
#         if packet.haslayer(TCP):
#             if packet[TCP].flags == 'S':  # Paquete SYN
#                 syn_time = packet.time
#             elif packet[TCP].flags == 'SA':  # Paquete SYN-ACK
#                 syn_ack_time = packet.time
#             elif packet[TCP].flags == 'A':  # Paquete ACK
#                 ack_time = packet.time
#         # Imprimir la información de cada paquete
#         print(f"Packet {packet_count}:")
#         print(f"STTL: {sttl}")
#         print(f"DTTL: {dttl}")
#         print(f"Start Time: {start_time}")
#         print(f"Last Time: {last_time}")
#         print(f"SYN Time: {syn_time}")
#         print(f"SYN-ACK Time: {syn_ack_time}")
#         print(f"ACK Time: {ack_time}")

import scapy

print(scapy.__version__)


# # Capturar paquetes en la red
# print("Iniciando captura de paquetes...")
# sniff(prn=process_packet, filter="tcp", count=10)
