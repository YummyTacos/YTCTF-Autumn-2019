
 
jmp main

  label  print
 
 dup
	 jz	  print_end
	
  printc
 
jmp  print

  label	  print_end
 

drop
	
ret
  label 	input
 
 dup	
	 readc 
 dup			retrieve  push 	 	 \n
	  	sub
	 jz		input_end
  push 	1
	   add
 
jmp 	input

  label		input_end
 
 dup  push 	    	33
	  	sub  push 	     32
 
	swap		 store  push  0
		 store
	
ret
  label  	xor_init
  push 	 2
  push  0
		 store  push 		3
  push  0
		 store
  label   xor
 
 dup  push 	 2
	 		mod  push  0
 
	swap		 store  push 	 2
	 	 div 
	swap 
 dup  push 	 2
	 		mod  push 	1
 
	swap		 store  push 	 2
	 	 div  push  0
			retrieve  push 	1
			retrieve	   add  push 	 2
	 		mod  push 	 2
			retrieve
 	call 	 shl
  push 	 2
			retrieve  push 	1
	   add 
	swap  push 		3
			retrieve	   add  push 		3
 
	swap		 store 
 dup  push 	   8
	  	sub 
	swap    push 	 2
 
	swap		 store
		jn   xor
 

drop 

drop
	
ret
  label 	 shl
 
 dup
	 jz		 shl_end
 
	swap  push 	 2
	  
mul 
	swap  push 	1
	  	sub
 
jmp 	 shl

  label		 shl_end
 

drop
	
ret
  label main
  push  0
  push 			    112
  push 	  4
  push 	 	 10
  push 	  	 18
  push 	  4
  push 	   	17
  push 	   	  68
  push  \0
  push 	 	 \n
  push 					 	}
  push 		  			g
  push 	      @
  push  		   	1
  push 		  		 f
  push 	 					_
  push 		  	 	e
  push 		   		c
  push 		    	a
  push 			    p
  push 			  		s
  push 		  	 	e
  push 			 	  t
  push 		 	  	i
  push 		 	   h
  push 			 			w
  push 	 					_
  push 	 					_
  push 		 			 n
  push  		  		3
  push 		  	  d
  push 		  	  d
  push  		   	1
  push 		 	   h
  push 				 		{
  push 		  		 f
  push 			 	  t
  push 		   		c
  push 			 	  t
  push 				  	y

 	call  print
  push 	 				 94
  push 		   	49
  push 	 		  44
  push  \0
  push 	     space
  push 					 >
  push 					 >
  push 					 >
  push 	 	 \n
  push 		  			g
  push 		    	a
  push 		 		  l
  push 		  		 f
  push 	     space
  push 			 	  t
  push 			 	 	u
  push 			    p
  push 		 			 n
  push 	  	  	I

 	call  print
  push 		 	 26
  push 		 		 54
  push 	 	  	41
  push 	   	 	69
  push 	     	65
  push 	1
  push 	  4
  push 		  12
  push 			 	29
  push 	    	33

 	call 	input
  push 	  	 18
  push 	 			23
  push 	 			23
  push 		 	13
  push 	    	33

  label    xor_loop
 
 dup			retrieve
	 jz 	  xor_loop_end
 
 dup 
 dup  push 	     32
	  	sub  push 	     32
			retrieve	 		mod  push 	    	33
	   add			retrieve 
	swap			retrieve
 	call  	xor_init
 
 dup  push 		3
			retrieve		 store  push 	1
	   add
 
jmp    xor_loop

  label 	  xor_loop_end
 

drop  push 	  4
  push 	    	33
		 store
  label			check_loop
  push 	  4
			retrieve			retrieve 
 dup
	 jz     check_loop_end
	  	sub  push 	  4
			retrieve  push 	1
	   add  push 	  4
 
	swap		 store
	 jz			check_loop

  label	    false
  push  \0
  push 		  	  d
  push 		    	a
  push 	    	 B

 	call  print

 
jmp    	END

  label     check_loop_end
 
	swap	  	sub
		jn	    flase
  push  \0
  push 		  	  d
  push 		 				o
  push 		 				o
  push 	   			G

 	call  print

  lable    	END



end
