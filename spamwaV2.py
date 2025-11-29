# Import modules yang work di Termux
from colorama import Fore, Style, init
import time
import random
import string
import urllib.parse
import webbrowser
import requests
import os

# Initialize colorama
init()

def banner():
    """Display banner"""
    print(Fore.CYAN + """
    
 ██████  ██  █████  ███    ███ 
██    ██ ██ ██   ██ ████  ████ 
██    ██ ██ ███████ ██ ████ ██ 
██    ██ ██ ██   ██ ██  ██  ██ 
 ██████  ██ ██   ██ ██      ██ 
                               
    """ + Style.RESET_ALL)
    print(Fore.GREEN + "WhatsApp Spam Tool - Termux Edition" + Style.RESET_ALL)
    print(Fore.YELLOW + "Created by: sh1vam-03" + Style.RESET_ALL)
    print(Fore.RED + "Use Responsibly!" + Style.RESET_ALL)
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
    whatsapp_url = f"https://wa.me/6285929887092?text=Test}"
    
    print(Fore.CYAN + f"📱 Target: {formatted_number}" + Style.RESET_ALL)
    print(Fore.CYAN + f"💬 Message: {message}" + Style.RESET_ALL)
    print(Fore.YELLOW + "🔗 Opening WhatsApp..." + Style.RESET_ALL)
    
    # Try to open in browser
    try:
        webbrowser.open(whatsapp_url)
        print(Fore.GREEN + "✅ WhatsApp opened! Tap 'Send' manually." + Style.RESET_ALL)
    except:
        print(Fore.YELLOW + f"📎 Manual URL: {whatsapp_url}" + Style.RESET_ALL)
    
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
    print(Fore.MAGENTA + "\n[⚡] QUICK SPAM MODE" + Style.RESET_ALL)
    
    phone_number = input(Fore.GREEN + "[+] Enter phone number: " + Style.RESET_ALL)
    
    if not phone_number.strip():
        print(Fore.RED + "❌ Phone number cannot be empty!" + Style.RESET_ALL)
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
        count = int(input(Fore.GREEN + "[+] How many spam messages: " + Style.RESET_ALL))
        delay = int(input(Fore.GREEN + "[+] Delay between messages (seconds): " + Style.RESET_ALL) or "2")
        
        print(Fore.YELLOW + f"\n🚀 QUICK SPAM MODE ACTIVATED!" + Style.RESET_ALL)
        print(Fore.YELLOW + f"📤 Sending {count} spam messages..." + Style.RESET_ALL)
        print(Fore.RED + "⚠️ Make sure WhatsApp is installed!" + Style.RESET_ALL)
        
        input(Fore.RED + "\n[!] Press Enter to START SPAMMING..." + Style.RESET_ALL)
        
        sent_count = 0
        for i in range(count):
            message = random.choice(spam_messages)
            print(Fore.CYAN + f"📤 SPAM {i+1}/{count}: {message}" + Style.RESET_ALL)
            
            if send_whatsapp_direct(phone_number, message):
                sent_count += 1
            
            if i < count - 1:  # Don't delay after last message
                print(Fore.YELLOW + f"⏳ Waiting {delay} seconds..." + Style.RESET_ALL)
                time.sleep(delay)
            
        print(Fore.GREEN + f"\n🎉 SPAM COMPLETED! {sent_count}/{count} messages prepared!" + Style.RESET_ALL)
        
    except ValueError:
        print(Fore.RED + "❌ Invalid number!" + Style.RESET_ALL)

