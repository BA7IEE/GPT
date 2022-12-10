import openai
import datetime
import os
import re


from sql import DB_OP
db = '/mnt/hgfs/ShareFile/sql/dna.db'

def log_time():
    now_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    return f'[{time_str}] '


def ai(prompt:str):
    openai.api_key = "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"
    prompt = prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
    )
    text = response["choices"][0]["text"]
    return text

coon = DB_OP(db)
while 1<5:
    q = input(f'{log_time()}请输入问题：')
    print(f'{log_time()}正在思考，请稍等......')
    a = ai(q)
    sql = f"insert into qa ( ask, answer ) values ('{q}', '{a}')"
    coon.addRecord('qa', 'answer', a, sql)
coon.db_close()