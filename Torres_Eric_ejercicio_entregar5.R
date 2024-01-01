#En primer lugar, se seleccionan dos proteínas que pertenezcan a la misma familia. 
#Se ha accedido a la base de datos SCOP (Structural classification of proteins), que clasifica a las proteínas de acuerdo a: familia, superfamilia, plegamiento y clase. 
#Para seleccionar las dos secuencias de proteínas con las que se va a trabajar, se han seleccionado las siguientes categorías de proteína en función de la jerarquía: Prealbumin-like (plegamiento), Starch-binding domain-like (superfamilia), Starch-binding domain (familia) y de ahí, las proteínas beta-amilasa de Bacillus cereus (accesión de Uniprot P36924) y glucosamilasa de Aspergillus niger (accesión de Uniprot P69328, isoforma 1)

#Cargamos los paquetes necesarios: 
library(seqinr)
library(Biostrings)

#Cargamos las secuencias de las proteínas elegidas:
P36924 <- read.fasta("P36924_ej5.fasta")[[1]]
P36924
P69328 <- read.fasta("P69328_ej5.fasta")[[1]]
P69328

#Realizar una alineamiento local utilizando el algoritmo de Smith-Waterman de las dos secuencias, utilizando como matriz de sustitución una matriz de la familia BLOSUM (razonar el tipo de matriz BLOSUM seleccionada) y como penalización por apertura del hueco d = 10 y por extensión del hueco e = 5

#Para realizar el alineamiento, utilizamos la función pairwiseAlignment(). Sin embargo, se requiere que las secuencias a alinear se encuentren como una cadena de caracteres (y no como un vector de caracteres) y que el código de una letra de los residuos esté en mayúscula. Para ello, vamos a transformar las secuencias proteicas con las funciones c2s() y toupper() de forma que se cumplan los requisitos:

P36924 <- toupper(c2s(P36924))
P69328 <- toupper(c2s(P69328))

#Ejercicio 1. Realizar una alineamiento local utilizando el algoritmo de Smith-Waterman de las dos secuencias, utilizando como matriz de sustitución una matriz de la familia BLOSUM (razonar el tipo de matriz BLOSUM seleccionada) y como penalización por apertura del hueco d = 10 y por extensión del hueco e = 5.

#La matriz BLOSUM utilizada es la BLOSUM62, considerada como la estándar. En la función pairwiseAlignment, gapExtension = e y gapOpening = d-e

align <- pairwiseAlignment(P36924, P69328,
                            substitutionMatrix="BLOSUM62", gapOpening=5, gapExtension=5,
                            scoreOnly=FALSE, type="local")

#Ejercicio 2. Indicar la puntuación obtenida, el % de identidad, de similitud de los aminoácidos alineados y el % de huecos utilizados.

#Utilizamos la función writePairwiseAlignments para obtener los resultados del alineamiento realizado.
writePairwiseAlignments(align,Matrix="BLOSUM62")

#De forma más particular, para obtener el porcentaje de identidad de los aminoácidos alineados, calculamos el cociente entre el número de coincidencias y el de caracteres alineados: 
identity_percentage <- (nmatch(align) / nchar(align)) * 100
round(identity_percentage, 2)

#Para el procentaje de similitud de los aminoácidos alineados, en primer lugar, obtenemos la matriz BLOSUM62 con la información de la matriz de sustitución utilizada. A continuación, aplicamos la función Similarity: 
data("BLOSUM62")
Similarity(align,BLOSUM62)

#Para obtener el porcentaje de huecos utilizados, obtenemos, en primer lugar, el número de huecos como la diferencia entre el total de caracteres alineados y el conjunto del número de coincidencias y no coincidencias. 
number_gaps <- nchar(align) - (nmismatch(align) + nmatch(align))
gaps_percentage <- (number_gaps / nchar(align)) * 100
round(gaps_percentage, 2)

#Ejercicio 3. Estimar por el método de los momentos los valores de los parámetros λ y u de la distribución Gumbel, de la puntuación de los alineamientos si la hipótesis nula es cierta. Utilizar para ello una simulación de 10000 alineamientos

#Para estimar los parámetros λ y u de la distribución de Gumbel que tiene la puntuación de los alineamientos (S) cuando la hipótesis nula es cierta, vamos a similar 10000 veces el alineamiento entre cadenas que tienen la misma proporción nucleotídica pero distinto orden que las secuencias de partida. Para simplificar computacionalmente la simulación (dado el ya alto número de simulaciones), una de las secuencias (P36924) se va a permutar mientras que otra (P69328) se va a quedar fija. 

#Para hacer la permutación de la secuencia, es necesario convertirla en un vector de caracteres:
permutation_seq <- s2c(P36924) 

#La permutación se hace por medio de la función sample()
nsim <- 10000  
tt <- replicate(nsim,{
  seqRand <- toupper(c2s(sample(permutation_seq)))
  pairwiseAlignment(P69328,seqRand, 
                    substitutionMatrix="BLOSUM62",gapOpening=5,
                    gapExtension=5,scoreOnly=TRUE,type="local")
})

## Histograma de los valores simulados
hist(tt,freq=FALSE)

#A continuación, calculamos la media y la varianza de los valores simulados:
mean_sim <- mean(tt)
mean_sim

var_sim <- var(tt)
var_sim

#Como la varianza de la variable aleatoria de Gumbel es: var = 1.645/lambda^2; es posible despejar lambda como lambda = 1.285/desvest 


#Obtenemos los valores de los parámetros lambda y u: 
lambda_gumbel <- 1.2825/sqrt(var_sim)
lambda_gumbel
u_gumbel <- mean_sim-0.45*sqrt(var_sim)
u_gumbel
K_gumbel <- exp(lambda_gumbel*u_gumbel)/(nchar(P36924)*nchar(P69328))
K_gumbel


#Representamos junto al histograma la función de densidad de la distribución de Gumbel
dGumbel <- function(x,lambda=1,u=0){lambda*exp(-(lambda*(x-u)+exp(-lambda*(x-u))))}
hist(tt,freq=FALSE)
curve(dGumbel(x,lambda=lambda_gumbel,u=u_gumbel),add=TRUE,col="blue")
