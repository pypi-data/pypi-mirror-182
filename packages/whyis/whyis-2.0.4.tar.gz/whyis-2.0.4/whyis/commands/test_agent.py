# -*- coding:utf-8 -*-

from flask_script import Command, Option

import flask
import rdflib

class TestAgent(Command):
    '''Runs a specified inference agent.'''

    def get_options(self):
        return [
            Option('-a', '--agent', dest='agent_path', help='Python path (dotted) of agent to use', required=True,
                   type=str),
            Option('-e', '--entity', dest="entity_uri", help='Entity URI to run against', type=rdflib.URIRef),
            Option('-d', '--dry-run', action="store_true", help='Do not store agent output', dest='dry_run'),
        ]

    def run(self, agent_path, entity_uri=None, dry_run=False):
        app = flask.current_app
        from pydoc import locate
        agent_class = locate(agent_path)
        agent = agent_class()
        agent.dry_run = dry_run
        if agent.dry_run:
            print("Dry run, not storing agent output.")
        agent.app = app
        print(agent.get_query())
        results = []
        #if agent.query_predicate == app.NS.whyis.globalChangeQuery:
        if (entity_uri):
            results.extend(agent.process_instance(app.db.resource(entity_uri), app.db))
        else:
            results.extend(agent.process_graph(app.db))
        #else:
        #    for resource in agent.getInstances(app.db):
        #        for np_uri, in app.db.query('''select ?np where {
#    graph ?assertion { ?e ?p ?o.}
#    ?np a np:Nanopublication;
#        np:hasAssertion ?assertion.
#}''', initBindings={'e': resource.identifier}, initNs=app.NS.prefixes):
#                    np = app.nanopub_manager.get(np_uri)
#                    results.extend(agent.process_graph(np))
        for np in results:
            print(np.identifier)
            if dry_run:
                print(rdflib.ConjunctiveGraph(np.store).serialize(format="trig"))
