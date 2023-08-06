
import setuptools

setuptools.setup(
	name="anapi",
	version="1.0.1",
	author="WiSpace",
	author_email="wiforumit@gmail.com",
	description="AnAPI lib",
	long_description="""
# AnAPI

## Class ChatAI

Arguments:
version="last",
api_key="standart_key"

**API key is not needed for API version 1.**

Functions:
get_answer(text: str) -> str — return answer from API


# Example

```py
import anapi

AI = anapi.ChatAI(1, api_key="Your api key")

while True:
    answer = AI.get_answer(input("You: "))

    print("Anya:", answer)

```
""",
	long_description_content_type="text/markdown",
	url="https://ai.wispace.ru/",
	packages=setuptools.find_packages(),
	python_requires='>=3.6',
)