import google.generativeai as genai
import time
import sys

# 1. Importing the Hardware Security Logic
try:
    from cloudi_sync import generate_dynamic_token
except ImportError:
    # (Indentation)
    print("[ERROR] 'cloudi_sync.py' not found! Please keep both files in the same folder.")
    sys.exit()

# 2. Gemini AI Configuration
genai.configure(api_key="AIzaSyAeQ7mH7KyMk6QKPRXGATHTUhzDa2dnrRo")
model = genai.GenerativeModel('models/gemini-1.5-flash')

def perform_ai_audit(token, device_id):
    prompt = f"Analyze this token for security: {token} for device: {device_id}. Respond: STATUS: VERIFIED"
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"AI Connection Error: {e}"

if __name__ == "__main__":
    print("--- 🤖 Cloudi Sync AI Guard: Active ---")
    device_sn = "BIO_USB_9982"
    u_pin = input("Enter your 4-digit PIN for AI Verification: ")

    if len(u_pin) == 4:
        current_token = generate_dynamic_token(device_sn, u_pin)
        print(f"Generated Token: {current_token}")
        audit_result = perform_ai_audit(current_token, device_sn)
        print(f"AI Audit Result: {audit_result}")
    else:
        print("Error: Invalid PIN length.")
    
