# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from AsposeOCRCloudSDK.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V5_DETECT_REGIONS = "/v5.0/ocr/DetectRegions"
    V5_IMAGE_PROCESSING_POST_UPSAMPLING_IMAGE_FILE = "/v5.0/ocr/ImageProcessing/PostUpsamplingImageFile"
    V5_IMAGE_PROCESSING_POST_BINARIZATION_FILE = "/v5.0/ocr/ImageProcessing/PostBinarizationFile"
    V5_IMAGE_PROCESSING_POST_SKEW_CORRECTION_FILE = "/v5.0/ocr/ImageProcessing/PostSkewCorrectionFile"
    V5_IMAGE_PROCESSING_POST_DEWARPING_FILE = "/v5.0/ocr/ImageProcessing/PostDewarpingFile"
    V5_IMAGE_PROCESSING_GET_RESULT_TASK = "/v5.0/ocr/ImageProcessing/GetResultTask"
    V5_IMAGE_PROCESSING_GET_RESULT_FILE = "/v5.0/ocr/ImageProcessing/GetResultFile"
    V5_RECOGNIZE_IMAGE = "/v5.0/ocr/RecognizeImage"
    V5_RECOGNIZE_PDF = "/v5.0/ocr/RecognizePdf"
    V5_RECOGNIZE_RECEIPT = "/v5.0/ocr/RecognizeReceipt"
    V5_RECOGNIZE_REGIONS = "/v5.0/ocr/RecognizeRegions"
    V5_RECOGNIZE_TABLE = "/v5.0/ocr/RecognizeTable"
    V5_TEXT_TO_SPEECH_POST_TEXT_TO_SPEECH = "/v5.0/ocr/TextToSpeech/PostTextToSpeech"
    V5_TEXT_TO_SPEECH_GET_TEXT_TO_SPEECH_RESULT = "/v5.0/ocr/TextToSpeech/GetTextToSpeechResult"
    V5_TEXT_TO_SPEECH_GET_TEXT_TO_SPEECH_RESULT_FILE = "/v5.0/ocr/TextToSpeech/GetTextToSpeechResultFile"
