## MANUAL DE USUARIO

Antes de correr el compilador es necesario tener instalado Python 3 y las librerias de pandas, ploty,pymongo, spcipy y matplotlib

#### Correr estos comandos:
```
pip3 install pandas
```
```
pip3 install plotly==4.3.0
```
```
python3 -m pip install pymongo
```
```
pip3 install scipy
```
```
python3 -mpip install matplotlib
```
### ¿Como hacer un programa?

Asi es la declaración:
```
PROGRAM algo:                                <--- Se declara el nombre del programa

VAR fact,i,num,nose:INT;                     <---Aquí se declaran las variables


FUNC INT:FACT(num INT,i INT,fact INT)        <---Se pueden hacer uso de funciones, y declaración 
VAR z:INT;                                       de variables locales
{
    WHILE(i < num+1)
    {
        fact = fact * i;
        i = i + 1;
    };
    RETURN(fact);

  
}

MAIN
{
    num = 5;
    i=1;
    fact=1;    
    PRINT(FACT(num,i,fact));
 
  
}

END                                          <---Se debe marcar el fin de la función
```
### ¿Como declarar variables?
```
VAR a,b:INT;
VAR arrP[5];
```
### ¿Como declarar funciones?
```
FUNC INT:FUNC1(n INT) 
VAR z:INT 
{

    codigo

};
```
### ¿Como se hace un if?
```
IF(x<=4)
{
  codigo
};
```
```
IF(n>1)
{
  codigo
}
ELSE
{
  codigo
};
```
### ¿Como se hace un while?
```
WHILE(i < num+1)
{
  codigo
};
```

### ¿Como se gráfica y/o hace los calculos estadisticos? 

```
PROGRAM algo:
VAR path:DATASET;

MAIN
{
  path = 'csv/microsoftStocks.csv';
  BASICV(path,'Close');
}

END
```
Aqui se muestra un ejemplo de como se usan las diferentes funciones especiales,
se suele mandar el nombre de las columnas x,y y para las funciones de 
AVERAGE, MEDIAN, VARIANZA y DESVT se puede escoger entre graficar en barchart
o piechart. (path,x,y,chart)

#### AVERAGE(path,'Carrera','Promedio','barchart');

#### MEDIAN(path,'Region','Total Profit','piechart');

#### PLOT(path,'High','Low','Date');

#### PIECHART(path,'Item Type','Total Revenue');

#### VARIANZA(path,'Carrera','Promedio','barchart');

#### DESVT(path,'Carrera','Promedio','barchart');

#### DISTN(path,'AAPL.Open');

#### BASICV(path,'Close');
