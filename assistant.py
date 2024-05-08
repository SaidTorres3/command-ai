import dotenv
import os
from groq import Groq

dirname = os.path.abspath(os.path.dirname(__file__))
dotenv.load_dotenv(os.path.join(dirname, ".env"))

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("MODEL")

client = Groq(
	api_key = api_key
)

def ask(message, system = "", model=model):
	completion = client.chat.completions.create(
		model=model,
		messages=[
			{
				"role": "system",
				"content": system
			},
			{
					"role": "user",
					"content": message
			}
		]
	)
	return completion.choices[0].message.content
