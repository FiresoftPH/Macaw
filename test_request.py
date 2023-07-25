import requests
from dotenv import dotenv_values

config = dotenv_values("Libs/.env")

# Checked

# Basiclly ask ai for answer to your question
def getAnswer():
    url = 'https://api.parrot.cmkl.ai/ai/getResponse'  # Replace with your server's URL

    # prompt = "What is coffee?"
    # prompt = "Why is it popular?"
    prompt = "What is a for loop and why is it considered more simple than while loops?"

    payload = {
        'username': config["TEST_USERNAME"],
        'email': config["TEST_EMAIL"],
        'code': [],
        "course": "Cloud Computing",
        "chatroom_name": "Python",
        "question": prompt,
        "api_key" : config['TEST_API_KEY']
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        # Wait for the response and then print it out
        response_data = response.json()
        print(response_data)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))

# Checked

# For getting the chat history for that certain room, backend automaticlly checks
# if the room is created or not, just send the room name.
def getHistory():
    url = 'https://api.parrot.cmkl.ai/ai/getFullHistory'  # Replace with your server's URL

    payload = {
        'username': config["TEST_USERNAME"],
        'email': config["TEST_EMAIL"],
        "course": "Computer Systems",
        "chatroom_name": "pgvxLjGb6W_cQMjzSL4it",
        "api_key" : config['TEST_API_KEY']
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exceptiPrincipal Of Computing Applicationson for 4xx and 5xx status codes

        # Wait for the response and then print it out
        response_data = response.json()
        print(response_data)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))

# CheckedPrincipal Of Computing Applications
    payload = {
        'username': config["TEST_USERNAME"],
        'email': config["TEST_EMAIL"],
        "course": "Calculus 1",
        "api_key" : config['TEST_API_KEY']
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        # Wait for the response and then print it out
        response_data = response.json()
        print(response_data)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))

# Checked
def getChatRoom():
    url = 'https://api.parrot.cmkl.ai/auth/chatroom/fetch'  # Replace with your server's URL

    payload = {
        'username': config["TEST_USERNAME"],
        'email': config["TEST_EMAIL"],
        "course": "Computer Systems",
        "api_key" : config['TEST_API_KEY']
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        # Wait for the response and then print it out
        response_data = response.json()
        print(response_data)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))

# Checked
def unenrollCourse():
    url = 'https://api.parrot.cmkl.ai/auth/unenroll'  # Replace with your server's URL

    payload = {
        'username': config["TEST_USERNAME"],
        'email': config["TEST_EMAIL"],
        "course": "Computer Systems",
        "api_key" : config['TEST_API_KEY']
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        # Wait for the response and then print it out
        response_data = response.json()
        print(response_data)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))

# Checked
def deleteChatRoom():
    url = 'https://api.parrot.cmkl.ai/auth/chatroom/delete'  # Replace with your server's URL
# Raise an exceptiPrincipal Of Computing Applicationson for 4xx and 5xx status codes

            # Wait for the response and then print it out
    payload = {
        'username': config["TEST_USERNAME"],
        'email': config["TEST_EMAIL"],
        "course": "Cloud Computing",
        "chatroom_name": "Python",
        "api_key" : config['TEST_API_KEY']
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        # Wait for the response and then print it out
        response_data = response.json()
        print(response_data)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))

# Checked
def runPythonCode():
    url = 'https://api.parrot.cmkl.ai/compileCode' 

#     code = '''
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# result = factorial(5)
# print("Factorial of 5:", result)
# '''
#     code = '''
# #include <stdio.h>

# int factorial(int n) {
#     if (n == 0) {
#         return 1;
#     } else {
#         return n * factorial(n - 1);
#     }
# }

# int main() {
#     int number = 5;
#     int result = factorial(number);
#     printf("Factorial of %d: %d\\n", number, result);
#     return 0;
# }
# '''
    code = '''
#include <iostream>

int factorial(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    int number = 5;
    int result = factorial(number);
    std::cout << "Factorial of " << number << ": " << result << std::endl;
    return 0;
}
'''

    payload = {
        'username': config["TEST_USERNAME"],
        'email': config["TEST_EMAIL"],
        'code' : code,
        "api_key" : config['TEST_API_KEY'],
        "file_extension": ".cpp"
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        # Wait for the response and then print it out
        # response_data = response.json()
        print(response.json())

    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))


# getAnswer()
# getHistory()
# getChatRoom()
# enrollCourse()
# unenrollCourse()
# deleteChatRoom()
runPythonCode()