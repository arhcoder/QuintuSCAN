from scapy.all import sniff, TCP

# Función de callback para procesar cada paquete capturado
def process_packet(packet):
    if packet.haslayer(TCP):
        # Obtener el valor de sttl
        if 'IP' in packet:
            sttl = packet['IP'].ttl
        else:
            sttl = None  # No hay información de ttl en el paquete
        
        # Obtener otros campos requeridos
        dttl = None  # No disponible en el paquete capturado
        start_time = packet.time
        last_time = packet.time
        tcp_round_trip_time = None
        tcp_setup_time_syn_ack = None
        tcp_setup_time_ack = None
        state_value = packet[TCP].sprintf("%TCP.flags%")
        is_ftp_login = None
        ct_ftp_cmd = None
        service = None

        # Mostrar los resultados
        print(f"sttl: {sttl}")
        print(f"dttl: {dttl}")
        print(f"Start Time: {start_time}")
        print(f"Last Time: {last_time}")
        print(f"TCP Round Trip Time: {tcp_round_trip_time}")
        print(f"TCP Setup Time SYN-ACK: {tcp_setup_time_syn_ack}")
        print(f"TCP Setup Time ACK: {tcp_setup_time_ack}")
        print(f"State Value: {state_value}")
        print(f"FTP Session Accessed: {is_ftp_login}")
        print(f"FTP Session Command Count: {ct_ftp_cmd}")
        print(f"Service: {service}")
        print()

# Capturar paquetes en la red
print("Iniciando captura de paquetes...")
sniff(prn=process_packet)
