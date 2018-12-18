# TODO: don't use round

from __future__ import division

from mpmath import *

# XXX: these shouldn't be visible(?)
LU_decomp = mp.LU_decomp
L_solve = mp.L_solve
U_solve = mp.U_solve
householder = mp.householder
improve_solution = mp.improve_solution

A1 = matrix([[3, 1, 6],
             [2, 1, 3],
             [1, 1, 1]])
b1 = [2, 7, 4]

A2 = matrix([[ 2, -1, -1,  2],
             [ 6, -2,  3, -1],
             [-4,  2,  3, -2],
             [ 2,  0,  4, -3]])
b2 = [3, -3, -2, -1]

A3 = matrix([[ 1,  0, -1, -1,  0],
             [ 0,  1,  1,  0, -1],
             [ 4, -5,  2,  0,  0],
             [ 0,  0, -2,  9,-12],
             [ 0,  5,  0,  0, 12]])
b3 = [0, 0, 0, 0, 50]

A4 = matrix([[10.235, -4.56,   0.,   -0.035,  5.67],
             [-2.463,  1.27,   3.97, -8.63,   1.08],
             [-6.58,   0.86,  -0.257, 9.32, -43.6 ],
             [ 9.83,   7.39, -17.25,  0.036, 24.86],
             [-9.31,  34.9,   78.56,  1.07,  65.8 ]])
b4 = [8.95, 20.54, 7.42, 5.60, 58.43]

A5 = matrix([[ 1,  2, -4],
             [-2, -3,  5],
             [ 3,  5, -8]])

A6 = matrix([[ 1.377360,  2.481400,   5.359190],
             [ 2.679280, -1.229560,  25.560210],
             [-1.225280+1.e6,  9.910180, -35.049900-1.e6]])
b6 = [23.500000, -15.760000, 2.340000]

A7 = matrix([[1, -0.5],
             [2, 1],
             [-2, 6]])
b7 = [3, 2, -4]

A8 = matrix([[1, 2, 3],
             [-1, 0, 1],
             [-1, -2, -1],
             [1, 0, -1]])
b8 = [1, 2, 3, 4]

A9 = matrix([[ 4,  2, -2],
             [ 2,  5, -4],
             [-2, -4, 5.5]])
b9 = [10, 16, -15.5]

A10 = matrix([[1.0 + 1.0j, 2.0, 2.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0]])
b10 = [1.0, 1.0 + 1.0j, 1.0]


def test_LU_decomp():
    A = A3.copy()
    b = b3
    A, p = LU_decomp(A)
    y = L_solve(A, b, p)
    x = U_solve(A, y)
    assert p == [2, 1, 2, 3]
    assert [round(i, 14) for i in x] == [3.78953107960742, 2.9989094874591098,
            -0.081788440567070006, 3.8713195201744801, 2.9171210468920399]
    A = A4.copy()
    b = b4
    A, p = LU_decomp(A)
    y = L_solve(A, b, p)
    x = U_solve(A, y)
    assert p == [0, 3, 4, 3]
    assert [round(i, 14) for i in x] == [2.6383625899619201, 2.6643834462368399,
            0.79208015947958998, -2.5088376454101899, -1.0567657691375001]
    A = randmatrix(3)
    bak = A.copy()
    LU_decomp(A, overwrite=1)
    assert A != bak

def test_inverse():
    for A in [A1, A2, A5]:
        inv = inverse(A)
        assert mnorm(A*inv - eye(A.rows), 1) < 1.e-14

def test_householder():
    mp.dps = 15
    A, b = A8, b8
    H, p, x, r = householder(extend(A, b))
    assert H == matrix(
    [[mpf('3.0'), mpf('-2.0'), mpf('-1.0'), 0],
     [-1.0,mpf('3.333333333333333'),mpf('-2.9999999999999991'),mpf('2.0')],
     [-1.0, mpf('-0.66666666666666674'),mpf('2.8142135623730948'),
      mpf('-2.8284271247461898')],
     [1.0, mpf('-1.3333333333333333'),mpf('-0.20000000000000018'),
      mpf('4.2426406871192857')]])
    assert p == [-2, -2, mpf('-1.4142135623730949')]
    assert round(norm(r, 2), 10) == 4.2426406870999998

    y = [102.102, 58.344, 36.463, 24.310, 17.017, 12.376, 9.282, 7.140, 5.610,
         4.488, 3.6465, 3.003]

    def coeff(n):
        # similiar to Hilbert matrix
        A = []
        for i in range(1, 13):
            A.append([1. / (i + j - 1) for j in range(1, n + 1)])
        return matrix(A)

    residuals = []
    refres = []
    for n in range(2, 7):
        A = coeff(n)
        H, p, x, r = householder(extend(A, y))
        x = matrix(x)
        y = matrix(y)
        residuals.append(norm(r, 2))
        refres.append(norm(residual(A, x, y), 2))
    assert [round(res, 10) for res in residuals] == [15.1733888877,
           0.82378073210000002, 0.302645887, 0.0260109244,
           0.00058653999999999998]
    assert norm(matrix(residuals) - matrix(refres), inf) < 1.e-13

