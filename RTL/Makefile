all: 
	iverilog -o rgu1 SimpleOperationTestBench.v RagenerationUnit.v Collaterals.v Module_FixedPointSquareRoot.v
	iverilog -o rgu2 SimpleOperationTestBench_2.v RagenerationUnit_2.v Collaterals.v Module_FixedPointSquareRoot.v
	iverilog -o rgu3 SimpleOperationTestBench_3.v RagenerationUnit_3.v Collaterals.v Module_FixedPointSquareRoot.v
	iverilog -o rgu4 SimpleOperationTestBench_4.v RagenerationUnit_4.v Collaterals.v Module_FixedPointSquareRoot.v	
	iverilog -o rgu5 SimpleOperationTestBench_5.v RagenerationUnit_5.v Collaterals.v Module_FixedPointSquareRoot.v
	iverilog -o rgu6 SimpleOperationTestBench_6.v RagenerationUnit_6.v Collaterals.v Module_FixedPointSquareRoot.v
	iverilog -o rgu7 SimpleOperationTestBench_7.v RagenerationUnit_7.v Collaterals.v Module_FixedPointSquareRoot.v
	vvp rgu1
	vvp rgu2
	vvp rgu3
	vvp rgu4
	vvp rgu5
	vvp rgu6
	vvp rgu7	

vvp:
	vvp rgu1
	vvp rgu2
	vvp rgu3
	vvp rgu4

gtk:
	gtkwave rgu1.vcd &
