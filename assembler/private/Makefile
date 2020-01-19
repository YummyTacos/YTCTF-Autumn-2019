Sources=assembler.asm
Executable=assembler

NASM=nasm
LD=ld
RM=rm

NASMFlags=-f elf64
LDFlags=-s
Source_Dir=src/
Object_Dir=obj/
Bin_Dir=bin/

Objects=$(Sources:%.asm=%.o)

AsmSources=$(addprefix $(Source_Dir),$(Sources))
CObjects=$(addprefix $(Object_Dir),$(Objects))
CExecutable=$(addprefix $(Bin_Dir),$(Executable))

all: $(CExecutable)

$(CExecutable): $(CObjects)
	$(LD) $(LDFlags) $^ -o $@

$(Object_Dir)%.o: $(Source_Dir)%.asm
	$(NASM) $(NASMFlags) $< -o $@

clean:
	$(RM) -f $(CExecutable) $(CObjects)

