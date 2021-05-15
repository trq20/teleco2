# Especificaciones

Hacer una serie de simulaciones sobre un circuito demodulador simple (detector de picos). Probar cambiando la frecuencia de la moduladora a tres valores distintos y asegurarse de que la frecuencia principal a la salida del demodulador coincida con ella. Completar una tabla como esta:

<div align="center">
  
| Número de medicion | Fm | Frecuencia medida | R | C |
| ------------------ | -- | ----------------- | - | - |
|||||
|||||

</div>

Corroboren que los valores de RC ayuden a filtrar mejor los armónicos que distorsionan la salida. Hacer por lo menos tres mediciones distintas.

Luego, armar un `README.md` con lo siguiente:

```markdown
# Demodulador - Detector de picos

Alumno: Apellido y nombre
Curso: Curso
Materia: Telecomunicaciones II

[Tabla de mediciones]

### Medición 1

[Imagen del osciloscopio]

[Imagen con el espectro de frecuencias]

...

## Conclusiones de la simulación

[Comenten y comparen las cosas que hayan observado al cambiar valores de resistencia y capacitor o cualquier otra cosa que hayan notado]
```

## Consideraciones

- Recuerden que el valor de la frecuencia de corte de un filtro (pasa bajos en este caso) se calcula como:

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=f_c = \frac{1}{2 \pi R C}">
</p>

- Para determinar los valores apropiados de capacitor y resistencia, pueden usar esta fórmula:

<p align="center">
  <img align="center" src="https://render.githubusercontent.com/render/math?math=f_{m_{max}} = \frac{\sqrt{1/m^2 - 1}}{2 \pi R C}">
</p>

## Como entregar

Pongan el `README.md` y las imágenes que hayan tomado dentro de una carpeta y corran en una terminal:

```
git init
git add .
git commit -m "Initial commit"
git checkout -b teleco2/2021/superheterodino/demodulador
git push https://github.com/trq20/USERNAME.git teleco2/2021/superheterodino/demodulador
```

Donde `USERNAME` es su nombre de usuario. Pueden verificar que se haya subido visitando `https://github.com/trq20/USERNAME/tree/teleco2/2021/superheterodino/demodulador`.

