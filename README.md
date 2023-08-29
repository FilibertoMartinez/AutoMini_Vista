


# Simulación de AutoMini V2 mediante Gazebo visualizando una vista en una ventana flotante.

## Instalaciones adicionales

### Configuración e instalación del Joystick

Instalar el controlador del Joystick desde la pagina oficial de [ROS](http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick#Installing)

### Configuración e instalación de AutoMini

Instalar el simulador de AutoMini desde el siguiente tutorial[.pdf](Documentos_de_instalación/Instalación_Simulador_GazeboAUTONOMOUS.pdf).

### Configuración del repositorio local   

Clonar el repositorio de AutoMini_Vista , dirigirse al directorio local donde se clonara el repositorio, en la terminal colocar

```
git clone https://github.com/FilibertoMartinez/AutoMini_Vista.git   
```
Para ver si el repositorio local está correctamente inicializado
#### -Comandos en Terminal 1

```
roscore  
```
#### -Comandos en Terminal 2
```
cd  AutoMini_Vista
source devel/setup.bash
cd src/Vista
rosrun Vista vista.py   
```
Si al ejecutar el programa nos aparece algo similar a ese texto quiere decir que la configuración se realizó correctamente. . ([INFO] [1693334210.836545]: publishing image  ).



##  Simulación AutoMini V2 con Joystick con Vista en ventana flotante


### -Comandos en Terminal 1  – AutoNomoMini en simulador Gazebo -

 En el directorio AutoNOMOS_simulation, ejecute el siguiente comando(Para el simulador virtual ):

```
 cd EK_AutoNOMOS_Sim/
 source devel/setup.bash
 roslaunch autonomos_gazebo_simulation curved_road.launch
```

Se debe abrir una nueva ventana de Gazebo con el automóvil y una pista.


### -Comandos en terminal 2 – Joystick node-

 /dev/input/jsX “X:0,1,2” colocar el número de puerto:
```
 rosparam set joy_node/dev "/dev/input/js0"
 rosrun joy joy_node                        
```

  Se levanta el nodo joy
 
### -Comandos en terminal 3 – Teleoperación con joystick-


- Dirigirse al  repositorio de AutoMini en simulación  mediante el Joystick el cual se  clonó previamente:

```
  source devel/setup.bash
  cd src/principal/src 
  rosrun principal joyop.py
```

### -Comandos en terminal 4 – Vista -


- Dirigirse al  repositorio de AutoMini en simulación  mediante el Joystick con Vista el cual se  clonó previamente:

```
  source devel/setup.bash
  cd src/Vista/src 
  rosrun Vista vista.py
```

Finalmente tendremos un entorno virtual en Gazebo y al pulsar un botón en el joystick este ejecutará cierto movimiento correspondiente el cual mostrara una vista frontal en una venta independiente para tener una mejor visualización de como se mueve el AutoMini V2 en la pista.
