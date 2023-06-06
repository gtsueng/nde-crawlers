from hub.dataload.nde import NDESourceUploader
from utils.csv_helper import get_source_data

# Example __metadata__ dictionary:
# <SOURCE_NAME> = https://api.data.niaid.nih.gov/v1/metadata
# __metadata__ = {
# "src_meta": {
# 'description': 'A short description of what the source offers, usually found on the source's about page',
# 'name': 'The full source name, Ex. Mendeley Data (not mendeley)',
# 'identifier':'includedInDataCatalog.name value',
# 'schema': 'A dict where the key is the source's metadata variable and the value is our transformation. Ex: {"summary":"description"},
# 'url': 'The source's URL homepage',
# }
# }


class Bioconductor_Uploader(NDESourceUploader):
    name = "bioconductor"
    __metadata__ = {
        "src_meta": {
            "sourceInfo": {
                "description": "Bioconductor is a free, open source and open development software project for the analysis and comprehension of genomic data generated by wet lab experiments in molecular biology. It holds a repository of R packages that facilitates rigorous and reproducible analysis of data from current and emerging biological assays. BioConductor delivers releases where a set of packages is published at once and intended for compatibility only with a certain version of R. This is in contrast to CRAN where packages are added continuously with no reference to particular versions of R. Additionally, BioConductor also comes with its own installation tool, BiocManager::install().",
                "identifier": "Bioconductor",
                "name": "Bioconductor",
                "schema": get_source_data(name),
                "url": "https://bioconductor.org/",
            }
        }
    }
