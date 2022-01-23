#
# Copyright (C) 2021 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/xiaomi/apollon

# Inherit from sm8250-common
include device/xiaomi/sm8250-common/BoardConfigCommon.mk

BUILD_BROKEN_DUP_RULES := true

# Display
TARGET_SCREEN_DENSITY := 440

# Init
TARGET_INIT_VENDOR_LIB := //$(DEVICE_PATH):init_xiaomi_apollon
TARGET_RECOVERY_DEVICE_MODULES := init_xiaomi_apollon

# Kernel
TARGET_KERNEL_CONFIG := vendor/apollo_defconfig

# OTA assert
TARGET_OTA_ASSERT_DEVICE := apollon,apollo,apollopro

# Properties
TARGET_VENDOR_PROP += $(DEVICE_PATH)/vendor.prop

# Releasetools
TARGET_RELEASETOOLS_EXTENSIONS := $(DEVICE_PATH)

# Inherit from the proprietary version
include vendor/xiaomi/apollon/BoardConfigVendor.mk
