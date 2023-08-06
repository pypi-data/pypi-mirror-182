from orkg.utils import NamespacedClient
from orkg.out import OrkgResponse
from orkg import subgraph
import pandas as pd
from csvw.parser import convert_orkg_statements_into_dataframe


class ObjectsClient(NamespacedClient):

    def add(self, params=None) -> OrkgResponse:
        """
        Warning: Super-users only should use this endpoint
        Create a new object in the ORKG instance
        :param params: orkg Object
        :return: an OrkgResponse object containing the newly created object resource
        """
        self.client.backend._append_slash = True
        response = self.client.backend.objects.POST(json=params, headers=self.auth)
        return self.client.wrap_response(response)

    def table_as_df(self, resource_id: str) -> pd.DataFrame:
        """
        Convert a CSVW representation in the ORKG to a pandas.DataFrame object
        :param resource_id: the resource id of the Table object
        :return a pandas dataframe object
        """
        if not self.client.resources.exists(resource_id):
            raise ValueError(f"resource {resource_id} doesn't exist in the graph!")
        if "Table" not in self.client.resources.by_id(resource_id).content['classes']:
            raise ValueError(f"resource {resource_id} is not of type orkgc:Table")
        statements = self.client.statements.bundle(thing_id=resource_id).content["statements"]
        return convert_orkg_statements_into_dataframe(self.client)

