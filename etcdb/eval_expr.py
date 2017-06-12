"""
Module provides functions to evaluate an expression given in
a WHERE statement.
Grammar of expression is described on MySQL website
(https://dev.mysql.com/doc/refman/5.7/en/expressions.html).
"""
from etcdb import OperationalError, __version__
from etcdb.resultset import Column
from etcdb.sqlparser.parser import SQLParserError


class EtdbFunction(object):
    def __init__(self, function_name, group=False, *args):
        self._function = function_name
        self._group = group
        self._args = args

    @property
    def function(self):
        return self._function

    @property
    def group(self):
        return self._group

    def __call__(self, *args, **kwargs):
        return self._function(*args, **kwargs)


def eval_identifier(row, identifier):
    """
    Get value of identifier for a given row

    :param row: row
    :type row: tuple(ColumnSet, Row)
    :param identifier: Identifier
    :type identifier: str
    :return: value of identifier
    """
    try:
        identifier_strip = identifier.split('.')[1]
    except IndexError:
        identifier_strip = identifier

    # If row isn't given return column name only
    if row:
        columns = row[0]
        data = row[1]
    else:
        return identifier_strip, None

    try:
        pos = columns.index(Column(identifier_strip))
        return identifier_strip, data[pos]
    except ValueError:
        raise OperationalError('Unknown identifier %s', identifier_strip)


def eval_string(value):
    """Evaluate string token"""
    return "'%s'" % value, value


def etcdb_version():
    return __version__


def etcdb_count(result_set):
    """
    Count rows in result set

    :param result_set: ResultSet instance
    :type result_set: ResultSet
    :return: number of rows in ResultSet
    :rtype: int
    """
    return len(result_set.rows) + 1


def eval_function_call(row, tree):
    """Evaluate function call
    :return: tuple with field name and EtdbFunction instance"""
    if tree == 'VERSION':
        # func = EtdbFunction(version, group=False)
        return "VERSION()", EtdbFunction(etcdb_version, group=False)
    if tree == 'COUNT':
        # func = EtdbFunction(version, group=False)
        return "COUNT(*)", EtdbFunction(etcdb_count, group=True)
    raise NotImplementedError('Unknown function %s' % tree)


def eval_simple_expr(row, tree):
    """Evaluate simple_expr"""
    if tree[0] == 'IDENTIFIER':
        return eval_identifier(row, tree[1])
    elif tree[0] == 'STRING' or tree[0] == 'literal':
        return eval_string(tree[1])
    elif tree[0] == 'function_call':
        return eval_function_call(row, tree[1])
    else:
        raise SQLParserError('%s is not implemented' % tree[0])


def eval_bit_expr(row, tree):
    """Evaluate bit_expr"""
    if tree[0] == 'simple_expr':
        return eval_simple_expr(row, tree[1])
    else:
        raise SQLParserError('%s is not implemented' % tree[0])


def eval_predicate(row, tree):
    """Evaluate predicate"""
    if tree[0] == 'bit_expr':
        return eval_bit_expr(row, tree[1])
    else:
        raise SQLParserError('%s is not implemented' % tree[0])


def eval_bool_primary(row, tree): # pylint: disable=too-many-return-statements
    """Evaluate bool_primary"""

    if tree[0] == 'IS NULL':

        bool_primary1 = eval_bool_primary(row, tree[1])
        return "%s IS NULL" % bool_primary1[0], \
               bool_primary1[1] is None

    elif tree[0] == 'IS NOT NULL':
        bool_primary1 = eval_bool_primary(row, tree[1])
        return "%s IS NOT NULL" % bool_primary1[0], \
               bool_primary1[1] is not None

    elif tree[0] == '=':
        bool_primary1 = eval_bool_primary(row, tree[1])
        bool_primary2 = eval_bool_primary(row, tree[2])

        return (
            "%s = %s" % (bool_primary1[0], bool_primary2[0]),
            bool_primary1[1] == bool_primary2[1]
        )

    elif tree[0] == '>=':
        bool_primary1 = eval_bool_primary(row, tree[1])
        bool_primary2 = eval_bool_primary(row, tree[2])

        return (
            "%s >= %s" % (bool_primary1[0], bool_primary2[0]),
            bool_primary1[1] >= bool_primary2[1]
        )

    elif tree[0] == '>':
        bool_primary1 = eval_bool_primary(row, tree[1])
        bool_primary2 = eval_bool_primary(row, tree[2])

        return (
            "%s > %s" % (bool_primary1[0], bool_primary2[0]),
            bool_primary1[1] > bool_primary2[1]
        )
    elif tree[0] == '<=':
        bool_primary1 = eval_bool_primary(row, tree[1])
        bool_primary2 = eval_bool_primary(row, tree[2])

        return (
            "%s <= %s" % (bool_primary1[0], bool_primary2[0]),
            bool_primary1[1] <= bool_primary2[1]
        )
    elif tree[0] == '<':
        bool_primary1 = eval_bool_primary(row, tree[1])
        bool_primary2 = eval_bool_primary(row, tree[2])

        return (
            "%s < %s" % (bool_primary1[0], bool_primary2[0]),
            bool_primary1[1] < bool_primary2[1]
        )
    elif tree[0] in ['<>', '!=']:
        bool_primary1 = eval_bool_primary(row, tree[1])
        bool_primary2 = eval_bool_primary(row, tree[2])

        return (
            "%s %s %s" % (bool_primary1[0], tree[0], bool_primary2[0]),
            bool_primary1[1] != bool_primary2[1]
        )
    elif tree[0] == 'predicate':
        return eval_predicate(row, tree[1])
    elif tree[0] == 'bit_expr':
        return eval_bit_expr(row, tree[1])
    else:
        raise SQLParserError('%s is not implemented' % tree[0])


def eval_expr(row, tree):
    """Evaluate expression

    :return: Tuple with string representation and value.
        For example, ('id', 5).
    :rtype: tuple
    """
    if tree[0] == 'OR':
        expr1 = eval_expr(row, tree[1])
        expr2 = eval_expr(row, tree[2])

        return (
            '%s OR %s' % (expr1[0], expr2[0]),
            expr1[1] or expr2[1]
        )
    elif tree[0] == 'AND':
        expr1 = eval_expr(row, tree[1])
        expr2 = eval_expr(row, tree[2])
        return (
            '%s AND %s' % (expr1[0], expr2[0]),
            expr1[1] and expr2[1]
        )
    elif tree[0] == 'bool_primary':
        return eval_bool_primary(row, tree[1])
    else:
        raise SQLParserError('%r is not implemented' % tree[0])
