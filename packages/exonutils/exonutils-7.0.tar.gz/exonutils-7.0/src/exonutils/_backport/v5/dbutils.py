# -*- coding: utf-8 -*-

__all__ = []

# supported DB backends
DB_BACKENDS = ['sqlite', 'pgsql', 'mysql', 'mssql']


def interactive_config(backends=None, defaults={}):
    from .console import ConsoleInput as Input

    default_backend = defaults.get('backend', None)
    default_database = defaults.get('database', None)
    default_host = defaults.get('host', 'localhost')
    default_port = defaults.get('port', None)
    default_username = defaults.get('username', None)
    default_password = defaults.get('password', None)

    cfg = {}

    if not backends:
        backends = DB_BACKENDS
    if type(backends) is list:
        if len(backends) == 1:
            cfg['backend'] = backends[0]
        else:
            cfg['backend'] = Input.select(
                "Select db backend", backends,
                default=default_backend, required=True)
    else:
        cfg['backend'] = backends

    if cfg['backend'] == 'sqlite':
        cfg['database'] = Input.get(
            "Enter db path", default=default_database, required=True)
    else:
        if not default_port:
            if cfg['backend'] == 'pgsql':
                default_port = 5432
            elif cfg['backend'] == 'mysql':
                default_port = 3306
            elif cfg['backend'] == 'mssql':
                default_port = 1433

        cfg['database'] = Input.get(
            "Enter db name", required=True)
        cfg['host'] = Input.get(
            "Enter db host", default=default_host, required=True)
        cfg['port'] = Input.number(
            "Enter db port", default=default_port, required=True)
        cfg['username'] = Input.get(
            "Enter db username", default=default_username)
        cfg['password'] = Input.passwd(
            "Enter db password", default=default_password)
        if cfg['password']:
            Input.confirm_passwd(
                "Confirm db password", cfg['password'])

    return cfg


def interactive_setup(cfg=None, defaults={}, quiet=False):
    if not cfg:
        cfg = interactive_config(defaults=defaults)

    backend = cfg.get('backend', '')
    if backend not in DB_BACKENDS:
        raise RuntimeError("invalid backend: %s" % backend)

    # call specefic setup function for each backend
    eval('interactive_%s_setup' % backend)(cfg, quiet=quiet)


# sqlite backend setup
def interactive_sqlite_setup(cfg, quiet=False):
    import os

    database = cfg.get('database', None)
    if not database:
        raise RuntimeError("invalid empty database name")

    # create db file
    if not os.path.exists(os.path.dirname(database)):
        os.makedirs(os.path.dirname(database))
    open(database, 'a').close()


# pgsql backend setup
def interactive_pgsql_setup(cfg, quiet=False):
    from .console import ConsoleInput as Input
    err = ''
    try:
        from psycopg2 import connect
    except ImportError:
        err = "[psycopg2] backend package not installed"
    if err:
        raise RuntimeError(err)

    host = cfg.get('host', None) or 'localhost'
    port = int(cfg.get('port', '0') or 5432)

    database = cfg.get('database', None)
    if not database:
        raise RuntimeError("invalid empty database name")
    username = cfg.get('username', None)
    if not username:
        raise RuntimeError("invalid empty database username")
    password = cfg.get('password', None)
    if not password:
        raise RuntimeError("invalid empty database password")

    # get superuser access for database setup
    adm_user = Input.get(
        "Enter DB server admin user", default='postgres')
    adm_pass = Input.get(
        "Enter DB server admin password", hidden=True, default='')

    def info(msg):
        if not quiet:
            print(msg)

    # create connection
    conn = connect(
        host=host, port=port, user=adm_user, password=adm_pass,
        database='postgres', client_encoding='utf8')
    conn.set_session(autocommit=True)

    # create role
    cur = conn.cursor()
    cur.execute("SELECT * FROM pg_roles WHERE rolname='%s';"
                % (username))
    if not cur.fetchall():
        cur.execute("CREATE ROLE %s LOGIN PASSWORD '%s';"
                    % (username, password))
    else:
        cur.execute("ALTER ROLE %s WITH PASSWORD '%s';"
                    % (username, password))
    cur.close()
    info("-- role created --")

    # create database
    cur = conn.cursor()
    cur.execute("SELECT * FROM pg_database WHERE datname='%s';"
                % (database))
    if not cur.fetchall():
        cur.execute("CREATE DATABASE %s OWNER %s ENCODING 'UTF8'"
                    % (database, username) +
                    " LC_COLLATE 'en_US.UTF-8' LC_CTYPE 'en_US.UTF-8';")
    cur.close()
    info("-- database created --")

    # grant privileges
    cur = conn.cursor()
    cur.execute("GRANT ALL PRIVILEGES ON DATABASE %s TO %s;"
                % (database, username))
    cur.close()
    info("-- privileges added --")

    conn.close()


