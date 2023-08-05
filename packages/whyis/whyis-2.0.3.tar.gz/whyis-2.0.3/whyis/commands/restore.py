# -*- coding:utf-8 -*-

from flask_script import Command, Option

import flask
from pathlib import Path
import os
import csv
from depot.manager import DepotManager
import tempfile


class Restore(Command):
    '''Restores a knowledge graph from an archive.'''

    def get_options(self):
        return [
            Option ('-a', '--archive', dest='input_directory', help='Backup path', required=True, type=str),
        ]

    def run(self, input_directory):
        app = flask.current_app
        from pydoc import locate
        Path(input_directory).mkdir(parents=True, exist_ok=True)
        nanopub_backup_dir = os.path.join(input_directory,'nanopublications')
        file_backup_dir = os.path.join(input_directory,'files')
        Path(nanopub_backup_dir).mkdir(parents=True, exist_ok=True)
        Path(file_backup_dir).mkdir(parents=True, exist_ok=True)
        DepotManager.configure('backup_files', {
            'depot.storage_path': file_backup_dir
        })
        backup_files = DepotManager.get('backup_files')
        DepotManager.configure('backup_nanopublications', {
            'depot.storage_path': nanopub_backup_dir
        })
        backup_nanopubs = DepotManager.get('backup_nanopublications')
        nanopub_list_file = os.path.join(input_directory,'nanopub_index')
        nanopub_to_fileid = {}
        new_nanopubs = set()
        if not os.path.exists(nanopub_list_file):
            print('''This is not a valid backup archive.
Please provide an archive generated by the backup command.''')
            return

        print("Loading Nanopub List...")
        with open(nanopub_list_file) as csvfile:
            reader = csv.reader(csvfile, delimiter="\t")
            nanopublications = [x for x in reader]
        with tempfile.NamedTemporaryFile(delete=True) as data:
            for i, (np_uri, file_id) in enumerate(nanopublications):
                fileinfo = backup_nanopubs.get(file_id)
                file_data = fileinfo.read()
                data.write(file_data)
                data.write(b'\n')
                data.flush()
                print("Gathering ",i+1," nanopublications...\r",end='',flush=True)
            data.seek(0)
            print("\nPublishing to database...",flush=True)
            app.db.store.publish(data)

        file_ids = backup_files.list()
        real_file_ids = set()
        for i, file_id in enumerate(file_ids):
            try:
                f = backup_files.get(file_id)
                app.file_depot.create(f, f.name, f.content_type, f.file_id)
            except IOError:
                # Looks like this one's missing.
                pass
            print("Restored ",i+1," files...\r",end='',flush=True)
        print('\n',flush=True)

        print('Restoring admin database...')
        with open(os.path.join(input_directory,'admin_graph.jsonld'), 'rb') as admin_nq:
            app.admin_db.load(admin_nq, format="json-ld")#application/json;charset=utf-8")

        print("Complete!")
