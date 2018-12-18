
from ._iwriter import iwriter_base

family = 0
bitplanes = 1

def mantissa(rulestring):

    return {0, 1, 2, 3, 4, 5, 6, 7, 8}

def create_rule(rulestring):

    with open('iterators_%s.h' % rulestring, 'w') as f:
        f.write('#pragma once\n')
        f.write('#include <stdint.h>\n')
        f.write('#include "../lifeconsts.h"\n')
        f.write('#include "../lifeperm.h"\n')
        f.write('#include "../eors.h"\n')
        f.write('namespace %s {\n\n' % rulestring.replace('-', '_'))

        for iset in [['sse2'], ['sse2', 'avx'], ['sse2', 'avx', 'avx2'],
                        ['sse2', 'avx', 'avx2', 'avx512']]:

            iw = b3s23writer(f, iset)

            if 'avx512' in iset:
                f.write('\n\n#ifdef __AVX512F__\n\n')
                iw.write_function(rulestring, 48, 28)

            iw.write_function(rulestring, 32, 28)
            iw.write_function(rulestring, 28, 24)
            iw.write_function(rulestring, 24, 20)
            iw.write_function(rulestring, 20, 16)
            iw.write_function(rulestring, 16, 12)
            iw.write_function(rulestring, 12, 8)
            iw.write_iterator()

        f.write('#include "../leaf_iterators_avx512.h"\n')
        f.write('#else\n')
        f.write('#include "../leaf_iterators.h"\n')
        f.write('#endif\n\n')
        f.write('}\n')

