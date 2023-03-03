import os
import openai
from dotenv import load_dotenv

load_dotenv()

def getKey():
    try:
        key = os.getenv("API_KEY")
        openai.api_key = key
        return "success"
    except Exception as e:
        return f"failure, {e}"


def gpt3Completion(prompt, engine='text-davinci-002', temp=0.7,
                   top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0,
                   stop=('USER:', 'TIM:')):
    max_retry = 5
    retry = 0
    # prompt = prompt.encode(encoding="ASCII", errors="ignore").decode()

    while retry < max_retry:
        try:
            # response = openai.Completion.create(engine=engine, prompt=prompt,
            #                                     temperature=temp, max_tokens=tokens,
            #                                     top_p=top_p, frequency_penalty=freq_pen,
            #                                     presence_penalty=pres_pen, stop=stop)
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                     messages=[{"role": "system", "content": prompt}])
            text = response['choices'][0]['message']['content'].strip()

            return text
        except Exception as e:
            retry += 1
            return e


if __name__ == '__main__':
    prompt = 'Summarize the text'
    result = gpt3Completion(prompt)
    print(result)
