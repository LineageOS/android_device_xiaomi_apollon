# Copyright (C) 2009 The Android Open Source Project
# Copyright (c) 2011, The Linux Foundation. All rights reserved.
# Copyright (C) 2017-2018 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import common
import re

def FullOTA_InstallEnd(info):
  OTA_InstallEnd(info)
  return

def IncrementalOTA_InstallEnd(info):
  OTA_InstallEnd(info)
  return

def AddImage(info, basename, dest):
  path = "IMAGES/" + basename
  if path not in info.input_zip.namelist():
    return

  data = info.input_zip.read(path)
  common.ZipWriteStr(info.output_zip, basename, data)
  info.script.AppendExtra('package_extract_file("%s", "%s");' % (basename, dest))

def AddImageRadio(info, basename, dest):
    name = basename
    data = info.input_zip.read("RADIO/" + basename)
    common.ZipWriteStr(info.output_zip, name, data)
    info.script.Print("Patching {} image unconditionally...".format(dest.split('/')[-1]))
    info.script.AppendExtra('package_extract_file("%s", "%s");' % (name, dest))

def OTA_InstallEnd(info):
  info.script.Print("Patching firmware images...")
  AddImage(info, "dtbo.img", "/dev/block/bootdevice/by-name/dtbo")
  AddImage(info, "vbmeta.img", "/dev/block/bootdevice/by-name/vbmeta")
  AddImage(info, "vbmeta_system.img", "/dev/block/bootdevice/by-name/vbmeta_system")

  AddImageRadio(info, "abl.elf", "/dev/block/bootdevice/by-name/ablbak");
  AddImageRadio(info, "aop.mbn", "/dev/block/bootdevice/by-name/aop");
  AddImageRadio(info, "BTFM.bin", "/dev/block/bootdevice/by-name/bluetooth");
  AddImageRadio(info, "cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlib");
  AddImageRadio(info, "cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64");
  AddImageRadio(info, "devcfg.mbn", "/dev/block/bootdevice/by-name/devcfg");
  AddImageRadio(info, "dspso.bin", "/dev/block/bootdevice/by-name/dsp");
  AddImageRadio(info, "featenabler.mbn", "/dev/block/bootdevice/by-name/featenabler");
  AddImageRadio(info, "hyp.mbn", "/dev/block/bootdevice/by-name/hyp");
  AddImageRadio(info, "km4.mbn", "/dev/block/bootdevice/by-name/keymaster");
  AddImageRadio(info, "NON-HLOS.bin", "/dev/block/bootdevice/by-name/modem");
  AddImageRadio(info, "qupv3fw.elf", "/dev/block/bootdevice/by-name/qupfw");
  AddImageRadio(info, "storsec.mbn", "/dev/block/bootdevice/by-name/storsec");
  AddImageRadio(info, "tz.mbn", "/dev/block/bootdevice/by-name/tz");
  AddImageRadio(info, "uefi_sec.mbn", "/dev/block/bootdevice/by-name/uefisecapp");
  AddImageRadio(info, "xbl_4.elf", "/dev/block/bootdevice/by-name/xbl_4");
  AddImageRadio(info, "xbl_5.elf", "/dev/block/bootdevice/by-name/xbl_5");
  AddImageRadio(info, "xbl_config_4.elf", "/dev/block/bootdevice/by-name/xbl_config_4");
  AddImageRadio(info, "xbl_config_5.elf", "/dev/block/bootdevice/by-name/xbl_config_5");
  return
