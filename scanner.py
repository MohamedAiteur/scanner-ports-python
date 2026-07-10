import socket
import sys

print("=" * 50)
print("🛡️ SCANNER DE PORTS RÉSEAU INTERACTIF v2 🛡️")
print("=" * 50)

saisie = input("👉 Entrez un nom de domaine ou une IP (ex: ynov.com) : ")

try:
    cible_ip = socket.gethostbyname(saisie)
    print(f"\n[+] Résolution DNS réussie : {saisie} -> {cible_ip}")
except socket.gaierror:
    print("\n❌ Erreur : Impossible de résoudre le nom de domaine.")
    sys.exit()

PORTS_COURANTS = {
    21: "FTP (Fichiers)",
    22: "SSH (Accès sécurisé)",
    23: "Telnet (Non sécurisé)",
    80: "HTTP (Web)",
    443: "HTTPS (Web sécurisé)"
}

print(f"🔍 Analyse en cours sur {cible_ip}... (Appuyez sur Ctrl+C pour stopper)\n")
print("-" * 50)

try:
    for port, service in PORTS_COURANTS.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        
        resultat = s.connect_ex((cible_ip, port))
        
        if resultat == 0:
            print(f"🟢 Port {port} [{service}] : OUVERT")
        else:
            print(f"🔴 Port {port} [{service}] : FERMÉ")
            
        s.close()

except KeyboardInterrupt:
    # Si l'utilisateur appuie sur Ctrl + C pendant le scan
    print("\n\n🛑 Scan interrompu proprement par l'utilisateur.")
    sys.exit()

print("-" * 50)
print("🎉 Scan terminé avec succès !")