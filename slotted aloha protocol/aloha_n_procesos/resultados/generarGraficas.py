import main
import pandas as pd
import matplotlib.pyplot as plt

dfto = main.df_TOemisores[["Media TO"]]
dftc = main.df_TCemisores[["Media TC"]]
dfts = main.df_TStotales[["Media TS"]]
dftp = main.df_TPemisores[["Media TP"]]
dfpg = pd.DataFrame(main.valores, columns=['Valores'])
plt.plot(dfto, dftc)
plt.scatter(dfto, dftc, color= "midnightblue")
plt.xlabel("Tráfico Ofrecido")
plt.ylabel("Tráfico Cursado")
plt.title("Tráfico cursado frente al Tráfico Ofrecido")
plt.xticks([0, 0.5, 1, 1.5, 2, 2.5])
plt.show()

plt.plot(dftc, dfts)
plt.scatter(dftc, dfts, color= "midnightblue")
plt.xlabel("Tráfico Cursado")
plt.ylabel("Tiempo de Servicio")
plt.title("Tiempo de Servicio frente al Tráfico Cursado")
plt.show()

plt.plot(dftc, dftp)
plt.scatter(dftc, dftp, color= "midnightblue")
plt.xlabel("Tráfico Cursado")
plt.ylabel("Tráfico Perdido")
plt.title("Tráfico Perdido frente al Tráfico Cursado")
plt.show()

plt.plot(dfpg["Valores"], dftp)
plt.scatter(dfpg["Valores"], dftp, color= "midnightblue")
plt.xlabel("PG")
plt.ylabel("Tráfico Perdido")
plt.title("Tráfico Perdido frente al PG")
plt.show()

plt.plot(dfpg["Valores"], dftc)
plt.scatter(dfpg["Valores"], dftc, color= "midnightblue")
plt.xlabel("PG")
plt.ylabel("Tráfico Cursado")
plt.title("Tráfico Cursado frente al PG")
plt.show()