def custom_spam():
    """Custom spam with user messages"""
    print(Fore.MAGENTA + "\n[📝] CUSTOM SPAM MODE" + Style.RESET_ALL)
    
    phone_number = input(Fore.GREEN + "[+] Enter phone number: " + Style.RESET_ALL)
    
    if not phone_number.strip():
        print(Fore.RED + "❌ Phone number cannot be empty!" + Style.RESET_ALL)
        return
    
    print(Fore.YELLOW + "\n💬 Message Options:" + Style.RESET_ALL)
    print("[1] Single message repeated")
    print("[2] Multiple different messages")
    print("[3] Message with counting")
    print("[4] Random text generator")
    
    choice = input(Fore.GREEN + "[+] Select option: " + Style.RESET_ALL)
    
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
            print(Fore.RED + "❌ Invalid option!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"❌ Error: {e}" + Style.RESET_ALL)

def single_message_spam(phone_number):
    """Single message repeated multiple times"""
    message = input(Fore.GREEN + "[+] Enter message to spam: " + Style.RESET_ALL)
    count = int(input(Fore.GREEN + "[+] How many times to send: " + Style.RESET_ALL))
    delay = int(input(Fore.GREEN + "[+] Delay between messages (seconds): " + Style.RESET_ALL) or "2")
    
    print(Fore.YELLOW + f"\n📤 Preparing to send {count} messages..." + Style.RESET_ALL)
    input(Fore.GREEN + "[+] Press Enter to start..." + Style.RESET_ALL)
    
    for i in range(count):
        print(Fore.CYAN + f"📤 Message {i+1}/{count}: {message}" + Style.RESET_ALL)
        send_whatsapp_direct(phone_number, message)
        
        if i < count - 1:
            print(Fore.YELLOW + f"⏳ Waiting {delay} seconds..." + Style.RESET_ALL)
            time.sleep(delay)

def multiple_messages_spam(phone_number):
    """Multiple different messages"""
    num_messages = int(input(Fore.GREEN + "[+] How many different messages: " + Style.RESET_ALL))
    
    messages = []
    for i in range(num_messages):
        msg = input(Fore.GREEN + f"[+] Message {i+1}: " + Style.RESET_ALL)
        messages.append(msg)
    
    repeat = int(input(Fore.GREEN + "[+] How many times to repeat sequence: " + Style.RESET_ALL) or "1")
    delay = int(input(Fore.GREEN + "[+] Delay between messages (seconds): " + Style.RESET_ALL) or "2")
    
    total_messages = len(messages) * repeat
    print(Fore.YELLOW + f"\n📤 Preparing to send {total_messages} messages..." + Style.RESET_ALL)
    input(Fore.GREEN + "[+] Press Enter to start..." + Style.RESET_ALL)
    
    for r in range(repeat):
        for i, msg in enumerate(messages):
            print(Fore.CYAN + f"🔄 Sequence {r+1}/{repeat} - Message {i+1}/{len(messages)}: {msg}" + Style.RESET_ALL)
            send_whatsapp_direct(phone_number, msg)
            
            if not (r == repeat-1 and i == len(messages)-1):  # Don't delay after last message
                print(Fore.YELLOW + f"⏳ Waiting {delay} seconds..." + Style.RESET_ALL)
                time.sleep(delay)

def counting_spam(phone_number):
    """Messages with counting"""
    base_message = input(Fore.GREEN + "[+] Enter base message: " + Style.RESET_ALL)
    count = int(input(Fore.GREEN + "[+] How many messages to send: " + Style.RESET_ALL))
    delay = int(input(Fore.GREEN + "[+] Delay between messages (seconds): " + Style.RESET_ALL) or "2")
    
    print(Fore.YELLOW + f"\n🔢 Preparing to send {count} counting messages..." + Style.RESET_ALL)
    input(Fore.GREEN + "[+] Press Enter to start..." + Style.RESET_ALL)
    
    for i in range(count):
        message = f"{base_message} {i+1}"
        print(Fore.CYAN + f"🔢 Counting {i+1}/{count}: {message}" + Style.RESET_ALL)
        send_whatsapp_direct(phone_number, message)
        
        if i < count - 1:
            print(Fore.YELLOW + f"⏳ Waiting {delay} seconds..." + Style.RESET_ALL)
            time.sleep(delay)

def random_text_spam(phone_number):
    """Random text spam"""
    count = int(input(Fore.GREEN + "[+] How many random messages: " + Style.RESET_ALL))
    delay = int(input(Fore.GREEN + "[+] Delay between messages (seconds): " + Style.RESET_ALL) or "2")
    
    # Word lists for random messages
    adjectives = ["amazing", "awesome", "brilliant", "cool", "excellent", "fantastic", 
                 "great", "incredible", "magnificent", "marvelous", "outstanding", 
                 "phenomenal", "remarkable", "spectacular", "wonderful"]
    
    nouns = ["message", "spam", "bot", "test", "experiment", "project", "program",
            "code", "script", "tool", "application", "system", "device", "machine"]
    
    verbs = ["sending", "delivering", "transmitting", "broadcasting", "dispatching",
            "forwarding", "transferring", "communicating", "sharing", "distributing"]
    
    print(Fore.YELLOW + f"\n🎲 Preparing to send {count} random messages..." + Style.RESET_ALL)
    input(Fore.GREEN + "[+] Press Enter to start..." + Style.RESET_ALL)
    
    for i in range(count):
        # Generate random message
        adj = random.choice(adjectives)
        noun = random.choice(nouns)
        verb = random.choice(verbs)
        
        message = f"This is an {adj} {noun} {verb} #{i+1}"
        print(Fore.CYAN + f"🎲 Random {i+1}/{count}: {message}" + Style.RESET_ALL)
        send_whatsapp_direct(phone_number, message)
        
        if i < count - 1:
            print(Fore.YELLOW + f"⏳ Waiting {delay} seconds..." + Style.RESET_ALL)
            time.sleep(delay)

def bulk_spam():
    """Bulk spam to multiple numbers"""
    print(Fore.MAGENTA + "\n[👥] BULK SPAM MODE" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "Enter phone numbers (one per line, type 'done' when finished):" + Style.RESET_ALL)
    phone_numbers = []
    
    while True:
        number = input(Fore.GREEN + "[+] Phone number: " + Style.RESET_ALL)
        if number.lower() == 'done':
            break
        if number.strip():
            phone_numbers.append(number.strip())
    
    if not phone_numbers:
        print(Fore.RED + "❌ No phone numbers entered!" + Style.RESET_ALL)
        return
    
    message = input(Fore.GREEN + "[+] Enter message to send: " + Style.RESET_ALL)
    delay = int(input(Fore.GREEN + "[+] Delay between numbers (seconds): " + Style.RESET_ALL) or "3")
    
    print(Fore.YELLOW + f"\n📤 Preparing to send to {len(phone_numbers)} numbers..." + Style.RESET_ALL)
    input(Fore.GREEN + "[+] Press Enter to start..." + Style.RESET_ALL)
    
    for i, number in enumerate(phone_numbers):
        print(Fore.CYAN + f"👥 Target {i+1}/{len(phone_numbers)}: {number}" + Style.RESET_ALL)
        send_whatsapp_direct(number, message)
        
        if i < len(phone_numbers) - 1:
            print(Fore.YELLOW + f"⏳ Waiting {delay} seconds..." + Style.RESET_ALL)
            time.sleep(delay)

def show_help():
    """Show help information"""
    print(Fore.CYAN + "\n" + "="*50 + Style.RESET_ALL)
    print(Fore.YELLOW + "📖 HELP & INSTRUCTIONS" + Style.RESET_ALL)
    print(Fore.CYAN + "="*50 + Style.RESET_ALL)
    
    print(Fore.GREEN + "\n🎯 How to use:" + Style.RESET_ALL)
    print("1. Choose spam mode")
    print("2. Enter target phone number (08123456789)")
    print("3. Configure messages and settings")
    print("4. Tool will open WhatsApp with pre-filled message")
    print("5. You need to manually tap 'Send' button")
    
    print(Fore.YELLOW + "\n⚠️ Important:" + Style.RESET_ALL)
    print("• WhatsApp must be installed on your device")
    print("• You need to manually send each message")
    print("• Use appropriate delays to avoid detection")
    print("• For educational purposes only")
    
    print(Fore.RED + "\n🚫 Warning:" + Style.RESET_ALL)
    print("Excessive spamming may violate WhatsApp's Terms of Service")
    print("Use responsibly and ethically")
    
    input(Fore.GREEN + "\n[+] Press Enter to continue..." + Style.RESET_ALL)

def main_menu():
    """Main menu"""
    while True:
        banner()
        
        print(Fore.YELLOW + "🏠 MAIN MENU" + Style.RESET_ALL)
        print("[1] ⚡ Quick Spam (Predefined messages)")
        print("[2] 📝 Custom Spam (Your own messages)") 
        print("[3] 👥 Bulk Spam (Multiple numbers)")
        print("[4] 📖 Help & Instructions")
        print("[0] ❌ Exit")
        
        choice = input(Fore.GREEN + "\n[+] Select option: " + Style.RESET_ALL)
        
        if choice == "1":
            quick_spam()
        elif choice == "2":
            custom_spam()
        elif choice == "3":
            bulk_spam()
        elif choice == "4":
            show_help()
        elif choice == "0":
            print(Fore.RED + "\n👋 Thank you for using WhatsApp Spam Tool!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "❌ Invalid option!" + Style.RESET_ALL)
            time.sleep(1)
        
        # Ask to continue or exit
        if choice != "0":
            cont = input(Fore.GREEN + "\n[+] Continue? (y/n): " + Style.RESET_ALL)
            if cont.lower() != 'y':
                print(Fore.RED + "👋 Goodbye!" + Style.RESET_ALL)
                break

# Run the tool
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n❌ Program interrupted by user" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"\n❌ Error: {e}" + Style.RESET_ALL)
