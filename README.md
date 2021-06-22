## Especificaciones

Van a encontrar dos circuitos moduladores de `DSBSC` ya funcionando a unas determinadas moduladoras y portadoras, pero no llegan a ser del todo `BLU` porque aún tiene ambas bandas laterales. A partir de estos circuitos deben:

- Simular ambos circuitos y observar las mediciones en el osciloscopio y el gráfico de Fourier.
- Proponer las características de un filtro que deban poner a la salida del modulador para poder eliminar la banda que no se desee.
- Las características arriba mencionadas deben estar en una tabla como esta:

| Tipo de filtro | Frecuencia de corte 1 | Frecuencia de corte 2 | Ancho de banda |
| -------------- | --------------------- | --------------------- | -------------- |
|                |                       |                       |                |

- Justificar la decisión.

Luego, armar un `README.md` con lo siguiente:

```markdown
# BLU - Moduladores

Alumno: Nombre y apellido
Curso: Curso
Materia: Telecomunicaciones II

## Anillo balanceado

[osciloscopio]

[fourier]

[tabla]

#### Justificación de la decisión:

## Puente balanceado

[osciloscopio]

[fourier]

[tabla]

#### Justificación de la decisión:
```

## Consideraciones

- Escencialmente tienen cuatro tipos de filtros, sean activos o pasivos: `pasa bajos`, `pasa altos`, `pasa banda`, `rechaza banda`. Dentro de esas opciones, hay algunos mas apropiados que otros para cada caso dependiendo de la banda que quieran suprimir y las frecuencias ya fijadas.
- **No tienen que calcular los componentes del filtro**. Solo es suficiente con que identifiquen el apropiado con las características que deba tener.
- No todos los filtros tienen un ancho de banda definido o dos frecuencias de corte.

## Como entregar

Pongan el `README.md` y las imagenes en una carpeta, abran una terminal y escriban:

```
git init
git add README.md img1.PNG img2.PNG img3.PNG img4.PNG
git commit -m "Iniitial commit"
git checkout -b teleco2/2021/blu/moduladores
git push https://github.com/trq20/USERNAME.git teleco2/2021/blu/moduladores
```

Donde `USERNAME` es su nombre de usuario de GitHub. Pueden verificar la entrega en `https://github.com/trq20/USERNAME/tree/teleco2/2021/blu/moduladores`.
