import socket
import sys
from datetime import datetime

print("=" * 50)
print("🛡️ SCANNER DE PORTS RÉSEAU INTERACTIF v3 🛡️")
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

# On récupère la date et l'heure actuelle pour l'historique
date_actuelle = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print(f"🔍 Analyse en cours sur {cible_ip}... (Appuyez sur Ctrl+C pour stopper)\n")
print("-" * 50)

try:
    # On ouvre (ou crée) le fichier rapport_scan.txt en mode écriture ('w')
    with open("rapport_scan.txt", "w", encoding="utf-8") as fichier_log:
        # Écriture de l'en-tête du rapport
        fichier_log.write(f"==================================================\n")
        fichier_log.write(f"🛡️ RAPPORT D'AUDIT RÉSEAU - SCANNER DE PORTS\n")
        fichier_log.write(f"📅 Date du scan : {date_actuelle}\n")
        fichier_log.write(f"🎯 Cible : {saisie} ({cible_ip})\n")
        fichier_log.write(f"==================================================\n\n")
        
        for port, service in PORTS_COURANTS.items():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)
            
            resultat = s.connect_ex((cible_ip, port))
            
            if resultat == 0:
                ligne_resultat = f"🟢 Port {port} [{service}] : OUVERT"
            else:
                ligne_resultat = f"🔴 Port {port} [{service}] : FERMÉ"
            
            # 1. On l'affiche dans le terminal de ton PC
            print(ligne_resultat)
            # 2. On l'écrit en même temps dans le fichier texte de logs
            fichier_log.write(ligne_resultat + "\n")
                
            s.close()
            
        fichier_log.write(f"\n--------------------------------------------------\n")
        fichier_log.write(f"🎉 Fin du scan réseau avec succès.\n")

except KeyboardInterrupt:
    print("\n\n🛑 Scan interrompu proprement par l'utilisateur.")
    sys.exit()

print("-" * 50)
print("🎉 Scan terminé ! Le fichier 'rapport_scan.txt' a été généré.")