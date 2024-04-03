import flet as ft
import time
from scapy.all import sniff, IP, TCP, UDP, ICMP
import numpy as np
from winotify import Notification
from flet import *

packet_count = 0

def main(page: ft.Page):
    page.title="El diablo"
    page.bgcolor="white"
    page.scroll="always"
    #page.scroll="always"
    # Contador para limitar la cantidad de paquetes procesados
    numberpack= ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    # Función de callback para procesar cada paquete capturado
    mytable = DataTable(
        #border=ft.border.all(2),
        border_radius=10,
        #vertical_lines=ft.border.BorderSide(3, "blue"),
        horizontal_lines=ft.border.BorderSide(0.5, "black"),
        sort_column_index=0,
        sort_ascending=True,
        heading_row_color=ft.colors.BLACK12,
        heading_row_height=100,
        data_row_color={"hovered": "black"},
        show_checkbox_column=True,
        divider_thickness=0,
        column_spacing=200,
        columns=[
            DataColumn(Text("Número de paquete")),
            DataColumn(Text("Ip fuente")),
            DataColumn(Text("Ip destino")),
        ],
        rows=[]
       # bgcolor="red"
    )
    page.add(mytable)
    def process_packet(packet):
        #time.sleep(1)
        global packet_count
        if packet.haslayer(IP):
            
            packet_count += 1
            # Número de paquete, IP fuente, IP destino
            mytable.rows.append(
                ft.DataRow(
                    cells=[
                       ft.DataCell(ft.Text(f"{packet_count}")),
                       ft.DataCell(ft.Text(f"{packet[IP].src}")),
                       ft.DataCell(ft.Text(f"{packet[IP].dst}")),
                    ],
                ),
            )
            
            numberpack.controls.append(
                ft.Text(f"{packet_count}| {packet[IP].src}-> {packet[IP].dst}")
            )
         
            page.add(numberpack)
            #print(f"{packet_count}  | {packet[IP].src} -> {packet[IP].dst}", end=" ")

            if packet.haslayer(TCP):
                # Protocolo TCP, puerto origen, puerto destino
                numberpack.controls.append(
                    ft.Text(f"| TCP:{packet[TCP].sport}->{packet[TCP].dport}")
                )
                page.add(numberpack)
                #print(f"|  TCP: {packet[TCP].sport} -> {packet[TCP].dport}", end=" ")

            elif packet.haslayer(UDP):
                # Protocolo UDP, puerto origen, puerto destino
                numberpack.controls.append(
                    ft.Text(f"| UDP:{packet[UDP].sport}-> {packet[UDP].dport}")
                )
                page.add(numberpack)
                #print(f"|  UDP: {packet[UDP].sport} -> {packet[UDP].dport}", end=" ")

            elif packet.haslayer(ICMP):
                numberpack.controls.append(
                    ft.Text(f"| ICMP: {packet[ICMP].type}/{packet[ICMP].code}")
                )
                page.add(numberpack)
                # Protocolo ICMP, tipo, código
                #print(f"| ICMP: {packet[ICMP].type}/{packet[ICMP].code}", end=" ")
            num_al= np.random.randint(1,20)
            numberpack.controls.append(
                ft.Text(num_al)
            )
            page.add(numberpack)
            if num_al==1 :
                # Crear una notificación
                toast = Notification(app_id="QuintuScan", 
                            title="Detección de anomalia", 
                            msg="Se ha detectado una anomalia en:", 
                            duration="short",
                            
                            )
                # Agregar un botón a la notificación
                toast.add_actions(label="Ver detalles")
                
                # Mostrar la notificación
                toast.show()
            
            
            numberpack.controls.append(
                ft.Text(f" |PAYLOAD -> {packet.payload} LEN -> {len(packet)} Time -> {packet.time} ID -> {packet.id}")
            )
            #print(f" |PAYLOAD  -> {packet.payload} LEN -> {len(packet)} TIME -> {packet.time} ID -> {packet.id}", end = " ")
            
            # Otros campos adicionales
            #print(f" | Duration: {packet.time} | Bytes from Source: {len(packet.payload)} | Bytes to Destination: {len(packet.payload)}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | Duration: {packet.time} | Bytes from Source: {len(packet.payload)} | Bytes to Destination: {len(packet.payload)}"),
            )
             #print(f" | TTL Source: {packet.ttl} | TTL Destination: {packet[IP].ttl} | Retransmitted Source: {packet.len} | Retransmitted Destination: {packet.len}", end=" "
            numberpack.controls.append(
                ft.Text(f" | TTL Source: {packet.ttl} | TTL Destination: {packet[IP].ttl} | Retransmitted Source: {packet.len} | Retransmitted Destination: {packet.len}")
            )
            #print(f" | Source BPS: {len(packet.payload)*8/packet.time} | Destination BPS: {len(packet.payload)*8/packet.time}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | Source BPS: {len(packet.payload)*8/packet.time} | Destination BPS: {len(packet.payload)*8/packet.time}")
            )
            #print(f" | Source Packet Count: {packet.len} | Destination Packet Count: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | Source Packet Count: {packet.len} | Destination Packet Count: {packet.len}")
            )
            #print(f" | Source TCP Window: {packet.len} | Destination TCP Window: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | Source TCP Window: {packet.len} | Destination TCP Window: {packet.len}")
            )
            #print(f" | Source TCP Base Seq: {packet.len} | Destination TCP Base Seq: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | Source TCP Base Seq: {packet.len} | Destination TCP Base Seq: {packet.len}")
            )
            #print(f" | Source Flow Packet Size Mean: {packet.len} | Destination Flow Packet Size Mean: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | Source Flow Packet Size Mean: {packet.len} | Destination Flow Packet Size Mean: {packet.len}")    
            )
            #print(f" | Pipelined Depth: {packet.len} | Uncompressed Content Size: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | Pipelined Depth: {packet.len} | Uncompressed Content Size: {packet.len}")
            )
            #print(f" | Source Jitter: {packet.len} | Destination Jitter: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | Source Jitter: {packet.len} | Destination Jitter: {packet.len}")
            )
            #print(f" | Record Start Time: {packet.len} | Record Last Time: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | Record Start Time: {packet.len} | Record Last Time: {packet.len}")
            )
            #print(f" | Source Interpacket Arrival Time: {packet.len} | Destination Interpacket Arrival Time: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | Source Interpacket Arrival Time: {packet.len} | Destination Interpacket Arrival Time: {packet.len}")
            )
            #print(f" | TCP Setup RTT: {packet.len} | TCP Setup Time SYN-ACK: {packet.len} | TCP Setup Time SYN-ACK: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | TCP Setup RTT: {packet.len} | TCP Setup Time SYN-ACK: {packet.len} | TCP Setup Time SYN-ACK: {packet.len}")
            )
            #print(f" | IP and Port Equality: {packet.len} | State No.: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | IP and Port Equality: {packet.len} | State No.: {packet.len}")
            )
            #print(f" | HTTP Method Flows: {packet.len} | FTP Login: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | HTTP Method Flows: {packet.len} | FTP Login: {packet.len}")
            )
            #print(f" | FTP Command Flows: {packet.len} | Service and Source Address Connections: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | FTP Command Flows: {packet.len} | Service and Source Address Connections: {packet.len}")
            )
            #print(f" | Service and Destination Address Connections: {packet.len} | Destination Address Connections: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | Service and Destination Address Connections: {packet.len} | Destination Address Connections: {packet.len}")
            )
            #print(f" | Source Address Connections: {packet.len} | Source Address and Destination Port Connections: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | Source Address Connections: {packet.len} | Source Address and Destination Port Connections: {packet.len}")
            )
            #print(f" | Destination Address and Source Port Connections: {packet.len} | Source and Destination Address Connections: {packet.len}", end=" ")
            numberpack.controls.append(
                ft.Text(f" | Destination Address and Source Port Connections: {packet.len} | Source and Destination Address Connections: {packet.len}")
            )
            #print()
            #print()
            numberpack.controls.append(
                ft.Text("")
            )
            numberpack.controls.append(
                ft.Text("")
            )
            page.add(numberpack)

    # Capturar paquetes en la red
    #print("Iniciando captura de paquetes...")
    numberpack.controls.append(
        ft.Text("Iniciando captura de paquetes...")
    )
    sniff(prn=process_packet)

ft.app(target=main)