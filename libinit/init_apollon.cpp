/*
 * Copyright (C) 2021 The LineageOS Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <libinit_kona.h>

static const variant_info_t apollo_info = {
    .sku_value = "std",

    .brand = "Xiaomi",
    .device = "apollo",
    .model = "Xiaomi Mi 10T",
    .build_description = "apollo-user 11 RKQ1.200826.002 V12.1.3.0.RJDMIXM release-keys",
    .build_fingerprint = "Xiaomi/apollo_global/apollo:11/RKQ1.200826.002/V12.1.3.0.RJDMIXM:user/release-keys",
};

static const variant_info_t apollopro_info = {
    .sku_value = "pro",

    .brand = "Xiaomi",
    .device = "apollo",
    .model = "Xiaomi Mi 10T Pro",
    .build_description = "apollopro-user 11 RKQ1.200826.002 V12.1.3.0.RJDMIXM release-keys",
    .build_fingerprint = "Xiaomi/apollopro_global/apollopro:11/RKQ1.200826.002/V12.1.3.0.RJDMIXM:user/release-keys",
};

static const std::vector<variant_info_t> variants = {
    apollo_info,
    apollopro_info,
};

void vendor_load_properties() {
    search_variant(variants);
}
