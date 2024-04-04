from scapy.all import *
import time

# Variables globales para mantener el estado de las conexiones y el tiempo del último paquete
last_time = None
last_size = None

# Variables globales para mantener el estado de las conexiones
connection_states = {}
src_dport_counts = {}
dst_sport_counts = {}
dst_src_counts = {}

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

# Función para actualizar los recuentos de conexiones
def update_connection_counts(packet, src_ip, dst_ip, src_port, dst_port, proto):
    global connection_states, src_dport_counts, dst_sport_counts, dst_src_counts

    # Actualizar los recuentos de conexiones según el protocolo
    if proto == 6:  # TCP
        tcp_layer = packet.getlayer(TCP)
        if tcp_layer:
            flags = tcp_layer.sprintf('%TCP.flags%')
            connection_states[(src_ip, dst_ip)] = flags
            src_dport_counts[(src_ip, dst_port)] = src_dport_counts.get((src_ip, dst_port), 0) + 1
            dst_sport_counts[(dst_ip, src_port)] = dst_sport_counts.get((dst_ip, src_port), 0) + 1
            dst_src_counts[(src_ip, dst_ip)] = dst_src_counts.get((src_ip, dst_ip), 0) + 1
            
            # Incrementar los contadores de tiempo de vida del estado de la conexión
            ttl = packet[IP].ttl if IP in packet else 0
            connection_states[(src_ip, dst_ip, "ct_state_ttl")] = ttl
            
            connection_states[(src_ip, dst_ip, "ct_src_dport_ltm")] = tcp_layer.sport
            connection_states[(src_ip, dst_ip, "ct_dst_sport_ltm")] = tcp_layer.dport
            connection_states[(src_ip, dst_ip, "ct_dst_src_ltm")] = dst_src_counts[(src_ip, dst_ip)]
            
    elif proto == 17:  # UDP
        connection_states[(src_ip, dst_ip)] = 0  # Estado 0 para UDP
        src_dport_counts[(src_ip, dst_port)] = src_dport_counts.get((src_ip, dst_port), 0) + 1
        dst_sport_counts[(dst_ip, src_port)] = dst_sport_counts.get((dst_ip, src_port), 0) + 1
        dst_src_counts[(src_ip, dst_ip)] = dst_src_counts.get((src_ip, dst_ip), 0) + 1
    elif proto == 1:  # ICMP
        connection_states[(src_ip, dst_ip)] = 0  # Estado 0 para ICMP
        src_dport_counts[(src_ip, dst_port)] = src_dport_counts.get((src_ip, dst_port), 0) + 1
        dst_sport_counts[(dst_ip, src_port)] = dst_sport_counts.get((dst_ip, src_port), 0) + 1
        dst_src_counts[(src_ip, dst_ip)] = dst_src_counts.get((src_ip, dst_ip), 0) + 1

