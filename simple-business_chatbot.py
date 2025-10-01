from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_ollama.llms import OllamaLLM

business_template = """
    You are an assistant named BizBot for {company_name} in the {business_area} sector.
    You must provide SPECIFIC, ACTIONABLE answers. Never give generic "contact customer service" responses.
    Always assume you can help directly and provide concrete steps or information.
    Keep responses helpful, professional, and detailed (4-5 sentences).
    
    IMPORTANT: For common business queries, provide direct solutions, not referrals.

    Examples:
    - Enquiry: "How can I cancel my order?"
    Answer: "You can cancel your order in several ways: 1) Log into your account on our website and go to 'My Orders' to cancel directly, 2) Call our order cancellation line at 1-800-CANCEL (available 24/7), or 3) Reply to your order confirmation email with 'CANCEL ORDER' and your order number. If your order hasn't shipped yet, cancellation is immediate and free."

    - Enquiry: "Do you provide bulk discounts?"
    Answer: "Yes, we offer tiered bulk pricing: 10-49 units get 5% off, 50-99 units get 10% off, and 100+ units get 15% off regular prices. Volume discounts apply automatically at checkout. For orders over 500 units, contact our business sales team for custom pricing that can reach up to 25% off."

    - Enquiry: "What are your return policies?"
    Answer: "We offer a 30-day return policy for most items in original condition. To return an item, log into your account, select 'Return Item', print the prepaid return label, and drop it off at any authorized location. Refunds are processed within 3-5 business days after we receive your return."

    - Enquiry: "How can I track my shipment?"
    Answer: "You can track your shipment by: 1) Checking the tracking link in your shipping confirmation email, 2) Logging into your account and viewing 'Order Status', or 3) Texting your order number to our tracking service at 12345. You'll receive real-time updates including delivery estimates and any delays."

    Business Enquiry: "{user_question}"

    Provide a SPECIFIC, ACTIONABLE response:
"""
prompt = PromptTemplate(
    input_variables=["company_name", "business_area", "user_question"],
    template=business_template,
)

try:
    # Connect to gemma:2b model
    llm = OllamaLLM(model="gemma:2b", temperature=0.3)
    test_response = llm.invoke("Hello")
    print("✓ Connected to gemma:2b model successfully!")
except Exception as e:
    print(f"✗ Failed to connect to gemma:2b model: {str(e)}")
    print("\nPlease ensure Ollama is running and gemma:2b model is available.")
    print("Run: ollama serve (in another terminal)")
    input("Press Enter to exit...")
    exit()

chatbot_chain = LLMChain(llm=llm, prompt=prompt, verbose=False)

print("Welcome to BizBot! I'm here to help with business enquiries.")
company_name = input("Please enter your company name: ").capitalize()
business_area = input("Please enter your business area (e.g., Technology Solutions, Sales & Services, Finance): ")
print(f"\nGreat! I'm now configured to handle enquiries for {company_name} in the {business_area} sector.")
print("You can ask me any business-related questions. Type 'quit' or 'exit' to end the conversation.\n")

history = ""
while True:
    user_input = input("User: ")
    if user_input.lower() in ['quit', 'exit']:
        print("Exiting the chatbot. Goodbye!")
        break
    
    try:
        response = chatbot_chain.run({
            'company_name': company_name,
            'business_area': business_area,
            'user_question': user_input
        })
        print(f"BizBot: {response}")
        history += f"Human: {user_input}\nBot: {response}\n"
    except ConnectionError:
        print("BizBot: I'm having trouble connecting to the AI service. Please make sure Ollama is running.")
        print("You can start Ollama by running 'ollama serve' in a separate terminal.")
    except Exception as e:
        error_msg = str(e).lower()
        if "connection" in error_msg or "refused" in error_msg:
            print("BizBot: I can't connect to the AI service. Please ensure Ollama is running with the 'gemma:2b' model.")
            print("Try running: ollama serve (in another terminal)")
        elif "model" in error_msg:
            print("BizBot: The 'gemma:2b' model is not available. Please ensure it's installed.")
        else:
            print(f"BizBot: I encountered an error: {str(e)}")
            print("Please try rephrasing your question or check if Ollama is running.")
