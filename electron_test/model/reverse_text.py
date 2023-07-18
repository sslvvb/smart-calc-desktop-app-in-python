# import sys

# def reverse_text(text):
#     return text[::-1]

# if __name__ == '__main__':
#     input_text = sys.argv[1]
#     reversed_text = reverse_text(input_text)
#     print(reversed_text)
#     print("Python version:", sys.version)


from flask import Flask
app = Flask(__name__)


@app.route('/test')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    # app.run
    app.run(host='127.0.0.1', port=5000)
