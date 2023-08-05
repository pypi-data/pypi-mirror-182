# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from AsposeOCRCloudSDK.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from AsposeOCRCloudSDK.model.dsr_confidence import DsrConfidence
from AsposeOCRCloudSDK.model.dsr_mode import DsrMode
from AsposeOCRCloudSDK.model.language import Language
from AsposeOCRCloudSDK.model.language_tts import LanguageTTS
from AsposeOCRCloudSDK.model.ocr_detect_regions_body import OCRDetectRegionsBody
from AsposeOCRCloudSDK.model.ocr_error import OCRError
from AsposeOCRCloudSDK.model.ocr_recognize_image_body import OCRRecognizeImageBody
from AsposeOCRCloudSDK.model.ocr_recognize_pdf_body import OCRRecognizePdfBody
from AsposeOCRCloudSDK.model.ocr_recognize_receipt_body import OCRRecognizeReceiptBody
from AsposeOCRCloudSDK.model.ocr_recognize_regions_body import OCRRecognizeRegionsBody
from AsposeOCRCloudSDK.model.ocr_recognize_table_body import OCRRecognizeTableBody
from AsposeOCRCloudSDK.model.ocr_rect import OCRRect
from AsposeOCRCloudSDK.model.ocr_region import OCRRegion
from AsposeOCRCloudSDK.model.ocr_response import OCRResponse
from AsposeOCRCloudSDK.model.ocr_result import OCRResult
from AsposeOCRCloudSDK.model.ocr_settings_detect_regions import OCRSettingsDetectRegions
from AsposeOCRCloudSDK.model.ocr_settings_recognize_image import OCRSettingsRecognizeImage
from AsposeOCRCloudSDK.model.ocr_settings_recognize_pdf import OCRSettingsRecognizePdf
from AsposeOCRCloudSDK.model.ocr_settings_recognize_receipt import OCRSettingsRecognizeReceipt
from AsposeOCRCloudSDK.model.ocr_settings_recognize_regions import OCRSettingsRecognizeRegions
from AsposeOCRCloudSDK.model.ocr_settings_recognize_table import OCRSettingsRecognizeTable
from AsposeOCRCloudSDK.model.ocr_task_status import OCRTaskStatus
from AsposeOCRCloudSDK.model.problem_details import ProblemDetails
from AsposeOCRCloudSDK.model.response_status_code import ResponseStatusCode
from AsposeOCRCloudSDK.model.result_type import ResultType
from AsposeOCRCloudSDK.model.result_type_tts import ResultTypeTTS
from AsposeOCRCloudSDK.model.result_type_table import ResultTypeTable
from AsposeOCRCloudSDK.model.tts_body import TTSBody
from AsposeOCRCloudSDK.model.tts_error import TTSError
from AsposeOCRCloudSDK.model.tts_response import TTSResponse
from AsposeOCRCloudSDK.model.tts_result import TTSResult
from AsposeOCRCloudSDK.model.tts_task_status import TTSTaskStatus
