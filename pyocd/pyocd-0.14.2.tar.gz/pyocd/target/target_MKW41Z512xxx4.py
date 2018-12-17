"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013,2018 ARM Limited

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

FLASH_ALGO = {
    'load_address' : 0x20000000,
    'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0x4937b510, 0x60082000, 0x78414836, 0x0f890649, 0xd0152902, 0x4a342100, 0x444a2900, 0xd0077011,
    0x229f7841, 0x70414011, 0x06497841, 0xd1fb0f89, 0x4448482e, 0xf85ef000, 0xd0002800, 0xbd102001,
    0xe7e82101, 0x44484828, 0x28007800, 0x4825d00a, 0x229f7841, 0x31404011, 0x78417041, 0x0f890649,
    0xd1fa2902, 0x47702000, 0xb5104820, 0x44484920, 0xf88cf000, 0xd1042800, 0x2100481c, 0xf0004448,
    0xbd10f946, 0x4c19b570, 0x444c4605, 0x4b184601, 0x68e24620, 0xf8b3f000, 0xd1052800, 0x46292300,
    0x68e24620, 0xf93df000, 0xb570bd70, 0x460b460c, 0x46014606, 0xb084480d, 0x44484615, 0xf8e2f000,
    0xd10a2800, 0x90029001, 0x48082101, 0x462b9100, 0x46314622, 0xf0004448, 0xb004f96b, 0x0000bd70,
    0x40048100, 0x4007e000, 0x00000004, 0x00000008, 0x6b65666b, 0xd00b2800, 0x68c949db, 0x0f090109,
    0xd007290f, 0x00494ad9, 0x5a51447a, 0xe0030289, 0x47702004, 0x04c92101, 0x2200b410, 0x60416002,
    0x60812102, 0x60c10289, 0x7a0c49d1, 0x40a3158b, 0x7ac96143, 0x62026102, 0x61816242, 0x2000bc10,
    0x28004770, 0x6101d002, 0x47702000, 0x47702004, 0x48c84602, 0x210168c0, 0x43080289, 0x60c849c5,
    0x48c54770, 0x70012170, 0x70012180, 0x06097801, 0x7800d5fc, 0xd5010681, 0x47702067, 0xd50106c1,
    0x47702068, 0xd0fc07c0, 0x47702069, 0xd1012800, 0x47702004, 0x4604b510, 0x48b84ab7, 0x48b86050,
    0xd0014281, 0xe000206b, 0x28002000, 0x4620d107, 0xffd7f7ff, 0x46204603, 0xffcaf7ff, 0xbd104618,
    0xd1012800, 0x47702004, 0x4614b510, 0x60622200, 0x60e260a2, 0x61626122, 0x61e261a2, 0x68c16021,
    0x68816061, 0xf0006840, 0x60a0f951, 0x20042108, 0x60e06121, 0x616161a0, 0x200061e0, 0xb5ffbd10,
    0x4615b089, 0x466a460c, 0xf7ff9809, 0x462affd9, 0x9b044621, 0xf0009809, 0x0007f90c, 0x9c00d130,
    0x19659e01, 0x46311e6d, 0xf0004628, 0x2900f92f, 0x1c40d002, 0x1e454370, 0xd81d42ac, 0x20090221,
    0x06000a09, 0x488c1809, 0x498d6041, 0x4288980c, 0x206bd001, 0x2000e000, 0xd1112800, 0xf7ff9809,
    0x4607ff80, 0x69009809, 0xd0002800, 0x2f004780, 0x19a4d102, 0xd9e142ac, 0xf7ff9809, 0x4638ff69,
    0xbdf0b00d, 0xd1012a00, 0x47702004, 0xb089b5ff, 0x461e4614, 0x466a460d, 0xf7ff9809, 0x4632ff91,
    0x9b034629, 0xf0009809, 0x0007f8c4, 0x9d00d12d, 0xd0262e00, 0x4870cc02, 0x99036081, 0xd0022904,
    0xd0072908, 0x022ae00e, 0x0a122103, 0x18510649, 0xe0076041, 0x60c1cc02, 0x2107022a, 0x06090a12,
    0x60411851, 0xf7ff9809, 0x4607ff3c, 0x69009809, 0xd0002800, 0x2f004780, 0x9803d103, 0x1a361945,
    0x9809d1d8, 0xff24f7ff, 0xb00d4638, 0x2800bdf0, 0x4a5cd005, 0x18890409, 0x60514a57, 0x2004e721,
    0xb5ff4770, 0x4614b08b, 0x460d461e, 0x980b466a, 0xff46f7ff, 0x46294622, 0x980b9b05, 0xf879f000,
    0xd1332800, 0x4629466a, 0xf7ff980b, 0x9d00ff39, 0x90089802, 0x42404269, 0x424f4001, 0xd10142af,
    0x183f9808, 0xd0202c00, 0x90090230, 0x42a61b7e, 0x4626d900, 0x99054630, 0xf888f000, 0x2101022a,
    0x06090a12, 0x493c1852, 0x9a09604a, 0x43100400, 0x608830ff, 0xf7ff980b, 0x2800fee4, 0x9808d106,
    0x19ad1ba4, 0x2c00183f, 0x2000d1e0, 0xbdf0b00f, 0xd1012b00, 0x47702004, 0xb089b5ff, 0x461d4616,
    0x466a460c, 0x98099f12, 0xfefaf7ff, 0x46214632, 0x98099b07, 0xf82df000, 0xd11d2800, 0x2e009c00,
    0x4929d01a, 0x18470638, 0x20010221, 0x06400a09, 0x48211809, 0x60876041, 0x60c16829, 0xf7ff9809,
    0x2800feb0, 0x9913d00a, 0xd0002900, 0x9914600c, 0xd0012900, 0x600a2200, 0xbdf0b00d, 0x1a769907,
    0x00890889, 0x9907194d, 0x2e00190c, 0xb00dd1dc, 0x2800bdf0, 0x2004d101, 0xb4104770, 0x42191e5b,
    0x421ad101, 0xbc10d002, 0x47702065, 0x428b6803, 0x6840d804, 0x18181889, 0xd2024288, 0x2066bc10,
    0xbc104770, 0x47702000, 0x40048040, 0x000003b4, 0x40020020, 0xf0003000, 0x40020000, 0x44ffffff,
    0x6b65666b, 0x4000ffff, 0x00ffffff, 0x460bb530, 0x20004601, 0x24012220, 0x460de009, 0x429d40d5,
    0x461dd305, 0x1b494095, 0x40954625, 0x46151940, 0x2d001e52, 0xbd30dcf1, 0x40020004, 0x40020010,
    0x00100008, 0x00200018, 0x00400030, 0x00800060, 0x010000c0, 0x02000180, 0x04000300, 0x00000600,
    0x00000000, 0x00000000,
    ],

    'pc_init' : 0x20000021,
    'pc_unInit': 0x20000065,
    'pc_program_page': 0x200000CB,
    'pc_erase_sector': 0x200000A5,
    'pc_eraseAll' : 0x20000089,

    'static_base' : 0x20000000 + 0x00000020 + 0x000004e0,
    'begin_stack' : 0x20000000 + 0x00000800,
    'begin_data' : 0x20000000 + 0x00000A00,
    'page_size' : 0x00000200,
    'analyzer_supported' : False,
    'analyzer_address' : 0x00000000  # ITCM, Analyzer 0x00000000..0x000000600
};

class KW41Z4(Kinetis):

    memoryMap = MemoryMap(
        FlashRegion(    start=0,           length=0x80000,      blocksize=0x800, is_boot_memory=True,
            algo=FLASH_ALGO, flash_class=Flash_Kinetis),
        RamRegion(      start=0x1fff8000,  length=0x20000)
        )

    def __init__(self, transport):
        super(KW41Z4, self).__init__(transport, self.memoryMap)
        self._svd_location = SVDFile(vendor="Freescale", filename="MKW41Z4.svd")

