# WhatsApp Spam Tool - Termux Edition
# Created by: mrLana

import time
import random
import urllib.parse
import os
import sys

# Color codes for Termux
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'

def banner():
    """Display banner"""
    print(Colors.CYAN + """
    
 ██████  ██  █████  ███    ███ 
██    ██ ██ ██   ██ ████  ████ 
██    ██ ██ ███████ ██ ████ ██ 
██    ██ ██ ██   ██ ██  ██  ██ 
 ██████  ██ ██   ██ ██      ██ 
                               
    """ + Colors.RESET)
    print(Colors.GREEN + "WhatsApp Spam Tool - Termux Edition" + Colors.RESET)
    print(Colors.YELLOW + "Created by: mrLana" + Colors.RESET)
    print(Colors.RED + "Use Responsibly!" + Colors.RESET)
    print()

def send_whatsapp_direct(phone_number, message):
    """
    Send WhatsApp message using direct WhatsApp link
    """
    # Format phone number
    formatted_number = format_phone_number(phone_number)
    
    # URL encode the message
    encoded_message = urllib.parse.quote(message)
    
    # Create WhatsApp URL
    whatsapp_url = f"https://wa.me/{formatted_number}?text={encoded_message}"
    
    print(Colors.CYAN + f"📱 Target: {formatted_number}" + Colors.RESET)
    print(Colors.CYAN + f"💬 Message: {message}" + Colors.RESET)
    print(Colors.YELLOW + "🔗 Creating WhatsApp link..." + Colors.RESET)
    
    # Display the link
    print(Colors.MAGENTA + f"📎 WhatsApp Link:" + Colors.RESET)
    print(Colors.GREEN + f"{whatsapp_url}" + Colors.RESET)
    
    # Try to open in browser (may not work in Termux)
    try:
        # For Termux, we can use termux-open-url
        os.system(f"termux-open-url '{whatsapp_url}'")
        print(Colors.GREEN + "✅ Opening WhatsApp..." + Colors.RESET)
    except:
        print(Colors.YELLOW + "📱 Copy link above and open manually in WhatsApp" + Colors.RESET)
    
    return True

def format_phone_number(phone_number):
    """
    Format phone number to international format
    """
    # Remove any non-digit characters
    cleaned = ''.join(filter(str.isdigit, phone_number))
    
    if cleaned.startswith('0'):
        return '62' + cleaned[1:]  # Indonesia country code
    elif not cleaned.startswith('62'):
        return '62' + cleaned
    
    return cleaned

def quick_spam():
    """Quick spam with predefined messages"""
    print(Colors.MAGENTA + "\n[⚡] QUICK SPAM MODE" + Colors.RESET)
    
    phone_number = input(Colors.GREEN + "[+] Enter phone number: " + Colors.RESET)
    
    if not phone_number.strip():
        print(Colors.RED + "❌ Phone number cannot be empty!" + Colors.RESET)
        return
    
    # Predefined spam messages
    spam_messages = [
        "😂 SPAM BOT ACTIVATED 😂",
        "🚀 AUTOMATED MESSAGE INCOMING 🚀", 
        "💥 BOT TESTING IN PROGRESS 💥",
        "🎯 TARGET ACQUIRED 🎯",
        "⚡ ELECTRIC SPAM ⚡",
        "🔥 FIRE IN THE HOLE 🔥",
        "💣 MESSAGE BOMB 💣",
        "🎪 SPAM CIRCUS 🎪",
        "🚨 ALERT: SPAM DETECTED 🚨",
        "🎭 BOT PERFORMANCE 🎭",
        "🌈 RAINBOW SPAM 🌈",
        "🎮 GAME OVER 🎮",
        "📱 MOBILE SPAM 📱",
        "💻 TERMUX POWER 💻",
        "🐍 PYTHON BOT 🐍"
    ]
    
    try:
        count = int(input(Colors.GREEN + "[+] How many spam messages: " + Colors.RESET))
        delay = int(input(Colors.GREEN + "[+] Delay between messages (seconds): " + Colors.RESET) or "2")
        
        print(Colors.YELLOW + f"\n🚀 QUICK SPAM MODE ACTIVATED!" + Colors.RESET)
        print(Colors.YELLOW + f"📤 Sending {count} spam messages..." + Colors.RESET)
        print(Colors.RED + "⚠️ Make sure WhatsApp is installed!" + Colors.RESET)
        
        input(Colors.RED + "\n[!] Press Enter to START SPAMMING..." + Colors.RESET)
        
        sent_count = 0
        for i in range(count):
            message = random.choice(spam_messages)
            print(Colors.CYAN + f"\n📤 SPAM {i+1}/{count}" + Colors.RESET)
            print(Colors.CYAN + f"💬 Message: {message}" + Colors.RESET)
            
            if send_whatsapp_direct(phone_number, message):
                sent_count += 1
            
            if i < count - 1:  # Don't delay after last message
                print(Colors.YELLOW + f"⏳ Waiting {delay} seconds..." + Colors.RESET)
                time.sleep(delay)
            
        print(Colors.GREEN + f"\n🎉 SPAM COMPLETED! {sent_count}/{count} messages prepared!" + Colors.RESET)
        
    except ValueError:
        print(Colors.RED + "❌ Invalid number!" + Colors.RESET)

