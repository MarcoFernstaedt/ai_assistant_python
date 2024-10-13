from openai import OpenAI
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import json

client = OpenAI()
client.api_key= os.getenv('OPENAI_API_KEY')

@csrf_exempt
def get_gpt_response(request):
    body = json.loads(request.body)
    message = body.get('message')

    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                # {"role": "assistant", "content": "You are my personal assistant. well rounded in Engineering, finance and you only give briefe answeres. unless i ask for more detail"},
                {
                    "role": "user",
                    "content": message  # Using the message from the request
                }
            ]
        )

        print(completion._request_id)
        # Print the response to the console
        response = completion.choices[0].message.content

        return JsonResponse({"response": response})

    except Exception as e:
        print(f"Error fetching GPT response: {e}")
        return JsonResponse({"error": "Something went wrong"}, status=500)
