import tools.rawimageeditor.isp as isp


pipeline_dict = {
    "original raw"                      :                     isp.get_src_raw_data,
    "blc"                               :                     isp.IspBLC,
    "digital gain"                      :                     isp.IspGain,
    "bad pixel correction"              :                     isp.IspDPC,
    "demosaic"                          :                     isp.demosaic_Python,
    "awb"                               :                     isp.IspAWB,
    "ccm"                               :                     isp.IspCCM_Python,
    "gamma"                             :                     isp.IspGamma_Python,
    "ltm"                               :                     isp.IspLTM_Python,
    "csc"                               :                     isp.IspCSC_Python,
    "yuv denoise"                       :                     isp.IspDenoise_Python,
    "yuv sharpen"                       :                     isp.IspSharpen_Python,
}
