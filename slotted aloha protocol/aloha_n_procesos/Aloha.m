# makefile for System: aloha

sctAUTOCFGDEP =
sctCOMPFLAGS = -DXUSE_GENERIC_FUNC

!include $(SCTDIR)\make.opt

default: aloha$(sctEXTENSION)

aloha$(sctEXTENSION): \
  aloha$(sctOEXTENSION) \
  $(sctLINKKERNELDEP)
	$(sctLD) @<<
	$(sctLDFLAGS)
	 aloha$(sctOEXTENSION) $(sctLINKKERNEL)
	/OUT:aloha$(sctEXTENSION)
<<

aloha$(sctOEXTENSION): \
  aloha.c
	$(sctCC) @<<
	$(sctCPPFLAGS) $(sctCCFLAGS)
	$(sctIFDEF)
	/Foaloha$(sctOEXTENSION)
	aloha.c
<<
