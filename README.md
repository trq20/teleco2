# Especificaciones

Hacer un programa que grafique el rendimiento de las siguientes modulaciones AM para índices de modulación de 0 a 1:

- Doble banda lateral, portadora de máxima potencia (`DSBFC`).
- Banda lateral única, portadora de máxima potencia (`SSBFC`).
- Banda lateral única, portadora reducida (`SSBRC`).
- Banda lateral única, portadora suprimida (`SSBSC`).
- Banda lateral independiente (`ISB`).

El gráfico debe tener un `label` para cada curva de rendimiento indicando el nombre de la modulación como se mencionan arriba (`DSBFC`, `SSBFC`, etc).

Luego, armar un `README.md` con lo siguiente:

```markdown
# Rendimiento - BLU

Alumno: Apellido y nombre
Curso: Curso
Materia: Telecomunicaciones II

[Gráfico]
```

## Como entregar

Pongan en una carpeta el `README.md`, `rendimiento.py` y `img.png` en una carpeta, abran una terminal y corran:

```
git init
git add README.md rendimiento.py img.png
git commit -m "Initial commit"
git checkout -b teleco2/2021/blu/rendimiento
git push https://github.com/trq20/USERNAME.git teleco2/2021/blu/rendimiento
```

Donde `USERNAME` es su nombre de usuario de GitHub. Pueden verificar la entrega en `https://github.com/trq20/USERNAME/tree/teleco2/2021/blu/rendimiento`.

