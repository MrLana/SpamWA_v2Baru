# WhatsApp Auto Send - Ultramsg API
# Created by: mrLana
# Using Your Ultramsg Credentials

import http.client
import ssl
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
    print(f"{Colors.MAGENTA}⚡ Instance: instance153232{Colors.RESET}")
    print()

class UltramsgSender:
    def __init__(self):
        self.instance_id = "instance153232"
        self.token = "01snpp492l4wxz3c"
        self.base_url = "api.ultramsg.com"
    
    def send_message(self, phone, message):
        """Send message using Ultramsg API"""
        try:
            # Create HTTPS connection
            conn = http.client.HTTPSConnection(self.base_url, context=ssl._create_unverified_context())
            
            # Prepare payload
            payload = f"token={self.token}&to={phone}&body={message}"
            payload = payload.encode('utf8').decode('iso-8859-1')
            
            headers = {'content-type': "application/x-www-form-urlencoded"}
            
            # API endpoint
            endpoint = f"/{self.instance_id}/messages/chat"
            
            print(f"{Colors.CYAN}📤 Sending to {phone}...{Colors.RESET}")
            print(f"{Colors.CYAN}💬 Message: {message}{Colors.RESET}")
            
            # Send request
            conn.request("POST", endpoint, payload, headers)
            
            # Get response
            res = conn.getresponse()
            data = res.read()
            result = data.decode("utf-8")
            
            print(f"{Colors.GREEN}📡 API Response: {result}{Colors.RESET}")
            
            # Parse JSON response
            try:
                result_json = json.loads(result)
                if result_json.get('sent') == 'true':
                    print(f"{Colors.GREEN}✅ Message sent successfully!{Colors.RESET}")
                    return True
                else:
                    error_msg = result_json.get('error', 'Unknown error')
                    print(f"{Colors.RED}❌ Failed: {error_msg}{Colors.RESET}")
                    return False
            except:
                if '"sent":"true"' in result:
                    print(f"{Colors.GREEN}✅ Message sent successfully!{Colors.RESET}")
                    return True
                else:
                    print(f"{Colors.RED}❌ Failed to send message{Colors.RESET}")
                    return False
                
        except Exception as e:
            print(f"{Colors.RED}❌ Error: {str(e)}{Colors.RESET}")
            return False

def test_connection():
    """Test Ultramsg connection"""
    print(f"{Colors.MAGENTA}\n[🧪] TEST ULTRAMSG CONNECTION{Colors.RESET}")
    
    sender = UltramsgSender()
    
    print(f"{Colors.YELLOW}🔧 Testing credentials...{Colors.RESET}")
    print(f"{Colors.GREEN}🆔 Instance: {sender.instance_id}{Colors.RESET}")
    print(f"{Colors.GREEN}🔑 Token: {sender.token}{Colors.RESET}")
    
    # Test number
    test_number = "+6285929887092"
    test_message = "🔥 Test message from Ultramsg API - mrLana Bot"
    
    print(f"{Colors.YELLOW}📱 Test Number: {test_number}{Colors.RESET}")
    print(f"{Colors.CYAN}💬 Test Message: {test_message}{Colors.RESET}")
    
    input(f"{Colors.GREEN}[+] Press Enter to test...{Colors.RESET}")
    
    if sender.send_message(test_number, test_message):
        print(f"{Colors.GREEN}🎉 ULTRAMSG CONNECTION SUCCESSFUL!{Colors.RESET}")
    else:
        print(f"{Colors.RED}❌ ULTRAMSG CONNECTION FAILED{Colors.RESET}")

