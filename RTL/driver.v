task drv_random;

input integer iteration;

  repeat (iteration) begin  
    @(negedge iClock or negedge iReset) begin
	if(RGU.wInstructionPointer == 6'd0) begin
	        random = $random;
	end	//RGU.DATA_RAM.Ram[1] = {11'b0,random,17'b0};   
    end
  end
endtask

task drv_ram;

input integer iteration;

  repeat (iteration) begin  
    @(negedge iClock) begin
	RGU.DATA_RAM.Ram[1] = {8'b0,random,17'b0};   
    end
  end
endtask
