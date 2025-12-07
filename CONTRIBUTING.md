🤝 Contributing to Raven-stars-omega / راهنمای مشارکت
We welcome contributions from researchers, developers, and enthusiasts interested in cognitive architectures, semantic measurement, and the philosophical underpinnings of ATCA. Please follow these guidelines to ensure a smooth contribution process.
ما از مشارکت محققان، توسعه‌دهندگان و علاقه‌مندان به معماری‌های شناختی، سنجش معنایی و مبانی فلسفی ATCA استقبال می‌کنیم. لطفاً برای اطمینان از یک فرآیند مشارکت روان، این دستورالعمل‌ها را دنبال کنید.
Getting Started / شروع به کار
1. Setup / راه‌اندازی
We strongly recommend using the provided setup script to initialize your development environment:
توصیه می‌کنیم برای راه‌اندازی محیط توسعه خود از اسکریپت زیر استفاده کنید:
# Clone the repository
git clone [https://github.com/amirraven708-png/Raven-stars-omega.git](https://github.com/amirraven708-png/Raven-stars-omega.git)
cd Raven-stars-omega

# Run the setup script (creates virtual environment and installs dependencies)
./scripts/setup_dev.sh

2. Fork and Branch / فورک و شاخه
 * Fork the repository on GitHub.
 * Clone your fork locally.
 * Create a new branch for your feature or fix:
   git checkout -b feature/your-awesome-feature
   or git checkout -b fix/bug-description
 * مخزن را در GitHub فورک (Fork) کنید.
 * فورک خود را به صورت محلی کلون (Clone) کنید.
 * یک شاخه جدید برای قابلیت یا رفع مشکل خود ایجاد کنید:
   git checkout -b feature/your-awesome-feature
   یا git checkout -b fix/bug-description
Submission Process / فرآیند ارسال
1. Style Guide / راهنمای استایل
We use Black for code formatting and enforce strict typing using MyPy. Your code must pass all formatting and type checks.
ما از Black برای قالب‌بندی کد و از MyPy برای بررسی تایپ‌های سخت‌گیرانه استفاده می‌کنیم. کد شما باید از تمام بررسی‌های قالب‌بندی و تایپ عبور کند.
# Format your code using Black
black src tests

# Check types using MyPy
mypy src

2. Testing / تست‌نویسی
All new features or bug fixes must include corresponding tests in the tests/ directory.
تمام قابلیت‌های جدید یا رفع اشکال‌ها باید شامل تست‌های مربوطه در پوشه tests/ باشند.
# Run all tests
pytest tests/ -v

3. Commit Messages / پیام‌های کامیت
We follow the Conventional Commits specification. Use clear prefixes:
ما از استاندارد Conventional Commits پیروی می‌کنیم. از پیشوندهای واضح استفاده کنید:
| Prefix (پیشوند) | Meaning (معنی) | Example (مثال) |
|---|---|---|
| feat: | A new feature | feat: Add Golden Zone detection logic |
| fix: | A bug fix | fix: Resolve race condition in Amir's Time |
| docs: | Documentation changes | docs: Update architecture guide |
| refactor: | Code change that neither fixes a bug nor adds a feature | refactor: Simplify RAM16 initialization |
| chore: | Maintenance tasks | chore: Update black configuration |
🎯 Code of Conduct / منشور اخلاقی
Please review and abide by the Code of Conduct. We are committed to providing a harassment-free environment for everyone.
لطفاً منشور اخلاقی را بررسی کرده و به آن پایبند باشید. ما متعهد به فراهم کردن محیطی عاری از آزار و اذیت برای همه هستیم.
