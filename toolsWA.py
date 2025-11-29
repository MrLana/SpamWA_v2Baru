# WhatsApp Auto Spam Tool with PyWhatKit
# Created by: mrLana

import pywhatkit as kit
import time
import random
from datetime import datetime, timedelta

def banner():
    print("""
    
 ██████  ██  █████  ███    ███ 
██    ██ ██ ██   ██ ████  ████ 
██    ██ ██ ███████ ██ ████ ██ 
██    ██ ██ ██   ██ ██  ██  ██ 
 ██████  ██ ██   ██ ██      ██ 
                               
    """)
    print("🚀 WhatsApp Auto Spam Tool")
    print("📱 Created by: mrLana")
    print("=" * 40)

def send_instant_message(phone, message):
    """Mengirim pesan instan"""
    try:
        kit.sendwhatmsg_instantly(
            phone_no=phone,
            message=message,
            wait_time=15,
            tab_close=True
        )
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def send_scheduled_message(phone, message, hours, minutes):
    """Mengirim pesan terjadwal"""
    try:
        kit.sendwhatmsg(
            phone_no=phone,
            message=message,
            time_hour=hours,
            time_min=minutes,
            wait_time=15,
            tab_close=True
        )
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def quick_auto_spam():
    """Mode spam cepat"""
    print("\n[⚡] MODE SPAM CEPAT")
    
    phone = input("[+] Nomor target (contoh: +628123456789): ").strip()
    if not phone:
        print("❌ Nomor tidak boleh kosong!")
        return
    
    # Predefined messages
    spam_messages = [
        "😂 SPAM BOT BY MRLANA 😂",
        "🚀 PESAN OTOMATIS TERKIRIM 🚀",
        "💥 BOT SEDANG BERJALAN 💥",
        "🎯 PESAN DARI PYTHON BOT 🎯",
        "⚡ AUTO SENDER ACTIVATED ⚡",
        "🔥 PYWHATKIT POWER 🔥",
        "💻 CREATED BY MRLANA 💻",
        "🐍 PYTHON WHATSAPP BOT 🐍"
    ]
    
    try:
        count = int(input("[+] Jumlah pesan: "))
        delay = int(input("[+] Delay antar pesan (detik): ") or "2")
        
        print(f"\n📤 Mengirim {count} pesan ke {phone}...")
        print("⚠️ Pastikan WhatsApp Web terbuka di browser!")
        input("\n[!] Press Enter untuk mulai...")
        
        success = 0
        for i in range(count):
            message = random.choice(spam_messages)
            print(f"\n📤 Pesan {i+1}/{count}: {message}")
            
            if send_instant_message(phone, f"{message} #{i+1}"):
                success += 1
                print("✅ Berhasil dikirim!")
            else:
                print("❌ Gagal mengirim!")
            
            if i < count - 1:
                print(f"⏳ Menunggu {delay} detik...")
                time.sleep(delay)
        
        print(f"\n🎉 Selesai! {success}/{count} pesan terkirim!")
        
    except ValueError:
        print("❌ Input tidak valid!")
    except Exception as e:
        print(f"❌ Error: {e}")

def custom_auto_spam():
    """Mode spam custom"""
    print("\n[📝] MODE SPAM CUSTOM")
    
    phone = input("[+] Nomor target (contoh: +628123456789): ").strip()
    if not phone:
        print("❌ Nomor tidak boleh kosong!")
        return
    
    print("\n💬 Pilihan pesan:")
    print("[1] Pesan tunggal berulang")
    print("[2] Multiple pesan berbeda")
    print("[3] Pesan berhitung")
    
    choice = input("[+] Pilih tipe pesan: ")
    
    try:
        if choice == "1":
            single_message_spam(phone)
        elif choice == "2":
            multiple_messages_spam(phone)
        elif choice == "3":
            counting_spam(phone)
        else:
            print("❌ Pilihan tidak valid!")
    except Exception as e:
        print(f"❌ Error: {e}")

def single_message_spam(phone):
    """Pesan tunggal berulang"""
    message = input("[+] Masukkan pesan: ")
    count = int(input("[+] Jumlah pengulangan: "))
    delay = int(input("[+] Delay (detik): ") or "2")
    
    print(f"\n📤 Mengirim '{message}' sebanyak {count} kali...")
    input("[!] Press Enter untuk mulai...")
    
    success = 0
    for i in range(count):
        print(f"\n📤 Pengiriman {i+1}/{count}")
        
        if send_instant_message(phone, f"{message} #{i+1}"):
            success += 1
            print("✅ Berhasil!")
        else:
            print("❌ Gagal!")
        
        if i < count - 1:
            print(f"⏳ Delay {delay} detik...")
            time.sleep(delay)
    
    print(f"\n🎉 {success}/{count} pesan terkirim!")

