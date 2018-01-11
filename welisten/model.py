"""
WeListen website (database) API.

Adapted from EECS485 Project 2 by Andrew DeOrio <awdeorio@umich.edu>
"""
import sqlite3
import flask
import welisten


def dict_factory(cursor, row):
    """
    Convert database row objects to a dictionary.

    This is useful for building dictionaries which are then used to render a
    template. Note that this would be inefficient for large queries.
    """
    output = {}
    for idx, col in enumerate(cursor.description):
        output[col[0]] = row[idx]
    return output


def get_db():
    """Open a new database connection."""
    if not hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db = sqlite3.connect(
            welisten.app.config['DATABASE_FILENAME'])
        flask.g.sqlite_db.row_factory = dict_factory

        # Foreign keys have to be enabled per-connection.  This is an sqlite3
        # backwards compatibility thing.
        flask.g.sqlite_db.execute("PRAGMA foreign_keys = ON")

    return flask.g.sqlite_db


def query_db(query, args=(), one=False):
    """Execute a query on an open database."""
    cur = get_db().execute(query, args)
    retval = cur.fetchall()
    cur.close()
    return (retval[0] if retval else None) if one else retval


@welisten.app.teardown_appcontext
def close_db(error):
    # pylint: disable=unused-argument
    """Close the database at the end of a request."""
    if hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db.commit()
        flask.g.sqlite_db.close()
