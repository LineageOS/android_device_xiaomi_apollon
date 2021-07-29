/*
 * Copyright (C) 2021 The LineageOS Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <libinit_kona.h>

static const variant_info_t apollocn_info = {
    .hwc_value = "CN",
    .sku_value = "",

    .brand = "Redmi",
    .device = "apollo",
    .marketname = "K30S Ultra",
    .model = "M2007J3SC",
    .build_description = "apollo-user 11 RKQ1.200826.002 V12.5.1.0.RJDCNXM release-keys",
    .build_fingerprint = "Redmi/apollo/apollo:11/RKQ1.200826.002/V12.5.1.0.RJDCNXM:user/release-keys",

    .nfc = true,
};

static const variant_info_t apollo_info = {
    .hwc_value = "",
    .sku_value = "std",

    .brand = "Xiaomi",
    .device = "apollo",
    .marketname = "Mi 10T",
    .model = "M2007J3SY",
    .build_description = "apollo-user 11 RKQ1.200826.002 V12.1.3.0.RJDMIXM release-keys",
    .build_fingerprint = "Xiaomi/apollo_global/apollo:11/RKQ1.200826.002/V12.1.3.0.RJDMIXM:user/release-keys",

    .nfc = true,
};

static const variant_info_t apollopro_info = {
    .hwc_value = "",
    .sku_value = "pro",

    .brand = "Xiaomi",
    .device = "apollo",
    .marketname = "Mi 10T Pro",
    .model = "M2007J3SG",
    .build_description = "apollopro-user 11 RKQ1.200826.002 V12.1.3.0.RJDMIXM release-keys",
    .build_fingerprint = "Xiaomi/apollopro_global/apollopro:11/RKQ1.200826.002/V12.1.3.0.RJDMIXM:user/release-keys",

    .nfc = true,
};

static const std::vector<variant_info_t> variants = {
    apollocn_info,
    apollo_info,
    apollopro_info,
};

void vendor_load_properties() {
    search_variant(variants);
    set_dalvik_heap();
}