def quick_spam():
    """Quick auto spam"""
    print(f"{Colors.MAGENTA}\n[⚡] QUICK AUTO SPAM{Colors.RESET}")
    
    sender = UltramsgSender()
    
    phone = input(f"{Colors.GREEN}[+] Enter target number (with +): {Colors.RESET}").strip()
    if not phone:
        print(f"{Colors.RED}❌ Phone number required!{Colors.RESET}")
        return
    
    spam_messages = [
        "🚀 AUTO SEND VIA ULTRAMSG",
        "💻 Instance: instance153232", 
        "📱 Created by: mrLana",
        "⚡ FULLY AUTOMATIC",
        "🎯 NO MANUAL CLICK",
        "🔥 ULTRAMSG API WORKING",
        "💥 INSTANT DELIVERY",
        "🎪 AUTO MESSAGE SYSTEM"
    ]
    
    try:
        count = int(input(f"{Colors.GREEN}[+] Number of messages: {Colors.RESET}"))
        delay = int(input(f"{Colors.GREEN}[+] Delay between messages (seconds): {Colors.RESET}") or "3")
        
        print(f"{Colors.YELLOW}\n🚀 Starting Auto Spam...{Colors.RESET}")
        print(f"{Colors.YELLOW}📱 Target: {phone}{Colors.RESET}")
        print(f"{Colors.YELLOW}📤 Count: {count} messages{Colors.RESET}")
        print(f"{Colors.YELLOW}⏰ Delay: {delay} seconds{Colors.RESET}")
        
        input(f"{Colors.RED}\n[!] Press Enter to START...{Colors.RESET}")
        
        success = 0
        for i in range(count):
            message = random.choice(spam_messages)
            print(f"{Colors.CYAN}\n📤 Sending {i+1}/{count}{Colors.RESET}")
            
            if sender.send_message(phone, f"{message} #{i+1}"):
                success += 1
            
            if i < count - 1:
                print(f"{Colors.YELLOW}⏳ Waiting {delay} seconds...{Colors.RESET}")
                time.sleep(delay)
        
        print(f"{Colors.GREEN}\n🎉 COMPLETE! {success}/{count} messages sent!{Colors.RESET}")
        
    except ValueError:
        print(f"{Colors.RED}❌ Invalid input!{Colors.RESET}")

def custom_spam():
    """Custom spam"""
    print(f"{Colors.MAGENTA}\n[📝] CUSTOM SPAM{Colors.RESET}")
    
    sender = UltramsgSender()
    
    phone = input(f"{Colors.GREEN}[+] Enter target number (with +): {Colors.RESET}").strip()
    if not phone:
        print(f"{Colors.RED}❌ Phone number required!{Colors.RESET}")
        return
    
    print(f"{Colors.YELLOW}\n📝 Message Type:{Colors.RESET}")
    print("[1] Single message (repeated)")
    print("[2] Multiple messages")
    print("[3] Counting messages")
    
    choice = input(f"{Colors.GREEN}[+] Select: {Colors.RESET}")
    
    try:
        if choice == "1":
            message = input(f"{Colors.GREEN}[+] Enter message: {Colors.RESET}")
            count = int(input(f"{Colors.GREEN}[+] Repeat count: {Colors.RESET}"))
            delay = int(input(f"{Colors.GREEN}[+] Delay (seconds): {Colors.RESET}") or "3")
            
            print(f"{Colors.YELLOW}\n📤 Sending '{message}' {count} times...{Colors.RESET}")
            input(f"{Colors.GREEN}[+] Press Enter to start...{Colors.RESET}")
            
            success = 0
            for i in range(count):
                print(f"{Colors.CYAN}\n🔄 Sending {i+1}/{count}{Colors.RESET}")
                if sender.send_message(phone, f"{message} [#{i+1}]"):
                    success += 1
                if i < count - 1:
                    time.sleep(delay)
            
            print(f"{Colors.GREEN}\n🎉 {success}/{count} sent!{Colors.RESET}")
            
        elif choice == "2":
            num_msg = int(input(f"{Colors.GREEN}[+] How many different messages: {Colors.RESET}"))
            messages = []
            for i in range(num_msg):
                msg = input(f"{Colors.GREEN}[+] Message {i+1}: {Colors.RESET}")
                messages.append(msg)
            
            repeat = int(input(f"{Colors.GREEN}[+] Repeat sequence: {Colors.RESET}") or "1")
            delay = int(input(f"{Colors.GREEN}[+] Delay (seconds): {Colors.RESET}") or "3")
            
            total = len(messages) * repeat
            print(f"{Colors.YELLOW}\n📤 Total {total} messages...{Colors.RESET}")
            input(f"{Colors.GREEN}[+] Press Enter to start...{Colors.RESET}")
            
            success = 0
            for r in range(repeat):
                for i, msg in enumerate(messages):
                    print(f"{Colors.CYAN}\n🔢 Seq {r+1}/{repeat} - Msg {i+1}/{len(messages)}{Colors.RESET}")
                    if sender.send_message(phone, f"{msg} [S:{r+1}-M:{i+1}]"):
                        success += 1
                    if not (r == repeat-1 and i == len(messages)-1):
                        time.sleep(delay)
            
            print(f"{Colors.GREEN}\n🎉 {success}/{total} sent!{Colors.RESET}")
            
        elif choice == "3":
            base_msg = input(f"{Colors.GREEN}[+] Base message: {Colors.RESET}")
            count = int(input(f"{Colors.GREEN}[+] Number of messages: {Colors.RESET}"))
            delay = int(input(f"{Colors.GREEN}[+] Delay (seconds): {Colors.RESET}") or "3")
            
            print(f"{Colors.YELLOW}\n🔢 Sending {count} counting messages...{Colors.RESET}")
            input(f"{Colors.GREEN}[+] Press Enter to start...{Colors.RESET}")
            
            success = 0
            for i in range(count):
                message = f"{base_msg} {i+1}"
                print(f"{Colors.CYAN}\n🔢 Message {i+1}/{count}{Colors.RESET}")
                if sender.send_message(phone, message):
                    success += 1
                if i < count - 1:
                    time.sleep(delay)
            
            print(f"{Colors.GREEN}\n🎉 {success}/{count} sent!{Colors.RESET}")
            
        else:
            print(f"{Colors.RED}❌ Invalid choice!{Colors.RESET}")
            
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")

