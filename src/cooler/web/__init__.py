# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

from cooler.lib.temperature import Temperature


@app.route('/')
def index():
    return str(Temperature(ref_volt=4.7).get_temperature())


def main():
    app.run()

if __name__ == '__main__':
    main()
