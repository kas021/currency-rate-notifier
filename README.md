# Currency Rate Notifier 💱

![Currency Exchange](https://raw.githubusercontent.com/kas021/currency-rate-notifier/main/currency-banner.svg)

A Python automation tool that fetches live currency exchange rates (GBP, USD, EUR) and delivers them straight to your inbox. Perfect for travelers, forex traders, or anyone keeping tabs on international currencies.

## ✨ Features

- **Real-time Exchange Rates**: Pulls the latest currency data from a reliable API
- **Multiple Currencies**: Tracks GBP, USD, and EUR conversions
- **Email Notifications**: Sends formatted reports directly to your email
- **Flexible Scheduling**: Run manually or set up automated daily checks
- **Secure Configuration**: Uses environment variables for sensitive data
- **Common Conversions**: Includes helpful conversion amounts (100, 500, 1000)

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- A Gmail account (or other SMTP-compatible email service)
- API key from [ExchangeRate-API](https://www.exchangerate-api.com/) (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kas021/currency-rate-notifier.git
   cd currency-rate-notifier
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the project root:
   ```env
   EXCHANGE_API_KEY=your_api_key_here
   SENDER_EMAIL=your_email@gmail.com
   SENDER_PASSWORD=your_app_password
   RECIPIENT_EMAIL=recipient@example.com
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   ```

   > **Note for Gmail users**: You'll need to create an [App Password](https://support.google.com/accounts/answer/185833) instead of using your regular password.

4. **Run the script**
   ```bash
   python currency_notifier.py
   ```

## 📧 Email Setup

### Gmail Configuration

1. Enable 2-factor authentication on your Google account
2. Generate an App Password:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Create a new app password for "Mail"
   - Use this password in your `.env` file

### Other Email Providers

Update the `SMTP_SERVER` and `SMTP_PORT` in your `.env` file:

- **Outlook/Hotmail**: `smtp.office365.com`, port `587`
- **Yahoo**: `smtp.mail.yahoo.com`, port `587`
- **Custom SMTP**: Check your provider's documentation

## ⚙️ Configuration

You can customize the script by modifying these variables in `currency_notifier.py`:

- `BASE_CURRENCY`: The reference currency (default: USD)
- `TARGET_CURRENCIES`: List of currencies to track (default: GBP, EUR)

## 🔄 Automation

### Using Cron (Linux/Mac)

Run daily at 9 AM:
```bash
0 9 * * * cd /path/to/currency-rate-notifier && python3 currency_notifier.py
```

### Using Task Scheduler (Windows)

1. Open Task Scheduler
2. Create a new task
3. Set trigger to daily at your preferred time
4. Set action to run `python.exe` with argument pointing to `currency_notifier.py`

### Using GitHub Actions

Check the `.github/workflows/daily-rates.yml` file for an automated cloud-based solution.

## 📊 Sample Output

You'll receive an email like this:

```
Currency Exchange Rates Report - 2025-10-28 09:00:00
==================================================

Base Currency: USD

1 USD = 0.7834 GBP
1 USD = 0.9124 EUR

==================================================

Common Conversions:
100 USD = 78.34 GBP
500 USD = 391.70 GBP
1000 USD = 783.40 GBP
100 USD = 91.24 EUR
500 USD = 456.20 EUR
1000 USD = 912.40 EUR
```

## 🔒 Security Notes

- **Never commit your `.env` file** to version control
- Keep your API keys and passwords secure
- Use environment variables for all sensitive data
- Consider using a dedicated email account for automated notifications

## 🛠️ Troubleshooting

**API Errors**: Verify your API key is valid and hasn't exceeded rate limits

**Email Not Sending**: 
- Check your SMTP credentials
- Ensure you're using an app password (not your regular password)
- Verify firewall isn't blocking port 587

**Module Not Found**: Run `pip install -r requirements.txt` again

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📬 Contact

Questions or suggestions? Open an issue or reach out through GitHub.

---

**Made with ❤️ for currency enthusiasts**
