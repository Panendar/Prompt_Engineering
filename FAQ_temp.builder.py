import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file in the current directory
load_dotenv()

examples = {
    "Orders": [
        {
            "Question": "How do I cancel my order?",
            "Answer" : "You can cancel your order from your account in \"MY ORDERS\" section"
        },
        {
            "Question": "Can I track my order?",
            "Answer" : "Yes, once ordered, you can see continuous tracking through app or link for further details which is being shared through email."
        }
    ],
    "Refunds" :[
        {
            "Question": "How do I initiate a refund?",
            "Answer" : "You can initiate a refund from your account in the \"MY ORDERS\" section"
        },
        {
            "Question": "What is the refund process?",
            "Answer" : "Once your refund request is received, it will be processed within 5-7 business days."
        }
    ],
    "Discounts" : [
        {
            "Question" : "Do you offer student discounts?",
            "Answer" : "Yes, we provide a 10% discount for students with a valid student email."
        }
    ],
    "Shipping" : [
        {
           "Question" : "How long does the shipping takes?",
           "Answer" : "Shipping usually takes 3-5 business days depending on your location." 
        }
    ],
    "Account": [
        {
            "Question": "How do I change my account details?",
            "Answer": "Account details can be changed from the \"MY ACCOUNT\" section."
        }
    ],
    "Policies" : [
        {
            "Question" : "What are all the different policies you have?",
            "Answer" : "We have different policies like Privacy Policy, Refund Policy, Shipping Policy, Terms of Service etc."
        }
    ]
}



user_question = input("Please enter your question here: ").strip()
company_name = input("Please enter the company name here: ").strip()
problem_area = input("Please enter the problem area here: \n Examples: Orders, Refunds, Discounts, Policies: ").strip()
tone = "polite"

faq_template = """
You are a customer support assistant for {company_name}. 
Your job is to answer FAQs about {problem_area} (such as shipping, policies, or orders).  
Always keep your response {tone} and limit it to **1–2 sentences maximum**.

{examples}

Customer Question: "{user_question}"

Final Answer:
"""

prompt = faq_template.format(
    company_name=company_name,
    user_question=user_question,
    problem_area=problem_area,
    tone=tone,
    examples=examples
)

print(f"Generated Prompt:\n{prompt}")

def get_response(prompt):
    api_key = os.getenv("my_api")
    
    # Debug: Print API key status (without exposing the full key)
    if api_key:
        print(f"API key loaded: {api_key[:10]}...")
    else:
        print("Error: API key not found. Please check your .env file.")
        return
    
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "sonar",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        # Extract and print just the response content
        result = response.json()
        answer = result['choices'][0]['message']['content']
        print("\nAI Response:")
        print(answer)
    
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your API key in the .env file.")
        else:
            print(f"API Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Call the function to get and print the response
get_response(prompt)