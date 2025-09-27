# Simple Business Chatbot

A Python-based AI chatbot that provides specific, actionable responses to business enquiries. Built using LangChain and Ollama with the Gemma 2B model for efficient local AI processing.

## 📁 Project Structure

```
prompt_Engineering/
├── .gitignore                 # Git ignore rules
├── basic_chatbot.py          # Main business chatbot script
├── FAQ_temp.builder.py       # FAQ template builder (legacy)
└── README.md                 # Project documentation
```

## 🚀 Features

- **AI-Powered Responses**: Uses Gemma 2B model via Ollama for intelligent responses
- **Business Focus**: Specialized for handling business enquiries (orders, returns, support)
- **Specific Answers**: Provides actionable solutions instead of generic "contact support" responses
- **Company Customization**: Personalizes responses based on company name and business area
- **Memory Efficient**: Uses lightweight Gemma 2B model (1.7GB) optimized for local systems
- **Interactive Interface**: Clean command-line interface with proper error handling

## 🛠️ Setup

### Prerequisites

- Python 3.x
- Ollama (for running local AI models)
- Required Python packages:
  - `langchain`
  - `langchain-ollama`

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/prompt_Engineering.git
   cd prompt_Engineering
   ```

2. **Install Python dependencies**:

   ```bash
   pip install langchain langchain-ollama
   ```

3. **Install Ollama**:

   - Download from https://ollama.ai
   - Install for your operating system
   - Restart terminal after installation

4. **Install the AI model**:
   ```bash
   ollama pull gemma:2b
   ollama serve
   ```

## 📋 Usage

### Running the Chatbot

1. **Start Ollama service** (in one terminal):

   ```bash
   ollama serve
   ```

2. **Run the chatbot** (in another terminal):
   ```bash
   python basic_chatbot.py
   ```

### Example Interaction

```
✓ Connected to gemma:2b model successfully!
Welcome to BizBot! I'm here to help with business enquiries.
Please enter your company name: Amazon
Please enter your business area: Orders

Great! I'm now configured to handle enquiries for Amazon in the Orders sector.
You can ask me any business-related questions. Type 'quit' or 'exit' to end the conversation.

User: How can I cancel my order?
BizBot: You can cancel your order in several ways: 1) Log into your account on our website and go to 'My Orders' to cancel directly, 2) Call our order cancellation line at 1-800-CANCEL (available 24/7), or 3) Reply to your order confirmation email with 'CANCEL ORDER' and your order number. If your order hasn't shipped yet, cancellation is immediate and free.

User: exit
Exiting the chatbot. Goodbye!
```

## 🔧 Configuration

### Model Settings

The chatbot uses the Gemma 2B model for optimal performance:

- **Model**: `gemma:2b` (1.7GB)
- **Temperature**: 0.3 (for focused, consistent responses)
- **Memory requirement**: ~3GB RAM
- **Response style**: Specific and actionable

### Supported Business Areas

The chatbot is optimized for:

- **Orders**: Cancellation, tracking, modifications
- **Returns & Refunds**: Process guidance, status updates
- **Shipping**: Delivery information, tracking
- **Account Management**: Profile updates, login issues
- **General Support**: Product questions, policies

## 📝 File Descriptions

### `basic_chatbot.py`

Main chatbot script containing:

- AI model connection and configuration
- Business-focused prompt templates
- Interactive chat interface
- Error handling and recovery
- Company and business area customization

### `FAQ_temp.builder.py` (Legacy)

Original FAQ template builder - kept for reference but not actively used.

## 🔮 Future Improvements

<!-- Potential enhancements to make this into an all-rounder simple chatbot:
     - Add support for multiple domains (academic tutoring, software help, general Q&A)
     - Implement context memory for multi-turn conversations with better continuity -->

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with different business scenarios
5. Submit a pull request

## 📄 License

This project is available for educational and personal use.

---

**Note**: This chatbot runs entirely locally using Ollama, ensuring privacy and no API costs. The Gemma 2B model provides efficient performance suitable for most business support scenarios.
