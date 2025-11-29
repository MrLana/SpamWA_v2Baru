# WhatsApp Auto Send - Ultramsg API
# Created by: mrLana
# USING YOUR WORKING ULTRAMSG CODE

import http.client
import ssl
import time
import random

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
    print(f"{Colors.MAGENTA}⚡ USING YOUR WORKING ULTRAMSG CODE{Colors.RESET}")
    print()

class UltramsgSender:
    def __init__(self):
        self.token = "5432"  # Token dari kode Anda
        self.instance_id = "instance1"  # Instance ID dari kode Anda
    
    def send_message(self, phone, message):
        """Send message using Ultramsg API - YOUR WORKING CODE"""
        try:
            conn = http.client.HTTPSConnection("api.ultramsg.com", context=ssl._create_unverified_context())
            
            payload = f"token={self.token}&to={phone}&body={message}"
            payload = payload.encode('utf8').decode('iso-8859-1')
            
            headers = {'content-type': "application/x-www-form-urlencoded"}
            
            print(f"{Colors.CYAN}📤 Sending to {phone}...{Colors.RESET}")
            conn.request("POST", f"/{self.instance_id}/messages/chat", payload, headers)
            
            res = conn.getresponse()
            data = res.read()
            result = data.decode("utf-8")
            
            print(f"{Colors.GREEN}✅ API Response: {result}{Colors.RESET}")
            
            # Check if message was sent successfully
            if '"sent":"true"' in result:
                print(f"{Colors.GREEN}✅ Message sent successfully!{Colors.RESET}")
                return True
            else:
                print(f"{Colors.RED}❌ Failed to send message{Colors.RESET}")
                return False
                
        except Exception as e:
            print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
            return False

def test_ultramsg():
    """Test your Ultramsg connection"""
    print(f"{Colors.MAGENTA}\n[🧪] TEST ULTRAMSG CONNECTION{Colors.RESET}")
    
    sender = UltramsgSender()
    
    # Test dengan nomor +6285929887092
    test_phone = "+6285929887092"
    test_message = "Test message from Ultramsg API - mrLana Bot"
    
    print(f"{Colors.YELLOW}🔧 Testing connection to {test_phone}{Colors.RESET}")
    print(f"{Colors.CYAN}💬 Message: {test_message}{Colors.RESET}")
    
    input(f"{Colors.GREEN}[+] Press Enter to test...{Colors.RESET}")
    
    if sender.send_message(test_phone, test_message):
        print(f"{Colors.GREEN}🎉 ULTRAMSG CONNECTION SUCCESSFUL!{Colors.RESET}")
    else:
        print(f"{Colors.RED}❌ ULTRAMSG CONNECTION FAILED{Colors.RESET}")

def quick_auto_spam():
    """Quick auto spam dengan Ultramsg"""
    print(f"{Colors.MAGENTA}\n[⚡] QUICK AUTO SPAM{Colors.RESET}")
    
    sender = UltramsgSender()
    
    phone = input(f"{Colors.GREEN}[+] Enter target number (with +): {Colors.RESET}").strip()
    if not phone:
        print(f"{Colors.RED}❌ Phone number required!{Colors.RESET}")
        return
    
    spam_messages = [
        "🚀 AUTO SEND VIA ULTRAMSG API",
        "💻 USING YOUR WORKING ULTRAMSG CODE", 
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
        print(f"{Colors.GREEN}🔑 Using Token: {sender.token}{Colors.RESET}")
        print(f"{Colors.GREEN}🆔 Instance: {sender.instance_id}{Colors.RESET}")
        
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

def custom_auto_spam():
    """Custom auto spam"""
    print(f"{Colors.MAGENTA}\n[📝] CUSTOM AUTO SPAM{Colors.RESET}")
    
    sender = UltramsgSender()
    
    phone = input(f"{Colors.GREEN}[+] Enter target number (with +): {Colors.RESET}").strip()
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

def show_credentials():
    """Show current Ultramsg credentials"""
    print(f"{Colors.MAGENTA}\n[🔑] CURRENT CREDENTIALS{Colors.RESET}")
    sender = UltramsgSender()
    print(f"{Colors.GREEN}🆔 Instance ID: {sender.instance_id}{Colors.RESET}")
    print(f"{Colors.GREEN}🔑 Token: {sender.token}{Colors.RESET}")
    print(f"{Colors.YELLOW}📱 Default Test Number: +6285929887092{Colors.RESET}")
    
    input(f"{Colors.GREEN}\n[+] Press Enter to continue...{Colors.RESET}")

def main_menu():
    """Main menu"""
    while True:
        banner()
        
        print(f"{Colors.YELLOW}🏠 MAIN MENU:{Colors.RESET}")
        print("[1] 🧪 Test Connection")
        print("[2] ⚡ Quick Auto Spam")
        print("[3] 📝 Custom Auto Spam")
        print("[4] 🔑 Show Credentials")
        print("[0] ❌ Exit")
        
        choice = input(f"{Colors.GREEN}\n[+] Select menu: {Colors.RESET}")
        
        if choice == "1":
            test_ultramsg()
        elif choice == "2":
            quick_auto_spam()
        elif choice == "3":
            custom_auto_spam()
        elif choice == "4":
            show_credentials()
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
