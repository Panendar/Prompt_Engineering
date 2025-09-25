# prompt_Engineering

A Python-based FAQ template builder that generates customer support prompts for AI assistants. This tool creates structured prompts for customer service scenarios across different business areas.

## 📁 Project Structure

```
prompt_Engineering/
├── .gitignore              # Git ignore rules (includes .env)
├── FAQ_temp.builder.py     # Main FAQ template builder script
└── README.md              # Project documentation
```

> **⚠️ Important**: The `.env` file containing actual API keys is not included in this repository for security reasons. You'll need to create your own environment file as described in the setup instructions below.

## 🚀 Features

- **Interactive Input**: Prompts user for question and company name
- **Predefined Examples**: Includes sample FAQs for various categories:
  - Orders (cancellation, tracking)
  - Refunds (initiation, process)
  - Discounts (student discounts)
  - Shipping (delivery times)
  - Account (profile management)
  - Policies (company policies)
- **Template Generation**: Creates structured prompts for AI customer support
- **Customizable Tone**: Uses polite tone with response length limits

## 🛠️ Setup

### Prerequisites

- Python 3.x
- Required packages (commented out in current version):
  - `requests`
  - `python-dotenv`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/prompt_Engineering.git
   cd prompt_Engineering
   ```

2. **Create your environment file**:

   Create a `.env` file in the project root with your API key:

   ```bash
   # For Windows PowerShell
   echo 'my_api = "your_actual_api_key_here"' | Out-File -FilePath .env -Encoding utf8

   # For Linux/Mac or Git Bash
   echo 'my_api = "your_actual_api_key_here"' > .env
   ```

   Replace `your_actual_api_key_here` with your actual Perplexity AI API key from https://www.perplexity.ai/

3. Install dependencies (if using API features):
   ```bash
   pip install requests python-dotenv
   ```

> **🔐 Security Note**: Never commit your `.env` file to version control. It contains sensitive API keys that should remain private.

## 📋 Usage

### Basic Usage (Current Configuration)

```bash
python FAQ_temp.builder.py
```

The script will:

1. Prompt for your question
2. Ask for company name
3. Generate and display a formatted FAQ template prompt

### Example Output

```
Please enter your question here: How can I cancel my order?
Please enter the company name here: Amazon

Generated Prompt:
You are a customer support assistant for Amazon.
Always keep your response polite and limit it to **1–2 sentences maximum**.

[Examples from predefined FAQ categories]

Customer Question: "How can I cancel my order?"

Final Answer:
```

## 🔧 Configuration

### Environment Variables

**⚠️ Security Notice**: The `.env` file is excluded from version control for security reasons.

1. **Copy the example file**:

   ```bash
   cp .env.example .env
   ```

2. **Edit your `.env` file** and add your API key:

   ```
   my_api = "your_actual_api_key_here"
   ```

3. **Never commit the `.env` file** - it contains sensitive information and is already in `.gitignore`

### API Key Setup

- Get your API key from [Perplexity AI](https://www.perplexity.ai/)
- Replace `"your_actual_api_key_here"` with your real API key
- Keep your API key private and never share it publicly

### FAQ Categories

The script includes predefined examples for:

- **Orders**: Cancellation and tracking queries
- **Refunds**: Process and initiation steps
- **Discounts**: Student and promotional offers
- **Shipping**: Delivery timeframes and logistics
- **Account**: Profile and settings management
- **Policies**: Company terms and conditions

## 📝 File Descriptions

### `FAQ_temp.builder.py`

Main script containing:

- FAQ example data structure
- User input handlers
- Template formatting logic
- API integration code (currently commented out)

### `.env` (Not included in repository)

Environment configuration file that you need to create locally:

- Contains sensitive API keys for external services
- Should never be committed to version control
- Use `.env.example` as a template for creating your own

### `.env.example`

Template file showing the required environment variables without sensitive data.

## 🔮 Future Enhancements

The codebase includes commented sections for:

- API integration with Perplexity AI
- Automated response generation
- Error handling and validation
- Response formatting and display

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is available for educational and personal use.

---

**Note**: The current version focuses on prompt generation. API integration features are commented out and can be enabled by uncommenting the relevant sections and ensuring proper dependencies are installed.