def multiple_messages_spam(phone):
    """Multiple pesan berbeda"""
    num_messages = int(input("[+] Berapa banyak pesan berbeda: "))
    
    messages = []
    for i in range(num_messages):
        msg = input(f"[+] Pesan {i+1}: ")
        messages.append(msg)
    
    repeat = int(input("[+] Ulang sequence berapa kali: ") or "1")
    delay = int(input("[+] Delay (detik): ") or "2")
    
    total = len(messages) * repeat
    print(f"\n📤 Total {total} pesan akan dikirim...")
    input("[!] Press Enter untuk mulai...")
    
    success = 0
    for r in range(repeat):
        for i, msg in enumerate(messages):
            print(f"\n🔄 Sequence {r+1}/{repeat} - Pesan {i+1}/{len(messages)}")
            
            if send_instant_message(phone, f"{msg} [S:{r+1}-P:{i+1}]"):
                success += 1
                print("✅ Berhasil!")
            else:
                print("❌ Gagal!")
            
            if not (r == repeat-1 and i == len(messages)-1):
                print(f"⏳ Delay {delay} detik...")
                time.sleep(delay)
    
    print(f"\n🎉 {success}/{total} pesan terkirim!")

def counting_spam(phone):
    """Pesan berhitung"""
    base_msg = input("[+] Pesan dasar: ")
    count = int(input("[+] Jumlah pesan: "))
    delay = int(input("[+] Delay (detik): ") or "2")
    
    print(f"\n🔢 Mengirim {count} pesan berhitung...")
    input("[!] Press Enter untuk mulai...")
    
    success = 0
    for i in range(count):
        message = f"{base_msg} {i+1}"
        print(f"\n🔢 Pesan {i+1}/{count}: {message}")
        
        if send_instant_message(phone, message):
            success += 1
            print("✅ Berhasil!")
        else:
            print("❌ Gagal!")
        
        if i < count - 1:
            print(f"⏳ Delay {delay} detik...")
            time.sleep(delay)
    
    print(f"\n🎉 {success}/{count} pesan terkirim!")

def scheduled_messages():
    """Pesan terjadwal"""
    print("\n[⏰] MODE PESAN TERJADWAL")
    
    phone = input("[+] Nomor target: ").strip()
    if not phone:
        print("❌ Nomor tidak boleh kosong!")
        return
    
    message = input("[+] Pesan: ")
    count = int(input("[+] Jumlah pesan: "))
    interval = int(input("[+] Interval menit antar pesan: ") or "1")
    
    # Waktu sekarang
    now = datetime.now()
    print(f"\n⏰ Waktu sekarang: {now.strftime('%H:%M')}")
    
    start_hour = int(input("[+] Jam mulai (0-23): "))
    start_minute = int(input("[+] Menit mulai (0-59): "))
    
    print(f"\n📅 Mengirim {count} pesan mulai {start_hour:02d}:{start_minute:02d}")
    input("[!] Press Enter untuk konfirmasi...")
    
    success = 0
    current_time = datetime.now().replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
    
    for i in range(count):
        print(f"\n⏰ Pesan {i+1} dijadwalkan: {current_time.strftime('%H:%M')}")
        
        try:
            kit.sendwhatmsg(
                phone_no=phone,
                message=f"{message} #{i+1}",
                time_hour=current_time.hour,
                time_min=current_time.minute,
                wait_time=15,
                tab_close=True
            )
            success += 1
            print("✅ Berhasil dijadwalkan!")
        except Exception as e:
            print(f"❌ Gagal: {e}")
        
        # Tambah interval untuk pesan berikutnya
        current_time += timedelta(minutes=interval)
    
    print(f"\n🎉 {success}/{count} pesan berhasil dijadwalkan!")

def show_help():
    """Menampilkan bantuan"""
    print("""
📖 CARA PENGGUNAAN:

1. **Pastikan:**
   - WhatsApp Web sudah login di browser
   - Browser tidak dalam mode incognito
   - Koneksi internet stabil

2. **Format Nomor:**
   - Gunakan format internasional
   - Contoh: +628123456789

3. **Proses:**
   - Program akan buka browser otomatis
   - Tunggu hingga halaman WhatsApp load
   - Pesan akan terkirim otomatis
   - Tab browser akan tertutup sendiri

4. **Tips:**
   - Gunakan delay minimal 2 detik
   - Jangan spam berlebihan
   - Untuk testing, gunakan nomor sendiri

⚠️  PERINGATAN:
   - Jangan disalahgunakan!
   - Resiko ditanggung pengguna
   - Untuk edukasi dan testing saja
    """)
    input("\n[+] Press Enter untuk kembali...")

def main_menu():
    """Menu utama"""
    while True:
        banner()
        
        print("🏠 MENU UTAMA:")
        print("[1] ⚡ Spam Cepat (Pesan Random)")
        print("[2] 📝 Spam Custom (Pesan Custom)")
        print("[3] ⏰ Pesan Terjadwal")
        print("[4] 📖 Cara Penggunaan")
        print("[0] ❌ Keluar")
        
        choice = input("\n[+] Pilih menu: ")
        
        if choice == "1":
            quick_auto_spam()
        elif choice == "2":
            custom_auto_spam()
        elif choice == "3":
            scheduled_messages()
        elif choice == "4":
            show_help()
        elif choice == "0":
            print("\n👋 Terima kasih telah menggunakan WhatsApp Auto Tool!")
            break
        else:
            print("❌ Pilihan tidak valid!")
            time.sleep(1)
        
        # Tanya apakah lanjut
        if choice != "0":
            cont = input("\n[+] Lanjutkan? (y/n): ").lower()
            if cont != 'y':
                print("👋 Sampai jumpa!")
                break

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n❌ Program dihentikan oleh user")
    except Exception as e:
        print(f"\n❌ Error: {e}")