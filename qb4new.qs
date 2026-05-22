namespace Quantum.QB4 {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Diagnostics;

    @EntryPoint()
    operation QB4Run() : Unit {
        mutable num0000 = 0;
        mutable num0001 = 0;
        mutable num0010 = 0;
        mutable num0011 = 0;
        mutable num0100 = 0;
        mutable num0101 = 0;
        mutable num0110 = 0;
        mutable num0111 = 0;
        mutable num1000 = 0;
        mutable num1001 = 0;
        mutable num1010 = 0;
        mutable num1011 = 0;
        mutable num1100 = 0;
        mutable num1101 = 0;
        mutable num1110 = 0;
        mutable num1111 = 0;

        use qubits = Qubit[4];

        for _test in 1..100 {

            Set(Zero, qubits[0]);
            Set(Zero, qubits[1]);
            Set(Zero, qubits[2]);
            Set(Zero, qubits[3]);

            //Demo of pass through (NOP)
            //Set (Zero, qubits[0]);
            //Set (Zero, qubits[1]);
            //Set (Zero, qubits[2]);
            //Set (Zero, qubits[3]);

            //Demo of NOT gate
            //Set (Zero, qubits[0]);
            //X(qubits[0]);

            //Demo of Hadamard
            //Set (Zero, qubits[0]);
            //H(qubits[0]);

            //Demo of SWAP
            //Set (One, qubits[0]);
            //SWAP (qubits[0],qubits[1]);

            //Demo of Controlled-NOT   ( CNOT )
            //Set (One, qubits[0]);
            //Set (Zero, qubits[1]);
            //CNOT(qubits[0],qubits[1]);

            //Demo of Bell State
            Set (Zero, qubits[0]);
            Set (Zero, qubits[1]);
            H(qubits[0]);
            CNOT(qubits[0],qubits[1]);

            //Demo of Toffoli Gate in general configuration
            //Set (One, qubits[0]);
            //Set (One, qubits[1]);
            //Set (One, qubits[2]);
            //CCNOT(qubits[0],qubits[1],qubits[2]);

            //Demo of Toffoli Gate in NOT configuration
            //Set (One, qubits[0]); // Always 1
            //Set (One, qubits[1]); // Always 1
            //Set (One, qubits[2]); // Input of NOT gate. Gets inverted by NOT
            //CCNOT(qubits[0],qubits[1],qubits[2]);

            //Demo of Toffoli Gate in AND configuration
            //Set (One, qubits[0]); // Input 1 of AND
            //Set (One, qubits[1]); // Input 2 of AND
            //Set (Zero, qubits[2]);// Initialized to 0. Gets the result of AND
            //CCNOT(qubits[0],qubits[1],qubits[2]);

            //Demo of Toffoli Gate in FANOUT configuration
            //Set (One, qubits[0]); // Always 1
            //Set (One, qubits[1]); // Input & Pass through.
            //Set (Zero, qubits[2]); //Initialized to 0. Gets a result of the fanout from qubits[1]
            //CCNOT(qubits[0],qubits[1],qubits[2]);



            let res0 = M(qubits[0]);
            let res1 = M(qubits[1]);
            let res2 = M(qubits[2]);
            let res3 = M(qubits[3]);

            if (res3 == Zero and res2 == Zero and res1 == Zero and res0 == Zero) { set num0000 += 1; }
            if (res3 == Zero and res2 == Zero and res1 == Zero and res0 == One)  { set num0001 += 1; }
            if (res3 == Zero and res2 == Zero and res1 == One  and res0 == Zero) { set num0010 += 1; }
            if (res3 == Zero and res2 == Zero and res1 == One  and res0 == One)  { set num0011 += 1; }
            if (res3 == Zero and res2 == One  and res1 == Zero and res0 == Zero) { set num0100 += 1; }
            if (res3 == Zero and res2 == One  and res1 == Zero and res0 == One)  { set num0101 += 1; }
            if (res3 == Zero and res2 == One  and res1 == One  and res0 == Zero) { set num0110 += 1; }
            if (res3 == Zero and res2 == One  and res1 == One  and res0 == One)  { set num0111 += 1; }
            if (res3 == One  and res2 == Zero and res1 == Zero and res0 == Zero) { set num1000 += 1; }
            if (res3 == One  and res2 == Zero and res1 == Zero and res0 == One)  { set num1001 += 1; }
            if (res3 == One  and res2 == Zero and res1 == One  and res0 == Zero) { set num1010 += 1; }
            if (res3 == One  and res2 == Zero and res1 == One  and res0 == One)  { set num1011 += 1; }
            if (res3 == One  and res2 == One  and res1 == Zero and res0 == Zero) { set num1100 += 1; }
            if (res3 == One  and res2 == One  and res1 == Zero and res0 == One)  { set num1101 += 1; }
            if (res3 == One  and res2 == One  and res1 == One  and res0 == Zero) { set num1110 += 1; }
            if (res3 == One  and res2 == One  and res1 == One  and res0 == One)  { set num1111 += 1; }
        }

        // Return qubits to |0⟩ before release (strict simulators may care)
        Set(Zero, qubits[0]);
        Set(Zero, qubits[1]);
        Set(Zero, qubits[2]);
        Set(Zero, qubits[3]);

        let shots = 100.0;

        Message($"0000 -> {IntAsDouble(num0000)/shots}");
        Message($"0001 -> {IntAsDouble(num0001)/shots}");
        Message($"0010 -> {IntAsDouble(num0010)/shots}");
        Message($"0011 -> {IntAsDouble(num0011)/shots}");
        Message($"0100 -> {IntAsDouble(num0100)/shots}");
        Message($"0101 -> {IntAsDouble(num0101)/shots}");
        Message($"0110 -> {IntAsDouble(num0110)/shots}");
        Message($"0111 -> {IntAsDouble(num0111)/shots}");
        Message($"1000 -> {IntAsDouble(num1000)/shots}");
        Message($"1001 -> {IntAsDouble(num1001)/shots}");
        Message($"1010 -> {IntAsDouble(num1010)/shots}");
        Message($"1011 -> {IntAsDouble(num1011)/shots}");
        Message($"1100 -> {IntAsDouble(num1100)/shots}");
        Message($"1101 -> {IntAsDouble(num1101)/shots}");
        Message($"1110 -> {IntAsDouble(num1110)/shots}");
        Message($"1111 -> {IntAsDouble(num1111)/shots}");
    }

    operation Set(desired : Result, q : Qubit) : Unit {
    if (M(q) != desired) {
        X(q);
    }
}
}