def show_info():
    """Show Ultramsg info"""
    print(f"{Colors.MAGENTA}\n[🔑] ULTRAMSG INFORMATION{Colors.RESET}")
    
    sender = UltramsgSender()
    print(f"{Colors.GREEN}🌐 API URL: https://api.ultramsg.com/{Colors.RESET}")
    print(f"{Colors.GREEN}🆔 Instance ID: {sender.instance_id}{Colors.RESET}")
    print(f"{Colors.GREEN}🔑 Token: {sender.token}{Colors.RESET}")
    print(f"{Colors.YELLOW}📱 Your Number: +6285929887092{Colors.RESET}")
    print(f"{Colors.CYAN}💡 Status: ACTIVE{Colors.RESET}")
    
    input(f"{Colors.GREEN}\n[+] Press Enter to continue...{Colors.RESET}")

def main_menu():
    """Main menu"""
    while True:
        banner()
        
        print(f"{Colors.YELLOW}🏠 MAIN MENU:{Colors.RESET}")
        print("[1] 🧪 Test Connection")
        print("[2] ⚡ Quick Spam")
        print("[3] 📝 Custom Spam")
        print("[4] 🔑 Show Info")
        print("[0] ❌ Exit")
        
        choice = input(f"{Colors.GREEN}\n[+] Select: {Colors.RESET}")
        
        if choice == "1":
            test_connection()
        elif choice == "2":
            quick_spam()
        elif choice == "3":
            custom_spam()
        elif choice == "4":
            show_info()
        elif choice == "0":
            print(f"{Colors.RED}\n👋 Thank you!{Colors.RESET}")
            break
        else:
            print(f"{Colors.RED}❌ Invalid!{Colors.RESET}")
        
        if choice != "0":
            input(f"{Colors.GREEN}\n[+] Continue? (Enter){Colors.RESET}")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"{Colors.RED}\n\n❌ Stopped{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}\n❌ Error: {e}{Colors.RESET}")
