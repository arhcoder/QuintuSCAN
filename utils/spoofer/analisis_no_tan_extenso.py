from scapy.all import sniff, TCP

# Función de callback para procesar cada paquete capturado
def process_packet(packet):
    if packet.haslayer(TCP):
        # Calcular el tiempo de ida y vuelta de la conexión TCP
        if hasattr(packet[TCP], 'sent_time') and packet[TCP].sent_time is not None:
            tcp_round_trip_time = packet.time - packet[TCP].sent_time
        else:
            tcp_round_trip_time = None

        # Obtener otros campos requeridos
        start_time = packet.time
        last_time = packet.time
        tcp_setup_time_syn_ack = None  # No se puede calcular sin más información
        tcp_setup_time_ack = None  # No se puede calcular sin más información
        state_value = packet[TCP].sprintf("%TCP.flags%")
        ftp_session_accessed = None  # No se tiene información sobre una sesión FTP
        ftp_session_command_count = None  # No se tiene información sobre una sesión FTP
        service = None  # No se tiene información sobre el servicio

        # Mostrar los resultados
        print(f"Start Time: {start_time}")
        print(f"Last Time: {last_time}")
        print(f"TCP Round Trip Time: {tcp_round_trip_time}")
        print(f"TCP Setup Time SYN-ACK: {tcp_setup_time_syn_ack}")
        print(f"TCP Setup Time ACK: {tcp_setup_time_ack}")
        print(f"State Value: {state_value}")
        print(f"FTP Session Accessed: {ftp_session_accessed}")
        print(f"FTP Session Command Count: {ftp_session_command_count}")
        print(f"Service: {service}")
        print()

# Capturar paquetes en la red
print("Iniciando captura de paquetes...")
sniff(prn=process_packet)
