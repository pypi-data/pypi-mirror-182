import typing_extensions

from AsposeOCRCloudSDK.apis.tags import TagValues
from AsposeOCRCloudSDK.apis.tags.detect_regions_api import DetectRegionsApi
from AsposeOCRCloudSDK.apis.tags.image_processing_api import ImageProcessingApi
from AsposeOCRCloudSDK.apis.tags.recognize_image_api import RecognizeImageApi
from AsposeOCRCloudSDK.apis.tags.recognize_pdf_api import RecognizePdfApi
from AsposeOCRCloudSDK.apis.tags.recognize_receipt_api import RecognizeReceiptApi
from AsposeOCRCloudSDK.apis.tags.recognize_regions_api import RecognizeRegionsApi
from AsposeOCRCloudSDK.apis.tags.recognize_table_api import RecognizeTableApi
from AsposeOCRCloudSDK.apis.tags.text_to_speech_api import TextToSpeechApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DETECT_REGIONS: DetectRegionsApi,
        TagValues.IMAGE_PROCESSING: ImageProcessingApi,
        TagValues.RECOGNIZE_IMAGE: RecognizeImageApi,
        TagValues.RECOGNIZE_PDF: RecognizePdfApi,
        TagValues.RECOGNIZE_RECEIPT: RecognizeReceiptApi,
        TagValues.RECOGNIZE_REGIONS: RecognizeRegionsApi,
        TagValues.RECOGNIZE_TABLE: RecognizeTableApi,
        TagValues.TEXT_TO_SPEECH: TextToSpeechApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DETECT_REGIONS: DetectRegionsApi,
        TagValues.IMAGE_PROCESSING: ImageProcessingApi,
        TagValues.RECOGNIZE_IMAGE: RecognizeImageApi,
        TagValues.RECOGNIZE_PDF: RecognizePdfApi,
        TagValues.RECOGNIZE_RECEIPT: RecognizeReceiptApi,
        TagValues.RECOGNIZE_REGIONS: RecognizeRegionsApi,
        TagValues.RECOGNIZE_TABLE: RecognizeTableApi,
        TagValues.TEXT_TO_SPEECH: TextToSpeechApi,
    }
)
