/*
 * Copyright (C) 2021-2025 The LineageOS Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <libvariant.h>

static const variant_info apollo_global_info = {
    .hwc_value = "",
    .sku_value = "std",

    .brand = "Xiaomi",
    .device = "apollo",
    .marketname = "Mi 10T",
    .model = "M2007J3SY",
    .build_fingerprint = "Xiaomi/apollo_global/apollo:12/RKQ1.211001.001/V14.0.4.0.SJDMIXM:user/release-keys",

    .nfc = true,
};

static const variant_info apollopro_info = {
    .hwc_value = "",
    .sku_value = "pro",

    .brand = "Xiaomi",
    .device = "apollo",
    .marketname = "Mi 10T Pro",
    .model = "M2007J3SG",
    .build_fingerprint = "Xiaomi/apollopro_global/apollo:12/RKQ1.211001.001/V14.0.4.0.SJDMIXM:user/release-keys",

    .nfc = true,
};

static const variant_info apollo_info = {
    .hwc_value = "",
    .sku_value = "",

    .brand = "Redmi",
    .device = "apollo",
    .marketname = "Redmi K30S Ultra",
    .model = "M2007J3SC",
    .build_fingerprint = "Redmi/apollo/apollo:12/RKQ1.211001.001/V14.0.5.0.SJDCNXM:user/release-keys",

    .nfc = true,
};

const std::vector<variant_info> variants = {
    apollo_global_info,
    apollopro_info,
    apollo_info,
};
