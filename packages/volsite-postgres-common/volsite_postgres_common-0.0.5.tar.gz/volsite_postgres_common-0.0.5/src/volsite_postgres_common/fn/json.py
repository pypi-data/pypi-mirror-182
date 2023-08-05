from psycopg2._json import Json
import json
from volsite_postgres_common.api.CA import CA
from volsite_postgres_common.test.Timer import Timer
from volsite_postgres_common.test.db.ATestDb import ATestDb


def json_fn(fn: str, input_j: dict, conn, attList,
            do_commit: bool = False,
            print_input_output: bool = True,
            print_long_att: bool = True):  # -> dict:
    cursor = conn.cursor()
    if print_input_output:
        print(f'==== [FN] {fn} ====')
        print('=== Input ===')
        print('<code>')
        print_json_by_attributes(input_j, attList, print_long_att)
        print('</code>')
    cursor.execute(f'SELECT {fn}( %s::JSONB ) AS {CA.Result}', (
        Json(input_j),
    ))
    rows = cursor.fetchall()
    assert 1 == len(rows)
    # print('[json_fn] rows[0] = %r' % rows[0])
    if do_commit:
        conn.commit()
    output = rows[0][CA.Result]
    if print_input_output:
        print('=== Output ===')
        print('<code>')
        print_json_by_attributes(output, attList, print_long_att)
        print('</code>')
    return output


def print_json_by_attributes(j, attList, print_long_att: bool = False):
    if not print_long_att:
        print(json.dumps(j, indent=4, sort_keys=True))
        return

    abb_att = {}

    for a in attList:
        for name in a.__dict__:
            abb = a.__dict__[name]
            abb_att[f"\"{abb}\":"] = f"\"{abb}__{name}\":"

    res = json.dumps(j, indent=4, sort_keys=True)
    for att in abb_att.keys():
        res = res.replace(att, abb_att[att])
    print(res)


def json_fn_db(
        fn: str, input_j: dict,
        test_db: ATestDb, attList,
        do_commit: bool = False,
        print_long_att: bool = True):  # -> dict:
    with Timer(fn):
        return json_fn(fn, input_j, test_db.p_conn, attList,
                       do_commit=do_commit,
                       print_input_output=test_db.print_input_output,
                       print_long_att=print_long_att)