# mysql backend setup
def interactive_mysql_setup(cfg, quiet=False):
    from .console import ConsoleInput as Input
    err = ''
    try:
        from MySQLdb import connect
    except ImportError:
        err = "[mysqlclient] backend package not installed"
    if err:
        raise RuntimeError(err)

    def info(msg):
        if not quiet:
            print(msg)

    host = cfg.get('host', None) or 'localhost'
    port = int(cfg.get('port', None) or 3306)

    database = cfg.get('database', None)
    if not database:
        raise RuntimeError("invalid empty database name")
    username = cfg.get('username', None)
    if not username:
        raise RuntimeError("invalid empty database username")
    password = cfg.get('password', None)
    if not password:
        raise RuntimeError("invalid empty database password")

    # get superuser access for database setup
    adm_user = Input.get(
        "Enter DB server admin user", default='root')
    adm_pass = Input.get(
        "Enter DB server admin password", hidden=True, default='')

    # create connection
    conn = connect(
        host=host, port=port, user=adm_user, password=adm_pass,
        charset='utf8mb4', connect_timeout=30)

    # create database
    cur = conn.cursor()
    cur.execute("SHOW DATABASES LIKE '%s';" % database)
    if not cur.fetchall():
        cur.execute("CREATE DATABASE %s" % database +
                    " CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    cur.close()
    info("-- database created --")

    # create user and grant privileges
    cur = conn.cursor()
    cur.execute("SELECT * FROM mysql.user " +
                "WHERE user='%s' AND host='%%';" % username)
    if not cur.fetchall():
        cur.execute("CREATE USER '%s'@'%%' IDENTIFIED BY '%s';"
                    % (username, password))
    else:
        cur.execute("ALTER USER '%s'@'%%' IDENTIFIED BY '%s';"
                    % (username, password))
    cur.execute("GRANT ALL ON %s.* TO %s@'%%';" % (database, username))
    cur.execute("FLUSH PRIVILEGES;")
    cur.close()
    info("-- user created --")
    info("-- privileges added --")

    conn.close()


# mssql backend setup
def interactive_mssql_setup(cfg, quiet=False):
    err = ''
    try:
        from pymssql import connect
    except ImportError:
        err = "[pymssql] backend package not installed"
    if err:
        raise RuntimeError(err)

    def info(msg):
        if not quiet:
            print(msg)

    host = cfg.get('host', None) or 'localhost'
    port = int(cfg.get('port', None) or 1433)

    database = cfg.get('database', None)
    if not database:
        raise RuntimeError("invalid empty database name")
    username = cfg.get('username', None)
    if not username:
        raise RuntimeError("invalid empty database username")
    password = cfg.get('password', None)
    if not password:
        raise RuntimeError("invalid empty database password")

    # create connection
    conn = connect(
        host=host, port=port, user=username, password=password,
        charset='utf8', login_timeout=30)

    # create database
    cur = conn.cursor()
    cur.execute("SELECT name FROM sys.databases WHERE name='%s'" % database)
    if cur.fetchall():
        info("-- database created --")
    else:
        info("-- FAILED!! database doesn't exist on server --")

    cur.close()
    conn.close()
