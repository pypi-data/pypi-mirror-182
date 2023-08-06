from pystac import Link, Provider, ProviderRole

# Collection
TITLE = "FWS National Wetlands Inventory"
DESCRIPTION = (
    "The Wetlands Data Layer is the product of over 45 years of work by the National Wetlands"
    " Inventory (NWI) and its collaborators and currently contains more than 35 million wetland and"
    " deepwater features. This dataset, covering the conterminous United States, Hawaii,"
    " Puerto Rico, the Virgin Islands, Guam, the major Northern Mariana Islands and Alaska,"
    " continues to grow at a rate of 50 to100 million acres annually as data are updated."
    " The data layer is updated twice a year and these changes are reflected on the mapper and in"
    " the data downloads.\n\n"
    "**NOTE:** Due to the variation in use and analysis of this data by the end user, each of"
    " states wetlands data extends beyond the state boundary. Each state includes wetlands data"
    " that intersect the 1:24,000 quadrangles that contain part of that state (1:2,000,000 source"
    " data). This allows the user to clip the data to their specific analysis datasets."
    " Beware that two adjacent states will contain some of the same data along their borders."
)
# Bounding boxes - note: crosses the antimeridian!
COLLECTION_BBOXES = [
    # Union
    [-64.54958, 13.16667, 144.6, 71.99633],
    # Split into two parts as it crosses the antimeridian
    [144.6, 13.16667, 180.0, 71.99633],
    [-180.0, 13.16667, -64.54958, 71.99633],
]

PROVIDER_USFWS = Provider(
    name="U.S. Fish and Wildlife Service",
    roles=[ProviderRole.PRODUCER, ProviderRole.LICENSOR],
    description=(
        "The U.S. Fish and Wildlife Service is the principal federal agency tasked with providing"
        " information to the public on the extent and status of the nation's wetland and deepwater"
        " habitats, as well as changes to these habitats over time."
    ),
    url="https://www.fws.gov",
    extra_fields={"email": "wetlands_team@fws.gov"},
)

KEYWORDS = [
    "FWS",
    "USFWS",
    "U.S. Fish and Wildlife Service",
    "NWI",
    "National Wetlands Inventory",
    "wetlands",
    "deepwater habitats",
    "hydrography",
    "surface water",
    "swamps",
    "marshes",
    "bogs",
    "fens",
    "coastal waters",
]

LINK_LICENSE = Link(
    target="http://www.usa.gov/publicdomain/label/1.0/",
    media_type="text/html",
    title="US Public Domain",
    rel="license",
)
LINK_LANDING_PAGE = Link(
    target="https://www.fws.gov/program/national-wetlands-inventory",
    media_type="text/html",
    title="Project Landing Page",
    rel="about",
)
LINK_FACT_SHEET = Link(
    target="https://www.fws.gov/sites/default/files/documents/national-wetlands-inventory-fact-sheet.pdf",  # noqa: E501
    media_type="application/pdf",
    title="Project Fact Sheet",
    rel="about",
)
LINK_METADATA = Link(
    target="https://www.fws.gov/wetlands/Data/metadata/FWS_Wetlands.xml",
    media_type="application/xml",
    title="Wetlands metadata",
    rel="describedby",
)

# Extensions
NWI_EXTENSION = "https://stac-extensions.github.io/usfws-nwi/v1.0.0/schema.json"
PROCESSING_EXTENSION = "https://stac-extensions.github.io/processing/v1.1.0/schema.json"
# For summaries, until supported: https://github.com/stac-utils/pystac/issues/890
PROJECTION_EXTENSION = "https://stac-extensions.github.io/projection/v1.0.0/schema.json"

# Assets
PARQUET_MEDIA_TYPE = "application/x-parquet"
PARQUET_ROLES = ["data", "cloud-optimized"]
PARQUET_GEOMETRY_COL = "geometry"
PARQUET_GEOMETRY_TYPE = "Polygon"

SHP_TITLE = "Source assets in a ZIP file"
SHP_DESCRIPTION = (
    "The ZIP archive contains the original data files in ESRI Shapefile format."
)
SHP_MEDIA_TYPE = "application/zip"
SHP_ROLES = ["data", "archive", "source"]
SHP_KEY = "source"