def custom_spam():
    """Custom spam with user messages"""
    print(Colors.MAGENTA + "\n[📝] CUSTOM SPAM MODE" + Colors.RESET)
    
    phone_number = input(Colors.GREEN + "[+] Enter phone number: " + Colors.RESET)
    
    if not phone_number.strip():
        print(Colors.RED + "❌ Phone number cannot be empty!" + Colors.RESET)
        return
    
    print(Colors.YELLOW + "\n💬 Message Options:" + Colors.RESET)
    print("[1] Single message repeated")
    print("[2] Multiple different messages")
    print("[3] Message with counting")
    print("[4] Random text generator")
    
    choice = input(Colors.GREEN + "[+] Select option: " + Colors.RESET)
    
    try:
        if choice == "1":
            single_message_spam(phone_number)
        elif choice == "2":
            multiple_messages_spam(phone_number)
        elif choice == "3":
            counting_spam(phone_number)
        elif choice == "4":
            random_text_spam(phone_number)
        else:
            print(Colors.RED + "❌ Invalid option!" + Colors.RESET)
    except Exception as e:
        print(Colors.RED + f"❌ Error: {e}" + Colors.RESET)

def single_message_spam(phone_number):
    """Single message repeated multiple times"""
    message = input(Colors.GREEN + "[+] Enter message to spam: " + Colors.RESET)
    count = int(input(Colors.GREEN + "[+] How many times to send: " + Colors.RESET))
    delay = int(input(Colors.GREEN + "[+] Delay between messages (seconds): " + Colors.RESET) or "2")
    
    print(Colors.YELLOW + f"\n📤 Preparing to send {count} messages..." + Colors.RESET)
    input(Colors.GREEN + "[+] Press Enter to start..." + Colors.RESET)
    
    for i in range(count):
        print(Colors.CYAN + f"\n📤 Message {i+1}/{count}" + Colors.RESET)
        print(Colors.CYAN + f"💬 Message: {message}" + Colors.RESET)
        send_whatsapp_direct(phone_number, message)
        
        if i < count - 1:
            print(Colors.YELLOW + f"⏳ Waiting {delay} seconds..." + Colors.RESET)
            time.sleep(delay)

def multiple_messages_spam(phone_number):
    """Multiple different messages"""
    num_messages = int(input(Colors.GREEN + "[+] How many different messages: " + Colors.RESET))
    
    messages = []
    for i in range(num_messages):
        msg = input(Colors.GREEN + f"[+] Message {i+1}: " + Colors.RESET)
        messages.append(msg)
    
    repeat = int(input(Colors.GREEN + "[+] How many times to repeat sequence: " + Colors.RESET) or "1")
    delay = int(input(Colors.GREEN + "[+] Delay between messages (seconds): " + Colors.RESET) or "2")
    
    total_messages = len(messages) * repeat
    print(Colors.YELLOW + f"\n📤 Preparing to send {total_messages} messages..." + Colors.RESET)
    input(Colors.GREEN + "[+] Press Enter to start..." + Colors.RESET)
    
    for r in range(repeat):
        for i, msg in enumerate(messages):
            print(Colors.CYAN + f"\n🔄 Sequence {r+1}/{repeat} - Message {i+1}/{len(messages)}" + Colors.RESET)
            print(Colors.CYAN + f"💬 Message: {msg}" + Colors.RESET)
            send_whatsapp_direct(phone_number, msg)
            
            if not (r == repeat-1 and i == len(messages)-1):  # Don't delay after last message
                print(Colors.YELLOW + f"⏳ Waiting {delay} seconds..." + Colors.RESET)
                time.sleep(delay)

def counting_spam(phone_number):
    """Messages with counting"""
    base_message = input(Colors.GREEN + "[+] Enter base message: " + Colors.RESET)
    count = int(input(Colors.GREEN + "[+] How many messages to send: " + Colors.RESET))
    delay = int(input(Colors.GREEN + "[+] Delay between messages (seconds): " + Colors.RESET) or "2")
    
    print(Colors.YELLOW + f"\n🔢 Preparing to send {count} counting messages..." + Colors.RESET)
    input(Colors.GREEN + "[+] Press Enter to start..." + Colors.RESET)
    
    for i in range(count):
        message = f"{base_message} {i+1}"
        print(Colors.CYAN + f"\n🔢 Counting {i+1}/{count}" + Colors.RESET)
        print(Colors.CYAN + f"💬 Message: {message}" + Colors.RESET)
        send_whatsapp_direct(phone_number, message)
        
        if i < count - 1:
            print(Colors.YELLOW + f"⏳ Waiting {delay} seconds..." + Colors.RESET)
            time.sleep(delay)

