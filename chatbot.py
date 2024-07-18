from openai import OpenAI


client = OpenAI()


def text_generation(prompts):
    stream = client.chat.completions.create(
        messages=prompts,
        model='gpt-3.5-turbo-0125',
        temperature=0,
        max_tokens=1000,
        stream=True
    )

    print('Chatbot: ', end='')
    full_response = ''
    for chunk in stream:
        response = chunk.choices[0].delta.content
        if response:
            print(response, end='')
            full_response += response
    print()

    prompts.append({'role': 'assistant', 'content': full_response})
    return prompts


if __name__ == '__main__':
    print('Bem-vindo ao Chatbot com Python da Openai :)')
    prompts = []
    while True:
        input_user = input('User: ')
        prompts.append({'role': 'user', 'content': input_user})
        text_generation(prompts)