class b3s23writer(iwriter_base):

    def load_and_hshift(self, i, oddgen, terminal):

        d = '(%1)' if (oddgen) else '(%0)'

        if ('avx512' in self.iset):
            n = [64, 48, 32, 16, 64][int(terminal)]
            self.read16n(n, d, 64 * i, 7 - 7 * (i % 2))
            regname = '%%zmm'
            inreg = regname + str(7 - 7 * (i % 2))
        else:
            regbytes = 32 if ('avx2' in self.iset) else 16
            regname = '%%ymm' if (('avx2' in self.iset) and not terminal) else '%%xmm'
            accessor = 'vmovdqu' if ('avx' in self.iset) else 'movups'
            inreg = regname + str(7 - 7 * (i % 2))

            d = d if (i == 0) else (str(regbytes * i) + d)

            self.printinstr('%s %s, %s' % (accessor, d, inreg))

        if ('avx' in self.iset):
            self.printinstr('vpsrld $1, %s, %s6' % (inreg, regname))
            self.printinstr('vpslld $1, %s, %s1' % (inreg, regname))
        else:
            self.printinstr('movdqa %s, %s6' % (inreg, regname))
            self.printinstr('movdqa %s, %s1' % (inreg, regname))
            self.printinstr('psrld $1, %s6' % regname)
            self.printinstr('pslld $1, %s1' % regname)

    def horizontal_adders(self, i):

        if ('avx512' in self.iset):
            # self.trogicgate(0b01100110, 6, 1, 9 - 7 * (i % 2)) # XOR2
            self.logicgate('pxord', 6, 1, 9 - 7 * (i % 2))
            self.trogicgate(0b11101000, 6, 1, 7 - 7 * (i % 2), 12 - 7 * (i % 2)) # MAJ
            # self.trogicgate(0b01100110, 7 - 7 * (i % 2), 9 - 7 * (i % 2), 11 - 7 * (i % 2)) # XOR3
            self.logicgate('pxord', 7 - 7 * (i % 2), 9 - 7 * (i % 2), 11 - 7 * (i % 2))
        else:
            self.logicgate('pxor', 6, 1, 9 - 7 * (i % 2))
            self.logicgate('pand', 6, 1, 10 - 7 * (i % 2))
            self.logicgate('pand', 7 - 7 * (i % 2), 9 - 7 * (i % 2), 1)
            self.logicgate('pxor', 7 - 7 * (i % 2), 9 - 7 * (i % 2), 11 - 7 * (i % 2))
            self.logicgate('por', 1, 10 - 7 * (i % 2), 12 - 7 * (i % 2))

    def vertical_bitshifts(self, i):

        if 'avx512' in self.iset:
            self.printinstr('vmovdqa64 %%zmm16, %%zmm18')
            self.printinstr('vmovdqa64 %%zmm17, %%zmm6')
            self.printinstr('vmovdqa64 %%zmm17, %%zmm8')
            self.printinstr('vmovdqa64 %%zmm16, %%zmm20')
            self.printinstr('vmovdqa64 %%zmm16, %%zmm19')
            self.logicgate('permi2d',  9 - 7 * (i % 2), 2 + 7 * (i % 2), 18)
            self.logicgate('permi2d', 11 - 7 * (i % 2), 4 + 7 * (i % 2), 6)
            self.logicgate('permi2d', 12 - 7 * (i % 2), 5 + 7 * (i % 2), 8)
            self.logicgate('permi2d',  7 - 7 * (i % 2), 0 + 7 * (i % 2), 20)
            self.logicgate('permi2d', 12 - 7 * (i % 2), 5 + 7 * (i % 2), 19)
        elif 'avx2' in self.iset:
            self.logicgate('pblendd $1,',  9 - 7 * (i % 2), 2 + 7 * (i % 2), 2 + 7 * (i % 2))
            self.logicgate('pblendd $1,', 10 - 7 * (i % 2), 3 + 7 * (i % 2), 3 + 7 * (i % 2))
            self.logicgate('pblendd $3,', 11 - 7 * (i % 2), 4 + 7 * (i % 2), 6)
            self.logicgate('pblendd $3,', 12 - 7 * (i % 2), 5 + 7 * (i % 2), 8)
            self.logicgate('pblendd $1,',  7 - 7 * (i % 2), 0 + 7 * (i % 2), 0 + 7 * (i % 2))
            self.logicgate('permd', 2 + 7 * (i % 2), 13, 2 + 7 * (i % 2))
            self.logicgate('permd', 3 + 7 * (i % 2), 13, 3 + 7 * (i % 2))
            self.printinstr('vpermq $57, %%ymm6, %%ymm6')
            self.printinstr('vpermq $57, %%ymm8, %%ymm8')
            self.logicgate('permd', 0 + 7 * (i % 2), 13, 0 + 7 * (i % 2))
        else:
            self.logicgate('pand', 13, 2 + 7 * (i % 2), 2 + 7 * (i % 2))
            self.logicgate('pand', 13, 3 + 7 * (i % 2), 3 + 7 * (i % 2))
            self.logicgate('pand', 13, 0 + 7 * (i % 2), 0 + 7 * (i % 2))
            self.logicgate('pandn',  9 - 7 * (i % 2), 13, 1)
            self.logicgate('por', 1, 2 + 7 * (i % 2), 2 + 7 * (i % 2))
            self.logicgate('pandn', 10 - 7 * (i % 2), 13, 1)
            self.logicgate('por', 1, 3 + 7 * (i % 2), 3 + 7 * (i % 2))
            self.logicgate('pandn',  7 - 7 * (i % 2), 13, 1)
            self.logicgate('por', 1, 0 + 7 * (i % 2), 0 + 7 * (i % 2))
            self.logicgate('shufps $0x39,',  2 + 7 * (i % 2), 2 + 7 * (i % 2), 2 + 7 * (i % 2))
            self.logicgate('shufps $0x39,',  3 + 7 * (i % 2), 3 + 7 * (i % 2), 3 + 7 * (i % 2))
            self.logicgate('shufps $0x4e,', 11 - 7 * (i % 2), 4 + 7 * (i % 2), 6)
            self.logicgate('shufps $0x4e,', 12 - 7 * (i % 2), 5 + 7 * (i % 2), 8)
            self.logicgate('shufps $0x39,',  0 + 7 * (i % 2), 0 + 7 * (i % 2), 0 + 7 * (i % 2))

    def everything_else(self, i):
        '''
        This routine ensures that the next cell state resides in register 6.
        '''

        if 'avx512' in self.iset:
            self.trogicgate(0b10010110, 18, 4 + 7 * (i % 2), 6) # XOR8
            self.trogicgate(0b10110010, 18, 6, 4 + 7 * (i % 2)) # MAJ(XOR2, XOR3, XOR3)
            self.trogicgate(0b10100110, 4 + 7 * (i % 2), 19, 18) # XOR(g, AND(19, NOT(18)))
            self.trogicgate(0b00010110, 18, 5 + 7 * (i % 2), 8) # 1OF3
            self.trogicgate(0b10100010, 8, 4 + 7 * (i % 2), 18) # AND(f, OR(i, NOT(g)))
            self.trogicgate(0b10101000, 18, 20, 6) # AND(h, OR(d, 20))
        else:
            self.logicgate('pxor', 4 + 7 * (i % 2), 6, 6)
            self.logicgate('pxor', 6, 2 + 7 * (i % 2), 2 + 7 * (i % 2))
            self.logicgate('por', 6, 4 + 7 * (i % 2), 1)
            self.logicgate('pand', 2 + 7 * (i % 2), 6, 6)
            self.logicgate('pandn', 1, 6, 6)

            self.logicgate('por', 2 + 7 * (i % 2), 0 + 7 * (i % 2), 0 + 7 * (i % 2)) # odd | centre-on

            self.logicgate('pxor', 5 + 7 * (i % 2), 6, 1)
            self.logicgate('por',  5 + 7 * (i % 2), 6, 6)
            self.logicgate('por',  3 + 7 * (i % 2), 8, 2 + 7 * (i % 2))
            self.logicgate('pxor', 3 + 7 * (i % 2), 8, 8)
            self.logicgate('pxor', 2 + 7 * (i % 2), 6, 6)
            self.logicgate('pxor', 8, 1, 1)
            self.logicgate('pand', 1, 6, 6)
            self.logicgate('pand', 0 + 7 * (i % 2), 6, 6)


    def save_result_avx512(self, i, oddgen, terminal, diff=False):

        n = [64, 48, 32, 16, 64][int(terminal)]

        e = '(%0)' if oddgen else '(%1)'
        offset = 64 * (i - 1) + (8 if oddgen else 0)

        if diff:
            self.read16n(n, e, offset, 8)
            self.trogicgate(0b11100100, 14, 8, 6) # Use reg14 as a mask
            self.write16n(n, 6, offset, e)
            if (diff == 'initial'):
                self.logicgate('pxord', 6, 8, 15)
                self.write16n(64, 15, 0, '(%1)')
            elif (diff == 'final'):
                self.logicgate('pxord', 6, 8, 8)
                self.printinstr('vshufi32x4 $78, %s, %s, %s' % ('%%zmm15', '%%zmm15', '%%zmm13'))
                self.logicgate('pord', 13, 15, 15)
                self.write16n(32, 15, 32, '(%1)')
                self.write16n(n, 8, 64, '(%1)')
            else:
                self.trogicgate(0b11110110, 6, 8, 15)
        else:
            self.write16n(n, 6, offset, e)

    def save_result(self, i, oddgen, terminal, diff=False):

        regbytes = 32 if ('avx2' in self.iset) else 16
        if oddgen:
            e = str(regbytes * (i - 1) + 8) + '(%0)'
        else:
            e = '(%1)' if (i == 1) else (str(regbytes * (i - 1)) + '(%1)')

        regname = '%%ymm' if (('avx2' in self.iset) and not terminal) else '%%xmm'
        accessor = 'vmovdqu' if ('avx' in self.iset) else 'movups'
        if diff:
            self.logicgate('pand', 14, 6, 6, regname)
            self.printinstr('%s %s, %s8' % (accessor, e, regname))
            self.logicgate('pandn', 8, 14, 1, regname)
            self.logicgate('por', 6, 1, 1, regname)
            self.printinstr('%s %s1, %s' % (accessor, regname, e))
            regname = '%%ymm' if ('avx2' in self.iset) else '%%xmm'
            if (diff == 'initial'):
                self.logicgate('pxor', 1, 8, 15)
                self.printinstr('%s %s15, %s' % (accessor, regname, '(%1)'))
            else:
                self.logicgate('pxor', 1, 8, 8)
                self.logicgate('por', 8, 15, 15)
            if (diff == 'final'):
                pos2 = '64(%1)' if ('avx2' in self.iset) else '32(%1)'
                pos1 = '32(%1)' if ('avx2' in self.iset) else '16(%1)'
                self.printinstr('%s %s8, %s' % (accessor, regname, pos2))
                self.printinstr('%s %s15, %s' % (accessor, regname, pos1))
        else:
            self.printinstr('%s %s6, %s' % (accessor, regname, e))

    def prologue(self):

        self.f.write('        asm (\n')

    def epilogue(self, dwidth):

        self.f.write('                : /* no output operands */ \n')
        self.f.write('                : "r" (d), "r" (e)')
        if (dwidth):
            self.f.write(', "r" (apg::__sixteen%d)' % dwidth)
        self.f.write('\n')
        self.f.write('                : "ebx", ')
        for i in range(21 if ('avx512' in self.iset) else 16):
            self.f.write('"xmm%d", ' % i)
            if (i % 6 == 4):
                self.f.write('\n' + (' ' * 20))
        self.f.write('"memory");\n\n')

    def assemble(self, rulestring, oddgen, rowcount, dwidth):

        self.prologue()
        self.preparethings(dwidth)

        rpr = 16 if ('avx512' in self.iset) else (8 if ('avx2' in self.iset) else 4)

        iters  = (rowcount - (8 if oddgen else 4)) // rpr + 2
        riters = (rowcount - 4) // rpr + 1

        for i in range(iters):

            if (i < riters):
                terminal = max(0, ((i + 1) * rpr - rowcount) // 4)
                self.load_and_hshift(i, oddgen, terminal)
                self.horizontal_adders(i)

            if (i > 0):
                self.vertical_bitshifts(i)
                self.everything_else(i)
                terminal = max(0, (i * rpr + (4 if oddgen else 0) - rowcount) // 4)

                if oddgen:
                    if (i == 1):
                        diff = 'initial'
                    elif (i + 1 == iters):
                        diff = 'final'
                    else:
                        diff = True
                else:
                    diff = False

                if 'avx512' in self.iset:
                    self.save_result_avx512(i, oddgen, terminal, diff)
                else:
                    self.save_result(i, oddgen, terminal, diff)

        self.epilogue(dwidth)

