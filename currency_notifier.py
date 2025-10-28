import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os
from time import sleep

# Configuration - These should be set as environment variables for security
API_KEY = os.getenv('EXCHANGE_API_KEY', 'your_api_key_here')
BASE_CURRENCY = 'USD'
TARGET_CURRENCIES = ['GBP', 'EUR']

# Email configuration
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
SENDER_EMAIL = os.getenv('SENDER_EMAIL', 'your_email@gmail.com')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD', 'your_app_password')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', 'recipient@example.com')


def fetch_exchange_rates():
    """
    Fetches current exchange rates from the API.
    Returns a dictionary with currency codes and their rates.
    """
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}'
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get('result') == 'success':
            return data.get('conversion_rates', {})
        else:
            print(f"API Error: {data.get('error-type', 'Unknown error')}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch rates: {e}")
        return None


def format_rate_message(rates):
    """
    Formats the exchange rates into a readable email message.
    """
    if not rates:
        return None
    
    # Get current date and time for the report
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    message_lines = [
        f"Currency Exchange Rates Report - {current_time}",
        "=" * 50,
        f"\nBase Currency: {BASE_CURRENCY}\n"
    ]
    
    # Add rates for each target currency
    for currency in TARGET_CURRENCIES:
        if currency in rates:
            rate = rates[currency]
            message_lines.append(f"1 {BASE_CURRENCY} = {rate:.4f} {currency}")
        else:
            message_lines.append(f"{currency}: Rate not available")
    
    # Calculate some useful conversions
    message_lines.append("\n" + "=" * 50)
    message_lines.append("\nCommon Conversions:")
    
    for currency in TARGET_CURRENCIES:
        if currency in rates:
            rate = rates[currency]
            for amount in [100, 500, 1000]:
                converted = amount * rate
                message_lines.append(
                    f"{amount} {BASE_CURRENCY} = {converted:.2f} {currency}"
                )
    
    return "\n".join(message_lines)


def send_email_notification(subject, body):
    """
    Sends an email with the exchange rate information.
    """
    if not body:
        print("No message body to send")
        return False
    
    try:
        # Create message container
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        
        # Add the message body
        text_part = MIMEText(body, 'plain')
        msg.attach(text_part)
        
        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        
        print(f"Email sent successfully to {RECIPIENT_EMAIL}")
        return True
        
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
        return False
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


def main():
    """
    Main function that orchestrates the currency rate notification process.
    """
    print("Starting currency rate notifier...")
    
    # Step 1: Fetch the latest exchange rates
    print("Fetching exchange rates...")
    rates = fetch_exchange_rates()
    
    if not rates:
        print("Could not retrieve exchange rates. Exiting.")
        return
    
    # Step 2: Format the message
    print("Formatting rate information...")
    message_body = format_rate_message(rates)
    
    # Step 3: Send the email
    print("Sending email notification...")
    subject = f"Daily Currency Rates - {datetime.now().strftime('%Y-%m-%d')}"
    success = send_email_notification(subject, message_body)
    
    if success:
        print("Currency rate notification completed successfully!")
    else:
        print("Failed to complete currency rate notification.")


if __name__ == "__main__":
    main()
