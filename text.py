"""Instantiate a DBStorage object
SEPH_MYSQL_USER = SePh_dev
SEPH_MYSQL_PWD = aagituu1031
SEPH_MYSQL_HOST = localhost
SEPH_MYSQL_DB = SepH_dev_db
"""
__engine = create_engine('mysql+mysqldb://SePh_dev:aagituu1031@localhost/SePh_dev_db')

""".
                                format(SEPH_MYSQL_USER,
                                        SEPH_MYSQL_PWD,
                                        SEPH_MYSQL_HOST,
                                        SEPH_MYSQL_DB))
                                        """