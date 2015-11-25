task checker;

//Esta tarea corresponde a la implementacion del modulo de comparacion (checkers) de la salida de datos

input integer iteration;
real error;

repeat (iteration) @ (posedge iClock) begin
	if (RGU.wInstructionPointer == 6'd0 && RGU.rResult !== 64'd0) begin
		$fdisplay(log, "Time=%.0f, Entrada=x%d, RGU Inverse square=x%d",$time,RGU.DATA_RAM.Ram[1],RGU.rResult);
	end
end
endtask
