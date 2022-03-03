# Bellman-BigNat

This repository is a fork of [bellman-bignat](https://github.com/alex-ozdemir/bellman-bignat).
However, it contains the scripts that compute the proving and verification time of SNARKs based Merkle-proof aggregation.
These metrics serve as baseline to compare the performance of [Hyperproofs aggregation](https://eprint.iacr.org/2021/599.pdf).

## Instructions
These instructions have been tested on Ubuntu 20.04 with 32 GB RAM. However, it should be possible to replicate this on other operating systems.

0. Install rust nightly, python, and pandas.
   ```bash
   $ sudo apt-get install git python curl python3-pip libgmp-dev libflint-dev
   $ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

   > Choose 2 (Customize installation)
   > Choose x86_64-unknown-linux-gnu
   > Choose nightly
   > Choose default
   > Modify PATH variable? Y
   > Choose 1 (Proceed with installation)

   $ git clone https://github.com/hyperproofs/bellman-bignat.git
   $ cd bellman-bignat
   $ pip3 install -U pip pandas matplotlib

   ```
1. Run ```merkle-snarks-setup.sh```: This generates 53 GBs of SNARK parameters in folders ```pedersen-30```  and ```poseidon-30```.

2. Run ```merkle-snarks-bench.sh```: This generates the ```merkle-snarks-baseline.log``` which is automatically parsed by ```parse-logs.py```.

3. Copy ```pedersen-30-single.csv``` and ```poseidon-30-single.csv``` to [hyperproofs-go/plots](https://github.com/hyperproofs/hyperproofs-go/tree/main/plots).

## Sample output

```
 # Merkle Proofs  Init (s)  Param gen (s)  Synthesis (s)  Prover (s)  Verifier (s) Hash function
               8  0.011392       2.403595       0.922309   44.918239      0.003730      Pedersen
              16  0.019049       4.898610       1.837778   85.370906      0.003674      Pedersen
              32  0.034131       9.920707       3.680107  164.299951      0.003691      Pedersen
              64  0.065413      19.573609       7.406033  322.721494      0.003663      Pedersen
             128  0.124417      39.021922      14.783027  629.780660      0.003680      Pedersen
             256  0.244170      78.775146      29.487790 1245.032973      0.003701      Pedersen
 # Merkle Proofs  Init (s)  Param gen (s)  Synthesis (s)  Prover (s)  Verifier (s) Hash function
               8  0.037389       0.362338       1.890126   13.127884      0.003666      Poseidon
              16  0.063023       0.697382       3.750457   25.145480      0.003714      Poseidon
              32  0.112790       1.374306       7.545367   46.991624      0.003632      Poseidon
              64  0.211571       2.756442      14.998816   90.728152      0.003645      Poseidon
             128  0.411693       5.491860      30.172766  169.656314      0.003691      Poseidon
             256  0.813977      11.038503      59.979579  330.578018      0.003676      Poseidon
             512  1.600210      22.028196     120.165705  638.422871      0.003619      Poseidon
            1024  3.197752      44.199119     239.177287 1224.297817      0.003645      Poseidon
            2048  6.352535      88.361105     481.768391 2435.668560      0.003630      Poseidon
```
