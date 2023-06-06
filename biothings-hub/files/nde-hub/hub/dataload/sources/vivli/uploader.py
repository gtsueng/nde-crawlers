from hub.dataload.nde import NDESourceUploader
from utils.pubtator import standardize_data
from utils.utils import check_schema


class VivliUploader(NDESourceUploader):
    name = "vivli"
    __metadata__ = {
        "src_meta": {
            "url": "https://search.vivli.org/",
            "license_url": "https://vivli.org/resources/vivli-data-use-agreement/",
        }
    }

    @check_schema
    def load_data(self, data_folder):
        pubtator_docs = standardize_data(data_folder)
        for doc in pubtator_docs:
            yield doc
