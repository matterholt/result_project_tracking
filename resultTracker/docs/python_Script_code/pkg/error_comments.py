import sys
def sql_header_error(issue):
    desc = """
    Error has accrued !!!
    Template file does not have correct column names
    Database contains => \n
    """ 
    error = desc + issue + "\n"
    sys.exit()