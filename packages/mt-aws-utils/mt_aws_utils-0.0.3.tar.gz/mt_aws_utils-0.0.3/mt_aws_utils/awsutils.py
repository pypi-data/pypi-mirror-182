'''Mark This database utility module.'''

from mt_aws_utils.dbutil import Db


class AWSMarkThis(Db):
    '''AWS MarkThis database access layer'''

    def sheet_insert(self, rows):
        '''Insert sheets.
        rows is a list of tuples.  Each row has the following items in order
        sheetid, owner, title, style, answers_csv '''

        qry = '''INSERT into sheet
                 (sheetid, owner, title, style, answers_csv, created_at)
                 VALUES(%s, %s, %s, %s, %s, NOW())'''

        return self.executemany(qry, rows)

    def sheet_get(self, sheetid):
        '''gets sheet info for sheetid'''
        qry = 'SELECT * FROM sheet WHERE sheetid=%s'

        for row in self.namedselect(qry, (sheetid,)):
            return row

        return None

    def stack_insert(self, stack):
        '''Insert stack'''

        arglist = ()
        columns = []

        for key, val in stack.items():
            columns += [key]
            arglist += (val,)

        qry = 'INSERT into stack (' + ', '.join(columns) + ') ' +\
              'VALUES(' + ', '.join(['%s'] * len(columns)) + ')'

        return self.singlequery(qry, arglist)