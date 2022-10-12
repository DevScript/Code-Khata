# " "
# ' '
# ''' '''
# For string

2+3

x <- 2+3

x-2

y <- 'Sahil'

log(1)
log10(1)
sqrt(4)

4^2

pi

a <- 'BaBaG'
b <- 4.56
c <- 4^2
d <- 'Sajan'
v = c(1,3,5,7,8)

empName = c("Sahil","Aammar","Akash","Hassan")

# Arithmetic Operators

# +
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v+t)

# -
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v-t)

# *
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v*t)

# /
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v/t)

# %%
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v%%t)

# %/%
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v%/%t)

# ^
v <- c( 2,5.5,6)
t <- c(8, 3, 4)
print(v^t)

# Relational Operators
# >
v <- c(2,5.5,6,9)
t <- c(8,2.5,14,9)
print(v>t)

# <
v <- c(2,5.5,6,9)
t <- c(8,2.5,14,9)
print(v < t)

# ==
v <- c(2,5.5,6,9)
t <- c(8,2.5,14,9)
print(v == t)

# <=
v <- c(2,5.5,6,9)
t <- c(8,2.5,14,9)
print(v<=t)

# >=
v <- c(2,5.5,6,9)
t <- c(8,2.5,14,9)
print(v>=t)

# !=
v <- c(2,5.5,6,9)
t <- c(8,2.5,14,9)
print(v!=t)

# Logical operator
# &
v <- c(3,1,TRUE,2+3i)
t <- c(4,1,FALSE,2+3i)
print(v&t)


# |
v <- c(3,0,TRUE,2+2i)
t <- c(4,0,FALSE,2+3i)
print(v|t)

# !
v <- c(3,0,TRUE,2+2i)
print(!v)

# &&
v <- c(3,0,TRUE,2+2i)
t <- c(1,3,TRUE,2+3i)
print(v&&t)

# ||
v <- c(0,0,TRUE,2+2i)
t <- c(0,3,TRUE,2+3i)
print(v||t)

# Assignment Operators
# <− or = or  <<−
v1 <- c(3,1,TRUE,2+3i)
v2 <<- c(3,1,TRUE,2+3i)
v3 = c(3,1,TRUE,2+3i)
print(v1)
print(v2)
print(v3)

# -> or  ->>
c(3,1,TRUE,2+3i) -> v1
c(3,1,TRUE,2+3i) ->> v2 
print(v1)
print(v2)

# Miscellaneous Operators
# :
v <- 2:8
print(v)

# %in%
v1 <- 8
v2 <- 12
t <- 1:10
print(v1 %in% t) 
print(v2 %in% t) 

# %*%
M = matrix( c(2,6,5,1,10,4), nrow = 2,ncol = 3,byrow = TRUE)
t = M %*% t(M)
print(t)