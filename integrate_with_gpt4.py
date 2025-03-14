# integrate_with_gpt4.py
import os
import openai

def get_enhanced_response(processed_data):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Based on the following processed log data, provide actionable security insights: {processed_data}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a cybersecurity AI assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    data = "Multiple failed login attempts from IP 192.168.1.10 detected."
    print("Enhanced Response:", get_enhanced_response(data))