def random_text_spam(phone_number):
    """Random text spam"""
    count = int(input(Colors.GREEN + "[+] How many random messages: " + Colors.RESET))
    delay = int(input(Colors.GREEN + "[+] Delay between messages (seconds): " + Colors.RESET) or "2")
    
    # Word lists for random messages
    adjectives = ["amazing", "awesome", "brilliant", "cool", "excellent", "fantastic", 
                 "great", "incredible", "magnificent", "marvelous", "outstanding", 
                 "phenomenal", "remarkable", "spectacular", "wonderful"]
    
    nouns = ["message", "spam", "bot", "test", "experiment", "project", "program",
            "code", "script", "tool", "application", "system", "device", "machine"]
    
    verbs = ["sending", "delivering", "transmitting", "broadcasting", "dispatching",
            "forwarding", "transferring", "communicating", "sharing", "distributing"]
    
    print(Colors.YELLOW + f"\n🎲 Preparing to send {count} random messages..." + Colors.RESET)
    input(Colors.GREEN + "[+] Press Enter to start..." + Colors.RESET)
    
    for i in range(count):
        # Generate random message
        adj = random.choice(adjectives)
        noun = random.choice(nouns)
        verb = random.choice(verbs)
        
        message = f"This is an {adj} {noun} {verb} #{i+1}"
        print(Colors.CYAN + f"\n🎲 Random {i+1}/{count}" + Colors.RESET)
        print(Colors.CYAN + f"💬 Message: {message}" + Colors.RESET)
        send_whatsapp_direct(phone_number, message)
        
        if i < count - 1:
            print(Colors.YELLOW + f"⏳ Waiting {delay} seconds..." + Colors.RESET)
            time.sleep(delay)

def show_help():
    """Show help information"""
    print(Colors.CYAN + "\n" + "="*50 + Colors.RESET)
    print(Colors.YELLOW + "📖 HELP & INSTRUCTIONS" + Colors.RESET)
    print(Colors.CYAN + "="*50 + Colors.RESET)
    
    print(Colors.GREEN + "\n🎯 Cara Pakai:" + Colors.RESET)
    print("1. Pilih mode spam")
    print("2. Masukkan nomor target (contoh: 08123456789)")
    print("3. Atur pesan dan pengaturan")
    print("4. Program akan buka WhatsApp dengan pesan siap kirim")
    print("5. Anda harus TAP SEND manual di WhatsApp")
    
    print(Colors.YELLOW + "\n⚠️ Penting:" + Colors.RESET)
    print("• WhatsApp harus terinstall di HP")
    print("• Anda perlu tap SEND manual setiap pesan")
    print("• Gunakan delay yang wajar (minimal 2-3 detik)")
    print("• Untuk keperluan edukasi saja")
    
    print(Colors.RED + "\n🚫 Peringatan:" + Colors.RESET)
    print("Spam berlebihan bisa melanggar Terms of Service WhatsApp")
    print("Gunakan dengan bijak dan bertanggung jawab")
    
    input(Colors.GREEN + "\n[+] Press Enter to continue..." + Colors.RESET)

def main_menu():
    """Main menu"""
    while True:
        banner()
        
        print(Colors.YELLOW + "🏠 MAIN MENU" + Colors.RESET)
        print("[1] ⚡ Quick Spam (Pesan random)")
        print("[2] 📝 Custom Spam (Pesan custom)") 
        print("[3] 📖 Cara Pakai")
        print("[0] ❌ Keluar")
        
        choice = input(Colors.GREEN + "\n[+] Pilih menu: " + Colors.RESET)
        
        if choice == "1":
            quick_spam()
        elif choice == "2":
            custom_spam()
        elif choice == "3":
            show_help()
        elif choice == "0":
            print(Colors.RED + "\n👋 Terima kasih telah menggunakan WhatsApp Spam Tool!" + Colors.RESET)
            break
        else:
            print(Colors.RED + "❌ Pilihan tidak valid!" + Colors.RESET)
            time.sleep(1)
        
        # Ask to continue or exit
        if choice != "0":
            cont = input(Colors.GREEN + "\n[+] Lanjutkan? (y/n): " + Colors.RESET)
            if cont.lower() != 'y':
                print(Colors.RED + "👋 Sampai jumpa!" + Colors.RESET)
                break

# Run the tool
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(Colors.RED + "\n\n❌ Program dihentikan oleh user" + Colors.RESET)
    except Exception as e:
        print(Colors.RED + f"\n❌ Error: {e}" + Colors.RESET)
