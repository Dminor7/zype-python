import time
from zype.exceptions import ZypeException
from zype.adapters import ZypeAdapter, generate_wrapper_from_adapter, JSONAdapterMixin
from zype.resource_mapping import RESOURCE_MAPPING


class _Zype(JSONAdapterMixin, ZypeAdapter):
    api_root = "https://api.zype.com"

    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(_Zype, self).get_request_kwargs(api_params, *args, **kwargs)

        if "params" in params:
            params["params"].update({"api_key": api_params.get("api_key")})
        else:
            params["params"] = {"api_key": api_params.get("api_key")}

        return params

    def get_api_root(self, api_params, **kwargs):
        if api_params.get("api_root"):
            return api_params.get("api_root")
        return self.api_root

    def get_iterator_list(self, response_data):
        return response_data["response"]

    def get_iterator_next_request_kwargs(
        self, iterator_request_kwargs, response_data, response
    ):
        paging = response_data.get("pagination")
        if not paging:
            return
        next_page = paging.get("next")

        if current := paging.get("current"):
            if current % 10 == 0:
                time.sleep(0.2)

        if next_page:
            params = iterator_request_kwargs["params"]
            params["page"] = next_page
            iterator_request_kwargs["params"] = params
            return iterator_request_kwargs


Zype = generate_wrapper_from_adapter(_Zype)
