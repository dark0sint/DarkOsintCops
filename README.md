# DarkOsintCops

DarkOsintCops adalah aplikasi pencarian .onion yang menggabungkan hasil dari berbagai mesin pencari di jaringan Tor.

## Cara Pakai

1. Pastikan Tor berjalan dan proxy SOCKS5 di `127.0.0.1:9050`.
2. Jalankan:

```bash
python darkosintcops.py "kata kunci pencarian" --output hasil.csv --limit 20
