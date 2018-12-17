"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2016,2018 Freescale Semiconductor, Inc.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from .family.target_kinetis import Kinetis
from .family.flash_kinetis import Flash_Kinetis
from ..core.memory_map import (FlashRegion, RamRegion, MemoryMap)
from ..debug.svd import SVDFile
import logging

RCM_MR = 0x4007f010
RCM_MR_BOOTROM_MASK = 0x6

FLASH_ALGO = {
    'load_address' : 0x20000000,
    'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0xb510482d, 0x6041492b, 0x71fff64f, 0x68016081, 0x0180f021, 0x0120f041, 0x48286001, 0xf0004448,
    0x2800f851, 0x2001bf18, 0x2000bd10, 0x48234770, 0x4923b510, 0xf0004448, 0x2800f89d, 0xbd10bf18,
    0x481e2100, 0x4010e8bd, 0xf0004448, 0xb570b962, 0x46054c1a, 0x4601444c, 0x46204b19, 0xf00068e2,
    0x2800f8c2, 0xbd70bf18, 0x46292300, 0xe8bd68e2, 0x48124070, 0xf0004448, 0xb570b956, 0x460b460c,
    0x46014606, 0xb084480d, 0x44484615, 0xf8f5f000, 0xbf1c2800, 0xbd70b004, 0x21012000, 0x1000e9cd,
    0x48069002, 0x4622462b, 0x44484631, 0xf989f000, 0xbd70b004, 0xd928c520, 0x40052000, 0x00000004,
    0x6b65666b, 0xbf042800, 0x47702004, 0x6cc949f0, 0x6103f3c1, 0xbf08290f, 0x2100f44f, 0x4aedbf1f,
    0xf832447a, 0x02891011, 0x2200b410, 0x2100e9c0, 0x60812101, 0x03094be8, 0xf89360c1, 0x110cc000,
    0xfc0cfa04, 0xc014f8c0, 0x618378db, 0xf04f6102, 0xe9c052a0, 0xbc102108, 0x47702000, 0xbf0e2800,
    0x61012004, 0x47702000, 0x48dc4602, 0x49db6800, 0x0020f040, 0x46086008, 0xf0406800, 0x60080010,
    0x48d74770, 0x70012170, 0x70012180, 0xf0117801, 0xd0fb0f80, 0xf0107800, 0xbf1c0f20, 0x47702067,
    0x0f10f010, 0x2068bf1c, 0xf0104770, 0xbf180001, 0x47702069, 0xbf042800, 0x47702004, 0x4604b510,
    0xf06f4ac7, 0x6050403b, 0x428148c6, 0x206bbf14, 0x28002000, 0xbd10bf18, 0xf7ff4620, 0x4603ffd2,
    0xf7ff4620, 0x4618ffc1, 0x2800bd10, 0x2004bf04, 0x23004770, 0x60936053, 0x611360d3, 0x61936153,
    0x601161d3, 0x605168c1, 0x1001e9d0, 0xf0f0fbb1, 0x20086090, 0xe9c22110, 0xe9c20103, 0x20041005,
    0x200061d0, 0xe92d4770, 0xb0884df0, 0x46984615, 0x4682460c, 0xf7ff466a, 0x462affd8, 0x46504621,
    0xf0009b04, 0x0007f92f, 0xb008bf1c, 0x8df0e8bd, 0x4600e9dd, 0x1e451960, 0xf0f6fbb5, 0x5110fb06,
    0x1c40b111, 0x1e454370, 0xbf9842ac, 0xb270f8df, 0xf024d81c, 0xf040407f, 0xf8cb6010, 0x48990004,
    0xbf144580, 0x2000206b, 0xbf1c2800, 0xe8bdb008, 0x46508df0, 0xff75f7ff, 0xf8da4607, 0x28000010,
    0x4780bf18, 0x4434b917, 0xd9e242ac, 0xf7ff4650, 0xb008ff5b, 0xe8bd4638, 0x2a008df0, 0x2004bf04,
    0xe92d4770, 0xb08945f0, 0x461e4614, 0x4680460d, 0xf7ff466a, 0x4632ff8a, 0x46404629, 0xf0009b03,
    0x0007f8e1, 0xb009bf1c, 0x85f0e8bd, 0x2e009d00, 0xf8dfbf18, 0xd025a1ec, 0x0b04f854, 0x0008f8ca,
    0x28049803, 0xf025bf04, 0xf040407f, 0xd00960c0, 0xd1092808, 0x0b04f854, 0x000cf8ca, 0x407ff025,
    0x60e0f040, 0x0004f8ca, 0xf7ff4640, 0xf8d8ff2a, 0x46071010, 0xbf182900, 0xb91f4788, 0x44059803,
    0xd1d91a36, 0xf7ff4640, 0xb009ff0f, 0xe8bd4638, 0x280085f0, 0x2004bf04, 0x4a634770, 0x4101ea42,
    0x60514a5f, 0xe92de70d, 0xb0884dff, 0x469a4614, 0x466a460d, 0xf7ff9808, 0x4622ff38, 0x9b054629,
    0xf0009808, 0x2800f88f, 0xb00cbf1c, 0x8df0e8bd, 0x4629466a, 0xf7ff9808, 0x9e00ff28, 0x8008f8dd,
    0xf1c84270, 0x40080100, 0x42b74247, 0x4447bf08, 0xbf182c00, 0xb128f8df, 0x1bbdd01f, 0xbf8842a5,
    0x98054625, 0x417ff026, 0xf0f0fbb5, 0x7180f041, 0x1004f8cb, 0xea400400, 0xf040200a, 0xf8cb00ff,
    0x98080008, 0xfecdf7ff, 0xbf1c2800, 0xe8bdb00c, 0x1b648df0, 0x4447442e, 0xb00cd1df, 0xe8bd2000,
    0x2b008df0, 0x2004bf04, 0xe92d4770, 0xb0884dff, 0xe9dd4616, 0x461d7a14, 0x466a460c, 0x8058f8dd,
    0xf7ff9808, 0xe9ddfee2, 0x46323007, 0xf0004621, 0x2800f839, 0xb00cbf1c, 0x8df0e8bd, 0x2e009c00,
    0xb00cbf04, 0x8df0e8bd, 0xb094f8df, 0x407ff06f, 0x6707ea40, 0x407ff024, 0x7000f040, 0x0004f8cb,
    0x7008f8cb, 0xf8cb6828, 0x9808000c, 0xfe89f7ff, 0xf1bab168, 0xbf180f00, 0x4000f8ca, 0x0f00f1b8,
    0x2100bf1c, 0x1000f8c8, 0xe8bdb00c, 0x99078df0, 0xf0211a76, 0x440d0103, 0x440c9907, 0xb00cd1da,
    0x8df0e8bd, 0xbf042800, 0x47702004, 0x42191e5b, 0x421abf0e, 0x47702065, 0x428b6803, 0x6840d806,
    0x44184411, 0xbf244288, 0x47702000, 0x47702066, 0x40048000, 0x000003d0, 0x40020028, 0x40001400,
    0x40020000, 0x6b65666b, 0x4000ffff, 0x40020004, 0x40020010, 0x00100008, 0x00200018, 0x00400030,
    0x00800060, 0x010000c0, 0x02000180, 0x04000300, 0x00000600, 0x00000000,
    ],

    'pc_init' : 0x20000021,
    'pc_unInit': 0x2000004B,
    'pc_program_page': 0x2000009B,
    'pc_erase_sector': 0x2000006F,
    'pc_eraseAll' : 0x2000004F,

    'static_base' : 0x20000000 + 0x00000020 + 0x000004d4,
    'begin_stack' : 0x20000000 + 0x00000800,
    'begin_data' : 0x20000000 + 0x00000A00,
    'page_size' : 0x00001000,
    'analyzer_supported' : True,
    'analyzer_address' : 0x1ffff000,  # Analyzer 0x1ffff000..0x1ffff600
    'page_buffers' : [0x20003000, 0x20004000],   # Enable double buffering
    'min_program_length' : 8,
};

class KE18F16(Kinetis):

    memoryMap = MemoryMap(
        FlashRegion(    start=0,           length=0x80000,       blocksize=0x1000, is_boot_memory=True,
            algo=FLASH_ALGO, flash_class=Flash_Kinetis),
        RamRegion(      start=0x1fff8000,  length=0x10000)
        )

    def __init__(self, link):
        super(KE18F16, self).__init__(link, self.memoryMap)
        self._svd_location = SVDFile(vendor="Freescale", filename="MKE18F16.svd")

    def create_init_sequence(self):
        seq = super(KE18F16, self).create_init_sequence()

        seq.insert_after('create_cores',
            ('disable_rom_remap', self.disable_rom_remap)
            )

        return seq

    def disable_rom_remap(self):
        # Disable ROM vector table remapping.
        self.write32(RCM_MR, RCM_MR_BOOTROM_MASK)

