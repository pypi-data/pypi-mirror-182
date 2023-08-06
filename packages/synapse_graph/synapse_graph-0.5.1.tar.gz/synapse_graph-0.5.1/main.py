import os
import synapse_graph

MATRIX_TOKEN = os.getenv('MATRIX_TOKEN')
MATRIX_HOMESERVER_DOMAIN = os.getenv('MATRIX_HOMESERVER_DOMAIN')
HEADERS = {
    'Authorization': f'Bearer {MATRIX_TOKEN}'
}

graph = synapse_graph.SynapseGraph(MATRIX_HOMESERVER_DOMAIN, HEADERS, MATRIX_HOMESERVER_DOMAIN, hide_usernames=False)
graph.calculate_edges(u2u_relation=True)
graph.show()

# print(graph.get_html())
