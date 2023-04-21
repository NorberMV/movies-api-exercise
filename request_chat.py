import requests


def req(data=None):
    if data:
        data = {"prompt": user_input}
    response = requests.post('http://localhost/generate', json=data)
    return response.text


# Entry Point
if __name__=="__main__":

    intro_message = ""
    quitt = False

    while not quitt:
        user_input = str(input("Ask GPT>> "))
        try:
            chat_resp = req(user_input)
        except Exception as e:
            raise e
        print(f"{chat_resp!r}")
        exit_response = str(input("\n\nDo you want to exit ? Y/N: ")).lower()
        if exit_response == "y":
            quitt = True
