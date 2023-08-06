from typing import List
import pandas as pd
import networkx as nx


def convert_orkg_statements_into_dataframe(client) -> pd.DataFrame:
    # columns = list(filter(lambda x: x["predicate"]["id"] == "CSVW_Columns", statements))
    # rows = list(filter(lambda x: x["predicate"]["id"] == "CSVW_Rows", statements))
    # values = [ for r in rows]
    graph = client.graph.subgraph(self.client, resource_id)
    pass
