selected_columns = [
    "original_shape_SurfaceVolumeRatio",
    "original_firstorder_Kurtosis",
    "original_firstorder_Minimum",
    "original_glcm_Idmn",
    "original_gldm_LowGrayLevelEmphasis",
    "original_glrlm_LowGrayLevelRunEmphasis",
    "original_glrlm_ShortRunLowGrayLevelEmphasis",
    "original_glszm_LargeAreaHighGrayLevelEmphasis",
    "original_glszm_LowGrayLevelZoneEmphasis",
    "original_glszm_SmallAreaLowGrayLevelEmphasis",
    "original_ngtdm_Strength"
]

new_columns = []

for column in selected_columns:
    new_columns.append(column + "_10mm")

print(new_columns)