# Función de callback para procesar cada paquete capturado
def process_packet(packet):
    global last_time, last_size

    printed_something = False  # Variable auxiliar para verificar si algo se ha impreso

    if IP in packet:
        proto = packet[IP].proto
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Asignar valor 1 si el protocolo es TCP, 2 si es UDP, 3 si es ICMP, 0 si no lo es
        if proto == 6:  # TCP
            protocol_label = "1"
            state = packet[TCP].sprintf('%TCP.flags%')
            state_INT = 1 if state == "INT" else 0
            state_CON = 1 if state == "CON" else 0
            state_FIN = 1 if state == "FIN" else 0
            sttl = packet[IP].ttl if IP in packet else 0
            swin = packet[TCP].window
            dwin = packet[TCP].options[3][1] if packet[TCP].options and len(packet[TCP].options) > 3 else 0  # Extraer dwin si existe
        elif proto == 17:  # UDP
            protocol_label = "2"
            sttl = packet[IP].ttl if IP in packet else 0
            swin = 0  # No hay campo de ventana en UDP
            dwin = 0
            state = None
            state_INT = None
            state_CON = None
            state_FIN = None
        elif proto == 1:  # ICMP
            protocol_label = "3"
            sttl = packet[IP].ttl if IP in packet else 0
            swin = 0  # No hay campo de ventana en ICMP
            dwin = 0
            state = None
            state_INT = None
            state_CON = None
            state_FIN = None
        else:
            protocol_label = "0"
            state_code = 0
            state_INT = 0
            state_CON = 0
            state_FIN = 0
            sttl = packet[IP].ttl if IP in packet else 0
            swin = 0
            dwin = 0
            state = None
            state_INT = None
            state_CON = None
            state_FIN = None

        if proto == 6:#TCP
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            # Calcular la tasa de bits de destino
            dload = calculate_dload(packet)
            
            # Actualizar los recuentos de conexiones
            update_connection_counts(packet, src_ip, dst_ip, src_port, dst_port, proto)
            
            # Imprimir los detalles del paquete si algo se imprime
            if not printed_something:
                printed_something = True
                print("Tráfico anómalo")
            #print(f"PROTO: {protocol_label}, IPSRC: {src_ip} : SPORT: {src_port}, IPDST: {dst_ip} : DPORT: {dst_port}, STATE: {state}, STTL: {sttl}, DLOAD: {dload}, SWIN: {swin}, DWIN: {dwin}, STATE_INT: {state_INT}, STATE_CON: {state_CON}, CT_STATE_TTL: {connection_states.get((src_ip, dst_ip, 'ct_state_ttl'), STATE_FIN: {state_FIN}")
            #print()
            #print()

        elif proto == 17:#UDP
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            # Calcular la tasa de bits de destino
            dload = calculate_dload(packet)
            
            # Actualizar los recuentos de conexiones
            update_connection_counts(packet, src_ip, dst_ip, src_port, dst_port, proto)
            
            # Imprimir los detalles del paquete si algo se imprime
            if not printed_something:
                printed_something = True
                print("Tráfico anómalo")
                data = {
                    "sttl": sttl,
                    "state_INT": state_INT,
                    "ct_state_ttl": src_ip,
                    "proto_tcp": proto,
                    "swin": swin,
                    "dload": dload,
                    "state_CON": state_CON,
                    "dwin": dwin,
                    "state_FIN": state_FIN
                }
            #print(f"PROTO: {protocol_label}, IPSRC: {src_ip} : SPORT: {src_port}, IPDST: {dst_ip} : DPORT: {dst_port}, STATE: {state}, STTL: {sttl}, DLOAD: {dload}, SWIN: {swin}, DWIN: {dwin}, STATE_INT: {state_INT}, STATE_CON: {state_CON}, STATE_FIN: {state_FIN}")
            #print()
            #print()
        
        elif proto == 1:#ICMP
            src_port = packet[ICMP].sport
            dst_port = packet[ICMP].dport
            # Calcular la tasa de bits de destino
            dload = calculate_dload(packet)

            # Actualizar los recuentos de conexiones
            update_connection_counts(packet, src_ip, dst_ip, src_port, dst_port, proto)

            # Imprimir los detalles del paquete si algo se imprime
            if not printed_something:
                printed_something = True
                print("Tráfico anómalo")
            #print(f"PROTO: {protocol_label}, IPSRC: {src_ip} : SPORT: {src_port}, IPDST: {dst_ip} : DPORT: {dst_port}, STATE: {state}, STTL: {sttl}, DLOAD: {dload}, SWIN: {swin}, DWIN: {dwin}, STATE_INT: {state_INT}, STATE_CON: {state_CON}, STATE_FIN: {state_FIN}")
            #print()
            #print()

    # Si nada se ha impreso, imprimir "FALSE"
    if not printed_something:
        print("Tráfico regular")

# Iniciar la captura de paquetes
sniff(prn=process_packet, store=0)
