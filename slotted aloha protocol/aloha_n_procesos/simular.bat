@echo off
set SDTEXTSYNFILE=siminit.syn
for %%i in (0 01 025 05 075 1 125 150 175 2 25 3 35 4 45 5 6 7 8 9 95) do (
echo PG=0.%%i en fichero: resultado_0_%%i.txt
echo N_nodos 7 > siminit.syn
echo PG 0.%%i >> siminit.syn
aloha_smc.exe > resultados\resultado_0_%%i.txt
)