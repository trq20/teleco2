# Especificaciones

Hacer tres simulaciones distintas con los dos circuitos que van a encontrar en el repositorio. Y armar una tabla como la siguiente para cada circuito:

| N | Em | Ec | m | fm | fc | Δf |
| - | -- | -- | - | -- | -- | -- |
| 1 |    |    |   |    |    |    |
| 2 |    |    |   |    |    |    |
| 3 |    |    |   |    |    |    |

Donde:
- N: Número de medición.
- Em: Amplitud de la moduladora.
- Ec: Amplitud de la portadora.
- m: Índice de modulación **medido** (aproximado).
- fm: Frecuencia de moduladora.
- fc: Frecuencia de portadora.
- Δf: Ancho de banda **medido**. 

Luego armar un `README.md` con este formato:

```markdown
# Moduladores AM

Alumno: Apellido y nombre
Curso: Curso
Materia: Telecomunicaciones II

## Mediciones

### Modulador con diodo

[Tabla con resultados del circuito con diodo]

#### Medición 1

[Imagen del osciloscopio]
[Imagen del gráfico de Fourier]

...

### Modulador con transistor

[Tabla con resultados del circuito con transistor]

#### Medición 1

[Imagen del osciloscopio]
[Imagen del gráfico de Fourier]

...

## Conclusiones de ambos circuitos

[Comenten y comparen las cosas que hayan observado en las simulaciones]
```

## Consideraciones

- Los parámetros que elijan para la `moduladora` y `portadora` no deben generar distorsión en la señal de AM.
- En el modulador con diodo, las tensiones de las señales pueden estar en el orden de los pocos Volts.
- En el modulador con transistor, las tensiones de las señales no deben superar los pocos cientos de mili Volts.
- Usen frecuencias de moduladora entre `1KHz-20KHz`. Para la portadora, usen frecuencias entre los `100KHz-1500KHz`.
- El gráfico de Fourier ya está configurado puede tomar un tiempo en dar sus resultados. Se inicia la simulación de Fourier seleccionando la opción haciendo click derecho en el gráfico.
- Cuando cambien la frecuencia de portadora del circuito modulador con diodo, tengan en cuenta que van a tener que cambiar los componentes del circuito tanque RLC para que sintonice esa frecuencia. Pueden fijar el valor de L o C y despejar el otro de esta fórmula:

<img src="https://render.githubusercontent.com/render/math?math=f_0 = \frac{1}{2 \pi \sqrt{LC}}">

## Como entregar

Pongan el `README.md` y las imágenes que hayan tomado dentro de una carpeta y corran en una terminal:

```
git init
git add .
git commit -m "Initial commit"
git checkout -b teleco2/2021/am/moduladores
git push https://github.com/trq20/USERNAME.git teleco2/2021/am/moduladores
```

Donde `USERNAME` es su nombre de usuario. Pueden verificar que se haya subido visitando `https://github.com/trq20/USERNAME/tree/teleco2/2021/am/moduladores`.