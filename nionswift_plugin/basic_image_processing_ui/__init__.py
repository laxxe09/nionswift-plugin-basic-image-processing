# import components so they get registered with Nion Swift
from nionswift_plugin.basic_image_processing_ui.BasicImageProcessingPanel import run as run_v1
from nionswift_plugin.basic_image_processing_ui.BasicImageProcessingPanelv2 import run as run_v2
from nionswift_plugin.basic_image_processing_ui.BasicImageProcessingPanelv3 import run as run_v3

# Register both panels when the plugin is loaded
run_v1()
run_v2()
run_v3()
