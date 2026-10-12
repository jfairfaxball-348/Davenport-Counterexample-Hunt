# S032 separate INTERNAL same-executor adversarial reconstruction

This is a second symbolic pass by the session executor, NOT an external independent reviewer, Lean/Palomar or hosted CI.

1. Projective expansion: h_X=0,1,2,3 contributes respectively C(N,3), C(N-1,2), N-2, 1 potential deletion triples; h>=4 cannot contribute. The converse is false: individual nonzero factors may sum to zero across projective points.
2. Exceptional pair extensions: h=0/1 can cover any pair; h=2 requires at least one of its two zero indices in the pair, capacity C(N,2)-C(N-2,2)=2N-3; h=3 requires the pair subset H_X, capacity 3.
3. Every nonzero original z_i defines p+1 different projective annihilating functionals. Since q=p²+p+1 and N=3p, sum h=3(q-1), so sum(3-h)=3 (not zero!). If all h>=4, contradiction immediately, without any use of Psi.
4. Two original indexed positions with independent z give one annihilating projective functional; collinear nonzero z give p+1. This proves sum C(h,2)=C(N,2)+p E_par, not C(N,2)+(p+1)E_par.
5. For U algebra, E=sum_{j>=4}(j-3)Q_j >= H=sum_{j>=4}Q_j; Q2=3-3Q0-2Q1+E and Q3=q-Q0-Q1-Q2-H. Substitute carefully: coefficient of Q0 is C(N,3)-1-3(N-3); of Q1 C(N-1,2)-1-2(N-3); both nonnegative N>=21. E term (N-3)E-H >=0. Therefore U>=q+3N-9, NOT an upper bound this small.
6. p=7 b10 s+ t4 L13, forced nonzero >=24, forced exceptional unordered pairs >=72, q57,N21,U>=111. With Q0=Q1=0, Q2>=3, not <=1. Any claim that 111<24 is manifestly false.
7. Rank-one cap proof uses p scalars in one direction and the elementary p-term partial-sums theorem; no need to assume p equal vectors. Projective p+1 *distinct directions* needed for full-line blocking is different.
8. Threshold n=3(p-1) for three-deletion CW is equality, not strict. Other k>=3, source upgrades, D2 and classical rank3 D1 conjecture remain OPEN here.

FIRST STOP: no m=2p exclusion because the raw union covering inequality provably cannot contradict S031. Next route requires overlap/cancellation/actual b-block zero-sum restrictions.
