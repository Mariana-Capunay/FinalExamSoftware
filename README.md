# FinalExamSoftware


To run the program: 



    uvicorn <main_file>:<app_name> --reload


or :


    python main.py


    
The default url is: http://127.0.0.1:8000/


To see the endpoints documentation http://127.0.0.1:8000/docs


To run the tests, execute: 

    pytest


# Solution P3

## Soporte de valor máximo de 200 soles

Si la transferencia debe ser como máximo 200 soles por día, se debe asignar a una variable tal como ´max_transfer´ el valor de 200. De este modo, en cada transferencia ir disminuyendo el valor de la a max_transfer. Si el valor de la transferencia es mayor a max_transfer, se debe retornar un mensaje de error. Guardar el valor de la primera transferencia en variable que indique la fecha de la transferencia. Ahora, si la fecha de la transferencia es diferente a la fecha de la primera transferencia, se debe reiniciar el valor de max_transfer a 200 y guardar la fecha de la transferencia en la variable de la fecha de la primera transferencia.

## Casos de prueba necesarios (caso de maximo valor de 200 soles)

Para este caso, se deben realizar los siguientes casos de prueba:

1. Transferencia de 200 soles en la primera transferencia
    - Se espera que la transferencia sea exitosa
2. Transferencia de 201 soles en la primera transferencia
    - Se espera que la transferencia falle

3. Diferentes montos de trasnferencia en el mismo día (menores a 200 soles)
    - Se espera que la transferencia sea exitosa

4. Diferentes montos de trasnferencia en el mismo día (mayores a 200 soles)
    - Se espera que la transferencia falle

## Los casos de prueba existentes garantizar que no se introduzcan errores en el código

Los casos de prueba existentes garantizan que no se introduzcan errores en el código, ya que se están probando los casos de éxito y de fallo. Por lo tanto, se está probando el código en diferentes escenarios y se está garantizando que el código funcione correctamente.



