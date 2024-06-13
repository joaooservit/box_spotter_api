from flask import Flask

app = Flask(__name__)

@app.route('/spotter', methods=['POST'])
def hello_world():
    # abre um arquivo txt, escreve ola e fecha
    file = open("teste.txt", "w")
    file.write("ola")
    file.close()
    
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
