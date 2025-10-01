# Daily Life Assistant Chatbot (Dod Bot)

A Python-based AI chatbot that provides practical, actionable advice for everyday life situations. Built using LangChain and Ollama with the Gemma 2B model for efficient local AI processing.

## 📁 Project Structure

```
prompt_Engineering/
├── daily-chatbot.py          # Main daily life assistant chatbot
├── daily-prompt.txt          # Jinja2 template for conversation prompts
├── simple-business_chatbot.py # Alternative business-focused chatbot
├── FAQ_temp.builder.py       # FAQ template builder utility
└── README.md                 # Project documentation
```

## 🚀 Features

- **Daily Life Focus**: Specialized for everyday challenges (study tips, health, productivity, etc.)
- **Practical Advice**: Provides specific, actionable solutions with 3-4 sentence responses
- **Conversation Continuity**: Maintains conversation history and asks follow-up questions
- **Template-Based Responses**: Uses Jinja2 templates for consistent, structured responses
- **Memory Efficient**: Uses lightweight Gemma 2B model (1.7GB) optimized for local systems
- **Clean Interface**: Simple command-line interface with proper error handling

## 🛠️ Setup

### Prerequisites

- Python 3.x
- Ollama (for running local AI models)
- Required Python packages:
  - `langchain-ollama`
  - `jinja2`

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Panendar/prompt_Engineering.git
   cd prompt_Engineering
   ```

2. **Install Python dependencies**:

   ```bash
   pip install langchain-ollama jinja2
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

2. **Run the daily life chatbot** (in another terminal):
   ```bash
   python daily-chatbot.py
   ```

### Example Interaction

```
✓ Connected to gemma:2b model successfully!
Welcome to Dod Bot! I'm here to help with your daily enquiries.
You can ask me any daily life-related questions. Type 'quit' or 'exit' to end the conversation.

User: How can I stay focused while studying?
Dod Bot is getting your response...
Dod Bot: Try the Pomodoro technique: work for 25 minutes, then take a 5-minute break to maintain concentration. Create a dedicated study space free from distractions like phones or social media. Use active recall methods like flashcards or teaching concepts aloud to engage your brain more effectively. What subject are you finding most challenging to focus on?

User: I want to wake up earlier but I keep oversleeping
Dod Bot is getting your response...
Dod Bot: Set your alarm across the room so you have to physically get up to turn it off. Go to bed 15 minutes earlier each night until you reach your target bedtime gradually. Expose yourself to bright light immediately upon waking to reset your circadian rhythm naturally. What time are you currently going to bed?

User: quit
Exiting the chatbot. Goodbye!
```

## 🔧 Configuration

### Model Settings

The chatbot uses the Gemma 2B model for optimal performance:

- **Model**: `gemma:2b` (1.7GB)
- **Temperature**: 0.3 (for focused, consistent responses)
- **Memory requirement**: ~3GB RAM
- **Response style**: 3-4 sentences with follow-up questions

### Template Customization

The bot uses `daily-prompt.txt` template with these response rules:

- Keep responses to exactly 3-4 sentences maximum
- Be warm, friendly, and conversational
- Give ONE specific, actionable solution
- End with a follow-up question to keep conversation going

### Supported Daily Life Areas

The chatbot provides advice for:

- **Study & Learning**: Focus techniques, time management, learning strategies
- **Health & Wellness**: Sleep, exercise, stress management, nutrition
- **Productivity**: Work habits, organization, goal setting
- **Personal Development**: Skill building, motivation, habit formation
- **Social & Relationships**: Communication, networking, friendship building
- **Financial Management**: Budgeting, saving, expense tracking

## 📝 File Descriptions

### `daily-chatbot.py`

Main daily life assistant chatbot containing:

- AI model connection and configuration (Gemma 2B)
- Jinja2 template integration for structured responses
- Interactive chat interface with conversation history
- Error handling and recovery mechanisms
- Simple, clean user experience

### `daily-prompt.txt`

Jinja2 template file containing:

- Response format rules and guidelines
- Example conversations for consistent behavior
- Template variables for question and history injection
- Conversational flow instructions

### `simple-business_chatbot.py`

Alternative business-focused chatbot for comparison.

### `FAQ_temp.builder.py`

Utility script for building FAQ templates - kept for reference.

## 🔮 Future Improvements

Potential enhancements for the daily life assistant:

- **Multi-domain Support**: Academic tutoring, career advice, hobby guidance
- **Memory Enhancement**: Better conversation context retention across sessions
- **Personalization**: User preferences and learning from interaction patterns
- **Voice Integration**: Speech-to-text and text-to-speech capabilities
- **Mobile App**: GUI interface for better accessibility

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with different daily life scenarios
5. Submit a pull request

## 📄 License

This project is available for educational and personal use.

---

**Note**: This chatbot runs entirely locally using Ollama, ensuring complete privacy and no API costs. The Gemma 2B model provides efficient performance suitable for daily life advice and conversation, while the Jinja2 templating ensures consistent, helpful responses.
