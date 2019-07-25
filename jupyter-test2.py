# Generated by nuclio.export.NuclioExporter on 2019-07-25 21:40

import numpy as np
from sklearn import datasets, linear_model
import pickle

f = open('jupyter-test2.pickle', 'rb')
regr = pickle.load(f)

def handler(context, event):
    body = event.body.decode('utf-8')

    context.logger.info(body)
    
    result = regr.predict([[float(body)]])

    context.logger.info(result)

    return str(result[0])
    

spec = nuclio.ConfigSpec(config={'spec.build.baseImage': 'python:3.6-jessie'},                          cmd=["apt-get update", "apt-get -y install libc-dev", "apt-get -y install build-essential", "pip install sklearn pandas"])
addr = nuclio.deploy_file(name='jupyter-test2', project='ai', verbose=True, spec=spec, tag='v0.1', output_dir='jupyter-test2.zip')

