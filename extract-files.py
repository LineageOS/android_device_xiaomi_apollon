#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    'vendor/etc/camera/camxoverridesettings.txt': blob_fixup()
        .regex_replace('0x10098', '0')
        .regex_replace('0x1F', '0x0'),
    'vendor/etc/init/init.batterysecret.rc': blob_fixup()
        .regex_replace('.*seclabel u:r:batterysecret:s0\n', ''),
    'vendor/etc/libnfc-nci.conf': blob_fixup()
        .add_line_if_missing('LEGACY_MIFARE_READER=1'),
    'vendor/lib/liba2dpoffload_apollon.so': blob_fixup()
        .replace_needed('libaudioroute.so', 'libaudioroute-v34.so'),
    'vendor/lib/libaudioroute_ext.so': blob_fixup()
        .replace_needed('libaudioroute.so', 'libaudioroute-v34.so'),
    'vendor/lib/hw/audio.primary.apollon.so': blob_fixup()
        .binary_regex_replace(
            b'/vendor/lib/liba2dpoffload.so',
            b'liba2dpoffload_apollon.so\x00\x00\x00\x00',
        )
        .replace_needed('libaudioroute.so', 'libaudioroute-v34.so'),
    'vendor/lib64/camera/components/com.mi.node.watermark.so': blob_fixup()
        .add_needed('libpiex_shim.so'),
    (
        'vendor/lib64/libMIAIHDRhvx_interface.so',
        'vendor/lib64/libarcsoft_hdrplus_hvx_stub.so',
        'vendor/lib64/libarcsoft_super_night_raw.so',
        'vendor/lib64/libmialgo_rfs.so',
    ): blob_fixup()
        .clear_symbol_version('remote_handle_close')
        .clear_symbol_version('remote_handle_invoke')
        .clear_symbol_version('remote_handle_open')
        .clear_symbol_version('remote_register_buf')
        .clear_symbol_version('remote_register_buf_attr'),
    (
        'vendor/lib64/libalAILDC.so',
        'vendor/lib64/libalLDC.so',
        'vendor/lib64/libalhLDC.so',
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    'vendor/lib64/vendor.qti.hardware.camera.postproc@1.0-service-impl.so': blob_fixup()
        .binary_regex_replace(b'\x9A\x0A\x00\x94', b'\x1F\x20\x03\xD5'),
}  # fmt: skip

namespace_imports = [
    'hardware/qcom-caf/common/libqti-perfd-client',
    'hardware/qcom-caf/sm8250',
    'hardware/xiaomi',
    'vendor/qcom/opensource/display',
    'vendor/xiaomi/sm8250-common',
]

module = ExtractUtilsModule(
    'apollon',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 'sm8250-common', module.vendor)
    utils.run()
