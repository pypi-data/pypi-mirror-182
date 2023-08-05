import typing_extensions

from AsposeOCRCloudSDK.paths import PathValues
from AsposeOCRCloudSDK.apis.paths.v5_detect_regions import V5DetectRegions
from AsposeOCRCloudSDK.apis.paths.v5_image_processing_post_upsampling_image_file import V5ImageProcessingPostUpsamplingImageFile
from AsposeOCRCloudSDK.apis.paths.v5_image_processing_post_binarization_file import V5ImageProcessingPostBinarizationFile
from AsposeOCRCloudSDK.apis.paths.v5_image_processing_post_skew_correction_file import V5ImageProcessingPostSkewCorrectionFile
from AsposeOCRCloudSDK.apis.paths.v5_image_processing_post_dewarping_file import V5ImageProcessingPostDewarpingFile
from AsposeOCRCloudSDK.apis.paths.v5_image_processing_get_result_task import V5ImageProcessingGetResultTask
from AsposeOCRCloudSDK.apis.paths.v5_image_processing_get_result_file import V5ImageProcessingGetResultFile
from AsposeOCRCloudSDK.apis.paths.v5_recognize_image import V5RecognizeImage
from AsposeOCRCloudSDK.apis.paths.v5_recognize_pdf import V5RecognizePdf
from AsposeOCRCloudSDK.apis.paths.v5_recognize_receipt import V5RecognizeReceipt
from AsposeOCRCloudSDK.apis.paths.v5_recognize_regions import V5RecognizeRegions
from AsposeOCRCloudSDK.apis.paths.v5_recognize_table import V5RecognizeTable
from AsposeOCRCloudSDK.apis.paths.v5_text_to_speech_post_text_to_speech import V5TextToSpeechPostTextToSpeech
from AsposeOCRCloudSDK.apis.paths.v5_text_to_speech_get_text_to_speech_result import V5TextToSpeechGetTextToSpeechResult
from AsposeOCRCloudSDK.apis.paths.v5_text_to_speech_get_text_to_speech_result_file import V5TextToSpeechGetTextToSpeechResultFile

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V5_DETECT_REGIONS: V5DetectRegions,
        PathValues.V5_IMAGE_PROCESSING_POST_UPSAMPLING_IMAGE_FILE: V5ImageProcessingPostUpsamplingImageFile,
        PathValues.V5_IMAGE_PROCESSING_POST_BINARIZATION_FILE: V5ImageProcessingPostBinarizationFile,
        PathValues.V5_IMAGE_PROCESSING_POST_SKEW_CORRECTION_FILE: V5ImageProcessingPostSkewCorrectionFile,
        PathValues.V5_IMAGE_PROCESSING_POST_DEWARPING_FILE: V5ImageProcessingPostDewarpingFile,
        PathValues.V5_IMAGE_PROCESSING_GET_RESULT_TASK: V5ImageProcessingGetResultTask,
        PathValues.V5_IMAGE_PROCESSING_GET_RESULT_FILE: V5ImageProcessingGetResultFile,
        PathValues.V5_RECOGNIZE_IMAGE: V5RecognizeImage,
        PathValues.V5_RECOGNIZE_PDF: V5RecognizePdf,
        PathValues.V5_RECOGNIZE_RECEIPT: V5RecognizeReceipt,
        PathValues.V5_RECOGNIZE_REGIONS: V5RecognizeRegions,
        PathValues.V5_RECOGNIZE_TABLE: V5RecognizeTable,
        PathValues.V5_TEXT_TO_SPEECH_POST_TEXT_TO_SPEECH: V5TextToSpeechPostTextToSpeech,
        PathValues.V5_TEXT_TO_SPEECH_GET_TEXT_TO_SPEECH_RESULT: V5TextToSpeechGetTextToSpeechResult,
        PathValues.V5_TEXT_TO_SPEECH_GET_TEXT_TO_SPEECH_RESULT_FILE: V5TextToSpeechGetTextToSpeechResultFile,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V5_DETECT_REGIONS: V5DetectRegions,
        PathValues.V5_IMAGE_PROCESSING_POST_UPSAMPLING_IMAGE_FILE: V5ImageProcessingPostUpsamplingImageFile,
        PathValues.V5_IMAGE_PROCESSING_POST_BINARIZATION_FILE: V5ImageProcessingPostBinarizationFile,
        PathValues.V5_IMAGE_PROCESSING_POST_SKEW_CORRECTION_FILE: V5ImageProcessingPostSkewCorrectionFile,
        PathValues.V5_IMAGE_PROCESSING_POST_DEWARPING_FILE: V5ImageProcessingPostDewarpingFile,
        PathValues.V5_IMAGE_PROCESSING_GET_RESULT_TASK: V5ImageProcessingGetResultTask,
        PathValues.V5_IMAGE_PROCESSING_GET_RESULT_FILE: V5ImageProcessingGetResultFile,
        PathValues.V5_RECOGNIZE_IMAGE: V5RecognizeImage,
        PathValues.V5_RECOGNIZE_PDF: V5RecognizePdf,
        PathValues.V5_RECOGNIZE_RECEIPT: V5RecognizeReceipt,
        PathValues.V5_RECOGNIZE_REGIONS: V5RecognizeRegions,
        PathValues.V5_RECOGNIZE_TABLE: V5RecognizeTable,
        PathValues.V5_TEXT_TO_SPEECH_POST_TEXT_TO_SPEECH: V5TextToSpeechPostTextToSpeech,
        PathValues.V5_TEXT_TO_SPEECH_GET_TEXT_TO_SPEECH_RESULT: V5TextToSpeechGetTextToSpeechResult,
        PathValues.V5_TEXT_TO_SPEECH_GET_TEXT_TO_SPEECH_RESULT_FILE: V5TextToSpeechGetTextToSpeechResultFile,
    }
)
