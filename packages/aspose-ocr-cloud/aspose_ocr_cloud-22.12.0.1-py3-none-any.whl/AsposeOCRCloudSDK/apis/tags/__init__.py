# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from AsposeOCRCloudSDK.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    DETECT_REGIONS = "DetectRegions"
    IMAGE_PROCESSING = "ImageProcessing"
    RECOGNIZE_IMAGE = "RecognizeImage"
    RECOGNIZE_PDF = "RecognizePdf"
    RECOGNIZE_RECEIPT = "RecognizeReceipt"
    RECOGNIZE_REGIONS = "RecognizeRegions"
    RECOGNIZE_TABLE = "RecognizeTable"
    TEXT_TO_SPEECH = "TextToSpeech"
