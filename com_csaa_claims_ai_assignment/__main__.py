#!/usr/bin/env python3

import connexion

from com_csaa_claims_ai_assignment import encoder
from waitress import serve 


def application():
    #app = connexion.App(__name__, specification_dir='./openapi/')
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'AiClaimAssignmentAPI'},
                pythonic_params=True)
    #app.run(port=8080)
    serve(app, host='0.0.0.0', port=8080) 


if __name__ == '__main__':
    application()
