"After using data.py to generate dataframes, use this to display them in a web broswer"

import os
from flask import render_template
from flask import Flask, jsonify
from api import GetJSON
import pandas as pd

app = Flask(__name__)

@app.route("/api")
def get_api():
    return jsonify(GetJSON().get_data())

@app.route("/")
def show_tables():
    eth = pd.read_excel('ethexcel.xlsx', header=0, delim_whitespace=True)
    gaming = pd.read_excel('gamingexcel.xlsx', header=0, delim_whitespace=True)
    gurus = pd.read_excel('gurusexcel.xlsx', header=0, delim_whitespace=True)
    econ = pd.read_excel('econexcel.xlsx', header=0, delim_whitespace=True)
    ai = pd.read_excel('aiexcel.xlsx', header=0, delim_whitespace=True)
    btc = pd.read_excel('btcxcel.xlsx', header=0, delim_whitespace=True)
    space = pd.read_excel('spaceexcel.xlsx', header=0, delim_whitespace=True)
    systems = pd.read_excel('systemsexcel.xlsx', header=0, delim_whitespace=True)
    cryptofunds = pd.read_excel('cryptofundsexcel.xlsx', header=0, delim_whitespace=True)
    dao = pd.read_excel('daoexcel.xlsx', header=0, delim_whitespace=True)
    defi = pd.read_excel('defiexcel.xlsx', header=0, delim_whitespace=True)
    network = pd.read_excel('networkexcel.xlsx', header=0, delim_whitespace=True)
    politicaleconomy = pd.read_excel('politicaleconomyexcel.xlsx', header=0, delim_whitespace=True)
    psych = pd.read_excel('psychexcel.xlsx', header=0, delim_whitespace=True)
    techexecs = pd.read_excel('techexecsexcel.xlsx', header=0, delim_whitespace=True)
    vc = pd.read_excel('vcexcel.xlsx', header=0, delim_whitespace=True)
    

    eth.set_index(['url'], inplace=True,)
    eth.index.name="Ethereum"
    gaming.set_index(['url'], inplace=True,)
    gaming.index.name=" Crypto Gaming"
    gurus.set_index(['url'], inplace=True,)
    gurus.index.name="Cryptogurus"
    econ.set_index(['url'], inplace=True,)
    econ.index.name="Economics"
    ai.set_index(['url'], inplace=True,)
    ai.index.name="Artifcial Intelligence"
    btc.set_index(['url'], inplace=True,)
    btc.index.name="Bitcoin"
    space.set_index(['url'], inplace=True,)
    space.index.name="Space"
    systems.set_index(['url'], inplace=True,)
    systems.index.name="Systems"
    cryptofunds.set_index(['url'], inplace=True,)
    cryptofunds.index.name="Cryptofunds"

    dao.set_index(['url'], inplace=True,)
    dao.index.name="dao"
    defi.set_index(['url'], inplace=True,)
    defi.index.name="defi"
    network.set_index(['url'], inplace=True,)
    network.index.name="network"
    politicaleconomy.set_index(['url'], inplace=True,)
    politicaleconomy.index.name="politicaleconomy"
    psych.set_index(['url'], inplace=True,)
    psych.index.name="psych"
    techexecs.set_index(['url'], inplace=True,)
    techexecs.index.name="techexecs"
    vc.set_index(['url'], inplace=True,)
    vc.index.name="vc"

    eth_table = eth
    gaming_table = gaming
    gurus_table = gurus
    econ_table = econ
    ai_table = ai
    btc_table = btc
    space_table = space
    systems_table = systems
    cryptofunds_table = cryptofunds
    dao_table = dao
    defi_table = defi
    network_table = network
    politicaleconomy_table = politicaleconomy
    psych_table = psych
    techexecs_table = techexecs
    vc_table = vc


    return render_template('view.html',tables=[eth_table.to_html(classes='text'),
                                               gaming_table.to_html(classes='text'),
                                               gurus_table.to_html(classes='text'),
                                               econ_table.to_html(classes='text'),
                                               ai_table.to_html(classes='text'),
                                               btc_table.to_html(classes='text'),
                                               space_table.to_html(classes='text'),
                                               systems_table.to_html(classes='text'),
                                               dao_table.to_html(classes='text'),
                                               defi_table.to_html(classes='text'),
                                               network_table.to_html(classes='text'),
                                               politicaleconomy_table.to_html(classes='text'),
                                               psych_table.to_html(classes='text'),
                                               techexecs_table.to_html(classes='text'),
                                               vc_table.to_html(classes='text')],
                                               titles = ['na', 'Lists'])



if __name__ == "__main__":
    os.system("python data.py")
    app.run(debug=True)
    # In order to run the following line, put together a bash file with a 'rm *.<file_type>'.
    # Be sure the right permissions are set up for it --> chmod 755 <file_name>.sh
    # os.system("./remove_files.sh")
