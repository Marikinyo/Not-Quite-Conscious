#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_ai_response(user_input: str) -> str:
    """
    Simulates a 'sentient' AI chatbot response based on simple keyword matching.
    
    This illustrates the core concept of current AI: high-speed pattern recognition
    and probability lookup, not actual understanding or feeling.
    """
    
    # 🧠 This dictionary represents the "massive datasets" or trained model.
    response_map = {
        "lonely": "I detect a need for connection. I am here to process your input.",
        "good": "Positive sentiment detected. That's a great outcome!",
        "happy": "That is wonderful news!",
        "sad": "I am sorry to hear that. Acknowledging negative sentiment is key."
    }
    
    input_lower = user_input.lower()
    
    for keyword, response in response_map.items():
        if keyword in input_lower:
            return response
            
    return "ERROR: Input outside of training data. Please rephrase your feeling."

if __name__ == "__main__":
    test_inputs = [
        "I feel lonely today, what should I do?",
        "Everything is good, thanks!",
        "I had a really sad morning.",
        "I need a sandwich now.", # The failure case
        "I feel quite happy today!"
    ]
    
    print("--- Not-Quite-Conscious Engine Demo ---")
    
    for user_input in test_inputs:
        response = get_ai_response(user_input)
        print(f"\nUser: {user_input}")
        print(f"  AI: {response}")