def test_factorization():
    A = randmatrix(5)
    P, L, U = lu(A)
    assert mnorm(P*A - L*U, 1) < 1.e-15

def test_solve():
    assert norm(residual(A6, lu_solve(A6, b6), b6), inf) < 1.e-10
    assert norm(residual(A7, lu_solve(A7, b7), b7), inf) < 1.5
    assert norm(residual(A8, lu_solve(A8, b8), b8), inf) <= 3 + 1.e-10
    assert norm(residual(A6, qr_solve(A6, b6)[0], b6), inf) < 1.e-10
    assert norm(residual(A7, qr_solve(A7, b7)[0], b7), inf) < 1.5
    assert norm(residual(A8, qr_solve(A8, b8)[0], b8), 2) <= 4.3
    assert norm(residual(A10, lu_solve(A10, b10), b10), 2) < 1.e-10
    assert norm(residual(A10, qr_solve(A10, b10)[0], b10), 2) < 1.e-10

def test_solve_overdet_complex():
    A = matrix([[1, 2j], [3, 4j], [5, 6]])
    b = matrix([1 + j, 2, -j])
    assert norm(residual(A, lu_solve(A, b), b)) < 1.0208

def test_singular():
    mp.dps = 15
    A = [[5.6, 1.2], [7./15, .1]]
    B = repr(zeros(2))
    b = [1, 2]
    def _assert_ZeroDivisionError(statement):
        try:
            eval(statement)
            assert False
        except (ZeroDivisionError, ValueError):
            pass
    for i in ['lu_solve(%s, %s)' % (A, b), 'lu_solve(%s, %s)' % (B, b),
              'qr_solve(%s, %s)' % (A, b), 'qr_solve(%s, %s)' % (B, b)]:
        _assert_ZeroDivisionError(i)

def test_cholesky():
    assert fp.cholesky(fp.matrix(A9)) == fp.matrix([[2, 0, 0], [1, 2, 0], [-1, -3/2, 3/2]])
    x = fp.cholesky_solve(A9, b9)
    assert fp.norm(fp.residual(A9, x, b9), fp.inf) == 0

def test_det():
    assert det(A1) == 1
    assert round(det(A2), 14) == 8
    assert round(det(A3)) == 1834
    assert round(det(A4)) == 4443376
    assert det(A5) == 1
    assert round(det(A6)) == 78356463
    assert det(zeros(3)) == 0

def test_cond():
    mp.dps = 15
    A = matrix([[1.2969, 0.8648], [0.2161, 0.1441]])
    assert cond(A, lambda x: mnorm(x,1)) == mpf('327065209.73817754')
    assert cond(A, lambda x: mnorm(x,inf)) == mpf('327065209.73817754')
    assert cond(A, lambda x: mnorm(x,'F')) == mpf('249729266.80008656')

@extradps(50)
def test_precision():
    A = randmatrix(10, 10)
    assert mnorm(inverse(inverse(A)) - A, 1) < 1.e-45

def test_interval_matrix():
    a = iv.matrix([['0.1','0.3','1.0'],['7.1','5.5','4.8'],['3.2','4.4','5.6']])
    b = iv.matrix(['4','0.6','0.5'])
    c = iv.lu_solve(a, b)
    assert c[0].delta < 1e-13
    assert c[1].delta < 1e-13
    assert c[2].delta < 1e-13
    assert 5.25823271130625686059275 in c[0]
    assert -13.155049396267837541163 in c[1]
    assert 7.42069154774972557628979 in c[2]

def test_LU_cache():
    A = randmatrix(3)
    LU = LU_decomp(A)
    assert A._LU == LU_decomp(A)
    A[0,0] = -1000
    assert A._LU is None

def test_improve_solution():
    A = randmatrix(5, min=1e-20, max=1e20)
    b = randmatrix(5, 1, min=-1000, max=1000)
    x1 = lu_solve(A, b) + randmatrix(5, 1, min=-1e-5, max=1.e-5)
    x2 = improve_solution(A, x1, b)
    assert norm(residual(A, x2, b), 2) < norm(residual(A, x1, b), 2)

def test_exp_pade():
    for i in range(3):
        dps = 15
        extra = 5
        mp.dps = dps + extra
        dm = 0
        while not dm:
            m = randmatrix(3)
            dm = det(m)
        m = m/dm
        a = diag([1,2,3])
        a1 = m**-1 * a * m
        mp.dps = dps
        e1 = expm(a1, method='pade')
        mp.dps = dps + extra
        e2 = m * a1 * m**-1
        d = e2 - a
        #print d
        mp.dps = dps
        assert norm(d, inf).ae(0)
    mp.dps = 15

