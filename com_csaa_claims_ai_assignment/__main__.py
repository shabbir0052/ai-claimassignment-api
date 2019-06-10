#!/usr/bin/env python3

import connexion

from com_csaa_claims_ai_assignment import encoder


def main():
    #app = connexion.App(__name__, specification_dir='./openapi/')
    app = connexion.App(__name__, specification_dir='./openapi/', server='gevent')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'AiClaimAssignmentAPI'},
                pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
