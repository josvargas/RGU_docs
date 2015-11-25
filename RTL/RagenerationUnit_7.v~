/**********************************************************************************
Theia, Ray Cast Programable graphic Processing Unit.
Copyright (C) 2014  Diego Valverde (diego.valverde.g@gmail.com)

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

***********************************************************************************/
`include "Definitions.v"

module RayGenerationUnit
(
 input wire                       iClock,
 input wire                       iReset,
 input wire                       iEnable,
  
 //FIFO Signals
 output reg                    oFifoPush,
 output wire [`GPU_WORD-1:0]   oFifoData,
 
 //UART signals
 input wire                    iUartSelected,
 input wire                    iUartWrite,
 input wire   [7:0]            iUartAddr,
 input wire   [`GPU_WORD-1:0]  iUartData,
 output wire  [`GPU_WORD-1:0]  oUartData
);

wire [`RGU_INSN_SZ-1:0]          wInstructionData,wCurrentInstruction;
wire [2:0]                       wOperation;
wire [5:0]                       wInstructionAddr,wInstructionPointer;
wire                             wInstructionWriteEnable;
wire [`RGU_RF_BUS_SZ-1:0]        wRegReadAddr0,wRegReadAddr1,wRegWriteAddr,wDestination;
reg  [`RGU_RF_BUS_SZ-1:0]        rRegWriteAddr,rRegReadAddr0,rRegReadAddr1;
wire                             wRegWriteEnable;
reg  [2*`GPU_WORD-1:0]  	rResult, rResultOld;
wire [2*`GPU_WORD-1:0]  	wRegWriteData;
wire [`GPU_WORD-1:0] 		wSrtRoot;
wire [2*`GPU_WORD-1:0]  	wA, wB, wSubResult, wSourceA, wSourceB;
reg                   		rDataWriteEnable;
wire                  		wInstructionStopBit;
wire                  		wInstructionResetBit;

assign oFifoData   = wA[31:0];

assign oUartData               = (iUartAddr[`RGU_UART_ADDR_INSN]) ? wCurrentInstruction   : wB[31:0];	//Select between instruction or register to output into UART
assign wInstructionAddr        = (iEnable) ? wInstructionPointer     : iUartAddr[4:0];
assign wInstructionData        = iUartData[15:0];
assign wInstructionWriteEnable = (~iEnable & iUartAddr[`RGU_UART_ADDR_INSN] & iUartWrite & iUartSelected );
assign wInstructionStopBit     = wCurrentInstruction[ `RGU_STOP_BIT ];
assign wInstructionResetBit    = (wInstructionPointer == 6'd36);

//Register file UART MUX select
assign wRegReadAddr0    = (iEnable) ? wCurrentInstruction[ `RGU_OPERAND_B_RNG ] : iUartAddr[`RGU_RF_BUS_SZ-1:0];
assign wRegReadAddr1    = wCurrentInstruction[ `RGU_OPERAND_A_RNG ];
assign wRegWriteAddr    = (iEnable) ?  wDestination : iUartAddr[`RGU_RF_BUS_SZ-1:0];
assign wRegWriteEnable  = (iEnable) ? rDataWriteEnable           : (~iUartAddr[`RGU_UART_ADDR_INSN] & iUartWrite & iUartSelected);
assign wRegWriteData    = (iEnable) ? rResult                    : iUartData;

UPCOUNTER_POSEDGE # (6) IP
(
.Clock(   iClock                            ), 
.Reset(   iReset | wInstructionResetBit     ),
.Initial( 5'b0                              ),
.Enable(  iEnable & ~wInstructionStopBit    ), 
.Q(       wInstructionPointer               )
);

RAM_DUAL_READ_PORT # ( .DATA_WIDTH(64), .ADDR_WIDTH(`RGU_RF_BUS_SZ), .MEM_SIZE(32) ) DATA_RAM
(
  .Clock(          iClock           ) ,
  .iWriteEnable(   wRegWriteEnable  ),
  .iReadAddress0(  wRegReadAddr0    ),
  .iReadAddress1(  wRegReadAddr1    ),
  .iWriteAddress(  wRegWriteAddr    ),
  .iDataIn(        wRegWriteData    ),
  .oDataOut0(      wSourceB         ),
  .oDataOut1(      wSourceA         )
 
);

RAM_SINGLE_READ_PORT # ( .DATA_WIDTH(`RGU_INSN_SZ), .ADDR_WIDTH(6), .MEM_SIZE(64) ) INSTRUCTION_RAM
(
  .Clock( iClock ) ,
  .iWriteEnable(  wInstructionWriteEnable ),
  .iReadAddress0( wInstructionPointer     ),
  .iWriteAddress( wInstructionAddr        ),
  .iDataIn(       wInstructionData        ),
  .oDataOut0(     wCurrentInstruction     )
 
);

FFD_POSEDGE_SYNCRONOUS_RESET # (3) FFD_OP
(
.Clock(   iClock                                       ), 
.Reset(   iReset                                       ),
.Enable(  1'b1                                         ),
.D(       wCurrentInstruction [ `RGU_OPERATION_RNG ]  ),
.Q(       wOperation                                   )
);


FFD_POSEDGE_SYNCRONOUS_RESET # (`RGU_RF_BUS_SZ) FFD_DST
(
.Clock(   iClock                                       ), 
.Reset(   iReset                                       ),
.Enable(  1'b1                                         ),
.D(       wCurrentInstruction[ `RGU_DST_RNG ]         ),
.Q(       wDestination                                 )
);

SUB SUBTRACT
(
	.iA( wA),
	.iB( wB ),
	.oR( wSubResult )
);

/*SQUAREROOT_LUT SQRT
(
	.I(wA[31:0]),
	.O(wSrtRoot)
);*/	

SquareRoot sqrt
(
	.iOperand(wA[31:0]),							
	.oResult(wSrtRoot)
);

always @ ( posedge iClock )
begin

	if ( iReset ) 
		rRegWriteAddr <= 0;
	else rRegWriteAddr <= wRegWriteAddr; 
end

always @ ( posedge iClock )
begin

	if ( iReset )
		rResultOld <= 0;
	else rResultOld <= rResult;
end

always @ ( posedge iClock )
begin

	if ( iReset )
		rRegReadAddr1 <= 0;
	else rRegReadAddr1 <= wRegReadAddr1;
end

always @ ( posedge iClock )
begin

	if ( iReset )
		rRegReadAddr0 <= 0;
	else rRegReadAddr0 <= wRegReadAddr0;
end

assign wA = (rRegWriteAddr!=rRegReadAddr1 || wOperation==3'd5)?wSourceA:rResultOld;

assign wB = (rRegWriteAddr!=rRegReadAddr0 || wOperation==3'd5)?wSourceB:rResultOld;

always @ ( * )
begin
	case (wOperation)
	
	
	`RGU_NOP:
	begin
		rDataWriteEnable   = 1'b0;
		rResult            = 32'b0;
		oFifoPush          = 1'b0;
		

	end
	
	`RGU_MUL: 
	begin
		rDataWriteEnable   = 1'b1;
		rResult            = (wA * wB)>>`SCALE;
		oFifoPush          = 1'b0;

	end
	
	`RGU_SUB: 
	begin
		rDataWriteEnable   = 1'b1;
      		rResult            = wSubResult;
		oFifoPush          = 1'b0;
		

	end
	
	`RGU_ADD: 
	begin
		rDataWriteEnable   = 1'b1;
      		rResult            = wA+wB;
		oFifoPush          = 1'b0;
	end
	
	`RGU_DIV: 
	begin
		rDataWriteEnable   = 1'b1;
      		rResult            = wA >> 1;
		oFifoPush          = 1'b0;
		
	
	end
	
	`RGU_SQRT:
	begin
	   	rDataWriteEnable   = 1'b1;
		rResult            = {32'b0,wSrtRoot};
		oFifoPush          = 1'b0;
	end
	
	`RGU_PUSH:
	begin
	   	rDataWriteEnable   = 1'b1;
		rResult            = wA; //wSrtRoot;
		oFifoPush          = 1'b1;

	end
	
	default:
	begin
		rDataWriteEnable   = 1'b0;
		rResult            = 32'b0;
		oFifoPush          = 1'b0;
	end
	endcase
end
/*
	  
	  
	  
*/
/*
//----------------------------------------------------------
function GenerateRay()
{
	vector UnnormalizedDirection, S,Xn, tmp;
	gDebugState = DB_STATE_GEN_RAY;
	UnnormalizedDirection = (ProjectionWindowMin + Pixel2DPosition * ProjectionWindowScale  ) - CameraPosition;	
	
	tmp = UnnormalizedDirection * UnnormalizedDirection;		//tmp = (x^2,y^2,z^2)   
	S = tmp.xxx + tmp.yyy + tmp.zzz;
	Xn = inv_sqrt ( S ); // this is 1/sqrt( int( S )) = Xn
	RayDirection = UnnormalizedDirection * ( (Xn >> R0.yyy)*((0x60000,0x60000,0x60000)  - S*Xn*Xn ) );
	
	
			  RayDirection.x = 0xffff1ea7;
			  RayDirection.y = 0xfffe3d54;
			  RayDirection.z = 0xffffa525;
	
		 
		
	return ;

}
*/


endmodule
