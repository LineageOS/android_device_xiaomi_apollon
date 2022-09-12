/*
 * Copyright (C) 2021 The LineageOS Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <libinit_dalvik_heap.h>
#include <libinit_variant.h>

#include "vendor_init.h"

static const variant_info_t apollo_global_info = {
    .hwc_value = "",
    .sku_value = "std",

    .brand = "Xiaomi",
    .device = "apollo",
    .marketname = "Mi 10T",
    .model = "M2007J3SY",
    .build_fingerprint = "Xiaomi/apollo_global/apollo:12/RKQ1.211001.001/V13.0.5.0.SJDMIXM:user/release-keys",

    .nfc = true,
};

static const variant_info_t apollopro_info = {
    .hwc_value = "",
    .sku_value = "pro",

    .brand = "Xiaomi",
    .device = "apollo",
    .marketname = "Mi 10T Pro",
    .model = "M2007J3SG",
    .build_fingerprint = "Xiaomi/apollopro_global/apollo:12/RKQ1.211001.001/V13.0.5.0.SJDMIXM:user/release-keys",

    .nfc = true,
};

static const variant_info_t apollo_info = {
    .hwc_value = "",
    .sku_value = "",

    .brand = "Redmi",
    .device = "apollo",
    .marketname = "Redmi K30S Ultra",
    .model = "M2007J3SC",
    .build_fingerprint = "Redmi/apollo/apollo:12/RKQ1.211001.001/V13.0.6.0.SJDCNXM:user/release-keys",

    .nfc = true,
};

static const std::vector<variant_info_t> variants = {
    apollo_global_info,
    apollopro_info,
    apollo_info,
};

void vendor_load_properties() {
    search_variant(variants);
    set_dalvik_heap();
}
