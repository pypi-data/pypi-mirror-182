from typing import cast

import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session

from chalk import realtime
from chalk.features import DataFrame, features
from chalk.sql import BaseSQLSourceProtocol
from chalk.testing import _assert_frame_equal_ignore_order

seed_db = """
DROP TABLE IF EXISTS mappings_table;

CREATE TABLE mappings_table (
    id INT PRIMARY KEY,
    ufrom TEXT,   -- maps to `u_from` feature, implicitly
    uto TEXT,     -- maps to `u_to` feature, implicitly
    col_a TEXT,   -- maps to `column_a` feature, explicitly
    swap_b TEXT,  -- maps to `swap_c` feature, explicitly
    swap_c TEXT,  -- maps to `swap_b` feature, explicitly
    unused TEXT   -- unused
);

INSERT INTO mappings_table(id, ufrom, uto, col_a, swap_b, swap_c, unused) VALUES
  (0, 'from', 'to', 'value_a', 'value_b', 'value_c', 'unused');
"""


@pytest.fixture
def init_db(temp_sqlite_source: BaseSQLSourceProtocol):
    with Session(temp_sqlite_source.get_engine()) as session, session.begin():
        for statement in seed_db.split(";"):
            if statement != "":
                session.execute(text(statement))


@features
class MappingFeatures:
    id: int
    u_from: str
    u_to: str
    column_a: str
    swap_b: str
    swap_c: str


def test_sql_resolver_implicit_mapping_rules(init_db: None, temp_sqlite_source: BaseSQLSourceProtocol):
    @realtime
    def resolve_mapping_features() -> DataFrame[MappingFeatures]:
        return cast(
            DataFrame,
            temp_sqlite_source.query_string(
                """
            SELECT * FROM mappings_table;
            """,
                fields={
                    "col_a": MappingFeatures.column_a,
                    "swap_b": MappingFeatures.swap_c,
                    "swap_c": MappingFeatures.swap_b,
                },
            ).all(),
        )

    results = resolve_mapping_features()
    _assert_frame_equal_ignore_order(
        results,
        DataFrame(
            [MappingFeatures(id=0, u_from="from", u_to="to", column_a="value_a", swap_b="value_c", swap_c="value_b")]
        ),
    )
