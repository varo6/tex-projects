# makefile for System: Aloha

sctAUTOCFGDEP =
sctCOMPFLAGS = -DXUSE_GENERIC_FUNC

!include $(SCTDIR)\make.opt

default: Aloha$(sctEXTENSION)

Aloha$(sctEXTENSION): \
  Aloha$(sctOEXTENSION) \
  $(sctLINKKERNELDEP)
	$(sctLD) @<<
	$(sctLDFLAGS)
	 Aloha$(sctOEXTENSION) $(sctLINKKERNEL)
	/OUT:Aloha$(sctEXTENSION)
<<

Aloha$(sctOEXTENSION): \
  Aloha.c
	$(sctCC) @<<
	$(sctCPPFLAGS) $(sctCCFLAGS)
	$(sctIFDEF)
	/FoAloha$(sctOEXTENSION)
	Aloha.c
<<
