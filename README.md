# Kata TDD: Simulador del Juego Dudo Chileno
El Dudo es un juego tradicional chileno que se juega con dados en "cachos". Las reglas utilizadas para la implementación son las especificadas en al siguiente página: https://www.donpichuncho.cl/aprende-a-jugar-dudo-en-cacho

## Colaboradores TDD 2
Matías Ignacio García Padilla
Francisca Isidora Núñez Larenas
Ignacio Alejandro Padilla Palacios

## Instalación y Ejecución
Las siguientes instrucciones asumen el uso de PyCharm, el código puede presentar problemas de ruta dentro de otros editores de código. 

Se debe configurar el proyecto para que instale las dependencias de:

    requirements.txt

Revisar que el intérprete de Python sea válido,.

El código no cuenta con un archivo main para inicializar la partida, sino que el proyecto consiste en al ejecución de tests con pytest, corroborando que el coverage de éstos sea mayor al 90%.

Para hacer esto, abrir la terminal desde la raíz del proyecto y ejecutar:

    pytest --cov
    o
    python -m pytest --cov=src --cov-report=term-missing

Con ésto, el código presentará los tests que fueron aprobados con el porcentaje de coverage correspondiente.


##  Estructura del código
Para el desarrollo del proyecto, se mantuvo la mayoría de la estructura recomendada por el profesor:
```
src/
├── juego/
│   ├── dado.py
│   ├── cacho.py
│   ├── validador_apuesta.py
│   ├── contador_pintas.py
│   ├── arbitro_ronda.py
│   └── gestor_partida.py
│
tests/
├── test_dado.py
├── test_cacho.py
├── test_validador_apuesta.py
├── test_contador_pintas.py
├── test_arbitro_ronda.py
├── test_gestor_partida.py
└── test_integracion.py
```
## Imagen de prueba del coverage
<img width="1441" height="410" alt="image" src="https://github.com/user-attachments/assets/b8ffe54f-2da5-4600-a9e5-5eb4901367cf" />




