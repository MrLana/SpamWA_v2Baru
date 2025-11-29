# WhatsApp Auto Send - Ultramsg API
# Created by: mrLana
# AUTO SEND TANPA KLIK MANUAL

import requests
import time
import random
import json

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'

def banner():
    print(f"""{Colors.CYAN}
    
 ██████  ██  █████  ███    ███ 
██    ██ ██ ██   ██ ████  ████ 
██    ██ ██ ███████ ██ ████ ██ 
██    ██ ██ ██   ██ ██  ██  ██ 
 ██████  ██ ██   ██ ██      ██ 
                               
    {Colors.RESET}""")
    print(f"{Colors.GREEN}🚀 WhatsApp Auto Send - Ultramsg API{Colors.RESET}")
    print(f"{Colors.YELLOW}📱 Created by: mrLana{Colors.RESET}")
    print(f"{Colors.MAGENTA}⚡ FULLY AUTOMATIC - NO MANUAL CLICK{Colors.RESET}")
    print()

class UltramsgSender:
    def __init__(self):
        self.instance_id = None
        self.token = None
        self.setup_credentials()
    
    def setup_credentials(self):
        """Setup Ultramsg credentials"""
        print(f"{Colors.YELLOW}🔑 ULTRAMSG API SETUP{Colors.RESET}")
        print(f"{Colors.CYAN}1. Visit: https://ultramsg.com/{Colors.RESET}")
        print(f"{Colors.CYAN}2. Sign up for free account{Colors.RESET}")
        print(f"{Colors.CYAN}3. Get Instance ID and Token from dashboard{Colors.RESET}")
        print()
        
        self.instance_id = input(f"{Colors.GREEN}[+] Enter Instance ID: {Colors.RESET}").strip()
        self.token = input(f"{Colors.GREEN}[+] Enter Token: {Colors.RESET}").strip()
        
        if not self.instance_id or not self.token:
            print(f"{Colors.RED}❌ Instance ID and Token are required!{Colors.RESET}")
            print(f"{Colors.YELLOW}⚠️ Using demo mode for testing{Colors.RESET}")
        else:
            print(f"{Colors.GREEN}✅ Ultramsg credentials saved!{Colors.RESET}")
    
    def format_phone(self, phone):
        """Format phone number to international"""
        cleaned = ''.join(filter(str.isdigit, phone))
        if cleaned.startswith('0'):
            return '62' + cleaned[1:]  # Indonesia
        elif not cleaned.startswith('62'):
            return '62' + cleaned
        return cleaned
    
    def send_message(self, phone, message):
        """Send message using Ultramsg API"""
        try:
            formatted_phone = self.format_phone(phone)
            
            if not self.instance_id or not self.token:
                # Demo mode
                print(f"{Colors.YELLOW}🔄 DEMO MODE: Simulating send to {formatted_phone}{Colors.RESET}")
                print(f"{Colors.CYAN}💬 Message: {message}{Colors.RESET}")
                time.sleep(2)
                print(f"{Colors.GREEN}✅ Demo: Message would be sent via Ultramsg!{Colors.RESET}")
                return True
            
            # Ultramsg API endpoint
            url = f"https://api.ultramsg.com/{self.instance_id}/messages/chat"
            
            payload = {
                "token": self.token,
                "to": formatted_phone,
                "body": message,
                "priority": 10
            }
            
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            print(f"{Colors.CYAN}📤 Sending to {formatted_phone} via Ultramsg...{Colors.RESET}")
            response = requests.post(url, data=payload, headers=headers, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                if result.get('sent') == 'true':
                    print(f"{Colors.GREEN}✅ Message sent successfully via Ultramsg!{Colors.RESET}")
                    return True
                else:
                    print(f"{Colors.RED}❌ Failed: {result.get('message', 'Unknown error')}{Colors.RESET}")
                    return False
            else:
                print(f"{Colors.RED}❌ API Error: Status {response.status_code}{Colors.RESET}")
                return False
                
        except requests.exceptions.Timeout:
            print(f"{Colors.RED}❌ Request timeout! Check internet connection{Colors.RESET}")
            return False
        except Exception as e:
            print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
            return False

def quick_ultramsg_spam():
    """Quick spam dengan Ultramsg"""
    print(f"{Colors.MAGENTA}\n[⚡] ULTRAMSG QUICK SPAM{Colors.RESET}")
    
    sender = UltramsgSender()
    
    phone = input(f"{Colors.GREEN}[+] Enter target number: {Colors.RESET}").strip()
    if not phone:
        print(f"{Colors.RED}❌ Phone number required!{Colors.RESET}")
        return
    
    spam_messages = [
        "🚀 AUTO SEND VIA ULTRAMSG API",
        "💻 ULTRAMSG POWERED BOT", 
        "📱 CREATED BY MRLANA",
        "⚡ FULLY AUTOMATIC MESSAGE",
        "🎯 NO MANUAL CLICK REQUIRED",
        "🔥 ULTRAMSG API WORKING",
        "💥 INSTANT DELIVERY",
        "🎪 ULTRAMSG AUTOMATION"
    ]
    
    try:
        count = int(input(f"{Colors.GREEN}[+] Number of messages: {Colors.RESET}"))
        delay = int(input(f"{Colors.GREEN}[+] Delay between messages (seconds): {Colors.RESET}") or "5")
        
        print(f"{Colors.YELLOW}\n🚀 Starting Ultramsg Auto Spam...{Colors.RESET}")
        print(f"{Colors.YELLOW}📱 Target: {phone}{Colors.RESET}")
        print(f"{Colors.YELLOW}📤 Count: {count} messages{Colors.RESET}")
        print(f"{Colors.YELLOW}⏰ Delay: {delay} seconds{Colors.RESET}")
        
        if not sender.instance_id or not sender.token:
            print(f"{Colors.RED}⚠️ DEMO MODE: Messages won't be actually sent!{Colors.RESET}")
            print(f"{Colors.YELLOW}💡 Get free credentials from ultramsg.com{Colors.RESET}")
        
        input(f"{Colors.RED}\n[!] Press Enter to START AUTO SEND...{Colors.RESET}")
        
        success = 0
        for i in range(count):
            message = random.choice(spam_messages)
            print(f"{Colors.CYAN}\n📤 Message {i+1}/{count}{Colors.RESET}")
            print(f"{Colors.CYAN}💬 Content: {message}{Colors.RESET}")
            
            if sender.send_message(phone, f"{message} #{i+1}"):
                success += 1
                print(f"{Colors.GREEN}✅ AUTO SENT SUCCESS!{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ AUTO SEND FAILED{Colors.RESET}")
            
            if i < count - 1:
                print(f"{Colors.YELLOW}⏳ Waiting {delay} seconds...{Colors.RESET}")
                time.sleep(delay)
        
        print(f"{Colors.GREEN}\n🎉 ULTRAMSG MISSION COMPLETE!{Colors.RESET}")
        print(f"{Colors.GREEN}📊 {success}/{count} messages AUTO SENT!{Colors.RESET}")
        
    except ValueError:
        print(f"{Colors.RED}❌ Invalid input!{Colors.RESET}")

def custom_ultramsg_spam():
    """Custom spam dengan Ultramsg"""
    print(f"{Colors.MAGENTA}\n[📝] ULTRAMSG CUSTOM SPAM{Colors.RESET}")
    
    sender = UltramsgSender()
    
    phone = input(f"{Colors.GREEN}[+] Enter target number: {Colors.RESET}").strip()
    if not phone:
        print(f"{Colors.RED}❌ Phone number required!{Colors.RESET}")
        return
    
    print(f"{Colors.YELLOW}\n💬 Message Options:{Colors.RESET}")
    print("[1] Single message (repeated)")
    print("[2] Multiple different messages")
    print("[3] Counting messages")
    
    choice = input(f"{Colors.GREEN}[+] Select option: {Colors.RESET}")
    
    try:
        if choice == "1":
            single_message_spam(phone, sender)
        elif choice == "2":
            multiple_messages_spam(phone, sender)
        elif choice == "3":
            counting_spam(phone, sender)
        else:
            print(f"{Colors.RED}❌ Invalid choice!{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")

def single_message_spam(phone, sender):
    """Single message repeated"""
    message = input(f"{Colors.GREEN}[+] Enter message: {Colors.RESET}")
    count = int(input(f"{Colors.GREEN}[+] Repeat count: {Colors.RESET}"))
    delay = int(input(f"{Colors.GREEN}[+] Delay between messages (seconds): {Colors.RESET}") or "5")
    
    print(f"{Colors.YELLOW}\n📤 Sending '{message}' {count} times via Ultramsg...{Colors.RESET}")
    
    if not sender.instance_id or not sender.token:
        print(f"{Colors.RED}⚠️ DEMO MODE: Messages won't be actually sent!{Colors.RESET}")
    
    input(f"{Colors.GREEN}[+] Press Enter to start AUTO SEND...{Colors.RESET}")
    
    success = 0
    for i in range(count):
        print(f"{Colors.CYAN}\n📤 Auto Sending {i+1}/{count}{Colors.RESET}")
        
        if sender.send_message(phone, f"{message} [#{i+1}]"):
            success += 1
            print(f"{Colors.GREEN}✅ AUTO SENT!{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ SEND FAILED{Colors.RESET}")
        
        if i < count - 1:
            print(f"{Colors.YELLOW}⏳ Auto waiting {delay} seconds...{Colors.RESET}")
            time.sleep(delay)
    
    print(f"{Colors.GREEN}\n🎉 {success}/{count} messages AUTO SENT via Ultramsg!{Colors.RESET}")

def multiple_messages_spam(phone, sender):
    """Multiple different messages"""
    num_msg = int(input(f"{Colors.GREEN}[+] How many different messages: {Colors.RESET}"))
    
    messages = []
    for i in range(num_msg):
        msg = input(f"{Colors.GREEN}[+] Message {i+1}: {Colors.RESET}")
        messages.append(msg)
    
    repeat = int(input(f"{Colors.GREEN}[+] Repeat sequence how many times: {Colors.RESET}") or "1")
    delay = int(input(f"{Colors.GREEN}[+] Delay between messages (seconds): {Colors.RESET}") or "5")
    
    total = len(messages) * repeat
    print(f"{Colors.YELLOW}\n📤 Total {total} messages will be AUTO SENT via Ultramsg...{Colors.RESET}")
    
    if not sender.instance_id or not sender.token:
        print(f"{Colors.RED}⚠️ DEMO MODE: Messages won't be actually sent!{Colors.RESET}")
    
    input(f"{Colors.GREEN}[+] Press Enter to start AUTO SEND...{Colors.RESET}")
    
    success = 0
    for r in range(repeat):
        for i, msg in enumerate(messages):
            print(f"{Colors.CYAN}\n🔄 Sequence {r+1}/{repeat} - Message {i+1}/{len(messages)}{Colors.RESET}")
            
            if sender.send_message(phone, f"{msg} [S:{r+1}-M:{i+1}]"):
                success += 1
                print(f"{Colors.GREEN}✅ AUTO SENT!{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ SEND FAILED{Colors.RESET}")
            
            if not (r == repeat-1 and i == len(messages)-1):
                print(f"{Colors.YELLOW}⏳ Auto waiting {delay} seconds...{Colors.RESET}")
                time.sleep(delay)
    
    print(f"{Colors.GREEN}\n🎉 {success}/{total} messages AUTO SENT via Ultramsg!{Colors.RESET}")

def counting_spam(phone, sender):
    """Counting messages"""
    base_msg = input(f"{Colors.GREEN}[+] Base message: {Colors.RESET}")
    count = int(input(f"{Colors.GREEN}[+] Number of messages: {Colors.RESET}"))
    delay = int(input(f"{Colors.GREEN}[+] Delay between messages (seconds): {Colors.RESET}") or "5")
    
    print(f"{Colors.YELLOW}\n🔢 Sending {count} counting messages via Ultramsg...{Colors.RESET}")
    
    if not sender.instance_id or not sender.token:
        print(f"{Colors.RED}⚠️ DEMO MODE: Messages won't be actually sent!{Colors.RESET}")
    
    input(f"{Colors.GREEN}[+] Press Enter to start AUTO SEND...{Colors.RESET}")
    
    success = 0
    for i in range(count):
        message = f"{base_msg} {i+1}"
        print(f"{Colors.CYAN}\n🔢 Auto Sending {i+1}/{count}{Colors.RESET}")
        print(f"{Colors.CYAN}💬 Content: {message}{Colors.RESET}")
        
        if sender.send_message(phone, message):
            success += 1
            print(f"{Colors.GREEN}✅ AUTO SENT!{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ SEND FAILED{Colors.RESET}")
        
        if i < count - 1:
            print(f"{Colors.YELLOW}⏳ Auto waiting {delay} seconds...{Colors.RESET}")
            time.sleep(delay)
    
    print(f"{Colors.GREEN}\n🎉 {success}/{count} messages AUTO SENT via Ultramsg!{Colors.RESET}")

def setup_ultramsg():
    """Setup Ultramsg credentials separately"""
    print(f"{Colors.MAGENTA}\n[🔑] ULTRAMSG SETUP{Colors.RESET}")
    
    sender = UltramsgSender()
    print(f"{Colors.GREEN}✅ Ultramsg setup completed!{Colors.RESET}")
    
    input(f"{Colors.GREEN}[+] Press Enter to continue...{Colors.RESET}")

def show_ultramsg_help():
    """Show Ultramsg help information"""
    print(f"""{Colors.CYAN}
📖 ULTRAMSG API GUIDE:

1. GET CREDENTIALS:
   - Visit: https://ultramsg.com/
   - Sign up for free account
   - Verify your phone number
   - Get Instance ID and Token from dashboard

2. FREE PLAN:
   - 50 messages per day
   - 3 connected devices
   - Basic features
   - No credit card required

3. HOW IT WORKS:
   - Messages sent via Ultramsg servers
   - Direct to WhatsApp (not SMS)
   - No manual click required
   - Real WhatsApp messages

4. SUPPORTED FORMATS:
   - Text messages
   - Images
   - Documents
   - Location

{Colors.YELLOW}
⚡ FEATURES:
   - ✅ AUTO SEND tanpa klik manual
   - ✅ Real WhatsApp messages
   - ✅ Free quota available
   - ✅ Easy setup
   - ✅ Termux compatible

{Colors.GREEN}
🎯 FOR NUMBER: +6285929887092
   You can use Ultramsg to send REAL WhatsApp messages
   without any manual action!
{Colors.RESET}""")
    
    input(f"{Colors.GREEN}\n[+] Press Enter to continue...{Colors.RESET}")

def main_menu():
    """Main menu"""
    while True:
        banner()
        
        print(f"{Colors.YELLOW}🏠 MAIN MENU:{Colors.RESET}")
        print("[1] ⚡ Quick Auto Spam")
        print("[2] 📝 Custom Auto Spam")
        print("[3] 🔑 Setup Ultramsg")
        print("[4] 📖 Ultramsg Guide")
        print("[0] ❌ Exit")
        
        choice = input(f"{Colors.GREEN}\n[+] Select menu: {Colors.RESET}")
        
        if choice == "1":
            quick_ultramsg_spam()
        elif choice == "2":
            custom_ultramsg_spam()
        elif choice == "3":
            setup_ultramsg()
        elif choice == "4":
            show_ultramsg_help()
        elif choice == "0":
            print(f"{Colors.RED}\n👋 Thank you for using Ultramsg Auto Send!{Colors.RESET}")
            break
        else:
            print(f"{Colors.RED}❌ Invalid choice!{Colors.RESET}")
            time.sleep(1)
        
        if choice != "0":
            cont = input(f"{Colors.GREEN}\n[+] Continue? (y/n): {Colors.RESET}").lower()
            if cont != 'y':
                print(f"{Colors.RED}👋 Goodbye!{Colors.RESET}")
                break

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"{Colors.RED}\n\n❌ Program interrupted by user{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}\n❌ Error: {e}{Colors.RESET}")