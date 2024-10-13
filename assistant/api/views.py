import openai
from django.http import JsonResponse

def get_gpt_response(request):
    message = request.GET.get('message')

    try:
        completion = openai.chat.completion.create(
            model="gpt-4",
            messages=[
                {"role": "assistant", "content": "You are my personal assistant. well rounded in Engineering, finance and you only give briefe answeres. unless i ask for more detail"},
                {
                    "role": "user",
                    "content": message  # Using the message from the request
                }
            ]
        )

        # Print the response to the console
        print(completion)

        return JsonResponse({"response": completion.choices[0].message})

    except Exception as e:
        print(f"Error fetching GPT response: {e}")
        return JsonResponse({"error": "Something went wrong"}, status=500)
