#
# Copyright (C) 2021 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/xiaomi/apollon

# Inherit from sm8250-common
include device/xiaomi/sm8250-common/BoardConfigCommon.mk

# Bluetooth
BOARD_BLUETOOTH_BDROID_BUILDCFG_INCLUDE_DIR := $(DEVICE_PATH)/bluetooth/include

BUILD_BROKEN_DUP_RULES := true

# Display
TARGET_SCREEN_DENSITY := 440

# Kernel
TARGET_KERNEL_CONFIG := vendor/apollo_defconfig

# OTA assert
TARGET_OTA_ASSERT_DEVICE := apollon,apollo,apollopro

# Inherit from the proprietary version
include vendor/xiaomi/apollon/BoardConfigVendor.mk
