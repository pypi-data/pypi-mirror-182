from volsite_postgres_common.db.CFn import CFn


def sql__to_id(*att: str) -> str:
    return f"{CFn.bigint_2_id}({'.'.join(att)})"
