import socket
import time

def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP

def report_ip(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = extract_ip()
    sock.sendto(bytes(ip, 'utf-8'), (target_ip, target_port))
    sock.close()

def receive_ip(target_port, output_file):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", target_port))
    data, addr = sock.recvfrom(1024)
    ip_address = data.decode('utf-8')
    with open(output_file, 'w') as file:
        file.write(ip_address)
    
target_ip = "218.194.38.252"
target_port = 35456

time.sleep(30)
report_ip(target_ip, target_port)
